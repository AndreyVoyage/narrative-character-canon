"""Temporary-Git helpers for deploy-tool tests."""
import hashlib, importlib.util, json, subprocess, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
TOOL=ROOT/"tools"/"deploy_visual_canon_result.py"
def load_tool():
    spec=importlib.util.spec_from_file_location("deploy_tool_test",TOOL); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def run(cmd,cwd): return subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,encoding="utf-8")
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

class Repo:
    def __init__(self):
        self.tmp=tempfile.TemporaryDirectory(); self.root=Path(self.tmp.name)/"repo"; self.root.mkdir()
        run(["git","init","-b","main"],self.root); run(["git","config","user.email","test@example.com"],self.root); run(["git","config","user.name","Test"],self.root)
        self.char="TESTX"; base=self.root/"AI_CHARACTERS"/self.char
        self.registry=base/"06_prompts"/"TESTX_PROMPT_RUN_LOG.jsonl"
        self.index=base/"06_prompts"/"TESTX_PROMPT_INDEX.md"; self.prompt=base/"06_prompts"/"TESTX_WORKING_SCENE_PROMPTS.md"
        self.results=base/"10_notes"/"TESTX_TEST_RESULTS.md"; self.presets=base/"10_notes"/"TESTX_REFERENCE_PRESETS.json"; self.ref=base/"03_face_sheet"/"TESTX_face.png"
        for p in [self.registry,self.index,self.prompt,self.results,self.presets,self.ref]: p.parent.mkdir(parents=True,exist_ok=True)
        pid="TESTX_TEST10_SCENE_V1"; refs=["AI_CHARACTERS/TESTX/03_face_sheet/TESTX_face.png"]
        self.registry.write_text(json.dumps({"prompt_id":pid,"character_id":"TESTX","scene_id":"scene","version":"V1","reference_paths":refs,"selected":False,"human_approval":False,"verdict":"DRAFT","deployed":False},separators=(",",":"))+"\n",encoding="utf-8")
        self.index.write_text("# Index\nENTRY TESTX_TEST10_SCENE_V1\n",encoding="utf-8"); self.prompt.write_text("# Prompts\n## TESTX_TEST10_SCENE_V1\nPROMPT_ID: TESTX_TEST10_SCENE_V1\n",encoding="utf-8")
        self.results.write_text("# Results\nANCHOR_RESULTS\n",encoding="utf-8"); self.presets.write_text('{"scene_presets": {}}\n',encoding="utf-8"); self.ref.write_bytes(b"\x89PNG\r\n\x1a\nREF")
        (self.root/".gitattributes").write_text("*.png filter=lfs diff=lfs merge=lfs -text\n",encoding="utf-8")
        (self.root/"tools").mkdir(); (self.root/"tools"/"validate_visual_canon_pipeline.py").write_text("raise SystemExit(0)\n",encoding="utf-8")
        run(["git","add","."],self.root); run(["git","commit","-m","base"],self.root)
        self.source=Path(self.tmp.name)/"source.png"; self.source.write_bytes(b"\x89PNG\r\n\x1a\nSOURCE")
        self.out="AI_CHARACTERS/TESTX/07_generated/canon_tests/10_scene/TESTX_test10_scene_v1_APPROVED.png"
        self.request=self.make_request()
    def make_request(self):
        paths=[self.registry,self.index,self.prompt,self.results,self.presets]
        rel=lambda p:p.relative_to(self.root).as_posix()
        return {"schema_version":"1.0","operation_id":"op-test-001","expected_git_head":run(["git","rev-parse","HEAD"],self.root).stdout.strip(),"character_id":"TESTX","prompt_id":"TESTX_TEST10_SCENE_V1","test_number":10,"scene_id":"scene","version":"V1","source_image_path":str(self.source),"source_image_sha256":sha(self.source),"planned_output_path":self.out,"selected":True,"human_approval":True,"approval_evidence":[{"kind":"commit","value":"a"*40}],"verdict":"APPROVED_AS_TEST","role":"MAIN","storage":"repo_tracked","content_tier":"public_filtered","reference_paths":["AI_CHARACTERS/TESTX/03_face_sheet/TESTX_face.png"],"prompt_linkage":{"prompt_index_path":rel(self.index),"prompt_index_required_text":"ENTRY TESTX_TEST10_SCENE_V1","prompt_source_path":rel(self.prompt),"prompt_heading":"## TESTX_TEST10_SCENE_V1"},"expected_file_hashes":{rel(p):sha(p) for p in paths},"expected_absent_paths":[self.out],"updates":{"prompt_record":{"registry_path":rel(self.registry),"set_fields":{"selected":True,"human_approval":True,"verdict":"APPROVED_AS_TEST","role":"MAIN","storage":"repo_tracked","content_tier":"public_filtered","deployed":True,"output_path":self.out}},"test_results":{"path":rel(self.results),"unique_anchor":"ANCHOR_RESULTS","entry_markdown":"TEST10 ENTRY"},"reference_presets":{"path":rel(self.presets),"container_path":["scene_presets"],"preset_id":"scene","preset_value":{"selected_prompt_id":"TESTX_TEST10_SCENE_V1"}},"canon_index":None}}
    def write_request(self):
        p=Path(self.tmp.name)/"request.json"; p.write_text(json.dumps(self.request),encoding="utf-8"); return p
    def close(self): self.tmp.cleanup()
