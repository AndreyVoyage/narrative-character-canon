#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Per-record validation tests using small fixtures."""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = REPO_ROOT / "tools" / "validate_visual_canon_pipeline.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

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


def _run_validator(repo_root):
    cmd = [sys.executable, str(VALIDATOR), "--repo-root", str(repo_root), "--no-color"]
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def _build_repo(fixture_name, refs_to_create=None, prompts=None):
    """Create a temporary repo containing one fixture log and minimal policy."""
    prompts = prompts or {}
    tmp = tempfile.mkdtemp(prefix="ncc_validator_")
    root = Path(tmp)
    char_dir = root / "AI_CHARACTERS" / "TESTX" / "06_prompts"
    char_dir.mkdir(parents=True)
    log_src = FIXTURES / fixture_name / "prompt_run_log.jsonl"
    log_dst = char_dir / "TESTX_PROMPT_RUN_LOG.jsonl"
    shutil.copy2(log_src, log_dst)

    policy_dir = root / "configs" / "visual_canon"
    policy_dir.mkdir(parents=True)
    (policy_dir / "pipeline_policy.json").write_text(json.dumps(DEFAULT_POLICY, ensure_ascii=False, indent=2), encoding="utf-8")
    (policy_dir / "prompt_record.schema.json").write_text("{}", encoding="utf-8")
    (policy_dir / "character_manifest.schema.json").write_text("{}", encoding="utf-8")

    if refs_to_create:
        for ref in refs_to_create:
            ref_path = root / ref.replace("/", "\\" if sys.platform == "win32" else "/")
            ref_path.parent.mkdir(parents=True, exist_ok=True)
            ref_path.write_bytes(b"\x89PNG\r\n\x1a\n")

    for prompt_path, size in prompts.items():
        p = root / prompt_path.replace("/", "\\" if sys.platform == "win32" else "/")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b" " * size if size else b"")

    return root


class TestPromptRecordValidation(unittest.TestCase):
    def test_valid_strict_passes(self):
        refs = ["AI_CHARACTERS/TESTA/03_face_sheet/TESTA_face_canon_v1.png"]
        root = _build_repo("valid_strict", refs_to_create=refs)
        try:
            result = _run_validator(root)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertNotIn("[ERROR]", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_invalid_jsonl_fails(self):
        root = _build_repo("invalid_jsonl")
        try:
            result = _run_validator(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("VC-005", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_duplicate_prompt_id_fails(self):
        refs = ["AI_CHARACTERS/TESTD/03_face_sheet/TESTD_face.png"]
        root = _build_repo("invalid_duplicate_id", refs_to_create=refs)
        try:
            result = _run_validator(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("VC-009", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_shared_prompt_id_with_different_variant_passes(self):
        """Same canonical prompt_id with different attempt/variant/output is allowed."""
        refs = ["AI_CHARACTERS/TESTV/03_face_sheet/TESTV_face.png"]
        root = _build_repo("valid_variant_shared_id", refs_to_create=refs)
        try:
            result = _run_validator(root)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertNotIn("VC-009", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_variant_label_in_prompt_id_fails(self):
        refs = ["AI_CHARACTERS/TESTE/03_face_sheet/TESTE_face.png"]
        root = _build_repo("invalid_variant_in_id", refs_to_create=refs)
        try:
            result = _run_validator(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("VC-011", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_missing_reference_fails(self):
        # Intentionally do not create the missing reference.
        root = _build_repo("invalid_missing_reference")
        try:
            result = _run_validator(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("VC-016", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_selected_without_approval_fails(self):
        refs = ["AI_CHARACTERS/TESTG/03_face_sheet/TESTG_face.png"]
        root = _build_repo("invalid_selected_without_approval", refs_to_create=refs)
        try:
            result = _run_validator(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("VC-019", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_local_only_leak_fails(self):
        refs = ["AI_CHARACTERS/TESTH/03_face_sheet/TESTH_face.png"]
        root = _build_repo("invalid_local_only_leak", refs_to_create=refs)
        try:
            result = _run_validator(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("VC-024", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_multiple_main_fails(self):
        refs = ["AI_CHARACTERS/TESTI/03_face_sheet/TESTI_face.png"]
        root = _build_repo("invalid_multiple_main", refs_to_create=refs)
        try:
            result = _run_validator(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("VC-021", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_empty_prompt_source_fails(self):
        refs = ["AI_CHARACTERS/TESTJ/03_face_sheet/TESTJ_face.png"]
        prompts = {"AI_CHARACTERS/TESTJ/06_prompts/TESTJ_PROMPT.md": 0}
        root = _build_repo("invalid_empty_prompt", refs_to_create=refs, prompts=prompts)
        try:
            result = _run_validator(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("VC-008", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_mojibake_warns_but_passes(self):
        refs = ["AI_CHARACTERS/TESTK/03_face_sheet/TESTK_face.png"]
        root = _build_repo("invalid_mojibake", refs_to_create=refs)
        try:
            result = _run_validator(root)
            self.assertEqual(result.returncode, 0)
            self.assertIn("VC-007", result.stdout)
            self.assertIn("[WARNING]", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
