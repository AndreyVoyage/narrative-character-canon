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

## Completed — NCC-KIRA-ANDREY-JOINT-CONTROL-TESTS

Status: DONE / JOINT_CONTROL_TESTS_APPROVED (2026-07-02)

Goal:
Verify KIRA and ANDREY together after both reached CANON_READY_2D.

Completed:

* JOINT TEST 01 generated and approved.
* JOINT TEST 02 generated and approved.
* JOINT TEST 03 generated and approved after wrong gym scene rejection.
* JOINT TEST 04 generated and approved after wrong living room scene rejection.
* `KIRA_ANDREY_JOINT_TEST_RESULTS.md` updated.
* `KIRA_ANDREY_JOINT_CANON_INDEX.md` created.
* `KIRA_ANDREY_REFERENCE_PRESETS.json` created.

Result:
KIRA + ANDREY joint control tests are approved.

## Completed — NCC-VOYAGE-SQLITE-MEMORY

Status: DONE / SQLITE_MEMORY_SETUP_DONE (2026-07-02)

Completed:

* Local SQLite memory schema created.
* Local SQLite DB initialized outside repo.
* Memory status tool created.
* Memory export tool created.
* `CONTEXT_SNAPSHOT.md` exported.
* `STATE_EXPORT.json` exported.
* `EVENTS_EXPORT.jsonl` exported.
* SQLite workflow documented.

Result:
Voyage-lite structured memory is available for future character, pair, scene, 3D and decision workflows.

DB policy:
SQLite DB is local runtime memory and must not be committed.

## Current — NEXT DIRECTION

Status: PENDING DECISION

Next options:

1. Duo scene packs for `KIRA_ANDREY`
2. `NCC-ANDREY-3D-REFERENCE-PACK`
3. `NCC-KIRA-3D-REFERENCE-PACK`
4. Next character canon pack
5. Continue SQLite memory automation

Forbidden:

* do not use rejected/wrong-scene joint outputs as canon;
* do not overwrite approved joint tests;
* do not treat Kira heels as changing barefoot canon height.

## Next-later — NCC-ANDREY-3D-REFERENCE-PACK

Status: POSTPONED

Next goal:
Prepare 3D reference pack structure and requirements using active face canon, body canon and approved control tests.

Forbidden:

* do not regenerate approved control tests unless user explicitly requests candidate variants;
* do not change active canon images;
* do not mark private/local-only outputs as public canon.
