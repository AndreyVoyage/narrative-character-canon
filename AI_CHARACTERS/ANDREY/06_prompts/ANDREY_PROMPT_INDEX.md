# ANDREY Prompt Index

## Status
PROMPT_PIPELINE_ACTIVE

## Purpose

This folder stores prompt templates, working scene prompts, reference maps, and prompt run logs for ANDREY Senior generations.

## Prompt Files

* `ANDREY_FACE_CANON_PROMPT.txt` — original face canon prompt kit (exact archive).
* `ANDREY_BODY_CANON_PROMPT.txt` — original body canon prompt kit (exact archive).
* `ANDREY_CONTROL_TEST_PROMPTS.txt` — original control test prompt kit (exact archive).
* `ANDREY_WORKING_SCENE_PROMPTS.md` — normalized reusable prompt sections.
* `ANDREY_PROMPT_RUN_LOG.jsonl` — machine-readable prompt run log.
* `ANDREY_PROMPT_INDEX.md` — this index.

## Active Prompt IDs

| Prompt ID | Target | Status | Source | Output |
|---|---|---|---|---|
| `ANDREY_FACE_CANON_V1_A_BASIC` | face canon sheet A basic expressions | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY/03_face_sheet/ANDREY_face_canon_v1_sheet_A_basic.png` |
| `ANDREY_FACE_CANON_V1_B_ANGLES` | face canon sheet B multi-angle | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY/03_face_sheet/ANDREY_face_canon_v1_sheet_B_angles.png` |
| `ANDREY_EXPRESSIONS_V1_C_REFINED` | expression sheet C refined | APPROVED | reconstructed_from_conversation_and_approved_result | `AI_CHARACTERS/ANDREY/03_face_sheet/expressions/ANDREY_expressions_v1_sheet_C_refined.png` |
| `ANDREY_BODY_CANON_V1_A_FRONT_SIDE_BACK` | body canon sheet A front side back 3Q | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_A_front_side_back.png` |
| `ANDREY_BODY_CANON_V1_B_POSE_VARIATIONS` | body canon sheet B pose variations | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_B_pose_variations.png` |
| `ANDREY_TEST01_NEUTRAL_STUDIO_PORTRAIT_V1` | neutral studio portrait | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY/07_generated/canon_tests/01_neutral_studio_portrait/ANDREY_test01_neutral_studio_portrait_v1.png` |
| `ANDREY_TEST02_FULL_BODY_BLUE_SHIRT_STUDIO_V1` | full body blue shirt studio | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY/07_generated/canon_tests/02_full_body_blue_shirt/ANDREY_test02_full_body_blue_shirt_studio_v1.png` |
| `ANDREY_TEST03_WARM_BAR_PORTRAIT_V1` | warm bar portrait | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY/07_generated/canon_tests/03_warm_bar_portrait/ANDREY_test03_warm_bar_portrait_v1.png` |
| `ANDREY_TEST04_FORMAL_EVENING_LOOK_V1` | formal evening look | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY/07_generated/canon_tests/04_formal_evening_look/ANDREY_test04_formal_evening_look_v1.png` |
| `ANDREY_TEST05_SPORTS_GYM_IDENTITY_V1` | sports gym identity | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY/07_generated/canon_tests/05_sports_gym_identity/ANDREY_test05_sports_gym_identity_v1.png` |
| `ANDREY_TEST06_SEA_YACHT_MOOD_V1` | sea yacht mood scene | APPROVED | exact_user_visible_prompt | `AI_CHARACTERS/ANDREY/07_generated/canon_tests/06_sea_yacht_mood/ANDREY_test06_sea_yacht_mood_scene_v1.png` |

## Reference Map

For solo ANDREY Senior prompts:

* Image A = `AI_CHARACTERS/ANDREY/03_face_sheet/ANDREY_face_canon_v1_sheet_A_basic.png`
* Image B = `AI_CHARACTERS/ANDREY/03_face_sheet/ANDREY_face_canon_v1_sheet_B_angles.png`
* Image C = `AI_CHARACTERS/ANDREY/03_face_sheet/expressions/ANDREY_expressions_v1_sheet_C_refined.png`
* Image D = `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_A_front_side_back.png`
* Image E = `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_B_pose_variations.png`

## Prompt Logging Rules

* Every approved/candidate/rejected generation must have a `prompt_id`.
* Every `prompt_id` must link to an output image path.
* Every prompt record must include a reference map.
* Exact visible prompts are stored as `exact_user_visible_prompt`.
* Reconstructed prompts are marked honestly as `reconstructed_from_conversation_and_approved_result`.
* Do not claim unavailable hidden tool prompts are exact.
* Preserve Andrey Senior identity: adult man, 38, 180 cm, athletic strong build, blue eyes, light blonde hair, light stubble, blue shirt signature.
* Keep content mature, non-explicit, and identity-stable.
