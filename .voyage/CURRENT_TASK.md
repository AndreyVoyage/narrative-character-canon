# CURRENT_TASK

## Previous task

**Task ID:** `NCC-DALLE-17-GENERATION-2026-07-09`

**Final status:** `CLOSED_REDESIGNED`

**Closure reason:** The original blind 17-image generation list was found to duplicate existing approved visual coverage. It was replaced by a coverage-based workflow.

### Completed results from the redesigned work

- OLGA pool/wellness public-safe v1 deployed and pushed in commit `6229e0d`.
- OLGA swimsuit pool/wellness v2/v3 retained in `LOCAL_STORAGE` by human decision B.
- OLGA DALL-E evening embankment ALT deployed and pushed in commit `8e07904`.
- `01_evening_embankment` remains MAIN.
- `08_dalle_evening_embankment` is ALT / DALL-E backend variant.
- Empty duplicate `09_yoga_studio` folder was removed.

### Superseded rule

Do not continue the original 17-image count mechanically.

### Active workflow rule

Before every future generation:

1. Audit existing visual coverage.
2. Extract exact character anchors from repo canon files.
3. Select explicit reference images.
4. Prepare `prompt_id`, `reference_paths`, `output_path`, and storage tier.
5. Generate only after the scene is confirmed missing.
6. Record APPROVED / REJECTED / DRAFT result.

---

## Completed task

**Task ID:** `NCC-OLGA-FORMAL-ELEGANT-REFERENCE-PREFLIGHT-2026-07-10`

**Final status:** `COMPLETED`

### Goal

Formal/elegant coverage was `PARTIALLY_COVERED`; dedicated indoor formal/elegant full-body coverage was missing.

### Result

- Attempts V1–V4 were reviewed.
- V4 was selected as the approved formal/elegant indoor full-body result.
- The canonical prompt is stored in `OLGA_WORKING_SCENE_PROMPTS_V2.md`.
- The approved image is prepared for repo deployment.

---

## Completed task

**Task ID:** `NCC-OLGA-TEST09-FORMAL-ELEGANT-DEPLOY-2026-07-10`

**Final status:** `COMPLETED_PUBLISHED`

### Published result

- Commit: `1f887dce3705546e356ff301554433063ed7ebcd`
- Push result: `SUCCESS`
- Published branch: `main`
- HEAD equals origin/main: `YES`
- Selected prompt: `OLGA_TEST09_FORMAL_ELEGANT_V4`
- Variant: `REFINED`
- Selected output: `AI_CHARACTERS/OLGA/07_generated/canon_tests/09_formal_elegant/OLGA_test09_formal_elegant_v4_APPROVED.png`
- Formal/elegant indoor full-body coverage: `COMPLETED`
- No deployment rerun required.

---

## Completed task

**Task ID:** `NCC-OLGA-NEXT-COVERAGE-AUDIT-2026-07-11`

**Final status:** `COMPLETED_HUMAN_REVIEWED`

### Audit result

- Approved OLGA images: 14 tracked images.
- Approved scene tests: 9.
- Recommended next missing coverage: neutral full-body height/environment scale check.
- Priority: `P0`.
- Proposed prompt: `OLGA_TEST10_NEUTRAL_HEIGHT_SCALE_CHECK_V1`.
- Proposed scene: `neutral_height_scale_check`.
- Planned folder: `AI_CHARACTERS/OLGA/07_generated/canon_tests/10_neutral_height_scale_check/`.
- Planned filename: `OLGA_test10_neutral_height_scale_check_v1_APPROVED.png`.
- Storage: `repo_tracked`.
- Content tier: `public_filtered`.
- Collision check: `PASS`.
- Repository modifications during audit: `NONE`.
- Generation: `NOT STARTED`.

### Human decision

Test10 is approved as the next OLGA coverage candidate but deferred until the shared visual-canon pipeline standard, schemas, manifests, and validator are defined.

- Test10 will be the first pilot of the standardized workflow.
- Mandatory initial references: OLGA face canon sheet, body canon sheet A, body canon sheet B.
- Test05 is optional because it may introduce office-style bias.
- Prefer flat shoes or minimal low heels.
- Prefer a neutral tailored dark blouse and straight dark trousers.
- Keep the camera neutral; do not exaggerate height with a low angle.
- Do not create the Test10 folder or register Test10 as generated/approved yet.

---

## Completed task

**Task ID:** `NCC-VISUAL-CANON-PIPELINE-STANDARD-PREFLIGHT-2026-07-12`

