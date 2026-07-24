#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCC Visual Canon Pipeline Validator (MVP)

A read-only validator for the narrative-character-canon visual-canon pipeline.
Checks prompt-run JSONL logs, policy files, and repository structure against the
Phase 1 workflow and pipeline_policy.json without modifying the repository.

Usage:
    python tools/validate_visual_canon_pipeline.py
    python tools/validate_visual_canon_pipeline.py --mode strict --json-report report.json
    python tools/validate_visual_canon_pipeline.py --character OLGA
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


__version__ = "1.1.0"

DEFAULT_REPO_ROOT = Path("C:/DEV/Narrative/narrative-character-canon")

REGISTRY_GLOB = "*_PROMPT_RUN_LOG.jsonl"

EXIT_PASS = 0
EXIT_VALIDATION_ERROR = 1
EXIT_CLI_ERROR = 2
EXIT_INTERNAL_ERROR = 3
EXIT_REPO_PREFLIGHT_FAIL = 4
EXIT_POLICY_LOAD_FAIL = 5

# Authoritative one-ID-one-meaning catalog. Entries marked "reserved" have no
# current implementation (no per-field logic exists yet); they keep their slot
# and description rather than being silently dropped or reassigned.
CHECK_CATALOG: Dict[str, str] = {
    "VC-001": "policy file load",
    "VC-002": "prompt schema load",
    "VC-003": "manifest schema load",
    "VC-004": "JSON parse",
    "VC-005": "JSONL parse",
    "VC-006": "UTF-8 decode",
    "VC-007": "mojibake detection",
    "VC-008": "empty prompt source",
    "VC-009": "duplicate canonical prompt ID",
    "VC-010": "canonical prompt-ID format",
    "VC-011": "variant-label separation",
    "VC-012": "character-ID consistency",
    "VC-013": "scene-ID format",  # reserved
    "VC-014": "version consistency",
    "VC-015": "prompt-source existence",
    "VC-016": "reference-path existence",
    "VC-017": "empty reference list",
    "VC-018": "output-path state rules",
    "VC-019": "selected/human-approval consistency",
    "VC-020": "role consistency",
    "VC-021": "selected MAIN uniqueness",
    "VC-022": "storage-tier consistency",
    "VC-023": "content-tier consistency",
    "VC-024": "local-only leakage",
    "VC-025": "Git LFS tracking",  # reserved
    "VC-026": "prompt-index linkage",  # reserved
    "VC-027": "prompt-volume indexing",  # reserved
    "VC-028": "preset linkage",  # reserved
    "VC-029": "Test Results linkage",  # reserved
    "VC-030": "active Voyage task consistency",  # reserved
    "VC-031": "Voyage decision-ID uniqueness",  # reserved
    "VC-032": "Git tracked-tree stability",  # reserved
    "VC-033": "manifest availability",  # reserved
    "VC-034": "legacy filename pattern",
    "VC-035": "legacy verdict mapping",  # reserved
    "VC-036": "legacy schema-version absence",
    "VC-037": "pair-namespace incompleteness",  # reserved
    "VC-038": "empty pipeline",
    "VC-039": "SQLite availability/freshness",  # reserved
    "VC-040": "reserved/deferred-check notice",
}

REQUIRED_POLICY_KEYS = [
    ("authority", "source_of_truth"),
    ("naming", "prompt_id"),
    ("naming", "approved_output_filename", "role_in_filename"),
    ("allowed_content_tiers",),
    ("sqlite_sync", "role"),
    ("allowed_verdicts",),
]

REQUIRED_FIELDS_STRICT = [
    "schema_version",
    "prompt_id",
    "character_ids",
    "primary_character_id",
    "test_id",
    "test_number",
    "scene_id",
    "version",
    "backend",
    "prompt_source",
    "reference_paths",
    "output_path",
    "verdict",
]

OPTIONAL_FIELDS = [
    "variant_label",
    "selected",
    "role",
    "storage",
    "content_tier",
    "human_approval",
    "notes",
    "timestamp",
    "run_id",
]

