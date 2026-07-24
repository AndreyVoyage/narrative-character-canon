# NIKA Prompt Index

## Status

PROMPT_PIPELINE_ACTIVE

## Purpose

This folder stores prompt templates, working scene prompts, and prompt run logs for NIKA generations.

## Prompt Files

- `NIKA_CANON_GENERATION_PROMPTS.txt` — original reusable generation prompt source (face, expressions, body, pose variations)
- `NIKA_WORKING_SCENE_PROMPTS.md` — normalized prompt sections and reconstructions
- `NIKA_PROMPT_RUN_LOG.jsonl` — machine-readable prompt run log
- `NIKA_PROMPT_INDEX.md` — this index

## Reference Map

| Letter | File | Role |
|---|---|---|
| A | `AI_CHARACTERS/NIKA/03_face_sheet/NIKA_face_canon_v1_sheet_A_APPROVED.png` | face canon |
| B | `AI_CHARACTERS/NIKA/04_body_sheet/NIKA_body_canon_v1_sheet_A_front_side_back_APPROVED.png` | body canon |
| C | `AI_CHARACTERS/NIKA/03_face_sheet/expressions/NIKA_expressions_v1_sheet_A_APPROVED.png` | expression canon |
| D | `AI_CHARACTERS/NIKA/01_refs_raw/NIKA_RAW_01_face_main_burgundy_expressions.png` | primary face ref |
| E | `AI_CHARACTERS/NIKA/01_refs_raw/NIKA_RAW_02_body_main_burgundy_multiview.png` | body main ref |
| F | `AI_CHARACTERS/NIKA/01_refs_raw/NIKA_RAW_04_style_main_burgundy_bar.png` | formal style main ref |
| G | `AI_CHARACTERS/NIKA/04_body_sheet/NIKA_body_canon_v1_sheet_B_pose_variations_APPROVED.png` | body canon B |

## Active Core Prompt IDs

| Prompt ID | Target | Status | Source | Output |
|---|---|---|---|---|
| `NIKA_FACE_CANON_V1` | face canon sheet A | APPROVED | `exact_user_visible_prompt` | `AI_CHARACTERS/NIKA/03_face_sheet/NIKA_face_canon_v1_sheet_A_APPROVED.png` |
| `NIKA_EXPRESSIONS_V1` | expression sheet A | APPROVED | `exact_user_visible_prompt` | `AI_CHARACTERS/NIKA/03_face_sheet/expressions/NIKA_expressions_v1_sheet_A_APPROVED.png` |
| `NIKA_BODY_CANON_V1` | body canon sheet A | APPROVED | `exact_user_visible_prompt` | `AI_CHARACTERS/NIKA/04_body_sheet/NIKA_body_canon_v1_sheet_A_front_side_back_APPROVED.png` |
| `NIKA_BODY_CANON_POSES_V1` | body canon sheet B | APPROVED | `exact_user_visible_prompt` | `AI_CHARACTERS/NIKA/04_body_sheet/NIKA_body_canon_v1_sheet_B_pose_variations_APPROVED.png` |

## Approved Control Tests

| Prompt ID | Test | Scene | Variant | Verdict | Role | Output |
|---:|---|---|---|---|---|---|
| `NIKA_TEST01_NEUTRAL_PORTRAIT_V1` | 01 | neutral_portrait | MAIN (v1) | APPROVED_WITH_MINOR_NOTES | MAIN | `AI_CHARACTERS/NIKA/07_generated/canon_tests/03_portrait_expression/NIKA_test01_neutral_portrait_v1_APPROVED.png` |
| `NIKA_TEST01_NEUTRAL_PORTRAIT_V1` | 01 | neutral_portrait | ALT (v2) | APPROVED_WITH_MINOR_NOTES | ALT | `AI_CHARACTERS/NIKA/07_generated/canon_tests/03_portrait_expression/NIKA_test01_neutral_portrait_v2_APPROVED.png` |
| `NIKA_TEST02_EVENING_EMBANKMENT_V1` | 02 | evening_embankment | MAIN | APPROVED_WITH_MINOR_NOTES | MAIN | `AI_CHARACTERS/NIKA/07_generated/canon_tests/01_evening_embankment/NIKA_test02_evening_embankment_v1_APPROVED.png` |
| `NIKA_TEST03_SPORTS_YOGA_V1` | 03 | sports_yoga | MAIN | APPROVED_WITH_MINOR_NOTES | MAIN | `AI_CHARACTERS/NIKA/07_generated/canon_tests/02_sports_yoga/NIKA_test03_sports_yoga_v1_APPROVED.png` |