import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from deploy_test_support import Repo, TOOL, load_tool


class CLI(unittest.TestCase):
    def invoke(self, *args):
        return subprocess.run([sys.executable, str(TOOL), *args], capture_output=True, text=True, encoding="utf-8")

    def test_help(self):
        self.assertEqual(self.invoke("--help").returncode, 0)

    def test_version(self):
        process = self.invoke("--version")
        self.assertEqual(process.returncode, 0)
        self.assertIn("1.0.1", process.stdout)

    def test_missing_request(self):
        self.assertEqual(self.invoke().returncode, 2)

    def test_malformed_json(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            root.mkdir()
            (root / ".git").mkdir()
            request = Path(directory) / "request.json"
            request.write_text("{", encoding="utf-8")
            self.assertEqual(self.invoke("--request", str(request), "--repo-root", str(root)).returncode, 2)

    def test_forbidden_flags_absent(self):
        help_text = self.invoke("--help").stdout
        for flag in ["--stage", "--commit", "--push", "--force", "--skip-validator", "--skip-lfs", "--allow-existing-output"]:
            self.assertNotIn(flag, help_text)

    def test_unknown_top_field(self):
        module = load_tool()
        with self.assertRaises(module.DeployError):
            module.validate_request({"bad": 1})

    def test_unknown_nested_field(self):
        module = load_tool()
        repo = Repo()
        try:
            request = repo.clone_request()
            request["prompt_linkage"]["bad"] = 1
            with self.assertRaises(module.DeployError):
                module.validate_request(request)
        finally:
            repo.close()

    def test_wrong_nested_type(self):
        module = load_tool()
        repo = Repo()
        try:
            request = repo.clone_request()
            request["updates"]["reference_presets"] = []
            with self.assertRaises(module.DeployError):
                module.validate_request(request)
        finally:
            repo.close()

    def test_boolean_not_integer(self):
        module = load_tool()
        repo = Repo()
        try:
            request = repo.clone_request()
            request["test_number"] = True
            with self.assertRaises(module.DeployError):
                module.validate_request(request)
        finally:
            repo.close()

    def test_invalid_sha_shape(self):
        module = load_tool()
        repo = Repo()
        try:
            request = repo.clone_request()
            request["source_image_sha256"] = "bad"
            with self.assertRaises(module.DeployError):
                module.validate_request(request)
        finally:
            repo.close()

    def test_schema_parses_without_duplicate_keys(self):
        path = TOOL.parents[1] / "configs" / "visual_canon" / "deployment_request.schema.json"
        duplicates = []

        def hook(pairs):
            result = {}
            for key, value in pairs:
                if key in result:
                    duplicates.append(key)
                result[key] = value
            return result

        json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)
        self.assertEqual(duplicates, [])

    def test_external_report_and_overwrite_refusal(self):
        module = load_tool()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            root.mkdir()
            output = Path(directory) / "report.json"
            module.report(str(output), root, {"ok": True}, False)
            self.assertTrue(output.exists())
            with self.assertRaises(module.DeployError) as caught:
                module.report(str(output), root, {"ok": True}, False)
            self.assertEqual(caught.exception.status, 2)

    def test_report_inside_repo_rejected(self):
        module = load_tool()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            root.mkdir()
            with self.assertRaises(module.DeployError):
                module.report(str(root / "report.json"), root, {}, False)

    def test_missing_report_parent(self):
        module = load_tool()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            root.mkdir()
            with self.assertRaises(module.DeployError):
                module.report(str(Path(directory) / "missing" / "report.json"), root, {}, False)

    def test_source_has_no_forbidden_authority(self):
        text = TOOL.read_text(encoding="utf-8")
        for token in ["sqlite3", "git add", "git commit", "git push", "shutil.move", "shell=True", "os.system"]:
            self.assertNotIn(token, text)


if __name__ == "__main__":
    unittest.main()
