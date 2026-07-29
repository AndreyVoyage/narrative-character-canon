# MAKSIM Prompt Index

Canonical prompt ID index for MAKSIM visual canon generation.

## Character

- Character ID: MAKSIM
- Pipeline status: PROMPT_PIPELINE_CREATED
- Last normalized: 2026-07-29

## Canonical source hierarchy

1. NCC repository visual canon (narrative-character-canon)
2. VNE/persona narrative sources (fallback only)
3. Approved prompt handoffs
4. Reconstructed prompts (labeled honestly)

## Canon identity anchors (OWNER_APPROVED_CANON)

- Height: 188 cm
- Weight direction: approximately 115 kg
- Body direction: tall classic golden-era bodybuilder
- Face: full warm good-natured masculine face, calm approachable gaze
- Eyes: light subdued gray or gray-green eyes
- Hair: dark-brown medium-length naturally wavy hair, swept back
- Stubble: short neat stubble
- Abdomen: controlled flat, non-protruding

## Prompt records

| # | Prompt ID | Attempt | Variant | GEN ID | Verdict | Role | Output |
|---|---|---|---|---|---|---|---|
| 1 | MAKSIM_FACE_CANON_V1 | 02 | — | e897b7a4-e1a3-4e21-a322-d91df1477de5 | APPROVED_WITH_MINOR_NOTES | FACE_MAIN | 03_face_sheet/MAKSIM_face_canon_v1_sheet_A_APPROVED.png |
| 2 | MAKSIM_EXPRESSIONS_V1 | 03 | — | e5ed21a7-eab3-4279-82c8-6b6db4917a78 | APPROVED_WITH_MINOR_NOTES | EXPRESSIONS_MAIN | 03_face_sheet/expressions/MAKSIM_expressions_v1_sheet_A_APPROVED.png |
| 3 | MAKSIM_BODY_CANON_V1 | 07 | MAIN | f88eac6c-9b82-4585-9568-e79cda528316 | APPROVED_WITH_MINOR_NOTES_AS_FINAL_BODY_CANON | BODY_MAIN | 04_body_sheet/MAKSIM_body_canon_v1_sheet_A_front_side_back_APPROVED.png |
| 4 | MAKSIM_EVERYDAY_CLOTHED_TURNAROUND_V1 | 02 | — | 8d58e39c-7a99-4e3c-9e2a-a25503f6216a | APPROVED_WITH_MINOR_NOTES_AS_CLOTHED_BODY_REFERENCE | BODY_SUPPORT | 04_body_sheet/clothed_references/MAKSIM_everyday_clothed_turnaround_v1_sheet_A_APPROVED.png |
| 5 | MAKSIM_NATURAL_MOTION_V1 | 02 | — | 22a9ad38-21f9-4c2c-86d3-22af503e443f | APPROVED_WITH_MINOR_NOTES_AS_NATURAL_MOTION_REFERENCE | MOTION_SUPPORT | 04_body_sheet/motion_references/MAKSIM_natural_motion_v1_six_pose_sheet_A_APPROVED.png |
| 6 | MAKSIM_MR_OLYMPIA_STAGE_V1 | 03 | — | bb7a7db0-965a-4038-9c07-b28498ff8250 | APPROVED_AS_PRIMARY_STAGE_POSE_REFERENCE | STAGE_PRIMARY | 04_body_sheet/stage_references/MAKSIM_mr_olympia_stage_v1_attempt03_six_pose_PRIMARY_REFERENCE.png |
| 7 | MAKSIM_MR_OLYMPIA_STAGE_V1 | 02 | — | 781f2a15-c75d-4450-933f-9bf864faf6b5 | APPROVED_AS_SECONDARY_STAGE_REFERENCE | STAGE_SECONDARY | 04_body_sheet/stage_references/MAKSIM_mr_olympia_stage_v1_attempt02_secondary_REFERENCE.png |
| 8 | MAKSIM_OUTFIT_VARIANTS_V1 | 01 | — | cd9e65d3-71f7-4458-96be-fe5712382415 | APPROVED_WITH_MINOR_NOTES_AS_WARDROBE_REFERENCE | WARDROBE_SUPPORT | 05_outfits/scene_outfits/MAKSIM_outfit_variants_v1_six_looks_sheet_A_APPROVED.png |
| 9 | MAKSIM_SCENE_OUTFITS_V1 | 01 | — | c59ff168-d49a-43fb-b5e7-7cee6cd9fbb9 | APPROVED_WITH_MINOR_NOTES_AS_SCENE_OUTFIT_REFERENCE | SCENE_OUTFIT_SUPPORT | 05_outfits/scene_outfits/MAKSIM_scene_outfits_v1_six_locations_sheet_A_APPROVED.png |

## Superseded attempts

- MAKSIM_FACE_CANON_V1 attempt 01 — REVISE (draft, not approved)
- MAKSIM_EXPRESSIONS_V1 attempt 02 — REVISE (draft, not approved)
- MAKSIM_BODY_CANON_V1 attempt 01 — REVISE (draft, not approved)
- MAKSIM_BODY_CANON_V1 attempt 02 — REVISE (draft, not approved)
- MAKSIM_BODY_CANON_V1 attempt 06 — REVISE (draft, REMOVED 2026-07-29: exact hash duplicate of approved natural motion sheet)

## Optional reference-only assets (not in prompt registry)

- MAKSIM_MR_OLYMPIA_STAGE_V1 attempt 01 — PHYSIQUE_REFERENCE (reference-only, stored in 07_generated/drafts/)

## Rules

- Drafts never override approved canon.
- Cross-character sauna/scale-test images are not BODY_MAIN and are not part of solo MAKSIM visual canon.
- Original exact generation prose may be reconstructed rather than verbatim where source prompt text was not preserved. All reconstructed prompts are labeled honestly.
- All records are selected for deployment but NOT YET COMMITTED (status as of 2026-07-29).

## Related files

- MAKSIM_PROMPT_RUN_LOG.jsonl — 9 JSONL records
- MAKSIM_WORKING_SCENE_PROMPTS.md — scene generation reference
- MAKSIM_CANON_GENERATION_PROMPTS.txt — original generation prompts (updated)
- MAKSIM_REFERENCE_PRESETS.json — canonical reference paths
- MAKSIM_CANON_INDEX.md — full canon index

---

*MAKSIM Prompt Index | NCC Visual Canon Pipeline | 2026-07-29*