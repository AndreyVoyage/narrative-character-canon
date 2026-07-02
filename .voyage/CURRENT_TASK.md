# CURRENT_TASK

## Completed — NCC-KIRA-PRESET-AUDIT

Status: DONE (2026-07-02)

Goal was: verify and fix `KIRA_REFERENCE_PRESETS.json` before using KIRA in GitHub-first scene packs.

Result: file is already valid — all `text_sources` and all `reference_images` across 7 `scene_presets` resolve to existing tracked files. No fix required. See [DECISIONS.md#decision-0004](DECISIONS.md).

## Completed — AGENTS.md audit

Status: DONE (2026-07-02)

Goal was: decide whether the untracked `AGENTS.md` should be committed. Result: EDIT_BEFORE_COMMIT — file was safe and useful, two stale/ambiguous spots fixed (KIRA status line, sauna example cross-reference), then committed and pushed. See [DECISIONS.md#decision-0005](DECISIONS.md).

## Completed — NCC-ANDREY-BODY-CANON

Status: DONE (2026-07-02)

Goal: Create ANDREY body canon so ANDREY moves from `FACE_CANON_ACTIVE / BODY_PENDING` toward `CANON_READY_2D` (per ROADMAP.md §9 "Immediate next actions").

Completed steps:

* Step 1: body canon prompt kit created (`ANDREY_BODY_CANON_PROMPT.txt` + negative prompt).
* Step 2: body canon Sheet A generated and saved — `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_A_front_side_back.png`.
* Step 3: body canon Sheet B generated and saved — `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_B_pose_variations.png` (file was saved on disk as `..._pose_set.png`; renamed to `..._pose_variations.png` with explicit user approval to match the canon filename convention).
* Step 4: `ANDREY_CANON_INDEX.md` and `ANDREY_REFERENCE_PRESETS.json` updated — body canon marked ACTIVE, `body_canon` preset points at the two new sheets + face canon, and the sheets were added to `sports`, `formal`, `bar`, `sauna` presets. `portrait` preset intentionally left face-only.

Note: A duplicate candidate of Sheet A (`candidates/ANDREY_body_canon_v1_sheet_A_front_side_back_candidate_02.png`) exists but was **not** added to active canon or presets, per instruction. Do not regenerate the same body sheet type unless the user explicitly requests candidate variants.

Andrey is **not** marked `CANON_READY_2D` — control tests and `ANDREY_TEST_RESULTS.md` are still pending.

## Next — NCC-ANDREY-CONTROL-TESTS

Status: NEXT (not started)

Goal: Run controlled test generations using active face canon (`03_face_sheet/`) and active body canon (`04_body_sheet/`) before marking Andrey as `CANON_READY_2D`.

Per [SCENE_REQUEST_RULES.md](SCENE_REQUEST_RULES.md), preparing test prompts/structure does not authorize generation — actual control-test image generation starts only when the user explicitly requests it.

Suggested first step (structure only, no generation): create `ANDREY_TEST_RESULTS.md` skeleton in `10_notes/` and control-test prompts in `06_prompts/`, mirroring the structure already used for KIRA (`KIRA_TEST_RESULTS.md.txt`, `canon_tests/01_evening_embankment/`, `02_sports_yoga/`, `03_portrait_expression/`).

Forbidden:

* do not generate the KIRA + ANDREY sauna scene — it is EXAMPLE, not REQUESTED (see [SCENE_REQUEST_RULES.md](SCENE_REQUEST_RULES.md))
* do not modify, rename, move, or delete existing active canon images without explicit request
* do not create fake refs or mark placeholders/drafts as approved canon without explicit user approval
* do not regenerate/duplicate body canon sheets unless the user explicitly requests candidate variants
