import unittest
from deploy_test_support import Repo, load_tool, sha
class Rollback(unittest.TestCase):
 def setUp(self): self.m=load_tool(); self.r=Repo()
 def tearDown(self): self.r.close()
 def attempt(self,validator):
  h=self.m.expected_hashes(self.r.root,self.r.request); c,_=self.m.prepare(self.r.root,self.r.request,self.r.source)
  with self.assertRaises(self.m.DeployError) as x: self.m.transaction(self.r.root,self.r.request,c,h,self.r.source,validator)
  return x.exception
 def test_post_validator_failure_rolls_back(self): self.attempt(lambda *a:(_ for _ in ()).throw(RuntimeError("fail"))); self.assertFalse((self.r.root/self.r.out).exists())
 def test_registry_restored(self): before=sha(self.r.registry); self.attempt(lambda *a:(_ for _ in ()).throw(RuntimeError())); self.assertEqual(before,sha(self.r.registry))
 def test_markdown_restored(self): before=sha(self.r.results); self.attempt(lambda *a:(_ for _ in ()).throw(RuntimeError())); self.assertEqual(before,sha(self.r.results))
 def test_preset_restored(self): before=sha(self.r.presets); self.attempt(lambda *a:(_ for _ in ()).throw(RuntimeError())); self.assertEqual(before,sha(self.r.presets))
 def test_exit_four(self): self.assertEqual(self.attempt(lambda *a:(_ for _ in ()).throw(RuntimeError())).status,4)
