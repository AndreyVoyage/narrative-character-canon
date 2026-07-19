# MARINA Canon Index

## Status
BASE_CANON_APPROVED / CONTROL_TESTS_APPROVED / PROMPT_PIPELINE_ACTIVE

## Character
MARINA

## Active version
Base canon v1.0

## Active canon files

* Face canon:
  `AI_CHARACTERS/MARINA/03_face_sheet/MARINA_face_canon_v1_sheet_A_APPROVED.png`
  * Prompt ID: `MARINA_FACE_CANON_V1_A`
  * SHA-256: `da85d0c282c2825d26480c403d092f997dc589a778805dd2c0e47353a84fa959`

* Expression canon:
  `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_A_APPROVED.png`
  * Prompt ID: `MARINA_EXPRESSIONS_V1_A`
  * SHA-256: `ee0d86402325e7a013f6d2b1892cbccc032107720a394ffa269b4f7030e11294`

* Body canon:
  `AI_CHARACTERS/MARINA/04_body_sheet/MARINA_body_canon_v1_sheet_A_APPROVED.png`
  * Prompt ID: `MARINA_BODY_CANON_V1_A`
  * SHA-256: `67598c7e171f72e90d7a161c209ef555651a5c72b55b672acdf85fdc57f3961f`

## Identity anchor

Adult woman, 155 cm, 45 kg, petite slender feminine build, compact realistic proportions, narrow shoulders, small defined waist, soft proportionate hips, naturally medium-full bust approximately Russian size 3, firm rounded and naturally lifted, proportionate to her petite frame, not exaggerated. Natural light brown hair with soft texture, thoughtful blue eyes, soft gentle features, shy but warm smile, natural skin texture, minimal makeup, pastel warm clothing, gentle intimate warmth, natural soft lighting.

## Folder structure

* `01_refs_raw/`
* `02_best_refs/`
* `03_face_sheet/`
* `03_face_sheet/expressions/`
* `04_body_sheet/`
* `04_body_sheet/candidates/`
* `05_outfits/` (casual/, evening_dress/, formal/, scene_outfits/, sports_look/, candidates/)
* `06_prompts/`
* `07_generated/` (canon_tests/, drafts/, rejected/)
* `08_masks/`
* `09_blender/`
* `10_notes/`

## Prompt pipeline

* Prompt index: `AI_CHARACTERS/MARINA/06_prompts/MARINA_PROMPT_INDEX.md`
* Working scene prompts: `AI_CHARACTERS/MARINA/06_prompts/MARINA_WORKING_SCENE_PROMPTS.md`
* Prompt run log: `AI_CHARACTERS/MARINA/06_prompts/MARINA_PROMPT_RUN_LOG.jsonl`
* Generation prompts: `AI_CHARACTERS/MARINA/06_prompts/MARINA_CANON_GENERATION_PROMPTS.txt`

## Notes

The three base-canon images were human-selected from existing AI-generated assets and imported into the repository without modifying the local source files. Exact per-image generation prompts are not available; records are marked `unknown_requires_manual_input` following the same pattern as KIRA base-canon records.

Control Tests 01–07 are human-approved and registered as MAIN control-test outputs. They validate MARINA across indoor, outdoor, casual, formal, emotional, and poolside scene contexts.

## Support expression references (SUPPORT)

* Expression sheet B (SUPPORT):
  `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_B_SUPPORT.png`
  * Prompt ID: `MARINA_EXPRESSIONS_V1_B`
  * Role: SUPPORT — not active MAIN
  * SHA-256: `9b82e6973b7f638d70613d40b80388b458909eee16b97dd82b5207cb2e46c24c`

* Expression sheet C (SUPPORT):
  `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_C_SUPPORT.png`
  * Prompt ID: `MARINA_EXPRESSIONS_V1_C`
  * Role: SUPPORT — not active MAIN
  * SHA-256: `489abedb7dadad523a8d80787ab8f03be0d54472d7ee42366be3c4a0aebc6a9f`

* Expression sheet D (SUPPORT):
  `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_D_SUPPORT.png`
  * Prompt ID: `MARINA_EXPRESSIONS_V1_D`
  * Role: SUPPORT — not active MAIN
  * SHA-256: `3c723384ba51c56946cd219893776d0a535f20a56b2a64662db0762f958e0505`

* Expression sheet E (SUPPORT):
  `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_E_SUPPORT.png`
  * Prompt ID: `MARINA_EXPRESSIONS_V1_E`
  * Role: SUPPORT — not active MAIN
  * SHA-256: `2cadc233a438ff36cc70f16529fa01db5df49cdb9c585870937b3aeb8768ebc3`

