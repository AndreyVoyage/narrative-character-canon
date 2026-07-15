import json
import unittest

from deploy_test_support import Repo, run, sha


class Apply(unittest.TestCase):
    def setUp(self):
        self.repo = Repo()

    def tearDown(self):
        self.repo.close()

    def apply(self, request=None):
        return self.repo.invoke(request, "--apply")

    def test_successful_public_cli_apply(self):
        process = self.apply()
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(json.loads(process.stdout)["status"], "APPLIED")

    def test_source_unchanged(self):
        before = sha(self.repo.source)
        self.assertEqual(self.apply().returncode, 0)
        self.assertEqual(before, sha(self.repo.source))

    def test_destination_hash(self):
        self.assertEqual(self.apply().returncode, 0)
        self.assertEqual(sha(self.repo.source), sha(self.repo.root / self.repo.out))

    def test_one_record_no_append(self):
        before_count = len(self.repo.registry.read_text(encoding="utf-8").splitlines())
        self.assertEqual(self.apply().returncode, 0)
        self.assertEqual(before_count, len(self.repo.registry.read_text(encoding="utf-8").splitlines()))

    def test_target_record_fields(self):
        self.assertEqual(self.apply().returncode, 0)
        record = json.loads(self.repo.registry.read_text(encoding="utf-8"))
        self.assertTrue(record["selected"])
        self.assertTrue(record["human_approval"])
        self.assertTrue(record["deployed"])
        self.assertEqual(record["output_path"], self.repo.out)

    def test_result_and_preset_inserted_once(self):
        self.assertEqual(self.apply().returncode, 0)
        self.assertEqual(self.repo.results.read_text(encoding="utf-8").count("TEST10 ENTRY"), 1)
        document = json.loads(self.repo.presets.read_text(encoding="utf-8"))
        self.assertEqual(document["scene_presets"]["scene"]["selected_prompt_id"], self.repo.pid)

    def test_canon_unchanged_for_test_verdict(self):
        before = sha(self.repo.canon)
        self.assertEqual(self.apply().returncode, 0)
        self.assertEqual(before, sha(self.repo.canon))

    def test_canon_updated_for_canon_verdict(self):
        request = self.repo.approve_as_canon(self.repo.clone_request())
        self.assertEqual(self.apply(request).returncode, 0)
        self.assertEqual(self.repo.canon.read_text(encoding="utf-8").count("CANON ENTRY"), 1)

    def test_exact_dirty_file_set(self):
        self.assertEqual(self.apply().returncode, 0)
        status = run(["git", "status", "--short"], self.repo.root).stdout
        for path in [self.repo.registry, self.repo.results, self.repo.presets]:
            self.assertIn(self.repo.rel(path), status)
        self.assertIn("07_generated/", status)
        self.assertNotIn("INVENTORY", status)

    def test_nothing_staged_and_head_unchanged(self):
        head = run(["git", "rev-parse", "HEAD"], self.repo.root).stdout
        self.assertEqual(self.apply().returncode, 0)
        self.assertEqual(run(["git", "diff", "--cached", "--name-only"], self.repo.root).stdout, "")
        self.assertEqual(head, run(["git", "rev-parse", "HEAD"], self.repo.root).stdout)


if __name__ == "__main__":
    unittest.main()
