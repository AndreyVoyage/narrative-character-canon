# PROJECT_DOCUMENTATION_INDEX

> **Статус:** ACTIVE — единая карта документации и управляющих файлов проекта `narrative-character-canon`.
> **Создан:** 2026-07-09
> **Источник:** Voyage framework memory + audit + dual-backend workflow TZ
> **Назначение:** Главная карта штаба. Читать первым перед любой работой с репозиторием.

---

# 1. Главная папка проекта

```text
C:\DEV\Narrative\narrative-character-canon\
```

Главные файлы верхнего уровня:

```text
C:\DEV\Narrative\narrative-character-canon\INVENTORY.md
C:\DEV\Narrative\narrative-character-canon\.gitignore
C:\DEV\Narrative\narrative-character-canon\.gitattributes
```

`INVENTORY.md` — важный контрольный файл. Содержит все tracked-файлы репозитория.

---

# 2. Voyage control layer

**Самый важный слой управления проектом.**

```text
C:\DEV\Narrative\narrative-character-canon\.voyage\
```

Основные файлы:

```text
.voyage\CHARACTER_REGISTRY.md      — статусы персонажей и пар
.voyage\CURRENT_TASK.md            — текущая/последняя задача
.voyage\DECISIONS.md               — архитектурные решения
.voyage\CONTEXT_SNAPSHOT.md        — актуальный снимок памяти
.voyage\STATE_EXPORT.json          — экспорт SQLite/state
.voyage\EVENTS_EXPORT.jsonl        — журнал событий
.voyage\SQLITE_MEMORY_STATUS.md    — статистика memory DB
.voyage\PROJECT_STATE.md           — состояние проекта
.voyage\SCENE_REQUEST_RULES.md     — правила REQUEST vs EXAMPLE
.voyage\LOCATION_REGISTRY.md       — локации, если используется
```

**Правило:** Перед любым действием проверить `CURRENT_TASK.md` и `PROJECT_STATE.md`.

---

# 3. Основные docs / plans / architecture

Папка:

```text
C:\DEV\Narrative\narrative-character-canon\docs\
```

Существующие:

```text
docs\GITHUB_REFERENCE_PACK_WORKFLOW.md
docs\VOYAGE_INTEGRATION_WORKFLOW.md
docs\NCC_DEPLOY_CHECKLIST.md              ← создан 2026-07-09 (D-010 fix)
docs\NCC_FOLDER_MAP.md
docs\NCC_VISUAL_CANON_WORKFLOW.md        ← создан 2026-07-12 (D-017)
```

Планируемые:

```text
docs\SCENE_WORKFLOW_DUAL_BACKEND_ARCHITECTURE_DRAFT.md
docs\PROJECT_DOCUMENTATION_INDEX.md       ← этот файл
```

---

# 4. Tools / automation

Папка:

```text
C:\DEV\Narrative\narrative-character-canon\tools\
```

Текущие инструменты:

```text
tools\build_scene_reference_pack.py           — сборщик reference pack / SFW prompt
tools\validate_visual_canon_pipeline.py       — read-only валидатор visual-canon pipeline (MVP)
tools\generate_inventory.py                   — регенерация INVENTORY.md
tools\voyage_memory_init.py                   — init SQLite memory
tools\voyage_memory_status.py                 — статус SQLite memory
tools\voyage_memory_record.py                 — запись task/decision/event/artifacts
tools\voyage_memory_export.py                 — экспорт .voyage STATE/EVENTS/CONTEXT
```

Планируемые:

```text
tools\scene_workflow\build_scene_workflow.py
tools\scene_workflow\character_loader.py
tools\scene_workflow\preset_resolver.py
tools\scene_workflow\prompt_renderer_safe.py
tools\scene_workflow\prompt_renderer_adult_local.py
tools\scene_workflow\comfyui_workflow_builder.py
tools\scene_workflow\vscno.py
tools\scene_workflow\policy_gate.py
```

---

# 5. configs

## 5.1. Созданные configs/visual_canon

Папка:

```text
C:\DEV\Narrative\narrative-character-canon\configs\visual_canon\
```

Файлы:

```text
configs\visual_canon\pipeline_policy.json
configs\visual_canon\prompt_record.schema.json
configs\visual_canon\character_manifest.schema.json
```

Назначение:

