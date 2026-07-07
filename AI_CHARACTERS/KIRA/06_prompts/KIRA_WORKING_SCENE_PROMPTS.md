# KIRA Working Scene Prompts

## Status

PROMPT_PIPELINE_ACTIVE_CORE

## Important Source Rules

- This file stores the exact reusable prompt-kit sources that already exist in `AI_CHARACTERS/KIRA/06_prompts/`.
- Base canon sheet entries do **not** have an exact per-image generation prompt stored anywhere in the repository. They are marked `unknown_requires_manual_input` and only reconstruction guidance is provided.
- Control test entries are best-effort reconstructions built from the prompt-kit files, canon docs, and test-result notes. They are marked `reconstructed_from_conversation_and_approved_result`.
- Do not treat reconstructed text as a verbatim generation log.

---

## Original Prompt Kit Sources

These four blocks are copied exactly from the existing prompt-kit files.

### KIRA_BASE_PROMPT.txt

```text
KIRA BASE PROMPT
Use for: any image generation with Kira

Kira, 26-year-old adult woman, 168 cm height, athletic slender feminine body, former hurdler / track athlete, narrow waist, strong athletic legs, firm glutes, developed feminine hips, toned but not bulky body, functional athletic beauty, graceful posture, natural medium-full bust with final visual target around 3+ size, proportional and natural.

Face canon:
oval face with high cheekbones, slightly angular but feminine jawline, expressive brown almond eyes with warm amber undertones, double eyelids with natural crease, natural arched medium-thickness eyebrows, straight refined nose with rounded tip, full lower lip, defined cupid's bow, natural pink-peach lips, smooth skin with natural texture, light freckles across nose and cheekbones, small beauty mark above left side of upper lip, slightly asymmetrical smile with right corner lifting higher.

Hair:
dark blonde / light brown shoulder-length natural wavy hair, soft volume around the face, warm highlights in cinematic light.

Character vibe:
warm, confident, athletic, feminine, emotionally expressive, independent, playful but not silly, soft but internally strong, steel butterfly energy, alive gaze, natural human expression.

Visual style:
photorealistic, cinematic, natural skin texture, realistic anatomy, high-detail editorial realism, warm natural light, realistic human proportions.

Core preservation rules:
preserve same face, same eyes, same hair, same freckles, same beauty mark, same athletic feminine body, same strong hurdler legs, same narrow waist, same natural 3+ bust target, same warm confident emotional presence.
```

### KIRA_EVENING_SCENE_PROMPT.txt

```text
KIRA EVENING SCENE PROMPT
Use for: bars, evening streets, embankment, romantic scenes, glamour scenes, cinematic portraits

Kira, 26-year-old adult woman, 168 cm, athletic slender feminine body, former hurdler / track athlete, narrow waist, strong athletic legs, firm glutes, feminine hips, natural full bust.

Important bust rule:
Final visual target is natural 3+ bust. If the image model visually reduces volume, write natural 4+ bust in the prompt to achieve final 3+ result. Bust must remain natural, proportional, elegant, not exaggerated, not artificial.

Face:
oval face, high cheekbones, expressive brown almond eyes with warm amber undertones, straight refined nose, full lower lip, defined cupid's bow, light freckles across nose and cheeks, small beauty mark above left upper lip, slightly asymmetrical smile, dark blonde shoulder-length natural wavy hair.

Outfit:
fitted red evening dress, elegant and cinematic, refined open neckline or strapless neckline, fabric emphasizing narrow waist, feminine hips, strong athletic legs, and natural full bust. High slit may reveal one strong athletic leg. The dress must look tasteful, adult, luxurious, and romantic, not vulgar.

Mood:
warm, cinematic, elegant, confident, playful, slightly mysterious, emotionally alive. Kira should look like an independent woman with soft fire in her eyes, not a passive model.

Lighting and scene:
golden hour, evening city lights, luxury bar, warm amber interior, romantic street, embankment, cinematic bokeh, natural skin texture, realistic anatomy, editorial photorealism.
```

### KIRA_SPORTS_SCENE_PROMPT.txt

