#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Discovery, --character scoping, check-catalog, and determinism tests."""

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = REPO_ROOT / "tools" / "validate_visual_canon_pipeline.py"

DEFAULT_POLICY = {
    "authority": {"source_of_truth": "git_repository"},
    "naming": {
        "prompt_id": {"variant_separate": True},
        "variant_label": {"separate_from_prompt_id": True},
        "approved_output_filename": {"role_in_filename": False},
    },
    "allowed_content_tiers": ["public_filtered", "adult_local", "private_local"],
    "sqlite_sync": {"role": "local_mirror_and_index"},
    "allowed_verdicts": {"machine_values": ["APPROVED_AS_TEST", "APPROVED_AS_CANON", "SUPERSEDED", "REJECTED", "DRAFT", "PENDING_REVIEW", "LEGACY_APPROVED"]},
    "allowed_backends": ["dalle", "midjourney", "stable_diffusion", "flux", "comfyui", "ideogram"],
    "allowed_storage_tiers": ["repo_tracked", "local_only"],
}


def _valid_record(character, seq, scene="scene_d01"):
    return {
        "schema_version": "1.0",
        "prompt_id": f"{character}_TESTD{seq:02d}_SCENE_V1",
        "character_ids": [character],
        "primary_character_id": character,
        "test_id": f"{character}_TESTD{seq:02d}",
        "test_number": seq,
        "scene_id": scene,
        "version": "V1",
        "backend": "dalle",
        "prompt_source": "exact_user_visible_prompt",
        "reference_paths": [],
        "output_path": f"AI_CHARACTERS/{character}/07_generated/test/{character.lower()}_test{seq:02d}_output_v1.png",
        "verdict": "APPROVED_AS_TEST",
    }


def _init_policy(root):
    policy_dir = root / "configs" / "visual_canon"
    policy_dir.mkdir(parents=True, exist_ok=True)
    (policy_dir / "pipeline_policy.json").write_text(json.dumps(DEFAULT_POLICY, ensure_ascii=False, indent=2), encoding="utf-8")
    (policy_dir / "prompt_record.schema.json").write_text("{}", encoding="utf-8")
    (policy_dir / "character_manifest.schema.json").write_text("{}", encoding="utf-8")


def _write_registry(root, character, records, filename=None):
    reg_dir = root / "AI_CHARACTERS" / character / "06_prompts"
    reg_dir.mkdir(parents=True, exist_ok=True)
    name = filename or f"{character}_PROMPT_RUN_LOG.jsonl"
    body = "\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n"
    (reg_dir / name).write_text(body, encoding="utf-8")


def _build_two_character_repo(olga_count=2, kira_count=3):
    tmp = tempfile.mkdtemp(prefix="ncc_validator_discovery_")
    root = Path(tmp)
    (root / "AI_CHARACTERS").mkdir(parents=True)
    _init_policy(root)
    _write_registry(root, "OLGA", [_valid_record("OLGA", i + 1) for i in range(olga_count)])
    _write_registry(root, "KIRA", [_valid_record("KIRA", i + 1) for i in range(kira_count)])
    return root


def _run_validator(repo_root, extra_args=None, cwd=None):
    cmd = [sys.executable, str(VALIDATOR), "--repo-root", str(repo_root), "--no-color"] + (extra_args or [])
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(cwd or REPO_ROOT))


def _run_with_report(repo_root, report_path, extra_args=None):
    args = ["--json-report", str(report_path)] + (extra_args or [])
    result = _run_validator(repo_root, extra_args=args)
    return result, json.loads(report_path.read_text(encoding="utf-8"))