* `pipeline_policy.json` — машиночитаемая политика: ID, вердикты, роли, storage/content tiers, human gates, concurrency.
* `prompt_record.schema.json` — JSON Schema для JSONL-реестра попыток (одна запись на `prompt_id`).
* `character_manifest.schema.json` — JSON Schema для durable per-character pipeline manifest.

Источник: `D-017` — adoption of universal authority hierarchy and schemas.

## 5.2. Планируемые configs/scene_workflow

Папка (ещё не создана):

```text
C:\DEV\Narrative\narrative-character-canon\configs\scene_workflow\
```

Планируемые файлы:

```text
configs\scene_workflow\backend_profiles.json
configs\scene_workflow\content_policy.json
configs\scene_workflow\vscno_lighting_map.json
configs\scene_workflow\comfyui_templates\
```

Критически важный файл:

```text
configs\scene_workflow\content_policy.json
```

Машиночитаемая политика (не парсинг IDENTITY.txt):

```json
{
  "character_age_rating": {
    "ANDREY": "adult_confirmed",
    "KIRA": "adult_confirmed",
    "OLGA": "adult_confirmed",
    "ANDREY_JUNIOR": "youthful_blocked_for_adult_local"
  }
}
```

---

# 6. Local storage / SQLite / generated scene packs

Локальное хранилище вне Git:

```text
C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\
```

SQLite memory:

```text
C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\voyage_memory\narrative_character_canon.sqlite
```

Планируемые scene outputs:

```text
C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\scene_packs\<SCENE_ID>\
```

Output-файлы для нового workflow:

```text
SCENE_REQUEST.json
SCENE_REFERENCE_PACK.md
SCENE_SAFE_PROMPT.txt
SCENE_ADULT_LOCAL_PROMPT.txt
SCENE_NEGATIVE_PROMPT.txt
SCENE_COMFYUI_WORKFLOW_DRAFT.json
SCENE_PARAMETERS.json
SCENE_VOYAGE_STATE.json
```

---

# 7. Character documentation — OLGA

```text
AI_CHARACTERS\OLGA\10_notes\OLGA_IDENTITY_DRAFT.md
AI_CHARACTERS\OLGA\10_notes\OLGA_CANON_INDEX.md
AI_CHARACTERS\OLGA\10_notes\OLGA_TEST_RESULTS.md
AI_CHARACTERS\OLGA\10_notes\OLGA_REFERENCE_PRESETS.json
```

Prompt pipeline:

```text
AI_CHARACTERS\OLGA\06_prompts\OLGA_CANON_GENERATION_PROMPTS.txt
AI_CHARACTERS\OLGA\06_prompts\OLGA_PROMPT_INDEX.md
AI_CHARACTERS\OLGA\06_prompts\OLGA_WORKING_SCENE_PROMPTS.md
AI_CHARACTERS\OLGA\06_prompts\OLGA_PROMPT_RUN_LOG.jsonl
AI_CHARACTERS\OLGA\06_prompts\OLGA_POOL_SCENE_PROMPT.md         ← добавлен 2026-07-09
```

Статус:

```text
OLGA = BASE_CANON_APPROVED / CONTROL_TESTS_APPROVED_LOCALLY / PROMPT_PIPELINE_ACTIVE
```

---

# 8. Character documentation — ANDREY_JUNIOR

```text
AI_CHARACTERS\ANDREY_JUNIOR\10_notes\ANDREY_JUNIOR_IDENTITY_DRAFT.md
AI_CHARACTERS\ANDREY_JUNIOR\10_notes\ANDREY_JUNIOR_CANON_INDEX.md
AI_CHARACTERS\ANDREY_JUNIOR\10_notes\ANDREY_JUNIOR_TEST_RESULTS.md
AI_CHARACTERS\ANDREY_JUNIOR\10_notes\ANDREY_JUNIOR_REFERENCE_PRESETS.json
```

Prompt pipeline:

```text
AI_CHARACTERS\ANDREY_JUNIOR\06_prompts\ANDREY_JUNIOR_CANON_GENERATION_PROMPTS.txt
AI_CHARACTERS\ANDREY_JUNIOR\06_prompts\ANDREY_JUNIOR_PROMPT_INDEX.md
AI_CHARACTERS\ANDREY_JUNIOR\06_prompts\ANDREY_JUNIOR_WORKING_SCENE_PROMPTS.md
AI_CHARACTERS\ANDREY_JUNIOR\06_prompts\ANDREY_JUNIOR_PROMPT_RUN_LOG.jsonl
```