```text
KIRA SPORTS SCENE PROMPT
Use for: gym, yoga, running, stretching, hurdles, warm-up, training scenes

Kira, 26-year-old adult woman, 168 cm, former hurdler / track athlete, athletic slender feminine body, narrow waist, strong functional legs, firm glutes, developed athletic thighs, toned calves, feminine hips, toned abdomen, athletic but not bulky upper body, natural medium-full bust with final visual target around 3+ size.

Important body rule:
sports top may compress the bust, but Kira must not become flat-chested or tiny-busted. Keep natural 3+ visual target while preserving believable athletic proportions.

Sports outfit:
fitted black sports top, fitted athletic shorts or leggings, clean training look, gym / yoga / running / stretching context. Clothing should show athletic form clearly without exaggeration.

Sports body:
strong hurdler legs, powerful but feminine thighs, firm glutes, narrow waist, functional athletic posture, coordinated movement, graceful body control, springy runner's legs, not bodybuilding, not crossfit-heavy, not fragile.

Face and hair:
same Kira face, expressive brown / amber eyes, oval face, high cheekbones, freckles, beauty mark above left upper lip, dark blonde natural wavy shoulder-length hair, warm confident gaze. Hair may be tied back or slightly messy for training, but identity must stay recognizable.

Mood:
focused, confident, playful, alive, athletic, disciplined, warm.
```

### KIRA_NEGATIVE_PROMPT.txt

```text
KIRA NEGATIVE PROMPT
Use for: all Kira image generations

Do not make Kira:
underage, teen-looking, childlike, too young, older than 26, wrong face, different woman, wrong identity, wrong hair color, platinum blonde hair, black hair, straight flat hair, short hair, excessive makeup, plastic skin, doll skin, anime, cartoon, 3d render, CGI look, mannequin look.

Body errors:
flat-chested, tiny-busted, too small bust, exaggerated artificial bust, implant-like bust, balloon-like bust, weak legs, thin fashion-model legs, flat glutes, narrow boyish hips, boxy torso, thick waist, fragile body, underweight body, bodybuilder body, crossfit-heavy body, huge shoulders, bulky arms, overly dry six-pack, harsh competition fitness look.

Face errors:
square masculine jaw, overfilled lips, distorted nose, wrong eye color, dead eyes, blank expression, missing freckles, missing beauty mark, overly perfect symmetrical fake face, old-looking face, excessive retouching.

Anatomy errors:
bad anatomy, distorted anatomy, extra limbs, missing limbs, bad hands, bad fingers, extra fingers, fused fingers, twisted arms, broken wrists, deformed legs, incorrect proportions, warped face, asymmetrical eyes, stretched body, unnatural pose.

Image errors:
low quality, blurry, pixelated, overexposed, underexposed, bad crop, duplicated character, text, logo, watermark, signature, frame, UI elements.

Tone errors:
vulgar, explicit, pornographic, cheap erotic look, fetish look, tasteless pose, overly aggressive sexuality, objectified mannequin pose.

Keep:
adult, tasteful, cinematic, photorealistic, elegant, natural, emotionally alive, athletic feminine Kira.
```

---

## Prompt Section — KIRA_FACE_CANON_V1_A

- **Prompt ID:** `KIRA_FACE_CANON_V1_A`
- **Status:** APPROVED
- **Output path:** `AI_CHARACTERS/KIRA/03_face_sheet/KIRA_face_canon_sheet_A.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Source files used:** `KIRA_BASE_PROMPT.txt`, `KIRA_CANON_INDEX.md.txt`, `KIRA_IDENTITY.txt.txt`
- **Reference map:** A
- **Reconstruction guidance:** This output is the active face-canon sheet. A full exact generation prompt is not stored. Any future regeneration should use `KIRA_BASE_PROMPT.txt` plus the FACE CANON section of `KIRA_CANON_INDEX.md.txt` (oval face, high cheekbones, expressive brown/amber eyes, dark blonde/light brown shoulder-length wavy hair, light freckles, beauty mark above left upper lip, full lower lip, slight asymmetrical smile, warm confident gaze).
- **Negative prompt source:** `KIRA_NEGATIVE_PROMPT.txt`
- **Result notes:** Active face identity anchor. Listed in `KIRA_CANON_INDEX.md.txt` and used as Image A in the reference map.

---

## Prompt Section — KIRA_BODY_CANON_V4_A

- **Prompt ID:** `KIRA_BODY_CANON_V4_A`
- **Status:** APPROVED
- **Output path:** `AI_CHARACTERS/KIRA/04_body_sheet/KIRA_BODY_CANON_v4_sheet_A_4views.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Source files used:** `KIRA_BASE_PROMPT.txt`, `KIRA_CANON_INDEX.md.txt`
- **Reference map:** A + B
- **Reconstruction guidance:** This output is the active body-canon sheet. A full exact generation prompt is not stored. Any future regeneration should use `KIRA_BASE_PROMPT.txt` plus the BODY CANON section of `KIRA_CANON_INDEX.md.txt` (26-year-old adult woman, 168 cm, athletic slender feminine body, former hurdler/track athlete, natural 3+ bust target, narrow waist, strong hurdler legs, firm glutes, feminine hips, not bodybuilder/not skinny fashion model).
- **Negative prompt source:** `KIRA_NEGATIVE_PROMPT.txt`
- **Result notes:** Active body/proportion anchor. Listed in `KIRA_CANON_INDEX.md.txt` and used as Image B in the reference map.

