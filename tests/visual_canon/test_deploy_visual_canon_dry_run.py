import copy
import json
import unittest

from deploy_test_support import Repo, load_tool, run, sha


class DryRun(unittest.TestCase):
    def setUp(self):
        self.module = load_tool()
        self.repo = Repo()

    def tearDown(self):
        self.repo.close()

    def test_valid_public_cli_dry_run(self):
        process = self.repo.invoke()
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(json.loads(process.stdout)["status"], "DRY_RUN_VALID")

    def test_deterministic_public_cli_dry_run(self):
        first = self.repo.invoke()
        second = self.repo.invoke()
        self.assertEqual(first.stdout, second.stdout)

    def test_dry_run_no_mutation(self):
        before = self.repo.snapshot()
        process = self.repo.invoke()
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(before, self.repo.snapshot())

    def test_missing_approval(self):
        request = self.repo.clone_request()
        request["human_approval"] = False
        self.assertNotEqual(self.repo.invoke(request).returncode, 0)

    def test_empty_evidence(self):
        request = self.repo.clone_request()
        request["approval_evidence"] = []
        self.assertNotEqual(self.repo.invoke(request).returncode, 0)

    def test_evidence_missing_prompt_marker(self):
        request = self.repo.clone_request()
        request["approval_evidence"][0]["required_text"] = ["human_selected_and_approved"]
        self.assertNotEqual(self.repo.invoke(request).returncode, 0)

    def test_evidence_wrong_hash(self):
        request = self.repo.clone_request()
        request["approval_evidence"][0]["sha256"] = "0" * 64
        self.assertNotEqual(self.repo.invoke(request).returncode, 0)

    def test_wrong_head(self):
        request = self.repo.clone_request()
        request["expected_git_head"] = "0" * 40
        self.assertEqual(self.repo.invoke(request).returncode, 3)

    def test_dirty_tracked_tree(self):
        self.repo.index.write_text("dirty", encoding="utf-8")
        self.assertEqual(self.repo.invoke().returncode, 3)

    def test_staged_file(self):
        self.repo.index.write_text("dirty", encoding="utf-8")
        run(["git", "add", self.repo.rel(self.repo.index)], self.repo.root)
        self.assertEqual(self.repo.invoke().returncode, 3)

    def test_destination_collision(self):
        path = self.repo.root / self.repo.out
        path.parent.mkdir(parents=True)
        path.write_bytes(b"x")
        self.assertEqual(self.repo.invoke().returncode, 3)

    def test_source_hash_change(self):
        self.repo.source.write_bytes(b"\x89PNG\r\n\x1a\nchanged")
        self.assertEqual(self.repo.invoke().returncode, 3)

    def test_source_invalid_png(self):
        request = self.repo.clone_request()
        self.repo.source.write_bytes(b"not png")
        request["source_image_sha256"] = sha(self.repo.source)
        self.assertEqual(self.repo.invoke(request).returncode, 1)

    def test_rejected_record_cannot_be_approved(self):
        record = json.loads(self.repo.registry.read_text(encoding="utf-8"))
        record["verdict"] = "REJECTED"
        self.repo.registry.write_text(json.dumps(record) + "\n", encoding="utf-8")
        request = self.repo.clone_request()
        self.repo.refresh_hashes(request)
        self.assertNotEqual(self.repo.invoke(request).returncode, 0)


if __name__ == "__main__":
    unittest.main()
