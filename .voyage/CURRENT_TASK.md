# CURRENT_TASK

## Just completed — NCC-KIRA-PRESET-AUDIT

Status: DONE (2026-07-02)

Goal was: verify and fix `KIRA_REFERENCE_PRESETS.json` before using KIRA in GitHub-first scene packs.

Result: file is already valid — all `text_sources` and all `reference_images` across 7 `scene_presets` resolve to existing tracked files. No fix required. See [DECISIONS.md#decision-0004](DECISIONS.md).

## Next — NCC-ANDREY-BODY-CANON

Status: NEXT (not started)

Goal: Create ANDREY body canon so ANDREY moves from FACE_CANON_ACTIVE/BODY_PENDING to CANON_READY_2D (per ROADMAP.md §9 "Immediate next actions").

Allowed files for next task:

* `AI_CHARACTERS/ANDREY/06_prompts/ANDREY_BODY_CANON_PROMPT.txt` (new)
* `AI_CHARACTERS/ANDREY/04_body_sheet/` (new generated sheets, once approved)
* `AI_CHARACTERS/ANDREY/10_notes/ANDREY_CANON_INDEX.md`
* `AI_CHARACTERS/ANDREY/10_notes/ANDREY_REFERENCE_PRESETS.json`

Optional docs to update after:

* `.voyage/PROJECT_STATE.md`
* `.voyage/CHARACTER_REGISTRY.md`
* `.voyage/DECISIONS.md`

Forbidden:

* do not generate the KIRA + ANDREY sauna scene — it is EXAMPLE, not REQUESTED (see [SCENE_REQUEST_RULES.md](SCENE_REQUEST_RULES.md))
* do not modify, rename, move, or delete existing images
* do not create fake refs or mark placeholders as complete
* do not edit `AGENTS.md`

Expected next report when this task is picked up:

* `ANDREY_BODY_CANON_PROMPT.txt` created or confirmed
* body canon sheets generated and reviewed (draft vs approved status noted)
* `ANDREY_CANON_INDEX.md` updated if body canon approved
* `ANDREY_REFERENCE_PRESETS.json` `body_canon` preset updated with new approved refs
* git status after
