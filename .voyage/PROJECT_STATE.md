# PROJECT_STATE

**Project:** narrative-character-canon

**Status:** ACTIVE / CHARACTER CANON REPOSITORY

**Last verified:** 2026-07-02

**Repository:** `C:\DEV\Narrative\narrative-character-canon`

**Purpose:** Единый источник правды для визуального канона персонажей Narrative / Voyage.

## Подтверждённые факты (проверено по файлам, не со слов)

* Repository foundation существует, `AI_CHARACTERS/` содержит 8 персонажей: ANDREY, KIRA, MARINA, NIKA, OLGA, SERGEY, MAKSIM, EGOR.
* `ROADMAP.md`, `PHASE_1_CURRENT_LAPTOP_CLOUD_PIPELINE.md`, `PHASE_2_LOCAL_AI_WORKSTATION_PIPELINE.md` существуют в корне.
* `docs/GITHUB_REFERENCE_PACK_WORKFLOW.md` и `tools/build_scene_reference_pack.py` / `.ps1` — рабочий GitHub-first scene reference tool.
* ANDREY: face canon Sheet A/B + expression Sheet C активны и tracked; `ANDREY_REFERENCE_PRESETS.json` заполнен (6 scene presets: portrait, body_canon, sports, formal, bar, sauna) и ссылается на существующие файлы. Body canon ещё не создан (нет файлов в `04_body_sheet/`, только `.gitkeep`).
* KIRA: face canon Sheet A/B, body canon Sheet A/B, outfits (evening_dress, sports_look), несколько approved canon_tests и `KIRA_REFERENCE_PRESETS.json` заполнен (7 scene presets, включая `sauna`) — все referenced paths в preset существуют в репозитории. Preset обновлён 2026-07-02, statuses "needs repo verification" из ROADMAP/AGENTS.md устарели относительно текущего состояния файла.
* MARINA, NIKA, OLGA, SERGEY, MAKSIM, EGOR: только структура папок (`.gitkeep`), `*_REFERENCE_PRESETS.json` присутствует, но с пустыми `scene_presets` и `text_sources: null` — это placeholder, не canon.
* AGENTS.md существует в рабочей директории, но **не tracked в git** (untracked file) — не редактировать без явного запроса пользователя.

## Известная осторожность

Не путать example сцену с реальной generation task. См. [.voyage/SCENE_REQUEST_RULES.md](SCENE_REQUEST_RULES.md).

Сцена "Кира и Андрей в сауне" (towel-covered conversation) использовалась как EXAMPLE / TOOL TEST IDEA при обсуждении reference-pack инструмента. Это не approved generation task — не генерировать, пока пользователь явно не попросит.

## Immediate next task

См. [.voyage/CURRENT_TASK.md](CURRENT_TASK.md).
