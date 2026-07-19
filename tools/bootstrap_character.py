#!/usr/bin/env python3
"""NCC Character Bootstrap MVP — create a new character namespace from an owner-authored JSON spec.

Standard library only.  Dry-run by default; writes require --apply.
Never generates, inspects, selects, approves, copies, renames, or deploys images.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

VERSION = "1.0.0"

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REQUIRED_SPEC_FIELDS = [
    "schema_version",
    "character_id",
    "display_name",
    "prompt_subject",
    "identity_anchor",
    "style_direction",
    "safety_rules",
    "next_step",
    "current_status",
    "reference_preset_status",
]

CHARACTER_ID_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")

RESERVED_NAMESPACE_PREFIXES = [
    "_JOINT_SCENES",
    "_SHARED",
    "_TEMPLATES",
]

MARKDOWN_TABLE_BREAK_CHARS = ["|", "\n"]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def eprint(*args, **kwargs):
    """Print to stderr."""
    kwargs.setdefault("file", sys.stderr)
    print(*args, **kwargs)


def run(cmd: list[str], cwd: Path, capture: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(cwd), capture_output=capture, text=True, encoding="utf-8", errors="replace")


def sha256_path(path: Path) -> str:
    """Return SHA-256 hex digest of a file's contents."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def git_head(cwd: Path) -> str:
    return run(["git", "rev-parse", "HEAD"], cwd).stdout.strip()


def git_origin_main(cwd: Path) -> str:
    return run(["git", "rev-parse", "origin/main"], cwd).stdout.strip()


def git_status_short(cwd: Path) -> str:
    return run(["git", "status", "--short"], cwd).stdout


def git_diff_cached(cwd: Path) -> str:
    return run(["git", "diff", "--cached", "--name-status"], cwd).stdout


# ---------------------------------------------------------------------------
# Preflight
# ---------------------------------------------------------------------------

PROTECTED_UNTRACKED = {".claude/", ".vscode/", "UNIFIED_CANON_TESTS_TEMPLATE.md", "repo_audit.txt"}

REQUIRED_FILE_PATHS = [
    "AI_CHARACTERS/",
    ".voyage/CHARACTER_REGISTRY.md",
    ".voyage/DECISIONS.md",
    ".voyage/PROJECT_STATE.md",
    "tools/generate_inventory.py",
    "tools/validate_visual_canon_pipeline.py",
]


def preflight(repo_root: Path, apply_mode: bool = False) -> dict:
    """Run full preflight. Returns dict with 'head', 'origin_main', 'file_hashes'."""
    errors: list[str] = []

    if not (repo_root / ".git").is_dir():
        errors.append("PREFLIGHT-001: Not a Git repository")

    branch = run(["git", "branch", "--show-current"], repo_root).stdout.strip()
    if branch != "main":
        errors.append(f"PREFLIGHT-002: Expected branch 'main', got '{branch}'")

    head = git_head(repo_root)
    origin_result = run(["git", "rev-parse", "origin/main"], repo_root)
    if origin_result.returncode == 0:
        origin_main = origin_result.stdout.strip()
        if head != origin_main:
            errors.append(f"PREFLIGHT-003: HEAD ({head[:8]}) != origin/main ({origin_main[:8]})")
    else:
        # No remote — allow in test/temp environments
        pass

    # Check tracked changes
    status = git_status_short(repo_root)
    tracked_changes = [line for line in status.splitlines() if line.strip() and not line.startswith("??")]
    if tracked_changes:
        errors.append(f"PREFLIGHT-004: Tracked changes detected:\n{chr(10).join(tracked_changes)}")

    # Check staged
    staged = git_diff_cached(repo_root)
    if staged.strip():
        errors.append(f"PREFLIGHT-005: Staged changes detected:\n{staged}")

    # Check untracked for protected-only allowance
    untracked_lines = [line[3:].strip() for line in status.splitlines() if line.startswith("??")]
    unexpected = set(untracked_lines) - PROTECTED_UNTRACKED
    if unexpected:
        errors.append(f"PREFLIGHT-006: Unexpected untracked paths: {sorted(unexpected)}")

    # Check required files
    for req_path in REQUIRED_FILE_PATHS:
        if not (repo_root / req_path).exists():
            errors.append(f"PREFLIGHT-007: Required path missing: {req_path}")

    if errors:
        for e in errors:
            eprint(e)
        sys.exit(4)

    # Collect SHA-256 of existing files that may be modified
    modifiable = [
        ".voyage/CHARACTER_REGISTRY.md",
        ".voyage/DECISIONS.md",
        ".voyage/PROJECT_STATE.md",
    ]
    file_hashes = {p: sha256_path(repo_root / p) for p in modifiable if (repo_root / p).exists()}

    return {"head": head, "file_hashes": file_hashes}


