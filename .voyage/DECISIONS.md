# DECISIONS

## DECISION-0001 — Use GitHub-first reference workflow

Date: 2026-07-01

Context: Manual reference upload caused friction and risk of wrong files.

Decision: Use GitHub-first reference packs with raw links and embedded text canon.

Affected files: `tools/build_scene_reference_pack.py`, `tools/build_scene_reference_pack.ps1`, `docs/GITHUB_REFERENCE_PACK_WORKFLOW.md`.

Reason: Reduces manual upload errors and keeps reference packs reproducible from tracked repo state.

Next action: Extend presets to remaining characters once their canon packs exist.

## DECISION-0002 — Scene examples are not generation tasks

Date: 2026-07-01

Context: "Kira and Andrey in sauna" was used as an example of how the reference-pack tool should work, not as a real request.

Decision: Example scenes must not be treated as approved generation tasks.

Affected files: none (workflow rule).

Reason: Prevents accidental generation/commit of images based on illustrative examples rather than explicit user requests.

Next action: Sauna scene should not be generated unless the user explicitly requests it. Rule enforced in [.voyage/SCENE_REQUEST_RULES.md](SCENE_REQUEST_RULES.md).

## DECISION-0003 — Voyage-lite memory layer

Date: 2026-07-02

Context: Project will grow with more characters, locations, 3D models and scenes; without a memory layer it's easy to confuse examples, drafts, approved canon, and placeholders across sessions and tools (ChatGPT, Kimi, Codex, Claude Code).

Decision: Add `.voyage/` memory/control files to preserve context and avoid confusion, plus `docs/VOYAGE_INTEGRATION_WORKFLOW.md` explaining the layer.

Affected files: `docs/VOYAGE_INTEGRATION_WORKFLOW.md`, `.voyage/README.md`, `.voyage/PROJECT_STATE.md`, `.voyage/CHARACTER_REGISTRY.md`, `.voyage/LOCATION_REGISTRY.md`, `.voyage/SCENE_REQUEST_RULES.md`, `.voyage/DECISIONS.md`, `.voyage/CURRENT_TASK.md`, `README.md`, `INVENTORY.md`.

Reason: Preserve project context; distinguish example vs task, draft vs approved, local-only vs GitHub-tracked, raw ref vs active canon.

Next action: Keep `.voyage/PROJECT_STATE.md` and `.voyage/CHARACTER_REGISTRY.md` updated as character canon packs progress.

## DECISION-0004 — KIRA_REFERENCE_PRESETS.json audit result

Date: 2026-07-02

Context: `AGENTS.md`/`ROADMAP.md` described KIRA as "canon-ready / needs repo verification." A `.backup_20260702_082208` of `KIRA_REFERENCE_PRESETS.json` exists, indicating the file was already edited earlier today.

Decision: Audited `AI_CHARACTERS/KIRA/10_notes/KIRA_REFERENCE_PRESETS.json` against the actual file tree. All `text_sources` paths and all `reference_images` in all 7 `scene_presets` (portrait, body_canon, sports, evening, bar, sauna, outdoor) exist in the repository. The file is valid and working — no fix was needed.

Affected files: none (verification only).

Reason: Avoid duplicating work or fabricating a "fix" for a file that is already correct.

Next action: Update `CHARACTER_REGISTRY.md` to reflect KIRA as verified; treat ANDREY body canon as the next actionable roadmap item instead.

## DECISION-0005 — AGENTS.md audited and committed

Date: 2026-07-02

Context: After adding the Voyage-lite layer, `git status` still showed `AGENTS.md` as untracked. A read-only audit was run to decide KEEP_AND_COMMIT / EDIT_BEFORE_COMMIT / DELETE_LOCAL / HOLD.

