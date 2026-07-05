# OLGA Prompt Index

## Status
PROMPT_PIPELINE_ACTIVE

## Purpose

This folder stores prompt templates, working scene prompts, reference maps, and prompt run logs for OLGA generations.

## Prompt Files

* `OLGA_CANON_GENERATION_PROMPTS.txt` — initial setup skeletons and generation rules.
* `OLGA_WORKING_SCENE_PROMPTS.md` — approved/reusable working prompts.
* `OLGA_PROMPT_RUN_LOG.jsonl` — machine-readable prompt run log.
* `OLGA_PROMPT_INDEX.md` — this index.

## Active Prompt IDs

| Prompt ID | Target | Status | Source | Output |
|---|---|---|---|---|
| OLGA_FACE_CANON_V1_A | face canon sheet | APPROVED | reconstructed_from_conversation_and_approved_result | `AI_CHARACTERS/OLGA/03_face_sheet/OLGA_face_canon_v1_sheet_A_APPROVED.png` |
| OLGA_EXPRESSIONS_V1_A | expression sheet | APPROVED | reconstructed_from_conversation_and_approved_result | `AI_CHARACTERS/OLGA/03_face_sheet/expressions/OLGA_expressions_v1_sheet_A_APPROVED.png` |
| OLGA_BODY_CANON_V1_A | body canon sheet A | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/OLGA/04_body_sheet/OLGA_body_canon_v1_sheet_A_front_side_back_APPROVED.png` |
| OLGA_BODY_CANON_V1_B | body pose variations | APPROVED | reconstructed_from_conversation_and_approved_result | `AI_CHARACTERS/OLGA/04_body_sheet/OLGA_body_canon_v1_sheet_B_pose_variations_APPROVED.png` |
| OLGA_TEST01_EVENING_EMBANKMENT_V1 | evening embankment | APPROVED | reconstructed_from_conversation_and_approved_result | `AI_CHARACTERS/OLGA/07_generated/canon_tests/01_evening_embankment/OLGA_test01_evening_embankment_v1_APPROVED.png` |
| OLGA_TEST02_SPORTS_YOGA_V1 | sports yoga | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/OLGA/07_generated/canon_tests/02_sports_yoga/OLGA_test02_sports_yoga_v1_APPROVED.png` |
| OLGA_TEST03_PORTRAIT_EXPRESSION_V1 | portrait expression | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/OLGA/07_generated/canon_tests/03_portrait_expression/OLGA_test03_portrait_expression_v1_APPROVED.png` |
| OLGA_TEST04_OUTDOOR_WALK_AJ_V1 | outdoor walk with ANDREY_JUNIOR | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/OLGA/07_generated/canon_tests/04_outdoor_walk_with_andrey_junior/OLGA_test04_outdoor_walk_with_andrey_junior_v1_APPROVED.png` |

## Reference Map

| Image | Path | Role |
|---|---|---|
| Image A | `AI_CHARACTERS/OLGA/02_refs_selected/OLGA_ref_face_primary_v1_SELECTED.jpg` | Primary selected face reference |
| Image B | `AI_CHARACTERS/OLGA/03_face_sheet/OLGA_face_canon_v1_sheet_A_APPROVED.png` | Approved face canon sheet |
| Image C | `AI_CHARACTERS/OLGA/03_face_sheet/expressions/OLGA_expressions_v1_sheet_A_APPROVED.png` | Approved expression sheet |
| Image D | `AI_CHARACTERS/OLGA/04_body_sheet/OLGA_body_canon_v1_sheet_B_pose_variations_APPROVED.png` | Approved body pose variations |
| Image E | `AI_CHARACTERS/ANDREY_JUNIOR/03_face_sheet/ANDREY_JUNIOR_face_canon_v1_sheet_A_APPROVED.png` | ANDREY_JUNIOR face canon reference |
| Image F | `AI_CHARACTERS/ANDREY_JUNIOR/04_body_sheet/ANDREY_JUNIOR_body_canon_v2_sheet_A_front_side_back_APPROVED.png` | ANDREY_JUNIOR body canon reference |

## Prompt Logging Rules

* Every approved/candidate/rejected generation must have a `prompt_id`.
* Every `prompt_id` must link to an output image path.
* Every prompt record must include a reference map.
* Exact visible prompts are stored as `exact_user_visible_prompt`.
* Reconstructed prompts are marked honestly as `reconstructed_from_conversation_and_approved_result`.
* Do not claim unavailable hidden tool prompts are exact.
