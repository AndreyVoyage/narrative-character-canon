# MARINA Working Scene Prompts

## Status

PROMPT_PIPELINE_ACTIVE

## Important Source Rules

- This file stores the exact reusable prompt-kit source from `MARINA_CANON_GENERATION_PROMPTS.txt` and prompt reconstructions.
- Base canon sheet entries do **not** have an exact per-image generation prompt stored anywhere in the repository. They are marked `unknown_requires_manual_input` and only reconstruction guidance is provided.
- Imported control tests whose exact original prompts are unavailable are marked `unknown_requires_manual_input`. Reference paths document current canon anchors for future reuse and are not represented as original generation inputs.
- Do not treat reconstructed text as a verbatim generation log.

---

## Original Prompt Kit Sources

These blocks are copied from `MARINA_CANON_GENERATION_PROMPTS.txt`.

### Identity Anchor

```text
Adult woman, 155 cm, 45 kg, petite slender feminine build, compact realistic proportions, narrow shoulders, small defined waist, soft proportionate hips, naturally medium-full bust approximately Russian size 3, firm rounded and naturally lifted, proportionate to her petite frame, not exaggerated. Natural light brown hair with soft texture, thoughtful blue eyes, soft gentle features, shy but warm smile, natural skin texture, minimal makeup, pastel warm clothing, gentle intimate warmth, natural soft lighting.
```

### Prompt Style Rules

```text
* Keep MARINA clearly an adult woman.
* Use phrases like "adult woman", "petite slender build", "compact proportions", "naturally medium-full bust proportionate to petite frame", "gentle feminine presence".
* Avoid sexualized wording.
* Avoid nude, lingerie, transparent clothing, fetish framing, or erotic staging.
* Avoid exaggerating body proportions.
* Avoid making her look too young or too old.
* Preserve the thoughtful blue eyes and shy but warm smile.
* Preserve the natural light brown hair with soft texture.
* Use photorealistic studio or natural window light reference language.
* Keep contexts gentle: portrait, home, street, casual, intimate, outdoor.
```

---

## Prompt Section — MARINA_FACE_CANON_V1_A

- **Prompt ID:** `MARINA_FACE_CANON_V1_A`
- **Status:** APPROVED
- **Output path:** `AI_CHARACTERS/MARINA/03_face_sheet/MARINA_face_canon_v1_sheet_A_APPROVED.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Source files used:** `MARINA_CANON_GENERATION_PROMPTS.txt`
- **Reference map:** A
- **Reconstruction guidance:** This output is the active face-canon sheet. A full exact generation prompt is not stored. The three approved base-canon images were human-selected from existing AI-generated assets and imported without modifying the local source files. Any future regeneration should use the Face Canon Sheet Prompt from `MARINA_CANON_GENERATION_PROMPTS.txt` plus the identity anchor (natural light brown hair, thoughtful blue eyes, soft gentle features, shy but warm smile).
- **Result notes:** Active face identity anchor. Imported from existing AI-generated assets.

---

## Prompt Section — MARINA_EXPRESSIONS_V1_A

- **Prompt ID:** `MARINA_EXPRESSIONS_V1_A`
- **Status:** APPROVED
- **Output path:** `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_A_APPROVED.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Source files used:** `MARINA_CANON_GENERATION_PROMPTS.txt`
- **Reference map:** A + C
- **Reconstruction guidance:** This output is the active expression-canon sheet. A full exact generation prompt is not stored. Any future regeneration should use the Expression Canon Sheet Prompt from `MARINA_CANON_GENERATION_PROMPTS.txt` with its six-expression range (neutral gentle, shy warm smile, thoughtful contemplation, soft laughter, tender warmth, peaceful calm).
- **Result notes:** Active expression reference. Imported from existing AI-generated assets.

---

## Prompt Section — MARINA_BODY_CANON_V1_A