def recheck_preflight(repo_root: Path, expected_head: str, expected_hashes: dict) -> list[str]:
    """Recheck before mutation. Returns list of error messages (empty = OK)."""
    errors = []
    current_head = git_head(repo_root)
    if current_head != expected_head:
        errors.append(f"CONCURRENCY: HEAD changed from {expected_head[:8]} to {current_head[:8]}")
    for path, expected_hash in expected_hashes.items():
        current_hash = sha256_path(repo_root / path)
        if current_hash != expected_hash:
            errors.append(f"CONCURRENCY: {path} hash changed")
    return errors


# ---------------------------------------------------------------------------
# Spec loading and validation
# ---------------------------------------------------------------------------


def load_and_validate_spec(spec_path: Path) -> dict:
    """Load spec JSON and validate against schema and business rules."""
    try:
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        eprint(f"SPEC-001: Cannot parse spec JSON: {exc}")
        sys.exit(2)

    # Load schema
    schema_path = Path(__file__).resolve().parent.parent / "configs" / "visual_canon" / "character_bootstrap.schema.json"
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except Exception as exc:
        eprint(f"SPEC-002: Cannot load bootstrap schema: {exc}")
        sys.exit(5)

    # Validate required fields
    missing = [f for f in REQUIRED_SPEC_FIELDS if f not in spec]
    if missing:
        eprint(f"SPEC-003: Missing required fields: {missing}")
        sys.exit(2)

    unknown = [k for k in spec if k not in REQUIRED_SPEC_FIELDS and k not in ["$schema"]]
    if unknown:
        eprint(f"SPEC-004: Unknown fields: {unknown}")
        sys.exit(2)

    # Check for blank/empty fields
    for field in REQUIRED_SPEC_FIELDS:
        if field == "safety_rules":
            if not isinstance(spec.get(field), list) or len(spec.get(field, [])) == 0:
                eprint(f"SPEC-005: '{field}' must be a non-empty list")
                sys.exit(2)
            for i, rule in enumerate(spec[field]):
                if not isinstance(rule, str) or not rule.strip():
                    eprint(f"SPEC-005: safety_rules[{i}] is blank or not a string")
                    sys.exit(2)
        elif field == "schema_version":
            if spec.get(field) != "1.0":
                eprint(f"SPEC-005: schema_version must be '1.0', got '{spec.get(field)}'")
                sys.exit(2)
        elif field == "current_status":
            if spec.get(field) not in ("TEXT_CANON_READY", "CANON_PROMPTS_CREATED"):
                eprint(f"SPEC-005: current_status must be TEXT_CANON_READY or CANON_PROMPTS_CREATED")
                sys.exit(2)
        else:
            val = spec.get(field, "")
            if not isinstance(val, str) or not val.strip():
                eprint(f"SPEC-005: '{field}' is blank or missing")
                sys.exit(2)

    # Validate character_id
    cid = spec["character_id"]
    if not CHARACTER_ID_RE.match(cid):
        eprint(f"SPEC-006: character_id '{cid}' must match ^[A-Z][A-Z0-9_]*$")
        sys.exit(2)
    if cid.startswith("_"):
        eprint(f"SPEC-007: character_id '{cid}' must not start with '_'")
        sys.exit(2)
    for prefix in RESERVED_NAMESPACE_PREFIXES:
        if cid.startswith(prefix):
            eprint(f"SPEC-008: character_id '{cid}' conflicts with reserved namespace '{prefix}'")
            sys.exit(2)

    # Check for Markdown-table-breaking characters in registry-visible fields
    check_fields = ["character_id", "display_name", "prompt_subject", "current_status", "reference_preset_status", "next_step"]
    for field in check_fields:
        val = spec.get(field, "")
        if isinstance(val, str):
            for ch in MARKDOWN_TABLE_BREAK_CHARS:
                if ch in val:
                    eprint(f"SPEC-009: '{field}' contains Markdown-table-breaking character: {repr(ch)}")
                    sys.exit(2)

    # Check for placeholder values
    placeholder_patterns = ["TODO", "FIXME", "placeholder", "replace_me", "TBD", "xxx"]
    for field in REQUIRED_SPEC_FIELDS:
        val = spec.get(field, "")
        if isinstance(val, str):
            val_lower = val.lower()
            for pp in placeholder_patterns:
                if pp.lower() in val_lower:
                    eprint(f"SPEC-010: '{field}' contains placeholder value: '{pp}'")
                    sys.exit(2)

    return spec


# ---------------------------------------------------------------------------
# Namespace collision check
# ---------------------------------------------------------------------------


def check_existing_namespace(repo_root: Path, character_id: str) -> None:
    """Check that the character namespace does not already exist."""
    char_dir = repo_root / "AI_CHARACTERS" / character_id
    if char_dir.exists():
        eprint(f"NAMESPACE-001: Character directory already exists: {char_dir}")
        sys.exit(2)

    # Case-insensitive check
    ai_dir = repo_root / "AI_CHARACTERS"
    if ai_dir.exists():
        for entry in ai_dir.iterdir():
            if entry.is_dir() and entry.name.upper() == character_id.upper():
                eprint(f"NAMESPACE-002: Case-insensitive collision with existing: {entry.name}")
                sys.exit(2)

    # Check registry row
    registry_path = repo_root / ".voyage" / "CHARACTER_REGISTRY.md"
    if registry_path.exists():
        text = registry_path.read_text(encoding="utf-8")
        if f"| {character_id} |" in text:
            eprint(f"NAMESPACE-003: Character ID '{character_id}' already has a registry row")
            sys.exit(2)


