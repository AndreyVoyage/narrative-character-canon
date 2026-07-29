# MAKSIM Working Scene Prompts

Рабочий scene-generation reference. Используется как основа для будущих запросов
на генерацию сцен с участием MAKSIM.

Характер: не новый канон, а вспомогательный prompt reference.

Статус: PROMPT_PIPELINE_CREATED / SCENE_PROMPTS_DRAFTED (2026-07-29).

---

## Reference Selection Order (по умолчанию)

| Priority | Asset | Role | Path |
|---|---|---|---|
| 1 | MAKSIM_face_canon_v1_sheet_A_APPROVED.png | FACE_MAIN | 03_face_sheet/ |
| 2 | MAKSIM_body_canon_v1_sheet_A_front_side_back_APPROVED.png | BODY_MAIN | 04_body_sheet/ |
| 3 | MAKSIM_expressions_v1_sheet_A_APPROVED.png | EXPRESSIONS_MAIN | 03_face_sheet/expressions/ |
| 4 | MAKSIM_everyday_clothed_turnaround_v1_sheet_A_APPROVED.png | CLOTHED_BODY_SUPPORT | 04_body_sheet/clothed_references/ |
| 5 | MAKSIM_natural_motion_v1_six_pose_sheet_A_APPROVED.png | MOTION_SUPPORT | 04_body_sheet/motion_references/ |
| 6 | MAKSIM_mr_olympia_stage_v1_attempt03_six_pose_PRIMARY_REFERENCE.png | STAGE_PRIMARY | 04_body_sheet/stage_references/ |
| 7 | MAKSIM_mr_olympia_stage_v1_attempt02_secondary_REFERENCE.png | STAGE_SECONDARY | 04_body_sheet/stage_references/ |
| 8 | MAKSIM_outfit_variants_v1_six_looks_sheet_A_APPROVED.png | WARDROBE_SUPPORT | 05_outfits/scene_outfits/ |
| 9 | MAKSIM_scene_outfits_v1_six_locations_sheet_A_APPROVED.png | SCENE_OUTFIT_SUPPORT | 05_outfits/scene_outfits/ |

---

## Multi-Character Scene Rules

- **MAKSIM height: 188 cm.** Floor plane must be shared when co-located with other characters.
- Neutral footwear preferred (flat or minimal low heel); no high heels on MAKSIM.
- Camera angle: neutral eye-level or slightly above; avoid low-angle height exaggeration.
- Other character heights are set by their own canon and not inferred from MAKSIM scenes.
- In duo scenes, position characters so that height difference is visible в естественной среде.

---

## Active Body Direction (OWNER_APPROVED_CANON)

Tall classic golden-era bodybuilder, 188 cm, approximately 115 kg.

Proportions: very wide shoulders, deep massive chest, pronounced V-taper,
powerful back, large arms and forearms, controlled waist, flat non-protruding
abdomen, massive thighs, legs and calves. Stage form may be competition-dry;
everyday form remains tall, large, and athletic.

Strength without aggression. Kind, calm, emotionally stable presence.

Restrictions:
- Preserve golden-era bodybuilder identity while avoiding IFBB mass-monster extremes.
- Avoid extreme vascularity or competition-level dryness outside stage scenes.
- Never use "sporty fit build", "athletic but not bulky", "lean elegant adult build",
  "medium build", "strongman physique", "powerlifter physique", or "protruding belly".

---

## Face Direction (OWNER_APPROVED_CANON)

Full warm good-natured masculine face, calm approachable gaze.
Light subdued gray or gray-green eyes.
Dark-brown medium-length naturally wavy hair, swept back.
Short neat stubble.

Restrictions:
- Never use "warm hazel eyes" or "light brown hair".
- Preserve short neat stubble; no clean-shaven, no long beard.

---

## Scene Prompt Blocks (reconstructed)

Точные verbatim prompts не сохранялись. Все блоки ниже помечены как
`reconstructed_from_owner_approved_canon_and_approved_result`.

### Neutral Studio Reference Scene

