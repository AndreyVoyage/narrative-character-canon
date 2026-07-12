#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legacy/compatibility mode tests for validate_visual_canon_pipeline.py."""

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


def _run_validator(repo_root, mode="compatibility"):
    cmd = [
        sys.executable, str(VALIDATOR),
        "--repo-root", str(repo_root),
        "--mode", mode,
        "--no-color",
    ]
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def _build_repo(fixture_name):
    tmp = tempfile.mkdtemp(prefix="ncc_validator_")
    root = Path(tmp)
    char_dir = root / "AI_CHARACTERS" / "TESTB" / "06_prompts"
    char_dir.mkdir(parents=True)
    log_src = FIXTURES / fixture_name / "prompt_run_log.jsonl"
    log_dst = char_dir / "TESTB_PROMPT_RUN_LOG.jsonl"
    shutil.copy2(log_src, log_dst)

    policy_dir = root / "configs" / "visual_canon"
    policy_dir.mkdir(parents=True)
    (policy_dir / "pipeline_policy.json").write_text(json.dumps(DEFAULT_POLICY, ensure_ascii=False, indent=2), encoding="utf-8")
    (policy_dir / "prompt_record.schema.json").write_text("{}", encoding="utf-8")
    (policy_dir / "character_manifest.schema.json").write_text("{}", encoding="utf-8")

    # Create files referenced by the legacy record.
    ref = root / "AI_CHARACTERS" / "TESTB" / "03_face_sheet" / "TESTB_face_canon_v1.png"
    ref.parent.mkdir(parents=True)
    ref.write_bytes(b"\x89PNG\r\n\x1a\n")
    prompt = root / "AI_CHARACTERS" / "TESTB" / "06_prompts" / "TESTB_IDENTITY.md.txt"
    prompt.parent.mkdir(parents=True, exist_ok=True)
    prompt.write_text("legacy prompt file", encoding="utf-8")

    return root


class TestLegacyCompatibility(unittest.TestCase):
    def test_legacy_passes_compatibility_with_warnings(self):
        root = _build_repo("valid_legacy")
        try:
            result = _run_validator(root, mode="compatibility")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("VC-036", result.stdout)
            self.assertIn("VC-034", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_legacy_fails_strict(self):
        root = _build_repo("valid_legacy")
        try:
            result = _run_validator(root, mode="strict")
            self.assertEqual(result.returncode, 1)
            self.assertIn("VC-036", result.stdout)
        finally:
            shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
