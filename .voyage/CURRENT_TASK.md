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

Note: The duplicate candidate of Sheet A was moved to LOCAL_STORAGE during housekeeping and is not part of active repo canon or presets. Do not regenerate the same body sheet type unless the user explicitly requests candidate variants.

Andrey is **not** marked `CANON_READY_2D` — control tests and `ANDREY_TEST_RESULTS.md` are still pending.

## Completed — NCC-ANDREY-CONTROL-TESTS

Status: DONE (2026-07-02)

Goal: Run controlled tests using active face canon (`03_face_sheet/`) and active body canon (`04_body_sheet/`) before marking Andrey as `CANON_READY_2D`.

Completed:

* TEST 01 generated and approved.
* TEST 02 generated and approved.
* TEST 03 generated and approved.
* TEST 04 generated and approved.
* TEST 05 generated and approved.
* TEST 06 generated and approved.
* `ANDREY_TEST_RESULTS.md` updated.
* `ANDREY_CANON_INDEX.md` updated.
* `ANDREY_REFERENCE_PRESETS.json` updated.

Result:
ANDREY is now CANON_READY_2D.

## Current — NCC-KIRA-ANDREY-JOINT-CONTROL-TESTS

Status: SETUP_DONE / GENERATION_PENDING

Goal:
Verify KIRA and ANDREY together after both reached CANON_READY_2D.

Completed:

* Joint control test prompt document created.
* Joint test result tracking document created.
* Joint test folders created.

Next:
Generate JOINT TEST 01 only after explicit user request.

Forbidden:

* do not generate sauna scene automatically;
* do not treat old sauna example as requested;
* do not blend identities;
* do not mark joint tests approved before review;
* do not create image placeholders.

## Next-later — NCC-ANDREY-3D-REFERENCE-PACK

Status: POSTPONED

Next goal:
Prepare 3D reference pack structure and requirements using active face canon, body canon and approved control tests.

Forbidden:

* do not regenerate approved control tests unless user explicitly requests candidate variants;
* do not change active canon images;
* do not mark private/local-only outputs as public canon.
