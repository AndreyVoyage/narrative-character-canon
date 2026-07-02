# CHARACTER_REGISTRY

| Character | Folder | Current status | Reference preset status | Next step |
|---|---|---|---|---|
| ANDREY | `AI_CHARACTERS/ANDREY` | CANON_READY_2D | WORKING / FACE + BODY + CONTROL TESTS INCLUDED | Prepare ANDREY_3D_REFERENCE_PACK when requested; KIRA + ANDREY joint tests pending |
| KIRA | `AI_CHARACTERS/KIRA` | CANON_READY_2D | WORKING — 7 scene presets (incl. `sauna`), verified 2026-07-02, all referenced files exist and text_sources resolve | Prepare 3D reference pack when requested |
| KIRA + ANDREY | `AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY` | JOINT_CONTROL_TESTS_APPROVED | WORKING — 4 approved joint tests, reference preset ready | Duo scene packs / 3D reference packs / SQLite memory |
| MARINA | `AI_CHARACTERS/MARINA` | EMPTY_STRUCTURE | PRESET_PLACEHOLDER — empty `scene_presets`, `text_sources` null | Audit actual refs before creating presets; create canon pack |
| NIKA | `AI_CHARACTERS/NIKA` | EMPTY_STRUCTURE | PRESET_PLACEHOLDER — empty `scene_presets`, `text_sources` null | Audit actual refs before creating presets; base canon must stay tasteful/non-explicit per ROADMAP Priority 4 |
| OLGA | `AI_CHARACTERS/OLGA` | EMPTY_STRUCTURE | PRESET_PLACEHOLDER — empty `scene_presets`, `text_sources` null | Audit actual refs before creating presets; create canon pack |
| SERGEY | `AI_CHARACTERS/SERGEY` | EMPTY_STRUCTURE | PRESET_PLACEHOLDER — empty `scene_presets`, `text_sources` null | Audit actual refs before creating presets; secondary character pack |
| MAKSIM | `AI_CHARACTERS/MAKSIM` | EMPTY_STRUCTURE | PRESET_PLACEHOLDER — empty `scene_presets`, `text_sources` null | Audit actual refs before creating presets; secondary character pack |
| EGOR | `AI_CHARACTERS/EGOR` | EMPTY_STRUCTURE | PRESET_PLACEHOLDER — empty `scene_presets`, `text_sources` null | Audit actual refs before creating presets; watch for drift into too-adult/muscular type per ROADMAP Priority 6 |

## Правило

Не отмечать персонажа как preset-ready, пока его `REFERENCE_PRESETS.json` не содержит непустой `scene_presets` со ссылками на реально существующие tracked-файлы. Статус в этой таблице должен сверяться с фактическим содержимым JSON, а не переноситься автоматически из старых отчётов (`AGENTS.md`, `ROADMAP.md`).

Статусы соответствуют определениям из [docs/VOYAGE_INTEGRATION_WORKFLOW.md](../docs/VOYAGE_INTEGRATION_WORKFLOW.md#6-статусы-персонажей).

## Voyage SQLite memory

Enabled via local runtime DB and tracked exports.
Use `.voyage/CONTEXT_SNAPSHOT.md` for compact ChatGPT handoff.
