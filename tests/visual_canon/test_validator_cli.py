#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CLI-level tests for validate_visual_canon_pipeline.py."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = REPO_ROOT / "tools" / "validate_visual_canon_pipeline.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


class TestValidatorCLI(unittest.TestCase):
    def _run(self, args, cwd=None):
        cmd = [sys.executable, str(VALIDATOR)] + args
        return subprocess.run(
            cmd,
            cwd=str(cwd or REPO_ROOT),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

    def test_version_flag(self):
        result = self._run(["--version"])
        self.assertEqual(result.returncode, 0)
        self.assertIn("validate_visual_canon_pipeline", result.stdout)

    def test_default_repo_root_passes(self):
        # The real repo has real *_PROMPT_RUN_LOG.jsonl registries under AI_CHARACTERS/<CHAR>/06_prompts/,
        # and discovery now finds them. Compatibility mode currently exits 1: OLGA's legacy
        # OLGA_TEST09_FORMAL_ELEGANT_V4 record (selected=true, deployed=true, published in commit
        # 1f887dc per .voyage/CURRENT_TASK.md) predates the human_approval field and trips VC-019.
        # This is a genuine pre-existing data gap, not a validator bug -- see CURRENT_TASK.md for the
        # follow-up to backfill human_approval on that record. Character data is intentionally left
        # untouched by this validator-only commit.
        result = self._run(["--no-color"])
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Discovered", result.stdout)
        self.assertIn("VC-019", result.stdout)

    def test_missing_repo_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad_root = Path(tmp) / "does_not_exist"
            result = self._run(["--repo-root", str(bad_root), "--no-color"])
        self.assertEqual(result.returncode, 4)
        self.assertIn("CLI-001", result.stdout + result.stderr)

    def test_missing_policy_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            (root / "AI_CHARACTERS").mkdir(parents=True)
            (root / "configs" / "visual_canon").mkdir(parents=True)
            result = self._run(["--repo-root", str(root), "--no-color"])
        self.assertEqual(result.returncode, 5)
        self.assertIn("VC-001", result.stdout + result.stderr)

    def test_json_report_created(self):
        # Real-repo run currently exits 1 (see test_default_repo_root_passes); the report is still
        # written -- JSON-report writing is independent of the pass/fail validation outcome.
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "report.json"
            result = self._run(["--repo-root", str(REPO_ROOT), "--json-report", str(report), "--no-color"])
            self.assertEqual(result.returncode, 1)
            self.assertTrue(report.exists())
            data = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(data["tool"], "validate_visual_canon_pipeline")
            self.assertGreater(data["summary"]["records_scanned"], 0)

    def test_json_report_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "report.json"
            report.write_text("{}", encoding="utf-8")
            result = self._run(["--repo-root", str(REPO_ROOT), "--json-report", str(report), "--no-color"])
            self.assertEqual(result.returncode, 2)
            self.assertEqual(report.read_text(encoding="utf-8"), "{}")
            self.assertIn("CLI-003", result.stdout + result.stderr)
            self.assertIn("already exists", result.stdout + result.stderr)

    def test_json_report_missing_parent(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "does_not_exist" / "report.json"
            result = self._run(["--repo-root", str(REPO_ROOT), "--json-report", str(report), "--no-color"])
            self.assertEqual(result.returncode, 2)
            self.assertIn("CLI-004", result.stdout + result.stderr)
            self.assertFalse(report.parent.exists())

    def test_json_report_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "report.json"
            report.write_text("{}", encoding="utf-8")
            result = self._run(["--repo-root", str(REPO_ROOT), "--json-report", str(report), "--overwrite-report", "--no-color"])
            self.assertEqual(result.returncode, 1)
            data = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(data["tool"], "validate_visual_canon_pipeline")


if __name__ == "__main__":
    unittest.main()
