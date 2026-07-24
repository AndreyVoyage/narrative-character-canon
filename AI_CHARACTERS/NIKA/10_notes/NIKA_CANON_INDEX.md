# NIKA Canon Index

## Status
BASE_CANON_APPROVED / CONTROL_TESTS_APPROVED / PROMPT_PIPELINE_ACTIVE

## Active Canon Files

### Imported Raw References

* Primary face reference (FACE_MAIN):
  `AI_CHARACTERS/NIKA/01_refs_raw/NIKA_RAW_01_face_main_burgundy_expressions.png`
* Body main reference (BODY_MAIN):
  `AI_CHARACTERS/NIKA/01_refs_raw/NIKA_RAW_02_body_main_burgundy_multiview.png`
* Body support reference (BODY_SUPPORT):
  `AI_CHARACTERS/NIKA/01_refs_raw/NIKA_RAW_03_body_support_gym_multiview.png`
* Formal style main (FORMAL_STYLE_MAIN):
  `AI_CHARACTERS/NIKA/01_refs_raw/NIKA_RAW_04_style_main_burgundy_bar.png`
* Formal support (FACE_SUPPORT / FORMAL_STYLE_SUPPORT):
  `AI_CHARACTERS/NIKA/01_refs_raw/NIKA_RAW_05_formal_support_burgundy_sheet.png`
* Sports outfit support (SPORTS_OUTFIT_SUPPORT):
  `AI_CHARACTERS/NIKA/01_refs_raw/NIKA_RAW_06_sports_support_gym_leggings.png`

### Approved Canon Sheets

* Face canon A:
  `AI_CHARACTERS/NIKA/03_face_sheet/NIKA_face_canon_v1_sheet_A_APPROVED.png`
* Expression canon A:
  `AI_CHARACTERS/NIKA/03_face_sheet/expressions/NIKA_expressions_v1_sheet_A_APPROVED.png`
* Body canon A (front / side / back):
  `AI_CHARACTERS/NIKA/04_body_sheet/NIKA_body_canon_v1_sheet_A_front_side_back_APPROVED.png`
* Body canon B (pose variations):
  `AI_CHARACTERS/NIKA/04_body_sheet/NIKA_body_canon_v1_sheet_B_pose_variations_APPROVED.png`

### Approved Control Tests

* TEST01 MAIN — neutral portrait (v1):
  `AI_CHARACTERS/NIKA/07_generated/canon_tests/03_portrait_expression/NIKA_test01_neutral_portrait_v1_APPROVED.png`
* TEST01 ALT — neutral portrait relaxed neckline (v2):
  `AI_CHARACTERS/NIKA/07_generated/canon_tests/03_portrait_expression/NIKA_test01_neutral_portrait_v2_APPROVED.png`
* TEST02 MAIN — evening embankment:
  `AI_CHARACTERS/NIKA/07_generated/canon_tests/01_evening_embankment/NIKA_test02_evening_embankment_v1_APPROVED.png`
* TEST03 MAIN — sports yoga:
  `AI_CHARACTERS/NIKA/07_generated/canon_tests/02_sports_yoga/NIKA_test03_sports_yoga_v1_APPROVED.png`

## Rejected / Held-Local Images

* Beach photo: REJECTED — identity and body-proportion drift; hair too long; visible graphic artifact.
* Black asymmetrical dress multi-panel sheet: HELD_LOCAL — not imported.
* Green-background pole-pose multi-panel sheet: HELD_LOCAL — not imported.

## Prompt Pipeline

* Prompt index: `AI_CHARACTERS/NIKA/06_prompts/NIKA_PROMPT_INDEX.md`
* Working scene prompts: `AI_CHARACTERS/NIKA/06_prompts/NIKA_WORKING_SCENE_PROMPTS.md`
* Prompt run log: `AI_CHARACTERS/NIKA/06_prompts/NIKA_PROMPT_RUN_LOG.jsonl`
* Canon generation prompts: `AI_CHARACTERS/NIKA/06_prompts/NIKA_CANON_GENERATION_PROMPTS.txt`

## Notes

Base canon and three control tests (four approved images including TEST01 ALT) are published.
All future generations must record prompt_id, references, output path, verdict, and notes.
Held-local and rejected images remain outside the deployed canon.