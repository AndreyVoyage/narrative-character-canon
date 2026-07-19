#!/usr/bin/env python3
"""NCC Cline reference-import script — copy owner-selected external visual references
into an existing character namespace from a SHA-256-verified JSON task spec.

Standard library only. Dry-run by default; writes require --apply.
Never edits image pixels, never touches metadata files, never stages/commits/pushes,
never touches SQLite.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

VERSION = "1.0.0"

SCHEMA_VERSION = "1.0"

TOP_LEVEL_FIELDS = {
    "schema_version",
    "task_id",
    "character_id",
    "expected_head",
    "source_files",
    "authorized_metadata_files",
    "regenerate_inventory",
    "run_validator",
    "stop_uncommitted",
}

SOURCE_FILE_FIELDS = {
    "path",
    "sha256",
    "target_relative_path",
    "role",
    "secondary_roles",
    "classification_status",
    "notes",
}

CHARACTER_ID_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")

PROTECTED_UNTRACKED = {".claude/", ".vscode/", "UNIFIED_CANON_TESTS_TEMPLATE.md", "repo_audit.txt"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def eprint(*args, **kwargs):
    """Print to stderr."""
    kwargs.setdefault("file", sys.stderr)
    print(*args, **kwargs)


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, encoding="utf-8", errors="replace")


def sha256_path(path: Path) -> str:
    """Return SHA-256 hex digest of a file's contents, streamed to avoid loading large files whole."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_head(cwd: Path) -> str:
    return run(["git", "rev-parse", "HEAD"], cwd).stdout.strip()


def git_status_short(cwd: Path) -> str:
    return run(["git", "status", "--short"], cwd).stdout


def git_diff_cached(cwd: Path) -> str:
    return run(["git", "diff", "--cached", "--name-status"], cwd).stdout


# ---------------------------------------------------------------------------
# Git preflight
# ---------------------------------------------------------------------------


def preflight(repo_root: Path, expected_head: str) -> str:
    """Run Git safety gates required before any write. Returns current HEAD. Exits 4 on failure."""
    errors: list[str] = []

    if not (repo_root / ".git").is_dir():
        errors.append("PREFLIGHT-001: Not a Git repository")

    branch = run(["git", "branch", "--show-current"], repo_root).stdout.strip()
    if branch != "main":
        errors.append(f"PREFLIGHT-002: Expected branch 'main', got '{branch}'")

    head = git_head(repo_root)
    if head != expected_head:
        errors.append(
            f"PREFLIGHT-003: HEAD ({head[:8]}) != task spec expected_head ({expected_head[:8]})"
        )

    origin_result = run(["git", "rev-parse", "origin/main"], repo_root)
    if origin_result.returncode == 0:
        origin_main = origin_result.stdout.strip()
        if head != origin_main:
            errors.append(f"PREFLIGHT-004: HEAD ({head[:8]}) != origin/main ({origin_main[:8]})")

    status = git_status_short(repo_root)
    tracked_changes = [line for line in status.splitlines() if line.strip() and not line.startswith("??")]
    if tracked_changes:
        errors.append(f"PREFLIGHT-005: Tracked changes detected:\n{chr(10).join(tracked_changes)}")

    staged = git_diff_cached(repo_root)
    if staged.strip():
        errors.append(f"PREFLIGHT-006: Staged changes detected:\n{staged}")

    untracked_lines = [line[3:].strip() for line in status.splitlines() if line.startswith("??")]
    unexpected = set(untracked_lines) - PROTECTED_UNTRACKED
    if unexpected:
        errors.append(f"PREFLIGHT-007: Unexpected untracked paths: {sorted(unexpected)}")

    if errors:
        for e in errors:
            eprint(e)
        sys.exit(4)

    return head


def recheck_preflight(repo_root: Path, expected_head: str) -> list[str]:
    """Recheck immediately before mutation. Returns list of error messages (empty = OK)."""
    errors = []
    current_head = git_head(repo_root)
    if current_head != expected_head:
        errors.append(f"CONCURRENCY: HEAD changed from {expected_head[:8]} to {current_head[:8]}")
    staged = git_diff_cached(repo_root)
    if staged.strip():
        errors.append("CONCURRENCY: staged changes appeared since preflight")
    return errors


# ---------------------------------------------------------------------------
# Task-spec loading and validation
# ---------------------------------------------------------------------------