- **Prompt ID:** `MARINA_BODY_CANON_V1_A`
- **Status:** APPROVED
- **Output path:** `AI_CHARACTERS/MARINA/04_body_sheet/MARINA_body_canon_v1_sheet_A_APPROVED.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Source files used:** `MARINA_CANON_GENERATION_PROMPTS.txt`
- **Reference map:** A + B
- **Reconstruction guidance:** This output is the active body-canon sheet. A full exact generation prompt is not stored. Any future regeneration should use the Body Canon Sheet Prompt from `MARINA_CANON_GENERATION_PROMPTS.txt` plus the identity anchor (155 cm, 45 kg, petite slender build, compact realistic proportions, narrow shoulders, small defined waist, soft proportionate hips, naturally medium-full bust approximately Russian size 3, not exaggerated).
- **Result notes:** Active body/proportion anchor. Imported from existing AI-generated assets.

---

## Prompt Section — MARINA_EXPRESSIONS_V1_B

- **Prompt ID:** `MARINA_EXPRESSIONS_V1_B`
- **Status:** APPROVED
- **Role:** SUPPORT
- **Output path:** `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_B_SUPPORT.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Source files used:** `MARINA_CANON_GENERATION_PROMPTS.txt`
- **Reference map:** A + C
- **Reconstruction guidance:** SUPPORT expression reference sheet B. Human-approved import. Not an active MAIN reference. A full exact generation prompt is not stored.
- **Result notes:** SUPPORT expression variant. Imported from existing AI-generated assets.

---

## Prompt Section — MARINA_EXPRESSIONS_V1_C

- **Prompt ID:** `MARINA_EXPRESSIONS_V1_C`
- **Status:** APPROVED
- **Role:** SUPPORT
- **Output path:** `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_C_SUPPORT.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Source files used:** `MARINA_CANON_GENERATION_PROMPTS.txt`
- **Reference map:** A + C
- **Reconstruction guidance:** SUPPORT expression reference sheet C. Human-approved import. Not an active MAIN reference. A full exact generation prompt is not stored.
- **Result notes:** SUPPORT expression variant. Imported from existing AI-generated assets.

---

## Prompt Section — MARINA_EXPRESSIONS_V1_D

- **Prompt ID:** `MARINA_EXPRESSIONS_V1_D`
- **Status:** APPROVED
- **Role:** SUPPORT
- **Output path:** `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_D_SUPPORT.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Source files used:** `MARINA_CANON_GENERATION_PROMPTS.txt`
- **Reference map:** A + C
- **Reconstruction guidance:** SUPPORT expression reference sheet D. Human-approved import. Not an active MAIN reference. A full exact generation prompt is not stored.
- **Result notes:** SUPPORT expression variant. Imported from existing AI-generated assets.

---

## Prompt Section — MARINA_EXPRESSIONS_V1_E

- **Prompt ID:** `MARINA_EXPRESSIONS_V1_E`
- **Status:** APPROVED
- **Role:** SUPPORT
- **Output path:** `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_E_SUPPORT.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Source files used:** `MARINA_CANON_GENERATION_PROMPTS.txt`
- **Reference map:** A + C
- **Reconstruction guidance:** SUPPORT expression reference sheet E. Human-approved import. Not an active MAIN reference. A full exact generation prompt is not stored.
- **Result notes:** SUPPORT expression variant. Imported from existing AI-generated assets.

---

## Prompt Section — MARINA_EXPRESSIONS_V1_F

- **Prompt ID:** `MARINA_EXPRESSIONS_V1_F`
- **Status:** APPROVED
- **Role:** SUPPORT
- **Output path:** `AI_CHARACTERS/MARINA/03_face_sheet/expressions/MARINA_expressions_v1_sheet_F_SUPPORT.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Source files used:** `MARINA_CANON_GENERATION_PROMPTS.txt`
- **Reference map:** A + C
- **Reconstruction guidance:** SUPPORT expression reference sheet F. Human-approved import. Not an active MAIN reference. A full exact generation prompt is not stored.
- **Result notes:** SUPPORT expression variant. Imported from existing AI-generated assets.

---

## Prompt Section — MARINA_OUTFIT_EVENING_PEACH_V1_A

