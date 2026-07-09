# NCC FOLDER MAP — Рабочие папки проекта

> **Статус:** ACTIVE | Единый источник правды для путей
> **Создан:** 2026-07-09
> **Правило:** При любом сомнении — открывать этот файл, не придумывать пути

---

## REPO ROOT (единственный)

```
C:\DEV\Narrative\narrative-character-canon\
```

Подпапки в корне:

```
AI_CHARACTERS\     ← персонажи (9 штук + _JOINT_SCENES)
docs\              ← документация проекта
tools\             ← скрипты Python/PowerShell
.voyage\           ← управление проектом (Voyage)
```

**НЕТ других папок в корне:**
- ❌ `LOCAL_STORAGE\` — это ВНЕ репо
- ❌ `10_notes\` — это ВНУТРИ каждого персонажа
- ❌ `06_prompts\` — это ВНУТРИ каждого персонажа

---

## AI_CHARACTERS (9 персонажей + joint)

```
AI_CHARACTERS\ANDREY\
AI_CHARACTERS\ANDREY_JUNIOR\
AI_CHARACTERS\EGOR\
AI_CHARACTERS\KIRA\
AI_CHARACTERS\MAKSIM\
AI_CHARACTERS\MARINA\
AI_CHARACTERS\NIKA\
AI_CHARACTERS\OLGA\
AI_CHARACTERS\SERGEY\
AI_CHARACTERS\_JOINT_SCENES\KIRA_ANDREY\
```

---

## Структура ВНУТРИ каждого персонажа (10 папок)

```
AI_CHARACTERS\<CHAR>\
├── 01_refs_raw\              ← сырые референсы
├── 02_best_refs\             ← лучшие референсы
├── 03_face_sheet\            ← face canon + expressions/
├── 04_body_sheet\            ← body canon + candidates/
├── 05_outfits\               ← casual, formal, evening_dress, sports_look, scene_outfits, candidates
├── 06_prompts\               ← prompt kits, generation prompts, run logs
├── 07_generated\             ← canon_tests/, drafts/, rejected/
├── 08_masks\                 ← маски для inpaint
├── 09_blender\               ← Blender, 3D reference packs
└── 10_notes\                 ← identity, canon index, test results, reference presets JSON
```

**Критическое правило:** `10_notes\` только ВНУТРИ персонажа. Никогда на уровне `AI_CHARACTERS\`.

---

## Локальное хранилище (вне Git, user-managed)

```
C:\DEV\Narrative\ФОТО\
├── Андрей младший\
├── Андрей старший\
├── Егор\
├── Кира\
├── Максим\
├── Марина\
├── Ника\
├── Ольга\
└── Сергей\
```

**Правило:** Я НЕ управляю этими папками. Пользователь сам решает куда сохранять. Я даю только `prompt_id` и `APPROVED/REJECTED`.

---

## Где что искать

| Что нужно | Где искать |
|-----------|-----------|
| Статусы персонажей | `.voyage/CHARACTER_REGISTRY.md` |
| Текущая задача | `.voyage/CURRENT_TASK.md` |
| Решения | `.voyage/DECISIONS.md` |
| Prompt pipeline | `AI_CHARACTERS/<CHAR>/06_prompts/` |
| Face canon | `AI_CHARACTERS/<CHAR>/03_face_sheet/` |
| Body canon | `AI_CHARACTERS/<CHAR>/04_body_sheet/` |
| Approved tests | `AI_CHARACTERS/<CHAR>/07_generated/canon_tests/` |
| Identity/presets | `AI_CHARACTERS/<CHAR>/10_notes/` |
| Локальные фото | `C:\DEV\Narrative\ФОТО\<Character>\` |
| Документация | `docs/` |
| Скрипты | `tools/` |

---

## Запрещено создавать

| Папка | Почему |
|-------|--------|
| `AI_CHARACTERS/10_notes/` | Должна быть внутри каждого персонажа |
| `AI_CHARACTERS/<CHAR>/07_generated/dalle_tests/` | Нет такой папки. Использовать `canon_tests/`, `drafts/`, `rejected/` |
| `LOCAL_STORAGE/narrative-character-canon/docs/` | LOCAL_STORAGE — вне репо, не создавать подпапки |
| Любые новые имена папок | Использовать только существующие из списка выше |

---

## Правила для AI-агента

1. **Перед предложением пути — открыть этот файл**
2. **Перед созданием файла — `ls` target папки**
3. **Никогда не придумывать имена папок**
4. **Никогда не создавать папки на уровне `AI_CHARACTERS/`**
5. **Локальные пути — user-managed, я только review**

---

*NCC FOLDER MAP | narrative-character-canon | 2026-07-09*
