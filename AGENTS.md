# AGENTS.md — narrative-character-canon

> This file is for AI coding agents working on the repository. Read it first before making changes.

## 1. Project overview

`narrative-character-canon` is a private, Git-tracked asset repository for AI-generated visual references of characters used in the Narrative / Voyage project. It is **not a compiled software product**. It is a curated, version-controlled library of character identity, reference sheets, prompt kits, generation tests, and future 3D/Blender preparation materials.

The repository is the single source of truth for:

- Character visual identity (text + images).
- Face, body, outfit, and expression reference sheets.
- Prompt kits and negative prompts.
- Control / canon test results.
- 3D reference packs and model specs (planned).
- Automation scripts for assembling scene reference packs.
- Universal visual-canon pipeline policy, schemas, and workflow (see `docs/NCC_VISUAL_CANON_WORKFLOW.md` and `configs/visual_canon/`).

All work is organised around per-character folders under `AI_CHARACTERS/`. Each character follows the same 10-subfolder layout so that tools, agents, and humans can navigate predictably.

### Characters currently in the repository

| Character | Status |
|---|---|
| ANDREY | `CANON_READY_2D` / `PROMPT_PIPELINE_ACTIVE` |
| ANDREY_JUNIOR | `BASE_CANON_APPROVED` / `CONTROL_TESTS_APPROVED` / `PROMPT_PIPELINE_ACTIVE` — son-version of ANDREY Senior, public_filtered only |
| KIRA | `CANON_READY_2D` / `PROMPT_PIPELINE_ACTIVE_CORE` |
| MARINA | `TEXT_CANON_READY` / `CANON_PROMPTS_CREATED` |
| NIKA | `TEXT_CANON_READY` / `CANON_PROMPTS_CREATED` |
| OLGA | `BASE_CANON_APPROVED` / `CONTROL_TESTS_APPROVED` (Tests 01–09 published) / `PROMPT_PIPELINE_ACTIVE` |
| SERGEY | `TEXT_CANON_READY` / `CANON_PROMPTS_CREATED` — secondary |
| MAKSIM | `TEXT_CANON_READY` / `CANON_PROMPTS_CREATED` — secondary |
| EGOR | `TEXT_CANON_READY` / `CANON_PROMPTS_CREATED` — secondary |

Joint pair: `KIRA + ANDREY` → `JOINT_CONTROL_TESTS_APPROVED` / `DUO_SCENE_PACKS_APPROVED`.

All future generation, selection, and deployment of visual-canon outputs must follow the universal pipeline in `docs/NCC_VISUAL_CANON_WORKFLOW.md`.

### Overall project phases

- **Phase 1 (current):** Weak laptop + cloud AI services. The repository is edited locally; heavy generation happens in browser/cloud tools. Documented in `PHASE_1_CURRENT_LAPTOP_CLOUD_PIPELINE.md`.
- **Phase 2 (future):** Powerful local workstation + local AI/3D/video pipeline (ComfyUI, Stable Diffusion/FLUX-style models, Blender, local LLMs). Documented in `PHASE_2_LOCAL_AI_WORKSTATION_PIPELINE.md`.

Read `ROADMAP.md` for priorities, definition-of-done criteria, and immediate next steps.

### Character-data source hierarchy, conflicts, and project boundary

This hierarchy governs **character facts used by this repository**; it is separate from the
repository-document authority order in `docs/NCC_VISUAL_CANON_WORKFLOW.md`:

1. **L1 — NCC repository visual canon.** `narrative-character-canon` is the primary source of truth
   for visual appearance, identity anchors, proportions, outfits, approved references, and visual
   prompt constraints.
2. **L2 — VNE/persona narrative sources.** `voyage-narrative-engine` or persona-style narrative
   sources are secondary. As fallback sources, they may be used only when the exact fact is absent in NCC.
   A known NCC/VNE contradiction is handled separately by the domain conflict rule below. The source
   must be explicitly provided or authorized; do not switch projects or continue foreign-project
   implementation during an NCC task.
3. **L3 — approved local photo/reference archives.** Use only approved local archives as tertiary
   visual support and only when the task boundary explicitly allows access.
