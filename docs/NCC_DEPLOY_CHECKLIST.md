# NCC DEPLOY CHECKLIST

> **Назначение:** Контрольный список для любого деплоя файлов в `narrative-character-canon`.  
> **Источник правил:** `AGENTS.md` разделы 5–6, `VOYAGE_INTEGRATION_WORKFLOW.md`, `docs/NCC_VISUAL_CANON_WORKFLOW.md`, `configs/visual_canon/pipeline_policy.json`.
> **Последнее обновление:** 2026-07-12 (после D-017 — universal visual-canon pipeline adoption).
> **Статус:** ACTIVE — обязателен к применению.

---

## 0. A — Before deploy-tool dry-run

**Никогда не начинай deploy без read-only аудита.**

- [ ] Прочитать `AGENTS.md`, `docs/NCC_VISUAL_CANON_WORKFLOW.md` и
  `configs/visual_canon/pipeline_policy.json`.
- [ ] Проверить `.voyage/CURRENT_TASK.md` и отсутствие конфликтующего human-authored решения.
- [ ] Убедиться, что prompt attempt уже зарегистрирован, сгенерирован, выбран и одобрен человеком.
- [ ] Убедиться, что prompt source, точный heading и Prompt Index entry уже существуют.
- [ ] Подготовить declarative request с exact source/destination, expected HEAD и SHA-256 всех targets.
- [ ] Проверить clean tracked tree и пустой Git index.

**Stop condition:** deploy tool не создаёт prompt/ID/record и не исправляет незавершённую подготовку.

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

## 2. B — Deploy-tool dry-run

- [ ] Run: `py -3 tools\deploy_visual_canon_result.py --request <external-request.json>`.
- [ ] Запустить tool без `--apply`; default mode обязан быть read-only.
- [ ] Проверить existing JSONL target record, prompt/index linkage, references и approval evidence.
- [ ] Проверить отсутствие destination collision и Git LFS attribute.
- [ ] Запустить full и character-scoped compatibility validator prechecks.
- [ ] Проверить deterministic plan: action, path, before state, planned change, validation status.
- [ ] Dry-run не должен изменять repo, Git index, Inventory, Voyage или SQLite.

---

## 3. C — Human approval to apply

- [ ] Human reviewer подтверждает exact dry-run plan.
- [ ] Request содержит `selected: true`, `human_approval: true`, approval evidence, exact source,
  exact destination, expected HEAD и target hashes.
- [ ] Apply разрешается только явным `--apply`; скрытых interactive defaults нет.

---

## 4. D — Deploy-tool apply

- [ ] After human approval run: `py -3 tools\deploy_visual_canon_result.py --request <external-request.json> --apply`.
- [ ] Tool повторяет все dry-run checks и rechecks HEAD/status/hashes непосредственно перед write.
- [ ] Source image копируется; source никогда не перемещается и не удаляется.
- [ ] Tool обновляет ровно одну existing JSONL record, Test Results, Presets и, только для
  `APPROVED_AS_CANON`, Canon Index.
- [ ] Prompt source, Working Prompt Volume и Prompt Index только валидируются и не редактируются.
- [ ] Temporary copies и recovery manifest находятся вне repo; post-validation failure запускает rollback.
- [ ] После apply запускаются character-scoped и full compatibility validators.
- [ ] Изменения остаются unstaged.

---

## 5. E — Human post-apply review

- [ ] Run `git status --short` and `git diff --check`; inspect `git diff` before any separate Inventory or staging task.
- [ ] Проверить `git status --short`, `git diff`, exact changed-file scope и validator output.
- [ ] Проверить новый binary, JSON/JSONL, UTF-8, references и LFS coverage.
- [ ] При неожиданном diff — STOP; deploy tool не исправляет scope через reset/clean.

---

## 6. F–J — Separate human-controlled tasks

### F. Separate inventory step

- [ ] Если Inventory требуется, отдельная approved задача создаёт backup и regenerates it.
- [ ] Inventory не является частью deploy-tool transaction.

### G. Separate staging and commit verification

- [ ] Human/controlled task stages exact files, verifies LFS pointer and cached diff, then commits.
- [ ] Deploy tool не выполняет `git add`, commit, amend, reset или clean.

### H. Separate push verification

- [ ] Отдельный read-only audit проверяет commit и выполняет только normal push после human approval.
- [ ] Deploy tool никогда не push/force-push.

### I. Separate Voyage closeout

- [ ] Human-authored task обновляет Voyage state после доказанного commit/push.
- [ ] Decisions остаются human-authored; deploy tool не меняет `.voyage/**`.

### J. Separate SQLite synchronization

- [ ] SQLite sync/export выполняется только отдельной approved задачей после publication.
- [ ] Deploy tool не читает и не пишет SQLite.

---

## 7. COMMON MISTAKES — DO NOT REPEAT

| Mistake | From | Lesson |
|---------|------|--------|
| `AI_CHARACTERS/10_notes/` created | D-010 | `10_notes/` is per-character ONLY |
| Group-level naming | D-010 | Use `[CHAR]_TYPE.ext`, not `GROUP_*` |
| No CHARACTER_REGISTRY update | D-010 | Always update registry on status change |
| No required human-authored DECISIONS entry | D-010 | Architectural decisions are recorded separately; deploy tool never writes them |
| No required Inventory update | D-010 | Refresh Inventory in a separate controlled step; deploy tool never writes it |
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

## 9. Pipeline-specific stop conditions

Stop and ask the human control room if:

- The operation is not authorized by `.voyage/CURRENT_TASK.md`.
- The validator reports errors.
- A canonical `prompt_id` would include a variant label.
- `MAIN` or `ALT` is required in the filename.
- A local-only path would be committed.
- `reference_paths` include untracked files or placeholders.

---

## 10. DECISION RECORD TEMPLATE

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