class SourceAction:
    def __init__(self, entry: dict, action: str, source_path: Path, target_path: Path, target_rel: Path):
        self.entry = entry
        self.action = action  # "COPY" or "REUSE_BY_HASH"
        self.source_path = source_path
        self.target_path = target_path
        self.target_rel = target_rel


def load_and_validate_spec(spec_path: Path, repo_root: Path) -> tuple[dict, list[SourceAction]]:
    """Load task spec JSON, validate the full contract, and classify every source file
    as COPY or REUSE_BY_HASH. Exits 2 on any contract violation."""
    try:
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        eprint(f"SPEC-001: Cannot parse task spec JSON: {exc}")
        sys.exit(2)

    if not isinstance(spec, dict):
        eprint("SPEC-002: Task spec must be a JSON object")
        sys.exit(2)

    unknown = set(spec) - TOP_LEVEL_FIELDS
    if unknown:
        eprint(f"SPEC-003: Unknown top-level fields: {sorted(unknown)}")
        sys.exit(2)

    missing = TOP_LEVEL_FIELDS - set(spec)
    if missing:
        eprint(f"SPEC-004: Missing required fields: {sorted(missing)}")
        sys.exit(2)

    if spec.get("schema_version") != SCHEMA_VERSION:
        eprint(f"SPEC-005: schema_version must be '{SCHEMA_VERSION}', got {spec.get('schema_version')!r}")
        sys.exit(2)

    for field in ("task_id", "character_id", "expected_head"):
        val = spec.get(field)
        if not isinstance(val, str) or not val.strip():
            eprint(f"SPEC-006: '{field}' is blank or missing")
            sys.exit(2)

    cid = spec["character_id"]
    if not CHARACTER_ID_RE.match(cid):
        eprint(f"SPEC-007: character_id '{cid}' must match ^[A-Z][A-Z0-9_]*$")
        sys.exit(2)

    char_root = repo_root / "AI_CHARACTERS" / cid
    if not char_root.is_dir():
        eprint(f"SPEC-008: character_id '{cid}' has no existing AI_CHARACTERS/{cid}/ folder")
        sys.exit(2)

    if not isinstance(spec.get("authorized_metadata_files"), list):
        eprint("SPEC-009: 'authorized_metadata_files' must be a list")
        sys.exit(2)
    if len(spec["authorized_metadata_files"]) != 0:
        eprint(
            "SPEC-010: 'authorized_metadata_files' must be empty in this MVP; "
            "metadata closeout is a separate phase"
        )
        sys.exit(2)

    for field in ("regenerate_inventory", "run_validator", "stop_uncommitted"):
        if not isinstance(spec.get(field), bool):
            eprint(f"SPEC-011: '{field}' must be a boolean")
            sys.exit(2)

    if spec["stop_uncommitted"] is not True:
        eprint("SPEC-012: 'stop_uncommitted' must be true")
        sys.exit(2)

    source_files = spec.get("source_files")
    if not isinstance(source_files, list) or len(source_files) == 0:
        eprint("SPEC-013: 'source_files' must be a non-empty list")
        sys.exit(2)

    actions: list[SourceAction] = []
    seen_targets: dict[str, int] = {}
    char_root_resolved = char_root.resolve()

    for i, entry in enumerate(source_files):
        if not isinstance(entry, dict):
            eprint(f"SPEC-014: source_files[{i}] must be an object")
            sys.exit(2)

        unknown_e = set(entry) - SOURCE_FILE_FIELDS
        if unknown_e:
            eprint(f"SPEC-015: source_files[{i}] has unknown fields: {sorted(unknown_e)}")
            sys.exit(2)
        missing_e = SOURCE_FILE_FIELDS - set(entry)
        if missing_e:
            eprint(f"SPEC-016: source_files[{i}] missing fields: {sorted(missing_e)}")
            sys.exit(2)

        for field in ("path", "sha256", "target_relative_path", "role", "classification_status"):
            val = entry.get(field)
            if not isinstance(val, str) or not val.strip():
                eprint(f"SPEC-017: source_files[{i}].{field} is blank or missing")
                sys.exit(2)

        secondary_roles = entry.get("secondary_roles")
        if not isinstance(secondary_roles, list) or not all(
            isinstance(r, str) and r.strip() for r in secondary_roles
        ):
            eprint(f"SPEC-018: source_files[{i}].secondary_roles must be a list of non-blank strings")
            sys.exit(2)

        if not isinstance(entry.get("notes"), str):
            eprint(f"SPEC-019: source_files[{i}].notes must be a string")
            sys.exit(2)

        sha = entry["sha256"]
        if not SHA256_RE.match(sha):
            eprint(f"SPEC-020: source_files[{i}].sha256 is not a valid 64-hex-char SHA-256: {sha!r}")
            sys.exit(2)
        sha = sha.lower()

        source_path = Path(entry["path"])
        if not source_path.is_absolute():
            eprint(f"SPEC-021: source_files[{i}].path must be an absolute path: {entry['path']!r}")
            sys.exit(2)
        if not source_path.is_file():
            eprint(f"SPEC-022: source_files[{i}].path does not exist or is not a file: {source_path}")
            sys.exit(2)

        actual_hash = sha256_path(source_path)
        if actual_hash != sha:
            eprint(
                f"SPEC-023: source_files[{i}] SHA-256 mismatch for {source_path}: "
                f"expected {sha}, got {actual_hash}"
            )
            sys.exit(2)

        target_rel_raw = entry["target_relative_path"]
        target_rel_path = Path(target_rel_raw)
        if target_rel_path.is_absolute():
            eprint(
                f"SPEC-024: source_files[{i}].target_relative_path must not be absolute: {target_rel_raw!r}"
            )
            sys.exit(2)
        if ".." in target_rel_path.parts:
            eprint(
                f"SPEC-025: source_files[{i}].target_relative_path must not contain '..': {target_rel_raw!r}"
            )
            sys.exit(2)

        target_path = (char_root / target_rel_path).resolve()
        if target_path != char_root_resolved and char_root_resolved not in target_path.parents:
            eprint(
                f"SPEC-026: source_files[{i}] target resolves outside AI_CHARACTERS/{cid}/: {target_path}"
            )
            sys.exit(2)

        dedup_key = str(target_path).lower()
        if dedup_key in seen_targets:
            eprint(
                f"SPEC-027: source_files[{i}] duplicate target_relative_path "
                f"(also used by source_files[{seen_targets[dedup_key]}]): {target_rel_raw}"
            )
            sys.exit(2)
        seen_targets[dedup_key] = i

        if target_path.exists():
            existing_hash = sha256_path(target_path)
            if existing_hash == sha:
                action = "REUSE_BY_HASH"
            else:
                eprint(
                    f"SPEC-028: source_files[{i}] target already exists with different content: "
                    f"{target_path} (existing sha256={existing_hash}, requested sha256={sha})"
                )
                sys.exit(2)
        else:
            action = "COPY"

        actions.append(SourceAction(entry, action, source_path, target_path, target_rel_path))

    return spec, actions


