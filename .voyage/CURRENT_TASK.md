# CURRENT_TASK

## Completed — NCC-KIRA-PRESET-AUDIT

Status: DONE (2026-07-02)

Goal was: verify and fix `KIRA_REFERENCE_PRESETS.json` before using KIRA in GitHub-first scene packs.

Result: file is already valid — all `text_sources` and all `reference_images` across 7 `scene_presets` resolve to existing tracked files. No fix required. See [DECISIONS.md#decision-0004](DECISIONS.md).

## Completed — AGENTS.md audit

Status: DONE (2026-07-02)

Goal was: decide whether the untracked `AGENTS.md` should be committed. Result: EDIT_BEFORE_COMMIT — file was safe and useful, two stale/ambiguous spots fixed (KIRA status line, sauna example cross-reference), then committed and pushed. See [DECISIONS.md#decision-0005](DECISIONS.md).

## In progress — NCC-ANDREY-BODY-CANON

Status: STEP 1 DONE, STEP 2 NOT STARTED

Goal: Create ANDREY body canon so ANDREY moves from `FACE_CANON_ACTIVE / BODY_PENDING` to `CANON_READY_2D` (per ROADMAP.md §9 "Immediate next actions").

### Step 1 — Prompt kit (DONE, 2026-07-02)

Created, no images generated:

* `AI_CHARACTERS/ANDREY/06_prompts/ANDREY_BODY_CANON_PROMPT.txt` — Sheet A (front/side/back/3-4 view) and Sheet B (walking/relaxed standing/seated/3-4 pose) prompts, built from `ANDREY_IDENTITY.txt` BODY CANON section.
* `AI_CHARACTERS/ANDREY/06_prompts/ANDREY_BODY_CANON_NEGATIVE_PROMPT.txt`.

### Step 2 — Generate and review body canon sheets (NEXT, requires explicit request)

Per [SCENE_REQUEST_RULES.md](SCENE_REQUEST_RULES.md), having a prompt kit ready does not authorize generation — this step starts only when the user explicitly asks to generate the body canon sheets.

Target outputs (status GENERATED_DRAFT until approved):

* `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_A_front_side_back.png`
* `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_B_pose_variants.png`

Allowed files once generation is requested:

* `AI_CHARACTERS/ANDREY/07_generated/drafts/` (draft outputs first)
* `AI_CHARACTERS/ANDREY/04_body_sheet/` (only after explicit approval)
* `AI_CHARACTERS/ANDREY/10_notes/ANDREY_CANON_INDEX.md` (update after approval)
* `AI_CHARACTERS/ANDREY/10_notes/ANDREY_REFERENCE_PRESETS.json` (`body_canon` preset, update after approval)

Optional docs to update after approval:

* `.voyage/PROJECT_STATE.md`
* `.voyage/CHARACTER_REGISTRY.md`
* `.voyage/DECISIONS.md`

Forbidden:

* do not generate the KIRA + ANDREY sauna scene — it is EXAMPLE, not REQUESTED (see [SCENE_REQUEST_RULES.md](SCENE_REQUEST_RULES.md))
* do not modify, rename, move, or delete existing images
* do not create fake refs or mark placeholders/drafts as approved canon without explicit user approval

Expected next report when Step 2 is picked up:

* draft body canon sheets generated and reviewed against `ANDREY_IDENTITY.txt` BODY CANON section and face canon for identity drift
* explicit APPROVED_AS_CANON / REJECTED decision per [SCENE_REQUEST_RULES.md](SCENE_REQUEST_RULES.md) status vocabulary
* `ANDREY_CANON_INDEX.md` and `ANDREY_REFERENCE_PRESETS.json` updated only if approved
* `INVENTORY.md` regenerated
* git status after