4. **L4 — approved prompts, handoffs, or chat-derived facts.** Use only as reconstructed sources;
   label them honestly as reconstructed rather than exact primary canon.

If the fact is absent at every allowed level, record `unknown_requires_user_confirmation`; do not
guess. Resolve conflicts by domain:

- Visual appearance conflict: NCC wins.
- Biography, narrative-role, or relationship conflict: VNE/persona narrative authority wins.
- Unresolved or cross-domain contradiction: human confirmation is required; do not silently choose.

**Project boundary:** while working in `narrative-character-canon`, operate only on this project. If
a report or implementation task from another project appears, treat it as
cross-project contamination, stop, warn the user, and do not continue that foreign development here.

Internal factual values may be translated into safe visual prompt wording without changing the
underlying canon. For OLGA, preserve the approved generation-compensation rule: because generation
tends to reduce chest volume, prompt her bust about one visual size fuller than the intended final
result. This is prompt-surface compensation, not a canon change; avoid numeric measurements or cup
sizing.

## 2. Repository structure

```text
.
├── AI_CHARACTERS/              # One folder per character
│   └── <CHARACTER>/            # Character-specific assets
│       ├── 01_refs_raw/        # Raw downloaded/generated reference images
│       ├── 02_best_refs/       # Approved best references
│       ├── 03_face_sheet/      # Face canon sheets; expressions/ subfolder
│       ├── 04_body_sheet/      # Body canon sheets; candidates/ subfolder
│       ├── 05_outfits/         # Outfit canons: casual, formal, evening_dress, sports_look, scene_outfits, candidates
│       ├── 06_prompts/         # Prompt kits, negative prompts, prompt indexes, run logs
│       ├── 07_generated/       # Generated images: canon_tests/, drafts/, rejected/
│       ├── 08_masks/           # Segmentation masks / inpaint masks
│       ├── 09_blender/         # Blender files, blockouts, reference packs (future)
│       └── 10_notes/           # Canon index, identity, raw file map, test results, reference presets JSON
├── configs/                    # Universal machine-readable policy and JSON schemas
│   └── visual_canon/           # `pipeline_policy.json` + `prompt_record.schema.json` + `character_manifest.schema.json`
├── docs/                       # Additional workflow documentation
├── tools/                      # Python / PowerShell automation scripts
├── INVENTORY.md                # Auto-generated file/folder inventory
├── ROADMAP.md                  # Project roadmap and priorities
├── PHASE_1_CURRENT_LAPTOP_CLOUD_PIPELINE.md
├── PHASE_2_LOCAL_AI_WORKSTATION_PIPELINE.md
└── README.md
```

### Important generated / backup files

- `INVENTORY.md` is regenerated manually when the repository changes; backup copies (`*.backup_*`) are kept alongside it.
- `README.md.backup_*` and `INVENTORY.md.backup_*` files are ignored by Git via `.gitignore`.
- `*.zip` archives in the root are manual snapshots and are ignored by Git.

## 3. Technology stack

- **Version control:** Git with Git LFS for binary visual assets.
- **Tracked binary formats (LFS):** `.png`, `.jpg`, `.jpeg`, `.webp`, `.psd`, `.mp4`, `.mov`.
- **Scripting:** Python 3 (standard library only) and PowerShell 5+ / PowerShell Core.
- **Editors / control-room tools used by the owner:** VS Code, ChatGPT, Kimi Code / Codex, XnView MP, Krita, Blender, PureRef, Upscayl, ComfyUI (Phase 2).
- **No package manager files:** There is no `pyproject.toml`, `requirements.txt`, `package.json`, `Cargo.toml`, or similar. Python scripts intentionally use only the standard library.

## 4. Build, run, and test commands

There is no build step. The repository is a collection of assets and scripts.

### Run the scene reference pack tool

The main automation tool is `tools/build_scene_reference_pack.py`. It reads per-character `*_REFERENCE_PRESETS.json` files and produces a local scene pack with markdown, raw GitHub links, an embedded prompt, and a JSON summary.

PowerShell wrapper (recommended on Windows):

