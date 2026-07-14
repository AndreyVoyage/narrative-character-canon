#!/usr/bin/env python3
"""Dry-run-first deployment of one pre-registered visual-canon result."""
from __future__ import annotations

import argparse, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path, PurePosixPath
from typing import Any, Callable

__version__ = "1.0.0"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
REQUIRED = {"schema_version","operation_id","expected_git_head","character_id","prompt_id","test_number","scene_id","version","source_image_path","source_image_sha256","planned_output_path","selected","human_approval","approval_evidence","verdict","role","storage","content_tier","reference_paths","prompt_linkage","expected_file_hashes","expected_absent_paths","updates"}
OPTIONAL = {"character_ids","variant_label","backend","notes"}
SET_FIELDS = {"selected","human_approval","verdict","role","storage","content_tier","deployed","output_path"}


class DeployError(Exception):
    def __init__(self, status: int, code: str, message: str):
        super().__init__(message); self.status, self.code, self.message = status, code, message


def fail(status: int, code: str, message: str) -> None:
    raise DeployError(status, code, message)


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1048576), b""): h.update(chunk)
    return h.hexdigest()


def command(args: list[str], root: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    p = subprocess.run(args, cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check and p.returncode: fail(3, "DEPLOY-GIT-001", f"{' '.join(args)} failed: {p.stderr.strip()}")
    return p


def repository(explicit: str | None) -> Path:
    if explicit: root = Path(explicit).resolve()
    else:
        p = subprocess.run(["git","rev-parse","--show-toplevel"], capture_output=True, text=True, encoding="utf-8")
        if p.returncode: fail(3, "DEPLOY-GIT-002", "not inside a Git worktree")
        root = Path(p.stdout.strip()).resolve()
    if not (root / ".git").exists(): fail(3, "DEPLOY-GIT-002", "invalid Git worktree")
    return root


def relative(value: str) -> str:
    if not isinstance(value, str) or not value.strip(): fail(2, "DEPLOY-REQ-001", "empty repository path")
    value = value.replace("\\", "/"); p = PurePosixPath(value)
    if p.is_absolute() or re.match(r"^[A-Za-z]:", value) or ".." in p.parts: fail(3, "DEPLOY-GIT-003", f"unsafe path: {value}")
    if any(x in {".git",".voyage","LOCAL_STORAGE"} for x in p.parts): fail(3, "DEPLOY-GIT-003", f"protected path: {value}")
    return p.as_posix()


def target(root: Path, value: str, mutation: bool = False) -> tuple[str, Path]:
    rel = relative(value)
    if mutation and PurePosixPath(rel).parts[0] in {"configs","docs","tools","tests"}: fail(3, "DEPLOY-GIT-004", f"forbidden target: {rel}")
    path = (root / Path(rel)).resolve(strict=False)
    try: path.relative_to(root)
    except ValueError: fail(3, "DEPLOY-GIT-003", f"path escapes repository: {rel}")
    probe = path
    while not probe.exists() and probe != root: probe = probe.parent
    if probe.is_symlink(): fail(3, "DEPLOY-GIT-005", f"symlink path: {rel}")
    return rel, path


def json_object(path: Path, code: str = "DEPLOY-CLI-003") -> dict[str, Any]:
    duplicates: list[str] = []
    def hook(pairs):
        result = {}
        for k, v in pairs:
            if k in result: duplicates.append(k)
            result[k] = v
        return result
    try: data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)
    except (OSError, UnicodeError, json.JSONDecodeError) as e: fail(2, code, f"invalid JSON {path}: {e}")
    if duplicates: fail(2, "DEPLOY-REQ-002", f"duplicate keys: {sorted(set(duplicates))}")
    if not isinstance(data, dict): fail(2, "DEPLOY-REQ-003", "JSON root must be an object")
    return data


def validate_request(r: dict[str, Any]) -> None:
    if set(r) - REQUIRED - OPTIONAL or REQUIRED - set(r): fail(2, "DEPLOY-REQ-004", "unknown or missing top-level fields")
    fixed = {"schema_version":"1.0","selected":True,"human_approval":True,"storage":"repo_tracked","content_tier":"public_filtered"}
    if any(r.get(k) != v for k,v in fixed.items()): fail(1, "DEPLOY-REQ-005", "fixed deployment values violated")
    if r["verdict"] not in {"APPROVED_AS_TEST","APPROVED_AS_CANON"} or r["role"] not in {"MAIN","ALT"}: fail(1, "DEPLOY-REQ-005", "invalid verdict/role")
    if not re.fullmatch(r"[0-9a-fA-F]{40}", r["expected_git_head"]): fail(2, "DEPLOY-REQ-006", "invalid expected HEAD")
    if not isinstance(r["approval_evidence"], list) or not r["approval_evidence"]: fail(1, "DEPLOY-REQ-007", "approval evidence required")
    for e in r["approval_evidence"]:
        if not isinstance(e,dict) or set(e)!={"kind","value"} or e["kind"] not in {"repo_path","voyage_decision","commit"} or not e["value"]: fail(1,"DEPLOY-REQ-007","invalid approval evidence")
    refs = r["reference_paths"]
    if not isinstance(refs,list) or not refs or len({relative(x).casefold() for x in refs}) != len(refs): fail(1,"DEPLOY-REQ-008","references must be unique")
    out = relative(r["planned_output_path"])
    if not re.fullmatch(rf"AI_CHARACTERS/{re.escape(r['character_id'])}/07_generated/.+\.png", out): fail(1,"DEPLOY-REQ-009","invalid output path")
    if out.casefold() not in {relative(x).casefold() for x in r["expected_absent_paths"]}: fail(1,"DEPLOY-REQ-010","output must be expected absent")
    u = r["updates"]
    if not isinstance(u,dict) or set(u)!={"prompt_record","test_results","reference_presets","canon_index"}: fail(2,"DEPLOY-REQ-011","invalid updates")
    fields = u["prompt_record"].get("set_fields",{})
    if set(fields) != SET_FIELDS: fail(1,"DEPLOY-REQ-012","unsupported prompt-record mutation")
    expected = {"selected":True,"human_approval":True,"verdict":r["verdict"],"role":r["role"],"storage":"repo_tracked","content_tier":"public_filtered","deployed":True,"output_path":out}
    if fields != expected: fail(1,"DEPLOY-REQ-013","record update contradicts request")
    if (r["verdict"]=="APPROVED_AS_TEST") != (u["canon_index"] is None): fail(1,"DEPLOY-REQ-014","invalid Canon Index condition")


def git_check(root: Path, head: str, allowed_dirty: set[str] | None = None) -> None:
    if not command(["git","symbolic-ref","--quiet","--short","HEAD"],root).stdout.strip(): fail(3,"DEPLOY-GIT-006","detached HEAD")
    if command(["git","rev-parse","HEAD"],root).stdout.strip().lower()!=head.lower(): fail(3,"DEPLOY-GIT-007","HEAD mismatch")
    for marker in ["MERGE_HEAD","CHERRY_PICK_HEAD","REVERT_HEAD","rebase-merge","rebase-apply"]:
        if (root/".git"/marker).exists(): fail(3,"DEPLOY-GIT-008",f"Git operation active: {marker}")
    if command(["git","diff","--cached","--name-only"],root).stdout.strip(): fail(3,"DEPLOY-GIT-009","staged changes forbidden")
    dirty = set(filter(None,command(["git","diff","--name-only"],root).stdout.splitlines()))
    if dirty-(allowed_dirty or set()): fail(3,"DEPLOY-GIT-010",f"unexpected dirty files: {sorted(dirty)}")


def tracked(root: Path, rel: str) -> None:
    if command(["git","ls-files","--error-unmatch",rel],root,False).returncode: fail(3,"DEPLOY-GIT-011",f"untracked required file: {rel}")


def source_file(r: dict[str, Any]) -> Path:
    p = Path(r["source_image_path"]).expanduser().resolve()
    if not p.is_file() or p.is_symlink() or p.suffix.lower()!=".png": fail(1,"DEPLOY-REQ-015","invalid source")
    head = p.read_bytes()[:64]
    if not head.startswith(b"\x89PNG\r\n\x1a\n") or head.startswith(b"version https://git-lfs.github.com/spec/v1"): fail(1,"DEPLOY-REQ-016","source is not real PNG bytes")
    if digest(p).lower()!=r["source_image_sha256"].lower(): fail(3,"DEPLOY-GIT-012","source hash mismatch")
    return p


def expected_hashes(root: Path, r: dict[str, Any]) -> dict[str,str]:
    result={}; seen=set()
    for raw, expected in r["expected_file_hashes"].items():
        rel,p=target(root,raw)
        if rel.casefold() in seen: fail(1,"DEPLOY-REQ-018","duplicate normalized path")
        seen.add(rel.casefold())
        if not p.is_file() or p.is_symlink(): fail(3,"DEPLOY-GIT-013",f"missing expected file: {rel}")
        tracked(root,rel); actual=digest(p)
        if actual.lower()!=expected.lower(): fail(3,"DEPLOY-GIT-014",f"stale hash: {rel}")
        result[rel]=actual
    for raw in r["expected_absent_paths"]:
        rel,p=target(root,raw,True)
        if p.exists(): fail(3,"DEPLOY-GIT-015",f"collision: {rel}")
    return result


def once(text: str, needle: str, code: str) -> None:
    if text.count(needle)!=1: fail(1,code,f"required text must occur once: {needle}")


def markdown(text: str, update: dict[str,Any]) -> str:
    once(text,update["unique_anchor"],"DEPLOY-LINK-004")
    if update["entry_markdown"] in text: fail(1,"DEPLOY-LINK-005","Markdown entry collision")
    pos=text.index(update["unique_anchor"])+len(update["unique_anchor"])
    entry="\n"+update["entry_markdown"].rstrip("\n")+"\n"
    out=text[:pos]+entry+text[pos:]
    return out if out.endswith("\n") else out+"\n"


def prepare(root: Path, r: dict[str,Any], src: Path) -> tuple[dict[str,bytes],list[dict[str,str]]]:
    changes={relative(r["planned_output_path"]):src.read_bytes()}; plan=[]
    plan.append({"action":"COPY","path":relative(r["planned_output_path"]),"before":"ABSENT","change":"COPY_SOURCE","validation":"PASS"})
    pr=r["updates"]["prompt_record"]; reg_rel,reg=target(root,pr["registry_path"],True)
    lines=reg.read_text(encoding="utf-8").splitlines(); parsed=[]
    for n,line in enumerate(lines,1):
        if not line.strip(): continue
        try: parsed.append(json.loads(line))
        except json.JSONDecodeError as e: fail(1,"DEPLOY-LINK-002",f"invalid JSONL line {n}: {e}")
    ids=[x.get("prompt_id") for x in parsed]
    if len(ids)!=len(set(ids)): fail(1,"DEPLOY-LINK-003","duplicate prompt IDs")
    matches=[x for x in parsed if x.get("prompt_id")==r["prompt_id"]]
    if len(matches)!=1: fail(1,"DEPLOY-LINK-006","existing prompt record not unique")
    rec=matches[0]
    for k,v in {"character_id":r["character_id"],"scene_id":r["scene_id"],"version":r["version"]}.items():
        if k in rec and rec[k]!=v: fail(1,"DEPLOY-LINK-007",f"immutable mismatch: {k}")
    if rec.get("reference_paths") is not None and rec["reference_paths"]!=r["reference_paths"]: fail(1,"DEPLOY-LINK-008","reference mismatch")
    updated=dict(rec); updated.update(pr["set_fields"]); new=[]
    for line in lines:
        if line.strip() and json.loads(line).get("prompt_id")==r["prompt_id"]: new.append(json.dumps(updated,ensure_ascii=False,separators=(",",":")))
        else: new.append(line)
    changes[reg_rel]=("\n".join(new)+"\n").encode()
    plan.append({"action":"UPDATE","path":reg_rel,"before":digest(reg),"change":"ONE_JSONL_RECORD","validation":"PASS"})
    link=r["prompt_linkage"]; irel,ip=target(root,link["prompt_index_path"]); srel,sp=target(root,link["prompt_source_path"])
    it=ip.read_text(encoding="utf-8"); st=sp.read_text(encoding="utf-8")
    once(it,link["prompt_index_required_text"],"DEPLOY-LINK-011"); once(st,link["prompt_heading"],"DEPLOY-LINK-012")
    if r["prompt_id"] not in st: fail(1,"DEPLOY-LINK-013","prompt ID absent from source")
    for rel in (irel,srel): plan.append({"action":"VALIDATE","path":rel,"before":digest(root/rel),"change":"NONE","validation":"PASS"})
    for raw in r["reference_paths"]:
        rel,p=target(root,raw)
        if not p.is_file(): fail(1,"DEPLOY-LINK-014",f"missing reference: {rel}")
        tracked(root,rel)
    tr=r["updates"]["test_results"]; trel,trp=target(root,tr["path"],True); changes[trel]=markdown(trp.read_text(encoding="utf-8"),tr).encode()
    plan.append({"action":"UPDATE","path":trel,"before":digest(trp),"change":"INSERT_MARKDOWN","validation":"PASS"})
    rp=r["updates"]["reference_presets"]; rrel,rpath=target(root,rp["path"],True); doc=json_object(rpath,"DEPLOY-LINK-015"); container=doc
    for key in rp["container_path"]:
        if not isinstance(container,dict) or key not in container: fail(1,"DEPLOY-LINK-016","preset container missing")
        container=container[key]
    if not isinstance(container,dict) or rp["preset_id"] in container: fail(1,"DEPLOY-LINK-017","preset collision/container invalid")
    container[rp["preset_id"]]=rp["preset_value"]; changes[rrel]=(json.dumps(doc,ensure_ascii=False,indent=2)+"\n").encode()
    plan.append({"action":"UPDATE","path":rrel,"before":digest(rpath),"change":"INSERT_PRESET","validation":"PASS"})
    ci=r["updates"]["canon_index"]
    if ci:
        crel,cp=target(root,ci["path"],True); changes[crel]=markdown(cp.read_text(encoding="utf-8"),ci).encode()
        plan.append({"action":"UPDATE","path":crel,"before":digest(cp),"change":"INSERT_MARKDOWN","validation":"PASS"})
    return changes,plan


def lfs(root: Path, out: str) -> None:
    if not command(["git","check-attr","filter","--",out],root).stdout.rstrip().endswith(": lfs"): fail(1,"DEPLOY-LFS-001","destination lacks LFS")
    if command(["git","lfs","version"],root,False).returncode: fail(1,"DEPLOY-LFS-002","Git LFS unavailable")
    if command(["git","check-ignore","-q","--",out],root,False).returncode==0: fail(1,"DEPLOY-LFS-003","destination ignored")


def validators(root: Path, character: str) -> None:
    tool=root/"tools"/"validate_visual_canon_pipeline.py"
    for extra in ([],["--character",character]):
        p=command([sys.executable,str(tool),"--repo-root",str(root),"--mode","compatibility","--no-color",*extra],root,False)
        if p.returncode: fail(1,"DEPLOY-VALIDATOR-001",f"validator failed: {p.returncode}")


def transaction(root: Path,r: dict[str,Any],changes: dict[str,bytes],hashes: dict[str,str],src: Path,validator: Callable[[Path,str],None]=validators) -> dict[str,Any]:
    txn=Path(tempfile.mkdtemp(prefix=f"ncc_deploy_{r['operation_id']}_")); backups=txn/"backups"; prepared=txn/"prepared"; backups.mkdir(); prepared.mkdir()
    state={"operation_id":r["operation_id"],"status":"PREPARED","completed":[],"transaction_dir":str(txn)}; manifest=txn/"recovery_manifest.json"
    def save(): manifest.write_text(json.dumps(state,indent=2)+"\n",encoding="utf-8")
    save(); before=command(["git","status","--porcelain","--untracked-files=no"],root).stdout
    for rel,data in changes.items():
        pp=prepared/rel; pp.parent.mkdir(parents=True,exist_ok=True); pp.write_bytes(data); tp=root/rel
        if tp.exists(): bp=backups/rel; bp.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(tp,bp)
    try:
        git_check(root,r["expected_git_head"])
        for rel,h in hashes.items():
            if digest(root/rel).lower()!=h.lower(): fail(3,"DEPLOY-GIT-016",f"concurrent edit: {rel}")
        if digest(src).lower()!=r["source_image_sha256"].lower(): fail(3,"DEPLOY-GIT-012","source changed")
        order=[relative(r["planned_output_path"]),relative(r["updates"]["prompt_record"]["registry_path"]),relative(r["updates"]["test_results"]["path"]),relative(r["updates"]["reference_presets"]["path"])]
        if r["updates"]["canon_index"]: order.append(relative(r["updates"]["canon_index"]["path"]))
        for rel in order:
            tp=root/rel
            if rel in hashes and digest(tp).lower()!=hashes[rel].lower(): fail(3,"DEPLOY-GIT-016",f"target changed: {rel}")
            tp.parent.mkdir(parents=True,exist_ok=True); temp=tp.with_name(tp.name+"."+r["operation_id"]+".tmp"); shutil.copy2(prepared/rel,temp); os.replace(temp,tp)
            state["completed"].append(rel); save()
        git_check(root,r["expected_git_head"],set(changes)); validator(root,r["character_id"])
        if digest(src)!=r["source_image_sha256"].lower() or digest(root/relative(r["planned_output_path"]))!=digest(src): fail(4,"DEPLOY-TXN-001","image hash failure")
        shutil.rmtree(txn); return {"status":"APPLIED","changed_files":list(changes)}
    except Exception as exc:
        ok=True
        for rel in reversed(state["completed"]):
            tp=root/rel; bp=backups/rel
            try:
                if bp.exists(): tmp=tp.with_name(tp.name+".rollback.tmp"); shutil.copy2(bp,tmp); os.replace(tmp,tp)
                elif tp.exists():
                    tp.unlink()
                    if tp.parent!=root and tp.parent.exists() and not any(tp.parent.iterdir()): tp.parent.rmdir()
            except Exception: ok=False
        if command(["git","status","--porcelain","--untracked-files=no"],root,False).stdout!=before: ok=False
        state["status"]="ROLLED_BACK" if ok else "ROLLBACK_INCOMPLETE"; state["error"]=str(exc); save()
        if ok: shutil.rmtree(txn); fail(4,"DEPLOY-TXN-002","apply failed; repository restored")
        fail(4,"DEPLOY-TXN-003",f"rollback incomplete: {manifest}")


def report(path_value: str,root: Path,data: dict[str,Any],overwrite: bool) -> None:
    path=Path(path_value).resolve()
    try: path.relative_to(root); fail(2,"DEPLOY-CLI-004","report must be outside repository")
    except ValueError: pass
    if not path.parent.exists(): fail(2,"DEPLOY-CLI-005","report parent missing")
    if path.exists() and not overwrite: fail(2,"DEPLOY-CLI-006","report exists")
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")


def parser() -> argparse.ArgumentParser:
    p=argparse.ArgumentParser(prog="deploy_visual_canon_result",description="Deploy one existing human-approved visual-canon attempt.")
    p.add_argument("--request",required=True); p.add_argument("--repo-root"); p.add_argument("--apply",action="store_true")
    p.add_argument("--json-report"); p.add_argument("--overwrite-report",action="store_true"); p.add_argument("--no-color",action="store_true")
    p.add_argument("--version",action="version",version=f"%(prog)s {__version__}"); return p


def main(argv: list[str] | None=None) -> int:
    try:
        a=parser().parse_args(argv); root=repository(a.repo_root); r=json_object(Path(a.request).resolve()); validate_request(r)
        git_check(root,r["expected_git_head"]); src=source_file(r); hashes=expected_hashes(root,r); lfs(root,relative(r["planned_output_path"]))
        changes,plan=prepare(root,r,src); validators(root,r["character_id"])
        data={"tool":"deploy_visual_canon_result","version":__version__,"mode":"apply" if a.apply else "dry_run","operation_id":r["operation_id"],"status":"DRY_RUN_VALID","plan":plan,"changed_files":[]}
        if a.apply: data.update(transaction(root,r,changes,hashes,src))
        if a.json_report: report(a.json_report,root,data,a.overwrite_report)
        print(json.dumps(data,ensure_ascii=False,indent=2)); return 0
    except DeployError as e: print(f"[{e.code}] {e.message}",file=sys.stderr); return e.status
    except SystemExit: raise
    except Exception as e: print(f"[DEPLOY-INTERNAL] {e}",file=sys.stderr); return 5


if __name__=="__main__": raise SystemExit(main())