# ---------------------------------------------------------------------------
# Folder creation
# ---------------------------------------------------------------------------

FOLDERS = [
    "01_refs_raw",
    "02_best_refs",
    "03_face_sheet/expressions",
    "04_body_sheet/candidates",
    "05_outfits/casual",
    "05_outfits/formal",
    "05_outfits/evening_dress",
    "05_outfits/sports_look",
    "05_outfits/scene_outfits",
    "05_outfits/candidates",
    "06_prompts",
    "07_generated/canon_tests",
    "07_generated/drafts",
    "07_generated/rejected",
    "08_masks",
    "09_blender",
    "10_notes",
]

GITKEEP_FOLDERS = [
    "01_refs_raw",
    "02_best_refs",
    "03_face_sheet/expressions",
    "04_body_sheet/candidates",
    "05_outfits/casual",
    "05_outfits/formal",
    "05_outfits/evening_dress",
    "05_outfits/sports_look",
    "05_outfits/scene_outfits",
    "05_outfits/candidates",
    "07_generated/canon_tests",
    "07_generated/drafts",
    "07_generated/rejected",
    "08_masks",
    "09_blender",
]


def create_folder_structure(repo_root: Path, character_id: str, dry_run: bool) -> list[str]:
    """Create the canonical 10-subfolder structure. Returns list of created paths."""
    created: list[str] = []
    base = repo_root / "AI_CHARACTERS" / character_id
    for folder in FOLDERS:
        full = base / folder
        created.append(str(full.relative_to(repo_root)))
        if not dry_run:
            full.mkdir(parents=True, exist_ok=True)
    for folder in GITKEEP_FOLDERS:
        full = base / folder / ".gitkeep"
        created.append(str(full.relative_to(repo_root)))
        if not dry_run:
            full.parent.mkdir(parents=True, exist_ok=True)
            full.write_text("", encoding="utf-8")
    return created


# ---------------------------------------------------------------------------
# Base file creation
# ---------------------------------------------------------------------------


def generate_canon_prompts(spec: dict) -> str:
    """Generate <CHAR>_CANON_GENERATION_PROMPTS.txt from spec."""
    cid = spec["character_id"]
    subject = spec["prompt_subject"]
    identity = spec["identity_anchor"]
    style = spec["style_direction"]
    rules = spec["safety_rules"]
    rules_text = "\n".join(f"* {r}" for r in rules)

    return f"""# {cid} Canon Generation Prompts

Status:
PENDING / NOT_STARTED

Important:
These prompts are for reference and generation context only.
Generation still requires explicit user request.

Character:
{cid}

Active version:
Base canon v1.0

Identity anchor:
{identity}

Prompt style rules:
{rules_text}

---

## Face Canon Sheet Prompt

Target folder:
AI_CHARACTERS/{cid}/03_face_sheet/

Target filename:
{cid}_face_canon_v1_sheet_A.png

Prompt:
Photorealistic character face canon sheet of the same {subject}, neutral grey studio background, soft even studio lighting, no dramatic shadows, no text labels, no numbers, no watermark, 2 rows x 4 columns layout, 8 consistent head-and-shoulders portraits.

{subject} with {identity}.

Expression range:
1. neutral
2. slight smile
3. thoughtful
4. warm
5. serious
6. gentle
7. confident
8. relaxed

Photorealistic, masterpiece, best quality, 8k uhd, cinematic studio lighting.

---

## Expression Canon Sheet Prompt

Target folder:
AI_CHARACTERS/{cid}/03_face_sheet/expressions/

Target filename:
{cid}_expressions_v1_sheet_A.png

Prompt:
Photorealistic character expression canon sheet of the same {subject}, neutral grey studio background, soft even lighting. 2 rows x 3 columns layout, 6 consistent head-and-shoulders portraits.

{subject} with {identity}.

Expression range:
1. neutral
2. slight smile
3. thoughtful
4. warm
5. serious
6. gentle

Same identity across all panels. Photorealistic, 8k uhd, studio lighting.

---

## Body Canon Sheet Prompt

Target folder:
AI_CHARACTERS/{cid}/04_body_sheet/

Target filename:
{cid}_body_canon_v1_sheet_A_front_side_back.png

Prompt:
Photorealistic full-body character canon sheet of the same {subject}, 3-panel layout: front view, side profile, back view, neutral grey studio background, soft even lighting, realistic anatomy, natural proportions.

{subject}, {identity}, {style}.

Same identity across all panels. No text, no numbers, no watermark. Photorealistic, masterpiece, best quality, 8k uhd.

---

## Body Pose Variations Prompt

Target folder:
AI_CHARACTERS/{cid}/04_body_sheet/

Target filename:
{cid}_body_canon_v1_sheet_B_pose_variations.png

Prompt:
Photorealistic full-body character pose sheet of the same {subject}, 2 rows x 3 columns layout, 6 dynamic poses, neutral grey studio background, soft even lighting.

{subject}, {identity}, {style}.

Pose range:
1. Standing neutral, relaxed posture
2. Walking forward, natural stride
3. Seated, natural pose
4. Casual relaxed
5. Formal pose, confident standing
6. Outdoor natural

Same identity across all panels. Photorealistic, 8k uhd, studio lighting.

---

*{cid} Canon Generation Prompts | NCC Bootstrap | {datetime.date.today().isoformat()}*
"""


