# CURRENT_TASK

## Task ID
NCC-DALLE-17-GENERATION-2026-07-09

## Status
IN_PROGRESS

## Goal
Generate 17 DALL-E images across 8 characters (OLGA ×5, ANDREY ×4, KIRA ×3, EGOR/MAKSIM/MARINA/NIKA/SERGEY ×1 each). AJ excluded from public_filtered.

## Scope (what I can do)
1. Write generation prompts for DALL-E (ChatGPT)
2. Review generated images and give APPROVED/REJECTED verdict
3. Record prompt_id, output_path, reference_paths for APPROVED images
4. After all 17 images collected — write Kimi Code deploy prompt for NCC

## Forbidden Actions (CRITICAL)
1. **NEVER invent folder paths.** Before suggesting any path, run `ls` on target directory
2. **NEVER create new folder names** (like `dalle_tests/`). Use EXISTING subfolders only: `canon_tests/`, `drafts/`, `rejected/` under `07_generated/`
3. **NEVER suggest paths outside `07_generated/`** for generated images
4. **DO NOT** update `CHARACTER_REGISTRY.md` or `INVENTORY.md` during this task — deferred to final deploy step
5. **DO NOT** write files to NCC repo — only planning documents in workspace
6. **DO NOT** run git commands — deferred to final deploy

## Folder Structure (read-only, verified 2026-07-09)

```
AI_CHARACTERS/<CHAR>/07_generated/
├── canon_tests/     ← APPROVED images go here (with numbered subfolders)
├── drafts/          ← temporary / work-in-progress
└── rejected/        ← REJECTED images
```

**Naming convention for approved images:**
```
AI_CHARACTERS/<CHAR>/07_generated/canon_tests/<NN>_<scene_description>/
  <CHAR>_test<NN>_<scene>_v<version>[_APPROVED].png
```

## Local Storage (user-managed)
```
C:\DEV\Narrative\ФОТО\<Character in Russian>\
```
User manages local files. I only review and approve.

## Character Mapping (English → Russian folder)
| English | Russian Folder |
|---------|---------------|
| OLGA | Ольга |
| ANDREY | Андрей старший |
| KIRA | Кира |
| EGOR | Егор |
| MAKSIM | Максим |
| MARINA | Марина |
| NIKA | Ника |
| SERGEY | Сергей |

## Next Expected Report
After each image: user sends photo, I return DECISION_001 with APPROVED/REJECTED + prompt_id + notes.

## Forbid List
- No `dalle_tests/` folder creation
- No `AI_CHARACTERS/10_notes/` at character level
- No age numbers, no explicit content
- No git operations during generation phase

---
*Created: 2026-07-09*
*Task type: DALL-E generation + review*
*Framework: Voyage-lite*

## Progress Update — 2026-07-10

- Original 17-image DALL-E plan has been redesigned based on actual OLGA coverage.
- OLGA pool/wellness generation produced v1 (athleisure/public-safe), v2 (swimsuit-safe), and v3 (swimsuit canon) variants.
- Human decision: deploy only v1 athleisure/public-safe image to repo; keep v2/v3 local-only.
- Repo files updated: `OLGA_TEST_RESULTS.md`, `OLGA_PROMPT_RUN_LOG.jsonl`, `OLGA_WORKING_SCENE_PROMPTS.md`, `OLGA_REFERENCE_PRESETS.json`, `DECISIONS.md`, `CURRENT_TASK.md`, `INVENTORY.md`.
- Next generation should target remaining coverage gaps (formal/elegant, casual everyday, scale check, character poster) rather than follow the old blind 17-image list.