---

## Prompt Section — KIRA_EXPRESSIONS_V1_A

- **Prompt ID:** `KIRA_EXPRESSIONS_V1_A`
- **Status:** APPROVED
- **Output path:** `AI_CHARACTERS/KIRA/03_face_sheet/expressions/KIRA_expressions_v1_sheet_A_emotional.png`
- **Prompt source:** `unknown_requires_manual_input`
- **Source files used:** `KIRA_BASE_PROMPT.txt`, `KIRA_CANON_INDEX.md.txt`
- **Reference map:** A + B + C
- **Reconstruction guidance:** This output is the active expression-canon sheet. A full exact generation prompt is not stored. Any future regeneration should use `KIRA_BASE_PROMPT.txt` plus the EXPRESSIONS CANON section of `KIRA_CANON_INDEX.md.txt` (neutral, soft smile, playful smile, confident look, seductive but restrained, thoughtful, amused, slightly emotional/vulnerable; emotionally alive, natural, photorealistic, not blank/mannequin-like).
- **Negative prompt source:** `KIRA_NEGATIVE_PROMPT.txt`
- **Result notes:** Active expression reference. The canon index previously referenced a non-existent `KIRA_expressions_v1_sheet_A_basic.png`; this pipeline uses the actual file `KIRA_expressions_v1_sheet_A_emotional.png` and is used as Image C in the reference map.

---

## Prompt Section — KIRA_TEST01_EVENING_EMBANKMENT_V1_MAIN

- **Prompt ID:** `KIRA_TEST01_EVENING_EMBANKMENT_V1_MAIN`
- **Status:** APPROVED
- **Output path:** `AI_CHARACTERS/KIRA/07_generated/canon_tests/01_evening_embankment/KIRA_test01_evening_embankment_v2_MAIN.png`
- **Prompt source:** `reconstructed_from_conversation_and_approved_result`
- **Source files used:** `KIRA_BASE_PROMPT.txt`, `KIRA_EVENING_SCENE_PROMPT.txt`, `KIRA_NEGATIVE_PROMPT.txt`, `KIRA_TEST_RESULTS.md.txt`
- **Reference map:** A + B + C + D
- **Reconstructed prompt (best-effort):**

```text
Kira, 26-year-old adult woman, 168 cm, athletic slender feminine body, former hurdler / track athlete, narrow waist, strong athletic legs, firm glutes, feminine hips, natural full bust.

Face:
oval face, high cheekbones, expressive brown almond eyes with warm amber undertones, straight refined nose, full lower lip, defined cupid's bow, light freckles across nose and cheeks, small beauty mark above left upper lip, slightly asymmetrical smile, dark blonde shoulder-length natural wavy hair.

Outfit:
fitted red evening dress, elegant and cinematic, refined open neckline or strapless neckline, fabric emphasizing narrow waist, feminine hips, strong athletic legs, and natural full bust. High slit may reveal one strong athletic leg. Tasteful, adult, luxurious, romantic, not vulgar.

Scene:
Kira alone on a city embankment at evening golden hour, warm city lights reflecting on water, romantic cinematic atmosphere, soft bokeh, full-body or mid-body editorial composition.

Mood:
warm, cinematic, elegant, confident, playful, slightly mysterious, emotionally alive.

Visual style:
photorealistic, cinematic, natural skin texture, realistic anatomy, high-detail editorial realism, warm natural light.

Important rules:
Final visual target is natural 3+ bust; if the model visually reduces volume, write natural 4+ bust to achieve final 3+ result. Preserve same face, same eyes, same hair, same freckles, same beauty mark, same athletic feminine body, same strong hurdler legs, same narrow waist, same warm confident emotional presence.
```

- **Negative prompt source:** `KIRA_NEGATIVE_PROMPT.txt`
- **Result notes:** Approved main evening embankment control test. `KIRA_TEST_RESULTS.md.txt` notes: Kira face stable, evening dress works, natural 4+ prompt rule gives final 3+ effect, strong romantic evening mood, v2 is cleaner as main reference.

---

## Prompt Section — KIRA_TEST02_SPORTS_YOGA_V1_MAIN

- **Prompt ID:** `KIRA_TEST02_SPORTS_YOGA_V1_MAIN`
- **Status:** APPROVED
- **Output path:** `AI_CHARACTERS/KIRA/07_generated/canon_tests/02_sports_yoga/KIRA_test02_sports_yoga_v2_MAIN.png`
- **Prompt source:** `reconstructed_from_conversation_and_approved_result`
- **Source files used:** `KIRA_BASE_PROMPT.txt`, `KIRA_SPORTS_SCENE_PROMPT.txt`, `KIRA_NEGATIVE_PROMPT.txt`, `KIRA_TEST_RESULTS.md.txt`
- **Reference map:** A + B + C + E
- **Reconstructed prompt (best-effort):**

