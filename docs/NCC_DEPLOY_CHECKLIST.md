# NCC DEPLOY CHECKLIST

> **Назначение:** Контрольный список для любого деплоя файлов в `narrative-character-canon`.  
> **Источник правил:** `AGENTS.md` разделы 5–6, `VOYAGE_INTEGRATION_WORKFLOW.md`.  
> **Последнее обновление:** 2026-07-09 (после D-010 — agent folder discipline violation).  
> **Статус:** ACTIVE — обязателен к применению.

---

## 0. BEFORE YOU START — Read-Only Audit

**Никогда не начинай деплой без аудита.**

- [ ] Прочитать `AGENTS.md` раздел 5 — *File naming conventions*  
- [ ] Прочитать `AGENTS.md` раздел 6 — *Workflow instructions*  
- [ ] Прочитать `.voyage/VOYAGE_INTEGRATION_WORKFLOW.md` — *Статусы и фиксация решений*  
- [ ] Проверить `.voyage/CURRENT_TASK.md` — есть ли активная задача?  
- [ ] Проверить `.voyage/DECISIONS.md` — нет ли конфликтующих решений?

**Stop condition:** Если `CURRENT_TASK.md` запрещает редактировать целевые файлы — STOP.

---

## 1. TARGET VALIDATION

### 1.1 Папка существует?
- [ ] Выполнить `ls` на target папку
- [ ] Если папки нет — создать по шаблону `AI_CHARACTERS/<CHAR>/<SUBFOLDER>/`
- [ ] Если создаёшь новую папку — добавить `.gitkeep`

### 1.2 Правильный уровень?
- [ ] `10_notes/` — ТОЛЬКО внутри `AI_CHARACTERS/<CHAR>/`  
  ❌ **WRONG:** `AI_CHARACTERS/10_notes/`  
  ✅ **RIGHT:** `AI_CHARACTERS/OLGA/10_notes/`
- [ ] `06_prompts/` — ТОЛЬКО внутри `AI_CHARACTERS/<CHAR>/`
- [ ] `07_generated/` — ТОЛЬКО внутри `AI_CHARACTERS/<CHAR>/`
- [ ] **НИКОГДА** не создавать общие папки на уровне `AI_CHARACTERS/`

### 1.3 Naming convention?
- [ ] Файл начинается с `<CHARACTER>_` (uppercase)  
  Примеры: `OLGA_face_canon_v1_sheet_A_APPROVED.png`, `ANDREY_REFERENCE_PRESETS.json`
- [ ] Underscores, not spaces
- [ ] Status suffix если применимо: `_APPROVED`, `_MAIN`, `_ALT`, `_candidate`, `_FINAL`
- [ ] Для JSON: `<CHARACTER>_REFERENCE_PRESETS.json`
- [ ] Для generation prompts: `<CHARACTER>_CANON_GENERATION_PROMPTS.txt`
- [ ] Для markdown notes: `<CHARACTER>_<TYPE>.md`

---

## 2. BACKUP

- [ ] Если файл **существует** и будет перезаписан — создать backup  
  Pattern: `<FILENAME>.backup_YYYYMMDD_HHMMSS`
- [ ] Если файл **новый** — backup не нужен
- [ ] Никогда не удалять существующие файлы (только переименовывать в backup)

---

## 3. COPY / CREATE

- [ ] Скопировать файл в target папку
- [ ] Проверить что файл не пустой (`wc -c` > 0)
- [ ] Проверить что файл readable (`head -5`)
- [ ] Убедиться что путь не содержит `AI_CHARACTERS/10_notes/` (общая)

---

## 4. VOYAGE TRACKING — Обязательно!

### 4.1 CHARACTER_REGISTRY.md
- [ ] Если статус персонажа изменился — обновить `.voyage/CHARACTER_REGISTRY.md`
- [ ] Статусы по `VOYAGE_INTEGRATION_WORKFLOW.md`:
  - `EMPTY_STRUCTURE` → `RAW_BASED` → `TEXT_CANON_READY` → `FACE_CANON_ACTIVE` → `BODY_PENDING` → `CANON_READY_2D`
- [ ] Не отмечать `preset-ready` пока `scene_presets` не содержит реальные tracked-файлы

### 4.2 DECISIONS.md
- [ ] Создать запись `D-XXX` с:
  - Дата
  - Decision ID
  - Context
  - Decision
  - Affected files
  - Reason
  - Next action

### 4.3 INVENTORY.md
- [ ] Backup: `cp INVENTORY.md INVENTORY.md.backup_YYYYMMDD_HHMMSS`
- [ ] Добавить новые файлы в таблицу
- [ ] Удалить записи о удалённых файлах

---

## 5. GIT

- [ ] `git status` — проверить что изменения корректны
- [ ] `git add` — только нужные файлы
- [ ] `git diff --cached` — финальная проверка
- [ ] `git commit` с детальным сообщением:
  ```
  <TYPE>: <summary>
  
  - What changed
  - Why
  - Affected characters/files
  - Refs: D-XXX
  ```
- [ ] `git push origin main`
- [ ] Если push failed — STOP, не делать force push

---

## 6. POST-DEPLOY VERIFICATION

- [ ] Проверить что файлы на GitHub (remote) совпадают с local
- [ ] Проверить что `CHARACTER_REGISTRY.md` актуален
- [ ] Проверить что `DECISIONS.md` содержит запись
- [ ] Проверить что `INVENTORY.md` содержит новые записи
- [ ] Если деплойил Kimi Code — проверить его report

---

## 7. COMMON MISTAKES — DO NOT REPEAT

| Mistake | From | Lesson |
|---------|------|--------|
| `AI_CHARACTERS/10_notes/` created | D-010 | `10_notes/` is per-character ONLY |
| Group-level naming | D-010 | Use `[CHAR]_TYPE.ext`, not `GROUP_*` |
| No CHARACTER_REGISTRY update | D-010 | Always update registry on status change |
| No DECISIONS entry | D-010 | Every deploy needs D-XXX |
| No INVENTORY update | D-010 | Inventory must reflect actual state |
| Overwrite without backup | — | Always backup existing files |

---

## 8. QUICK REFERENCE — NCC Folder Structure

```
AI_CHARACTERS/<CHAR>/
├── 01_refs_raw/           # Raw downloaded/generated images
├── 02_best_refs/          # Approved best references
├── 03_face_sheet/         # Face canon + expressions/
├── 04_body_sheet/         # Body canon + candidates/
├── 05_outfits/            # casual, formal, evening_dress, sports_look, scene_outfits, candidates
├── 06_prompts/            # Prompt kits, generation prompts, negative prompts
├── 07_generated/          # canon_tests/, drafts/, rejected/
├── 08_masks/              # Segmentation masks
├── 09_blender/            # Blender files, 3D reference packs
└── 10_notes/              # Canon index, identity, test results, reference presets JSON
```

**Remember:** Each folder above lives INSIDE the character folder. Never at `AI_CHARACTERS/` level.

---

## 9. DECISION RECORD TEMPLATE

```markdown
Дата: YYYY-MM-DD
Decision ID: D-XXX
Context: <what happened>
Decision: <what was decided>
Affected files:
- `AI_CHARACTERS/...`
Reason: <why>
Result: <outcome>
Next action: <what to do next>
```

---

*NCC Deploy Checklist | Based on D-010 lesson | Voyage Framework | 2026-07-09*