def _load_validator_module():
    spec = importlib.util.spec_from_file_location("validate_visual_canon_pipeline_under_test", VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestDiscovery(unittest.TestCase):
    def test_discovers_multiple_real_named_registries(self):
        root = _build_two_character_repo(olga_count=2, kira_count=3)
        try:
            with tempfile.TemporaryDirectory() as tmp:
                report = Path(tmp) / "report.json"
                result, data = _run_with_report(root, report)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertEqual(data["summary"]["registries_scanned"], 2)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_aggregates_records_across_registries(self):
        root = _build_two_character_repo(olga_count=2, kira_count=3)
        try:
            with tempfile.TemporaryDirectory() as tmp:
                report = Path(tmp) / "report.json"
                result, data = _run_with_report(root, report)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertEqual(data["summary"]["records_scanned"], 5)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_character_scope_olga_only(self):
        root = _build_two_character_repo(olga_count=2, kira_count=3)
        try:
            with tempfile.TemporaryDirectory() as tmp:
                report = Path(tmp) / "report.json"
                result, data = _run_with_report(root, report, extra_args=["--character", "OLGA"])
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertEqual(data["summary"]["registries_scanned"], 1)
                self.assertEqual(data["summary"]["records_scanned"], 2)
                self.assertNotIn("KIRA_TESTD", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_character_scope_kira_only(self):
        root = _build_two_character_repo(olga_count=2, kira_count=3)
        try:
            with tempfile.TemporaryDirectory() as tmp:
                report = Path(tmp) / "report.json"
                result, data = _run_with_report(root, report, extra_args=["--character", "KIRA"])
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertEqual(data["summary"]["registries_scanned"], 1)
                self.assertEqual(data["summary"]["records_scanned"], 3)
                self.assertNotIn("OLGA_TESTD", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_unknown_character_exit_2(self):
        root = _build_two_character_repo()
        try:
            result = _run_validator(root, extra_args=["--character", "DOES_NOT_EXIST"])
            self.assertEqual(result.returncode, 2)
            self.assertIn("CLI-002", result.stdout + result.stderr)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_lowercase_unprefixed_name_not_discovered(self):
        tmp = tempfile.mkdtemp(prefix="ncc_validator_discovery_")
        root = Path(tmp)
        (root / "AI_CHARACTERS").mkdir(parents=True)
        _init_policy(root)
        _write_registry(root, "OLGA", [_valid_record("OLGA", 1)], filename="prompt_run_log.jsonl")
        try:
            with tempfile.TemporaryDirectory() as tmp2:
                report = Path(tmp2) / "report.json"
                result, data = _run_with_report(root, report)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertEqual(data["summary"]["registries_scanned"], 0)
                self.assertEqual(data["summary"]["records_scanned"], 0)
                self.assertIn("VC-038", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_uppercase_prefixed_name_discovered(self):
        tmp = tempfile.mkdtemp(prefix="ncc_validator_discovery_")
        root = Path(tmp)
        (root / "AI_CHARACTERS").mkdir(parents=True)
        _init_policy(root)
        _write_registry(root, "OLGA", [_valid_record("OLGA", 1)])
        try:
            with tempfile.TemporaryDirectory() as tmp2:
                report = Path(tmp2) / "report.json"
                result, data = _run_with_report(root, report)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertEqual(data["summary"]["registries_scanned"], 1)
                self.assertEqual(data["summary"]["records_scanned"], 1)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_no_registries_globally_reports_empty_pipeline(self):
        tmp = tempfile.mkdtemp(prefix="ncc_validator_discovery_")
        root = Path(tmp)
        (root / "AI_CHARACTERS").mkdir(parents=True)
        _init_policy(root)
        try:
            result = _run_validator(root)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("VC-038", result.stdout)
            self.assertIn("AI_CHARACTERS", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_known_character_without_registry_distinct_from_unknown(self):
        tmp = tempfile.mkdtemp(prefix="ncc_validator_discovery_")
        root = Path(tmp)
        (root / "AI_CHARACTERS" / "KIRA_ANDREY" / "06_prompts").mkdir(parents=True)
        _init_policy(root)
        try:
            result = _run_validator(root, extra_args=["--character", "KIRA_ANDREY"])
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("VC-038", result.stdout)
            self.assertIn("KIRA_ANDREY", result.stdout)
            self.assertNotIn("CLI-002", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)


class TestCheckCatalog(unittest.TestCase):
    def test_check_catalog_range_and_uniqueness(self):
        module = _load_validator_module()
        expected_ids = {f"VC-{i:03d}" for i in range(1, 41)}
        self.assertEqual(set(module.CHECK_CATALOG), expected_ids)
        self.assertNotIn("VC-041", module.CHECK_CATALOG)

    def test_critical_check_id_mappings(self):
        module = _load_validator_module()
        self.assertEqual(module.CHECK_CATALOG["VC-005"], "JSONL parse")
        self.assertEqual(module.CHECK_CATALOG["VC-006"], "UTF-8 decode")
        self.assertEqual(module.CHECK_CATALOG["VC-007"], "mojibake detection")
        self.assertEqual(module.CHECK_CATALOG["VC-008"], "empty prompt source")
        self.assertEqual(module.CHECK_CATALOG["VC-009"], "duplicate canonical prompt ID")


class TestDeterminism(unittest.TestCase):
    def test_deterministic_finding_order(self):
        root = _build_two_character_repo(olga_count=2, kira_count=3)
        try:
            with tempfile.TemporaryDirectory() as tmp:
                report_a = Path(tmp) / "a.json"
                report_b = Path(tmp) / "b.json"
                result_a, data_a = _run_with_report(root, report_a)
                result_b, data_b = _run_with_report(root, report_b)
                self.assertEqual(result_a.returncode, 0, result_a.stdout + result_a.stderr)
                self.assertEqual(result_b.returncode, 0, result_b.stdout + result_b.stderr)
                # Strip the "JSON report written to <path>" line: the path itself
                # legitimately differs between the two temp report files.
                def _strip_report_line(s):
                    return "\n".join(line for line in s.splitlines() if "JSON report written to" not in line)

                self.assertEqual(_strip_report_line(result_a.stdout), _strip_report_line(result_b.stdout))
                data_a.pop("timestamp_utc")
                data_b.pop("timestamp_utc")
                self.assertEqual(data_a, data_b)
        finally:
            shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
