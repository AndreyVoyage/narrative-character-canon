# MARINA Working Scene Prompts

## Status

PROMPT_PIPELINE_ACTIVE

## Important Source Rules

- This file stores the exact reusable prompt-kit source from `MARINA_CANON_GENERATION_PROMPTS.txt` and prompt reconstructions.
- Base canon sheet entries do **not** have an exact per-image generation prompt stored anywhere in the repository. They are marked `unknown_requires_manual_input` and only reconstruction guidance is provided.
- Future control test entries will be best-effort reconstructions built from the prompt-kit files, canon docs, and test-result notes. They will be marked `reconstructed_from_conversation_and_approved_result`.
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

*MARINA Working Scene Prompts | NCC Repository | 2026-07-18*