**Final status:** `COMPLETED`

### Result

- Authority hierarchy defined: `AGENTS.md` → `docs/NCC_VISUAL_CANON_WORKFLOW.md` → `configs/visual_canon/pipeline_policy.json` + schemas → per-character manifest → prompt records → `.voyage` state → SQLite mirror.
- Canonical ID model: `<CHARACTER_ID>_TEST<NN>_<SCENE_ID_UPPER>_V<VERSION>`; variant label separate; `MAIN`/`ALT` is metadata, not filename suffix.
- Prompt-record schema: one JSONL record per `prompt_id`, mandatory fields for references, verdict, role, storage, content tier.
- Character-manifest schema: durable per-character configuration without prompt-history duplication.
- Phase 1 implementation plan approved: create workflow doc, policy, schemas; update `AGENTS.md` and workflow cross-references; update Voyage control files; regenerate inventory; commit.

---

## Completed task

**Task ID:** `NCC-VISUAL-CANON-PIPELINE-PHASE1-IMPLEMENTATION-2026-07-12`

**Final status:** `COMPLETED_PUBLISHED`

### Goal

Create the authoritative Phase 1 universal visual-canon pipeline artifacts and update all dependent documentation and Voyage control files.

### Deliverables

- `docs/NCC_VISUAL_CANON_WORKFLOW.md` — universal human-readable workflow.
- `configs/visual_canon/pipeline_policy.json` — machine-readable policy.
- `configs/visual_canon/prompt_record.schema.json` — JSON Schema for prompt attempt records.
- `configs/visual_canon/character_manifest.schema.json` — JSON Schema for per-character manifests.
- `AGENTS.md` updated: character statuses, pipeline authority, key files.
- Cross-references updated in:
  - `docs/PROJECT_DOCUMENTATION_INDEX.md`
  - `docs/GITHUB_REFERENCE_PACK_WORKFLOW.md`
  - `docs/NCC_DEPLOY_CHECKLIST.md`
  - `docs/NCC_FOLDER_MAP.md`
  - `docs/VOYAGE_INTEGRATION_WORKFLOW.md`
  - `docs/VOYAGE_SQLITE_MEMORY_WORKFLOW.md`
  - `ROADMAP.md`
  - `README.md`
- `.voyage/DECISIONS.md` updated with `D-017`.
- `.voyage/PROJECT_STATE.md` refreshed.
- `.voyage/CHARACTER_REGISTRY.md` updated.
- `INVENTORY.md` regenerated with backup.

### Constraints respected

- No validator script created.
- No deploy tool created.
- No per-character manifests created.
- No OLGA Test10 folder or generation.
- No SQLite writes or exports.

### Next action

Proceed to validator MVP preflight.

---

## Active task

**Task ID:** `NCC-VISUAL-CANON-PIPELINE-VALIDATOR-MVP-2026-07-12`

**Status:** `READY_FOR_IMPLEMENTATION_PREFLIGHT`

**Priority:** `P0`

### Goal

Design and plan the minimum viable validator (`tools/validate_visual_canon_pipeline.py`) that enforces the universal pipeline policy and schemas before any future deploy operation.

### Preflight questions

1. Which checks can be implemented with the standard library only?
2. How should the validator read `pipeline_policy.json` and the JSON schemas?
3. How should it validate existing legacy records in compatibility mode vs strict mode?
4. Which checks must be ERROR vs WARNING for the OLGA Test10 pilot?
5. How should it report duplicate `prompt_id`, missing references, and ID mismatches?
6. How should it integrate with the future deploy tool?

### Expected next report

`=== NCC VISUAL CANON PIPELINE VALIDATOR MVP PREFLIGHT RESULT ===`

Sections:
1. Git state.
2. Active-task verification.
3. Required validation checks mapped to `docs/NCC_VISUAL_CANON_WORKFLOW.md` §24.
4. Proposed CLI interface.
5. Compatibility-mode vs strict-mode behavior.
6. Legacy handling for existing prompt-run logs.
7. Exit codes and report format.
8. Exact files to create/modify.
9. Files explicitly not to create.
10. OLGA Test10 pilot validation plan.
11. Risks and stop conditions.
12. Repo files modified: `NONE`.
13. Ready for human approval? `YES/NO`.

### Forbidden during the preflight

- No implementation or repo writes.
- No validator-script creation.
- No modification of `AGENTS.md`, workflow docs, or Voyage control files.
- No SQLite write or export.
- No image generation or Test10 folder.
- No prompt-log append.
- No commit or push.