def generate_prompt_index(spec: dict) -> str:
    """Generate <CHAR>_PROMPT_INDEX.md from spec."""
    cid = spec["character_id"]
    return f"""# {cid} Prompt Index

## Status

PROMPT_PIPELINE_NOT_STARTED

## Purpose

This folder stores prompt templates, working scene prompts, and prompt run logs for {cid} generations.

## Prompt Files

- `{cid}_CANON_GENERATION_PROMPTS.txt` — original reusable generation prompt source (face, expressions, body, pose variations)
- `{cid}_WORKING_SCENE_PROMPTS.md` — normalized prompt sections and reconstructions
- `{cid}_PROMPT_RUN_LOG.jsonl` — machine-readable prompt run log
- `{cid}_PROMPT_INDEX.md` — this index

## Reference Map

No approved reference images exist yet.

## Active Core Prompt IDs

None — generation has not started.

## Prompt Logging Rules

- Every future approved/candidate/rejected generation must have a `prompt_id`.
- Every `prompt_id` must link to an output image path.
- Every prompt record must include a reference map.
- Exact visible prompts are stored as `exact_user_visible_prompt`.
- Reconstructed prompts are marked honestly as `reconstructed_from_conversation_and_approved_result`.
- Unknown/unavailable prompts are marked as `unknown_requires_manual_input`.
- Do not claim unavailable hidden tool prompts are exact.
- Do not rename historical approved images during prompt backfill.
"""


def generate_working_scene_prompts(spec: dict) -> str:
    """Generate <CHAR>_WORKING_SCENE_PROMPTS.md from spec."""
    cid = spec["character_id"]
    return f"""# {cid} Working Scene Prompts

## Status

PROMPT_PIPELINE_NOT_STARTED

## Purpose

This file stores normalized prompt text sections and per-prompt-ID metadata for {cid} scene generation.

No prompt IDs have been created yet.

## Rules

- Every active prompt ID must have a section in this file.
- Prompt volumes are numbered intentionally.
- Rejected attempts may store metadata only.
- Do not create a new volume unless the current volume becomes unmanageable.

---

*{cid} Working Scene Prompts | NCC Bootstrap | {datetime.date.today().isoformat()}*
"""


def generate_identity_draft(spec: dict) -> str:
    """Generate <CHAR>_IDENTITY_DRAFT.md from spec."""
    cid = spec["character_id"]
    identity = spec["identity_anchor"]
    style = spec["style_direction"]
    display = spec["display_name"]
    return f"""# {cid} Identity Draft

## Status

TEXT_CANON_READY

## Display Name

{display}

## Identity Anchor

{identity}

## Style Direction

{style}

## Status

{spec['current_status']} / CANON_PROMPTS_CREATED

---

*{cid} Identity Draft | NCC Bootstrap | {datetime.date.today().isoformat()}*
"""


def generate_canon_index(spec: dict) -> str:
    """Generate <CHAR>_CANON_INDEX.md from spec."""
    cid = spec["character_id"]
    return f"""# {cid} Canon Index

## Status

TEXT_CANON_READY / CANON_PROMPTS_CREATED

## Purpose

Canon index for {cid}. No approved images exist yet.

## Active Files

None — generation has not started.

## Planned Canon Paths

| Role | Planned Path |
|---|---|
| Face canon | `AI_CHARACTERS/{cid}/03_face_sheet/{cid}_face_canon_v1_sheet_A_APPROVED.png` |
| Expression canon | `AI_CHARACTERS/{cid}/03_face_sheet/expressions/{cid}_expressions_v1_sheet_A_APPROVED.png` |
| Body canon A | `AI_CHARACTERS/{cid}/04_body_sheet/{cid}_body_canon_v1_sheet_A_APPROVED.png` |
| Body canon B | `AI_CHARACTERS/{cid}/04_body_sheet/{cid}_body_canon_v1_sheet_B_pose_variations_APPROVED.png` |

## Next Step

{spec['next_step']}

---

*{cid} Canon Index | NCC Bootstrap | {datetime.date.today().isoformat()}*
"""


def generate_test_results(spec: dict) -> str:
    """Generate <CHAR>_TEST_RESULTS.md from spec."""
    cid = spec["character_id"]
    return f"""# {cid} Test Results

## Status

NO_TESTS_RUN

## Purpose

Test results for {cid} control tests and scene tests.

No tests have been run yet.

## Rules

- Every test must have a `prompt_id`.
- Every test must reference the prompt index.
- Approved tests must have an output path.

---

*{cid} Test Results | NCC Bootstrap | {datetime.date.today().isoformat()}*
"""