# ---------------------------------------------------------------------------
# Dry-run output
# ---------------------------------------------------------------------------


def print_dry_run(spec: dict, actions: list[SourceAction], repo_root: Path) -> None:
    print(f"Task ID: {spec['task_id']}")
    print(f"Character ID: {spec['character_id']}")
    print()
    print("Planned actions:")
    for a in actions:
        rel_target = a.target_path.relative_to(repo_root)
        print(f"  {a.action}: {a.source_path} -> {rel_target}")
    print()
    copied = sum(1 for a in actions if a.action == "COPY")
    reused = sum(1 for a in actions if a.action == "REUSE_BY_HASH")
    print(f"Would copy: {copied}")
    print(f"Would reuse by hash: {reused}")
    print(f"Inventory regeneration requested: {spec['regenerate_inventory']}")
    print(f"Validator run requested: {spec['run_validator']}")
    print()
    print("No files written.")
    print("REPOSITORY_MODIFIED=NO")


# ---------------------------------------------------------------------------
# Apply with rollback
# ---------------------------------------------------------------------------


def apply_import(
    repo_root: Path, spec: dict, actions: list[SourceAction], expected_head: str
) -> list[Path]:
    """Execute the import with atomicity. On any failure, roll back newly copied files
    (and INVENTORY.md if it was regenerated) and re-raise."""
    cid = spec["character_id"]
    copied_paths: list[Path] = []
    inventory_path = repo_root / "INVENTORY.md"
    inventory_backup = inventory_path.read_bytes() if inventory_path.exists() else None

    try:
        errors = recheck_preflight(repo_root, expected_head)
        if errors:
            for e in errors:
                eprint(e)
            raise RuntimeError("Pre-mutation recheck failed")

        for a in actions:
            if a.action != "COPY":
                continue
            a.target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(str(a.source_path), str(a.target_path))
            dest_hash = sha256_path(a.target_path)
            if dest_hash != a.entry["sha256"].lower():
                raise RuntimeError(
                    f"Destination hash mismatch after copy: {a.target_path} "
                    f"(expected {a.entry['sha256'].lower()}, got {dest_hash})"
                )
            copied_paths.append(a.target_path)

        if spec["regenerate_inventory"]:
            print("Running generate_inventory.py...")
            result = run([sys.executable, str(repo_root / "tools" / "generate_inventory.py")], repo_root)
            if result.returncode != 0:
                eprint(result.stderr)
                raise RuntimeError("Inventory generation failed")

        if spec["run_validator"]:
            print("Running validate_visual_canon_pipeline.py...")
            result = run(
                [
                    sys.executable,
                    str(repo_root / "tools" / "validate_visual_canon_pipeline.py"),
                    "--mode",
                    "compatibility",
                    "--character",
                    cid,
                    "--no-color",
                ],
                repo_root,
            )
            if result.returncode != 0:
                eprint(result.stdout[-2000:])
                eprint(result.stderr[-2000:])
                raise RuntimeError("Validator failed")

        result = run(["git", "diff", "--check"], repo_root)
        if result.returncode != 0:
            eprint(result.stdout)
            eprint(result.stderr)
            raise RuntimeError("git diff --check failed")

        staged = git_diff_cached(repo_root)
        if staged.strip():
            raise RuntimeError("Unexpected staged changes detected after apply")

    except Exception:
        eprint("ROLLBACK initiated...")
        for p in copied_paths:
            if p.exists():
                p.unlink()
        if spec["regenerate_inventory"] and inventory_backup is not None:
            inventory_path.write_bytes(inventory_backup)
        raise

    return copied_paths


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="NCC Cline reference-import: copy owner-selected external visual "
        "references into a character namespace from a JSON task spec.",
    )
    parser.add_argument("--task-spec", type=str, default=None, help="Path to reference-import task spec JSON")
    parser.add_argument("--apply", action="store_true", help="Actually copy files (default is dry-run)")
    parser.add_argument("--repo-root", type=str, default=None, help="Repository root path")
    parser.add_argument("--version", action="store_true", help="Print version and exit")
    args = parser.parse_args()

    if args.version:
        print(f"import_references.py {VERSION}")
        return 0

    if not args.task_spec:
        parser.error("--task-spec is required (unless --version)")

    if args.repo_root:
        repo_root = Path(args.repo_root).resolve()
    else:
        # scripts/ -> ncc-reference-import/ -> skills/ -> .cline/ -> repo root
        repo_root = Path(__file__).resolve().parents[4]

    if not repo_root.is_dir():
        eprint(f"CLI-001: Repository root does not exist: {repo_root}")
        return 2

    spec_path = Path(args.task_spec).resolve()
    if not spec_path.is_file():
        eprint(f"CLI-002: Task spec file does not exist: {spec_path}")
        return 2

    spec, actions = load_and_validate_spec(spec_path, repo_root)

    expected_head = spec["expected_head"]
    preflight(repo_root, expected_head)

    if not args.apply:
        print_dry_run(spec, actions, repo_root)
        return 0

    try:
        apply_import(repo_root, spec, actions, expected_head)
    except Exception as exc:
        eprint(f"Import failed: {exc}")
        return 3

    copied = sum(1 for a in actions if a.action == "COPY")
    reused = sum(1 for a in actions if a.action == "REUSE_BY_HASH")

    print("=== NCC REFERENCE IMPORT RESULT ===")
    print(f"TASK_ID={spec['task_id']}")
    print(f"CHARACTER_ID={spec['character_id']}")
    print(f"COPIED={copied}")
    print(f"REUSED_BY_HASH={reused}")
    print("SOURCE_FILES_MODIFIED=NO")
    print("IMAGE_PIXELS_EDITED=NO")
    print("METADATA_CHANGED=NO")
    print(f"INVENTORY_CHANGED={'YES' if spec['regenerate_inventory'] else 'NO'}")
    print(f"VALIDATOR_ERRORS={'0' if spec['run_validator'] else 'NOT_RUN'}")
    print("STAGED=NO")
    print("COMMIT=NO")
    print("PUSH=NO")
    print("SQLITE_CHANGED=NO")
    print("VERDICT=REFERENCES_IMPORTED_UNCOMMITTED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
