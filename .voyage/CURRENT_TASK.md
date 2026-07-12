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

## Completed task

**Task ID:** `NCC-VISUAL-CANON-PIPELINE-VALIDATOR-MVP-2026-07-12`

**Final status:** `COMPLETED_LOCAL_AWAITING_VERIFICATION`

### Goal

Implement the minimum viable validator (`tools/validate_visual_canon_pipeline.py`) that enforces the universal pipeline policy and schemas before any future deploy operation.

### Deliverables

- `tools/validate_visual_canon_pipeline.py` — read-only validator MVP.
  - CLI: `--repo-root`, `--mode {compatibility,strict}`, `--character`, `--json-report`, `--overwrite-report`, `--no-color`, `--version`.
  - Exit codes: `0` pass, `1` validation errors, `2` CLI error, `3` internal failure, `4` repo preflight failure, `5` policy/schema load failure.
  - 40+ check IDs (`VC-001`–`VC-041`) covering policy, JSONL parsing, IDs, references, outputs, roles, MAIN uniqueness, local-only leakage, authority, and SQLite-sync policy.
- `tests/visual_canon/` — standard-library `unittest` suite.
  - `test_validator_cli.py`
  - `test_validator_prompt_records.py`
  - `test_validator_legacy_compatibility.py`
  - `fixtures/` with 11 required cases.
- Documentation updates:
  - `AGENTS.md` — validator invocation, test command, common agent tasks.
  - `docs/NCC_VISUAL_CANON_WORKFLOW.md` — §24 validator responsibility updated for MVP.
  - `docs/NCC_DEPLOY_CHECKLIST.md` — validator gate.
  - `docs/PROJECT_DOCUMENTATION_INDEX.md` — tool listing.
- `.voyage/CURRENT_TASK.md` and `.voyage/PROJECT_STATE.md` refreshed.

### Constraints respected

- Standard library only; no third-party dependencies.
- No repository writes by the validator.
- No SQLite writes.
- No character JSONL/prompts/presets/images modified.
- No `INVENTORY.md` regeneration required for tool-only change.
- No per-character manifests created.
- No OLGA Test10 folder or generation.
- No push.

### Verification command

```powershell
py -3 -m unittest discover -s tests/visual_canon -v
py -3 tools\validate_visual_canon_pipeline.py --mode compatibility --no-color
```

---

## Completed task

**Task ID:** `NCC-VISUAL-CANON-PIPELINE-VALIDATOR-MVP-VERIFY-2026-07-12`

**Final status:** `COMPLETED_NEEDS_IMPLEMENTATION_CORRECTION`

### Audit result

A read-only audit of commit `5589fcb` found the validator MVP never discovered any real character
registry:

- Discovery used the literal filename `prompt_run_log.jsonl`; real registries are named
  `<CHARACTER>_PROMPT_RUN_LOG.jsonl`, so 0 real registries were ever found.
- Both `compatibility` and `strict` modes scanned 0 files / 0 records against the real repo.
- `--character` was a documented no-op.
- The `VC-` check-ID catalog had collisions (`VC-003`, `VC-006`, `VC-009` each covered multiple
  unrelated findings) and an undocumented `VC-041`.
- JSON-report overwrite refusal returned exit code `0` instead of a CLI failure code.
- Architecture remained fully read-only and repairable; no push occurred.

Commit `5589fcb` was left unamended and unpushed.

---

## Completed task

**Task ID:** `NCC-VISUAL-CANON-VALIDATOR-MVP-DISCOVERY-CORRECTION-2026-07-12`

**Final status:** `COMPLETED_LOCAL_AWAITING_REVERIFY`

### Goal

Correct the validator MVP so it discovers and validates the repository's real character prompt
registries, implements functional `--character` scoping, stabilizes the `VC-001`–`VC-040` check
catalog, and adds realistic integration coverage — in a narrow follow-up commit on top of `5589fcb`.

### Result