ALLOWED_BACKENDS = {"dalle", "midjourney", "stable_diffusion", "flux", "comfyui", "ideogram", "unknown_backend"}
ALLOWED_ROLES = {"MAIN", "ALT", "REFERENCE_ONLY", "CANDIDATE", None}
ALLOWED_STORAGE = {"repo_tracked", "local_only", None}
ALLOWED_CONTENT_TIERS = {"public_filtered", "adult_local", "private_local"}
ALLOWED_VERDICTS = {
    "APPROVED_AS_TEST",
    "APPROVED_AS_CANON",
    "SUPERSEDED",
    "REJECTED",
    "DRAFT",
    "PENDING_REVIEW",
    "LEGACY_APPROVED",
}

MOJIBAKE_MARKERS = [
    "Ã©", "Ã±", "Ã", "Ð", "Â", "â", "ï", "¿", "½", "Ñ", "Â"
]

ROLE_WORDS = {"MAIN", "ALT", "REFERENCE_ONLY"}

# Findings using these codes are downgraded from [ERROR] to [WARNING] in compatibility mode.
COMPATIBILITY_DOWNGRADE_CODES = {"VC-012", "VC-014", "VC-018", "VC-034", "VC-036", "VC-040"}


class CharacterScopeError(Exception):
    """Raised when --character does not resolve to exactly one AI_CHARACTERS subdirectory."""

    def __init__(self, name: str, ambiguous: bool = False) -> None:
        self.name = name
        self.ambiguous = ambiguous
        super().__init__(name)


class Finding:
    """Single validation finding."""

    def __init__(
        self,
        level: str,
        code: str,
        path: Optional[str],
        line: Optional[int],
        message: str,
    ) -> None:
        self.level = level
        self.code = code
        self.path = path
        self.line = line
        self.message = message

    def __str__(self) -> str:
        parts = [f"{self.level} {self.code}"]
        if self.path:
            parts.append(self.path)
            if self.line is not None:
                parts[-1] += f":{self.line}"
        parts.append(self.message)
        return ": ".join(parts)


