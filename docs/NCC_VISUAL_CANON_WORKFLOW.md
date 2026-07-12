# NCC Visual Canon Pipeline Workflow

> **Authority level:** Level 2 — universal human-readable workflow for all AI agents and human reviewers.
> **Scope:** Visual-canon generation, selection, deployment, validation, Git publication, and local-memory synchronization for `narrative-character-canon`.
> **Status:** ACTIVE
> **Created:** 2026-07-12

---

## 1. Purpose and scope

This document defines the single universal pipeline that every character, scene, and generation attempt must follow. It prevents the manual correction sequence experienced during OLGA Test09 by making authority, IDs, states, and human gates explicit.

The pipeline applies to:

- New character canon creation.
- Control tests and scene tests.
- MAIN and ALT reference outputs.
- Pair / joint scenes.
- Local-only and private outputs.

It does not apply to:

- Administrative documentation updates without generation.
- Tool development (those follow normal software-engineering workflow).
- SQLite-memory tooling outside the synchronization rules below.

---

## 2. Authority hierarchy

Read these sources in order before any write-capable operation:

1. **Level 1 — `AGENTS.md`** — agent entry point and mandatory-read rules.
2. **Level 2 — `docs/NCC_VISUAL_CANON_WORKFLOW.md`** (this file) — universal workflow.
3. **Level 3 — `configs/visual_canon/pipeline_policy.json` and JSON schemas** — machine-readable policy and schemas.
4. **Level 4 — `AI_CHARACTERS/<CHAR>/10_notes/<CHAR>_PIPELINE_MANIFEST.json`** — per-character durable configuration (created after validator/deploy-tool pilot).
5. **Level 5 — prompt index, working prompt volumes, JSONL attempt registry, presets, test results, canon index** — operational records.
6. **Level 6 — `.voyage/CURRENT_TASK.md`, `.voyage/DECISIONS.md`, `.voyage/PROJECT_STATE.md`, `.voyage/CHARACTER_REGISTRY.md`** — Voyage operational state.
7. **Level 7 — local SQLite memory mirror** — query/index layer and audit helper.

Read these sources from top to bottom. Lower-numbered levels are higher authority; more specific levels extend and clarify the levels above them. The Git repository — published commits, tracked files, and verified `.voyage` state — is the primary source of truth. `AGENTS.md` is the mandatory agent entry point, but it does not override this universal workflow, the machine-readable policy, the JSON schemas, or any verified repository state. Local SQLite memory is only a mirror/index and must never silently overwrite authoritative repository files. If any source contradicts verified Git state, the Git state wins.

---

## 3. Source-of-truth policy

- **Git repository is the primary source of truth.** Published commits, tracked files, and `.voyage` control files are authoritative.
- **Local SQLite memory is a mirror and index.** It must never silently overwrite authoritative repository files.
- **Conflict resolution:** published Git state wins; SQLite lag is reported; SQLite is synchronized from verified repository facts; exports may update generated snapshot files (`.voyage/CONTEXT_SNAPSHOT.md`, `.voyage/STATE_EXPORT.json`, `.voyage/EVENTS_EXPORT.jsonl`) only through an explicit human-approved workflow.
- **Local-only paths and secrets** remain outside the repository and must not be referenced from repo-tracked presets or manifests.

---

## 4. Universal lifecycle

1. **Coverage audit** — confirm the scene/reference type is genuinely missing and non-duplicative.
2. **Scene request approval** — human converts EXAMPLE → REQUESTED.
3. **ID and path reservation** — reserve `test_id`, `prompt_id`, `scene_id`, planned output folder and filename.
4. **Reference pack** — select mandatory and optional references; build local reference pack.
5. **Generation attempts** — human generates images outside the repository.
6. **Attempt verdicts** — human labels each version: `DRAFT`, `CANDIDATE`, `SUPERSEDED`, `REJECTED`, `APPROVED_AS_TEST`, `APPROVED_AS_CANON`, `APPROVED_AS_LOCAL`.
7. **Selection and role** — human selects one MAIN per `test_id`; optional ALT records allowed.
8. **One-operation deploy** — deployment tool performs all repository updates atomically.
9. **Validator pass** — validator checks IDs, paths, records, and Git state.
10. **Commit** — human verifies staged scope; tool commits.
11. **Verify and push** — human final audit; pushes.
12. **SQLite sync** — record verified facts to local SQLite and export snapshots.