```powershell
.\tools\build_scene_reference_pack.ps1 `
    -Characters "KIRA,ANDREY" `
    -Scene "sauna" `
    -Description "Кира и Андрей в сауне разговаривают, укрытые по пояс полотенцем"
```

Direct Python invocation:

```powershell
python .\tools\build_scene_reference_pack.py `
    --characters KIRA,ANDREY `
    --scene sauna `
    --description "Кира и Андрей в сауне разговорывают, укрытые по пояс полотенцем"
```

Default paths in the scripts:

- Repo root: `C:\DEV\Narrative\narrative-character-canon`
- Output root: `C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\scene_packs`

This is an illustrative command only — see `.voyage/SCENE_REQUEST_RULES.md` before treating any scene as a real generation request.

Output files per scene pack:

- `SCENE_REFERENCE_PACK.md`
- `SCENE_RAW_LINKS.md`
- `SCENE_PROMPT.txt`
- `SCENE_PACK.json`

### Run the visual-canon pipeline validator

Read-only validator: `tools/validate_visual_canon_pipeline.py`. It checks prompt-run JSONL logs, policy/schema conformance, IDs, references, output paths, roles, and local-only path protection. It never modifies the repository.

```powershell
py -3 tools\validate_visual_canon_pipeline.py --mode compatibility --no-color
py -3 tools\validate_visual_canon_pipeline.py --mode strict --no-color
```

Tests are in `tests/visual_canon/` and use the standard-library `unittest` runner:

```powershell
py -3 -m unittest discover -s tests/visual_canon -v
```

### Run the visual-canon deploy tool

Always run the deploy tool in its default dry-run mode first. Use explicit `--apply` only after
human approval of the request and deterministic plan:

```powershell
py -3 tools\deploy_visual_canon_result.py --request <external-request.json>
py -3 tools\deploy_visual_canon_result.py --request <external-request.json> --apply
```

The tool leaves validated changes unstaged. It never modifies Voyage, Decisions, Inventory or
SQLite, and it never stages, commits or pushes.

### Inventory regeneration

`INVENTORY.md` is not regenerated automatically. When asked to update it, a script or agent should walk the `AI_CHARACTERS/` tree and rewrite `INVENTORY.md` with the current folder/file tree, file counts, extensions summary, and file list. Backup the old file first using the naming pattern `INVENTORY.md.backup_YYYYMMDD_HHMMSS`.

### Testing

The repository now has a standard-library `unittest` suite in `tests/visual_canon/` for the visual-canon pipeline validator. Run it whenever `tools/validate_visual_canon_pipeline.py` changes.

"Tests" in the creative sense remain visual control tests: generating images and reviewing them for identity drift against the canon.

When modifying scripts, verify by running them with realistic arguments and checking that:

- Output files are created in the expected local directory.
- JSON output is valid.
- No new files are written inside the repository unless explicitly requested.
- Generated markdown references only Git-tracked files.
- `tools/validate_visual_canon_pipeline.py` still passes against the real repo and its own unit tests.

## 5. Code and documentation style guidelines

### Language

- **Code comments and script docstrings:** English.
- **Markdown documentation:** Mixed. High-level README is English; detailed pipeline/roadmap docs are mostly Russian. Prefer to match the language of the file you are editing.
- **AI-facing canon files (identity, prompts, indices):** English.

### File naming conventions

Character assets use uppercase character ID prefixes. Examples from the repository:

```text
<CHARACTER>_RAW_<NN>_<description>.png
<CHARACTER>_face_canon_v<version>_sheet_<A|B>_<desc>.png
<CHARACTER>_body_canon_v<version>_sheet_<A|B>_<desc>.png
<CHARACTER>_expressions_v<version>_sheet_<A|B>_<desc>.png
<CHARACTER>_test<NN>_<scene>_v<version>[_MAIN|_ALT|_APPROVED].png
<CHARACTER>_CANON_INDEX.md
<CHARACTER>_IDENTITY.txt
<CHARACTER>_RAW_FILE_MAP.md
<CHARACTER>_REFERENCE_PRESETS.json
<CHARACTER>_TEST_RESULTS.md
<CHARACTER>_3D_REFERENCE_PACK.md   (planned)
<CHARACTER>_3D_MODEL_SPEC.md        (planned)
```

