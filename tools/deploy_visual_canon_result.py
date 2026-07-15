#!/usr/bin/env python3
"""Dry-run-first deployment of one pre-registered visual-canon result."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Callable

__version__ = "1.0.1"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
HEX40 = re.compile(r"^[0-9a-fA-F]{40}$")
HEX64 = re.compile(r"^[0-9a-fA-F]{64}$")
CHARACTER = re.compile(r"^[A-Z][A-Z0-9_]*$")
PROMPT_ID = re.compile(r"^[A-Z][A-Z0-9_]*_V[0-9]+$")
SCENE_ID = re.compile(r"^[a-z][a-z0-9_]*$")
VERSION = re.compile(r"^V[0-9]+$")
VARIANT = re.compile(r"^[A-Z][A-Z0-9_]*$")
OPERATION_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{2,127}$")
DECISION_ID = re.compile(r"^D-[0-9]{3,}$")

TOP_REQUIRED = {
    "schema_version", "operation_id", "expected_git_head", "character_id", "prompt_id",
    "test_number", "scene_id", "version", "source_image_path", "source_image_sha256",
    "planned_output_path", "selected", "human_approval", "approval_evidence", "verdict",
    "role", "storage", "content_tier", "reference_paths", "prompt_linkage",
    "expected_file_hashes", "expected_absent_paths", "updates",
}
TOP_OPTIONAL = {"character_ids", "variant_label", "backend", "notes"}
SET_FIELDS = {
    "selected", "human_approval", "verdict", "role", "storage", "content_tier",
    "deployed", "output_path",
}
TERMINAL_BAD_VERDICTS = {
    "REJECTED", "SUPERSEDED", "REJECTED_BODY_CANON", "REJECTED_PROPORTION_DRIFT",
    "ACCEPTABLE_CANDIDATE_SUPERSEDED",
}
PRIVATE_PARTS = {"local", "local_only", "private", "private_local", "adult_local", "quarantine", "archive"}


class DeployError(Exception):
    def __init__(self, status: int, code: str, message: str):
        super().__init__(message)
        self.status, self.code, self.message = status, code, message


def fail(status: int, code: str, message: str) -> None:
    raise DeployError(status, code, message)


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1048576), b""):
            h.update(chunk)
    return h.hexdigest()


def command(args: list[str], root: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    process = subprocess.run(
        args, cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    if check and process.returncode:
        fail(3, "DEPLOY-GIT-001", f"{' '.join(args)} failed: {process.stderr.strip()}")
    return process


def repository(explicit: str | None) -> Path:
    if explicit:
        root = Path(explicit).resolve()
    else:
        process = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        if process.returncode:
            fail(3, "DEPLOY-GIT-002", "not inside a Git worktree")
        root = Path(process.stdout.strip()).resolve()
    if not (root / ".git").exists():
        fail(3, "DEPLOY-GIT-002", "invalid Git worktree")
    return root


def relative(value: str, *, allow_voyage: bool = False) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(2, "DEPLOY-REQ-001", "empty repository path")
    value = value.replace("\\", "/")
    path = PurePosixPath(value)
    if path.is_absolute() or re.match(r"^[A-Za-z]:", value) or ".." in path.parts:
        fail(3, "DEPLOY-GIT-003", f"unsafe path: {value}")
    lowered = {part.casefold() for part in path.parts}
    forbidden = {".git", "local_storage"}
    if not allow_voyage:
        forbidden.add(".voyage")
    if lowered & forbidden:
        fail(3, "DEPLOY-GIT-003", f"protected path: {value}")
    return path.as_posix()


def target(root: Path, value: str, *, allow_voyage: bool = False) -> tuple[str, Path]:
    rel = relative(value, allow_voyage=allow_voyage)
    lexical = root.joinpath(*PurePosixPath(rel).parts)
    probe = root
    for part in PurePosixPath(rel).parts:
        probe = probe / part
        if probe.exists() and probe.is_symlink():
            fail(3, "DEPLOY-GIT-005", f"symlink path: {rel}")
    resolved = lexical.resolve(strict=False)
    try:
        resolved.relative_to(root.resolve())
    except ValueError:
        fail(3, "DEPLOY-GIT-003", f"path escapes repository: {rel}")
    return rel, resolved


def path_key(path: Path) -> str:
    return str(path.resolve(strict=False)).casefold()


def tracked(root: Path, rel: str) -> None:
    if command(["git", "ls-files", "--error-unmatch", "--", rel], root, False).returncode:
        fail(3, "DEPLOY-GIT-011", f"untracked required file: {rel}")


def json_load_text(text: str, code: str) -> Any:
    duplicates: list[str] = []

    def hook(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                duplicates.append(key)
            result[key] = value
        return result

    try:
        result = json.loads(text, object_pairs_hook=hook)
    except json.JSONDecodeError as error:
        fail(2, code, f"invalid JSON: {error}")
    if duplicates:
        fail(2, "DEPLOY-REQ-002", f"duplicate keys: {sorted(set(duplicates))}")
    return result


def json_object(path: Path, code: str = "DEPLOY-CLI-003") -> dict[str, Any]:
    try:
        text = path.read_bytes().decode("utf-8")
    except (OSError, UnicodeError) as error:
        fail(2, code, f"invalid JSON {path}: {error}")
    result = json_load_text(text, code)
    if not isinstance(result, dict):
        fail(2, "DEPLOY-REQ-003", "JSON root must be an object")
    return result


def exact_object(value: Any, required: set[str], optional: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(2, "DEPLOY-REQ-020", f"{label} must be an object")
    missing = required - set(value)
    unknown = set(value) - required - optional
    if missing or unknown:
        fail(2, "DEPLOY-REQ-021", f"invalid {label} fields; missing={sorted(missing)} unknown={sorted(unknown)}")
    return value


def string_value(value: Any, label: str, pattern: re.Pattern[str] | None = None) -> str:
    if not isinstance(value, str) or not value:
        fail(2, "DEPLOY-REQ-022", f"{label} must be a non-empty string")
    if pattern and not pattern.fullmatch(value):
        fail(2, "DEPLOY-REQ-022", f"invalid {label}: {value}")
    return value


def string_array(value: Any, label: str, *, normalized_paths: bool = False) -> list[str]:
    if not isinstance(value, list) or not value:
        fail(2, "DEPLOY-REQ-023", f"{label} must be a non-empty array")
    result = [string_value(item, f"{label} item") for item in value]
    keys = [relative(item).casefold() if normalized_paths else item for item in result]
    if len(keys) != len(set(keys)):
        fail(2, "DEPLOY-REQ-024", f"{label} contains duplicates")
    return result


def validate_markdown_update(value: Any, label: str) -> dict[str, Any]:
    update = exact_object(value, {"path", "unique_anchor", "entry_markdown"}, set(), label)
    string_value(update["path"], f"{label}.path")
    string_value(update["unique_anchor"], f"{label}.unique_anchor")
    string_value(update["entry_markdown"], f"{label}.entry_markdown")
    return update


def validate_evidence_shape(evidence: Any, prompt_id: str) -> None:
    if not isinstance(evidence, list) or not evidence:
        fail(1, "DEPLOY-REQ-007", "approval evidence required")
    identities: set[str] = set()
    for item in evidence:
        if not isinstance(item, dict) or "kind" not in item:
            fail(2, "DEPLOY-REQ-025", "invalid approval evidence item")
        kind = item.get("kind")
        common = {"kind", "assertion", "required_text"}
        if kind == "repo_path":
            required = common | {"path", "sha256"}
        elif kind == "voyage_decision":
            required = common | {"path", "decision_id", "sha256"}
        elif kind == "commit":
            required = common | {"commit_hash", "path"}
        else:
            fail(2, "DEPLOY-REQ-025", f"unsupported evidence kind: {kind}")
        exact_object(item, required, set(), f"{kind} evidence")
        if item["assertion"] != "human_selected_and_approved":
            fail(1, "DEPLOY-REQ-007", "approval assertion is not explicit")
        markers = string_array(item["required_text"], "approval required_text")
        if prompt_id not in markers:
            fail(1, "DEPLOY-REQ-007", "approval evidence must include exact prompt_id marker")
        if kind in {"repo_path", "voyage_decision"}:
            string_value(item["sha256"], "approval sha256", HEX64)
        if kind == "voyage_decision":
            string_value(item["decision_id"], "decision_id", DECISION_ID)
            if relative(item["path"], allow_voyage=True).casefold() != ".voyage/decisions.md":
                fail(1, "DEPLOY-REQ-007", "voyage evidence path must be .voyage/DECISIONS.md")
        if kind == "commit":
            string_value(item["commit_hash"], "commit_hash", HEX40)
        identity = json.dumps(item, ensure_ascii=False, sort_keys=True)
        if identity in identities:
            fail(2, "DEPLOY-REQ-026", "duplicate approval evidence")
        identities.add(identity)


def validate_request(request: dict[str, Any]) -> None:
    request = exact_object(request, TOP_REQUIRED, TOP_OPTIONAL, "request")
    string_value(request["schema_version"], "schema_version")
    if request["schema_version"] != "1.0":
        fail(2, "DEPLOY-REQ-004", "unsupported schema_version")
    string_value(request["operation_id"], "operation_id", OPERATION_ID)
    string_value(request["expected_git_head"], "expected_git_head", HEX40)
    string_value(request["character_id"], "character_id", CHARACTER)
    string_value(request["prompt_id"], "prompt_id", PROMPT_ID)
    if isinstance(request["test_number"], bool) or not isinstance(request["test_number"], int) or request["test_number"] < 1:
        fail(2, "DEPLOY-REQ-027", "test_number must be a positive integer")
    string_value(request["scene_id"], "scene_id", SCENE_ID)
    string_value(request["version"], "version", VERSION)
    string_value(request["source_image_path"], "source_image_path")
    string_value(request["source_image_sha256"], "source_image_sha256", HEX64)
    string_value(request["planned_output_path"], "planned_output_path")
    fixed = {
        "selected": True, "human_approval": True, "storage": "repo_tracked",
        "content_tier": "public_filtered",
    }
    if any(request.get(key) is not value if isinstance(value, bool) else request.get(key) != value for key, value in fixed.items()):
        fail(1, "DEPLOY-REQ-005", "fixed deployment values violated")
    if request["verdict"] not in {"APPROVED_AS_TEST", "APPROVED_AS_CANON"}:
        fail(1, "DEPLOY-REQ-005", "invalid verdict")
    if request["role"] not in {"MAIN", "ALT"}:
        fail(1, "DEPLOY-REQ-005", "invalid role")
    references = string_array(request["reference_paths"], "reference_paths", normalized_paths=True)
    del references
    if "character_ids" in request:
        ids = string_array(request["character_ids"], "character_ids")
        for character_id in ids:
            string_value(character_id, "character_ids item", CHARACTER)
        if request["character_id"] not in ids:
            fail(2, "DEPLOY-REQ-028", "primary character_id missing from character_ids")
    if "variant_label" in request:
        string_value(request["variant_label"], "variant_label", VARIANT)
    if "backend" in request:
        string_value(request["backend"], "backend")
    if "notes" in request and not isinstance(request["notes"], str):
        fail(2, "DEPLOY-REQ-022", "notes must be a string")
    validate_evidence_shape(request["approval_evidence"], request["prompt_id"])

    linkage = exact_object(
        request["prompt_linkage"],
        {"prompt_index_path", "prompt_index_required_text", "prompt_source_path", "prompt_heading"},
        set(), "prompt_linkage",
    )
    for key in linkage:
        string_value(linkage[key], f"prompt_linkage.{key}")

    hashes = request["expected_file_hashes"]
    if not isinstance(hashes, dict) or not hashes:
        fail(2, "DEPLOY-REQ-029", "expected_file_hashes must be a non-empty object")
    normalized_hashes: set[str] = set()
    for raw, value in hashes.items():
        rel = relative(string_value(raw, "hash path"))
        string_value(value, f"hash for {rel}", HEX64)
        if rel.casefold() in normalized_hashes:
            fail(2, "DEPLOY-REQ-018", "duplicate normalized hash path")
        normalized_hashes.add(rel.casefold())
    string_array(request["expected_absent_paths"], "expected_absent_paths", normalized_paths=True)

    updates = exact_object(
        request["updates"], {"prompt_record", "test_results", "reference_presets", "canon_index"}, set(), "updates"
    )
    prompt_record = exact_object(updates["prompt_record"], {"registry_path", "set_fields"}, set(), "prompt_record")
    string_value(prompt_record["registry_path"], "registry_path")
    set_fields = exact_object(prompt_record["set_fields"], SET_FIELDS, set(), "set_fields")
    output = relative(request["planned_output_path"])
    expected_fields = {
        "selected": True, "human_approval": True, "verdict": request["verdict"],
        "role": request["role"], "storage": "repo_tracked", "content_tier": "public_filtered",
        "deployed": True, "output_path": output,
    }
    if set_fields != expected_fields:
        fail(1, "DEPLOY-REQ-013", "record update contradicts request")
    validate_markdown_update(updates["test_results"], "test_results")
    presets = exact_object(
        updates["reference_presets"], {"path", "container_path", "preset_id", "preset_value"}, set(), "reference_presets"
    )
    string_value(presets["path"], "reference_presets.path")
    string_array(presets["container_path"], "reference_presets.container_path")
    string_value(presets["preset_id"], "reference_presets.preset_id")
    if not isinstance(presets["preset_value"], dict):
        fail(2, "DEPLOY-REQ-020", "preset_value must be an object")
    canon = updates["canon_index"]
    if request["verdict"] == "APPROVED_AS_TEST":
        if canon is not None:
            fail(1, "DEPLOY-REQ-014", "Canon Index must be null for APPROVED_AS_TEST")
    else:
        if canon is None:
            fail(1, "DEPLOY-REQ-014", "Canon Index update required for APPROVED_AS_CANON")
        validate_markdown_update(canon, "canon_index")


@dataclass(frozen=True)
class Contract:
    character_root_rel: str
    character_root: Path
    registry: tuple[str, Path]
    test_results: tuple[str, Path]
    presets: tuple[str, Path]
    canon_index: tuple[str, Path] | None
    prompt_index: tuple[str, Path]
    prompt_source: tuple[str, Path]
    destination: tuple[str, Path]
    references: tuple[tuple[str, Path], ...]

    @property
    def mutations(self) -> tuple[tuple[str, Path], ...]:
        values = [self.destination, self.registry, self.test_results, self.presets]
        if self.canon_index:
            values.append(self.canon_index)
        return tuple(values)

    @property
    def hashed(self) -> tuple[tuple[str, Path], ...]:
        values = [self.registry, self.test_results, self.presets, self.prompt_index, self.prompt_source]
        if self.canon_index:
            values.append(self.canon_index)
        return tuple(values)


def character_root(root: Path, character_id: str) -> tuple[str, Path]:
    base = root / "AI_CHARACTERS"
    candidates: list[Path] = []
    if base.is_dir():
        candidates.extend(path for path in base.iterdir() if path.is_dir() and not path.name.startswith("_") and path.name.casefold() == character_id.casefold())
        for container in base.iterdir():
            if not container.is_dir() or not container.name.startswith("_"):
                continue
            candidates.extend(path for path in container.iterdir() if path.is_dir() and path.name.casefold() == character_id.casefold())
    unique = {path_key(path): path for path in candidates}
    if len(unique) != 1:
        fail(3, "DEPLOY-GIT-020", f"character namespace must resolve exactly once: {character_id}")
    path = next(iter(unique.values()))
    if path.is_symlink():
        fail(3, "DEPLOY-GIT-005", "character root may not be a symlink")
    resolved = path.resolve()
    try:
        resolved.relative_to(base.resolve())
    except ValueError:
        fail(3, "DEPLOY-GIT-003", "character root escapes AI_CHARACTERS")
    return resolved.relative_to(root.resolve()).as_posix(), resolved


def require_exact(root: Path, raw: str, expected: str, label: str) -> tuple[str, Path]:
    rel, path = target(root, raw)
    expected_rel, expected_path = target(root, expected)
    if path_key(path) != path_key(expected_path) or rel.casefold() != expected_rel.casefold():
        fail(1, "DEPLOY-AUTH-001", f"{label} must be exactly {expected_rel}")
    return expected_rel, expected_path


def resolve_contract(root: Path, request: dict[str, Any]) -> Contract:
    char = request["character_id"]
    root_rel, char_root = character_root(root, char)
    prompts = f"{root_rel}/06_prompts"
    notes = f"{root_rel}/10_notes"
    registry = require_exact(root, request["updates"]["prompt_record"]["registry_path"], f"{prompts}/{char}_PROMPT_RUN_LOG.jsonl", "prompt registry")
    results = require_exact(root, request["updates"]["test_results"]["path"], f"{notes}/{char}_TEST_RESULTS.md", "Test Results")
    presets = require_exact(root, request["updates"]["reference_presets"]["path"], f"{notes}/{char}_REFERENCE_PRESETS.json", "Reference Presets")
    index = require_exact(root, request["prompt_linkage"]["prompt_index_path"], f"{prompts}/{char}_PROMPT_INDEX.md", "Prompt Index")
    canon = None
    if request["updates"]["canon_index"] is not None:
        canon = require_exact(root, request["updates"]["canon_index"]["path"], f"{notes}/{char}_CANON_INDEX.md", "Canon Index")

    source_rel, source = target(root, request["prompt_linkage"]["prompt_source_path"])
    source_parent = (char_root / "06_prompts").resolve()
    try:
        source.relative_to(source_parent)
    except ValueError:
        fail(1, "DEPLOY-AUTH-002", "prompt source must remain under the character 06_prompts directory")
    if source.parent != source_parent or not re.fullmatch(rf"{re.escape(char)}_.*PROMPT.*\.(?:md|txt)", source.name, re.IGNORECASE):
        fail(1, "DEPLOY-AUTH-002", "invalid prompt-source artifact")
    if path_key(source) in {path_key(registry[1]), path_key(index[1])}:
        fail(1, "DEPLOY-AUTH-002", "registry/index cannot be prompt source")

    out_rel, out = target(root, request["planned_output_path"])
    generated = (char_root / "07_generated").resolve()
    try:
        out.relative_to(generated)
    except ValueError:
        fail(1, "DEPLOY-AUTH-003", "destination must remain under the character 07_generated directory")
    if out.suffix.lower() != ".png" or any(part.casefold() in PRIVATE_PARTS for part in PurePosixPath(out_rel).parts):
        fail(1, "DEPLOY-AUTH-003", "destination is not an approved public PNG path")

    references: list[tuple[str, Path]] = []
    character_ids = request.get("character_ids", [char])
    for raw in request["reference_paths"]:
        rel, path = target(root, raw)
        allowed = False
        try:
            path.relative_to(char_root)
            allowed = True
        except ValueError:
            joint = (root / "AI_CHARACTERS" / "_JOINT_SCENES").resolve()
            try:
                path.relative_to(joint)
                allowed = len(character_ids) > 1
            except ValueError:
                pass
        if not allowed or any(part.casefold() in PRIVATE_PARTS for part in PurePosixPath(rel).parts):
            fail(1, "DEPLOY-AUTH-004", f"reference outside allowed namespace: {rel}")
        references.append((rel, path))

    contract = Contract(root_rel, char_root, registry, results, presets, canon, index, (source_rel, source), (out_rel, out), tuple(references))
    roles: list[tuple[str, tuple[str, Path]]] = [
        ("destination", contract.destination), ("registry", contract.registry),
        ("test_results", contract.test_results), ("presets", contract.presets),
        ("prompt_index", contract.prompt_index), ("prompt_source", contract.prompt_source),
    ]
    if contract.canon_index:
        roles.append(("canon_index", contract.canon_index))
    roles.extend((f"reference[{index}]", value) for index, value in enumerate(contract.references))
    seen: dict[str, str] = {}
    for role, (_, path) in roles:
        key = path_key(path)
        if key in seen:
            fail(1, "DEPLOY-AUTH-005", f"semantic path alias: {role} equals {seen[key]}")
        seen[key] = role
    return contract


def source_file(request: dict[str, Any]) -> Path:
    path = Path(request["source_image_path"]).expanduser()
    if path.is_symlink():
        fail(1, "DEPLOY-REQ-015", "source may not be a symlink")
    path = path.resolve()
    if not path.is_file() or path.suffix.lower() != ".png":
        fail(1, "DEPLOY-REQ-015", "invalid source")
    head = path.read_bytes()[:64]
    if not head.startswith(PNG_SIGNATURE) or head.startswith(b"version https://git-lfs.github.com/spec/v1"):
        fail(1, "DEPLOY-REQ-016", "source is not real PNG bytes")
    if digest(path).lower() != request["source_image_sha256"].lower():
        fail(3, "DEPLOY-GIT-012", "source hash mismatch")
    return path


def exact_hashes(root: Path, request: dict[str, Any], contract: Contract) -> dict[str, str]:
    provided: dict[str, tuple[str, str]] = {}
    for raw, expected in request["expected_file_hashes"].items():
        rel, path = target(root, raw)
        key = path_key(path)
        if key in provided:
            fail(2, "DEPLOY-REQ-018", "duplicate normalized hash path")
        provided[key] = (rel, expected.lower())
    required = {path_key(path): (rel, path) for rel, path in contract.hashed}
    if set(provided) != set(required):
        missing = sorted(required[key][0] for key in set(required) - set(provided))
        extra = sorted(provided[key][0] for key in set(provided) - set(required))
        fail(1, "DEPLOY-AUTH-006", f"expected_file_hashes must equal exact contract; missing={missing} extra={extra}")
    result: dict[str, str] = {}
    for key, (rel, path) in required.items():
        if not path.is_file() or path.is_symlink():
            fail(3, "DEPLOY-GIT-013", f"missing expected file: {rel}")
        tracked(root, rel)
        actual = digest(path)
        if actual.lower() != provided[key][1]:
            fail(3, "DEPLOY-GIT-014", f"stale hash: {rel}")
        result[rel] = actual

    absent = request["expected_absent_paths"]
    if len(absent) != 1:
        fail(1, "DEPLOY-AUTH-007", "expected_absent_paths must contain only the destination")
    absent_rel, absent_path = target(root, absent[0])
    if path_key(absent_path) != path_key(contract.destination[1]) or absent_rel.casefold() != contract.destination[0].casefold():
        fail(1, "DEPLOY-AUTH-007", "expected_absent_paths must equal planned_output_path")
    if absent_path.exists():
        fail(3, "DEPLOY-GIT-015", f"collision: {absent_rel}")
    return result


def required_markers(text: str, markers: list[str], code: str) -> None:
    for marker in markers:
        if marker not in text:
            fail(1, code, f"required evidence marker missing: {marker}")


def validate_evidence(root: Path, request: dict[str, Any], contract: Contract) -> tuple[tuple[str, Path], ...]:
    evidence_paths: list[tuple[str, Path]] = []
    mutation_keys = {path_key(path) for _, path in contract.mutations}
    all_role_keys = mutation_keys | {path_key(contract.prompt_index[1]), path_key(contract.prompt_source[1])}
    all_role_keys |= {path_key(path) for _, path in contract.references}
    for item in request["approval_evidence"]:
        markers = item["required_text"]
        kind = item["kind"]
        if kind == "voyage_decision":
            rel, path = target(root, item["path"], allow_voyage=True)
            tracked(root, rel)
            text = path.read_bytes().decode("utf-8")
            if digest(path).lower() != item["sha256"].lower():
                fail(3, "DEPLOY-GIT-021", "stale Voyage evidence hash")
            if text.count(item["decision_id"]) != 1:
                fail(1, "DEPLOY-AUTH-008", "decision ID must occur exactly once")
            required_markers(text, markers, "DEPLOY-AUTH-008")
        elif kind == "repo_path":
            rel, path = target(root, item["path"])
            try:
                path.relative_to(contract.character_root)
            except ValueError:
                fail(1, "DEPLOY-AUTH-008", "repo_path evidence must remain in character namespace")
            if path.suffix.lower() not in {".md", ".txt", ".json", ".jsonl"}:
                fail(1, "DEPLOY-AUTH-008", "repo_path evidence must be a tracked text artifact")
            tracked(root, rel)
            text = path.read_bytes().decode("utf-8")
            if digest(path).lower() != item["sha256"].lower():
                fail(3, "DEPLOY-GIT-021", "stale repo evidence hash")
            required_markers(text, markers, "DEPLOY-AUTH-008")
        else:
            rel = relative(item["path"], allow_voyage=True)
            process = command(["git", "cat-file", "-e", f"{item['commit_hash']}^{{commit}}"], root, False)
            if process.returncode:
                fail(1, "DEPLOY-AUTH-008", "approval commit does not exist")
            process = command(["git", "show", f"{item['commit_hash']}:{rel}"], root, False)
            if process.returncode:
                fail(1, "DEPLOY-AUTH-008", "approval path absent at commit")
            required_markers(process.stdout, markers, "DEPLOY-AUTH-008")
            _, path = target(root, rel, allow_voyage=True)
        key = path_key(path)
        if key in all_role_keys:
            fail(1, "DEPLOY-AUTH-005", "approval evidence aliases another semantic role")
        all_role_keys.add(key)
        evidence_paths.append((rel, path))
    return tuple(evidence_paths)


def git_check(root: Path, head: str, allowed_dirty: set[str] | None = None) -> None:
    if not command(["git", "symbolic-ref", "--quiet", "--short", "HEAD"], root).stdout.strip():
        fail(3, "DEPLOY-GIT-006", "detached HEAD")
    if command(["git", "rev-parse", "HEAD"], root).stdout.strip().lower() != head.lower():
        fail(3, "DEPLOY-GIT-007", "HEAD mismatch")
    for marker in ["MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD", "rebase-merge", "rebase-apply"]:
        if (root / ".git" / marker).exists():
            fail(3, "DEPLOY-GIT-008", f"Git operation active: {marker}")
    if command(["git", "diff", "--cached", "--name-only"], root).stdout.strip():
        fail(3, "DEPLOY-GIT-009", "staged changes forbidden")
    dirty = set(filter(None, command(["git", "diff", "--name-only"], root).stdout.splitlines()))
    if dirty - (allowed_dirty or set()):
        fail(3, "DEPLOY-GIT-010", f"unexpected dirty files: {sorted(dirty)}")


def once(text: str, needle: str, code: str) -> None:
    if text.count(needle) != 1:
        fail(1, code, f"required text must occur once: {needle}")


def decode_text(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    newline = "\r\n" if b"\r\n" in raw else "\n"
    return text, newline


def markdown(text: str, update: dict[str, Any], newline: str) -> str:
    anchor = update["unique_anchor"]
    once(text, anchor, "DEPLOY-LINK-004")
    if update["entry_markdown"] in text:
        fail(1, "DEPLOY-LINK-005", "Markdown entry collision")
    position = text.index(anchor) + len(anchor)
    entry = newline + update["entry_markdown"].rstrip("\r\n").replace("\n", newline) + newline
    output = text[:position] + entry + text[position:]
    return output if output.endswith(("\n", "\r")) else output + newline


def validate_linkage_and_references(root: Path, request: dict[str, Any], contract: Contract) -> None:
    for rel, path in [contract.prompt_index, contract.prompt_source, *contract.references]:
        if not path.is_file() or path.is_symlink():
            fail(1, "DEPLOY-LINK-014", f"missing validation artifact: {rel}")
        tracked(root, rel)
    index_text = contract.prompt_index[1].read_bytes().decode("utf-8")
    source_text = contract.prompt_source[1].read_bytes().decode("utf-8")
    linkage = request["prompt_linkage"]
    once(index_text, linkage["prompt_index_required_text"], "DEPLOY-LINK-011")
    once(source_text, linkage["prompt_heading"], "DEPLOY-LINK-012")
    if request["prompt_id"] not in source_text:
        fail(1, "DEPLOY-LINK-013", "prompt ID absent from source")


def normalized_references(values: Any) -> list[str]:
    if not isinstance(values, list):
        return []
    return [relative(value).casefold() for value in values]


def prepare(root: Path, request: dict[str, Any], source: Path, contract: Contract | None = None) -> tuple[dict[str, bytes], list[dict[str, str]]]:
    contract = contract or resolve_contract(root, request)
    changes: dict[str, bytes] = {contract.destination[0]: source.read_bytes()}
    plan = [{"action": "COPY", "path": contract.destination[0], "before": "ABSENT", "change": "COPY_SOURCE", "validation": "PASS"}]

    registry_rel, registry = contract.registry
    raw_lines = registry.read_bytes().decode("utf-8").splitlines(keepends=True)
    records: list[tuple[int, dict[str, Any]]] = []
    prompt_ids: list[str] = []
    for index, line in enumerate(raw_lines):
        if not line.strip():
            continue
        record = json_load_text(line, "DEPLOY-LINK-002")
        if not isinstance(record, dict):
            fail(1, "DEPLOY-LINK-002", f"JSONL line {index + 1} must be an object")
        records.append((index, record))
        prompt_ids.append(record.get("prompt_id"))
    if len(prompt_ids) != len(set(prompt_ids)):
        fail(1, "DEPLOY-LINK-003", "duplicate prompt IDs")
    matches = [(index, record) for index, record in records if record.get("prompt_id") == request["prompt_id"]]
    if len(matches) != 1:
        fail(1, "DEPLOY-LINK-006", "existing prompt record not unique")
    line_index, record = matches[0]
    identity = {
        "prompt_id": request["prompt_id"], "character_id": request["character_id"],
        "test_number": request["test_number"], "scene_id": request["scene_id"], "version": request["version"],
    }
    for key, expected in identity.items():
        if key not in record or record[key] != expected:
            fail(1, "DEPLOY-LINK-007", f"immutable mismatch: {key}")
    for optional in ("variant_label", "backend"):
        if optional in request or optional in record:
            if request.get(optional) != record.get(optional):
                fail(1, "DEPLOY-LINK-007", f"immutable mismatch: {optional}")
    requested_ids = request.get("character_ids", [request["character_id"]])
    if "character_ids" in record and record["character_ids"] != requested_ids:
        fail(1, "DEPLOY-LINK-007", "immutable mismatch: character_ids")
    if "primary_character_id" in record and record["primary_character_id"] != request["character_id"]:
        fail(1, "DEPLOY-LINK-007", "immutable mismatch: primary_character_id")
    if normalized_references(record.get("reference_paths")) != normalized_references(request["reference_paths"]):
        fail(1, "DEPLOY-LINK-008", "reference mismatch")
    for key, expected in {
        "prompt_source_path": contract.prompt_source[0], "prompt_source": contract.prompt_source[0],
        "prompt_heading": request["prompt_linkage"]["prompt_heading"],
        "prompt_index_path": contract.prompt_index[0],
    }.items():
        if key in record and relative(record[key]).casefold() != relative(expected).casefold() if key != "prompt_heading" else record[key] != expected:
            fail(1, "DEPLOY-LINK-007", f"immutable mismatch: {key}")
    if str(record.get("verdict", "")).upper() in TERMINAL_BAD_VERDICTS:
        fail(1, "DEPLOY-LINK-009", "rejected/superseded attempt cannot be approved")
    if record.get("deployed") is True or record.get("output_path"):
        fail(1, "DEPLOY-LINK-010", "conflicting existing deployment")

    updated = dict(record)
    updated.update(request["updates"]["prompt_record"]["set_fields"])
    old_line = raw_lines[line_index]
    ending = "\r\n" if old_line.endswith("\r\n") else "\n" if old_line.endswith("\n") else ""
    raw_lines[line_index] = json.dumps(updated, ensure_ascii=False, separators=(",", ":")) + ending
    changes[registry_rel] = "".join(raw_lines).encode("utf-8")
    plan.append({"action": "UPDATE", "path": registry_rel, "before": digest(registry), "change": "ONE_JSONL_RECORD", "validation": "PASS"})

    validate_linkage_and_references(root, request, contract)
    for rel, path in (contract.prompt_index, contract.prompt_source):
        plan.append({"action": "VALIDATE", "path": rel, "before": digest(path), "change": "NONE", "validation": "PASS"})

    results_rel, results_path = contract.test_results
    results_text, results_newline = decode_text(results_path)
    changes[results_rel] = markdown(results_text, request["updates"]["test_results"], results_newline).encode("utf-8")
    plan.append({"action": "UPDATE", "path": results_rel, "before": digest(results_path), "change": "INSERT_MARKDOWN", "validation": "PASS"})

    presets_rel, presets_path = contract.presets
    document = json_object(presets_path, "DEPLOY-LINK-015")
    container: Any = document
    preset_update = request["updates"]["reference_presets"]
    for key in preset_update["container_path"]:
        if not isinstance(container, dict) or key not in container:
            fail(1, "DEPLOY-LINK-016", "preset container missing")
        container = container[key]
    if not isinstance(container, dict) or preset_update["preset_id"] in container:
        fail(1, "DEPLOY-LINK-017", "preset collision/container invalid")
    container[preset_update["preset_id"]] = preset_update["preset_value"]
    changes[presets_rel] = (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    plan.append({"action": "UPDATE", "path": presets_rel, "before": digest(presets_path), "change": "INSERT_PRESET", "validation": "PASS"})

    if contract.canon_index:
        canon_rel, canon_path = contract.canon_index
        canon_text, canon_newline = decode_text(canon_path)
        changes[canon_rel] = markdown(canon_text, request["updates"]["canon_index"], canon_newline).encode("utf-8")
        plan.append({"action": "UPDATE", "path": canon_rel, "before": digest(canon_path), "change": "INSERT_MARKDOWN", "validation": "PASS"})
    return changes, plan


def lfs(root: Path, output: str) -> None:
    if not command(["git", "check-attr", "filter", "--", output], root).stdout.rstrip().endswith(": lfs"):
        fail(1, "DEPLOY-LFS-001", "destination lacks LFS")
    if command(["git", "lfs", "version"], root, False).returncode:
        fail(1, "DEPLOY-LFS-002", "Git LFS unavailable")
    if command(["git", "check-ignore", "-q", "--", output], root, False).returncode == 0:
        fail(1, "DEPLOY-LFS-003", "destination ignored")


def validators(root: Path, character: str, *, post: bool = False) -> None:
    tool = root / "tools" / "validate_visual_canon_pipeline.py"
    order = [["--character", character], []] if post else [[], ["--character", character]]
    for extra in order:
        process = command(
            [sys.executable, str(tool), "--repo-root", str(root), "--mode", "compatibility", "--no-color", *extra],
            root, False,
        )
        if process.returncode:
            scope = "character" if extra else "full"
            fail(1, "DEPLOY-VALIDATOR-001", f"{scope} validator failed: {process.returncode}")


def verify_hashes(root: Path, hashes: dict[str, str]) -> None:
    for rel, expected in hashes.items():
        path = root / Path(rel)
        if not path.is_file() or digest(path).lower() != expected.lower():
            fail(3, "DEPLOY-GIT-016", f"concurrent edit: {rel}")


def verify_preconditions(root: Path, request: dict[str, Any], contract: Contract, source: Path, hashes: dict[str, str]) -> None:
    git_check(root, request["expected_git_head"])
    verify_hashes(root, hashes)
    if contract.destination[1].exists():
        fail(3, "DEPLOY-GIT-015", f"collision: {contract.destination[0]}")
    if digest(source).lower() != request["source_image_sha256"].lower():
        fail(3, "DEPLOY-GIT-012", "source changed")
    validate_linkage_and_references(root, request, contract)
    validate_evidence(root, request, contract)


def transaction(
    root: Path,
    request: dict[str, Any],
    changes: dict[str, bytes],
    hashes: dict[str, str],
    source: Path,
    contract: Contract | None = None,
    post_validator: Callable[[Path, str], None] | None = None,
    event_hook: Callable[[str, str | None], None] | None = None,
    replace: Callable[[str | os.PathLike[str], str | os.PathLike[str]], None] = os.replace,
    rollback_replace: Callable[[str | os.PathLike[str], str | os.PathLike[str]], None] = os.replace,
) -> dict[str, Any]:
    contract = contract or resolve_contract(root, request)
    hook = event_hook or (lambda _event, _rel: None)
    hook("before_second_preconditions", None)
    verify_preconditions(root, request, contract, source, hashes)

    order = [rel for rel, _ in contract.mutations]
    transaction_dir = Path(tempfile.mkdtemp(prefix=f"ncc_deploy_{request['operation_id']}_"))
    backups, prepared = transaction_dir / "backups", transaction_dir / "prepared"
    backups.mkdir()
    prepared.mkdir()
    manifest = transaction_dir / "recovery_manifest.json"
    before_status = command(["git", "status", "--porcelain", "--untracked-files=no"], root).stdout
    state: dict[str, Any] = {
        "operation_id": request["operation_id"], "expected_head": request["expected_git_head"],
        "status": "PREPARED", "target_hashes": hashes, "replacement_order": order,
        "backup_paths": {}, "completed": [], "incomplete_steps": [],
        "transaction_dir": str(transaction_dir),
    }

    def save() -> None:
        manifest.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for rel, data in changes.items():
        prepared_path = prepared / Path(rel)
        prepared_path.parent.mkdir(parents=True, exist_ok=True)
        prepared_path.write_bytes(data)
        target_path = root / Path(rel)
        if target_path.exists():
            backup = backups / Path(rel)
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target_path, backup)
            state["backup_paths"][rel] = str(backup)
    save()
    created_directories: list[Path] = []
    try:
        hook("before_first_mutation", None)
        verify_preconditions(root, request, contract, source, hashes)
        for rel in order:
            hook("before_replace", rel)
            target_path = root / Path(rel)
            if rel == contract.destination[0]:
                if target_path.exists():
                    fail(3, "DEPLOY-GIT-015", f"collision: {rel}")
            else:
                expected = hashes[rel]
                if digest(target_path).lower() != expected.lower():
                    fail(3, "DEPLOY-GIT-016", f"target changed immediately before replacement: {rel}")
            git_check(root, request["expected_git_head"], set(state["completed"]))
            missing: list[Path] = []
            parent = target_path.parent
            while parent != root and not parent.exists():
                missing.append(parent)
                parent = parent.parent
            target_path.parent.mkdir(parents=True, exist_ok=True)
            created_directories.extend(reversed(missing))
            temporary = target_path.with_name(target_path.name + "." + request["operation_id"] + ".tmp")
            shutil.copy2(prepared / Path(rel), temporary)
            replace(temporary, target_path)
            state["completed"].append(rel)
            state["status"] = "APPLYING"
            save()
            hook("after_replace", rel)

        git_check(root, request["expected_git_head"], set(changes))
        if post_validator:
            post_validator(root, request["character_id"])
        else:
            validators(root, request["character_id"], post=True)
        if digest(source).lower() != request["source_image_sha256"].lower() or digest(contract.destination[1]) != digest(source):
            fail(4, "DEPLOY-TXN-001", "image hash failure")
        shutil.rmtree(transaction_dir)
        return {"status": "APPLIED", "changed_files": order}
    except Exception as error:
        if not state["completed"]:
            shutil.rmtree(transaction_dir, ignore_errors=True)
            if isinstance(error, DeployError):
                raise
            fail(4, "DEPLOY-TXN-002", f"apply failed before mutation: {error}")
        for rel in reversed(state["completed"]):
            target_path = root / Path(rel)
            backup = backups / Path(rel)
            try:
                if backup.exists():
                    temporary = target_path.with_name(target_path.name + ".rollback.tmp")
                    shutil.copy2(backup, temporary)
                    rollback_replace(temporary, target_path)
                    if digest(target_path).lower() != hashes[rel].lower():
                        raise OSError("restored hash mismatch")
                elif target_path.exists():
                    target_path.unlink()
            except Exception as restore_error:
                state["incomplete_steps"].append({"path": rel, "error": str(restore_error)})
        for directory in reversed(created_directories):
            try:
                if directory.exists() and not any(directory.iterdir()):
                    directory.rmdir()
            except OSError:
                pass
        restored = command(["git", "status", "--porcelain", "--untracked-files=no"], root, False).stdout == before_status
        state["status"] = "ROLLED_BACK" if not state["incomplete_steps"] and restored else "ROLLBACK_INCOMPLETE"
        state["error"] = str(error)
        save()
        if state["status"] == "ROLLED_BACK":
            shutil.rmtree(transaction_dir)
            fail(4, "DEPLOY-TXN-002", "apply failed; repository restored")
        fail(4, "DEPLOY-TXN-003", f"rollback incomplete: {manifest}")


def report(path_value: str, root: Path, data: dict[str, Any], overwrite: bool) -> None:
    path = Path(path_value).resolve()
    try:
        path.relative_to(root)
        fail(2, "DEPLOY-CLI-004", "report must be outside repository")
    except ValueError:
        pass
    if not path.parent.exists():
        fail(2, "DEPLOY-CLI-005", "report parent missing")
    if path.exists() and not overwrite:
        fail(2, "DEPLOY-CLI-006", "report exists")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        prog="deploy_visual_canon_result",
        description="Deploy one existing human-approved visual-canon attempt.",
    )
    result.add_argument("--request", required=True)
    result.add_argument("--repo-root")
    result.add_argument("--apply", action="store_true")
    result.add_argument("--json-report")
    result.add_argument("--overwrite-report", action="store_true")
    result.add_argument("--no-color", action="store_true")
    result.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return result


def main(argv: list[str] | None = None) -> int:
    try:
        arguments = parser().parse_args(argv)
        root = repository(arguments.repo_root)
        request = json_object(Path(arguments.request).resolve())
        validate_request(request)
        contract = resolve_contract(root, request)
        git_check(root, request["expected_git_head"])
        source = source_file(request)
        hashes = exact_hashes(root, request, contract)
        validate_evidence(root, request, contract)
        lfs(root, contract.destination[0])
        changes, plan = prepare(root, request, source, contract)
        validators(root, request["character_id"], post=False)
        data: dict[str, Any] = {
            "tool": "deploy_visual_canon_result", "version": __version__,
            "mode": "apply" if arguments.apply else "dry_run", "operation_id": request["operation_id"],
            "status": "DRY_RUN_VALID", "plan": plan, "changed_files": [],
        }
        if arguments.apply:
            data.update(transaction(root, request, changes, hashes, source, contract))
        if arguments.json_report:
            report(arguments.json_report, root, data, arguments.overwrite_report)
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return 0
    except DeployError as error:
        print(f"[{error.code}] {error.message}", file=sys.stderr)
        return error.status
    except SystemExit:
        raise
    except Exception as error:
        print(f"[DEPLOY-INTERNAL] {error}", file=sys.stderr)
        return 5


if __name__ == "__main__":
    raise SystemExit(main())
