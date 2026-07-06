# CHARACTER_REGISTRY

| Character | Folder | Current status | Reference preset status | Next step |
|---|---|---|---|---|
| ANDREY | `AI_CHARACTERS/ANDREY` | CANON_READY_2D / PROMPT_PIPELINE_ACTIVE | WORKING / FACE + BODY + CONTROL TESTS + PROMPT PIPELINE INCLUDED | Backfill KIRA prompt pipeline, then prepare ANDREY_3D_REFERENCE_PACK when requested |
| KIRA | `AI_CHARACTERS/KIRA` | CANON_READY_2D | WORKING — 7 scene presets (incl. `sauna`), verified 2026-07-02, all referenced files exist and text_sources resolve | Prepare 3D reference pack when requested |
| KIRA + ANDREY | `AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY` | JOINT_CONTROL_TESTS_APPROVED / DUO_SCENE_PACKS_APPROVED | WORKING — 4 approved joint tests, 6 approved scene packs, reference preset ready | Next: additional duo scene packs / body-wardrobe-context refs / 3D reference packs |
| ANDREY_JUNIOR | `AI_CHARACTERS/ANDREY_JUNIOR` | BASE_CANON_APPROVED / CONTROL_TESTS_APPROVED / PROMPT_PIPELINE_ACTIVE | son of ANDREY Senior, short compact build, about 47 kg, son-version active, prompt pipeline active | Continue controlled scene testing with prompt_id logging |
| MARINA | `AI_CHARACTERS/MARINA` | EMPTY_STRUCTURE | PRESET_PLACEHOLDER — empty `scene_presets`, `text_sources` null | Audit actual refs before creating presets; create canon pack |
| NIKA | `AI_CHARACTERS/NIKA` | EMPTY_STRUCTURE | PRESET_PLACEHOLDER — empty `scene_presets`, `text_sources` null | Audit actual refs before creating presets; base canon must stay tasteful/non-explicit per ROADMAP Priority 4 |
| SERGEY | `AI_CHARACTERS/SERGEY` | EMPTY_STRUCTURE | PRESET_PLACEHOLDER — empty `scene_presets`, `text_sources` null | Audit actual refs before creating presets; secondary character pack |
| MAKSIM | `AI_CHARACTERS/MAKSIM` | EMPTY_STRUCTURE | PRESET_PLACEHOLDER — empty `scene_presets`, `text_sources` null | Audit actual refs before creating presets; secondary character pack |
| OLGA | `AI_CHARACTERS/OLGA` | BASE_CANON_APPROVED / CONTROL_TESTS_APPROVED_LOCALLY | WORKING — base canon + tests 01–06, prompt pipeline active | Continue controlled scene testing with prompt_id logging |
| EGOR | `AI_CHARACTERS/EGOR` | EMPTY_STRUCTURE | PRESET_PLACEHOLDER — empty `scene_presets`, `text_sources` null | Audit actual refs before creating presets; watch for drift into too-adult/muscular type per ROADMAP Priority 6 |

## Правило

Не отмечать персонажа как preset-ready, пока его `REFERENCE_PRESETS.json` не содержит непустой `scene_presets` со ссылками на реально существующие tracked-файлы. Статус в этой таблице должен сверяться с фактическим содержимым JSON, а не переноситься автоматически из старых отчётов (`AGENTS.md`, `ROADMAP.md`).

Статусы соответствуют определениям из [docs/VOYAGE_INTEGRATION_WORKFLOW.md](../docs/VOYAGE_INTEGRATION_WORKFLOW.md#6-статусы-персонажей).

## Voyage SQLite memory

Enabled via local runtime DB and tracked exports.
Use `.voyage/CONTEXT_SNAPSHOT.md` for compact ChatGPT handoff.

Record command:
`tools/voyage_memory_record.py` is available for incremental memory updates.