- **Prompt ID:** `MARINA_OUTFIT_EVENING_PEACH_V1_A`
- **Status:** APPROVED
- **Role:** MAIN OUTFIT REFERENCE
- **Outfit category:** evening_dress
- **Output path:** `AI_CHARACTERS/MARINA/05_outfits/MARINA_outfit_evening_peach_v1_sheet_A_APPROVED.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Source files used:** `MARINA_CANON_GENERATION_PROMPTS.txt`
- **Reference map:** A + B
- **Reconstruction guidance:** MAIN evening outfit reference — peach dress. Human-approved import. A full exact generation prompt is not stored.
- **Result notes:** Active MAIN evening outfit canon. Imported from existing AI-generated assets.

---

## Prompt Section — MARINA_OUTFIT_EVENING_PEACH_V1_B

- **Prompt ID:** `MARINA_OUTFIT_EVENING_PEACH_V1_B`
- **Status:** APPROVED
- **Role:** SUPPORT OUTFIT REFERENCE
- **Outfit category:** evening_dress
- **Output path:** `AI_CHARACTERS/MARINA/05_outfits/MARINA_outfit_evening_peach_v1_portrait_SUPPORT.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Source files used:** `MARINA_CANON_GENERATION_PROMPTS.txt`
- **Reference map:** A + peach sheet A
- **Reconstruction guidance:** SUPPORT portrait for peach evening outfit. Human-approved import. Not an active MAIN reference. A full exact generation prompt is not stored.
- **Result notes:** SUPPORT outfit variant. Imported from existing AI-generated assets.

---

## Prompt Section — MARINA_OUTFIT_WARM_EVENING_V1_A

- **Prompt ID:** `MARINA_OUTFIT_WARM_EVENING_V1_A`
- **Status:** APPROVED
- **Role:** SUPPORT OUTFIT REFERENCE
- **Outfit category:** evening_dress
- **Output path:** `AI_CHARACTERS/MARINA/05_outfits/MARINA_outfit_warm_evening_v1_portrait_SUPPORT.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Source files used:** `MARINA_CANON_GENERATION_PROMPTS.txt`
- **Reference map:** A + peach sheet A
- **Reconstruction guidance:** SUPPORT portrait for warm evening outfit. Human-approved import. Not an active MAIN reference. A full exact generation prompt is not stored.
- **Result notes:** SUPPORT outfit variant. Imported from existing AI-generated assets.

---

## Prompt Section — MARINA_TEST01_RAINY_CAFE_V1

- **Prompt ID:** `MARINA_TEST01_RAINY_CAFE_V1`
- **Status:** APPROVED
- **Role:** MAIN
- **Verdict:** APPROVED_AS_TEST
- **Test number:** `01`
- **Scene ID:** `rainy_cafe`
- **Output path:** `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test01_rainy_cafe_v1_APPROVED.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Reference map:** active MARINA face canon + expression canon + body canon
- **Source honesty:** The exact original generation prompt and backend are unavailable. The active canon references are recorded as present-day validation anchors, not as a claim about the original generation inputs.
- **Result notes:** Human-approved existing scene image registered as MARINA Test01 (Rainy cafe); MAIN control-test output.

---

## Prompt Section — MARINA_TEST02_THEATER_MELANCHOLY_V1

- **Prompt ID:** `MARINA_TEST02_THEATER_MELANCHOLY_V1`
- **Status:** APPROVED
- **Role:** MAIN
- **Verdict:** APPROVED_AS_TEST
- **Test number:** `02`
- **Scene ID:** `theater_melancholy`
- **Output path:** `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test02_theater_melancholy_v1_APPROVED.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Reference map:** active MARINA face canon + expression canon + body canon
- **Source honesty:** The exact original generation prompt and backend are unavailable. The active canon references are recorded as present-day validation anchors, not as a claim about the original generation inputs.
- **Result notes:** Human-approved existing scene image registered as MARINA Test02 (Theater melancholy); MAIN control-test output.

---

## Prompt Section — MARINA_TEST03_EVENING_CITY_BALCONY_V1

- **Prompt ID:** `MARINA_TEST03_EVENING_CITY_BALCONY_V1`
- **Status:** APPROVED
- **Role:** MAIN
- **Verdict:** APPROVED_AS_TEST
- **Test number:** `03`
- **Scene ID:** `evening_city_balcony`
- **Output path:** `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test03_evening_city_balcony_v1_APPROVED.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Reference map:** active MARINA face canon + expression canon + body canon
- **Source honesty:** The exact original generation prompt and backend are unavailable. The active canon references are recorded as present-day validation anchors, not as a claim about the original generation inputs.
- **Result notes:** Human-approved existing scene image registered as MARINA Test03 (Evening city balcony); MAIN control-test output.