* Expression sheet F (SUPPORT):
  `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_F_SUPPORT.png`
  * Prompt ID: `MARINA_EXPRESSIONS_V1_F`
  * Role: SUPPORT — not active MAIN
  * SHA-256: `e2d38458581129ef6668bf34778c4d8ad28657f025149b46d0f886ea771dab5e`

## Outfit canon

* Evening peach dress (MAIN):
  `AI_CHARACTERS/MARINA/05_outfits/MARINA_outfit_evening_peach_v1_sheet_A_APPROVED.png`
  * Prompt ID: `MARINA_OUTFIT_EVENING_PEACH_V1_A`
  * Role: MAIN OUTFIT REFERENCE
  * SHA-256: `36946df15287140fecdb9ed8fab95667a996cd30ec95b404c001a02d61fcdc3e`

* Evening peach portrait (SUPPORT):
  `AI_CHARACTERS/MARINA/05_outfits/MARINA_outfit_evening_peach_v1_portrait_SUPPORT.png`
  * Prompt ID: `MARINA_OUTFIT_EVENING_PEACH_V1_B`
  * Role: SUPPORT OUTFIT REFERENCE
  * SHA-256: `208342e87b896378855dcb7afbbef6135ca1c78bb41e0124d3ba8222d6008f02`

* Warm evening portrait (SUPPORT):
  `AI_CHARACTERS/MARINA/05_outfits/MARINA_outfit_warm_evening_v1_portrait_SUPPORT.png`
  * Prompt ID: `MARINA_OUTFIT_WARM_EVENING_V1_A`
  * Role: SUPPORT OUTFIT REFERENCE
  * SHA-256: `ac00afe3e921d74a6c7b49bbd740e3e736bdaed127c0adacc8d729b2d47b89d8`

## Approved control tests

* Test01 — Rainy cafe:
  `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test01_rainy_cafe_v1_APPROVED.png`
  * Prompt ID: `MARINA_TEST01_RAINY_CAFE_V1`
  * Verdict: `APPROVED_AS_TEST`
  * Role: `MAIN`
  * SHA-256: `6f49909b313785eb0a663b5517f03cb65030d98e864d70658217a9c64b6d4b5e`

* Test02 — Theater melancholy:
  `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test02_theater_melancholy_v1_APPROVED.png`
  * Prompt ID: `MARINA_TEST02_THEATER_MELANCHOLY_V1`
  * Verdict: `APPROVED_AS_TEST`
  * Role: `MAIN`
  * SHA-256: `a743b3e994be35f954bb4e61749dc774f46b8461a714c178617e150e76ff2faf`

* Test03 — Evening city balcony:
  `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test03_evening_city_balcony_v1_APPROVED.png`
  * Prompt ID: `MARINA_TEST03_EVENING_CITY_BALCONY_V1`
  * Verdict: `APPROVED_AS_TEST`
  * Role: `MAIN`
  * SHA-256: `19fc949a03568500e7e23bcdf3e63ce15549c79d72d22941bbdefec2a3565492`

* Test04 — Autumn street portrait:
  `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test04_autumn_street_portrait_v1_APPROVED.png`
  * Prompt ID: `MARINA_TEST04_AUTUMN_STREET_PORTRAIT_V1`
  * Verdict: `APPROVED_AS_TEST`
  * Role: `MAIN`
  * SHA-256: `e813e1826b8e4fca99415f6c82fec4a335fa3acfd720fcd92c51e05f307bd927`

* Test05 — Morning pajamas:
  `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test05_morning_pajamas_v1_APPROVED.png`
  * Prompt ID: `MARINA_TEST05_MORNING_PAJAMAS_V1`
  * Verdict: `APPROVED_AS_TEST`
  * Role: `MAIN`
  * SHA-256: `cdd6d6f0a4883947856661b58eca5957518c4e930a528fbb7b0273c046e632ed`

* Test06 — White garden formal:
  `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test06_white_garden_formal_v1_APPROVED.png`
  * Prompt ID: `MARINA_TEST06_WHITE_GARDEN_FORMAL_V1`
  * Verdict: `APPROVED_AS_TEST`
  * Role: `MAIN`
  * SHA-256: `e7e7a11693324d4312dfc9718e3eee11827443b84bf99086c832cf92c3346d90`

* Test07 — Pool sunset:
  `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test07_pool_sunset_v1_APPROVED.png`
  * Prompt ID: `MARINA_TEST07_POOL_SUNSET_V1`
  * Verdict: `APPROVED_AS_TEST`
  * Role: `MAIN`
  * SHA-256: `7739db6e04c6253371531972bbefbfabaa7ce7ebdbdcbe6774dc5ad7a868ee79`
## Next action

MARINA Test01–Test07 are complete. Awaiting human selection of the next character or coverage target.

---

*MARINA Canon Index | NCC Repository | 2026-07-18*
