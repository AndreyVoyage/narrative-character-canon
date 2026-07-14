import copy, unittest
from deploy_test_support import Repo, load_tool
class Concurrency(unittest.TestCase):
 def setUp(self): self.m=load_tool(); self.r=Repo()
 def tearDown(self): self.r.close()
 def test_dirty_tracked(self): self.r.index.write_text("dirty"); self.assertRaises(self.m.DeployError,self.m.git_check,self.r.root,self.r.request["expected_git_head"])
 def test_stale_target_hash(self): self.r.results.write_text("changed"); self.assertRaises(self.m.DeployError,self.m.expected_hashes,self.r.root,self.r.request)
 def test_source_hash_change(self): self.r.source.write_bytes(b"\x89PNG\r\n\x1a\nchanged"); self.assertRaises(self.m.DeployError,self.m.source_file,self.r.request)
 def test_unsafe_traversal(self): self.assertRaises(self.m.DeployError,self.m.relative,"../escape")
 def test_local_storage_forbidden(self): self.assertRaises(self.m.DeployError,self.m.relative,"LOCAL_STORAGE/private.png")
 def test_unsupported_record_field(self):
  q=copy.deepcopy(self.r.request); q["updates"]["prompt_record"]["set_fields"]["prompt_id"]="bad"
  self.assertRaises(self.m.DeployError,self.m.validate_request,q)
