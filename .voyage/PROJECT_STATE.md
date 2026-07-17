# PROJECT_STATE

**Project:** narrative-character-canon

**Status:** ACTIVE / CHARACTER CANON REPOSITORY

**Last verified:** 2026-07-17

**Repository:** `C:\DEV\Narrative\narrative-character-canon`

**Deploy-tool publication verification HEAD:** `50e56c663b4ee776799eb4a88c5a3f6362486dd3`

**Deploy tool state:** `PUBLISHED_POST_PUSH_VERIFIED`

**Deploy tool version:** `1.0.1`

**Purpose:** Единый источник правды для визуального канона персонажей Narrative / Voyage.

---

## Подтверждённые факты (проверено по файлам, не со слов)

* Repository foundation существует, `AI_CHARACTERS/` содержит 9 персонажей: ANDREY, ANDREY_JUNIOR, EGOR, KIRA, MAKSIM, MARINA, NIKA, OLGA, SERGEY; плюс `_JOINT_SCENES/KIRA_ANDREY`.
* `AGENTS.md` tracked в Git и актуален (обновлён 2026-07-12 после D-017).
* `ROADMAP.md`, `PHASE_1_CURRENT_LAPTOP_CLOUD_PIPELINE.md`, `PHASE_2_LOCAL_AI_WORKSTATION_PIPELINE.md` существуют в корне.
* `docs/NCC_VISUAL_CANON_WORKFLOW.md` — ACTIVE universal workflow (создан 2026-07-12).
* `configs/visual_canon/pipeline_policy.json` — ACTIVE machine-readable policy.
* `configs/visual_canon/prompt_record.schema.json` — ACTIVE JSON Schema для JSONL-реестра.
* `configs/visual_canon/character_manifest.schema.json` — ACTIVE JSON Schema для per-character manifests.
* `tools/validate_visual_canon_pipeline.py` — ACTIVE validator MVP (read-only, standard library, compatibility/strict modes).
* `tests/visual_canon/` — ACTIVE standard-library `unittest` suite for the validator.
* `docs/GITHUB_REFERENCE_PACK_WORKFLOW.md` и `tools/build_scene_reference_pack.py` / `.ps1` — рабочий GitHub-first scene reference tool.
* ANDREY: `CANON_READY_2D` / `PROMPT_PIPELINE_ACTIVE`; face/body/expression canons и control tests 01–06 опубликованы.
* ANDREY_JUNIOR: `BASE_CANON_APPROVED` / `CONTROL_TESTS_APPROVED` / `PROMPT_PIPELINE_ACTIVE`; son-version active; public_filtered only.
* KIRA: `CANON_READY_2D` / `PROMPT_PIPELINE_ACTIVE_CORE`; face/body/outfit canons и control tests опубликованы.
* KIRA_ANDREY: `JOINT_CONTROL_TESTS_APPROVED` / `DUO_SCENE_PACKS_APPROVED`.
* OLGA: `BASE_CANON_APPROVED` / `CONTROL_TESTS_APPROVED` (Tests 01–09 published, Test10 registered not deployed) / `PROMPT_PIPELINE_ACTIVE`. Test10 (`neutral_height_scale_check`) candidate 02 is HUMAN_APPROVED with future deployment role MAIN; candidate 01 rejected; one pre-deploy JSONL holding record exists; image remains in external LOCAL_STORAGE; no deployment has occurred; destination folder remains absent.
* MARINA, NIKA, SERGEY, MAKSIM, EGOR: `TEXT_CANON_READY` / `CANON_PROMPTS_CREATED`; папки структуры и generation prompts есть, изображений пока нет.
* SQLite DB отстаёт от репозитория (последнее обновление 2026-07-07); синхронизация отложена до Phase 7 / отдельного задачи. Репозиторий остаётся авторитетным источником правды.
* Validator MVP is published at `78da93a`; 32/32 tests pass, and compatibility mode scans 4 registries / 46 records with 0 errors.
* Deploy-tool MVP (`d15b43c`) and authority-enforcement correction (`2d808a9`) are published; post-push convergence was verified at `50e56c663b4ee776799eb4a88c5a3f6362486dd3`.
* Deploy tool state: `PUBLISHED_POST_PUSH_VERIFIED`; version: `1.0.1`.
* Technical validation: 112 tests passed at the verified implementation commit; validator baseline is 4 registries / 46 records / 0 errors / 153 legacy warnings.
* The original authority/Inventory exploit is blocked; rollback and concurrency behavior were independently verified.
* OLGA Test10 registration state: candidate 02 HUMAN_APPROVED; future deployment role MAIN confirmed; candidate 01 rejected; one pre-deploy JSONL holding record appended (`verdict=CANDIDATE`, `selected=false`, `deployed=false`); role, output_path, storage, and content_tier absent.
* Approved candidate exists externally: `LOCAL_STORAGE/narrative-character-canon/generation_candidates/OLGA/Test10/OLGA_TEST10_NEUTRAL_HEIGHT_SCALE_CHECK_V1_candidate_02_HUMAN_APPROVED.png`.
* Candidate SHA-256: `1717cd17dc43cdbf019cd269752ca183cbf8a21bc618da6f8bd123c406708757`; dimensions: `1122 × 1402`; Generation ID: `24a30d17-42db-422b-8eff-0d99f8607410`.
* Approval record SHA-256: `4f5d479ba64a5bb3b9bf3ad2282110a0ebd5a851cdd212d9fe32c6a6c70bf120`.
* Test10 prompt source: `AI_CHARACTERS/OLGA/06_prompts/OLGA_WORKING_SCENE_PROMPTS_V2.md`; Prompt Index: `AI_CHARACTERS/OLGA/06_prompts/OLGA_PROMPT_INDEX.md`.
* Mandatory OLGA face canon and body references A/B are verified; optional Test05 omitted.
* No image has been copied into the repository.
* Test10 deployment destination `AI_CHARACTERS/OLGA/07_generated/canon_tests/10_neutral_height_scale_check/` remains absent.
* No deployment has occurred. No deploy-tool dry-run or apply has been run.
* Registration commit contains exactly four files (JSONL holding record, D-020, CURRENT_TASK, PROJECT_STATE), not pushed.
* Inventory and SQLite remain unchanged.
* Active next step: `NCC-OLGA-TEST10-DEPLOYMENT-PREFLIGHT-2026-07-17` (`READY_FOR_READONLY_DEPLOYMENT_PREFLIGHT`).
* Decision D-020 recorded.

---

## Активные ограничения

* Только один write-capable agent одновременно.
* Перед записью: clean tree, no staged files, expected HEAD match, target files re-read.
* Любая генерация изображений требует предварительного `prompt_id`, `reference_paths`, и planned `output_path`.
* Test10 generation candidates must remain outside the final canon destination until human selection; do not create JSONL registration or deploy before a real approved attempt exists.
* Local-only и private/adult outputs не коммитить; не ссылаться на них из repo-tracked presets/manifests.

---

## Immediate next task

См. `.voyage/CURRENT_TASK.md` — `NCC-OLGA-TEST10-DEPLOYMENT-PREFLIGHT-2026-07-17`.

**Status:** `READY_FOR_READONLY_DEPLOYMENT_PREFLIGHT`

**Priority:** `P0`