- Use underscores, not spaces.
- Keep filenames descriptive.
- Append status suffixes such as `_MAIN`, `_ALT`, `_APPROVED`, `_REFERENCE_ONLY`, `_FINAL`, `_candidate`.

### Folder discipline

- Put raw downloads in `01_refs_raw/`.
- Put approved best references in `02_best_refs/`.
- Put face sheets in `03_face_sheet/`; expression sheets in `03_face_sheet/expressions/`.
- Put body sheets in `04_body_sheet/`; candidates in `04_body_sheet/candidates/`.
- Put outfit canons in the relevant `05_outfits/<category>/` folder; candidates in `05_outfits/candidates/`.
- Put prompt files in `06_prompts/`.
- Put generated test images in `07_generated/canon_tests/<scene>/`; drafts in `drafts/`; rejected in `rejected/`.
- Put masks in `08_masks/`.
- Put Blender files and 3D reference packs in `09_blender/`.
- Put notes, indices, and JSON presets in `10_notes/`.

### Markdown style

- Use ATX headings (`#`).
- Use horizontal rules (`---`) to separate major sections in canon index files.
- Use bullet lists for file references and rules.
- Keep canon index files explicit: state status, purpose, active files, and next steps.

### JSON style (reference presets)

Each `*_REFERENCE_PRESETS.json` follows this schema:

```json
{
  "character": "CHARACTER_ID",
  "version": "v1.0",
  "last_updated": "YYYY-MM-DD",
  "root": "AI_CHARACTERS/CHARACTER_ID",
  "text_sources": {
    "identity": "AI_CHARACTERS/CHARACTER_ID/10_notes/CHARACTER_ID_IDENTITY.txt",
    "canon_index": "AI_CHARACTERS/CHARACTER_ID/10_notes/CHARACTER_ID_CANON_INDEX.md",
    ...
  },
  "scene_presets": {
    "scene_name": {
      "description": "...",
      "reference_images": [
        "AI_CHARACTERS/CHARACTER_ID/03_face_sheet/..."
      ],
      "prompt_goal": "..."
    }
  }
}
```

Rules for presets:

- Only reference Git-tracked files.
- Do not include `.gitkeep`, guessed paths, placeholders, or untracked files.
- Use forward slashes in all paths inside JSON.

## 6. Workflow instructions

### When adding a new character

1. Create `AI_CHARACTERS/<CHARACTER>/` with all 10 subfolders and relevant `candidates/` subfolders.
2. Add `.gitkeep` files to empty folders that must be preserved.
3. Create `10_notes/<CHARACTER>_REFERENCE_PRESETS.json` with at least the character metadata.
4. Create `10_notes/<CHARACTER>_IDENTITY.txt` and `10_notes/<CHARACTER>_CANON_INDEX.md` when canon work begins.
5. Update `README.md` if the character list changes.
6. Update `ROADMAP.md` status if needed.
7. Regenerate `INVENTORY.md` and keep a backup.
8. Commit.

### When approving a new reference image

1. Rename the file according to the naming convention.
2. Move it to the correct subfolder.
3. Update the character's `*_CANON_INDEX.md` to mark it active.
4. Update `*_REFERENCE_PRESETS.json` if the image should be used by the scene pack tool.
5. Regenerate `INVENTORY.md`.
6. Commit.

### When running the scene pack tool

1. Verify the requested scene exists in each character's presets or has a valid fallback.
2. Run the tool and inspect `SCENE_REFERENCE_PACK.md` for `MISSING` or `NOT TRACKED` warnings.
3. Fix any missing files or presets before generation.
4. Do not commit the generated scene packs — they live in `LOCAL_STORAGE` outside the repository.

## 7. Security and sensitive content considerations

