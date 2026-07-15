"""Temporary-Git helpers for deploy-tool tests."""
import copy
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools" / "deploy_visual_canon_result.py"


def load_tool():
    spec = importlib.util.spec_from_file_location("deploy_tool_test", TOOL)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, capture_output=True, text=True, encoding="utf-8", env=env)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class Repo:
    def __init__(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "repo"
        self.root.mkdir()
        run(["git", "init", "-b", "main"], self.root)
        run(["git", "config", "user.email", "test@example.com"], self.root)
        run(["git", "config", "user.name", "Test"], self.root)
        self.char = "TESTX"
        self.base = self.root / "AI_CHARACTERS" / self.char
        self.registry = self.base / "06_prompts" / "TESTX_PROMPT_RUN_LOG.jsonl"
        self.index = self.base / "06_prompts" / "TESTX_PROMPT_INDEX.md"
        self.prompt = self.base / "06_prompts" / "TESTX_WORKING_SCENE_PROMPTS.md"
        self.results = self.base / "10_notes" / "TESTX_TEST_RESULTS.md"
        self.presets = self.base / "10_notes" / "TESTX_REFERENCE_PRESETS.json"
        self.canon = self.base / "10_notes" / "TESTX_CANON_INDEX.md"
        self.approval = self.base / "10_notes" / "TESTX_APPROVAL.md"
        self.ref = self.base / "03_face_sheet" / "TESTX_face.png"
        for path in [self.registry, self.index, self.prompt, self.results, self.presets, self.canon, self.approval, self.ref]:
            path.parent.mkdir(parents=True, exist_ok=True)
        self.pid = "TESTX_TEST10_SCENE_V1"
        self.refs = ["AI_CHARACTERS/TESTX/03_face_sheet/TESTX_face.png"]
        record = {
            "prompt_id": self.pid,
            "character_id": "TESTX",
            "test_number": 10,
            "scene_id": "scene",
            "version": "V1",
            "reference_paths": self.refs,
            "prompt_source_path": "AI_CHARACTERS/TESTX/06_prompts/TESTX_WORKING_SCENE_PROMPTS.md",
            "prompt_heading": "## TESTX_TEST10_SCENE_V1",
            "prompt_index_path": "AI_CHARACTERS/TESTX/06_prompts/TESTX_PROMPT_INDEX.md",
            "selected": False,
            "human_approval": False,
            "verdict": "DRAFT",
            "deployed": False,
        }
        self.registry.write_text(json.dumps(record, separators=(",", ":")) + "\n", encoding="utf-8")
        self.index.write_text("# Index\nENTRY TESTX_TEST10_SCENE_V1\n", encoding="utf-8")
        self.prompt.write_text("# Prompts\n## TESTX_TEST10_SCENE_V1\nPROMPT_ID: TESTX_TEST10_SCENE_V1\n", encoding="utf-8")
        self.results.write_text("# Results\nANCHOR_RESULTS\n", encoding="utf-8")
        self.presets.write_text('{"scene_presets": {}}\n', encoding="utf-8")
        self.canon.write_text("# Canon\nANCHOR_CANON\n", encoding="utf-8")
        self.approval.write_text("# Approval\nhuman_selected_and_approved\nTESTX_TEST10_SCENE_V1\n", encoding="utf-8")
        self.ref.write_bytes(b"\x89PNG\r\n\x1a\nREF")
        (self.root / ".gitattributes").write_text("*.png filter=lfs diff=lfs merge=lfs -text\n", encoding="utf-8")
        (self.root / "tools").mkdir()
        (self.root / "tools" / "validate_visual_canon_pipeline.py").write_text("raise SystemExit(0)\n", encoding="utf-8")
        run(["git", "add", "."], self.root)
        run(["git", "commit", "-m", "base"], self.root)
        self.source = Path(self.tmp.name) / "source.png"
        self.source.write_bytes(b"\x89PNG\r\n\x1a\nSOURCE")
        self.out = "AI_CHARACTERS/TESTX/07_generated/canon_tests/10_scene/TESTX_test10_scene_v1_APPROVED.png"
        self.request = self.make_request()

    def rel(self, path):
        return Path(path).relative_to(self.root).as_posix()

    def make_request(self):
        request = {
            "schema_version": "1.0",
            "operation_id": "op-test-001",
            "expected_git_head": run(["git", "rev-parse", "HEAD"], self.root).stdout.strip(),
            "character_id": "TESTX",
            "prompt_id": self.pid,
            "test_number": 10,
            "scene_id": "scene",
            "version": "V1",
            "source_image_path": str(self.source),
            "source_image_sha256": sha(self.source),
            "planned_output_path": self.out,
            "selected": True,
            "human_approval": True,
            "approval_evidence": [{
                "kind": "repo_path",
                "assertion": "human_selected_and_approved",
                "path": self.rel(self.approval),
                "sha256": sha(self.approval),
                "required_text": [self.pid, "human_selected_and_approved"],
            }],
            "verdict": "APPROVED_AS_TEST",
            "role": "MAIN",
            "storage": "repo_tracked",
            "content_tier": "public_filtered",
            "reference_paths": self.refs,
            "prompt_linkage": {
                "prompt_index_path": self.rel(self.index),
                "prompt_index_required_text": "ENTRY TESTX_TEST10_SCENE_V1",
                "prompt_source_path": self.rel(self.prompt),
                "prompt_heading": "## TESTX_TEST10_SCENE_V1",
            },
            "expected_file_hashes": {},
            "expected_absent_paths": [self.out],
            "updates": {
                "prompt_record": {
                    "registry_path": self.rel(self.registry),
                    "set_fields": {
                        "selected": True,
                        "human_approval": True,
                        "verdict": "APPROVED_AS_TEST",
                        "role": "MAIN",
                        "storage": "repo_tracked",
                        "content_tier": "public_filtered",
                        "deployed": True,
                        "output_path": self.out,
                    },
                },
                "test_results": {
                    "path": self.rel(self.results),
                    "unique_anchor": "ANCHOR_RESULTS",
                    "entry_markdown": "TEST10 ENTRY",
                },
                "reference_presets": {
                    "path": self.rel(self.presets),
                    "container_path": ["scene_presets"],
                    "preset_id": "scene",
                    "preset_value": {"selected_prompt_id": self.pid},
                },
                "canon_index": None,
            },
        }
        self.refresh_hashes(request)
        return request

    def required_hash_paths(self, request=None):
        request = request or self.request
        paths = [
            request["updates"]["prompt_record"]["registry_path"],
            request["updates"]["test_results"]["path"],
            request["updates"]["reference_presets"]["path"],
            request["prompt_linkage"]["prompt_index_path"],
            request["prompt_linkage"]["prompt_source_path"],
        ]
        if request["updates"]["canon_index"]:
            paths.append(request["updates"]["canon_index"]["path"])
        return paths

    def refresh_hashes(self, request=None):
        request = request or self.request
        request["expected_file_hashes"] = {
            rel.replace("\\", "/"): sha(self.root / Path(rel.replace("\\", "/")))
            for rel in self.required_hash_paths(request)
        }

    def approve_as_canon(self, request=None):
        request = request or self.request
        request["verdict"] = "APPROVED_AS_CANON"
        request["updates"]["prompt_record"]["set_fields"]["verdict"] = "APPROVED_AS_CANON"
        request["updates"]["canon_index"] = {
            "path": self.rel(self.canon),
            "unique_anchor": "ANCHOR_CANON",
            "entry_markdown": "CANON ENTRY",
        }
        self.refresh_hashes(request)
        return request

    def write_request(self, request=None):
        path = Path(self.tmp.name) / "request.json"
        path.write_text(json.dumps(request or self.request), encoding="utf-8")
        return path

    def invoke(self, request=None, *extra):
        return run(
            [sys.executable, str(TOOL), "--request", str(self.write_request(request)), "--repo-root", str(self.root), "--no-color", *extra],
            self.root,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )

    def snapshot(self):
        return {
            path.relative_to(self.root).as_posix(): path.read_bytes()
            for path in self.root.rglob("*")
            if path.is_file() and ".git" not in path.parts
        }

    def clone_request(self):
        return copy.deepcopy(self.request)

    def close(self):
        self.tmp.cleanup()