Статус:

```text
ANDREY_JUNIOR = BASE_CANON_APPROVED / CONTROL_TESTS_APPROVED / PROMPT_PIPELINE_ACTIVE
```

**Важно:** blocked для adult_local (public_filtered only).

---

# 9. Character documentation — ANDREY Senior

```text
AI_CHARACTERS\ANDREY\10_notes\ANDREY_IDENTITY.txt
AI_CHARACTERS\ANDREY\10_notes\ANDREY_CANON_INDEX.md
AI_CHARACTERS\ANDREY\10_notes\ANDREY_TEST_RESULTS.md
AI_CHARACTERS\ANDREY\10_notes\ANDREY_REFERENCE_PRESETS.json
AI_CHARACTERS\ANDREY\10_notes\ANDREY_CANON_APPROVAL_WORKSHEET.md    ← добавлен 2026-07-09
```

Prompt pipeline:

```text
AI_CHARACTERS\ANDREY\06_prompts\ANDREY_PROMPT_INDEX.md
AI_CHARACTERS\ANDREY\06_prompts\ANDREY_WORKING_SCENE_PROMPTS.md
AI_CHARACTERS\ANDREY\06_prompts\ANDREY_PROMPT_RUN_LOG.jsonl
```

Старые prompt kit файлы:

```text
AI_CHARACTERS\ANDREY\06_prompts\ANDREY_FACE_CANON_PROMPT.txt
AI_CHARACTERS\ANDREY\06_prompts\ANDREY_FACE_CANON_NEGATIVE_PROMPT.txt
AI_CHARACTERS\ANDREY\06_prompts\ANDREY_BODY_CANON_PROMPT.txt
AI_CHARACTERS\ANDREY\06_prompts\ANDREY_BODY_CANON_NEGATIVE_PROMPT.txt
AI_CHARACTERS\ANDREY\06_prompts\ANDREY_CONTROL_TEST_PROMPTS.txt
AI_CHARACTERS\ANDREY\06_prompts\ANDREY_KIRA_JOINT_CONTROL_TEST_PROMPTS.txt
```

Статус:

```text
ANDREY = CANON_READY_2D / PROMPT_PIPELINE_ACTIVE
```

---

# 10. Character documentation — KIRA

Legacy docs:

```text
AI_CHARACTERS\KIRA\10_notes\KIRA_IDENTITY.txt.txt
AI_CHARACTERS\KIRA\10_notes\KIRA_CANON_INDEX.md.txt
AI_CHARACTERS\KIRA\10_notes\KIRA_TEST_RESULTS.md.txt
AI_CHARACTERS\KIRA\10_notes\KIRA_REFERENCE_PRESETS.json
AI_CHARACTERS\KIRA\10_notes\KIRA_APPROVAL_CRITERIA.md.txt
AI_CHARACTERS\KIRA\10_notes\KIRA_APPROVAL_CRITERIA_ENG.md.txt
AI_CHARACTERS\KIRA\10_notes\KIRA_CANON_APPROVAL_WORKSHEET.md    ← добавлен 2026-07-09
```

Prompt pipeline:

```text
AI_CHARACTERS\KIRA\06_prompts\KIRA_PROMPT_INDEX.md
AI_CHARACTERS\KIRA\06_prompts\KIRA_WORKING_SCENE_PROMPTS.md
AI_CHARACTERS\KIRA\06_prompts\KIRA_PROMPT_RUN_LOG.jsonl
AI_CHARACTERS\KIRA\06_prompts\KIRA_BASE_PROMPT.txt
AI_CHARACTERS\KIRA\06_prompts\KIRA_EVENING_SCENE_PROMPT.txt
AI_CHARACTERS\KIRA\06_prompts\KIRA_SPORTS_SCENE_PROMPT.txt
AI_CHARACTERS\KIRA\06_prompts\KIRA_NEGATIVE_PROMPT.txt
```

Статус:

```text
KIRA = CANON_READY_2D / PROMPT_PIPELINE_ACTIVE_CORE
```

Legacy cleanup отложен:

```text
.md.txt rename       — deferred
.txt.txt rename      — deferred
_MAIN/_ALT/_FINAL    — deferred
```

---

# 11. Group C — EMPTY_STRUCTURE → TEXT_CANON_READY

Персонажи: EGOR, MAKSIM, MARINA, NIKA, SERGEY

Структура папок создана (10 subfolders each).

