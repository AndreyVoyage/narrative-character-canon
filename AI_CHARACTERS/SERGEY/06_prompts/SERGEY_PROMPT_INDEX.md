# SERGEY Prompt Index

## Status

PROMPT_PIPELINE_ACTIVE

## Purpose

This folder stores prompt templates, working scene prompts, and prompt run logs for SERGEY generations.

## Prompt Files

- `SERGEY_CANON_GENERATION_PROMPTS.txt` — original reusable generation prompt source (face, expressions, body, pose variations)
- `SERGEY_WORKING_SCENE_PROMPTS.md` — normalized prompt sections and reconstructions
- `SERGEY_PROMPT_RUN_LOG.jsonl` — machine-readable prompt run log
- `SERGEY_PROMPT_INDEX.md` — this index

## Reference Map

| Letter | File | Role |
|---|---|---|
| A | `AI_CHARACTERS/SERGEY/03_face_sheet/SERGEY_face_canon_v1_sheet_A_APPROVED.png` | face canon |
| B | `AI_CHARACTERS/SERGEY/04_body_sheet/SERGEY_body_canon_v1_sheet_A_front_side_back_APPROVED.png` | body canon |
| C | `AI_CHARACTERS/SERGEY/03_face_sheet/expressions/SERGEY_expressions_v1_sheet_A_APPROVED.png` | expression canon |
| D | `AI_CHARACTERS/SERGEY/04_body_sheet/SERGEY_body_canon_v1_sheet_B_pose_variations_APPROVED.png` | body canon B |
| E | `AI_CHARACTERS/SERGEY/01_refs_raw/SERGEY_RAW_01_face_main_bar.jpg` | primary face ref |
| F | `AI_CHARACTERS/SERGEY/01_refs_raw/SERGEY_RAW_02_body_main_navy_suit_multiview.png` | body main ref |

## Active Core Prompt IDs

| Prompt ID | Target | Status | Source | Output |
|---|---|---|---|---|
| `SERGEY_FACE_CANON_V1` | face canon sheet A | APPROVED | `SERGEY_CANON_GENERATION_PROMPTS.txt` | `AI_CHARACTERS/SERGEY/03_face_sheet/SERGEY_face_canon_v1_sheet_A_APPROVED.png` |
| `SERGEY_EXPRESSIONS_V1` | expression sheet A | APPROVED | `SERGEY_CANON_GENERATION_PROMPTS.txt` | `AI_CHARACTERS/SERGEY/03_face_sheet/expressions/SERGEY_expressions_v1_sheet_A_APPROVED.png` |
| `SERGEY_BODY_CANON_V1` | body canon sheet A | APPROVED_WITH_MINOR_NOTES | `SERGEY_CANON_GENERATION_PROMPTS.txt` | `AI_CHARACTERS/SERGEY/04_body_sheet/SERGEY_body_canon_v1_sheet_A_front_side_back_APPROVED.png` |
| `SERGEY_BODY_CANON_POSES_V1` | body canon sheet B | APPROVED_WITH_MINOR_NOTES | `SERGEY_CANON_GENERATION_PROMPTS.txt` | `AI_CHARACTERS/SERGEY/04_body_sheet/SERGEY_body_canon_v1_sheet_B_pose_variations_APPROVED.png` |

## Approved Control Tests

| Prompt ID | Test | Scene | Variant | Verdict | Role | Output |
|---:|---|---|---|---|---|---|
| `SERGEY_TEST01_NEUTRAL_PORTRAIT_V1` | 01 | neutral_portrait | MAIN | APPROVED_WITH_MINOR_NOTES | MAIN | `AI_CHARACTERS/SERGEY/07_generated/canon_tests/03_portrait_expression/SERGEY_test01_neutral_portrait_v1_APPROVED.png` |
| `SERGEY_TEST02_EVENING_EMBANKMENT_V1` | 02 | evening_embankment | MAIN | APPROVED_WITH_MINOR_NOTES | MAIN | `AI_CHARACTERS/SERGEY/07_generated/canon_tests/01_evening_embankment/SERGEY_test02_evening_embankment_v1_APPROVED.png` |
| `SERGEY_TEST03_SPORTS_YOGA_V1` | 03 | sports_yoga | MAIN | APPROVED_WITH_MINOR_NOTES | MAIN | `AI_CHARACTERS/SERGEY/07_generated/canon_tests/02_sports_yoga/SERGEY_test03_sports_yoga_v1_APPROVED.png` |