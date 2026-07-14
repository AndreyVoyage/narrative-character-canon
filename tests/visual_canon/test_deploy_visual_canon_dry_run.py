import copy, unittest
from deploy_test_support import Repo, load_tool
class DryRun(unittest.TestCase):
 def setUp(self): self.m=load_tool(); self.r=Repo()
 def tearDown(self): self.r.close()
 def test_valid_request(self): self.m.validate_request(self.r.request)
 def test_missing_approval(self):
  q=copy.deepcopy(self.r.request); q["human_approval"]=False
  with self.assertRaises(self.m.DeployError): self.m.validate_request(q)
 def test_empty_evidence(self):
  q=copy.deepcopy(self.r.request); q["approval_evidence"]=[]
  with self.assertRaises(self.m.DeployError): self.m.validate_request(q)
 def test_wrong_head(self):
  with self.assertRaises(self.m.DeployError): self.m.git_check(self.r.root,"0"*40)
 def test_hashes_and_prepare_no_mutation(self):
  before=self.r.registry.read_bytes(); h=self.m.expected_hashes(self.r.root,self.r.request); changes,plan=self.m.prepare(self.r.root,self.r.request,self.r.source)
  self.assertTrue(h); self.assertTrue(plan); self.assertEqual(before,self.r.registry.read_bytes())
 def test_destination_collision(self):
  p=self.r.root/self.r.out; p.parent.mkdir(parents=True); p.write_bytes(b"x")
  with self.assertRaises(self.m.DeployError): self.m.expected_hashes(self.r.root,self.r.request)