- This is a **private repository**. Do not push sensitive character materials to public repositories.
- Base character canon must stay neutral, reusable, and production-safe.
- Adult/private scene outputs must be kept separate from core canon. Use the private workflow structure described in `PHASE_1_CURRENT_LAPTOP_CLOUD_PIPELINE.md` (outside the repo under `LOCAL_STORAGE`) and never commit such outputs.
- Only adult characters may appear in adult/private scenes.
- Do not commit `*.zip`, `*.backup_*`, `Thumbs.db`, `desktop.ini`, or `.DS_Store` files. These are already ignored.
- Large binary assets must be tracked by Git LFS, not stored as plain Git blobs. This is enforced by `.gitattributes`.
- When editing scripts, avoid writing files outside the repo root or `LOCAL_STORAGE` paths unless explicitly requested.

## 8. Common agent tasks

| Task | What to do |
|---|---|
| Update inventory | Walk `AI_CHARACTERS/`, rewrite `INVENTORY.md`, backup old file, commit. |
| Bootstrap a new character | Use `tools/bootstrap_character.py` with an owner-authored JSON spec; dry-run first, then `--apply`. Never run apply on the real repo without explicit human approval. |
| Add a new character (manual) | Create folder structure, `.gitkeep` files, preset JSON, identity + canon index skeletons, update README/ROADMAP, regenerate inventory, commit. |
| Update a preset | Edit `<CHARACTER>_REFERENCE_PRESETS.json`; verify every `reference_images` path exists and is tracked; do not add placeholders. |
| Update canon index | Edit `<CHARACTER>_CANON_INDEX.md`; keep status fields, active file lists, and next steps accurate. |
| Fix a script bug | Edit `tools/build_scene_reference_pack.py` or `.ps1`; run a test invocation; do not commit output packs. |
| Validate pipeline state | Run `py -3 tools/validate_visual_canon_pipeline.py --no-color`; fix errors before commit. |
| Maintain validator | Edit `tools/validate_visual_canon_pipeline.py`; add/update tests in `tests/visual_canon/`; run `py -3 -m unittest discover -s tests/visual_canon -v`. |
| Apply universal visual-canon pipeline | Read `docs/NCC_VISUAL_CANON_WORKFLOW.md` first; follow ID reservation, reference-first, one-operation deploy, and validation rules. |
| Prepare 3D reference pack | Create `<CHARACTER>_3D_REFERENCE_PACK.md` and `<CHARACTER>_3D_MODEL_SPEC.md` in `10_notes/`; collect refs in `09_blender/01_reference_pack/`. |

## 9. Key files to read for context

| File | Purpose |
|---|---|
| `README.md` | Quick project summary and documentation index. |
| `ROADMAP.md` | Priorities, definition-of-done, next actions. |
| `PHASE_1_CURRENT_LAPTOP_CLOUD_PIPELINE.md` | Current workflow: laptop + cloud AI. |
| `PHASE_2_LOCAL_AI_WORKSTATION_PIPELINE.md` | Future local AI/3D/video pipeline. |
| `docs/GITHUB_REFERENCE_PACK_WORKFLOW.md` | How the scene reference pack tool works. |
| `INVENTORY.md` | Current file tree and asset inventory. |
| `docs/NCC_VISUAL_CANON_WORKFLOW.md` | Universal visual-canon pipeline (generation, selection, deploy, validation, sync). |
| `configs/visual_canon/pipeline_policy.json` | Machine-readable policy for IDs, verdicts, storage/content tiers, and concurrency. |
| `configs/visual_canon/prompt_record.schema.json` | JSON Schema for one-record-per-prompt-ID JSONL entries. |
| `configs/visual_canon/character_manifest.schema.json` | JSON Schema for durable per-character pipeline manifests. |
| `AI_CHARACTERS/ANDREY/10_notes/ANDREY_CANON_INDEX.md` | Example of a full canon index. |
| `AI_CHARACTERS/ANDREY/10_notes/ANDREY_REFERENCE_PRESETS.json` | Example of an active preset file. |

## 10. Contact / ownership

This is a personal creative project. Strategic decisions (approve/regenerate, canon changes, roadmap priorities) are made by the repository owner through ChatGPT as the control room. Agents such as Kimi Code / Codex perform local edits, validation, inventory updates, and safe commits under those decisions.
