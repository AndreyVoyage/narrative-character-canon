# ANDREY_JUNIOR Prompt Index

## Status
PROMPT_PIPELINE_ACTIVE

## Purpose

This folder stores prompt templates, working scene prompts, reference maps, and prompt run logs for ANDREY_JUNIOR generations.

## Prompt Files

* `ANDREY_JUNIOR_CANON_GENERATION_PROMPTS.txt` — original working prompt source and exact visible prompt archive.
* `ANDREY_JUNIOR_WORKING_SCENE_PROMPTS.md` — normalized reusable prompt sections.
* `ANDREY_JUNIOR_PROMPT_RUN_LOG.jsonl` — machine-readable prompt run log.
* `ANDREY_JUNIOR_PROMPT_INDEX.md` — this index.

## Active Prompt IDs

| Prompt ID | Target | Status | Source | Output |
|---|---|---|---|---|
| `ANDREY_JUNIOR_FACE_CANON_V1_A` | face canon sheet | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY_JUNIOR/03_face_sheet/ANDREY_JUNIOR_face_canon_v1_sheet_A_APPROVED.png` |
| `ANDREY_JUNIOR_EXPRESSIONS_V2_A` | expression sheet | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY_JUNIOR/03_face_sheet/expressions/ANDREY_JUNIOR_expressions_v2_sheet_A_APPROVED.png` |
| `ANDREY_JUNIOR_BODY_CANON_V2_A` | body canon sheet A | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY_JUNIOR/04_body_sheet/ANDREY_JUNIOR_body_canon_v2_sheet_A_front_side_back_APPROVED.png` |
| `ANDREY_JUNIOR_BODY_CANON_V2_B` | body pose variations | APPROVED | reconstructed_from_conversation_and_approved_result | `AI_CHARACTERS/ANDREY_JUNIOR/04_body_sheet/ANDREY_JUNIOR_body_canon_v2_sheet_B_pose_variations_APPROVED.png` |
| `ANDREY_JUNIOR_TEST01_NEUTRAL_STUDIO_PORTRAIT_V1` | neutral studio portrait | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/01_neutral_studio_portrait/ANDREY_JUNIOR_test01_neutral_studio_portrait_v1_APPROVED.png` |
| `ANDREY_JUNIOR_TEST02_FULL_BODY_STUDIO_V1` | full body studio | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/02_full_body_studio/ANDREY_JUNIOR_test02_full_body_studio_v1_APPROVED.png` |
| `ANDREY_JUNIOR_TEST03_ATHLETIC_GYM_IDENTITY_V1` | athletic gym identity | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/03_athletic_gym_identity/ANDREY_JUNIOR_test03_athletic_gym_identity_v1_APPROVED.png` |
| `ANDREY_JUNIOR_TEST04_CASUAL_OUTFIT_V1` | casual outfit | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/04_casual_outfit/ANDREY_JUNIOR_test04_casual_outfit_v1_APPROVED.png` |
| `ANDREY_JUNIOR_TEST05_SCALE_COMPACT_BODY_CHECK_V1` | scale compact body check | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/05_scale_compact_body_check/ANDREY_JUNIOR_test05_scale_compact_body_check_v1_APPROVED.png` |
| `ANDREY_JUNIOR_TEST06_FATHER_SON_SCALE_CHECK_V2` | father-son scale check | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/06_father_son_scale_check/ANDREY_JUNIOR_test06_father_son_scale_check_v2_APPROVED.png` |
| `ANDREY_JUNIOR_TEST07_FATHER_SON_CASUAL_OUTDOOR_V1` | father-son casual outdoor | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/07_father_son_casual_outdoor/ANDREY_JUNIOR_test07_father_son_casual_outdoor_v1_APPROVED.png` |
| `ANDREY_JUNIOR_TEST08_FATHER_SON_HOME_CONVERSATION_V1` | father-son home conversation | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/08_father_son_home_conversation/ANDREY_JUNIOR_test08_father_son_home_conversation_v1_APPROVED.png` |
| `ANDREY_JUNIOR_TEST09_FATHER_SON_TRAINING_COACHING_V1` | father-son training coaching | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY_JUNIOR/07_generated/canon_tests/09_father_son_training_coaching/ANDREY_JUNIOR_test09_father_son_training_coaching_v1_APPROVED.png` |

## Reference Map

For solo ANDREY_JUNIOR prompts:

* Image A = `AI_CHARACTERS/ANDREY_JUNIOR/03_face_sheet/ANDREY_JUNIOR_face_canon_v1_sheet_A_APPROVED.png`
* Image B = `AI_CHARACTERS/ANDREY_JUNIOR/03_face_sheet/expressions/ANDREY_JUNIOR_expressions_v2_sheet_A_APPROVED.png`
* Image C = `AI_CHARACTERS/ANDREY_JUNIOR/04_body_sheet/ANDREY_JUNIOR_body_canon_v2_sheet_A_front_side_back_APPROVED.png`
* Image D = `AI_CHARACTERS/ANDREY_JUNIOR/04_body_sheet/ANDREY_JUNIOR_body_canon_v2_sheet_B_pose_variations_APPROVED.png`

For father-son prompts:

* Image A = `AI_CHARACTERS/ANDREY/03_face_sheet/ANDREY_face_canon_v1_sheet_A_basic.png`
* Image B = `AI_CHARACTERS/ANDREY/03_face_sheet/expressions/ANDREY_expressions_v1_sheet_C_refined.png`
* Image C = `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_A_front_side_back.png`
* Image D = `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_B_pose_variations.png`
* Image E = `AI_CHARACTERS/ANDREY_JUNIOR/03_face_sheet/ANDREY_JUNIOR_face_canon_v1_sheet_A_APPROVED.png`
* Image F = `AI_CHARACTERS/ANDREY_JUNIOR/03_face_sheet/expressions/ANDREY_JUNIOR_expressions_v2_sheet_A_APPROVED.png`
* Image G = `AI_CHARACTERS/ANDREY_JUNIOR/04_body_sheet/ANDREY_JUNIOR_body_canon_v2_sheet_A_front_side_back_APPROVED.png`
* Image H = `AI_CHARACTERS/ANDREY_JUNIOR/04_body_sheet/ANDREY_JUNIOR_body_canon_v2_sheet_B_pose_variations_APPROVED.png`

## Prompt Logging Rules

* Every approved/candidate/rejected generation must have a `prompt_id`.
* Every `prompt_id` must link to an output image path.
* Every prompt record must include a reference map.
* Exact visible prompts are stored as `exact_user_visible_prompt`.
* Reconstructed prompts are marked honestly as `reconstructed_from_conversation_and_approved_result`.
* Do not claim unavailable hidden tool prompts are exact.
* Do not use the active character name inside image-generation prompts when it causes filter or identity drift; use neutral reference-role wording when needed.
* For ANDREY_JUNIOR scenes, keep content family-neutral, natural, and age-appropriate.