def generate_reference_presets(spec: dict) -> str:
    """Generate <CHAR>_REFERENCE_PRESETS.json from spec."""
    cid = spec["character_id"]
    preset = {
        "character": cid,
        "active_version": f"{cid.lower()}_base_canon_v1.0",
        "status": spec["reference_preset_status"],
        "last_updated": datetime.date.today().isoformat(),
        "identity_summary": {
            "role": spec["prompt_subject"],
            "height_direction": "TBD — no generation yet",
            "body_direction": spec["identity_anchor"],
            "face_direction": spec["identity_anchor"],
            "hair_direction": "TBD — no generation yet",
            "style_direction": spec["style_direction"],
        },
        "active_canon": {
            "primary_face_reference": None,
            "face_canon": f"AI_CHARACTERS/{cid}/03_face_sheet/{cid}_face_canon_v1_sheet_A_APPROVED.png",
            "expression_canon": f"AI_CHARACTERS/{cid}/03_face_sheet/expressions/{cid}_expressions_v1_sheet_A_APPROVED.png",
            "body_canon_a": f"AI_CHARACTERS/{cid}/04_body_sheet/{cid}_body_canon_v1_sheet_A_APPROVED.png",
        },
        "planned_canon_paths": {
            "face_canon": f"AI_CHARACTERS/{cid}/03_face_sheet/{cid}_face_canon_v1_sheet_A_APPROVED.png",
            "expression_canon": f"AI_CHARACTERS/{cid}/03_face_sheet/expressions/{cid}_expressions_v1_sheet_A_APPROVED.png",
            "body_canon_a": f"AI_CHARACTERS/{cid}/04_body_sheet/{cid}_body_canon_v1_sheet_A_APPROVED.png",
            "body_canon_b": f"AI_CHARACTERS/{cid}/04_body_sheet/{cid}_body_canon_v1_sheet_B_pose_variations_APPROVED.png",
        },
        "control_tests": [],
        "scene_presets": {},
        "prompt_pipeline": {
            "status": "PROMPT_PIPELINE_NOT_STARTED",
            "prompt_index": f"AI_CHARACTERS/{cid}/06_prompts/{cid}_PROMPT_INDEX.md",
            "working_scene_prompts": f"AI_CHARACTERS/{cid}/06_prompts/{cid}_WORKING_SCENE_PROMPTS.md",
            "prompt_run_log": f"AI_CHARACTERS/{cid}/06_prompts/{cid}_PROMPT_RUN_LOG.jsonl",
        },
        "safety_rules": spec["safety_rules"],
    }
    return json.dumps(preset, indent=2, ensure_ascii=False) + "\n"


FILES_UNDER_06 = [
    ("CANON_GENERATION_PROMPTS.txt", generate_canon_prompts),
    ("PROMPT_INDEX.md", generate_prompt_index),
    ("WORKING_SCENE_PROMPTS.md", generate_working_scene_prompts),
    ("PROMPT_RUN_LOG.jsonl", lambda spec: ""),
]

FILES_UNDER_10 = [
    ("IDENTITY_DRAFT.md", generate_identity_draft),
    ("CANON_INDEX.md", generate_canon_index),
    ("TEST_RESULTS.md", generate_test_results),
    ("REFERENCE_PRESETS.json", generate_reference_presets),
]


def create_base_files(repo_root: Path, spec: dict, dry_run: bool) -> list[str]:
    """Create all base files. Returns list of created relative paths."""
    cid = spec["character_id"]
    created: list[str] = []
    base = repo_root / "AI_CHARACTERS" / cid

    for suffix, gen_func in FILES_UNDER_06:
        content = gen_func(spec)
        path = base / "06_prompts" / f"{cid}_{suffix}"
        rel = str(path.relative_to(repo_root))
        created.append(rel)
        if not dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    for suffix, gen_func in FILES_UNDER_10:
        content = gen_func(spec)
        path = base / "10_notes" / f"{cid}_{suffix}"
        rel = str(path.relative_to(repo_root))
        created.append(rel)
        if not dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    return created


# ---------------------------------------------------------------------------
# Voyage and inventory updates
# ---------------------------------------------------------------------------


def build_registry_row(spec: dict) -> str:
    cid = spec["character_id"]
    folder = f"`AI_CHARACTERS/{cid}`"
    status = spec["current_status"]
    preset_status = spec["reference_preset_status"]
    next_step = spec["next_step"]
    return f"| {cid} | {folder} | {status} | {preset_status} | {next_step} |"