Создано 2026-07-09:

```text
AI_CHARACTERS\<CHAR>\10_notes\<CHAR>_REFERENCE_PRESETS.json
AI_CHARACTERS\<CHAR>\06_prompts\<CHAR>_CANON_GENERATION_PROMPTS.txt
```

Статус:

```text
EGOR    = TEXT_CANON_READY / CANON_PROMPTS_CREATED
MAKSIM  = TEXT_CANON_READY / CANON_PROMPTS_CREATED
MARINA  = TEXT_CANON_READY / CANON_PROMPTS_CREATED
NIKA    = TEXT_CANON_READY / CANON_PROMPTS_CREATED
SERGEY  = TEXT_CANON_READY / CANON_PROMPTS_CREATED
```

**Не создано (deferred):**

```text
<CHAR>_IDENTITY.txt
<CHAR>_CANON_INDEX.md
<CHAR>_TEST_RESULTS.md
```

---

# 12. Joint scenes — KIRA_ANDREY

Папка:

```text
AI_CHARACTERS\_JOINT_SCENES\KIRA_ANDREY\
```

Вероятные подпапки:

```text
01_evening_embankment_walk
02_warm_bar_dialogue
03_yacht_sunset
04_studio_character_poster
05_rainy_city_street
06_cozy_interior_conversation
```

Планируемый joint prompt pipeline:

```text
AI_CHARACTERS\_JOINT_SCENES\KIRA_ANDREY\06_prompts\KIRA_ANDREY_PROMPT_INDEX.md
AI_CHARACTERS\_JOINT_SCENES\KIRA_ANDREY\06_prompts\KIRA_ANDREY_WORKING_SCENE_PROMPTS.md
AI_CHARACTERS\_JOINT_SCENES\KIRA_ANDREY\06_prompts\KIRA_ANDREY_PROMPT_RUN_LOG.jsonl
```

**Статус:** JOINT_CONTROL_TESTS_APPROVED / DUO_SCENE_PACKS_APPROVED

---

# 13. Prompt pipeline — структура правил

У каждого закрытого персонажа есть локальный набор правил:

```text
AI_CHARACTERS\<CHAR>\06_prompts\<CHAR>_PROMPT_INDEX.md
```

Хранят:

```text
prompt_id rules
source honesty rules (exact vs reconstructed vs unknown)
reference map rules
output_path mapping
future generation logging rules
```

---

# 14. Что пока НЕ закрыто

```text
KIRA_ANDREY joint prompt pipeline        — ещё нужен audit/backfill
folder schema normalization              — отложено
_APPROVED naming normalization            — отложено
KIRA .md.txt / .txt.txt cleanup           — отложено
ANDREY stale empty folders cleanup        — отложено
configs/scene_workflow/                   — ещё не создано
tools/scene_workflow/                     — ещё не реализовано
content_policy.json                       — ещё не создан
vscno_lighting_map.json                   — ещё не создан
ComfyUI workflow builder                  — ещё не реализован
Group C IDENTITY.txt / CANON_INDEX.md     — deferred
```

---

# 15. Локальное хранилище — user-managed

```text
C:\DEV\Narrative\ФОТО\
├── Ольга\          (20+ файлов)
├── Кира\           (18 файлов)
├── Марина\         (20 файлов)
├── Ника\           (18 файлов)
├── Егор\           (2 файла)
├── Максим\         (1 файл)
├── Сергей\         (2 файла)
├── Андрей младший\
└── Андрей старший\
```

**Правило:** User manages local files. NCC repo tracks only approved canon.

---

# 16. Критические правила проекта

1. **10-subfolder structure** внутри каждого персонажа (01_refs_raw → 10_notes)
2. **НИКОГДА** не создавать папок на уровне `AI_CHARACTERS/` (только внутри персонажа)
3. **prompt_id обязателен** для каждого APPROVED изображения
4. **PROMPT_RUN_LOG.jsonl** — machine-readable log для каждого персонажа
5. **CHARACTER_REGISTRY.md** — обновлять при смене статуса
6. **DECISIONS.md** — фиксировать каждое архитектурное решение
7. **INVENTORY.md** — обновлять при изменениях (backup first)
8. **ANDREY_JUNIOR** — blocked для adult_local, public_filtered only
9. **LOCAL_STORAGE** — вне Git, user-managed
10. **APPROVED naming:** `<CHAR>_test<NN>_<scene>_v<version>_APPROVED.png`

