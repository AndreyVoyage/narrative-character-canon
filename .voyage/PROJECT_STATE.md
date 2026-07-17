# PROJECT_STATE

**Project:** narrative-character-canon

**Status:** ACTIVE / CHARACTER CANON REPOSITORY

**Last verified:** 2026-07-17

**Repository:** `C:\DEV\Narrative\narrative-character-canon`

**Published HEAD / origin/main:** `50e56c663b4ee776799eb4a88c5a3f6362486dd3`

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
* OLGA: `BASE_CANON_APPROVED` / `CONTROL_TESTS_APPROVED` (Tests 01–09 published) / `PROMPT_PIPELINE_ACTIVE`. Test10 (`neutral_height_scale_check`) approved as the next deployment candidate, but is not deployed; its source image and prompt record still require read-only preflight verification.
* MARINA, NIKA, SERGEY, MAKSIM, EGOR: `TEXT_CANON_READY` / `CANON_PROMPTS_CREATED`; папки структуры и generation prompts есть, изображений пока нет.
* SQLite DB отстаёт от репозитория (последнее обновление 2026-07-07); синхронизация отложена до Phase 7 / отдельного задачи. Репозиторий остаётся авторитетным источником правды.
* Validator MVP is published at `78da93a`; 32/32 tests pass, and compatibility mode scans 4 registries / 46 records with 0 errors.
* Deploy-tool MVP (`d15b43c`) and authority-enforcement correction (`2d808a9`) are published; post-push convergence was verified at `50e56c663b4ee776799eb4a88c5a3f6362486dd3`.
* Deploy tool state: `PUBLISHED_POST_PUSH_VERIFIED`; version: `1.0.1`.
* Technical validation: 112 tests passed at the verified implementation commit; validator baseline is 4 registries / 46 records / 0 errors / 153 legacy warnings.
* The original authority/Inventory exploit is blocked; rollback and concurrency behavior were independently verified.
* OLGA Test10 is not deployed. Read-only inspection confirmed that its planned destination folder and file do not exist yet.
* No Test10 deployment request has been applied, and no production deploy `--apply` occurred.
* Inventory and character files were unchanged by publication; SQLite remains unsynchronised; D-018 remains unchanged.

---

## Активные ограничения

* Только один write-capable agent одновременно.
* Перед записью: clean tree, no staged files, expected HEAD match, target files re-read.
* Любая генерация изображений требует предварительного `prompt_id`, `reference_paths`, и planned `output_path`.
* OLGA Test10 не создавать, не копировать и не деплоить до завершения read-only deployment preflight и отдельной человеческой проверки dry-run.
* Local-only и private/adult outputs не коммитить; не ссылаться на них из repo-tracked presets/manifests.

---

## Immediate next task

См. `.voyage/CURRENT_TASK.md` — `NCC-OLGA-TEST10-DEPLOYMENT-PREFLIGHT-2026-07-17`.

**Status:** `READY_FOR_READONLY_PREFLIGHT`

**Priority:** `P0`