```text
Kira, 26-year-old adult woman, 168 cm, former hurdler / track athlete, athletic slender feminine body, narrow waist, strong functional legs, firm glutes, developed athletic thighs, toned calves, feminine hips, toned abdomen, athletic but not bulky upper body, natural medium-full bust with final visual target around 3+ size.

Face and hair:
same Kira face, expressive brown / amber eyes, oval face, high cheekbones, freckles, beauty mark above left upper lip, dark blonde natural wavy shoulder-length hair, warm confident gaze. Hair tied back or slightly messy for training.

Sports outfit:
fitted black sports top, fitted athletic shorts or leggings, clean training look.

Scene:
yoga studio or gym, Kira in a stretching / yoga pose, controlled athletic movement, full-body composition showing strong hurdler legs, narrow waist, firm glutes, and natural athletic proportions.

Mood:
focused, confident, playful, alive, athletic, disciplined, warm.

Visual style:
photorealistic, natural skin texture, realistic anatomy, premium gym / yoga studio atmosphere, soft natural or studio light, editorial realism.

Important rules:
Sports top may compress bust naturally but Kira must not become flat-chested. Keep natural 3+ visual target. Preserve face, hair, freckles, beauty mark, strong hurdler legs, narrow waist, feminine hips. Not bodybuilding, not crossfit-heavy, not fragile.
```

- **Negative prompt source:** `KIRA_NEGATIVE_PROMPT.txt`
- **Result notes:** Approved main sports/yoga control test. `KIRA_TEST_RESULTS.md.txt` notes: Kira face stable, sports outfit works, strong hurdler legs visible, waist and athletic body read correctly, sports top compresses bust naturally but does not make her flat, v2 is the strongest sports/yoga test.

---

## Prompt Section — KIRA_TEST03_PORTRAIT_EXPRESSION_V1

- **Prompt ID:** `KIRA_TEST03_PORTRAIT_EXPRESSION_V1`
- **Status:** APPROVED
- **Output path:** `AI_CHARACTERS/KIRA/07_generated/canon_tests/03_portrait_expression/KIRA_test02_bar_romance_v1_APPROVED.png`
- **Prompt source:** `reconstructed_from_conversation_and_approved_result`
- **Source files used:** `KIRA_BASE_PROMPT.txt`, `KIRA_EVENING_SCENE_PROMPT.txt`, `KIRA_NEGATIVE_PROMPT.txt`, `KIRA_TEST_RESULTS.md.txt`
- **Reference map:** A + B + C + D
- **Reconstructed prompt (best-effort):**

```text
Kira, 26-year-old adult woman, 168 cm, athletic slender feminine body, former hurdler / track athlete, narrow waist, strong athletic legs, firm glutes, feminine hips, natural full bust.

Face:
oval face, high cheekbones, expressive brown almond eyes with warm amber undertones, straight refined nose, full lower lip, defined cupid's bow, light freckles across nose and cheeks, small beauty mark above left upper lip, slightly asymmetrical smile, dark blonde shoulder-length natural wavy hair.

Outfit:
fitted red evening dress, elegant and cinematic, refined open neckline or strapless neckline, fabric emphasizing narrow waist, feminine hips, strong athletic legs, and natural full bust. Tasteful, adult, luxurious, romantic, not vulgar.

Scene:
bar or lounge interior, warm amber evening light, close-up portrait or medium shot, Kira seated or leaning at a bar, romantic relaxed atmosphere.

Mood:
warm, cinematic, elegant, confident, playful, slightly mysterious, emotionally alive. Soft fire in her eyes, independent woman, not a passive model.

Visual style:
photorealistic, cinematic, natural skin texture, realistic anatomy, high-detail editorial realism, warm amber interior light.

Important rules:
Final visual target is natural 3+ bust; if the model visually reduces volume, write natural 4+ bust to achieve final 3+ result. Preserve face, hair, freckles, beauty mark, athletic feminine body, strong hurdler legs, narrow waist, warm confident emotional presence.
```

- **Negative prompt source:** `KIRA_NEGATIVE_PROMPT.txt`
- **Result notes:** Approved portrait/bar-romance expression test. `KIRA_TEST_RESULTS.md.txt` notes: face close to Kira canon, hair/freckles/eyes/expression good, bar/romantic atmosphere works, red dress and evening mood work. Approved as a scene result, not as main identity reference. Historical filename remains `KIRA_test02_bar_romance_v1_APPROVED.png`.
