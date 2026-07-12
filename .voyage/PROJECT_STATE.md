# PROJECT_STATE

**Project:** narrative-character-canon

**Status:** ACTIVE / CHARACTER CANON REPOSITORY

**Last verified:** 2026-07-12

**Repository:** `C:\DEV\Narrative\narrative-character-canon`

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
* OLGA: `BASE_CANON_APPROVED` / `CONTROL_TESTS_APPROVED` (Tests 01–09 published) / `PROMPT_PIPELINE_ACTIVE`. Test10 (`neutral_height_scale_check`) approved как следующий coverage candidate, но deferred до готовности validator MVP и deploy-tool MVP.
* MARINA, NIKA, SERGEY, MAKSIM, EGOR: `TEXT_CANON_READY` / `CANON_PROMPTS_CREATED`; папки структуры и generation prompts есть, изображений пока нет.
* SQLite DB отстаёт от репозитория (последнее обновление 2026-07-07); синхронизация отложена до Phase 7 / отдельного задачи. Репозиторий остаётся авторитетным источником правды.
* Validator MVP implemented and passing its own tests; awaiting independent read-only verification before deploy-tool MVP preflight.

---

## Активные ограничения

* Только один write-capable agent одновременно.
* Перед записью: clean tree, no staged files, expected HEAD match, target files re-read.
* Любая генерация изображений требует предварительного `prompt_id`, `reference_paths`, и planned `output_path`.
* OLGA Test10 не создавать, не генерировать и не деплоить до завершения validator MVP и deploy-tool MVP.
* Local-only и private/adult outputs не коммитить; не ссылаться на них из repo-tracked presets/manifests.

---

## Immediate next task

См. `.voyage/CURRENT_TASK.md` — `NCC-VISUAL-CANON-PIPELINE-VALIDATOR-MVP-VERIFY-2026-07-12`.
