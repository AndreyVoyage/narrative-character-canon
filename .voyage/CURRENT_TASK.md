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

## Active task

**Task ID:** `NCC-VISUAL-CANON-PIPELINE-STANDARD-PREFLIGHT-2026-07-12`

**Status:** `READY_FOR_READONLY_PREFLIGHT`

**Priority:** `P0`

### Goal

Audit the repository's existing visual-canon rules, schemas, indexes, tools, Voyage workflows, character-specific prompt pipelines, and local SQLite-memory workflow. Produce an implementation plan for a universal pipeline that prevents the long manual correction sequence experienced with OLGA Test09.

### Preflight questions

1. Which required rules already exist?
2. Which rules are only implicit or character-specific?
3. Which files should become authoritative?
4. Which existing documents should be extended rather than duplicated?
5. Which validator and schema files are genuinely missing?
6. How should per-character manifests be structured?
7. How should local Voyage SQLite memory be checked and synchronized?
8. How should one approved image be deployed through one controlled operation?
9. How will Test10 be used as the first pilot?
10. How can other characters adopt the standard without repeating OLGA's technical debt?

### Candidate files to evaluate, not automatically create

- `docs/NCC_VISUAL_CANON_WORKFLOW.md`
- `configs/visual_canon/pipeline_policy.json`
- `configs/visual_canon/prompt_record.schema.json`
- `tools/validate_visual_canon_pipeline.py`
- `AI_CHARACTERS/<CHARACTER>/10_notes/<CHARACTER>_PIPELINE_MANIFEST.json`

### Existing files to inspect first

- `AGENTS.md`
- `docs/NCC_DEPLOY_CHECKLIST.md`
- `docs/GITHUB_REFERENCE_PACK_WORKFLOW.md`
- `docs/VOYAGE_INTEGRATION_WORKFLOW.md`
- `docs/VOYAGE_SQLITE_MEMORY_WORKFLOW.md`
- `docs/PROJECT_DOCUMENTATION_INDEX.md`
- `docs/NCC_FOLDER_MAP.md`
- `.voyage/SCENE_REQUEST_RULES.md`
- `.voyage/CURRENT_TASK.md`
- `.voyage/DECISIONS.md`
- `.voyage/PROJECT_STATE.md`
- Existing tools and validators.
- All character prompt indexes, prompt-run logs, reference presets, and manifest-like files.

### Expected next report

`=== NCC VISUAL CANON PIPELINE STANDARD PREFLIGHT RESULT ===`

Expected sections:

1. Git state.
2. Active-task verification.
3. Existing authoritative workflow files.
4. Existing character-specific pipeline structures.
5. Rules already enforced.
6. Rules documented but not enforced.
7. Missing universal rules.
8. Existing tools that can be reused.
9. Duplicate-document risk.
10. Proposed authority hierarchy.
11. Proposed universal ID model.
12. Proposed prompt-record schema.
13. Proposed per-character manifest schema.
14. Proposed validation checks.
15. Proposed one-operation deployment workflow.
16. Proposed SQLite-memory synchronization workflow.
17. Exact files to create.
18. Exact files to modify.
19. Files explicitly not to create.
20. Migration impact for OLGA.
21. Migration impact for KIRA.
22. Migration impact for ANDREY.
23. Migration impact for other characters.
24. Test10 pilot plan.
25. Risks and stop conditions.
26. Implementation phases.
27. Repo files modified: `NONE`.
28. Ready for human approval? `YES/NO`.

### Forbidden during the preflight

- No implementation or repo writes.
- No schema-file or validator-script creation.
- No modification of `AGENTS.md` or workflow documentation.
- No SQLite write or export.
- No image generation or Test10 folder.
- No prompt-log append.
- No commit or push.