def update_character_registry(repo_root: Path, spec: dict, dry_run: bool) -> str | None:
    """Append a registry row. Returns the relative path if modified."""
    path = repo_root / ".voyage" / "CHARACTER_REGISTRY.md"
    if not path.exists():
        return None
    row = build_registry_row(spec)
    if not dry_run:
        content = path.read_text(encoding="utf-8")
        # Find the table header line
        lines = content.splitlines(keepends=True)
        # Insert new row before the first blank line after the table
        new_lines = []
        inserted = False
        header_seen = False
        for i, line in enumerate(lines):
            new_lines.append(line)
            if "| Character | Folder | Current status" in line:
                header_seen = True
            if header_seen and line.strip().startswith("|") and i + 1 < len(lines):
                next_line = lines[i + 1]
                if next_line.strip() == "" or (not next_line.strip().startswith("|") and next_line.strip() != "" and not inserted):
                    new_lines.append(row + "\n")
                    inserted = True
            # If we reached the end of the table marker section (blank line after last row, before ##)
            if header_seen and line.strip() == "" and not inserted:
                # Find the last table row we just passed
                # Actually, let's just insert after the last row-like line before a blank line
                pass
        if not inserted:
            # Append at end of table rows (before the blank line after the table)
            # Simpler: find the last line matching "| <CHAR>" pattern and insert after
            pass
        # Use a simpler approach: find the last existing character row and insert after it
        result_lines = []
        inserted_row = False
        last_char_row_idx = -1
        for i, line in enumerate(lines):
            if line.strip().startswith("|") and not line.strip().startswith("|---") and not line.strip().startswith("| Character"):
                parts = line.split("|")
                if len(parts) >= 3 and parts[1].strip():
                    last_char_row_idx = i

        for i, line in enumerate(lines):
            result_lines.append(line)
            if i == last_char_row_idx and not inserted_row:
                result_lines.append(row + "\n")
                inserted_row = True

        if not inserted_row:
            # Fallback: find the separator line and insert after last char row
            pass

        path.write_text("".join(result_lines), encoding="utf-8")
    return str(path.relative_to(repo_root))


def build_decision_entry(spec: dict, created_paths: list[str]) -> str:
    """Build a decision entry for the bootstrap operation."""
    cid = spec["character_id"]
    created_list = "\n".join(f"* `{p}`" for p in sorted(created_paths))
    return f"""
## DECISION-XXXX — Bootstrap character {cid}

Date: {datetime.date.today().isoformat()}

Context:
Owner-authored JSON spec bootstrapped character {cid} via `tools/bootstrap_character.py`.

Decision:
Create {cid} character namespace with canonical folder structure and base files.

Created files:
{created_list}

No images were generated, copied, renamed, or deployed.

Next step:
{spec['next_step']}
"""


def update_decisions(repo_root: Path, spec: dict, created_paths: list[str], dry_run: bool) -> str | None:
    path = repo_root / ".voyage" / "DECISIONS.md"
    if not path.exists():
        return None
    entry = build_decision_entry(spec, created_paths)
    if not dry_run:
        content = path.read_text(encoding="utf-8")
        path.write_text(content.rstrip() + "\n" + entry, encoding="utf-8")
    return str(path.relative_to(repo_root))


def update_project_state(repo_root: Path, spec: dict, dry_run: bool) -> str | None:
    path = repo_root / ".voyage" / "PROJECT_STATE.md"
    if not path.exists():
        return None
    cid = spec["character_id"]
    if not dry_run:
        content = path.read_text(encoding="utf-8")
        # Add character mention to confirmed facts
        char_line = f"* {cid}: `{spec['current_status']}` / `CANON_PROMPTS_CREATED`; bootstrap complete, no images yet."
        if f"* {cid}:" not in content:
            # Insert after the last confirmed-fact about existing characters
            lines = content.splitlines()
            new_lines = []
            inserted = False
            for line in lines:
                new_lines.append(line)
                if line.strip().startswith("*") and ("TEXT_CANON_READY" in line or "BASE_CANON_APPROVED" in line or "CANON_READY" in line) and not inserted:
                    pass  # wait for end of character list
            # Simpler: append before "## Активные ограничения"
            if "## Активные ограничения" in content:
                content = content.replace("## Активные ограничения", f"{char_line}\n\n## Активные ограничения")
            path.write_text(content, encoding="utf-8")
    return str(path.relative_to(repo_root))


def update_current_task(repo_root: Path, spec: dict, dry_run: bool) -> str | None:
    path = repo_root / ".voyage" / "CURRENT_TASK.md"
    if not path.exists():
        return None
    cid = spec["character_id"]
    if not dry_run:
        content = path.read_text(encoding="utf-8")
        entry = f"""
## Completed task

**Task ID:** `NCC-{cid}-BOOTSTRAP-{datetime.date.today().isoformat()}`

**Final status:** `COMPLETED_BOOTSTRAP`

### Goal

Bootstrap {cid} character namespace from owner-authored JSON spec.

### Result

- Canonical folder structure created under `AI_CHARACTERS/{cid}/`.
- Base prompt files, reference presets, and metadata created.
- No images generated or deployed.
- Next step: {spec['next_step']}

---
"""
        # Insert before "## Active task" or append
        if "## Active task" in content:
            content = content.replace("## Active task", entry + "\n## Active task")
        else:
            content = content.rstrip() + "\n" + entry
        path.write_text(content, encoding="utf-8")
    return str(path.relative_to(repo_root))


