import json
import os
import re
import unittest
from pathlib import Path

from deploy_test_support import Repo, load_tool, run, sha


class Rollback(unittest.TestCase):
    def setUp(self):
        self.module = load_tool()
        self.repo = Repo()

    def tearDown(self):
        self.repo.close()

    def prepared(self, request=None):
        request = request or self.repo.request
        contract = self.module.resolve_contract(self.repo.root, request)
        hashes = self.module.exact_hashes(self.repo.root, request, contract)
        changes, _ = self.module.prepare(self.repo.root, request, self.repo.source, contract)
        return request, contract, hashes, changes

    def attempt_after(self, rel, request=None):
        request, contract, hashes, changes = self.prepared(request)
        before = {path: sha(self.repo.root / path) for path in hashes}

        def hook(event, current):
            if event == "after_replace" and current == rel:
                raise RuntimeError("injected failure")

        with self.assertRaises(self.module.DeployError) as caught:
            self.module.transaction(
                self.repo.root, request, changes, hashes, self.repo.source, contract,
                post_validator=lambda *_: None, event_hook=hook,
            )
        self.assertEqual(caught.exception.status, 4)
        self.assertFalse((self.repo.root / self.repo.out).exists())
        self.assertEqual(before, {path: sha(self.repo.root / path) for path in hashes})
        self.assertEqual(run(["git", "status", "--porcelain", "--untracked-files=no"], self.repo.root).stdout, "")

    def test_failure_after_destination_rolls_back(self):
        self.attempt_after(self.repo.out)

    def test_failure_after_registry_rolls_back(self):
        self.attempt_after(self.repo.rel(self.repo.registry))

    def test_failure_after_results_rolls_back(self):
        self.attempt_after(self.repo.rel(self.repo.results))

    def test_failure_after_presets_rolls_back(self):
        self.attempt_after(self.repo.rel(self.repo.presets))

    def test_failure_after_canon_rolls_back(self):
        request = self.repo.approve_as_canon(self.repo.clone_request())
        self.attempt_after(self.repo.rel(self.repo.canon), request)

    def test_character_post_validator_failure_rolls_back(self):
        request, contract, hashes, changes = self.prepared()
        before = sha(self.repo.registry)

        def character_failure(*_):
            raise self.module.DeployError(1, "DEPLOY-VALIDATOR-001", "character validator failed")

        with self.assertRaises(self.module.DeployError) as caught:
            self.module.transaction(self.repo.root, request, changes, hashes, self.repo.source, contract, post_validator=character_failure)
        self.assertEqual(caught.exception.status, 4)
        self.assertEqual(before, sha(self.repo.registry))

    def test_full_post_validator_failure_rolls_back(self):
        request, contract, hashes, changes = self.prepared()
        source_hash = sha(self.repo.source)

        def full_failure(*_):
            raise RuntimeError("full validator failed")

        with self.assertRaises(self.module.DeployError):
            self.module.transaction(self.repo.root, request, changes, hashes, self.repo.source, contract, post_validator=full_failure)
        self.assertEqual(source_hash, sha(self.repo.source))
        self.assertFalse((self.repo.root / self.repo.out).exists())

    def test_incomplete_rollback_retains_manifest(self):
        request, contract, hashes, changes = self.prepared()
        registry_rel = self.repo.rel(self.repo.registry)

        def hook(event, rel):
            if event == "after_replace" and rel == registry_rel:
                raise RuntimeError("apply failure")

        def broken_restore(source, destination):
            if str(destination).endswith("TESTX_PROMPT_RUN_LOG.jsonl"):
                raise OSError("restore blocked")
            os.replace(source, destination)

        with self.assertRaises(self.module.DeployError) as caught:
            self.module.transaction(
                self.repo.root, request, changes, hashes, self.repo.source, contract,
                post_validator=lambda *_: None, event_hook=hook, rollback_replace=broken_restore,
            )
        self.assertEqual(caught.exception.code, "DEPLOY-TXN-003")
        match = re.search(r"rollback incomplete: (.+recovery_manifest\.json)", caught.exception.message)
        self.assertIsNotNone(match)
        manifest = Path(match.group(1))
        self.assertTrue(manifest.exists())
        state = json.loads(manifest.read_text(encoding="utf-8"))
        self.assertEqual(state["status"], "ROLLBACK_INCOMPLETE")
        self.assertTrue(state["incomplete_steps"])


if __name__ == "__main__":
    unittest.main()