---

## 5. Coverage-first gate

Before any generation:

- Audit existing approved images for the character.
- Build a coverage matrix.
- Identify duplicates and adjacent coverage.
- Rank genuinely missing coverage.
- Select one recommended next task.
- Obtain human approval before reserving IDs.

Do not generate because a scene "sounds nice". Generate because coverage is missing.

---

## 6. Reference-first gate

Before any generation:

- Identify mandatory face/body references from the character manifest or presets.
- Identify optional references.
- Confirm every reference path exists and is Git-tracked.
- Build a local reference pack.
- Record `reference_paths` in the planned prompt attempt.

Do not generate without explicit reference selection.

---

## 7. ID reservation before generation

Reserve and document before generation:

- `character_ids` (array; first is primary).
- `primary_character_id`.
- `test_number` integer.
- `scene_id` lowercase snake_case.
- `test_id`: `<CHARACTER_ID>_TEST<NN>_<SCENE_ID_UPPER>`.
- `prompt_id`: `<TEST_ID>_V<VERSION>`.
- planned output folder: `AI_CHARACTERS/<CHAR>/07_generated/canon_tests/<NN>_<scene_id>/`.
- planned output filename: `<CHAR>_test<NN>_<scene_id>_v<version>_APPROVED.png`.

If multiple characters appear in a pair scene, use a pair namespace and reference both character manifests.

---

## 8. Prompt-attempt states

| State | Meaning | Output path required? |
|---|---|---|
| `DRAFT` | Generation requested, not reviewed. | No |
| `CANDIDATE` | Visually acceptable, awaiting selection. | No |
| `SUPERSEDED` | Acceptable but replaced by later version. | No |
| `REJECTED` | Not used; reason required. | No |
| `APPROVED_AS_TEST` | Selected for repo as control test. | Yes |
| `APPROVED_AS_CANON` | Selected for repo as active canon. | Yes |
| `APPROVED_AS_LOCAL` | Selected but kept local-only. | No (local path may be recorded separately) |

Rules:

- Exactly one record per canonical `prompt_id` exists in the JSONL registry.
- Exactly one selected MAIN per `test_id`.
- Multiple ALT records per `test_id` are allowed.
- Rejected undeployed attempts must not invent a fake output path.

---

## 9. Human approval gates

| Gate | Approver | Output |
|---|---|---|
| Scene request | Human control room | EXAMPLE → REQUESTED |
| Coverage recommendation | Human control room | Approved next scene and test number |
| Reference pack | Human control room | Approved references before generation |
| Attempt verdict | Human reviewer | Label per version |
| Selection and role | Human reviewer | Selected MAIN / ALT |
| Deploy scope | Human reviewer | Staged files and commit message |
| Push | Human reviewer | Final verification and push |

Canonical IDs, verdicts, selected results, and decision IDs are never auto-approved or auto-fixed.

---

## 10. Prompt storage and prompt volumes

- Every active prompt ID must resolve to a section in a working prompt volume.
- Prompt volumes are numbered intentionally (`*_WORKING_SCENE_PROMPTS.md`, `*_WORKING_SCENE_PROMPTS_V2.md`, etc.).
- The prompt index must list every volume and every active prompt ID.
- Rejected attempts may store metadata only, but must still have a JSONL registry record.
- Do not create a new volume unless the current volume becomes unmanageable.

---

## 11. Output-path planning

Planned output paths must be recorded before generation for repo-tracked attempts.

Future approved filename format:

```text
<CHAR>_test<NN>_<scene_id>_v<version>_APPROVED.png
```

Example:

```text
OLGA_test10_neutral_height_scale_check_v1_APPROVED.png
```

`MAIN` and `ALT` are metadata fields, not required filename suffixes. Historical filenames remain unchanged.

---

## 12. MAIN / ALT role rules

- `role` is metadata: `MAIN` or `ALT`.
- One selected `MAIN` per `test_id`.
- `ALT` records are comparison references or backend variants.
- `ALT` must not silently replace `MAIN`.
- Preset registration must reflect the role.

---

## 13. Storage tiers

- `repo_tracked` — stored in the Git repository, subject to LFS and content policy.
- `local_only` — stored outside the repository, never committed.

Local-only outputs must not be referenced from repo-tracked presets or manifests.

---

## 14. Content tiers

- `public_filtered` — safe for repository; non-explicit.
- `adult_local` — adult content; local-only.
- `private_local` — private content; local-only.

Only adult characters may appear in `adult_local` or `private_local` outputs. Base canon remains neutral and production-safe.

---

## 15. Local-only protection

- Local-only images live in `LOCAL_STORAGE/` or other user-managed paths.
- They are never committed.
- They are never referenced by GitHub raw links.
- A local-only record may note the local path in its `local_only_reason`, but the JSONL registry must not treat that path as a repo output.

---

## 16. One-record-per-prompt-ID JSONL rule

- The JSONL file is the authoritative prompt-attempt registry.
- Exactly one JSON object per canonical `prompt_id`.
- It is not a multi-event append-only event stream; Git history and Voyage decisions provide audit history.
- When an attempt is updated (e.g., verdict changes), the existing line is conceptually replaced; in practice the file may be rewritten by the deploy tool.

---

## 17. Test Results, Preset, and Canon Index linkage

After a repo-tracked selection:

- JSONL registry record must exist with `selected: true`, `role`, `output_path`, `storage`, `content_tier`.
- Prompt index must list the selected prompt ID.
- Working prompt volume must contain the prompt text or metadata.
- Test results must mention the selected output.
- Reference preset must register the scene (MAIN or ALT).
- Canon index may be updated if the output becomes active canon.

Validator ensures these linkages are consistent.

---

## 18. Git LFS requirements

Tracked binary formats (`.png`, `.jpg`, `.jpeg`, `.webp`, `.psd`, `.mp4`, `.mov`) must be covered by `.gitattributes` and stored via Git LFS. The validator checks this.

---

## 19. Voyage task and decision requirements

- Every deploy operation must have a corresponding Voyage task.
- Every significant architectural or policy decision must be recorded in `.voyage/DECISIONS.md` with a unique `D-XXX` ID.
- `.voyage/CURRENT_TASK.md` must be updated when tasks complete or new tasks begin.
- `.voyage/PROJECT_STATE.md` must be refreshed when facts become stale.
- `.voyage/CHARACTER_REGISTRY.md` must reflect actual tracked files and presets.

---

## 20. SQLite synchronization policy

- SQLite records verified repository facts **after** Git commit.
- Exports (`CONTEXT_SNAPSHOT.md`, `STATE_EXPORT.json`, `EVENTS_EXPORT.jsonl`) are generated from SQLite and may be committed as generated snapshots.
- SQLite must not silently overwrite authoritative `.voyage/*.md` files.
- If SQLite lags behind the repo, the validator reports it and the next deploy operation synchronizes the DB from verified repo facts.
- Local-only paths and secrets never enter tracked exports.

---

## 21. UTF-8 policy

- All new text and JSON files must be UTF-8 without BOM.
- Existing files keep their encoding; convert only if corruption is detected.
- Mojibake is not permitted. Validate with `file -i`, Python UTF-8 decode, or equivalent.

---

## 22. Concurrent-agent and stale-editor policy