# ---------------------------------------------------------------------------
# Dry-run output
# ---------------------------------------------------------------------------


def print_dry_run(spec: dict, dirs: list[str], files: list[str], modified: list[str]) -> None:
    cid = spec["character_id"]
    print(f"Character ID: {cid}")
    print()
    print("Planned directories:")
    for d in sorted(dirs):
        print(f"  {d}")
    print()
    print("Planned files:")
    for f in sorted(files):
        print(f"  {f}")
    print()
    print("Files that would be modified:")
    for m in sorted(modified):
        print(f"  {m}")
    print()
    print("Zero prompt records")
    print("No image operation")
    print("No stage/commit/push/SQLite")
    print()
    print("REPOSITORY_MODIFIED=NO")


# ---------------------------------------------------------------------------
# Apply with rollback
# ---------------------------------------------------------------------------


def apply_bootstrap(repo_root: Path, spec: dict, preflight_data: dict, transaction_dir: Path) -> None:
    """Execute bootstrap with atomicity. On failure, rollback to transaction backup."""
    cid = spec["character_id"]
    char_root = repo_root / "AI_CHARACTERS" / cid
    modifiable_paths = [
        repo_root / ".voyage" / "CHARACTER_REGISTRY.md",
        repo_root / ".voyage" / "DECISIONS.md",
        repo_root / ".voyage" / "PROJECT_STATE.md",
        repo_root / ".voyage" / "CURRENT_TASK.md",
    ]

    # Phase 1: backup modifiable files to transaction dir
    backup_dir = transaction_dir / "backup"
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup_map: dict[Path, bytes] = {}
    for p in modifiable_paths:
        if p.exists():
            backup_map[p] = p.read_bytes()
            shutil.copy2(str(p), str(backup_dir / p.name))

    created_files: list[Path] = []
    try:
        # Recheck preflight
        errors = recheck_preflight(repo_root, preflight_data["head"], preflight_data["file_hashes"])
        if errors:
            eprint("Pre-mutation recheck failed:")
            for e in errors:
                eprint(f"  {e}")
            raise RuntimeError("Pre-mutation recheck failed")

        # Create folders
        base = repo_root / "AI_CHARACTERS" / cid
        for folder in FOLDERS:
            full = base / folder
            full.mkdir(parents=True, exist_ok=True)
        for folder in GITKEEP_FOLDERS:
            full = base / folder / ".gitkeep"
            full.parent.mkdir(parents=True, exist_ok=True)
            full.write_text("", encoding="utf-8")
            created_files.append(full)

        # Create base files
        for suffix, gen_func in FILES_UNDER_06:
            content = gen_func(spec)
            path = base / "06_prompts" / f"{cid}_{suffix}"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            created_files.append(path)

        for suffix, gen_func in FILES_UNDER_10:
            content = gen_func(spec)
            path = base / "10_notes" / f"{cid}_{suffix}"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            created_files.append(path)

        # Update Voyage files
        cid = spec["character_id"]

        # Character registry
        reg_path = repo_root / ".voyage" / "CHARACTER_REGISTRY.md"
        row = build_registry_row(spec)
        reg_content = reg_path.read_text(encoding="utf-8")
        reg_lines = reg_content.splitlines(keepends=True)
        last_char_row_idx = -1
        for i, line in enumerate(reg_lines):
            if line.strip().startswith("|") and not line.strip().startswith("|---") and not line.strip().startswith("| Character"):
                parts = line.split("|")
                if len(parts) >= 3 and parts[1].strip():
                    last_char_row_idx = i
        new_reg_lines = []
        for i, line in enumerate(reg_lines):
            new_reg_lines.append(line)
            if i == last_char_row_idx:
                new_reg_lines.append(row + "\n")
        reg_path.write_text("".join(new_reg_lines), encoding="utf-8")

        # Decisions
        all_created = [str(p.relative_to(repo_root)) for p in created_files]
        all_created += [str(p.relative_to(repo_root)) for p in [base / d for d in FOLDERS]]
        dec_path = repo_root / ".voyage" / "DECISIONS.md"
        dec_entry = build_decision_entry(spec, all_created)
        dec_content = dec_path.read_text(encoding="utf-8")
        dec_path.write_text(dec_content.rstrip() + "\n" + dec_entry, encoding="utf-8")

        # Project state
        ps_path = repo_root / ".voyage" / "PROJECT_STATE.md"
        ps_content = ps_path.read_text(encoding="utf-8")
        char_line = f"* {cid}: `{spec['current_status']}` / `CANON_PROMPTS_CREATED`; bootstrap complete, no images yet."
        if "## Активные ограничения" in ps_content:
            ps_content = ps_content.replace("## Активные ограничения", f"{char_line}\n\n## Активные ограничения")
        ps_path.write_text(ps_content, encoding="utf-8")

        # Current task
        ct_path = repo_root / ".voyage" / "CURRENT_TASK.md"
        ct_content = ct_path.read_text(encoding="utf-8")
        ct_entry = f"""
## Completed task

**Task ID:** `NCC-{cid}-BOOTSTRAP-{datetime.date.today().isoformat()}`

**Final status:** `COMPLETED_BOOTSTRAP`

### Goal

Bootstrap {cid} character namespace from owner-authored JSON spec via `tools/bootstrap_character.py`.

### Result

- Canonical folder structure created under `AI_CHARACTERS/{cid}/`.
- Base prompt files, reference presets, and metadata created.
- No images generated or deployed.

### Next step

{spec['next_step']}

---
"""
        if "## Active task" in ct_content:
            ct_content = ct_content.replace("## Active task", ct_entry + "\n## Active task")
        else:
            ct_content = ct_content.rstrip() + "\n" + ct_entry
        ct_path.write_text(ct_content, encoding="utf-8")

        # Run inventory generation
        print("Running generate_inventory.py...")
        result = run([sys.executable, str(repo_root / "tools" / "generate_inventory.py")], repo_root)
        if result.returncode != 0:
            eprint(f"Inventory generation failed: {result.stderr}")
            raise RuntimeError("Inventory generation failed")

        # Run validator
        print("Running validate_visual_canon_pipeline.py...")
        result = run(
            [sys.executable, str(repo_root / "tools" / "validate_visual_canon_pipeline.py"),
             "--mode", "compatibility", "--character", cid, "--no-color"],
            repo_root,
        )
        if result.returncode not in (0,):
            eprint(f"Validator failed for {cid}: exit {result.returncode}")
            eprint(result.stdout[-2000:] if len(result.stdout) > 2000 else result.stdout)
            eprint(result.stderr[-2000:] if len(result.stderr) > 2000 else result.stderr)
            raise RuntimeError("Validator failed for new character")

        # Run git diff --check
        result = run(["git", "diff", "--check"], repo_root)
        if result.returncode != 0:
            eprint(f"git diff --check failed: {result.stderr}")
            raise RuntimeError("git diff --check failed")

    except Exception:
        # Rollback
        eprint("ROLLBACK initiated...")
        # Remove character directory
        if char_root.exists():
            shutil.rmtree(str(char_root), ignore_errors=True)
        # Restore modifiable files
        for p, original_bytes in backup_map.items():
            p.write_bytes(original_bytes)
        eprint(f"Rollback complete. Backup preserved at: {backup_dir}")
        raise

    print(f"Bootstrap apply completed for {cid}")
    print(f"Backup preserved at: {backup_dir}")
    return transaction_dir


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="NCC Character Bootstrap MVP — create a new character namespace from a JSON spec.",
    )
    parser.add_argument("--spec", type=str, default=None, help="Path to bootstrap spec JSON")
    parser.add_argument("--apply", action="store_true", help="Actually write files (default is dry-run)")
    parser.add_argument("--repo-root", type=str, default=None, help="Repository root path")
    parser.add_argument("--version", action="store_true", help="Print version and exit")
    args = parser.parse_args()

    if args.version:
        print(f"bootstrap_character.py {VERSION}")
        return 0

    if not args.spec:
        parser.error("--spec is required (unless --version)")

    # Resolve repo root
    if args.repo_root:
        repo_root = Path(args.repo_root).resolve()
    else:
        repo_root = Path(__file__).resolve().parent.parent

    if not repo_root.is_dir():
        eprint(f"CLI-001: Repository root does not exist: {repo_root}")
        return 2

    spec_path = Path(args.spec).resolve()
    if not spec_path.is_file():
        eprint(f"CLI-002: Spec file does not exist: {spec_path}")
        return 2

    # Load and validate spec
    spec = load_and_validate_spec(spec_path)
    cid = spec["character_id"]

    # Run preflight
    preflight_data = preflight(repo_root, apply_mode=args.apply)

    # Check namespace
    check_existing_namespace(repo_root, cid)

    # Plan operations
    dirs = create_folder_structure(repo_root, cid, dry_run=True)
    files = create_base_files(repo_root, spec, dry_run=True)
    modified = []
    modifiable_voyage = [
        ".voyage/CHARACTER_REGISTRY.md",
        ".voyage/DECISIONS.md",
        ".voyage/PROJECT_STATE.md",
        ".voyage/CURRENT_TASK.md",
    ]
    for p in modifiable_voyage:
        if (repo_root / p).exists():
            modified.append(p)

    if not args.apply:
        print_dry_run(spec, dirs, files, modified)
        return 0

    # Apply mode
    # Create transaction directory
    transaction_root = os.environ.get(
        "NCC_TRANSACTION_ROOT",
        r"C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\transactions",
    )
    transaction_dir = Path(transaction_root) / f"bootstrap_{cid}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    transaction_dir.mkdir(parents=True, exist_ok=True)

    try:
        apply_bootstrap(repo_root, spec, preflight_data, transaction_dir)
    except Exception as exc:
        eprint(f"Bootstrap failed: {exc}")
        return 3

    print(f"Bootstrap complete for {cid}")
    print("Remember: changes are UNSTAGED. Review with `git diff` before staging/committing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())