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

## Completed — NCC-VOYAGE-SQLITE-RECORD-COMMAND

Status: DONE / RECORD_COMMAND_READY (2026-07-02)

Completed:

* `tools/voyage_memory_record.py` created.
* Record command supports `event`/`task`/`decision`/`commit`/`character`/`pair`/`artifact`.
* Dry-run verified.
* Test `MEMORY_RECORD_TOOL_ADDED` event recorded.
* `NCC-VOYAGE-SQLITE-RECORD-COMMAND` task recorded.
* `DECISION-0015` recorded in SQLite.
* Memory exports regenerated.

Result:
Voyage-lite SQLite memory can now be updated incrementally after future workflows.

## Completed — NCC-VOYAGE-SQLITE-RECORD-COMMAND

Status: DONE / RECORD_COMMAND_READY (2026-07-02)

Completed:

* `tools/voyage_memory_record.py` created.
* Record command supports `event`/`task`/`decision`/`commit`/`character`/`pair`/`artifact`.
* Dry-run verified.
* Test `MEMORY_RECORD_TOOL_ADDED` event recorded.
* `NCC-VOYAGE-SQLITE-RECORD-COMMAND` task recorded.
* `DECISION-0015` recorded in SQLite.
* Memory exports regenerated.

Result:
Voyage-lite SQLite memory can now be updated incrementally after future workflows.

## Completed — NCC-KIRA-ANDREY-DUO-SCENE-PACKS

Status: DONE / DUO_SCENE_PACKS_APPROVED (2026-07-02)

Goal:
Generate and approve six KIRA + ANDREY duo scene packs after joint control tests passed.

Completed:

* SCENE PACK 01 generated and approved.
* SCENE PACK 02 generated and approved.
* SCENE PACK 03 generated and approved.
* SCENE PACK 04 generated and approved.
* SCENE PACK 05 generated and approved.
* SCENE PACK 06 generated across versions; v4 selected and approved.
* Scene pack results updated.
* Scene pack index updated.
* Scene pack JSON spec updated.
* `KIRA_ANDREY_REFERENCE_PRESETS.json` updated with `duo_scene_packs` preset.
* SQLite memory records added.
* Memory exports regenerated.

Result:
KIRA + ANDREY duo scene packs are approved.

Next:
Choose one:

1. Additional KIRA_ANDREY duo scene packs
2. KIRA_ANDREY body/wardrobe/context refs
3. ANDREY 3D reference pack
4. KIRA 3D reference pack
5. Next character canon pack

Forbidden:

* do not use SCENE PACK 06 v1/v2/v3 as canon;
* do not overwrite approved scene pack outputs;
* do not treat Kira heels as changing barefoot canon height;
* do not include sauna unless explicitly requested.

## Completed — NCC-ANDREY-JUNIOR-CANON-SETUP

Status: DONE / SETUP_COMMITTED (2026-07-03)

Character:
ANDREY_JUNIOR

Completed:

* ANDREY_JUNIOR folder structure created.
* Identity draft created.
* Canon index created.
* Test result tracker created.
* Reference presets JSON created.
* Canon generation prompt pack created.
* Planned solo control test folders created.
* No images generated in setup step.

Result:
ANDREY_JUNIOR canon workflow is ready for generation.

## Completed — NCC-ANDREY-JUNIOR-BASE-CANON-AND-CONTROL-TESTS

Status: DONE / CONTROL_TESTS_APPROVED (2026-07-04)

Character:
ANDREY_JUNIOR

Completed:

* Son-version identity approved.
* Face canon sheet generated and approved.
* Expression sheet generated and approved.
* Body canon sheets A and B generated and approved.
* Solo control tests 01–09 generated and approved.
* Test 06 v2 approved after v1 father proportion drift.
* Test 08 approved with stronger Andrey Senior references.
* Notes, prompts and reference presets updated to son-version.
* SQLite memory updated.
* Memory exports regenerated.

Result:
ANDREY_JUNIOR son-version base canon and control tests are approved locally.

Next:
Start OLGA canon setup only after explicit user request.

Forbidden:

* do not confuse ANDREY_JUNIOR with ANDREY Senior;
* do not revert to old adult/20+ direction as active canon;
* do not make him tall or bulky;
* do not start Olga until explicitly requested.

## Completed — NCC-OLGA-CANON-SETUP

Status: DONE / SETUP_COMMITTED (2026-07-04)

Character:
OLGA

Completed:

* OLGA folder structure created.
* Identity draft created.
* Canon index created.
* Test result tracker created.
* Reference presets JSON created.
* Prompt pack created.
* No images generated in setup step.

Result:
OLGA canon setup was complete and ready for controlled generation.

## Completed — NCC-OLGA-BASE-CANON-CONTROL-TESTS-PROMPT-PIPELINE

Status: DONE / BASE_CANON_APPROVED (2026-07-05)

Character:
OLGA

Completed:

* OLGA primary selected face reference added.
* OLGA face canon sheet generated and approved.
* OLGA expression sheet generated and approved.
* OLGA body canon sheets A and B generated and approved.
* OLGA control tests 01–04 generated and approved.
* OLGA prompt index created.
* OLGA working scene prompts file created.
* OLGA prompt run log JSONL created.
* OLGA canon index, test results and reference presets updated.
* SQLite memory updated.
* Memory exports regenerated.

Result:
OLGA base canon and initial control tests are approved locally. Prompt logging is normalized.

Next:
Continue OLGA controlled scene testing only after prompt_id logging is active for every generation.

Forbidden:

