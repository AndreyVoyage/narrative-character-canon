import json, subprocess, sys, tempfile, unittest
from pathlib import Path
from deploy_test_support import TOOL, load_tool
class CLI(unittest.TestCase):
 def invoke(self,*a): return subprocess.run([sys.executable,str(TOOL),*a],capture_output=True,text=True)
 def test_help(self): self.assertEqual(self.invoke("--help").returncode,0)
 def test_version(self): self.assertEqual(self.invoke("--version").returncode,0)
 def test_missing_request(self): self.assertEqual(self.invoke().returncode,2)
 def test_malformed_json(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"x"; p.write_text("{")
   self.assertEqual(self.invoke("--request",str(p),"--repo-root",d).returncode,3)
 def test_forbidden_flags_absent(self):
  text=self.invoke("--help").stdout
  for flag in ["--stage","--commit","--push","--force","--skip-validator"]: self.assertNotIn(flag,text)
 def test_unknown_top_field(self):
  m=load_tool()
  with self.assertRaises(m.DeployError): m.validate_request({"bad":1})
 def test_request_schema_parses_without_duplicate_keys(self):
  p=TOOL.parents[1]/"configs"/"visual_canon"/"deployment_request.schema.json"; duplicates=[]
  def hook(pairs):
   d={}
   for k,v in pairs:
    if k in d: duplicates.append(k)
    d[k]=v
   return d
  json.loads(p.read_text(encoding="utf-8"),object_pairs_hook=hook); self.assertEqual(duplicates,[])
 def test_external_report_and_overwrite_refusal(self):
  m=load_tool()
  with tempfile.TemporaryDirectory() as d:
   root=Path(d)/"repo"; root.mkdir(); out=Path(d)/"report.json"
   m.report(str(out),root,{"ok":True},False); self.assertTrue(out.exists())
   with self.assertRaises(m.DeployError): m.report(str(out),root,{"ok":True},False)
 def test_missing_report_parent(self):
  m=load_tool()
  with tempfile.TemporaryDirectory() as d:
   root=Path(d)/"repo"; root.mkdir()
   with self.assertRaises(m.DeployError): m.report(str(Path(d)/"missing"/"x.json"),root,{},False)
 def test_source_has_no_forbidden_authority(self):
  text=TOOL.read_text(encoding="utf-8")
  for token in ["sqlite3","INVENTORY.md","git add","git commit","git push","shutil.move"]: self.assertNotIn(token,text)
