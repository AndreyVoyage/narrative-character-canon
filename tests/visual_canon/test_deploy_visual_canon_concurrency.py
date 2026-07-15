import unittest

from deploy_test_support import Repo, load_tool, run, sha


class Concurrency(unittest.TestCase):
    def setUp(self):
        self.module = load_tool()
        self.repo = Repo()

    def tearDown(self):
        self.repo.close()

    def prepared(self):
        contract = self.module.resolve_contract(self.repo.root, self.repo.request)
        hashes = self.module.exact_hashes(self.repo.root, self.repo.request, contract)
        changes, _ = self.module.prepare(self.repo.root, self.repo.request, self.repo.source, contract)
        return contract, hashes, changes

    def transaction_with_hook(self, hook):
        contract, hashes, changes = self.prepared()
        return self.module.transaction(
            self.repo.root, self.repo.request, changes, hashes, self.repo.source, contract,
            post_validator=lambda *_: None, event_hook=hook,
        )

    def test_head_change_before_transaction(self):
        def hook(event, _rel):
            if event == "before_second_preconditions":
                self.repo.index.write_text("changed", encoding="utf-8")
                run(["git", "add", self.repo.rel(self.repo.index)], self.repo.root)
                run(["git", "commit", "-m", "concurrent"], self.repo.root)
        with self.assertRaises(self.module.DeployError) as caught:
            self.transaction_with_hook(hook)
        self.assertEqual(caught.exception.code, "DEPLOY-GIT-007")
        self.assertFalse((self.repo.root / self.repo.out).exists())

    def test_tracked_change_before_transaction(self):
        def hook(event, _rel):
            if event == "before_second_preconditions":
                self.repo.results.write_text("changed", encoding="utf-8")
        with self.assertRaises(self.module.DeployError) as caught:
            self.transaction_with_hook(hook)
        self.assertEqual(caught.exception.code, "DEPLOY-GIT-010")

    def test_staged_change_before_transaction(self):
        def hook(event, _rel):
            if event == "before_second_preconditions":
                self.repo.results.write_text("changed", encoding="utf-8")
                run(["git", "add", self.repo.rel(self.repo.results)], self.repo.root)
        with self.assertRaises(self.module.DeployError) as caught:
            self.transaction_with_hook(hook)
        self.assertEqual(caught.exception.code, "DEPLOY-GIT-009")

    def test_registry_hash_change_before_mutation(self):
        def hook(event, _rel):
            if event == "before_first_mutation":
                self.repo.registry.write_text("changed", encoding="utf-8")
        with self.assertRaises(self.module.DeployError):
            self.transaction_with_hook(hook)
        self.assertFalse((self.repo.root / self.repo.out).exists())

    def test_prompt_index_hash_change_before_mutation(self):
        def hook(event, _rel):
            if event == "before_first_mutation":
                self.repo.index.write_text("changed", encoding="utf-8")
        with self.assertRaises(self.module.DeployError):
            self.transaction_with_hook(hook)
        self.assertFalse((self.repo.root / self.repo.out).exists())

    def test_prompt_source_hash_change_before_mutation(self):
        def hook(event, _rel):
            if event == "before_first_mutation":
                self.repo.prompt.write_text("changed", encoding="utf-8")
        with self.assertRaises(self.module.DeployError):
            self.transaction_with_hook(hook)
        self.assertFalse((self.repo.root / self.repo.out).exists())

    def test_source_hash_change_before_mutation(self):
        def hook(event, _rel):
            if event == "before_first_mutation":
                self.repo.source.write_bytes(b"\x89PNG\r\n\x1a\nchanged")
        with self.assertRaises(self.module.DeployError) as caught:
            self.transaction_with_hook(hook)
        self.assertEqual(caught.exception.code, "DEPLOY-GIT-012")

    def test_destination_appears_before_mutation(self):
        def hook(event, _rel):
            if event == "before_first_mutation":
                path = self.repo.root / self.repo.out
                path.parent.mkdir(parents=True)
                path.write_bytes(b"other")
        with self.assertRaises(self.module.DeployError) as caught:
            self.transaction_with_hook(hook)
        self.assertEqual(caught.exception.code, "DEPLOY-GIT-015")

    def test_results_change_immediately_before_replacement(self):
        result_rel = self.repo.rel(self.repo.results)
        external = b"external late edit\n"

        def hook(event, rel):
            if event == "before_replace" and rel == result_rel:
                self.repo.results.write_bytes(external)
        with self.assertRaises(self.module.DeployError) as caught:
            self.transaction_with_hook(hook)
        self.assertEqual(caught.exception.status, 4)
        self.assertEqual(self.repo.results.read_bytes(), external)
        self.assertFalse((self.repo.root / self.repo.out).exists())

    def test_presets_change_immediately_before_replacement(self):
        presets_rel = self.repo.rel(self.repo.presets)
        external = b'{"external": true}\n'

        def hook(event, rel):
            if event == "before_replace" and rel == presets_rel:
                self.repo.presets.write_bytes(external)
        with self.assertRaises(self.module.DeployError):
            self.transaction_with_hook(hook)
        self.assertEqual(self.repo.presets.read_bytes(), external)
        self.assertFalse((self.repo.root / self.repo.out).exists())


if __name__ == "__main__":
    unittest.main()
