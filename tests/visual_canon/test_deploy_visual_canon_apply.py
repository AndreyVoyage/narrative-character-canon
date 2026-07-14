import copy, unittest
from deploy_test_support import Repo, load_tool, sha
class Apply(unittest.TestCase):
 def setUp(self): self.m=load_tool(); self.r=Repo()
 def tearDown(self): self.r.close()
 def apply(self,q=None):
  q=q or self.r.request; h=self.m.expected_hashes(self.r.root,q); c,_=self.m.prepare(self.r.root,q,self.r.source)
  return self.m.transaction(self.r.root,q,c,h,self.r.source,lambda *a:None)
 def test_success(self): self.assertEqual(self.apply()["status"],"APPLIED")
 def test_source_unchanged(self): before=sha(self.r.source); self.apply(); self.assertEqual(before,sha(self.r.source))
 def test_destination_hash(self): self.apply(); self.assertEqual(sha(self.r.source),sha(self.r.root/self.r.out))
 def test_one_record_no_append(self): self.apply(); self.assertEqual(len(self.r.registry.read_text().splitlines()),1)
 def test_result_and_preset(self): self.apply(); self.assertIn("TEST10 ENTRY",self.r.results.read_text()); self.assertIn('"scene"',self.r.presets.read_text())
 def test_canon_for_test_forbidden(self):
  q=copy.deepcopy(self.r.request); q["updates"]["canon_index"]={"path":"x","unique_anchor":"x","entry_markdown":"x"}
  with self.assertRaises(self.m.DeployError): self.m.validate_request(q)
