#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unit tests for tools/bootstrap_character.py using temporary Git repositories.

Never modifies the real repository or AI_CHARACTERS/**.
"""

from __future__ import annotations

import datetime
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL = REPO_ROOT / "tools" / "bootstrap_character.py"

# Valid spec template reused across tests
VALID_SPEC = {
    "schema_version": "1.0",
    "character_id": "TESTX",
    "display_name": "Test Character X",
    "prompt_subject": "adult woman",
    "identity_anchor": "adult woman with test features",
    "style_direction": "neutral studio",
    "safety_rules": ["non-explicit only"],
    "next_step": "Generate face canon via DALL-E",
    "current_status": "TEXT_CANON_READY",
    "reference_preset_status": "PENDING — no approved images",
}


def run(cmd, cwd, env=None):
    return subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, encoding="utf-8", errors="replace", env=env or {})


def make_temp_repo():
    """Create a disposable Git repository with minimal NCC structure."""
    tmp = tempfile.TemporaryDirectory()
    root = Path(tmp.name) / "repo"
    root.mkdir()
    run(["git", "init", "-b", "main"], root)
    run(["git", "config", "user.email", "test@test.com"], root)
    run(["git", "config", "user.name", "Test"], root)

    # Required structure
    (root / "AI_CHARACTERS").mkdir()
    (root / "configs" / "visual_canon").mkdir(parents=True)
    (root / "tools").mkdir()
    (root / ".voyage").mkdir()

    # Copy real schema for spec validation
    schema_src = REPO_ROOT / "configs" / "visual_canon" / "character_bootstrap.schema.json"
    shutil.copy2(str(schema_src), str(root / "configs" / "visual_canon" / "character_bootstrap.schema.json"))

    # Create required existing files
    (root / ".voyage" / "CHARACTER_REGISTRY.md").write_text(
        "# CHARACTER_REGISTRY\n\n"
        "| Character | Folder | Current status | Reference preset status | Next step |\n"
        "|---|---|---|---|---|\n"
        "| EXISTING | `AI_CHARACTERS/EXISTING` | TEXT_CANON_READY | PENDING | Generate |\n\n"
        "## Правило\n",
        encoding="utf-8",
    )
    (root / ".voyage" / "DECISIONS.md").write_text("# DECISIONS\n\n", encoding="utf-8")
    (root / ".voyage" / "PROJECT_STATE.md").write_text(
        "# PROJECT_STATE\n\n* EXISTING: `TEXT_CANON_READY`\n\n## Активные ограничения\n\n* Rule\n",
        encoding="utf-8",
    )
    (root / ".voyage" / "CURRENT_TASK.md").write_text(
        "# CURRENT_TASK\n\n## Active task\n\nSome task\n",
        encoding="utf-8",
    )

    # Fake tools
    (root / "tools" / "generate_inventory.py").write_text(
        "import sys; print('inventory ok'); sys.exit(0)\n", encoding="utf-8"
    )
    (root / "tools" / "validate_visual_canon_pipeline.py").write_text(
        "import sys; print('validator ok'); sys.exit(0)\n", encoding="utf-8"
    )

    # Commit everything
    run(["git", "add", "."], root)
    run(["git", "commit", "-m", "initial"], root)

    return tmp, root


def write_spec(root, spec):
    """Write spec to a temporary JSON file and return its path."""
    spec_path = Path(root) / ".." / "test_spec.json"
    spec_path = Path(tempfile.mkdtemp()) / "test_spec.json"
    spec_path.write_text(json.dumps(spec), encoding="utf-8")
    return spec_path


def invoke_tool(repo_root, spec_path, *extra, expect_fail=False):
    """Invoke bootstrap_character.py and return CompletedProcess."""
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "NCC_TRANSACTION_ROOT": str(Path(tempfile.mkdtemp()))}
    cmd = [sys.executable, str(TOOL), "--spec", str(spec_path), "--repo-root", str(repo_root)] + list(extra)
    return subprocess.run(cmd, cwd=str(repo_root), capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)


class TestBootstrapCLI(unittest.TestCase):
    """Test CLI basics: --help, --version."""

    def test_version(self):
        result = invoke_tool(REPO_ROOT, Path(tempfile.mkdtemp()) / "dummy.json", "--version", expect_fail=True)
        # --version exits 0 before spec check
        self.assertIn("bootstrap_character.py", result.stdout)

    def test_help(self):
        result = subprocess.run(
            [sys.executable, str(TOOL), "--help"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("bootstrap", result.stdout.lower())


class TestBootstrapDryRun(unittest.TestCase):
    """Test dry-run behavior: no writes."""

    def test_dry_run_performs_no_writes(self):
        tmp, root = make_temp_repo()
        try:
            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path)
            if result.returncode != 0:
                self.fail(f"Dry-run failed: {result.stdout}\n{result.stderr}")
            self.assertIn("REPOSITORY_MODIFIED=NO", result.stdout)
            self.assertIn("Character ID: TESTX", result.stdout)
            self.assertIn("Planned directories:", result.stdout)
            self.assertIn("Planned files:", result.stdout)
            # Verify nothing was written
            char_dir = root / "AI_CHARACTERS" / "TESTX"
            self.assertFalse(char_dir.exists(), "Character directory should not exist after dry-run")
        finally:
            tmp.cleanup()


class TestBootstrapApply(unittest.TestCase):
    """Test apply mode: creates exact structure and files."""

    def test_apply_creates_folders_and_files(self):
        tmp, root = make_temp_repo()
        try:
            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path, "--apply")
            if result.returncode != 0:
                self.fail(f"Apply failed: {result.stdout}\n{result.stderr}")

            char_dir = root / "AI_CHARACTERS" / "TESTX"
            self.assertTrue(char_dir.is_dir())

            # Check canonical folders exist
            for folder in [
                "01_refs_raw", "02_best_refs",
                "03_face_sheet/expressions",
                "04_body_sheet/candidates",
                "05_outfits/casual", "05_outfits/formal", "05_outfits/evening_dress",
                "05_outfits/sports_look", "05_outfits/scene_outfits", "05_outfits/candidates",
                "06_prompts", "07_generated/canon_tests", "07_generated/drafts",
                "07_generated/rejected", "08_masks", "09_blender", "10_notes",
            ]:
                self.assertTrue(
                    (char_dir / folder).is_dir(),
                    f"Missing folder: {folder}",
                )

            # Check base files under 06_prompts
            for suffix in [
                "CANON_GENERATION_PROMPTS.txt",
                "PROMPT_INDEX.md",
                "WORKING_SCENE_PROMPTS.md",
                "PROMPT_RUN_LOG.jsonl",
            ]:
                path = char_dir / "06_prompts" / f"TESTX_{suffix}"
                self.assertTrue(path.is_file(), f"Missing file: {path}")

            # Check base files under 10_notes
            for suffix in [
                "IDENTITY_DRAFT.md",
                "CANON_INDEX.md",
                "TEST_RESULTS.md",
                "REFERENCE_PRESETS.json",
            ]:
                path = char_dir / "10_notes" / f"TESTX_{suffix}"
                self.assertTrue(path.is_file(), f"Missing file: {path}")

            # Check .gitkeep files exist
            for folder in [
                "01_refs_raw", "02_best_refs",
                "03_face_sheet/expressions",
                "04_body_sheet/candidates",
                "05_outfits/casual", "05_outfits/formal", "05_outfits/evening_dress",
                "05_outfits/sports_look", "05_outfits/scene_outfits", "05_outfits/candidates",
                "07_generated/canon_tests", "07_generated/drafts", "07_generated/rejected",
                "08_masks", "09_blender",
            ]:
                gitkeep = char_dir / folder / ".gitkeep"
                self.assertTrue(gitkeep.is_file(), f"Missing .gitkeep: {gitkeep}")
                self.assertEqual(gitkeep.read_text(encoding="utf-8"), "")

            # Check JSONL is empty
            jsonl = char_dir / "06_prompts" / "TESTX_PROMPT_RUN_LOG.jsonl"
            content = jsonl.read_text(encoding="utf-8").strip()
            self.assertEqual(content, "", "JSONL should be empty")

            # Check presets JSON parses
            presets = char_dir / "10_notes" / "TESTX_REFERENCE_PRESETS.json"
            preset_data = json.loads(presets.read_text(encoding="utf-8"))
            self.assertEqual(preset_data["character"], "TESTX")
            self.assertEqual(preset_data["control_tests"], [])
            self.assertEqual(preset_data["scene_presets"], {})

            # Verify registry was updated
            reg = (root / ".voyage" / "CHARACTER_REGISTRY.md").read_text(encoding="utf-8")
            self.assertIn("| TESTX |", reg)

            # Verify decisions updated
            dec = (root / ".voyage" / "DECISIONS.md").read_text(encoding="utf-8")
            self.assertIn("TESTX", dec)

            # Verify project state updated
            ps = (root / ".voyage" / "PROJECT_STATE.md").read_text(encoding="utf-8")
            self.assertIn("TESTX", ps)

            # Verify current task updated
            ct = (root / ".voyage" / "CURRENT_TASK.md").read_text(encoding="utf-8")
            self.assertIn("TESTX", ct)
            self.assertIn("COMPLETED_BOOTSTRAP", ct)
        finally:
            tmp.cleanup()

    def test_apply_preserves_protected_untracked(self):
        """Protected untracked paths must be left alone."""
        tmp, root = make_temp_repo()
        try:
            # Create protected untracked paths
            protected_files = {}
            for p in [".claude/", ".vscode/", "UNIFIED_CANON_TESTS_TEMPLATE.md", "repo_audit.txt"]:
                full = root / p
                if p.endswith("/"):
                    full.mkdir(parents=True, exist_ok=True)
                else:
                    full.parent.mkdir(parents=True, exist_ok=True)
                    full.write_text("protected content", encoding="utf-8")
                    protected_files[p] = full.read_bytes()

            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path, "--apply")
            if result.returncode != 0:
                self.fail(f"Apply failed: {result.stdout}\n{result.stderr}")

            # Verify protected paths preserved
            for p, expected_bytes in protected_files.items():
                full = root / p
                self.assertTrue(full.exists(), f"Protected path removed: {p}")
                self.assertEqual(full.read_bytes(), expected_bytes, f"Protected path modified: {p}")
        finally:
            tmp.cleanup()


class TestBootstrapValidation(unittest.TestCase):
    """Test spec validation rules."""

    def _make_repo_and_apply(self, tmp_spec, expected_rc=None):
        tmp, root = make_temp_repo()
        try:
            spec_path = write_spec(root, tmp_spec)
            result = invoke_tool(root, spec_path)
            if expected_rc is not None:
                self.assertNotEqual(result.returncode, 0, f"Expected non-zero exit for invalid spec: {result.stdout}")
            return tmp, root, result
        finally:
            tmp.cleanup()

    def test_invalid_id_pattern(self):
        """Reject character_id not matching ^[A-Z][A-Z0-9_]*$."""
        for bad_id in ["test", "TestX", "TEST X", "123TEST", "_TEST", "TEST-1", "testx"]:
            spec = dict(VALID_SPEC)
            spec["character_id"] = bad_id
            tmp, root = make_temp_repo()
            try:
                spec_path = write_spec(root, spec)
                result = invoke_tool(root, spec_path)
                self.assertNotEqual(result.returncode, 0, f"Should reject ID '{bad_id}': {result.stdout}")
            finally:
                tmp.cleanup()

    def test_case_insensitive_collision(self):
        """Reject namespace that collides case-insensitively."""
        spec = dict(VALID_SPEC)
        spec["character_id"] = "EXISTING"  # same as EXISTING in registry
        tmp, root = make_temp_repo()
        try:
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path)
            self.assertNotEqual(result.returncode, 0, f"Should reject case-insensitive collision: {result.stdout}")
        finally:
            tmp.cleanup()

    def test_existing_registry_row(self):
        """Reject character_id that already appears in the registry table."""
        spec = dict(VALID_SPEC)
        spec["character_id"] = "EXISTING"  # already in registry
        tmp, root = make_temp_repo()
        try:
            # Also create the actual directory to trigger the collision
            (root / "AI_CHARACTERS" / "EXISTING").mkdir(parents=True, exist_ok=True)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path)
            self.assertNotEqual(result.returncode, 0, f"Should reject existing registry row: {result.stdout}")
        finally:
            tmp.cleanup()

    def test_missing_required_fields(self):
        """Reject spec with missing fields."""
        for field in VALID_SPEC:
            spec = dict(VALID_SPEC)
            del spec[field]
            tmp, root = make_temp_repo()
            try:
                spec_path = write_spec(root, spec)
                result = invoke_tool(root, spec_path)
                self.assertNotEqual(
                    result.returncode, 0,
                    f"Should reject missing '{field}': {result.stdout}",
                )
            finally:
                tmp.cleanup()

    def test_blank_fields(self):
        """Reject blank/empty required fields."""
        for field in VALID_SPEC:
            if field == "safety_rules":
                continue  # tested separately
            if field == "schema_version":
                continue  # tested separately
            if field == "current_status":
                continue  # tested separately
            spec = dict(VALID_SPEC)
            spec[field] = ""
            tmp, root = make_temp_repo()
            try:
                spec_path = write_spec(root, spec)
                result = invoke_tool(root, spec_path)
                self.assertNotEqual(
                    result.returncode, 0,
                    f"Should reject blank '{field}': {result.stdout}",
                )
            finally:
                tmp.cleanup()

    def test_empty_safety_rules(self):
        """Reject empty safety_rules list."""
        spec = dict(VALID_SPEC)
        spec["safety_rules"] = []
        tmp, root = make_temp_repo()
        try:
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path)
            self.assertNotEqual(result.returncode, 0, f"Should reject empty safety_rules: {result.stdout}")
        finally:
            tmp.cleanup()

    def test_placeholder_values(self):
        """Reject placeholder values like TODO, TBD, etc."""
        for placeholder in ["TODO", "TBD", "placeholder", "FIXME"]:
            spec = dict(VALID_SPEC)
            spec["identity_anchor"] = f"Some {placeholder} text"
            tmp, root = make_temp_repo()
            try:
                spec_path = write_spec(root, spec)
                result = invoke_tool(root, spec_path)
                self.assertNotEqual(
                    result.returncode, 0,
                    f"Should reject placeholder '{placeholder}': {result.stdout}",
                )
            finally:
                tmp.cleanup()

    def test_invalid_current_status(self):
        """Reject current_status outside allowed enum."""
        spec = dict(VALID_SPEC)
        spec["current_status"] = "UNKNOWN_STATUS"
        tmp, root = make_temp_repo()
        try:
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path)
            self.assertNotEqual(result.returncode, 0, f"Should reject bad status: {result.stdout}")
        finally:
            tmp.cleanup()

    def test_invalid_schema_version(self):
        """Reject schema_version != '1.0'."""
        spec = dict(VALID_SPEC)
        spec["schema_version"] = "2.0"
        tmp, root = make_temp_repo()
        try:
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path)
            self.assertNotEqual(result.returncode, 0, f"Should reject bad schema_version: {result.stdout}")
        finally:
            tmp.cleanup()

    def test_unknown_field(self):
        """Reject spec with unknown fields."""
        spec = dict(VALID_SPEC)
        spec["unknown_field"] = "value"
        tmp, root = make_temp_repo()
        try:
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path)
            self.assertNotEqual(result.returncode, 0, f"Should reject unknown field: {result.stdout}")
        finally:
            tmp.cleanup()

    def test_markdown_table_break_characters(self):
        """Reject spec with Markdown-table-breaking characters."""
        for ch in ["|", "\n"]:
            spec = dict(VALID_SPEC)
            spec["display_name"] = f"Bad{ch}Name"
            tmp, root = make_temp_repo()
            try:
                spec_path = write_spec(root, spec)
                result = invoke_tool(root, spec_path)
                self.assertNotEqual(
                    result.returncode, 0,
                    f"Should reject char {repr(ch)} in display_name: {result.stdout}",
                )
            finally:
                tmp.cleanup()


class TestBootstrapPreflight(unittest.TestCase):
    """Test preflight checks: dirty tree, staged changes, wrong branch, unexpected untracked."""

    def test_dirty_tracked_tree_rejected(self):
        tmp, root = make_temp_repo()
        try:
            # Create a tracked file modification
            (root / ".voyage" / "DECISIONS.md").write_text("# Modified\n", encoding="utf-8")
            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path)
            self.assertNotEqual(result.returncode, 0, f"Should reject dirty tree: {result.stdout}")
        finally:
            tmp.cleanup()

    def test_staged_changes_rejected(self):
        tmp, root = make_temp_repo()
        try:
            (root / ".voyage" / "DECISIONS.md").write_text("# Staged\n", encoding="utf-8")
            run(["git", "add", ".voyage/DECISIONS.md"], root)
            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path)
            self.assertNotEqual(result.returncode, 0, f"Should reject staged changes: {result.stdout}")
        finally:
            tmp.cleanup()

    def test_wrong_branch_rejected(self):
        tmp, root = make_temp_repo()
        try:
            run(["git", "checkout", "-b", "other"], root)
            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path)
            self.assertNotEqual(result.returncode, 0, f"Should reject non-main branch: {result.stdout}")
        finally:
            tmp.cleanup()

    def test_head_not_matching_origin(self):
        """When origin/main exists and HEAD diverges, preflight should reject."""
        tmp, root = make_temp_repo()
        try:
            # Add a remote so origin/main exists
            remote_dir = Path(tmp.name) / "remote"
            remote_dir.mkdir()
            run(["git", "init", "-b", "main", "--bare"], remote_dir)
            run(["git", "remote", "add", "origin", str(remote_dir)], root)
            run(["git", "push", "-u", "origin", "main"], root)
            # Now HEAD == origin/main. Make a diverging commit.
            (root / "extra.txt").write_text("diverging", encoding="utf-8")
            run(["git", "add", "."], root)
            run(["git", "commit", "-m", "diverging"], root)
            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path)
            self.assertNotEqual(result.returncode, 0, f"Should reject diverged HEAD: {result.stdout}")
        finally:
            tmp.cleanup()

    def test_unexpected_untracked_rejected(self):
        tmp, root = make_temp_repo()
        try:
            (root / "unexpected_untracked_file.txt").write_text("unexpected", encoding="utf-8")
            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path)
            self.assertNotEqual(result.returncode, 0, f"Should reject unexpected untracked: {result.stdout}")
        finally:
            tmp.cleanup()

    def test_protected_untracked_allowed(self):
        """Protected untracked paths (.claude/, .vscode/, etc.) are allowed."""
        tmp, root = make_temp_repo()
        try:
            for p in [".claude/", ".vscode/", "UNIFIED_CANON_TESTS_TEMPLATE.md", "repo_audit.txt"]:
                full = root / p
                if p.endswith("/"):
                    full.mkdir(parents=True, exist_ok=True)
                else:
                    full.parent.mkdir(parents=True, exist_ok=True)
                    full.write_text("ok", encoding="utf-8")
            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path)
            self.assertEqual(result.returncode, 0, f"Should allow protected untracked: {result.stdout}\n{result.stderr}")
        finally:
            tmp.cleanup()


class TestBootstrapRollback(unittest.TestCase):
    """Test rollback behavior on failure."""

    def test_validator_failure_rolls_back(self):
        tmp, root = make_temp_repo()
        try:
            # Make validator fail
            validator = root / "tools" / "validate_visual_canon_pipeline.py"
            validator.write_text("import sys; sys.exit(1)\n", encoding="utf-8")

            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path, "--apply")
            self.assertNotEqual(result.returncode, 0, f"Should fail on validator error: {result.stdout}")

            # Character directory should be rolled back
            char_dir = root / "AI_CHARACTERS" / "TESTX"
            self.assertFalse(char_dir.exists(), "Character directory should be rolled back")

            # Voyage files should be restored
            dec = (root / ".voyage" / "DECISIONS.md").read_text(encoding="utf-8")
            self.assertNotIn("TESTX", dec, "DECISIONS.md should be restored")
        finally:
            tmp.cleanup()

    def test_inventory_failure_rolls_back(self):
        tmp, root = make_temp_repo()
        try:
            inv = root / "tools" / "generate_inventory.py"
            inv.write_text("import sys; sys.exit(1)\n", encoding="utf-8")

            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path, "--apply")
            self.assertNotEqual(result.returncode, 0)

            char_dir = root / "AI_CHARACTERS" / "TESTX"
            self.assertFalse(char_dir.exists(), "Character directory should be rolled back")
        finally:
            tmp.cleanup()


class TestBootstrapNoStageCommitPush(unittest.TestCase):
    """Verify the tool never stages, commits, or pushes."""

    def test_apply_leaves_changes_unstaged(self):
        tmp, root = make_temp_repo()
        try:
            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path, "--apply")
            if result.returncode != 0:
                self.fail(f"Apply failed: {result.stdout}\n{result.stderr}")

            # Check nothing is staged
            staged = run(["git", "diff", "--cached", "--name-only"], root).stdout.strip()
            self.assertEqual(staged, "", f"Nothing should be staged, got: {staged}")

            # Check there are untracked changes (the new character)
            status = run(["git", "status", "--short"], root).stdout
            self.assertIn("??", status, "New character files should be untracked")

            # Verify we didn't commit
            log = run(["git", "log", "--oneline", "-1"], root).stdout
            self.assertIn("initial", log, "Should not have a new commit")
        finally:
            tmp.cleanup()


class TestBootstrapConcurrency(unittest.TestCase):
    """Test concurrent-modification detection."""

    def test_concurrent_target_hash_change_blocks(self):
        """Test that recheck_preflight correctly detects hash changes."""
        # Import the tool's recheck function directly
        import importlib.util
        spec_mod = importlib.util.spec_from_file_location("bootstrap_char", str(TOOL))
        bootstrap_module = importlib.util.module_from_spec(spec_mod)
        spec_mod.loader.exec_module(bootstrap_module)

        tmp, root = make_temp_repo()
        try:
            head = run(["git", "rev-parse", "HEAD"], root).stdout.strip()
            hashes = {
                ".voyage/CHARACTER_REGISTRY.md": bootstrap_module.sha256_path(root / ".voyage" / "CHARACTER_REGISTRY.md"),
            }
            # Modify a tracked file
            (root / ".voyage" / "CHARACTER_REGISTRY.md").write_text("# CHANGED\n", encoding="utf-8")
            errors = bootstrap_module.recheck_preflight(root, head, hashes)
            self.assertTrue(len(errors) > 0, "Should detect hash change")
            self.assertIn("CHARACTER_REGISTRY.md", errors[0])
        finally:
            tmp.cleanup()


class TestBootstrapFileContentIntegrity(unittest.TestCase):
    """Verify generated file content."""

    def test_canon_generation_prompts_content(self):
        tmp, root = make_temp_repo()
        try:
            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path, "--apply")
            if result.returncode != 0:
                self.fail(f"Apply failed: {result.stdout}\n{result.stderr}")

            prompts = (root / "AI_CHARACTERS" / "TESTX" / "06_prompts" / "TESTX_CANON_GENERATION_PROMPTS.txt").read_text(encoding="utf-8")
            self.assertIn("TESTX", prompts)
            self.assertIn(spec["identity_anchor"], prompts)
            self.assertIn(spec["prompt_subject"], prompts)
            self.assertIn("Face Canon Sheet Prompt", prompts)
            self.assertIn("Expression Canon Sheet Prompt", prompts)
            self.assertIn("Body Canon Sheet Prompt", prompts)
            self.assertIn("Body Pose Variations Prompt", prompts)
            self.assertIn("PENDING / NOT_STARTED", prompts)
        finally:
            tmp.cleanup()

    def test_reference_presets_has_empty_arrays(self):
        tmp, root = make_temp_repo()
        try:
            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path, "--apply")
            if result.returncode != 0:
                self.fail(f"Apply failed: {result.stdout}\n{result.stderr}")

            presets_path = root / "AI_CHARACTERS" / "TESTX" / "10_notes" / "TESTX_REFERENCE_PRESETS.json"
            data = json.loads(presets_path.read_text(encoding="utf-8"))
            self.assertEqual(data["control_tests"], [], "control_tests should be empty list")
            self.assertEqual(data["scene_presets"], {}, "scene_presets should be empty dict")
            self.assertEqual(data["status"], "PENDING — no approved images")
            self.assertIn("safety_rules", data)
            self.assertEqual(data["safety_rules"], spec["safety_rules"])
        finally:
            tmp.cleanup()

    def test_jsonl_is_empty(self):
        tmp, root = make_temp_repo()
        try:
            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path, "--apply")
            if result.returncode != 0:
                self.fail(f"Apply failed: {result.stdout}\n{result.stderr}")

            jsonl_path = root / "AI_CHARACTERS" / "TESTX" / "06_prompts" / "TESTX_PROMPT_RUN_LOG.jsonl"
            content = jsonl_path.read_text(encoding="utf-8").strip()
            self.assertEqual(content, "", "JSONL must be empty (zero generation attempts)")
        finally:
            tmp.cleanup()

    def test_identity_draft_content(self):
        tmp, root = make_temp_repo()
        try:
            spec = dict(VALID_SPEC)
            spec_path = write_spec(root, spec)
            result = invoke_tool(root, spec_path, "--apply")
            if result.returncode != 0:
                self.fail(f"Apply failed: {result.stdout}\n{result.stderr}")

            identity = (root / "AI_CHARACTERS" / "TESTX" / "10_notes" / "TESTX_IDENTITY_DRAFT.md").read_text(encoding="utf-8")
            self.assertIn(spec["display_name"], identity)
            self.assertIn(spec["identity_anchor"], identity)
            self.assertIn(spec["style_direction"], identity)
        finally:
            tmp.cleanup()


if __name__ == "__main__":
    unittest.main()