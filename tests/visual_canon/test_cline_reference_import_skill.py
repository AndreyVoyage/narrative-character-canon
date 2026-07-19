#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unit tests for .cline/skills/ncc-reference-import/scripts/import_references.py
using temporary Git repositories.

Never modifies the real repository, AI_CHARACTERS/**, or SQLite.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL = REPO_ROOT / ".cline" / "skills" / "ncc-reference-import" / "scripts" / "import_references.py"


def run(cmd, cwd, env=None):
    return subprocess.run(
        cmd, cwd=str(cwd), capture_output=True, text=True, encoding="utf-8", errors="replace", env=env
    )


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def make_temp_repo(character_id: str = "TESTX"):
    """Create a disposable Git repository with a minimal existing character namespace."""
    tmp = tempfile.TemporaryDirectory()
    root = Path(tmp.name) / "repo"
    root.mkdir()
    run(["git", "init", "-b", "main"], root)
    run(["git", "config", "user.email", "test@test.com"], root)
    run(["git", "config", "user.name", "Test"], root)

    (root / "AI_CHARACTERS" / character_id / "01_refs_raw").mkdir(parents=True)
    (root / "AI_CHARACTERS" / character_id / "01_refs_raw" / ".gitkeep").write_text("", encoding="utf-8")
    (root / "tools").mkdir()
    (root / "tools" / "generate_inventory.py").write_text(
        "import sys; print('inventory ok'); sys.exit(0)\n", encoding="utf-8"
    )
    (root / "tools" / "validate_visual_canon_pipeline.py").write_text(
        "import sys; print('validator ok'); sys.exit(0)\n", encoding="utf-8"
    )

    run(["git", "add", "."], root)
    run(["git", "commit", "-m", "initial"], root)

    head = run(["git", "rev-parse", "HEAD"], root).stdout.strip()
    return tmp, root, head


def make_bare_origin_and_diverge(root: Path):
    """Add an 'origin' remote pointing at the current HEAD, then create one more local
    commit so local HEAD diverges from origin/main while still matching the caller's
    already-recorded expected_head."""
    bare_dir = tempfile.mkdtemp()
    run(["git", "init", "--bare", "-b", "main", bare_dir], root)
    run(["git", "remote", "add", "origin", bare_dir], root)
    run(["git", "push", "origin", "main"], root)

    extra = root / "EXTRA_FILE.txt"
    extra.write_text("extra\n", encoding="utf-8")
    run(["git", "add", "EXTRA_FILE.txt"], root)
    run(["git", "commit", "-m", "diverge from origin"], root)
    return run(["git", "rev-parse", "HEAD"], root).stdout.strip()


def write_source_file(dir_path: Path, name: str, content: bytes) -> tuple[Path, str]:
    dir_path.mkdir(parents=True, exist_ok=True)
    p = dir_path / name
    p.write_bytes(content)
    return p, sha256_bytes(content)


def base_spec(head: str, character_id: str, source_files: list, **overrides) -> dict:
    spec = {
        "schema_version": "1.0",
        "task_id": "NCC-TESTX-REFERENCE-IMPORT-TEST",
        "character_id": character_id,
        "expected_head": head,
        "source_files": source_files,
        "authorized_metadata_files": [],
        "regenerate_inventory": False,
        "run_validator": True,
        "stop_uncommitted": True,
    }
    spec.update(overrides)
    return spec


def source_entry(path: Path, sha256: str, target_relative_path: str, **overrides) -> dict:
    entry = {
        "path": str(path),
        "sha256": sha256,
        "target_relative_path": target_relative_path,
        "role": "SUPPORT",
        "secondary_roles": [],
        "classification_status": "owner_selected_unclassified",
        "notes": "",
    }
    entry.update(overrides)
    return entry


def write_spec(spec: dict) -> Path:
    spec_path = Path(tempfile.mkdtemp()) / "task_spec.json"
    spec_path.write_text(json.dumps(spec), encoding="utf-8")
    return spec_path


def invoke(repo_root: Path, spec_path: Path, *extra):
    cmd = [sys.executable, str(TOOL), "--repo-root", str(repo_root), "--task-spec", str(spec_path)] + list(extra)
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    return run(cmd, repo_root, env=env)


class TestCLIBasics(unittest.TestCase):
    def test_version(self):
        result = subprocess.run([sys.executable, str(TOOL), "--version"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("import_references.py", result.stdout)

    def test_help(self):
        result = subprocess.run([sys.executable, str(TOOL), "--help"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("--task-spec", result.stdout)

    def test_missing_task_spec_arg(self):
        result = subprocess.run([sys.executable, str(TOOL)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)


class TestDryRun(unittest.TestCase):
    def test_dry_run_makes_no_writes(self):
        tmp, root, head = make_temp_repo()
        try:
            src_dir = Path(tempfile.mkdtemp())
            src_path, sha = write_source_file(src_dir, "ref01.jpg", b"hello world")
            spec = base_spec(
                head, "TESTX", [source_entry(src_path, sha, "01_refs_raw/TESTX_RAW_01.jpg")]
            )
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("REPOSITORY_MODIFIED=NO", result.stdout)
            self.assertIn("COPY:", result.stdout)

            target = root / "AI_CHARACTERS" / "TESTX" / "01_refs_raw" / "TESTX_RAW_01.jpg"
            self.assertFalse(target.exists())
            status = run(["git", "status", "--short"], root).stdout
            self.assertEqual(status.strip(), "")
        finally:
            tmp.cleanup()


class TestApply(unittest.TestCase):
    def test_successful_apply_copies_and_reuses(self):
        tmp, root, head = make_temp_repo()
        try:
            src_dir = Path(tempfile.mkdtemp())
            src1, sha1 = write_source_file(src_dir, "ref01.jpg", b"content one")
            src2, sha2 = write_source_file(src_dir, "ref02.jpg", b"content two")

            # Pre-place a target identical to src2, so it should be reused, not copied.
            # Commit it so the git-safety gate sees a clean tree (a real reuse-by-hash
            # target would already be tracked from a prior import).
            existing_target = root / "AI_CHARACTERS" / "TESTX" / "01_refs_raw" / "TESTX_RAW_02.jpg"
            existing_target.write_bytes(b"content two")
            run(["git", "add", "AI_CHARACTERS/TESTX/01_refs_raw/TESTX_RAW_02.jpg"], root)
            run(["git", "commit", "-m", "pre-existing reuse target"], root)
            head = run(["git", "rev-parse", "HEAD"], root).stdout.strip()

            spec = base_spec(
                head,
                "TESTX",
                [
                    source_entry(src1, sha1, "01_refs_raw/TESTX_RAW_01.jpg"),
                    source_entry(src2, sha2, "01_refs_raw/TESTX_RAW_02.jpg"),
                ],
            )
            spec_path = write_spec(spec)

            result = invoke(root, spec_path, "--apply")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("COPIED=1", result.stdout)
            self.assertIn("REUSED_BY_HASH=1", result.stdout)
            self.assertIn("VERDICT=REFERENCES_IMPORTED_UNCOMMITTED", result.stdout)

            target1 = root / "AI_CHARACTERS" / "TESTX" / "01_refs_raw" / "TESTX_RAW_01.jpg"
            self.assertTrue(target1.exists())
            self.assertEqual(target1.read_bytes(), b"content one")
        finally:
            tmp.cleanup()

    def test_no_staging_commit_push_sqlite(self):
        tmp, root, head = make_temp_repo()
        try:
            src_dir = Path(tempfile.mkdtemp())
            src1, sha1 = write_source_file(src_dir, "ref01.jpg", b"content one")
            spec = base_spec(head, "TESTX", [source_entry(src1, sha1, "01_refs_raw/TESTX_RAW_01.jpg")])
            spec_path = write_spec(spec)

            result = invoke(root, spec_path, "--apply")
            self.assertEqual(result.returncode, 0, result.stderr)

            head_after = run(["git", "rev-parse", "HEAD"], root).stdout.strip()
            self.assertEqual(head, head_after)

            staged = run(["git", "diff", "--cached", "--name-status"], root).stdout
            self.assertEqual(staged.strip(), "")

            status = run(["git", "status", "--short"], root).stdout
            self.assertIn("?? AI_CHARACTERS/TESTX/01_refs_raw/TESTX_RAW_01.jpg", status)

            sqlite_files = list(root.rglob("*.sqlite"))
            self.assertEqual(sqlite_files, [])
        finally:
            tmp.cleanup()


class TestValidationErrors(unittest.TestCase):
    def test_source_hash_mismatch(self):
        tmp, root, head = make_temp_repo()
        try:
            src_dir = Path(tempfile.mkdtemp())
            src, real_sha = write_source_file(src_dir, "ref01.jpg", b"actual content")
            wrong_sha = sha256_bytes(b"different content")
            spec = base_spec(head, "TESTX", [source_entry(src, wrong_sha, "01_refs_raw/TESTX_RAW_01.jpg")])
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 2)
            self.assertIn("SPEC-023", result.stderr)
        finally:
            tmp.cleanup()

    def test_missing_source(self):
        tmp, root, head = make_temp_repo()
        try:
            missing = Path(tempfile.mkdtemp()) / "does_not_exist.jpg"
            spec = base_spec(
                head, "TESTX", [source_entry(missing, "0" * 64, "01_refs_raw/TESTX_RAW_01.jpg")]
            )
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 2)
            self.assertIn("SPEC-022", result.stderr)
        finally:
            tmp.cleanup()

    def test_path_traversal_rejected(self):
        tmp, root, head = make_temp_repo()
        try:
            src_dir = Path(tempfile.mkdtemp())
            src, sha = write_source_file(src_dir, "ref01.jpg", b"content")
            spec = base_spec(head, "TESTX", [source_entry(src, sha, "../OTHER_CHAR/evil.jpg")])
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 2)
            self.assertIn("SPEC-025", result.stderr)
        finally:
            tmp.cleanup()

    def test_absolute_target_rejected(self):
        tmp, root, head = make_temp_repo()
        try:
            src_dir = Path(tempfile.mkdtemp())
            src, sha = write_source_file(src_dir, "ref01.jpg", b"content")
            windows_abs = str(root).split(":")[0] + ":\\Windows\\evil.jpg" if os.name == "nt" else "/etc/evil.jpg"
            spec = base_spec(head, "TESTX", [source_entry(src, sha, windows_abs)])
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 2)
            self.assertIn("SPEC-024", result.stderr)
        finally:
            tmp.cleanup()

    def test_differing_existing_target_rejected(self):
        tmp, root, head = make_temp_repo()
        try:
            src_dir = Path(tempfile.mkdtemp())
            src, sha = write_source_file(src_dir, "ref01.jpg", b"new content")

            existing_target = root / "AI_CHARACTERS" / "TESTX" / "01_refs_raw" / "TESTX_RAW_01.jpg"
            existing_target.write_bytes(b"old different content")

            spec = base_spec(head, "TESTX", [source_entry(src, sha, "01_refs_raw/TESTX_RAW_01.jpg")])
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 2)
            self.assertIn("SPEC-028", result.stderr)
        finally:
            tmp.cleanup()

    def test_duplicate_target_rejected(self):
        tmp, root, head = make_temp_repo()
        try:
            src_dir = Path(tempfile.mkdtemp())
            src1, sha1 = write_source_file(src_dir, "ref01.jpg", b"content one")
            src2, sha2 = write_source_file(src_dir, "ref02.jpg", b"content two")
            spec = base_spec(
                head,
                "TESTX",
                [
                    source_entry(src1, sha1, "01_refs_raw/TESTX_RAW_01.jpg"),
                    source_entry(src2, sha2, "01_refs_raw/TESTX_RAW_01.jpg"),
                ],
            )
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 2)
            self.assertIn("SPEC-027", result.stderr)
        finally:
            tmp.cleanup()

    def test_unknown_field_rejected(self):
        tmp, root, head = make_temp_repo()
        try:
            src_dir = Path(tempfile.mkdtemp())
            src, sha = write_source_file(src_dir, "ref01.jpg", b"content")
            spec = base_spec(head, "TESTX", [source_entry(src, sha, "01_refs_raw/TESTX_RAW_01.jpg")])
            spec["unexpected_field"] = "surprise"
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 2)
            self.assertIn("SPEC-003", result.stderr)
        finally:
            tmp.cleanup()

    def test_nonempty_authorized_metadata_rejected(self):
        tmp, root, head = make_temp_repo()
        try:
            src_dir = Path(tempfile.mkdtemp())
            src, sha = write_source_file(src_dir, "ref01.jpg", b"content")
            spec = base_spec(
                head,
                "TESTX",
                [source_entry(src, sha, "01_refs_raw/TESTX_RAW_01.jpg")],
                authorized_metadata_files=["AI_CHARACTERS/TESTX/10_notes/TESTX_CANON_INDEX.md"],
            )
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 2)
            self.assertIn("SPEC-010", result.stderr)
        finally:
            tmp.cleanup()

    def test_stop_uncommitted_false_rejected(self):
        tmp, root, head = make_temp_repo()
        try:
            src_dir = Path(tempfile.mkdtemp())
            src, sha = write_source_file(src_dir, "ref01.jpg", b"content")
            spec = base_spec(
                head, "TESTX", [source_entry(src, sha, "01_refs_raw/TESTX_RAW_01.jpg")], stop_uncommitted=False
            )
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 2)
            self.assertIn("SPEC-012", result.stderr)
        finally:
            tmp.cleanup()

    def test_unknown_character_rejected(self):
        tmp, root, head = make_temp_repo()
        try:
            src_dir = Path(tempfile.mkdtemp())
            src, sha = write_source_file(src_dir, "ref01.jpg", b"content")
            spec = base_spec(head, "DOES_NOT_EXIST", [source_entry(src, sha, "01_refs_raw/RAW_01.jpg")])
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 2)
            self.assertIn("SPEC-008", result.stderr)
        finally:
            tmp.cleanup()


class TestGitGates(unittest.TestCase):
    def test_dirty_tree_rejected(self):
        tmp, root, head = make_temp_repo()
        try:
            (root / "tools" / "generate_inventory.py").write_text("print('modified')\n", encoding="utf-8")

            src_dir = Path(tempfile.mkdtemp())
            src, sha = write_source_file(src_dir, "ref01.jpg", b"content")
            spec = base_spec(head, "TESTX", [source_entry(src, sha, "01_refs_raw/TESTX_RAW_01.jpg")])
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 4)
            self.assertIn("PREFLIGHT-005", result.stderr)
        finally:
            tmp.cleanup()

    def test_staged_state_rejected(self):
        tmp, root, head = make_temp_repo()
        try:
            (root / "NEW_FILE.txt").write_text("new\n", encoding="utf-8")
            run(["git", "add", "NEW_FILE.txt"], root)

            src_dir = Path(tempfile.mkdtemp())
            src, sha = write_source_file(src_dir, "ref01.jpg", b"content")
            spec = base_spec(head, "TESTX", [source_entry(src, sha, "01_refs_raw/TESTX_RAW_01.jpg")])
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 4)
            self.assertIn("PREFLIGHT-006", result.stderr)
        finally:
            tmp.cleanup()

    def test_unexpected_untracked_rejected(self):
        tmp, root, head = make_temp_repo()
        try:
            (root / "RANDOM_UNTRACKED.txt").write_text("surprise\n", encoding="utf-8")

            src_dir = Path(tempfile.mkdtemp())
            src, sha = write_source_file(src_dir, "ref01.jpg", b"content")
            spec = base_spec(head, "TESTX", [source_entry(src, sha, "01_refs_raw/TESTX_RAW_01.jpg")])
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 4)
            self.assertIn("PREFLIGHT-007", result.stderr)
        finally:
            tmp.cleanup()

    def test_protected_untracked_allowed_and_preserved(self):
        tmp, root, head = make_temp_repo()
        try:
            (root / ".vscode").mkdir()
            (root / ".vscode" / "settings.json").write_text("{}\n", encoding="utf-8")
            (root / "repo_audit.txt").write_text("audit\n", encoding="utf-8")

            src_dir = Path(tempfile.mkdtemp())
            src, sha = write_source_file(src_dir, "ref01.jpg", b"content")
            spec = base_spec(head, "TESTX", [source_entry(src, sha, "01_refs_raw/TESTX_RAW_01.jpg")])
            spec_path = write_spec(spec)

            result = invoke(root, spec_path, "--apply")
            self.assertEqual(result.returncode, 0, result.stderr)

            self.assertEqual((root / ".vscode" / "settings.json").read_text(encoding="utf-8"), "{}\n")
            self.assertEqual((root / "repo_audit.txt").read_text(encoding="utf-8"), "audit\n")
        finally:
            tmp.cleanup()

    def test_expected_head_mismatch_rejected(self):
        tmp, root, head = make_temp_repo()
        try:
            src_dir = Path(tempfile.mkdtemp())
            src, sha = write_source_file(src_dir, "ref01.jpg", b"content")
            spec = base_spec(
                head, "TESTX", [source_entry(src, sha, "01_refs_raw/TESTX_RAW_01.jpg")], expected_head="0" * 40
            )
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 4)
            self.assertIn("PREFLIGHT-003", result.stderr)
        finally:
            tmp.cleanup()

    def test_origin_mismatch_rejected(self):
        tmp, root, head = make_temp_repo()
        try:
            diverged_head = make_bare_origin_and_diverge(root)

            src_dir = Path(tempfile.mkdtemp())
            src, sha = write_source_file(src_dir, "ref01.jpg", b"content")
            spec = base_spec(
                diverged_head, "TESTX", [source_entry(src, sha, "01_refs_raw/TESTX_RAW_01.jpg")]
            )
            spec_path = write_spec(spec)

            result = invoke(root, spec_path)
            self.assertEqual(result.returncode, 4)
            self.assertIn("PREFLIGHT-004", result.stderr)
        finally:
            tmp.cleanup()


class TestRollback(unittest.TestCase):
    def test_rollback_after_second_copy_failure(self):
        tmp, root, head = make_temp_repo()
        try:
            src_dir = Path(tempfile.mkdtemp())
            src1, sha1 = write_source_file(src_dir, "ref01.jpg", b"content one")
            src2, sha2 = write_source_file(src_dir, "ref02.jpg", b"content two")

            # Pre-create a *file* at the path the second entry needs as a directory,
            # so its mkdir(parents=True) fails only at copy time (after the first
            # entry has already been copied), not during upfront validation. Commit
            # it so the git-safety gate sees a clean tree.
            blocker = root / "AI_CHARACTERS" / "TESTX" / "01_refs_raw" / "blocker"
            blocker.write_bytes(b"i am a file, not a directory")
            run(["git", "add", "AI_CHARACTERS/TESTX/01_refs_raw/blocker"], root)
            run(["git", "commit", "-m", "pre-existing blocker file"], root)
            head = run(["git", "rev-parse", "HEAD"], root).stdout.strip()

            spec = base_spec(
                head,
                "TESTX",
                [
                    source_entry(src1, sha1, "01_refs_raw/TESTX_RAW_01.jpg"),
                    source_entry(src2, sha2, "01_refs_raw/blocker/TESTX_RAW_02.jpg"),
                ],
            )
            spec_path = write_spec(spec)

            result = invoke(root, spec_path, "--apply")
            self.assertEqual(result.returncode, 3)
            self.assertIn("ROLLBACK initiated", result.stderr)

            target1 = root / "AI_CHARACTERS" / "TESTX" / "01_refs_raw" / "TESTX_RAW_01.jpg"
            self.assertFalse(target1.exists(), "first copied file must be rolled back")

            status = run(["git", "status", "--short"], root).stdout
            leftover = [
                line
                for line in status.splitlines()
                if "TESTX_RAW_01.jpg" in line or "TESTX_RAW_02.jpg" in line
            ]
            self.assertEqual(leftover, [])
        finally:
            tmp.cleanup()


if __name__ == "__main__":
    unittest.main()
