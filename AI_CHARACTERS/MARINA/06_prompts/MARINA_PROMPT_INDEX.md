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

## Known Deferred Issues

- Exact per-image generation prompts for base canon sheets are unavailable; records are marked `unknown_requires_manual_input`.
- Control tests remain PENDING; no generated test images exist yet.
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