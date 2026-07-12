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
        # The real repo should pass in compatibility mode (it has no prompt_run_log files).
        result = self._run(["--no-color"])
        self.assertEqual(result.returncode, 0)

    def test_missing_repo_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad_root = Path(tmp) / "does_not_exist"
            result = self._run(["--repo-root", str(bad_root), "--no-color"])
        self.assertEqual(result.returncode, 4)
        self.assertIn("VC-001", result.stdout + result.stderr)

    def test_missing_policy_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            (root / "AI_CHARACTERS").mkdir(parents=True)
            (root / "configs" / "visual_canon").mkdir(parents=True)
            result = self._run(["--repo-root", str(root), "--no-color"])
        self.assertEqual(result.returncode, 5)
        self.assertIn("VC-002", result.stdout + result.stderr)

    def test_json_report_created(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "report.json"
            result = self._run(["--repo-root", str(REPO_ROOT), "--json-report", str(report), "--no-color"])
            self.assertEqual(result.returncode, 0)
            self.assertTrue(report.exists())
            data = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(data["tool"], "validate_visual_canon_pipeline")

    def test_json_report_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "report.json"
            report.write_text("{}", encoding="utf-8")
            result = self._run(["--repo-root", str(REPO_ROOT), "--json-report", str(report), "--no-color"])
            self.assertEqual(result.returncode, 0)
            self.assertEqual(report.read_text(encoding="utf-8"), "{}")
            self.assertIn("already exists", result.stdout + result.stderr)

    def test_json_report_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "report.json"
            report.write_text("{}", encoding="utf-8")
            result = self._run(["--repo-root", str(REPO_ROOT), "--json-report", str(report), "--overwrite-report", "--no-color"])
            self.assertEqual(result.returncode, 0)
            data = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(data["tool"], "validate_visual_canon_pipeline")


if __name__ == "__main__":
    unittest.main()