---

# 17. Быстрые ссылки

| Что нужно | Где искать |
|-----------|-----------|
| Статусы персонажей | `.voyage/CHARACTER_REGISTRY.md` |
| Текущая задача | `.voyage/CURRENT_TASK.md` |
| Архитектурные решения | `.voyage/DECISIONS.md` |
| Универсальный pipeline | `docs/NCC_VISUAL_CANON_WORKFLOW.md` |
| Машиночитаемая политика | `configs/visual_canon/pipeline_policy.json` |
| Правила деплоя | `docs/NCC_DEPLOY_CHECKLIST.md` |
| Структура папок | Этот файл (раздел 1, 7–12) |
| Prompt pipeline | `AI_CHARACTERS/<CHAR>/06_prompts/` |
| Canon refs | `AI_CHARACTERS/<CHAR>/03_face_sheet/`, `04_body_sheet/` |
| Local photos | `C:\DEV\Narrative\ФОТО\<Character>\` |

---

# 18. Prompt для Kimi Code: полный аудит

```text
NCC-PROJECT-DOCUMENTATION-INDEX-AUDIT

Repository:
C:\DEV\Narrative\narrative-character-canon

Mode:
READ-ONLY DOCUMENTATION INVENTORY AUDIT.
Do not create, edit, rename, move, delete, stage, commit, or push files.
Do not modify images.
Do not modify SQLite DB.
Do not modify .voyage.
Do not modify INVENTORY.md.
Do not stage `.vscode/`.

Goal:
Find and list all documentation, planning, contract, rule, policy, prompt-pipeline, Voyage, and architecture files in the narrative-character-canon project.

Start checks:
1. cd C:\DEV\Narrative\narrative-character-canon
2. Print:
   - git status --short
   - git branch --show-current
   - git rev-parse HEAD
   - git rev-parse origin/main
   - git log --oneline -10

Expected:
- branch main
- HEAD == origin/main
- working tree clean except untracked `.vscode/`

Audit these areas:
1. Root docs:
   - *.md
   - *.txt
   - *.json
   - INVENTORY.md

2. docs/
   - all markdown/json/txt files
   - workflow docs
   - architecture docs
   - contracts
   - plans

3. .voyage/
   - all markdown/json/jsonl/txt files
   - registry
   - current task
   - decisions
   - rules
   - exports
   - state files

4. tools/
   - Python tools
   - scripts
   - tool docs if present

5. configs/
   - if exists, list all files
   - if not exists, report missing/planned

6. AI_CHARACTERS/*/10_notes/
   - identity files
   - canon indexes
   - test results
   - reference presets
   - approval criteria
   - raw file maps
   - any docs

7. AI_CHARACTERS/*/06_prompts/
   - prompt indexes
   - working scene prompts
   - prompt run logs
   - generation prompt kits
   - negative prompt kits
   - scripts

8. AI_CHARACTERS/_JOINT_SCENES/
   - joint notes
   - joint prompts
   - joint indexes
   - approved scene docs
   - prompt logs if present

9. LOCAL_STORAGE references
   - do not scan external LOCAL_STORAGE unless inside repo
   - report documented LOCAL_STORAGE paths from docs/tools

For every file found, produce table:

| Category | Path | Type | Purpose | Status |
|---|---|---|---|---|

Status values:
- ACTIVE
- LEGACY
- GENERATED_EXPORT
- PROMPT_PIPELINE
- RULE
- PLAN
- CONTRACT
- DRAFT
- UNKNOWN_NEEDS_REVIEW

Also produce:
1. Top 20 most important control documents
2. Missing planned documents
3. Duplicates / stale docs
4. Deferred cleanup docs
5. Recommended master index file path:
   docs/PROJECT_DOCUMENTATION_INDEX.md

Final report format:

=== NCC-PROJECT-DOCUMENTATION-INDEX-AUDIT RESULT ===

1. Git status before
2. Documentation categories found
3. Root docs
4. docs/
5. .voyage/
6. tools/
7. configs/
8. Character notes files
9. Character prompt pipeline files
10. Joint scene docs
11. Local storage references
12. Top 20 control documents
13. Missing planned documents
14. Stale/legacy/duplicate docs
15. Recommended next WRITE step
16. Git status after

Important:
Read-only only. No writes. No commit. No push.
```

---

*PROJECT_DOCUMENTATION_INDEX | narrative-character-canon | 2026-07-12*