---

## Prompt Section — MARINA_TEST04_AUTUMN_STREET_PORTRAIT_V1

- **Prompt ID:** `MARINA_TEST04_AUTUMN_STREET_PORTRAIT_V1`
- **Status:** APPROVED
- **Role:** MAIN
- **Verdict:** APPROVED_AS_TEST
- **Test number:** `04`
- **Scene ID:** `autumn_street_portrait`
- **Output path:** `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test04_autumn_street_portrait_v1_APPROVED.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Reference map:** active MARINA face canon + expression canon + body canon
- **Source honesty:** The exact original generation prompt and backend are unavailable. The active canon references are recorded as present-day validation anchors, not as a claim about the original generation inputs.
- **Result notes:** Human-approved existing scene image registered as MARINA Test04 (Autumn street portrait); MAIN control-test output.

---

## Prompt Section — MARINA_TEST05_MORNING_PAJAMAS_V1

- **Prompt ID:** `MARINA_TEST05_MORNING_PAJAMAS_V1`
- **Status:** APPROVED
- **Role:** MAIN
- **Verdict:** APPROVED_AS_TEST
- **Test number:** `05`
- **Scene ID:** `morning_pajamas`
- **Output path:** `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test05_morning_pajamas_v1_APPROVED.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Reference map:** active MARINA face canon + expression canon + body canon
- **Source honesty:** The exact original generation prompt and backend are unavailable. The active canon references are recorded as present-day validation anchors, not as a claim about the original generation inputs.
- **Result notes:** Human-approved existing scene image registered as MARINA Test05 (Morning pajamas); MAIN control-test output.

---

## Prompt Section — MARINA_TEST06_WHITE_GARDEN_FORMAL_V1

- **Prompt ID:** `MARINA_TEST06_WHITE_GARDEN_FORMAL_V1`
- **Status:** APPROVED
- **Role:** MAIN
- **Verdict:** APPROVED_AS_TEST
- **Test number:** `06`
- **Scene ID:** `white_garden_formal`
- **Output path:** `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test06_white_garden_formal_v1_APPROVED.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Reference map:** active MARINA face canon + expression canon + body canon
- **Source honesty:** The exact original generation prompt and backend are unavailable. The active canon references are recorded as present-day validation anchors, not as a claim about the original generation inputs.
- **Result notes:** Human-approved existing scene image registered as MARINA Test06 (White garden formal); MAIN control-test output.

---

## Prompt Section — MARINA_TEST07_POOL_SUNSET_V1

- **Prompt ID:** `MARINA_TEST07_POOL_SUNSET_V1`
- **Status:** APPROVED
- **Role:** MAIN
- **Verdict:** APPROVED_AS_TEST
- **Test number:** `07`
- **Scene ID:** `pool_sunset`
- **Output path:** `AI_CHARACTERS/MARINA/07_generated/canon_tests/MARINA_test07_pool_sunset_v1_APPROVED.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Reference map:** active MARINA face canon + expression canon + body canon
- **Source honesty:** The exact original generation prompt and backend are unavailable. The active canon references are recorded as present-day validation anchors, not as a claim about the original generation inputs.
- **Result notes:** Human-approved existing scene image registered as MARINA Test07 (Pool sunset); MAIN control-test output.

---
*MARINA Working Scene Prompts | NCC Repository | 2026-07-18*
