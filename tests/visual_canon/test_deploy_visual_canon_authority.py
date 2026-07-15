import copy
import json
import os
import unittest
from pathlib import Path

from deploy_test_support import Repo, load_tool, run, sha


class Authority(unittest.TestCase):
    def setUp(self):
        self.module = load_tool()
        self.repo = Repo()

    def tearDown(self):
        self.repo.close()

    def add_tracked(self, relative_path, content="ANCHOR\n"):
        path = self.repo.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        run(["git", "add", "--", relative_path], self.repo.root)
        run(["git", "commit", "-m", "fixture"], self.repo.root)
        self.repo.request["expected_git_head"] = run(["git", "rev-parse", "HEAD"], self.repo.root).stdout.strip()
        return path

    def assert_cli_rejected_without_mutation(self, request, protected=None):
        before = self.repo.snapshot()
        protected_hash = sha(protected) if protected else None
        head = run(["git", "rev-parse", "HEAD"], self.repo.root).stdout
        process = self.repo.invoke(request, "--apply")
        self.assertNotEqual(process.returncode, 0, process.stdout)
        self.assertRegex(process.stderr, r"\[DEPLOY-(?:AUTH|GIT|LINK|REQ)-[0-9]+\]")
        self.assertEqual(before, self.repo.snapshot())
        if protected:
            self.assertEqual(protected_hash, sha(protected))
        self.assertFalse((self.repo.root / self.repo.out).exists())
        self.assertEqual(run(["git", "diff", "--cached", "--name-only"], self.repo.root).stdout, "")
        self.assertEqual(head, run(["git", "rev-parse", "HEAD"], self.repo.root).stdout)

    def test_original_inventory_alias_exploit_rejected(self):
        inventory = self.add_tracked("INVENTORY.md", "# Inventory\nANCHOR_INV\n")
        request = self.repo.clone_request()
        request["expected_git_head"] = self.repo.request["expected_git_head"]
        request["updates"]["test_results"] = {
            "path": "INVENTORY.md", "unique_anchor": "ANCHOR_INV", "entry_markdown": "UNAUTHORIZED"
        }
        self.assert_cli_rejected_without_mutation(request, inventory)

    def test_test_results_prompt_index_alias_rejected(self):
        request = self.repo.clone_request()
        request["updates"]["test_results"]["path"] = self.repo.rel(self.repo.index)
        self.assert_cli_rejected_without_mutation(request, self.repo.index)

    def test_test_results_prompt_source_backslash_alias_rejected(self):
        request = self.repo.clone_request()
        request["updates"]["test_results"]["path"] = self.repo.rel(self.repo.prompt).replace("/", "\\")
        self.assert_cli_rejected_without_mutation(request, self.repo.prompt)

    def test_test_results_forbidden_root_aliases_rejected(self):
        fixtures = {
            ".voyage/CURRENT_TASK.md": "ANCHOR\n",
            "docs/x.md": "ANCHOR\n",
            "configs/x.md": "ANCHOR\n",
            "tests/x.md": "ANCHOR\n",
            "state.sqlite": "ANCHOR\n",
        }
        for path, content in fixtures.items():
            self.add_tracked(path, content)
        for path in fixtures:
            with self.subTest(path=path):
                request = self.repo.clone_request()
                request["expected_git_head"] = self.repo.request["expected_git_head"]
                request["updates"]["test_results"] = {"path": path, "unique_anchor": "ANCHOR", "entry_markdown": "BAD"}
                self.assert_cli_rejected_without_mutation(request, self.repo.root / path)

    def test_presets_unrelated_json_alias_rejected(self):
        other = self.add_tracked("AI_CHARACTERS/TESTX/10_notes/OTHER.json", "{}\n")
        request = self.repo.clone_request()
        request["expected_git_head"] = self.repo.request["expected_git_head"]
        request["updates"]["reference_presets"]["path"] = self.repo.rel(other)
        self.assert_cli_rejected_without_mutation(request, other)

    def test_canon_unrelated_markdown_alias_rejected(self):
        other = self.add_tracked("AI_CHARACTERS/TESTX/10_notes/OTHER.md", "ANCHOR\n")
        request = self.repo.approve_as_canon(self.repo.clone_request())
        request["expected_git_head"] = self.repo.request["expected_git_head"]
        request["updates"]["canon_index"]["path"] = self.repo.rel(other)
        self.assert_cli_rejected_without_mutation(request, other)

    def test_registry_unrelated_jsonl_alias_rejected(self):
        other = self.add_tracked("AI_CHARACTERS/TESTX/06_prompts/OTHER.jsonl", "{}\n")
        request = self.repo.clone_request()
        request["expected_git_head"] = self.repo.request["expected_git_head"]
        request["updates"]["prompt_record"]["registry_path"] = self.repo.rel(other)
        self.assert_cli_rejected_without_mutation(request, other)

    def test_cross_character_test_results_rejected(self):
        other = self.add_tracked("AI_CHARACTERS/OTHER/10_notes/OTHER_TEST_RESULTS.md", "ANCHOR\n")
        request = self.repo.clone_request()
        request["expected_git_head"] = self.repo.request["expected_git_head"]
        request["updates"]["test_results"]["path"] = self.repo.rel(other)
        self.assert_cli_rejected_without_mutation(request, other)

    def test_symlink_alias_rejected(self):
        alias = self.repo.base / "10_notes" / "ALIAS_TEST_RESULTS.md"
        try:
            alias.symlink_to(self.repo.results)
        except OSError:
            # When Windows denies symlink creation, create the alias as a regular file.
            # The require_exact call in resolve_contract will reject it because the
            # lexical path won't match the expected <CHAR>_TEST_RESULTS.md name.
            alias.write_text("alias", encoding="utf-8")
            run(["git", "add", "--", self.repo.rel(alias)], self.repo.root)
            run(["git", "commit", "-m", "alias"], self.repo.root)
            request = self.repo.clone_request()
            request["expected_git_head"] = run(["git", "rev-parse", "HEAD"], self.repo.root).stdout.strip()
            request["updates"]["test_results"]["path"] = self.repo.rel(alias)
            self.assert_cli_rejected_without_mutation(request, self.repo.results)
            return
        request = self.repo.clone_request()
        request["updates"]["test_results"]["path"] = self.repo.rel(alias)
        self.assert_cli_rejected_without_mutation(request, self.repo.results)

    def test_missing_each_required_hash_rejected(self):
        for path in list(self.repo.request["expected_file_hashes"]):
            with self.subTest(path=path):
                request = self.repo.clone_request()
                request["expected_file_hashes"].pop(path)
                self.assert_cli_rejected_without_mutation(request)

    def test_extra_hash_rejected(self):
        extra = self.add_tracked("AI_CHARACTERS/TESTX/10_notes/EXTRA.md", "extra\n")
        request = self.repo.clone_request()
        request["expected_git_head"] = self.repo.request["expected_git_head"]
        request["expected_file_hashes"][self.repo.rel(extra)] = sha(extra)
        self.assert_cli_rejected_without_mutation(request)

    def test_alias_duplicate_hash_rejected(self):
        request = self.repo.clone_request()
        key = self.repo.rel(self.repo.results)
        request["expected_file_hashes"][key.replace("/", "\\")] = request["expected_file_hashes"][key]
        self.assert_cli_rejected_without_mutation(request)

    def test_missing_destination_from_absent_set_rejected(self):
        request = self.repo.clone_request()
        request["expected_absent_paths"] = ["AI_CHARACTERS/TESTX/07_generated/other.png"]
        self.assert_cli_rejected_without_mutation(request)

    def test_extra_absent_path_rejected(self):
        request = self.repo.clone_request()
        request["expected_absent_paths"].append("AI_CHARACTERS/TESTX/07_generated/other.png")
        self.assert_cli_rejected_without_mutation(request)

    def test_valid_repo_path_evidence(self):
        process = self.repo.invoke()
        self.assertEqual(process.returncode, 0, process.stderr)

    def test_valid_commit_evidence(self):
        request = self.repo.clone_request()
        request["approval_evidence"] = [{
            "kind": "commit", "assertion": "human_selected_and_approved",
            "commit_hash": request["expected_git_head"], "path": self.repo.rel(self.repo.approval),
            "required_text": [self.repo.pid, "human_selected_and_approved"],
        }]
        self.assertEqual(self.repo.invoke(request).returncode, 0)

    def test_valid_voyage_decision_evidence(self):
        decision = self.add_tracked(
            ".voyage/DECISIONS.md",
            "Decision ID: D-999\nhuman_selected_and_approved\nTESTX_TEST10_SCENE_V1\n",
        )
        request = self.repo.clone_request()
        request["expected_git_head"] = self.repo.request["expected_git_head"]
        request["approval_evidence"] = [{
            "kind": "voyage_decision", "assertion": "human_selected_and_approved",
            "path": ".voyage/DECISIONS.md", "decision_id": "D-999", "sha256": sha(decision),
            "required_text": [self.repo.pid, "human_selected_and_approved"],
        }]
        self.assertEqual(self.repo.invoke(request).returncode, 0)

    def test_approval_evidence_cannot_alias_mutation(self):
        request = self.repo.clone_request()
        request["approval_evidence"] = [{
            "kind": "repo_path", "assertion": "human_selected_and_approved",
            "path": self.repo.rel(self.repo.results), "sha256": sha(self.repo.results),
            "required_text": [self.repo.pid],
        }]
        self.assert_cli_rejected_without_mutation(request)

    def test_immutable_test_number_mismatch_rejected(self):
        request = self.repo.clone_request()
        request["test_number"] = 11
        self.assert_cli_rejected_without_mutation(request)

    def test_immutable_reference_mismatch_rejected(self):
        request = self.repo.clone_request()
        request["reference_paths"] = [self.repo.rel(self.repo.approval)]
        self.assert_cli_rejected_without_mutation(request)

    def test_immutable_backend_mismatch_rejected(self):
        request = self.repo.clone_request()
        request["backend"] = "local"
        self.assert_cli_rejected_without_mutation(request)

    def test_conflicting_existing_deployment_rejected(self):
        record = json.loads(self.repo.registry.read_text(encoding="utf-8"))
        record["deployed"] = True
        self.repo.registry.write_text(json.dumps(record) + "\n", encoding="utf-8")
        self.repo.request["expected_file_hashes"][self.repo.rel(self.repo.registry)] = sha(self.repo.registry)
        self.assert_cli_rejected_without_mutation(self.repo.request)

    def test_validator_order(self):
        calls = []
        original = self.module.command

        def fake(args, root, check=True):
            if "validate_visual_canon_pipeline.py" in " ".join(args):
                calls.append("character" if "--character" in args else "full")
                class Result:
                    returncode = 0
                    stdout = ""
                    stderr = ""
                return Result()
            return original(args, root, check)

        self.module.command = fake
        try:
            self.module.validators(self.repo.root, self.repo.char, post=False)
            self.module.validators(self.repo.root, self.repo.char, post=True)
        finally:
            self.module.command = original
        self.assertEqual(calls, ["full", "character", "character", "full"])


if __name__ == "__main__":
    unittest.main()
