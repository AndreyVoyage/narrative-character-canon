# PROJECT_STATE

**Project:** narrative-character-canon

**Status:** ACTIVE / CHARACTER CANON REPOSITORY

**Last verified:** 2026-07-19

**Repository:** `C:\DEV\Narrative\narrative-character-canon`

**Published Test10 deployment HEAD:** `b5556f8a0d94b6a4f6478c92d0175900afe4ecda`

**Deploy tool state:** `PUBLISHED_POST_PUSH_VERIFIED`

**Deploy tool version:** `1.0.1`

**Purpose:** Единый источник правды для визуального канона персонажей Narrative / Voyage.

---

## Подтверждённые факты (проверено по файлам, не со слов)

* Bootstrap character tool MVP is implemented: `tools/bootstrap_character.py` with JSON schema contract at `configs/visual_canon/character_bootstrap.schema.json` and 30 tests at `tests/visual_canon/test_bootstrap_character.py`. Decision D-022 recorded.

* Cline control layer is implemented: `.clinerules/` (4 rule files) and `.cline/skills/ncc-reference-import/` (SKILL.md, example task-spec template, `scripts/import_references.py`). The skill is a dry-run-first, SHA-256-verified, copy-only reference importer with atomic rollback; it never edits metadata, stages, commits, pushes, or touches SQLite. 23 tests at `tests/visual_canon/test_cline_reference_import_skill.py`. Decision D-029 recorded.

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
* OLGA: `BASE_CANON_APPROVED` / `CONTROL_TESTS_APPROVED` (Tests 01–10 published) / `PROMPT_PIPELINE_ACTIVE`.
  * Test10 (`neutral_height_scale_check`) candidate 02 is published.
  * Prompt ID: `OLGA_TEST10_NEUTRAL_HEIGHT_SCALE_CHECK_V1`
  * Verdict: `APPROVED_AS_TEST`; Role: `MAIN`; Selected: `true`; Deployed: `true`.
  * Published commit: `b5556f8a0d94b6a4f6478c92d0175900afe4ecda`.
  * PNG path: `AI_CHARACTERS/OLGA/07_generated/canon_tests/10_neutral_height_scale_check/OLGA_test10_neutral_height_scale_check_v1_APPROVED.png`.
  * PNG SHA-256: `1717cd17dc43cdbf019cd269752ca183cbf8a21bc618da6f8bd123c406708757`.
  * Test Results and Reference Presets updated during deployment.
  * Canon Index correctly remained unchanged because Test10 is `APPROVED_AS_TEST`, not `APPROVED_AS_CANON`.
  * Inventory refresh remains pending as a separate optional task.
  * SQLite synchronization remains pending as a separate optional task.
* MARINA: `BASE_CANON_APPROVED` / `CONTROL_TESTS_APPROVED` / `PROMPT_PIPELINE_ACTIVE`; 3 base-canon images, 5 support expression sheets, 3 outfit references, and Control Tests 01–07 are published; prompt pipeline contains 18 unique records and scene presets are active.
* NIKA, SERGEY, MAKSIM, EGOR: `TEXT_CANON_READY` / `CANON_PROMPTS_CREATED`; папки структуры и generation prompts есть, изображений пока нет. EGOR VNE text canon sync complete (D-028): height (180 cm), weight (83 kg), cleft chin, aquiline nose added; stubble deferred; next step is user visual reference review.
* SQLite DB отстаёт от репозитория (последнее обновление 2026-07-07); синхронизация отложена как отдельная задача. Репозиторий остаётся авторитетным источником правды.
* Validator MVP is published at `78da93a`; 32/32 validator tests pass. After MARINA Test01–Test07 registration, compatibility mode discovers 5 character registries / 65 aggregate records.
* Deploy-tool MVP (`d15b43c`) and authority-enforcement correction (`2d808a9`) are published; post-push convergence was verified at `50e56c663b4ee776799eb4a88c5a3f6362486dd3`.
* Deploy tool state: `PUBLISHED_POST_PUSH_VERIFIED`; version: `1.0.1`.
* Technical validation: 112 tests passed at the verified implementation commit.
* Current validator baseline after MARINA Test01–Test07: 5 registries, 65 aggregate records, 0 errors; legacy warnings are non-blocking in compatibility mode.
* The original authority/Inventory exploit is blocked; rollback and concurrency behavior were independently verified.
* OLGA Test10 is fully published and deployed. The complete deploy-sequence chain (dry-run, apply, verify, commit-verify, push) was executed and all steps completed successfully.
* HEAD, origin/main, and remote main were synchronized at `ea8591c60e792470d0eea2653564a4138424439c` before the MARINA Test01–Test07 publication commit.
* Decision D-020 recorded.

---

## Активные ограничения

* Только один write-capable agent одновременно.
* Перед записью: clean tree, no staged files, expected HEAD match, target files re-read.
* Любая генерация изображений требует предварительного `prompt_id`, `reference_paths`, и planned `output_path`.
* Человеческое одобрение обязательно перед любой генерацией изображений.
* Local-only и private/adult outputs не коммитить; не ссылаться на них из repo-tracked presets/manifests.

---

## Immediate next task

См. `.voyage/CURRENT_TASK.md` — `NCC-NEXT-VISUAL-TARGET-SELECTION-2026-07-18`.

**Status:** `AWAITING_HUMAN_SELECTION`

**Priority:** `P0`

No new image generation is authorized until the human owner selects the next character and scene.