Decision: EDIT_BEFORE_COMMIT. AGENTS.md is safe (no secrets, no dangerous commands, no explicit content) and useful (repo structure, naming conventions, JSON schema, agent workflows, security rules) — it complements `.voyage` (state/decisions) and `docs/VOYAGE_INTEGRATION_WORKFLOW.md` (human workflow explanation) rather than duplicating them. Two stale/ambiguous spots were fixed before commit: the KIRA status row (was "needs repository verification", now points to `.voyage/CHARACTER_REGISTRY.md`) and the sauna example command in §4 (added a note pointing to `.voyage/SCENE_REQUEST_RULES.md` so it isn't misread as a real generation request).

Affected files: `AGENTS.md` (backed up first as `AGENTS.md.backup_20260702_095750`).

Reason: Keep AGENTS.md accurate and cross-referenced with the new memory layer instead of leaving it as a stale, disconnected untracked file.

Next action: Proceed to `NCC-ANDREY-BODY-CANON` (see `.voyage/CURRENT_TASK.md`).

## DECISION-0006 — Andrey body canon sheets accepted

Date: 2026-07-02

Context: Andrey body canon Sheet A and Sheet B were generated after face canon completion. On disk, Sheet A matched the expected filename (`ANDREY_body_canon_v1_sheet_A_front_side_back.png`) but Sheet B was saved as `ANDREY_body_canon_v1_sheet_B_pose_set.png` instead of the expected `..._pose_variations.png`. Work stopped per the "missing file" safety rule and the user was asked how to proceed; the user explicitly approved renaming the file to `ANDREY_body_canon_v1_sheet_B_pose_variations.png`. A duplicate candidate of Sheet A also exists in `04_body_sheet/candidates/`.

Decision: Use two active body canon files:

* Sheet A — technical front/side/back/3Q (`04_body_sheet/ANDREY_body_canon_v1_sheet_A_front_side_back.png`)
* Sheet B — pose variations, standing/walking/seated/3Q (`04_body_sheet/ANDREY_body_canon_v1_sheet_B_pose_variations.png`, renamed from `pose_set.png` with explicit user approval)

Important: Do not regenerate the same body sheet type unless explicitly requested. Duplicate outputs (e.g. `candidates/ANDREY_body_canon_v1_sheet_A_front_side_back_candidate_02.png`) are saved as candidates only, not active canon, and were not added to `ANDREY_CANON_INDEX.md` or presets.

Affected files: `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_B_pose_variations.png` (renamed), `AI_CHARACTERS/ANDREY/10_notes/ANDREY_CANON_INDEX.md`, `AI_CHARACTERS/ANDREY/10_notes/ANDREY_REFERENCE_PRESETS.json`, `.voyage/CURRENT_TASK.md`, `.voyage/CHARACTER_REGISTRY.md`, `INVENTORY.md`.

Result: Andrey moves from `BODY_PENDING` to `BODY_CANON_ACTIVE / CONTROL_TESTS_PENDING`. Not marked `CANON_READY_2D` until control tests and `ANDREY_TEST_RESULTS.md` exist.

Next action: `NCC-ANDREY-CONTROL-TESTS` (see `.voyage/CURRENT_TASK.md`).

## DECISION-0010 — Andrey control tests approved

Date: 2026-07-02

Context:
Andrey face canon and body canon were active. Six control tests were generated and reviewed.

Decision:
Approve all six control tests and mark Andrey as CANON_READY_2D.

Approved files:

* `AI_CHARACTERS/ANDREY/07_generated/canon_tests/01_neutral_studio_portrait/ANDREY_test01_neutral_studio_portrait_v1.png`
* `AI_CHARACTERS/ANDREY/07_generated/canon_tests/02_full_body_blue_shirt/ANDREY_test02_full_body_blue_shirt_studio_v1.png`
* `AI_CHARACTERS/ANDREY/07_generated/canon_tests/03_warm_bar_portrait/ANDREY_test03_warm_bar_portrait_v1.png`
* `AI_CHARACTERS/ANDREY/07_generated/canon_tests/04_formal_evening_look/ANDREY_test04_formal_evening_look_v1.png`
* `AI_CHARACTERS/ANDREY/07_generated/canon_tests/05_sports_gym_identity/ANDREY_test05_sports_gym_identity_v1.png`
* `AI_CHARACTERS/ANDREY/07_generated/canon_tests/06_sea_yacht_mood/ANDREY_test06_sea_yacht_mood_scene_v1.png`

Result:
Andrey moves to CANON_READY_2D.
Next stage: 3D reference pack or next character canon.

Important:
Do not regenerate approved control tests unless explicitly requested. New variants should be saved as candidates or alternatives, not overwrite approved files.

## DECISION-0011 — Run Kira and Andrey joint control tests before 3D stage

Date: 2026-07-02

Context:
Kira and Andrey both reached CANON_READY_2D. Before moving directly to 3D reference packs, duo scenes should be tested.

Decision:
Create KIRA + ANDREY joint control test structure and prompts before 3D stage.

Result:
NCC-KIRA-ANDREY-JOINT-CONTROL-TESTS becomes the current task. Andrey 3D reference pack is postponed until joint tests are prepared/reviewed.

Important:
The sauna scene remains an example unless explicitly requested as a real generation task.

## DECISION-0012 — Fix Kira test result filename reference

Date: 2026-07-02

Context:
Kira audit confirmed KIRA as CANON_READY_2D. Kira canon/test documents exist as tracked `.md.txt` files. One nonblocking inconsistency was found in `KIRA_TEST_RESULTS.md.txt`: TEST 3 referenced an outdated filename.

Decision:
Keep the existing `.md.txt` document names for now and fix only the outdated TEST 3 image filename reference.

Change:
Replaced `KIRA_test03_portrait_expression_v1_APPROVED.png` with `KIRA_test02_bar_romance_v1_APPROVED.png`.

Result:
`KIRA_TEST_RESULTS.md.txt` now matches the actual tracked approved image file used by `KIRA_REFERENCE_PRESETS.json`.

Important:
Do not rename Kira `.md.txt` notes to `.md` in this cleanup. Any naming convention migration should be a separate explicit task.

## DECISION-0013 — Approve Kira and Andrey joint control tests

Date: 2026-07-02

Context:
Kira and Andrey both reached CANON_READY_2D. Joint control tests were generated to verify identity stability, scale, scene compatibility and duo interaction.

Decision:
Approve four KIRA + ANDREY joint control tests:

* JOINT TEST 01 — Neutral studio duo
* JOINT TEST 02 — Evening embankment duo
* JOINT TEST 03 — Warm bar conversation
* JOINT TEST 04 — Sea / yacht mood duo

Approved files:

* `AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/01_neutral_studio_duo/KIRA_ANDREY_joint_test01_neutral_studio_duo_v2_APPROVED.png`
* `AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/02_evening_embankment_duo/KIRA_ANDREY_joint_test02_evening_embankment_duo_v1_APPROVED.png`
* `AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/03_warm_bar_conversation/KIRA_ANDREY_joint_test03_warm_bar_conversation_v1_APPROVED.png`
* `AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/04_sea_yacht_mood_duo/KIRA_ANDREY_joint_test04_sea_yacht_mood_duo_v1_APPROVED.png`

Rejected / ignored:

* first JOINT TEST 01 version with Kira identity drift;
* wrong gym outputs generated for JOINT TEST 03;
* wrong living room output generated for JOINT TEST 04;
* any composite/infographic/collage outputs.

Result:
KIRA_ANDREY pair becomes JOINT_CONTROL_TESTS_APPROVED and ready for duo scene workflows.

Important:
Kira barefoot height remains 168 cm. Heels may make her apparent height 176–178 cm in some scenes. Andrey remains 180 cm.

## DECISION-0014 — Add Voyage-lite SQLite memory layer

Date: 2026-07-02

Context:
Kira, Andrey and KIRA_ANDREY joint tests reached approved states. The project accumulated many canon statuses, approved outputs, rejected outputs, decisions and commit references.

Decision:
Add a local SQLite memory layer outside the repo and export compact project memory into tracked `.voyage` files.

Result:
SQLite DB becomes local runtime memory. GitHub stores only tools, docs and exports.

DB path:
`C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\voyage_memory\narrative_character_canon.sqlite`

Tracked exports:

* `.voyage/CONTEXT_SNAPSHOT.md`
* `.voyage/STATE_EXPORT.json`
* `.voyage/EVENTS_EXPORT.jsonl`

Important:
Do not commit `.sqlite`, `.sqlite3` or `.db` files. Use exports for ChatGPT/context handoff.

## DECISION-0015 — Add Voyage SQLite record command

Date: 2026-07-02

Context:
Voyage-lite SQLite memory was initialized, but future workflows needed an incremental way to record events, tasks, decisions, commits, characters, pairs and artifacts without rebuilding the DB.

Decision:
Add `tools/voyage_memory_record.py` as a local CLI for recording/updating structured memory facts.

Result:
Future workflows can record approved artifacts, rejected outputs, task changes, decisions and pair/character status changes directly into local SQLite memory, then export `.voyage` handoff files.

Important:
The SQLite DB remains local runtime memory and must not be committed. Only tools, docs and exports are tracked.

## DECISION-0016 — Prepare Kira and Andrey duo scene packs

Date: 2026-07-02

Context:
Kira and Andrey both reached CANON_READY_2D, and KIRA_ANDREY pair reached JOINT_CONTROL_TESTS_APPROVED. Voyage SQLite memory and record command are available.

Decision:
Prepare duo scene pack structure, prompts, index, result tracker and JSON spec before generating any new duo scenes.

Result:
NCC-KIRA-ANDREY-DUO-SCENE-PACKS becomes ready for explicit generation requests.

Important:
No images are generated in this setup step. Sauna remains EXAMPLE / NOT REQUESTED unless the user explicitly requests it as a real scene.

## DECISION-0017 — Approve Kira and Andrey duo scene packs

Date: 2026-07-02

Context:
KIRA_ANDREY pair reached JOINT_CONTROL_TESTS_APPROVED and the duo scene pack workflow was prepared. Six scene packs were generated and reviewed.

Decision:
Approve six KIRA + ANDREY duo scene pack outputs:

* SCENE PACK 01 — Evening embankment walk
* SCENE PACK 02 — Warm bar dialogue
* SCENE PACK 03 — Yacht sunset
* SCENE PACK 04 — Studio character poster
* SCENE PACK 05 — Rainy city street
* SCENE PACK 06 — Cozy interior conversation v4

Approved files:

* `AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/01_evening_embankment_walk/KIRA_ANDREY_scene01_evening_embankment_walk_v1_APPROVED.png`
* `AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/02_warm_bar_dialogue/KIRA_ANDREY_scene02_warm_bar_dialogue_v1_APPROVED.png`
* `AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/03_yacht_sunset/KIRA_ANDREY_scene03_yacht_sunset_v1_APPROVED.png`
* `AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/04_studio_character_poster/KIRA_ANDREY_scene04_studio_character_poster_v1_APPROVED.png`
* `AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/05_rainy_city_street/KIRA_ANDREY_scene05_rainy_city_street_v1_APPROVED.png`
* `AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/scene_packs/06_cozy_interior_conversation/KIRA_ANDREY_scene_pack06_cozy_interior_conversation_v4_APPROVED.png`

Rejected / ignored:

* SCENE PACK 06 v1 was not selected;
* SCENE PACK 06 v2 was held/candidate due to Kira leg/pose issue;
* SCENE PACK 06 v3 was rejected due to Andrey identity drift;
* only SCENE PACK 06 v4 is final approved.

Result:
KIRA_ANDREY pair becomes DUO_SCENE_PACKS_APPROVED and ready for future story/visual workflows.

Important:
Do not overwrite approved scene pack outputs. New variants must be saved as alternatives/candidates. Kira barefoot height remains 168 cm; Andrey remains 180 cm.

## DECISION-0018 — Start Andrey Junior canon workflow

Date: 2026-07-03

Context:
KIRA, ANDREY Senior and KIRA_ANDREY duo scene packs reached approved states. The next character workflow starts with ANDREY_JUNIOR.

Decision:
Create ANDREY_JUNIOR canon setup before any image generation.

Result:
ANDREY_JUNIOR becomes CANON_PENDING / SETUP_DONE. Face canon generation requires explicit user request.

Important:
ANDREY_JUNIOR must be treated as an adult compact young man 20+, 153 cm, 53 kg. Do not portray him as minor, teen or child.

## DECISION-0019 — Approve Andrey Junior son-version base canon and control tests

Date: 2026-07-04

Context:
ANDREY_JUNIOR was first started with an adult/20+ direction, then restarted as the younger son of ANDREY Senior. New locally generated base canon and control tests were reviewed and approved.

Decision:
Approve the son-version of ANDREY_JUNIOR as the active canon. Old adult/20+ direction is superseded and must not be used as active canon.

Approved base canon:

* `AI_CHARACTERS/ANDREY_JUNIOR/03_face_sheet/ANDREY_JUNIOR_face_canon_v1_sheet_A_APPROVED.png`
* `AI_CHARACTERS/ANDREY_JUNIOR/03_face_sheet/expressions/ANDREY_JUNIOR_expressions_v2_sheet_A_APPROVED.png`
* `AI_CHARACTERS/ANDREY_JUNIOR/04_body_sheet/ANDREY_JUNIOR_body_canon_v2_sheet_A_front_side_back_APPROVED.png`
* `AI_CHARACTERS/ANDREY_JUNIOR/04_body_sheet/ANDREY_JUNIOR_body_canon_v2_sheet_B_pose_variations_APPROVED.png`

Approved control tests:

* `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/01_neutral_studio_portrait/ANDREY_JUNIOR_test01_neutral_studio_portrait_v1_APPROVED.png`
* `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/02_full_body_studio/ANDREY_JUNIOR_test02_full_body_studio_v1_APPROVED.png`
* `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/03_athletic_gym_identity/ANDREY_JUNIOR_test03_athletic_gym_identity_v1_APPROVED.png`
* `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/04_casual_outfit/ANDREY_JUNIOR_test04_casual_outfit_v1_APPROVED.png`
* `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/05_scale_compact_body_check/ANDREY_JUNIOR_test05_scale_compact_body_check_v1_APPROVED.png`
* `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/06_father_son_scale_check/ANDREY_JUNIOR_test06_father_son_scale_check_v2_APPROVED.png`
* `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/07_father_son_casual_outdoor/ANDREY_JUNIOR_test07_father_son_casual_outdoor_v1_APPROVED.png`
* `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/08_father_son_home_conversation/ANDREY_JUNIOR_test08_father_son_home_conversation_v1_APPROVED.png`
* `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/09_father_son_training_coaching/ANDREY_JUNIOR_test09_father_son_training_coaching_v1_APPROVED.png`

Rejected / ignored:

* Old adult/20+ direction text and any images tied to that direction are not active canon.
* TEST 06 v1 was held/rejected due to Andrey Senior body proportion drift; v2 approved.

Result:
ANDREY_JUNIOR becomes BASE_CANON_APPROVED / CONTROL_TESTS_APPROVED.

Important:
ANDREY_JUNIOR is the son-version of ANDREY Senior: short compact build, about 47 kg, slim youthful physique, fair skin, bright blue eyes, light blonde / dark blonde messy hair, soft oval youthful face, gentle narrow jawline, clean-shaven, natural pinkness in cheeks. Keep prompts family-neutral, non-sexual and age-appropriate. Avoid explicit age numbers and avoid writing “Andrey Junior” inside image prompts when possible.

## DECISION-0020 — Start OLGA canon setup

Date: 2026-07-04

Context:
KIRA, ANDREY Senior, KIRA_ANDREY duo scene packs, and ANDREY_JUNIOR son-version canon have reached approved states. A new mature adult woman character, OLGA, is being introduced.

Decision:
Create OLGA canon setup files and folder structure before any image generation.

Result:
OLGA becomes CANON_PENDING / SETUP_DONE. Face canon generation requires explicit user approval.

Important:
OLGA is a mature adult woman character: very tall around 187 cm, athletic-curvy build, strong but feminine silhouette, realistic adult proportions, elegant dominant cinematic presence. Generation must remain non-explicit: avoid nude, lingerie, transparent clothing, fetish framing, or erotic posing; avoid exaggerated proportions, bodybuilder drift, or making her look too young.

## DECISION-0021 — Approve OLGA base canon and normalize prompt pipeline

Date: 2026-07-05

Context:
OLGA setup was committed, then local generations produced approved base canon sheets and control tests. Audit showed prompt logging was not normalized: only a setup skeleton existed, no prompt index, no working scene prompts, and no JSONL run log.

Decision:
Approve OLGA base canon and initial control tests locally. Normalize prompt logging by creating `OLGA_PROMPT_INDEX.md`, `OLGA_WORKING_SCENE_PROMPTS.md`, and `OLGA_PROMPT_RUN_LOG.jsonl`. Update OLGA canon index, test results, and reference presets to point to active approved files.

Approved base canon:

* `AI_CHARACTERS/OLGA/02_refs_selected/OLGA_ref_face_primary_v1_SELECTED.jpg`
* `AI_CHARACTERS/OLGA/03_face_sheet/OLGA_face_canon_v1_sheet_A_APPROVED.png`
* `AI_CHARACTERS/OLGA/03_face_sheet/expressions/OLGA_expressions_v1_sheet_A_APPROVED.png`
* `AI_CHARACTERS/OLGA/04_body_sheet/OLGA_body_canon_v1_sheet_A_front_side_back_APPROVED.png`
* `AI_CHARACTERS/OLGA/04_body_sheet/OLGA_body_canon_v1_sheet_B_pose_variations_APPROVED.png`

Approved control tests:

* `AI_CHARACTERS/OLGA/07_generated/canon_tests/01_evening_embankment/OLGA_test01_evening_embankment_v1_APPROVED.png`
* `AI_CHARACTERS/OLGA/07_generated/canon_tests/02_sports_yoga/OLGA_test02_sports_yoga_v1_APPROVED.png`
* `AI_CHARACTERS/OLGA/07_generated/canon_tests/03_portrait_expression/OLGA_test03_portrait_expression_v1_APPROVED.png`
* `AI_CHARACTERS/OLGA/07_generated/canon_tests/04_outdoor_walk_with_andrey_junior/OLGA_test04_outdoor_walk_with_andrey_junior_v1_APPROVED.png`

Prompt pipeline files:

* `AI_CHARACTERS/OLGA/06_prompts/OLGA_PROMPT_INDEX.md`
* `AI_CHARACTERS/OLGA/06_prompts/OLGA_WORKING_SCENE_PROMPTS.md`
* `AI_CHARACTERS/OLGA/06_prompts/OLGA_PROMPT_RUN_LOG.jsonl`

Result:
OLGA becomes BASE_CANON_APPROVED / CONTROL_TESTS_APPROVED_LOCALLY. Future image generations must record `prompt_id`, references, output path, verdict, and notes.

Important:
Prompt sources are marked honestly: exact visible prompts are `exact_user_visible_prompt`; reconstructed/inferred prompts are `reconstructed_from_conversation_and_approved_result`. Do not claim unavailable hidden tool prompts are exact.

## DECISION-0007 — Remove duplicate body candidate from active repo area

Date: 2026-07-02

Context: A duplicate Andrey body Sheet A candidate remained untracked after active body canon was committed.

Decision: Keep only two active body canon files in repository:

* Sheet A — `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_A_front_side_back.png`
* Sheet B — `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_B_pose_variations.png`

Duplicate candidate outputs should be stored in `LOCAL_STORAGE` or discarded, not left as untracked repo files.

Affected files: `AI_CHARACTERS/ANDREY/04_body_sheet/candidates/ANDREY_body_canon_v1_sheet_A_front_side_back_candidate_02.png` (moved to `LOCAL_STORAGE/narrative-character-canon/duplicate_candidates/ANDREY/body_sheet/`), `INVENTORY.md`, `.voyage/DECISIONS.md`.

Reason: Prevents confusion between active canon, candidates, and local-only duplicate outputs before control tests.

Result: Repository prepared for `NCC-ANDREY-CONTROL-TESTS`.

Next action: Create `ANDREY_TEST_RESULTS.md` structure and control test prompts, without generating images.

## DECISION-0008 — Andrey control tests require explicit generation requests

Date: 2026-07-02

Context:
Andrey face canon and body canon are active. Control test structure is being created.

Decision:
Create prompts, tracking document and folders first. Do not generate control test images automatically.

Result:
Control tests remain pending until the user explicitly requests each generation.

## DECISION-0022 — Normalize OLGA test05/test06 and enforce prompt logging

Date: 2026-07-05

Context:

Read-only audit detected two new untracked OLGA test folders with swapped IDs:

* Folder `05_business_interior/` contained `OLGA_test06_business_interior_v1_APPROVED.png`.
* Folder `06_indoor_lounge_conversation_with_andrey_junior/` contained `OLGA_test05_indoor_lounge_conversation_with_andrey_junior_v1_APPROVED.png`.
* An unlabeled raw file `1.png` was present in the business interior folder.

Decision:

* Business interior image is approved as **test05**.
* Indoor lounge conversation with ANDREY_JUNIOR is approved as **test06**.
* Rename both approved files so folder ID and filename ID match.
* Move unlabeled raw `1.png` to `AI_CHARACTERS/OLGA/08_rejected/OLGA_business_interior_raw_1_unlabeled_REJECTED.png`.
* Record prompt IDs `OLGA_TEST05_BUSINESS_INTERIOR_V1` and `OLGA_TEST06_INDOOR_LOUNGE_CONVERSATION_AJ_V1` in the prompt pipeline.
* Update `OLGA_CANON_INDEX.md`, `OLGA_TEST_RESULTS.md`, and `OLGA_REFERENCE_PRESETS.json`.
* Fix duplicate OLGA row in `.voyage/CHARACTER_REGISTRY.md`.

Affected files:

* `AI_CHARACTERS/OLGA/07_generated/canon_tests/05_business_interior/OLGA_test05_business_interior_v1_APPROVED.png`
* `AI_CHARACTERS/OLGA/07_generated/canon_tests/06_indoor_lounge_conversation_with_andrey_junior/OLGA_test06_indoor_lounge_conversation_with_andrey_junior_v1_APPROVED.png`
* `AI_CHARACTERS/OLGA/08_rejected/OLGA_business_interior_raw_1_unlabeled_REJECTED.png`
* `AI_CHARACTERS/OLGA/06_prompts/OLGA_PROMPT_INDEX.md`
* `AI_CHARACTERS/OLGA/06_prompts/OLGA_WORKING_SCENE_PROMPTS.md`
* `AI_CHARACTERS/OLGA/06_prompts/OLGA_PROMPT_RUN_LOG.jsonl`
* `AI_CHARACTERS/OLGA/10_notes/OLGA_CANON_INDEX.md`
* `AI_CHARACTERS/OLGA/10_notes/OLGA_TEST_RESULTS.md`
* `AI_CHARACTERS/OLGA/10_notes/OLGA_REFERENCE_PRESETS.json`
* `.voyage/CHARACTER_REGISTRY.md`
* `.voyage/CURRENT_TASK.md`
* `.voyage/DECISIONS.md`

Reason:

Prevents ID mismatch between folders, filenames, prompt_ids, and memory records. Keeps unlabeled raw outputs out of active canon. Enforces prompt logging for all future OLGA generations.

Result:

OLGA has 6 approved control tests (01–06) with consistent IDs and a complete prompt pipeline record.

Next action:

Continue controlled scene testing for OLGA with prompt_id logging.

## DECISION-0023 — Backfill ANDREY_JUNIOR prompt pipeline

Date: 2026-07-06

Context:

ANDREY_JUNIOR base canon and 9 solo control tests were approved earlier (`DECISION-0019`). The character had a working prompt source file (`ANDREY_JUNIOR_CANON_GENERATION_PROMPTS.txt`) but lacked the normalized prompt pipeline standard that OLGA now uses.

Decision:

* Create `ANDREY_JUNIOR_PROMPT_INDEX.md`, `ANDREY_JUNIOR_WORKING_SCENE_PROMPTS.md`, and `ANDREY_JUNIOR_PROMPT_RUN_LOG.jsonl`.
* Record 13 prompt IDs covering the 4 base canon images and 9 approved control tests.
* Mark 12 prompts as `exact_user_visible_prompt` copied from the existing working prompt source.
* Mark 1 prompt (`ANDREY_JUNIOR_BODY_CANON_V2_B`) as `reconstructed_from_conversation_and_approved_result` because the exact body pose-variation prompt was not archived separately.
* Update `ANDREY_JUNIOR_REFERENCE_PRESETS.json`, `ANDREY_JUNIOR_CANON_INDEX.md`, `ANDREY_JUNIOR_TEST_RESULTS.md`, and `ANDREY_JUNIOR_IDENTITY_DRAFT.md` to reference the new pipeline.
* Update `.voyage/CHARACTER_REGISTRY.md` to show `PROMPT_PIPELINE_ACTIVE` for ANDREY_JUNIOR.

Affected files:

* `AI_CHARACTERS/ANDREY_JUNIOR/06_prompts/ANDREY_JUNIOR_PROMPT_INDEX.md`
* `AI_CHARACTERS/ANDREY_JUNIOR/06_prompts/ANDREY_JUNIOR_WORKING_SCENE_PROMPTS.md`
* `AI_CHARACTERS/ANDREY_JUNIOR/06_prompts/ANDREY_JUNIOR_PROMPT_RUN_LOG.jsonl`
* `AI_CHARACTERS/ANDREY_JUNIOR/06_prompts/ANDREY_JUNIOR_CANON_GENERATION_PROMPTS.txt`
* `AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_REFERENCE_PRESETS.json`
* `AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_CANON_INDEX.md`
* `AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_TEST_RESULTS.md`
* `AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_IDENTITY_DRAFT.md`
* `.voyage/CHARACTER_REGISTRY.md`
* `.voyage/CURRENT_TASK.md`
* `.voyage/DECISIONS.md`

Superseded historical wording:

`DECISION-0018` described ANDREY_JUNIOR as an adult/20+ 153 cm/53 kg compact young man during initial setup. That direction was later superseded by the son-version canon in `DECISION-0019` and remains inactive. The active direction is son-version: short compact build, about 47 kg, slim youthful physique, family-neutral, non-sexual.

Reason:

Brings ANDREY_JUNIOR to the same prompt-logging standard as OLGA, making every approved image traceable to a `prompt_id`, reference map, output path, verdict, and notes.

Result:

ANDREY_JUNIOR becomes `BASE_CANON_APPROVED / CONTROL_TESTS_APPROVED / PROMPT_PIPELINE_ACTIVE`.

Next action:

Backfill prompt pipeline for ANDREY Senior, then KIRA, before any large folder schema migration.

---

## DECISION-0024 — ANDREY Senior prompt pipeline normalized

Date: 2026-07-06
Task ID: NCC-ANDREY-SENIOR-PROMPT-PIPELINE-BACKFILL

Decision:

Create a canonical prompt pipeline for ANDREY Senior matching the OLGA / ANDREY_JUNIOR normalized pattern.

Pipeline files:

* `AI_CHARACTERS/ANDREY/06_prompts/ANDREY_PROMPT_INDEX.md` — canonical prompt ID index (11 active prompts: 5 base canon + 6 control tests).
* `AI_CHARACTERS/ANDREY/06_prompts/ANDREY_WORKING_SCENE_PROMPTS.md` — full per-prompt text, reference map, output path, result notes.
* `AI_CHARACTERS/ANDREY/06_prompts/ANDREY_PROMPT_RUN_LOG.jsonl` — machine-readable JSONL log (11 entries).

Prompt IDs:

Base canon:

* `ANDREY_FACE_CANON_V1` -> `AI_CHARACTERS/ANDREY/02_face/ANDREY_FACE_CANON_5STARS_V2.png`
* `ANDREY_FACE_CANON_V2` -> `AI_CHARACTERS/ANDREY/02_face/ANDREY_FACE_CANON_5STARS_V3.png`
* `ANDREY_BODY_CANON_V1` -> `AI_CHARACTERS/ANDREY/03_body/ANDREY_BODY_CANON_V1.png`
* `ANDREY_BODY_CANON_V2` -> `AI_CHARACTERS/ANDREY/03_body/ANDREY_BODY_CANON_V2.png`
* `ANDREY_EXPRESSIONS_V1_C_REFINED` -> `AI_CHARACTERS/ANDREY/04_expressions/ANDREY_EXPRESSIONS_V1_C_REFINED.png` (reconstructed prompt from conversation + approved result)

Control tests:

* `ANDREY_TEST_01_DRAMATIC_LIGHT` -> `AI_CHARACTERS/ANDREY/05_tests/ANDREY_TEST_01_DRAMATIC_LIGHT.png`
* `ANDREY_TEST_02_NEUTRAL_BG` -> `AI_CHARACTERS/ANDREY/05_tests/ANDREY_TEST_02_NEUTRAL_BG.png`
* `ANDREY_TEST_03_OUTDOOR_SUN` -> `AI_CHARACTERS/ANDREY/05_tests/ANDREY_TEST_03_OUTDOOR_SUN.png`
* `ANDREY_TEST_04_EYE_COLOR` -> `AI_CHARACTERS/ANDREY/05_tests/ANDREY_TEST_04_EYE_COLOR.png`
* `ANDREY_TEST_05_HAIR_DETAIL` -> `AI_CHARACTERS/ANDREY/05_tests/ANDREY_TEST_05_HAIR_DETAIL.png`
* `ANDREY_TEST_06_SMIRK` -> `AI_CHARACTERS/ANDREY/05_tests/ANDREY_TEST_06_SMIRK.png`

Reference map for solo prompts:

* `A` — `02_face/ANDREY_FACE_CANON_5STARS_V2.png`
* `B` — `02_face/ANDREY_FACE_CANON_5STARS_V3.png`
* `C` — `03_body/ANDREY_BODY_CANON_V1.png`
* `D` — `03_body/ANDREY_BODY_CANON_V2.png`
* `E` — `04_expressions/ANDREY_EXPRESSIONS_V1_C_REFINED.png`

Approval status:

* All 11 prompts and outputs are approved as canon/control tests.
* Prompt source is `exact_user_visible_prompt` for 10 entries and `reconstructed_from_conversation_and_approved_result` for `ANDREY_EXPRESSIONS_V1_C_REFINED`.

Affected files:

* `AI_CHARACTERS/ANDREY/06_prompts/ANDREY_PROMPT_INDEX.md`
* `AI_CHARACTERS/ANDREY/06_prompts/ANDREY_WORKING_SCENE_PROMPTS.md`
* `AI_CHARACTERS/ANDREY/06_prompts/ANDREY_PROMPT_RUN_LOG.jsonl`
* `AI_CHARACTERS/ANDREY/10_notes/ANDREY_REFERENCE_PRESETS.json`
* `AI_CHARACTERS/ANDREY/10_notes/ANDREY_CANON_INDEX.md`
* `AI_CHARACTERS/ANDREY/10_notes/ANDREY_TEST_RESULTS.md`
* `.voyage/CHARACTER_REGISTRY.md`
* `.voyage/CURRENT_TASK.md`
* `.voyage/DECISIONS.md`

Reason:

Brings ANDREY Senior to the same prompt-logging standard as OLGA and ANDREY_JUNIOR, making every approved image traceable to a `prompt_id`, reference map, output path, verdict, and notes.

Result:

ANDREY Senior becomes `CANON_READY_2D / PROMPT_PIPELINE_ACTIVE`.

Next action:

Backfill prompt pipeline for KIRA, then prepare ANDREY_3D_REFERENCE_PACK when requested.

---

## DECISION-0025 — Backfill KIRA core prompt pipeline

Date: 2026-07-07
Task ID: NCC-KIRA-PROMPT-PIPELINE-BACKFILL

Decision:

Create a canonical prompt pipeline for KIRA matching the OLGA / ANDREY_JUNIOR / ANDREY Senior normalized pattern, using only the existing active canon images and prompt-kit files.

Pipeline files:

* `AI_CHARACTERS/KIRA/06_prompts/KIRA_PROMPT_INDEX.md` — canonical prompt ID index (6 core active prompts).
* `AI_CHARACTERS/KIRA/06_prompts/KIRA_WORKING_SCENE_PROMPTS.md` — full per-prompt text, reference map, output path, result notes.
* `AI_CHARACTERS/KIRA/06_prompts/KIRA_PROMPT_RUN_LOG.jsonl` — machine-readable JSONL log (6 entries).

Prompt IDs:

Base canon:

* `KIRA_FACE_CANON_V1_A` -> `AI_CHARACTERS/KIRA/03_face_sheet/KIRA_face_canon_sheet_A.png`
* `KIRA_BODY_CANON_V4_A` -> `AI_CHARACTERS/KIRA/04_body_sheet/KIRA_BODY_CANON_v4_sheet_A_4views.png`
* `KIRA_EXPRESSIONS_V1_A` -> `AI_CHARACTERS/KIRA/03_face_sheet/expressions/KIRA_expressions_v1_sheet_A_emotional.png`

Control tests:

* `KIRA_TEST01_EVENING_EMBANKMENT_V1_MAIN` -> `AI_CHARACTERS/KIRA/07_generated/canon_tests/01_evening_embankment/KIRA_test01_evening_embankment_v2_MAIN.png`
* `KIRA_TEST02_SPORTS_YOGA_V1_MAIN` -> `AI_CHARACTERS/KIRA/07_generated/canon_tests/02_sports_yoga/KIRA_test02_sports_yoga_v2_MAIN.png`
* `KIRA_TEST03_PORTRAIT_EXPRESSION_V1` -> `AI_CHARACTERS/KIRA/07_generated/canon_tests/03_portrait_expression/KIRA_test02_bar_romance_v1_APPROVED.png`

Reference map for solo prompts:

* `A` — `03_face_sheet/KIRA_face_canon_sheet_A.png`
* `B` — `04_body_sheet/KIRA_BODY_CANON_v4_sheet_A_4views.png`
* `C` — `03_face_sheet/expressions/KIRA_expressions_v1_sheet_A_emotional.png`
* `D` — `05_outfits/evening_dress/KIRA_evening_dress_FINAL_sheet_A_fullbody.png`
* `E` — `05_outfits/sports_look/KIRA_sports_look_v1_sheet_A_front_side_back.png`

Approval status:

* All 6 prompts and outputs are approved as canon/control tests.
* Base canon records are marked `unknown_requires_manual_input` because exact per-image generation prompts are not stored in repository files.
* Control-test records are marked `reconstructed_from_conversation_and_approved_result` because best-effort prompts were reconstructed from the prompt-kit files and test-result notes.

Corrections made:

* `KIRA_CANON_INDEX.md.txt` previously referenced `KIRA_expressions_v1_sheet_A_basic.png`; corrected to the actual file `KIRA_expressions_v1_sheet_A_emotional.png`.
* `KIRA_CANON_INDEX.md.txt` previously referenced `10_notes/KIRA_IDENTITY.txt`; corrected to the actual file `10_notes/KIRA_IDENTITY.txt.txt`.

Preserved (deferred):

* `.md.txt` and `.txt.txt` document extensions.
* Mixed filename suffixes: `_MAIN`, `_ALT`, `_APPROVED`, `FINAL`, and no suffix.
* KIRA folder/schema layout including `02_best_refs`, `08_masks`, `09_blender`, `07_generated/drafts`, `07_generated/rejected`.

Affected files:

* `AI_CHARACTERS/KIRA/06_prompts/KIRA_PROMPT_INDEX.md`
* `AI_CHARACTERS/KIRA/06_prompts/KIRA_WORKING_SCENE_PROMPTS.md`
* `AI_CHARACTERS/KIRA/06_prompts/KIRA_PROMPT_RUN_LOG.jsonl`
* `AI_CHARACTERS/KIRA/06_prompts/KIRA_BASE_PROMPT.txt`
* `AI_CHARACTERS/KIRA/06_prompts/KIRA_EVENING_SCENE_PROMPT.txt`
* `AI_CHARACTERS/KIRA/06_prompts/KIRA_SPORTS_SCENE_PROMPT.txt`
* `AI_CHARACTERS/KIRA/06_prompts/KIRA_NEGATIVE_PROMPT.txt`
* `AI_CHARACTERS/KIRA/10_notes/KIRA_REFERENCE_PRESETS.json`
* `AI_CHARACTERS/KIRA/10_notes/KIRA_CANON_INDEX.md.txt`
* `AI_CHARACTERS/KIRA/10_notes/KIRA_TEST_RESULTS.md.txt`
* `AI_CHARACTERS/KIRA/10_notes/KIRA_IDENTITY.txt.txt`
* `.voyage/CHARACTER_REGISTRY.md`
* `.voyage/CURRENT_TASK.md`
* `.voyage/DECISIONS.md`

Reason:

Brings KIRA to the same prompt-logging standard as OLGA, ANDREY_JUNIOR, and ANDREY Senior, making every approved image traceable to a `prompt_id`, reference map, output path, verdict, and notes.

Result:

KIRA becomes `CANON_READY_2D / PROMPT_PIPELINE_ACTIVE_CORE`.

Next action:

Backfill prompt pipeline for KIRA_ANDREY joint scenes, then prepare 3D reference packs when requested.

---

Дата:
2026-07-09

Decision ID:
D-010

Context:
VNE Visual Bridge production contract deployment. Agent created 13 files for 9 characters across NCC. Post-deployment audit revealed naming and location violations.

Decision:
Fix agent folder discipline violation and standardize all files to NCC naming convention.

Details:
1. Agent created `AI_CHARACTERS/10_notes/GROUP_C_CANON_GENERATION_PROMPTS.md` — wrong location. `10_notes/` must be per-character only, never at `AI_CHARACTERS/` level.
2. Agent did not follow `[CHARACTER]_CANON_GENERATION_PROMPTS.txt` naming convention for `06_prompts/` (used `.md` and group-level naming instead).
3. Agent did not update `CHARACTER_REGISTRY.md`, `INVENTORY.md`, or `DECISIONS.md` during deployment — violating Voyage tracking protocol.
4. Agent did not create per-character `IDENTITY.txt` or `CANON_INDEX.md` skeletons for Group C — violating AGENTS.md workflow for new characters.

Fix:
1. Removed `AI_CHARACTERS/10_notes/` folder entirely.
2. Created 5 per-character `[CHARACTER]_CANON_GENERATION_PROMPTS.txt` files in `AI_CHARACTERS/[CHAR]/06_prompts/`.
3. Updated `CHARACTER_REGISTRY.md`: EGOR/MAKSIM/MARINA/NIKA/SERGEY status → `TEXT_CANON_READY / CANON_PROMPTS_CREATED`.
4. Created this `DECISIONS.md` entry.
5. Regenerate `INVENTORY.md` (separate action).
6. Per-character `IDENTITY.txt` and `CANON_INDEX.md` skeletons deferred to user approval.

Affected files:
* `AI_CHARACTERS/EGOR/06_prompts/EGOR_CANON_GENERATION_PROMPTS.txt`
* `AI_CHARACTERS/MAKSIM/06_prompts/MAKSIM_CANON_GENERATION_PROMPTS.txt`
* `AI_CHARACTERS/MARINA/06_prompts/MARINA_CANON_GENERATION_PROMPTS.txt`
* `AI_CHARACTERS/NIKA/06_prompts/NIKA_CANON_GENERATION_PROMPTS.txt`
* `AI_CHARACTERS/SERGEY/06_prompts/SERGEY_CANON_GENERATION_PROMPTS.txt`
* `AI_CHARACTERS/ANDREY_JUNIOR/10_notes/ANDREY_JUNIOR_REFERENCE_PRESETS.json`
* `AI_CHARACTERS/OLGA/10_notes/OLGA_REFERENCE_PRESETS.json`
* `AI_CHARACTERS/ANDREY/10_notes/ANDREY_REFERENCE_PRESETS.json`
* `AI_CHARACTERS/KIRA/10_notes/KIRA_REFERENCE_PRESETS.json`
* `AI_CHARACTERS/ANDREY/10_notes/ANDREY_CANON_APPROVAL_WORKSHEET.md`
* `AI_CHARACTERS/KIRA/10_notes/KIRA_CANON_APPROVAL_WORKSHEET.md`
* `AI_CHARACTERS/OLGA/06_prompts/OLGA_POOL_SCENE_PROMPT.md`
* `.voyage/CHARACTER_REGISTRY.md`
* `.voyage/DECISIONS.md`

Reason:
Brings all 9 characters to consistent NCC naming convention, 10-subfolder structure, and Voyage tracking. Fixes the agent's folder discipline violation per `AGENTS.md` section 5.

Result:
Group A (OLGA, ANDREY_JUNIOR): production-ready with canonical JSON.
Group B (ANDREY, KIRA): `TEXT_CANON_READY` with APPROVAL worksheets.
Group C (EGOR, MAKSIM, MARINA, NIKA, SERGEY): `TEXT_CANON_READY` with generation prompts.

Next action:
Generate face/body canon images for Group C via DALL-E or RunPod, then create control tests. Per-character `IDENTITY.txt` and `CANON_INDEX.md` skeletons to be created before image generation begins.

---

Дата:
2026-07-09

Decision ID:
D-011

Context:
DALL-E generation plan for 17 images across 8 characters (excluding ANDREY_JUNIOR from public_filtered).

Decision:
Create DALL-E ChatGPT Generation Plan v1.0 with 17 images, 4 phases, DCB blocks, and DECISION_001 protocol.

Affected files:
* `workspace/DALLE_GENERATION_PLAN_v1.0.md` (not committed to NCC — planning document only)

Reason:
DALL-E does not support IP-Adapter or reference image upload. Consistency achieved through repeated DALL-E Character Blocks (DCB) in every prompt. AJ excluded due to `public_filtered` backend restriction.

Result:
Ready to begin `OLGA-01` portrait generation.

Next action:
Execute DALL-E generation plan phase by phase with `DECISION_001` after each image.

---

Дата: 2026-07-10
Decision ID: D-012
Context: OLGA pool/wellness generation produced public-safe athleisure v1 and swimsuit v2/v3 variants.
Decision: Human selected option B. Deploy only v1 athleisure/public-safe image to repo. Keep v2/v3 swimsuit variants local-only.
Affected files:
- `AI_CHARACTERS/OLGA/07_generated/canon_tests/07_pool_wellness_solo/OLGA_test07_pool_wellness_solo_v1_APPROVED.png`
- `AI_CHARACTERS/OLGA/10_notes/OLGA_TEST_RESULTS.md`
- `AI_CHARACTERS/OLGA/06_prompts/OLGA_PROMPT_RUN_LOG.jsonl`
- `AI_CHARACTERS/OLGA/06_prompts/OLGA_WORKING_SCENE_PROMPTS.md`
- `AI_CHARACTERS/OLGA/10_notes/OLGA_REFERENCE_PRESETS.json`
- `.voyage/DECISIONS.md`
- `.voyage/CURRENT_TASK.md`
- `INVENTORY.md`
Reason: Preserve repo as public-safe while keeping canon-correct swimsuit references in LOCAL_STORAGE.
Result: v1 repo-tracked; v2/v3 local-only.
Next action: Continue visual coverage based on actual missing targets.

---

Дата: 2026-07-10
Decision ID: D-013
Context: OLGA 08 DALL-E evening embankment image was initially questioned as local-only but human clarified it is an ordinary SFW photo.
Decision: Keep and deploy as repo-tracked approved DALL-E ALT/backend variant.
Reason: Preserve useful backend comparison reference and avoid losing approved visual work.
Affected files:
- `AI_CHARACTERS/OLGA/07_generated/canon_tests/08_dalle_evening_embankment/OLGA_test08_dalle_evening_embankment_v1_APPROVED.png`
- `AI_CHARACTERS/OLGA/10_notes/OLGA_TEST_RESULTS.md`
- `AI_CHARACTERS/OLGA/06_prompts/OLGA_PROMPT_RUN_LOG.jsonl`
- `AI_CHARACTERS/OLGA/06_prompts/OLGA_WORKING_SCENE_PROMPTS.md`
- `AI_CHARACTERS/OLGA/10_notes/OLGA_REFERENCE_PRESETS.json`
- `.voyage/DECISIONS.md`
- `.voyage/CURRENT_TASK.md`
- `INVENTORY.md`
Result: OLGA 08 DALL-E evening embankment is repo-tracked ALT reference; 01_evening_embankment remains MAIN.
Next action: Continue coverage-based generation and reference preset cleanup.

---

Date: 2026-07-10
Decision ID: D-014
Context: The original NCC-DALLE-17-GENERATION task produced duplicate-risk because existing coverage was not audited before generation.
Decision: Close the old task as CLOSED_REDESIGNED. Adopt mandatory coverage-first and reference-first workflow. Open a new read-only preflight task for OLGA formal/elegant coverage.
Affected files:
- `.voyage/CURRENT_TASK.md`
- `.voyage/DECISIONS.md`
Reason: Prevent duplicate images, preserve exact character canon, and ensure future scenes use the best existing references and documented anchor rules.
Results:
- Completed OLGA pool/wellness and evening embankment records remain authoritative.
- Future generation requires explicit reference selection before prompt creation.
Next action: Run OLGA formal/elegant reference preflight only.

---

Date: 2026-07-11
Decision ID: D-015
Context: Formal/elegant coverage was partial. Four controlled iterations were evaluated. The approved prompt was stored in an intentional Prompt Volume 2.
Decision: Select `OLGA_TEST09_FORMAL_ELEGANT_V4`, variant label `REFINED`, as the approved Test09 indoor formal/elegant full-body MAIN scene reference. Accept `OLGA_WORKING_SCENE_PROMPTS_V2.md` as indexed Prompt Volume 2.
Attempt outcomes:
- V1 rejected for reduced bust volume.
- V2 rejected for exaggerated hip width and waist-to-hip contrast.
- V3 acceptable but superseded.
- V4 approved.
Reason: V4 provides the strongest overall mature identity, bust/waist/hip balance, refined outfit, tall presence, and cultural-venue distinction.
Next action: Commit without push, then verify the commit before pushing.

---

Date: 2026-07-12
Decision ID: D-016
Context: OLGA Test09 exposed repeated manual failure modes: empty prompt file, mismatched prompt IDs, unindexed Prompt Volume 2, fragmented V1–V4 history, repeated deploy/verify/closeout steps, and uncertainty about whether universal rules were stored locally and in the repository.
Decision: Defer OLGA Test10 generation until a universal NCC visual-canon pipeline standard is designed and implemented.
Adopt:
- Coverage-first workflow.
- Reference-first workflow.
- Canonical prompt IDs.
- Explicit attempt history.
- Exact reference paths.
- Planned output paths before generation.
- MAIN/ALT role assignment.
- One controlled deployment operation.
- Validator-backed enforcement.
- Per-character pipeline manifests.
- Local Voyage SQLite synchronization verification.
Pilot: OLGA Test10 neutral height-scale check will be the first end-to-end validation of the new standard.
Reason: Prevent other characters from repeating OLGA's long technical-debt cleanup and reduce future workflows to audit → generate → select → single deploy → verify/push.
Next action: Run the read-only pipeline-standard preflight.

---

Date: 2026-07-12
Decision ID: D-017
Context: OLGA Test09 exposed repeated manual failure modes: empty prompt file, mismatched prompt IDs, unindexed Prompt Volume 2, fragmented V1–V4 history, repeated deploy/verify/closeout steps, and uncertainty about whether universal rules were stored locally and in the repository. A read-only preflight identified the missing authority hierarchy, schemas, and policy needed to prevent other characters from repeating the same cleanup.

Decision: Adopt a universal NCC visual-canon pipeline authority hierarchy and create the Phase 1 authoritative artifacts.

Authority hierarchy (highest first):
1. `AGENTS.md`
2. `docs/NCC_VISUAL_CANON_WORKFLOW.md`
3. `configs/visual_canon/pipeline_policy.json`
4. `configs/visual_canon/prompt_record.schema.json`
5. `configs/visual_canon/character_manifest.schema.json`
6. `AI_CHARACTERS/<CHAR>/10_notes/<CHAR>_PIPELINE_MANIFEST.json` (future)
7. `AI_CHARACTERS/<CHAR>/06_prompts/<CHAR>_PROMPT_INDEX.md`
8. `AI_CHARACTERS/<CHAR>/06_prompts/<CHAR>_WORKING_SCENE_PROMPTS*.md`
9. `AI_CHARACTERS/<CHAR>/06_prompts/<CHAR>_PROMPT_RUN_LOG.jsonl`
10. `AI_CHARACTERS/<CHAR>/10_notes/<CHAR>_REFERENCE_PRESETS.json`
11. `AI_CHARACTERS/<CHAR>/10_notes/<CHAR>_TEST_RESULTS.md`
12. `AI_CHARACTERS/<CHAR>/10_notes/<CHAR>_CANON_INDEX.md`
13. `.voyage/CURRENT_TASK.md`
14. `.voyage/DECISIONS.md`
15. `.voyage/PROJECT_STATE.md`
16. `.voyage/CHARACTER_REGISTRY.md`
17. Local SQLite mirror (non-authoritative)

Key rules adopted:
- Canonical prompt ID: `<CHARACTER_ID>_TEST<NN>_<SCENE_ID_UPPER>_V<VERSION>`. Variant label is separate and never part of the canonical ID.
- MAIN/ALT is metadata (`role` field), not a required filename suffix. Approved filename: `<CHAR>_test<NN>_<scene_id>_v<version>_APPROVED.png`.
- JSONL registry is authoritative: exactly one record per canonical `prompt_id`.
- Git repository is the source of truth; SQLite is a mirror/index.
- One write-capable agent at a time; stale-buffer overwrite is forbidden.
- Validator MVP and deploy-tool MVP must be implemented before OLGA Test10 is generated or deployed.

Affected files:
- `docs/NCC_VISUAL_CANON_WORKFLOW.md`
- `configs/visual_canon/pipeline_policy.json`
- `configs/visual_canon/prompt_record.schema.json`
- `configs/visual_canon/character_manifest.schema.json`
- `AGENTS.md`
- `docs/PROJECT_DOCUMENTATION_INDEX.md`
- `docs/GITHUB_REFERENCE_PACK_WORKFLOW.md`
- `docs/NCC_DEPLOY_CHECKLIST.md`
- `docs/NCC_FOLDER_MAP.md`
- `docs/VOYAGE_INTEGRATION_WORKFLOW.md`
- `docs/VOYAGE_SQLITE_MEMORY_WORKFLOW.md`
- `ROADMAP.md`
- `README.md`
- `.voyage/CURRENT_TASK.md`
- `.voyage/PROJECT_STATE.md`
- `.voyage/CHARACTER_REGISTRY.md`
- `INVENTORY.md`

Reason: Prevent other characters from repeating OLGA's long technical-debt cleanup and reduce future workflows to audit → generate → select → single deploy → verify/push.

Result:
- Phase 1 pipeline artifacts published.
- OLGA Test10 remains deferred until validator and deploy-tool MVPs are ready.
- Next task: `NCC-VISUAL-CANON-PIPELINE-VALIDATOR-MVP-2026-07-12`.

Next action: Run validator MVP preflight, then implement `tools/validate_visual_canon_pipeline.py`.

---

Date: 2026-07-14
Decision ID: D-018
Context: The deploy-tool MVP preflight found that the published workflow assigned the future tool responsibility for Decisions, Inventory, staging, commit, and publication state. This conflicted with the approved narrow, auditable, existing-record-only MVP.

Decision: Adopt a non-publishing deploy-tool boundary.

- Default mode is read-only dry-run; apply requires explicit `--apply`.
- One operation handles one existing registered, generated, human-selected and human-approved attempt.
- The tool copies the selected source output and never moves or deletes it.
- The tool may update exactly one existing prompt registry record, Test Results, Reference Presets,
  and Canon Index only when the explicit verdict is `APPROVED_AS_CANON`.
- Prompt Index, prompt source, prompt heading and working prompt volume must already exist; the tool
  validates their linkage without editing them.
- The tool does not modify Voyage files, Decisions, Inventory, manifests, policy or schemas.
- The tool does not stage, commit, amend, push, force, clean or reset.
- The tool performs no SQLite read, write, export, migration or rebuild.
- Failed post-validation requires rollback.

Human workflow owns inventory refresh, diff review, staging, commit, push verification, Voyage
closeout and SQLite synchronization.

Affected files:
- `docs/NCC_VISUAL_CANON_WORKFLOW.md`
- `docs/NCC_DEPLOY_CHECKLIST.md`
- `configs/visual_canon/pipeline_policy.json`
- `.voyage/CURRENT_TASK.md`
- `.voyage/PROJECT_STATE.md`
- `.voyage/DECISIONS.md`

Reason: Keep the deploy operation deterministic, reversible and reviewable while preserving human
authority over project history and Git publication.

Result: OLGA Test10 remains deferred until the deploy-tool implementation is tested, independently
verified and published.

Next action: Implement the deploy-tool MVP under the corrected authority, then verify and publish it
before starting the OLGA Test10 pilot.
