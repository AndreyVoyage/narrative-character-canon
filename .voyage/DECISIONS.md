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