- Discovery now matches `AI_CHARACTERS/<CHAR>/06_prompts/*_PROMPT_RUN_LOG.jsonl`; the real repo's 4
  registries (ANDREY, ANDREY_JUNIOR, KIRA, OLGA — 46 records total) are found and scanned.
- `--character <NAME>` resolves case-insensitively against `AI_CHARACTERS/` (including joint/pair
  namespaces one level under an underscore-prefixed container such as `_JOINT_SCENES`); unknown or
  ambiguous names exit `2` under a new `CLI-002` code, separate from the `VC-` catalog.
- `CHECK_CATALOG` (module-level, `VC-001`–`VC-040`, no `VC-041`) is now the single source of truth;
  every `_error`/`_warn` call site was remapped to it; fatal/CLI-level failures moved to `CLI-001`
  (repo-root preflight), `CLI-003`/`CLI-004` (JSON-report failures), and `INTERNAL`.
- JSON-report overwrite-refusal and missing-parent-directory failures now exit `2` (were `0`); the
  parent directory is never auto-created.
- 13 new tests added in `tests/visual_canon/test_validator_discovery.py`; the 3 existing test files
  updated to realistic `<CHAR>_PROMPT_RUN_LOG.jsonl` naming under `06_prompts/` and the new VC-code
  mapping. All 32 tests pass.

### Known pre-existing data gap (not fixed by this commit — validator-only scope)

Running the corrected validator against the real repo surfaces one genuine finding: OLGA's legacy
`OLGA_TEST09_FORMAL_ELEGANT_V4` record (`AI_CHARACTERS/OLGA/06_prompts/OLGA_PROMPT_RUN_LOG.jsonl`,
line 16 — already published/deployed per this file's `NCC-OLGA-TEST09-FORMAL-ELEGANT-DEPLOY-2026-07-10`
entry, commit `1f887dc`) has `selected: true` / `deployed: true` but no `human_approval` field, so it
trips `VC-019` as a hard error. Compatibility mode against the real repo therefore exits `1`, not `0`.
This is a real, pre-existing data-completeness gap the validator now correctly surfaces — not a
validator bug. Character data was intentionally left untouched by this commit; backfilling
`human_approval` on that record is separate follow-up work, not yet scheduled.

### Constraints respected

- No amend of `5589fcb`; no push.
- Changed files limited to `tools/validate_visual_canon_pipeline.py`, the three existing
  `tests/visual_canon/test_validator_*.py` files, the new `tests/visual_canon/test_validator_discovery.py`,
  and this file.
- No character JSONL/prompts/presets/images modified.
- No `.gitignore`, `AGENTS.md`, `docs/**`, `configs/visual_canon/**`, `.voyage/PROJECT_STATE.md`, or
  `.voyage/DECISIONS.md` changes.
- No manifests, SQLite, deploy tool, or OLGA Test10 work.

---

## Active task

**Task ID:** `NCC-VISUAL-CANON-VALIDATOR-MVP-REVERIFY-2026-07-12`

**Status:** `READY_FOR_READONLY_VERIFY`

**Priority:** `P0`

### Goal

Verify the two-commit validator implementation chain (`5589fcb` → discovery-correction commit): real
registry discovery, `--character` scoping, the stabilized check-ID catalog, tests, and JSON-report exit
behavior — before push.

### Scope

- Run validator on the real repo in both `compatibility` and `strict` modes; confirm nonzero
  registries/records scanned.
- Confirm `--character OLGA` / `--character KIRA` each scan exactly one registry with nonzero records,
  and an unknown character exits `2`.
- Confirm the `VC-001`–`VC-040` catalog and the known OLGA `VC-019` gap noted above.
- Confirm tests pass and coverage is sufficient.
- Do not modify repo files during verification.

### Next action after verify

Push both local commits to `origin/main`, then proceed to the deploy-tool MVP preflight or the OLGA
Test10 pilot, depending on human control-room decision.