- Only one write-capable agent may operate in the repository at a time.
- Before writes:
  - tracked tree must be clean;
  - nothing staged;
  - expected HEAD must match;
  - target files must be re-read immediately before writing;
  - detect external modification through content hash or modified timestamp where practical.
- Stale editor buffers must never overwrite newer disk content without human comparison.

---

## 23. Legacy compatibility

- Do not rename historical prompt files.
- Do not rename historical images.
- Do not rewrite valid legacy JSONL solely to match the new schema.
- Validators support a compatibility mode that warns about legacy fields but does not fail.
- Migration to strict mode is explicit and character-by-character.

---

## 24. Validator responsibility

The validator `tools/validate_visual_canon_pipeline.py` is available as of Phase 1 (MVP). It is read-only and never modifies the repository. Run it before every commit that touches the visual-canon pipeline:

```powershell
py -3 tools\validate_visual_canon_pipeline.py --mode compatibility --no-color
py -3 tools\validate_visual_canon_pipeline.py --mode strict --no-color
```

MVP checks:

- Policy and schema load.
- UTF-8 validity and mojibake hints.
- JSONL parseability.
- Required fields (strict mode errors; compatibility mode warns on legacy deviations).
- Duplicate `prompt_id` values.
- Variant label separation from `prompt_id`.
- `character_ids` / `primary_character_id` / `test_id` consistency.
- `test_number` and `version` consistency.
- `backend`, `verdict`, `role`, `storage`, `content_tier` against policy.
- `prompt_source` existence and non-emptiness; local-only leakage detection.
- `reference_paths` existence.
- `output_path` rules per `storage` and `content_tier`.
- Selected records require approved verdict and human-approval gate.
- MAIN uniqueness per `test_id`.
- Authority and SQLite-sync policy values.

Checks not yet implemented (reserved for Phase 2/3):

- Full canonical-ID consistency across filename, folder, index, preset, and test results.
- Prompt-index linkage.
- Test-results, preset, and canon-index linkage.
- Git LFS coverage verification.
- Voyage task-state validity.
- Decision-ID uniqueness.
- Git cleanliness and staged-scope validation.

Validator must pass before commit. Stop if the validator reports errors.

---

## 25. Deployment-tool responsibility

The deployment tool (`tools/deploy_visual_canon_result.py`, Phase 3) will:

- Reserve IDs and paths.
- Move the selected image into the repo folder.
- Update JSONL registry for all attempts (rejected + selected).
- Update prompt index and working prompt volumes.
- Update test results.
- Update reference preset.
- Conditionally update canon index.
- Update Voyage task/decision/state files.
- Regenerate inventory with backup.
- Run validator.
- Stage allowed files.
- Produce a human-review report.

The tool never commits or pushes without human approval.

---

## 26. Standard stop conditions

Stop and report to human control room if:

- HEAD does not match expected.
- tracked tree is dirty.
- staged files exist unexpectedly.
- active task does not authorize the operation.
- validator fails.
- canonical ID includes variant label.
- MAIN/ALT is required in filename.
- SQLite would overwrite authoritative repo files.
- local-only path would be committed.
- duplicate decision or prompt ID detected.
- reference path does not exist or is not tracked.

---

## 27. Minimal human workflow

For a new approved scene:

1. Human approves coverage recommendation.
2. Agent reserves IDs and builds reference pack.
3. Human approves reference pack.
4. Human generates attempts and selects MAIN/ALT.
5. Agent runs deploy tool; validator passes.
6. Human verifies staged scope.
7. Tool commits.
8. Human verifies commit and pushes.
9. Agent records to SQLite and exports snapshots.

---

## 28. OLGA Test10 pilot boundary

- OLGA Test10 (`neutral_height_scale_check`) is approved as the first pilot of the new pipeline.
- It must not be created, generated, or deployed until Phase 4.
- Phase 4 requires validator MVP and deploy-tool MVP to exist and be approved.
- The planned IDs and references may be documented in planning materials, but no filesystem entries may be created in Phase 1.