Photorealistic full-body portrait of the same adult man, neutral grey studio
background, soft even studio lighting, 2 rows x 3 columns layout.
Adult man, tall classic golden-era bodybuilder, 188 cm, approximately 115 kg,
very wide shoulders, deep massive chest, pronounced V-taper, powerful back,
large arms and forearms, controlled waist, flat non-protruding abdomen,
massive thighs, legs and calves. Dark-brown medium-length wavy hair swept back,
short neat stubble, light subdued gray or gray-green eyes, calm approachable
expression. Wearing fitted plain dark shirt and straight dark trousers.
Neutral standing pose, natural posture.
Photorealistic, masterpiece, best quality, 8k uhd.

### Everyday Clothed Scene

Photorealistic full-body portrait of the same adult man, outdoor natural
daylight, urban street background.
Adult man, tall classic golden-era bodybuilder, 188 cm.
Visible shoulders and upper body through casual fitted clothing.
Dark-brown wavy hair, short neat stubble, calm warm expression.
Smart casual outfit: dark polo or fitted shirt, dark trousers or jeans.
Confident natural posture, friendly approachable energy.
Photorealistic, natural daylight, 8k uhd.

### Business / Formal Scene

Photorealistic full-body portrait of the same adult man, upscale office
or venue interior, warm ambient lighting.
Adult man, tall classic golden-era bodybuilder, 188 cm, commanding but
calm presence. Wearing a well-fitted dark tailored suit, white shirt,
no tie or subtle tie. Standing with composed confidence.
Dark-brown wavy hair swept back, short neat stubble, light subdued gray
or gray-green eyes.
Photorealistic, masterpiece, best quality, 8k uhd.

### Gym Scene

Photorealistic full-body portrait of the same adult man, classic gym
environment, natural gym lighting, some equipment visible.
Adult man, tall classic golden-era bodybuilder, 188 cm, in fitted
athletic wear (dark tank top or fitted tee, athletic shorts or pants).
Visible shoulder, arm and back development. Controlled flat abdomen.
Calm focused expression, strength without aggression.
Dark-brown wavy hair, short neat stubble.
Photorealistic, 8k uhd, gym lighting.

### Stage Bodybuilding Scene

Photorealistic full-body portrait of the same adult man, competition
stage, stage lighting, posing trunks (public_filtered only — full
coverage front pose).
Adult man, tall classic golden-era bodybuilder, 188 cm, approximately
115 kg, competition-dry condition. Very wide shoulders, deep massive
chest, pronounced V-taper, powerful back, large arms and forearms,
controlled waist, flat abdomen, massive thighs and calves.
Classic front double bicep or front lat spread pose.
Calm confident expression, golden-era elegance without aggression.
Dark-brown wavy hair, short neat stubble, light subdued gray or
gray-green eyes.
Photorealistic, masterpiece, best quality, 8k uhd, stage lighting.
Avoid extreme vascularity and IFBB mass-monster proportions.

### Wellness / Sauna Scale-Comparison Scene

Photorealistic full-body portrait of the same adult man, modern spa or
sauna interior, warm ambient lighting, relaxed atmosphere.
Adult man, tall classic golden-era bodybuilder, 188 cm, seated or
standing in natural relaxed posture. Wearing towel wrap (public_filtered:
full coverage from waist to mid-thigh). Visible shoulders, chest, arms
and back show tall bodybuilder proportions.
Calm, relaxed, approachable expression.
Dark-brown wavy hair, short neat stubble, light subdued gray or
gray-green eyes.
Photorealistic, 8k uhd, warm ambient spa lighting.
Note: multi-character sauna scenes with other characters are for scale
comparison only and do not redefine solo MAKSIM body canon.

---

## Safety Rules

- Fully adult character only.
- Non-explicit generation contexts only (public_filtered).
- Avoid nude, lingerie, transparent clothing, fetish framing, erotic posing.
- Preserve golden-era bodybuilder identity while avoiding IFBB mass-monster extremes.
- Do not make the character look too young.
- Record prompt_id, references, output path, verdict, and notes for every generation.

---

*MAKSIM Working Scene Prompts | NCC Visual Canon Pipeline | 2026-07-29*