class Validator:
    """Read-only validator for the NCC visual-canon pipeline."""

    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args
        self.repo_root: Path = Path(args.repo_root).resolve()
        self.mode: str = args.mode
        self.use_color: bool = not args.no_color and sys.stdout.isatty()
        self.findings: List[Finding] = []
        self.policy: Dict[str, Any] = {}
        self.record_schema: Dict[str, Any] = {}
        self.manifest_schema: Dict[str, Any] = {}
        self._character_dir: Optional[Path] = None
        self._records_scanned: int = 0
        self._registries_scanned: int = 0

    def run(self) -> int:
        try:
            self._preflight_repo()
        except Exception as exc:
            print(f"[ERROR CLI-001] Repo root preflight failed: {exc}")
            return EXIT_REPO_PREFLIGHT_FAIL

        try:
            self._resolve_character_scope()
        except CharacterScopeError as exc:
            kind = "ambiguous" if exc.ambiguous else "unknown"
            print(f"[ERROR CLI-002] {kind} --character '{exc.name}'")
            return EXIT_CLI_ERROR

        try:
            self._load_policy_and_schemas()
        except Exception as exc:
            print(f"[ERROR INTERNAL] Policy/schema load failed: {exc}")
            return EXIT_POLICY_LOAD_FAIL

        if not self.policy:
            self._print_findings()
            return EXIT_POLICY_LOAD_FAIL

        try:
            self._validate_policy_authority()
            self._discover_and_validate_logs()
            self._print_findings()
        except Exception as exc:
            print(f"[ERROR INTERNAL] Internal validation failure: {exc}")
            self._print_findings()
            return EXIT_INTERNAL_ERROR

        report_exit = self._write_json_report()
        if report_exit is not None:
            return report_exit

        if any(f.level == "[ERROR]" for f in self.findings):
            return EXIT_VALIDATION_ERROR
        return EXIT_PASS

    # ------------------------------------------------------------------ helpers
    def _rel(self, path: Path) -> str:
        try:
            return str(path.relative_to(self.repo_root))
        except ValueError:
            return str(path)

    def _color(self, text: str, level: str) -> str:
        if not self.use_color:
            return text
        codes = {
            "[ERROR]": "\033[91m",
            "[WARNING]": "\033[93m",
            "[INFO]": "\033[94m",
        }
        reset = "\033[0m"
        return f"{codes.get(level, '')}{text}{reset}"

    def _add(self, level: str, code: str, path: Optional[str], line: Optional[int], message: str, force_error: bool = False) -> None:
        if force_error:
            level = "[ERROR]"
        elif level == "[ERROR]" and self.mode == "compatibility":
            if code in COMPATIBILITY_DOWNGRADE_CODES:
                level = "[WARNING]"
        self.findings.append(Finding(level, code, path, line, message))

    def _error(self, code: str, path: Optional[str], line: Optional[int], message: str) -> None:
        self._add("[ERROR]", code, path, line, message)

    def _warn(self, code: str, path: Optional[str], line: Optional[int], message: str) -> None:
        self._add("[WARNING]", code, path, line, message)

    def _info(self, code: str, message: str) -> None:
        self.findings.append(Finding("[INFO]", code, None, None, message))

    # ------------------------------------------------------------------ phases
    def _preflight_repo(self) -> None:
        if not self.repo_root.exists():
            raise FileNotFoundError(f"repo root does not exist: {self.repo_root}")
        if not self.repo_root.is_dir():
            raise NotADirectoryError(f"repo root is not a directory: {self.repo_root}")
        required = [
            self.repo_root / "AI_CHARACTERS",
            self.repo_root / "configs" / "visual_canon",
        ]
        for p in required:
            if not p.exists():
                raise FileNotFoundError(f"required path missing: {self._rel(p)}")

    def _resolve_character_scope(self) -> None:
        if not self.args.character:
            return
        ai_dir = self.repo_root / "AI_CHARACTERS"
        candidates = [d for d in ai_dir.iterdir() if d.is_dir()]
        # Joint/pair namespaces (e.g. KIRA_ANDREY) live one level deeper, under an
        # underscore-prefixed container directory such as _JOINT_SCENES.
        for child in list(candidates):
            if child.name.startswith("_"):
                candidates.extend(d for d in child.iterdir() if d.is_dir())
        matches = sorted(
            d for d in candidates
            if d.name.upper() == self.args.character.upper()
        )
        if len(matches) != 1:
            raise CharacterScopeError(self.args.character, ambiguous=len(matches) > 1)
        self._character_dir = matches[0]

    def _load_policy_and_schemas(self) -> None:
        policy_path = self.repo_root / "configs" / "visual_canon" / "pipeline_policy.json"
        record_schema_path = self.repo_root / "configs" / "visual_canon" / "prompt_record.schema.json"
        manifest_schema_path = self.repo_root / "configs" / "visual_canon" / "character_manifest.schema.json"

        self.policy = self._read_json(policy_path, "VC-001")
        self.record_schema = self._read_json(record_schema_path, "VC-002", optional=True) or {}
        self.manifest_schema = self._read_json(manifest_schema_path, "VC-003", optional=True) or {}

        for key_path in REQUIRED_POLICY_KEYS:
            d = self.policy
            for k in key_path:
                if not isinstance(d, dict) or k not in d:
                    self._error("VC-001", self._rel(policy_path), None, f"missing policy key {'.'.join(key_path)}")
                    break
                d = d[k]

    def _read_json(self, path: Path, code: str, optional: bool = False) -> Optional[Dict[str, Any]]:
        if not path.exists():
            if optional:
                self._warn(code, self._rel(path), None, "optional schema file missing; using empty schema")
                return None
            self._error(code, self._rel(path), None, "required JSON file missing")
            return None
        try:
            with path.open("r", encoding="utf-8") as fh:
                return json.load(fh)
        except json.JSONDecodeError as exc:
            self._error("VC-004", self._rel(path), exc.lineno, f"invalid JSON: {exc}")
        except UnicodeDecodeError as exc:
            self._error("VC-006", self._rel(path), None, f"not valid UTF-8: {exc}")
        except Exception as exc:
            self._error(code, self._rel(path), None, f"could not read: {exc}")
        return None

    def _validate_policy_authority(self) -> None:
        source = self.policy.get("authority", {}).get("source_of_truth")
        if source != "git_repository":
            self._error("VC-001", None, None, f"authority.source_of_truth must be 'git_repository', got {source!r}")
        sqlite_role = self.policy.get("sqlite_sync", {}).get("role")
        if sqlite_role != "local_mirror_and_index":
            self._error("VC-001", None, None, f"sqlite_sync.role must be 'local_mirror_and_index', got {sqlite_role!r}")
        prompt_id_naming = self.policy.get("naming", {}).get("prompt_id", {})
        variant_naming = self.policy.get("naming", {}).get("variant_label", {})
        if not (prompt_id_naming.get("variant_separate") and variant_naming.get("separate_from_prompt_id")):
            self._error("VC-001", None, None, "naming.prompt_id.variant_separate and naming.variant_label.separate_from_prompt_id must be true")
        if self.policy.get("naming", {}).get("approved_output_filename", {}).get("role_in_filename", True):
            self._error("VC-001", None, None, "naming.approved_output_filename.role_in_filename must be false")

    def _discover_and_validate_logs(self) -> None:
        if self._character_dir is not None:
            search_root = self._character_dir
            scope_label = f"character '{self.args.character}'"
        else:
            search_root = self.repo_root / "AI_CHARACTERS"
            scope_label = "AI_CHARACTERS"

        pattern = str(search_root / "**" / "06_prompts" / REGISTRY_GLOB)
        log_files = sorted(Path(p) for p in glob.glob(pattern, recursive=True))

        if not log_files:
            self._warn("VC-038", None, None, f"no prompt registries found for {scope_label}")
            return

        print(f"Discovered {len(log_files)} registry file(s) for {scope_label}.")

        all_records: List[Tuple[str, int, Dict[str, Any]]] = []
        for log_path in log_files:
            all_records.extend(self._validate_log_file_with_records(log_path))
        self._perform_duplicate_and_main_checks(all_records)
        self._records_scanned = len(all_records)
        self._registries_scanned = len(log_files)

    def _validate_log_file_with_records(self, log_path: Path) -> List[Tuple[str, int, Dict[str, Any]]]:
        rel = self._rel(log_path)
        records: List[Tuple[str, int, Dict[str, Any]]] = []
        try:
            raw_bytes = log_path.read_bytes()
        except Exception as exc:
            self._error("VC-005", rel, None, f"could not read log file: {exc}")
            return records
        try:
            text = raw_bytes.decode("utf-8")
        except UnicodeDecodeError as exc:
            self._error("VC-006", rel, None, f"log file is not valid UTF-8: {exc}")
            return records
        if self._looks_like_mojibake(text):
            self._warn("VC-007", rel, None, "possible mojibake detected (Windows-1252 artefacts)")
        for line_no, line in enumerate(text.splitlines(), start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                self._error("VC-005", rel, line_no, f"invalid JSONL line: {exc}")
                continue
            if not isinstance(record, dict):
                self._error("VC-005", rel, line_no, "JSONL line is not a JSON object")
                continue
            self._validate_record(rel, line_no, record)
            records.append((rel, line_no, record))
        return records

    def _looks_like_mojibake(self, text: str) -> bool:
        for marker in MOJIBAKE_MARKERS:
            if marker in text:
                return True
        return False

    def _validate_record(self, rel: str, line_no: int, record: Dict[str, Any]) -> None:
        # Required fields
        missing = [f for f in REQUIRED_FIELDS_STRICT if f not in record]
        if missing:
            if "schema_version" not in record:
                if self.mode == "strict":
                    self._error("VC-036", rel, line_no, f"legacy record without schema_version (missing {', '.join(missing)})")
                else:
                    self._warn("VC-036", rel, line_no, f"legacy record without schema_version (missing {', '.join(missing)})")
            else:
                self._add("[ERROR]", "VC-040", rel, line_no, f"missing required fields: {', '.join(missing)}")

        # Unknown fields
        known = set(REQUIRED_FIELDS_STRICT) | set(OPTIONAL_FIELDS)
        unknown = [k for k in record if k not in known]
        if unknown:
            self._warn("VC-040", rel, line_no, f"unknown fields: {', '.join(unknown)}")

        prompt_id = record.get("prompt_id")
        if prompt_id is not None:
            self._validate_prompt_id(rel, line_no, prompt_id, record)

        self._validate_character_ids(rel, line_no, record)
        self._validate_test_number(rel, line_no, record)
        self._validate_version(rel, line_no, record)
        self._validate_backend(rel, line_no, record)
        self._validate_prompt_source(rel, line_no, record)
        self._validate_reference_paths(rel, line_no, record)
        self._validate_output_path(rel, line_no, record)
        self._validate_verdict(rel, line_no, record)
        self._validate_selection(rel, line_no, record)
        self._validate_role(rel, line_no, record)
        self._validate_storage(rel, line_no, record)
        self._validate_content_tier(rel, line_no, record)
        self._validate_human_approval(rel, line_no, record)

    def _validate_prompt_id(self, rel: str, line_no: int, prompt_id: str, record: Dict[str, Any]) -> None:
        if not isinstance(prompt_id, str):
            self._error("VC-010", rel, line_no, "prompt_id must be a string")
            return
        if not re.fullmatch(r"[A-Z][A-Z0-9_]*", prompt_id):
            self._error("VC-010", rel, line_no, f"prompt_id '{prompt_id}' must be uppercase IDs/underscores only")
        variant_label = record.get("variant_label")
        if variant_label:
            # Variant label must not appear inside prompt_id.
            if str(variant_label).upper().replace("-", "_") in prompt_id:
                self._error("VC-011", rel, line_no, f"prompt_id '{prompt_id}' contains variant_label '{variant_label}'")
        # Cross-record duplicate check is done after all records are loaded.

    def _validate_character_ids(self, rel: str, line_no: int, record: Dict[str, Any]) -> None:
        cids = record.get("character_ids")
        primary = record.get("primary_character_id")
        if cids is not None and not isinstance(cids, list):
            self._error("VC-012", rel, line_no, "character_ids must be a list")
            return
        if isinstance(cids, list) and primary is not None:
            if primary not in cids:
                self._error("VC-012", rel, line_no, f"primary_character_id '{primary}' not in character_ids {cids}")
        # Test_id should begin with primary character id if both present.
        test_id = record.get("test_id")
        if test_id and primary:
            expected_prefix = f"{primary}_"
            if not str(test_id).startswith(expected_prefix):
                self._error("VC-012", rel, line_no, f"test_id '{test_id}' does not start with primary_character_id '{primary}'")

    def _validate_test_number(self, rel: str, line_no: int, record: Dict[str, Any]) -> None:
        tn = record.get("test_number")
        if tn is None:
            return
        if not isinstance(tn, int) or tn < 1:
            self._error("VC-040", rel, line_no, f"test_number must be a positive integer, got {tn!r}")

    def _validate_version(self, rel: str, line_no: int, record: Dict[str, Any]) -> None:
        version = record.get("version")
        prompt_id = record.get("prompt_id")
        if version and prompt_id:
            expected = f"_{str(version).upper()}"
            if not str(prompt_id).endswith(expected):
                self._error("VC-014", rel, line_no, f"prompt_id '{prompt_id}' does not end with version '{version}'")

    def _validate_backend(self, rel: str, line_no: int, record: Dict[str, Any]) -> None:
        backend = record.get("backend")
        if backend is None:
            return
        allowed = set(self.policy.get("allowed_backends", [])) | ALLOWED_BACKENDS
        if backend not in allowed:
            self._warn("VC-040", rel, line_no, f"backend '{backend}' not in allowed_backends policy")

    def _validate_prompt_source(self, rel: str, line_no: int, record: Dict[str, Any]) -> None:
        source = record.get("prompt_source")
        if source is None:
            return
        if not isinstance(source, str) or not source.strip():
            self._error("VC-015", rel, line_no, "prompt_source must be a non-empty string")
            return
        if source.strip().lower() == "exact_user_visible_prompt":
            return
        src_path = self.repo_root / source.replace("/", os.sep)
        if "LOCAL_STORAGE" in source.upper():
            self._error("VC-024", rel, line_no, f"prompt_source points to LOCAL_STORAGE: {source}")
        if not src_path.exists():
            self._warn("VC-015", rel, line_no, f"prompt_source file not found: {source}")
        else:
            size = src_path.stat().st_size
            if size == 0:
                self._error("VC-008", rel, line_no, f"prompt_source file is empty: {source}")
            elif self._has_deprecated_suffix(source):
                self._warn("VC-034", rel, line_no, f"prompt_source uses deprecated filename suffix: {source}")

    def _has_deprecated_suffix(self, path: str) -> bool:
        lower = path.lower()
        return lower.endswith(".md.txt") or lower.endswith(".txt.md") or "_backup_" in lower

    def _validate_reference_paths(self, rel: str, line_no: int, record: Dict[str, Any]) -> None:
        refs = record.get("reference_paths")
        if refs is None:
            return
        if not isinstance(refs, list):
            self._error("VC-017", rel, line_no, "reference_paths must be a list")
            return
        for ref in refs:
            if not isinstance(ref, str) or not ref.strip():
                self._error("VC-017", rel, line_no, "reference_paths entries must be non-empty strings")
                continue
            ref_path = self.repo_root / ref.replace("/", os.sep)
            if not ref_path.exists():
                self._error("VC-016", rel, line_no, f"reference path does not exist: {ref}")
            elif self._has_deprecated_suffix(ref):
                self._warn("VC-034", rel, line_no, f"reference path uses deprecated suffix: {ref}")

    def _validate_output_path(self, rel: str, line_no: int, record: Dict[str, Any]) -> None:
        out = record.get("output_path")
        if not out:
            return
        if not isinstance(out, str) or not out.strip():
            self._error("VC-018", rel, line_no, "output_path must be a non-empty string")
            return
        storage = record.get("storage")
        upper = out.upper()
        if storage == "repo_tracked" and "LOCAL_STORAGE" in upper:
            self._error("VC-024", rel, line_no, f"storage=repo_tracked but output_path is in LOCAL_STORAGE: {out}")
        if storage == "local_only" and "LOCAL_STORAGE" not in upper:
            self._warn("VC-024", rel, line_no, f"storage=local_only but output_path is not in LOCAL_STORAGE: {out}")
        if storage == "repo_tracked" and not upper.startswith("AI_CHARACTERS/"):
            self._warn("VC-018", rel, line_no, f"repo_tracked output_path should start with AI_CHARACTERS/: {out}")
        # Role must not appear in filename for approved outputs.
        basename = Path(out).name
        name_no_ext = Path(basename).stem.upper()
        parts = set(re.split(r"[_\.\-]", name_no_ext))
        if self.policy.get("approved_output_filename", {}).get("role_in_filename", True) is False:
            if parts & ROLE_WORDS:
                offending = sorted(parts & ROLE_WORDS)
                self._error("VC-018", rel, line_no, f"approved output filename contains role/status words {offending}: {out}")
        if self._has_deprecated_suffix(out):
            self._warn("VC-034", rel, line_no, f"output_path uses deprecated suffix: {out}")

    def _validate_verdict(self, rel: str, line_no: int, record: Dict[str, Any]) -> None:
        verdict = record.get("verdict")
        if verdict is None:
            return
        allowed = set(self.policy.get("allowed_verdicts", {}).get("machine_values", [])) | ALLOWED_VERDICTS
        if verdict not in allowed:
            self._warn("VC-019", rel, line_no, f"verdict '{verdict}' not in policy allowed list")

    def _validate_selection(self, rel: str, line_no: int, record: Dict[str, Any]) -> None:
        selected = record.get("selected")
        if selected is None:
            return
        if not isinstance(selected, bool):
            self._error("VC-019", rel, line_no, f"selected must be boolean, got {selected!r}")
            return
        verdict = record.get("verdict")
        human = record.get("human_approval")
        if selected:
            if verdict not in {"APPROVED_AS_TEST", "APPROVED_AS_CANON", "LEGACY_APPROVED"}:
                self._error("VC-019", rel, line_no, f"selected=true requires approved verdict, got {verdict!r}")
            if human not in {True, "owner"} and not (isinstance(human, str) and human.startswith("owner_")):
                self._error("VC-019", rel, line_no, f"selected=true requires human_approval gate, got {human!r}")
        else:
            role = record.get("role")
            if role == "MAIN":
                self._error("VC-020", rel, line_no, "selected=false cannot have role=MAIN")

    def _validate_role(self, rel: str, line_no: int, record: Dict[str, Any]) -> None:
        role = record.get("role")
        if role is None:
            return
        if role not in ALLOWED_ROLES:
            self._error("VC-020", rel, line_no, f"role '{role}' not in allowed roles {ALLOWED_ROLES}")

    def _validate_storage(self, rel: str, line_no: int, record: Dict[str, Any]) -> None:
        storage = record.get("storage")
        if storage is None:
            return
        allowed = set(self.policy.get("allowed_storage_tiers", [])) | ALLOWED_STORAGE
        if storage not in allowed:
            self._warn("VC-022", rel, line_no, f"storage '{storage}' not in allowed storage list")

    def _validate_content_tier(self, rel: str, line_no: int, record: Dict[str, Any]) -> None:
        tier = record.get("content_tier")
        if tier is None:
            return
        allowed = set(self.policy.get("allowed_content_tiers", [])) | ALLOWED_CONTENT_TIERS
        if tier not in allowed:
            self._error("VC-023", rel, line_no, f"content_tier '{tier}' not in allowed tiers")

    def _validate_human_approval(self, rel: str, line_no: int, record: Dict[str, Any]) -> None:
        ha = record.get("human_approval")
        if ha is None:
            return
        if isinstance(ha, bool):
            if ha is False and record.get("selected") is True:
                self._error("VC-019", rel, line_no, "selected=true with human_approval=false is forbidden")
            return
        if isinstance(ha, str):
            if not (ha == "owner" or ha.startswith("owner_")):
                self._warn("VC-019", rel, line_no, f"unrecognized human_approval value '{ha}'")
            return
        self._warn("VC-019", rel, line_no, f"human_approval should be bool or owner string, got {ha!r}")

    # ------------------------------------------------------------------ post-line checks
    def _perform_duplicate_and_main_checks(self, all_records: List[Tuple[str, int, Dict[str, Any]]]) -> None:
        # Composite dedup: (prompt_id, attempt, variant, output_path).
        # Canonical prompt_id may be shared across distinct attempts, variants,
        # or deployed output paths.  Only records that are indistinguishable on
        # all four axes are treated as accidental duplicates.
        comp: Dict[Tuple, List[Tuple[str, int]]] = {}
        main_keys: Dict[Tuple[str, str, str], List[Tuple[str, int, str]]] = {}
        for rel, line_no, record in all_records:
            pid = record.get("prompt_id")
            if pid:
                attempt = record.get("attempt")
                variant = record.get("variant")
                output = record.get("output_path", "")
                key = (pid, attempt, variant, output)
                comp.setdefault(key, []).append((rel, line_no))
            if record.get("role") == "MAIN" and record.get("selected") is True:
                test_id = record.get("test_id")
                scene_id = record.get("scene_id")
                primary = record.get("primary_character_id")
                key = (primary, test_id, scene_id)
                main_keys.setdefault(key, []).append((rel, line_no, pid or ""))
        for key, locations in comp.items():
            if len(locations) > 1:
                pid = key[0]
                for rel, line_no in locations:
                    self._error("VC-009", rel, line_no, f"duplicate record for prompt_id '{pid}': same attempt, variant and output_path across {len(locations)} record(s)")
        for key, locations in main_keys.items():
            if len(locations) > 1:
                for rel, line_no, pid in locations:
                    self._error("VC-021", rel, line_no, f"multiple selected MAIN records for {key}: {pid}")

    # ------------------------------------------------------------------ output
    def _print_findings(self) -> None:
        errors = sum(1 for f in self.findings if f.level == "[ERROR]")
        warnings = sum(1 for f in self.findings if f.level == "[WARNING]")
        infos = sum(1 for f in self.findings if f.level == "[INFO]")
        for f in self.findings:
            print(self._color(str(f), f.level))
        print()
        print(self._color(f"Summary: {errors} error(s), {warnings} warning(s), {infos} info message(s)", "[INFO]"))

    def _write_json_report(self) -> Optional[int]:
        if not self.args.json_report:
            return None
        report_path = Path(self.args.json_report)
        if not report_path.parent.exists():
            print(f"[ERROR CLI-004] Report parent directory does not exist: {report_path.parent}")
            return EXIT_CLI_ERROR
        if report_path.exists() and not self.args.overwrite_report:
            print(f"[ERROR CLI-003] Report file already exists: {report_path}")
            return EXIT_CLI_ERROR
        report = {
            "tool": "validate_visual_canon_pipeline",
            "version": __version__,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "repo_root": str(self.repo_root),
            "mode": self.mode,
            "character": self.args.character,
            "summary": {
                "errors": sum(1 for f in self.findings if f.level == "[ERROR]"),
                "warnings": sum(1 for f in self.findings if f.level == "[WARNING]"),
                "infos": sum(1 for f in self.findings if f.level == "[INFO]"),
                "registries_scanned": self._registries_scanned,
                "records_scanned": self._records_scanned,
            },
            "findings": [
                {
                    "level": f.level.strip("[]"),
                    "code": f.code,
                    "path": f.path,
                    "line": f.line,
                    "message": f.message,
                }
                for f in self.findings
            ],
        }
        with report_path.open("w", encoding="utf-8") as fh:
            json.dump(report, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print(f"JSON report written to {report_path}")
        return None


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="validate_visual_canon_pipeline",
        description="Validate the NCC visual-canon pipeline state.",
    )
    parser.add_argument(
        "--repo-root",
        default=str(DEFAULT_REPO_ROOT),
        help="Path to the narrative-character-canon repository root.",
    )
    parser.add_argument(
        "--mode",
        choices=["compatibility", "strict"],
        default="compatibility",
        help="Validation mode. Default: compatibility.",
    )
    parser.add_argument(
        "--character",
        default=None,
        help="Limit validation to a single character/namespace folder under AI_CHARACTERS (case-insensitive).",
    )
    parser.add_argument(
        "--json-report",
        default=None,
        help="Write a JSON report to the specified path.",
    )
    parser.add_argument(
        "--overwrite-report",
        action="store_true",
        help="Overwrite an existing JSON report file.",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable ANSI color output.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_arg_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as exc:
        return exc.code if isinstance(exc.code, int) else EXIT_CLI_ERROR

    validator = Validator(args)
    return validator.run()


if __name__ == "__main__":
    sys.exit(main())