* do not generate images automatically;
* do not use nude, lingerie, transparent, fetish or erotic contexts;
* do not make OLGA look too young;
* do not exaggerate body proportions;
* do not drift into bodybuilder build;
* do not record a generation without a prompt_id, reference map, output path and verdict.

## Completed — NCC-OLGA-TEST05-06-ID-FIX-AND-PROMPT-LOG

Status: DONE / CONTROL_TESTS_UPDATED (2026-07-05)

Character: OLGA

Completed:

* Normalized OLGA test05/test06 filenames to match folder IDs.
* Moved unlabeled raw `1.png` to `AI_CHARACTERS/OLGA/08_rejected/OLGA_business_interior_raw_1_unlabeled_REJECTED.png`.
* Updated `OLGA_PROMPT_INDEX.md` with prompt IDs `OLGA_TEST05_BUSINESS_INTERIOR_V1` and `OLGA_TEST06_INDOOR_LOUNGE_CONVERSATION_AJ_V1`.
* Updated `OLGA_WORKING_SCENE_PROMPTS.md` with reconstructed prompts and reference maps.
* Appended two valid JSONL records to `OLGA_PROMPT_RUN_LOG.jsonl`.
* Updated `OLGA_CANON_INDEX.md`, `OLGA_TEST_RESULTS.md`, and `OLGA_REFERENCE_PRESETS.json`.
* Fixed duplicate OLGA row in `.voyage/CHARACTER_REGISTRY.md`.
* Recorded task, decision, event, and artifact updates in SQLite memory.
* Regenerated `.voyage` memory exports.
* Regenerated `INVENTORY.md`.

Result:

OLGA now has 6 approved control tests (01–06) with consistent IDs, prompt pipeline records, and reference presets.

Next:

Continue controlled scene testing with prompt_id logging.

Forbidden:

* Do not generate images automatically.
* Do not use nude, lingerie, transparent, fetish or erotic contexts.
* Do not make OLGA look too young.
* Do not exaggerate body proportions.
* Do not drift into bodybuilder build.
* Do not record a generation without `prompt_id`, reference map, output path and verdict.

## Completed — NCC-ANDREY-JUNIOR-PROMPT-PIPELINE-BACKFILL

Status: DONE / PROMPT_PIPELINE_ACTIVE (2026-07-06)

Character: ANDREY_JUNIOR

Completed:

* Created `ANDREY_JUNIOR_PROMPT_INDEX.md` with 13 active prompt IDs.
* Created `ANDREY_JUNIOR_WORKING_SCENE_PROMPTS.md` with exact visible prompts (12) and one reconstructed prompt (body canon B).
* Created `ANDREY_JUNIOR_PROMPT_RUN_LOG.jsonl` with 13 valid JSONL records.
* Updated `ANDREY_JUNIOR_CANON_GENERATION_PROMPTS.txt` with pointer to normalized pipeline.
* Updated `ANDREY_JUNIOR_REFERENCE_PRESETS.json` with `prompt_pipeline` section.
* Updated `ANDREY_JUNIOR_CANON_INDEX.md` and `ANDREY_JUNIOR_TEST_RESULTS.md` with prompt IDs.
* Updated `ANDREY_JUNIOR_IDENTITY_DRAFT.md` with pipeline pointer.
* Fixed `CHARACTER_REGISTRY.md` row for ANDREY_JUNIOR.
* Recorded task/decision/event/artifacts in SQLite memory.
* Regenerated memory exports and `INVENTORY.md`.

Result:

ANDREY_JUNIOR now has a normalized prompt pipeline matching the OLGA standard.

Next:

Backfill prompt pipeline for ANDREY Senior, then KIRA, before any folder schema migration.

Forbidden:

* Do not generate images automatically.
* Do not use old adult/20+ direction as active canon.
* Do not make ANDREY_JUNIOR tall, bulky, or merge him with ANDREY Senior.
* Do not record a generation without `prompt_id`, reference map, output path and verdict.

## Completed — NCC-ANDREY-SENIOR-PROMPT-PIPELINE-BACKFILL

Status: DONE / PROMPT_PIPELINE_ACTIVE (2026-07-06)

Character: ANDREY Senior

Completed:

* Created `ANDREY_PROMPT_INDEX.md` with 11 active prompt IDs.
* Created `ANDREY_WORKING_SCENE_PROMPTS.md` with 10 exact visible prompts and 1 reconstructed prompt (expression sheet C).
* Created `ANDREY_PROMPT_RUN_LOG.jsonl` with 11 valid JSONL records.
* Updated `ANDREY_REFERENCE_PRESETS.json` with `prompt_pipeline` section.
* Updated `ANDREY_CANON_INDEX.md` and `ANDREY_TEST_RESULTS.md` with prompt IDs.
* Updated `CHARACTER_REGISTRY.md` row for ANDREY.
* Recorded task/decision/event/artifacts in SQLite memory.
* Regenerated memory exports and `INVENTORY.md`.

Result:

ANDREY Senior now has a normalized prompt pipeline matching the OLGA / ANDREY_JUNIOR standard.

Next:

Backfill prompt pipeline for KIRA, then prepare ANDREY_3D_REFERENCE_PACK when requested.

Forbidden:

* Do not generate images automatically.
* Do not rename approved ANDREY files in this step.
* Do not use rejected/wrong-scene outputs as canon.
* Do not record a generation without `prompt_id`, reference map, output path and verdict.

## Next-later — NCC-ANDREY-3D-REFERENCE-PACK

Status: POSTPONED

Next goal:
Prepare 3D reference pack structure and requirements using active face canon, body canon and approved control tests.

Forbidden:

* do not regenerate approved control tests unless user explicitly requests candidate variants;
* do not change active canon images;
* do not mark private/local-only outputs as public canon.
