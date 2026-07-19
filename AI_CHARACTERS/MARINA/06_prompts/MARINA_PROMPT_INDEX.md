# MARINA Prompt Index

## Status

PROMPT_PIPELINE_ACTIVE

## Purpose

This folder stores prompt templates, working scene prompts, and prompt run logs for MARINA generations.

## Prompt Files

- `MARINA_CANON_GENERATION_PROMPTS.txt` — original reusable generation prompt source (face, expressions, body, pose variations)
- `MARINA_WORKING_SCENE_PROMPTS.md` — normalized prompt sections and reconstructions
- `MARINA_PROMPT_RUN_LOG.jsonl` — machine-readable prompt run log
- `MARINA_PROMPT_INDEX.md` — this index

## Reference Map

| Letter | File | Role |
|---|---|---|
| A | `AI_CHARACTERS/MARINA/03_face_sheet/MARINA_face_canon_v1_sheet_A_APPROVED.png` | face canon |
| B | `AI_CHARACTERS/MARINA/04_body_sheet/MARINA_body_canon_v1_sheet_A_APPROVED.png` | body canon |
| C | `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_A_APPROVED.png` | expression canon |

## Active Core Prompt IDs

| Prompt ID | Target | Status | Source | Output |
|---|---|---|---|---|
| `MARINA_FACE_CANON_V1_A` | face canon sheet A | APPROVED | `unknown_requires_manual_input` | `AI_CHARACTERS/MARINA/03_face_sheet/MARINA_face_canon_v1_sheet_A_APPROVED.png` |
| `MARINA_EXPRESSIONS_V1_A` | expression sheet A | APPROVED | `unknown_requires_manual_input` | `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_A_APPROVED.png` |
| `MARINA_BODY_CANON_V1_A` | body canon sheet A | APPROVED | `unknown_requires_manual_input` | `AI_CHARACTERS/MARINA/04_body_sheet/MARINA_body_canon_v1_sheet_A_APPROVED.png` |

## Support Expression References

| Prompt ID | Target | Status | Source | Output |
|---|---|---|---|---|
| `MARINA_EXPRESSIONS_V1_B` | expression sheet B SUPPORT | APPROVED | `unknown_requires_manual_input` | `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_B_SUPPORT.png` |
| `MARINA_EXPRESSIONS_V1_C` | expression sheet C SUPPORT | APPROVED | `unknown_requires_manual_input` | `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_C_SUPPORT.png` |
| `MARINA_EXPRESSIONS_V1_D` | expression sheet D SUPPORT | APPROVED | `unknown_requires_manual_input` | `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_D_SUPPORT.png` |
| `MARINA_EXPRESSIONS_V1_E` | expression sheet E SUPPORT | APPROVED | `unknown_requires_manual_input` | `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_E_SUPPORT.png` |
| `MARINA_EXPRESSIONS_V1_F` | expression sheet F SUPPORT | APPROVED | `unknown_requires_manual_input` | `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_F_SUPPORT.png` |

## Outfit References

| Prompt ID | Target | Status | Source | Output |
|---|---|---|---|---|
| `MARINA_OUTFIT_EVENING_PEACH_V1_A` | evening peach dress sheet A MAIN | APPROVED | `unknown_requires_manual_input` | `AI_CHARACTERS/MARINA/05_outfits/MARINA_outfit_evening_peach_v1_sheet_A_APPROVED.png` |
| `MARINA_OUTFIT_EVENING_PEACH_V1_B` | evening peach portrait SUPPORT | APPROVED | `unknown_requires_manual_input` | `AI_CHARACTERS/MARINA/05_outfits/MARINA_outfit_evening_peach_v1_portrait_SUPPORT.png` |
| `MARINA_OUTFIT_WARM_EVENING_V1_A` | warm evening portrait SUPPORT | APPROVED | `unknown_requires_manual_input` | `AI_CHARACTERS/MARINA/05_outfits/MARINA_outfit_warm_evening_v1_portrait_SUPPORT.png` |

## Approved Control Tests

| Prompt ID | Test | Scene | Verdict | Role | Output |
|---|---:|---|---|---|---|
| `MARINA_TEST01_RAINY_CAFE_V1` | 01 | rainy_cafe | APPROVED_AS_TEST | MAIN | `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test01_rainy_cafe_v1_APPROVED.png` |
| `MARINA_TEST02_THEATER_MELANCHOLY_V1` | 02 | theater_melancholy | APPROVED_AS_TEST | MAIN | `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test02_theater_melancholy_v1_APPROVED.png` |
| `MARINA_TEST03_EVENING_CITY_BALCONY_V1` | 03 | evening_city_balcony | APPROVED_AS_TEST | MAIN | `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test03_evening_city_balcony_v1_APPROVED.png` |
| `MARINA_TEST04_AUTUMN_STREET_PORTRAIT_V1` | 04 | autumn_street_portrait | APPROVED_AS_TEST | MAIN | `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test04_autumn_street_portrait_v1_APPROVED.png` |
| `MARINA_TEST05_MORNING_PAJAMAS_V1` | 05 | morning_pajamas | APPROVED_AS_TEST | MAIN | `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test05_morning_pajamas_v1_APPROVED.png` |
| `MARINA_TEST06_WHITE_GARDEN_FORMAL_V1` | 06 | white_garden_formal | APPROVED_AS_TEST | MAIN | `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test06_white_garden_formal_v1_APPROVED.png` |
| `MARINA_TEST07_POOL_SUNSET_V1` | 07 | pool_sunset | APPROVED_AS_TEST | MAIN | `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test07_pool_sunset_v1_APPROVED.png` |

## Known Deferred Issues

- Exact per-image generation prompts for base canon sheets are unavailable; records are marked `unknown_requires_manual_input`.
- Control Tests 01–07 are human-approved and published as MAIN control-test outputs; exact original generation prompts and backends remain unavailable.
- `MARINA_CANON_GENERATION_PROMPTS.txt` contains template prompts for planned future generation but may not match the exact prompts that produced the three approved base-canon images.

## Prompt Logging Rules

- Every future approved/candidate/rejected generation must have a `prompt_id`.
- Every `prompt_id` must link to an output image path.
- Every prompt record must include a reference map.
- Exact visible prompts are stored as `exact_user_visible_prompt`.
- Reconstructed prompts are marked honestly as `reconstructed_from_conversation_and_approved_result`.
- Unknown/unavailable prompts are marked as `unknown_requires_manual_input`.
- Do not claim unavailable hidden tool prompts are exact.
- Do not rename historical approved images during prompt backfill.