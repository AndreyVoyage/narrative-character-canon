# KIRA Prompt Index

## Status

PROMPT_PIPELINE_ACTIVE_CORE

## Purpose

This folder stores prompt templates, working scene prompts, reference maps, and prompt run logs for KIRA generations.

## Prompt Files

- `KIRA_BASE_PROMPT.txt` — original reusable base prompt source
- `KIRA_EVENING_SCENE_PROMPT.txt` — original reusable evening/bar/embankment prompt source
- `KIRA_SPORTS_SCENE_PROMPT.txt` — original reusable sports/yoga prompt source
- `KIRA_NEGATIVE_PROMPT.txt` — original reusable negative prompt kit
- `KIRA_WORKING_SCENE_PROMPTS.md` — normalized prompt sections and reconstructions
- `KIRA_PROMPT_RUN_LOG.jsonl` — machine-readable prompt run log
- `KIRA_PROMPT_INDEX.md` — this index

## Reference Map

| Letter | File | Role |
|---|---|---|
| A | `AI_CHARACTERS/KIRA/03_face_sheet/KIRA_face_canon_sheet_A.png` | face canon |
| B | `AI_CHARACTERS/KIRA/04_body_sheet/KIRA_BODY_CANON_v4_sheet_A_4views.png` | body canon |
| C | `AI_CHARACTERS/KIRA/03_face_sheet/expressions/KIRA_expressions_v1_sheet_A_emotional.png` | expression canon |
| D | `AI_CHARACTERS/KIRA/05_outfits/evening_dress/KIRA_evening_dress_FINAL_sheet_A_fullbody.png` | evening dress reference |
| E | `AI_CHARACTERS/KIRA/05_outfits/sports_look/KIRA_sports_look_v1_sheet_A_front_side_back.png` | sports look reference |

## Active Core Prompt IDs

| Prompt ID | Target | Status | Source | Output |
|---|---|---|---|---|
| `KIRA_FACE_CANON_V1_A` | face canon sheet A | APPROVED | `unknown_requires_manual_input` | `AI_CHARACTERS/KIRA/03_face_sheet/KIRA_face_canon_sheet_A.png` |
| `KIRA_BODY_CANON_V4_A` | body canon sheet A | APPROVED | `unknown_requires_manual_input` | `AI_CHARACTERS/KIRA/04_body_sheet/KIRA_BODY_CANON_v4_sheet_A_4views.png` |
| `KIRA_EXPRESSIONS_V1_A` | expression sheet A | APPROVED | `unknown_requires_manual_input` | `AI_CHARACTERS/KIRA/03_face_sheet/expressions/KIRA_expressions_v1_sheet_A_emotional.png` |
| `KIRA_TEST01_EVENING_EMBANKMENT_V1_MAIN` | evening embankment control test | APPROVED | `reconstructed_from_conversation_and_approved_result` | `AI_CHARACTERS/KIRA/07_generated/canon_tests/01_evening_embankment/KIRA_test01_evening_embankment_v2_MAIN.png` |
| `KIRA_TEST02_SPORTS_YOGA_V1_MAIN` | sports/yoga control test | APPROVED | `reconstructed_from_conversation_and_approved_result` | `AI_CHARACTERS/KIRA/07_generated/canon_tests/02_sports_yoga/KIRA_test02_sports_yoga_v2_MAIN.png` |
| `KIRA_TEST03_PORTRAIT_EXPRESSION_V1` | portrait/bar-romance expression test | APPROVED | `reconstructed_from_conversation_and_approved_result` | `AI_CHARACTERS/KIRA/07_generated/canon_tests/03_portrait_expression/KIRA_test02_bar_romance_v1_APPROVED.png` |

## Known Deferred Issues

- KIRA docs use `.md.txt` and `.txt.txt`; cleanup is deferred.
- KIRA filenames use mixed suffixes: `_MAIN`, `_ALT`, `_APPROVED`, `FINAL`, and no suffix; naming normalization is deferred.
- KIRA ALT test files are approved alternates but are not included in the first core JSONL set.
- KIRA+ANDREY joint prompt pipeline is separate.
- Exact per-image prompts for base canon sheets are unavailable; records are marked `unknown_requires_manual_input`.

## Prompt Logging Rules

- Every future approved/candidate/rejected generation must have a `prompt_id`.
- Every `prompt_id` must link to an output image path.
- Every prompt record must include a reference map.
- Exact visible prompts are stored as `exact_user_visible_prompt`.
- Reconstructed prompts are marked honestly as `reconstructed_from_conversation_and_approved_result`.
- Unknown/unavailable prompts are marked as `unknown_requires_manual_input`.
- Do not claim unavailable hidden tool prompts are exact.
- Do not rename historical approved images during prompt backfill.
