# EGOR Prompt Index

## Status

PROMPT_PIPELINE_ACTIVE

## Purpose

This folder stores prompt templates, working scene prompts, and prompt run logs for EGOR generations.

## Prompt Files

- `EGOR_CANON_GENERATION_PROMPTS.txt` — original reusable generation prompt source (face, expressions, body, pose variations)
- `EGOR_WORKING_SCENE_PROMPTS.md` — normalized prompt sections and reconstructions
- `EGOR_PROMPT_RUN_LOG.jsonl` — machine-readable prompt run log
- `EGOR_PROMPT_INDEX.md` — this index

## Reference Map

| Letter | File | Role |
|---|---|---|
| A | `AI_CHARACTERS/EGOR/03_face_sheet/EGOR_face_canon_v1_sheet_A_APPROVED.png` | face canon |
| B | `AI_CHARACTERS/EGOR/04_body_sheet/EGOR_body_canon_v1_sheet_A_front_side_back_APPROVED.png` | body canon |
| C | `AI_CHARACTERS/EGOR/03_face_sheet/expressions/EGOR_expressions_v1_sheet_A_APPROVED.png` | expression canon |
| D | `AI_CHARACTERS/EGOR/01_refs_raw/EGOR_RAW_02_face_bar_burgundy.jpg` | primary face ref |

## Active Core Prompt IDs

| Prompt ID | Target | Status | Source | Output |
|---|---|---|---|---|
| `EGOR_FACE_CANON_V1` | face canon sheet A | APPROVED | `exact_user_visible_prompt` | `AI_CHARACTERS/EGOR/03_face_sheet/EGOR_face_canon_v1_sheet_A_APPROVED.png` |
| `EGOR_EXPRESSIONS_V1` | expression sheet A | APPROVED | `exact_user_visible_prompt` | `AI_CHARACTERS/EGOR/03_face_sheet/expressions/EGOR_expressions_v1_sheet_A_APPROVED.png` |
| `EGOR_BODY_CANON_V1` | body canon sheet A | APPROVED | `exact_user_visible_prompt` | `AI_CHARACTERS/EGOR/04_body_sheet/EGOR_body_canon_v1_sheet_A_front_side_back_APPROVED.png` |

## Approved Control Tests

| Prompt ID | Test | Scene | Verdict | Role | Output |
|---:|---|---|---|---|---|
| `EGOR_TEST01_NEUTRAL_PORTRAIT_V1` | 01 | neutral_portrait | APPROVED | MAIN | `AI_CHARACTERS/EGOR/07_generated/canon_tests/03_portrait_expression/EGOR_test01_neutral_portrait_v1_APPROVED.png` |
| `EGOR_TEST02_EVENING_EMBANKMENT_V1` | 02 | evening_embankment | APPROVED | MAIN | `AI_CHARACTERS/EGOR/07_generated/canon_tests/01_evening_embankment/EGOR_test02_evening_embankment_v1_APPROVED.png` |
| `EGOR_TEST03_SPORTS_YOGA_V1` | 03 | sports_yoga | APPROVED | MAIN | `AI_CHARACTERS/EGOR/07_generated/canon_tests/02_sports_yoga/EGOR_test03_sports_yoga_v1_APPROVED.png` |