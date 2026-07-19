# CHARACTER_REGISTRY

| Character | Folder | Current status | Reference preset status | Next step |
|---|---|---|---|---|
| ANDREY | `AI_CHARACTERS/ANDREY` | CANON_READY_2D / PROMPT_PIPELINE_ACTIVE | WORKING / FACE + BODY + CONTROL TESTS + PROMPT PIPELINE INCLUDED | Backfill KIRA prompt pipeline, then prepare ANDREY_3D_REFERENCE_PACK when requested |
| KIRA | `AI_CHARACTERS/KIRA` | CANON_READY_2D / PROMPT_PIPELINE_ACTIVE_CORE | WORKING — 7 scene presets + core prompt pipeline (6 active prompt IDs), verified 2026-07-07 | Backfill KIRA_ANDREY joint prompt pipeline, then prepare 3D reference pack when requested |
| KIRA + ANDREY | `AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY` | JOINT_CONTROL_TESTS_APPROVED / DUO_SCENE_PACKS_APPROVED | WORKING — 4 approved joint tests, 6 approved scene packs, reference preset ready | Next: additional duo scene packs / body-wardrobe-context refs / 3D reference packs |
| ANDREY_JUNIOR | `AI_CHARACTERS/ANDREY_JUNIOR` | BASE_CANON_APPROVED / CONTROL_TESTS_APPROVED / PROMPT_PIPELINE_ACTIVE | son of ANDREY Senior, short compact build, about 47 kg, son-version active, prompt pipeline active | Continue controlled scene testing with prompt_id logging |
| MARINA | `AI_CHARACTERS/MARINA` | BASE_CANON_APPROVED / CONTROL_TESTS_APPROVED / PROMPT_PIPELINE_ACTIVE | WORKING — 3 base-canon images + 7 approved control tests, support expressions/outfits and non-empty scene presets published | Await human selection of the next character or missing coverage target |
| NIKA | `AI_CHARACTERS/NIKA` | TEXT_CANON_READY / CANON_PROMPTS_CREATED | IDENTITY_SUMMARY + CANON_GENERATION_PROMPTS created, no images yet | Generate face canon + body canon via DALL-E or RunPod; base canon must stay tasteful/non-explicit per ROADMAP Priority 4 |
| SERGEY | `AI_CHARACTERS/SERGEY` | TEXT_CANON_READY / CANON_PROMPTS_CREATED | IDENTITY_SUMMARY + CANON_GENERATION_PROMPTS created, no images yet | Generate face canon + body canon via DALL-E or RunPod; create control tests |
| MAKSIM | `AI_CHARACTERS/MAKSIM` | TEXT_CANON_READY / CANON_PROMPTS_CREATED | IDENTITY_SUMMARY + CANON_GENERATION_PROMPTS created, no images yet | Generate face canon + body canon via DALL-E or RunPod; create control tests |
| OLGA | `AI_CHARACTERS/OLGA` | BASE_CANON_APPROVED / CONTROL_TESTS_APPROVED (Tests 01–10 published) / PROMPT_PIPELINE_ACTIVE | WORKING — base canon + tests 01–10 published (incl. DALL-E embankment ALT, formal/elegant Test09, height scale check Test10), prompt pipeline active | Awaiting human selection of the next character/scene; Test10 published at b5556f8 |
| EGOR | `AI_CHARACTERS/EGOR` | TEXT_CANON_READY / CANON_PROMPTS_CREATED | IDENTITY_SUMMARY + CANON_GENERATION_PROMPTS created, no images yet | Generate face canon + body canon via DALL-E or RunPod; watch for drift into too-adult/muscular type per ROADMAP Priority 6 |

## Правило

Не отмечать персонажа как preset-ready, пока его `REFERENCE_PRESETS.json` не содержит непустой `scene_presets` со ссылками на реально существующие tracked-файлы. Статус в этой таблице должен сверяться с фактическим содержимым JSON, а не переноситься автоматически из старых отчётов (`AGENTS.md`, `ROADMAP.md`).

Статусы соответствуют определениям из [docs/VOYAGE_INTEGRATION_WORKFLOW.md](../docs/VOYAGE_INTEGRATION_WORKFLOW.md#6-статусы-персонажей).

All future character status changes and approved outputs must follow the universal pipeline in `docs/NCC_VISUAL_CANON_WORKFLOW.md` and be recorded with a `prompt_id` in `AI_CHARACTERS/<CHAR>/06_prompts/<CHAR>_PROMPT_RUN_LOG.jsonl`.

## Voyage SQLite memory

Enabled via local runtime DB and tracked exports.
Use `.voyage/CONTEXT_SNAPSHOT.md` for compact ChatGPT handoff.

Record command:
`tools/voyage_memory_record.py` is available for incremental memory updates.
