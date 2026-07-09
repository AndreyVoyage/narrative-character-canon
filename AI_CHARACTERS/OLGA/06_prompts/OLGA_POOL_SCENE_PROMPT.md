# OLGA + ANDREY_JUNIOR — Pool Scene Prompt

> **Status:** READY FOR GENERATION
> **Scene ID:** pool_first_meet_olga_andrey_01
> **Backend:** RunPod + ComfyUI + SDXL + IP-Adapter
> **Content Tier:** sfw_cinematic
> **Preset:** OLGA pool (new) — for `OLGA_REFERENCE_PRESETS.json` v1.1
> **Safety:** family-neutral, no age terms, no romantic framing, private_local only

---

## REFERENCE MAP

| Label | Path | Role |
|-------|------|------|
| REF_OLGA_FACE | `AI_CHARACTERS/OLGA/03_face_sheet/OLGA_face_canon_v1_sheet_A_APPROVED.png` | face identity |
| REF_OLGA_EXPRESSION | `AI_CHARACTERS/OLGA/03_face_sheet/expressions/OLGA_expressions_v1_sheet_A_APPROVED.png` | expression range |
| REF_OLGA_BODY | `AI_CHARACTERS/OLGA/04_body_sheet/OLGA_body_canon_v1_sheet_A_front_side_back_APPROVED.png` | body proportions |
| REF_OLGA_POSE | `AI_CHARACTERS/OLGA/04_body_sheet/OLGA_body_canon_v1_sheet_B_pose_variations_APPROVED.png` | pose reference |
| REF_AJ_FACE | `AI_CHARACTERS/ANDREY_JUNIOR/03_face_sheet/ANDREY_JUNIOR_face_canon_v1_sheet_A_APPROVED.png` | face identity |
| REF_AJ_BODY | `AI_CHARACTERS/ANDREY_JUNIOR/04_body_sheet/ANDREY_JUNIOR_body_canon_v2_sheet_A_front_side_back_APPROVED.png` | body proportions |

---

## IMAGE PROMPT (EN)

[ENVIRONMENT]
Indoor swimming pool, soft natural morning light streaming through large frosted windows, subtle water reflections on blue ceramic tiles, clean modern pool interior, calm serene atmosphere, cinematic photorealistic, masterpiece, best quality, 8k uhd

[SUBJECT 1 — OLGA]
Adult woman (olga_adult), very tall athletic curvy build, strong but feminine proportions, realistic adult scale, dark brown straight hair shoulder-blade length pulled back in clean ponytail, mature dark-brown-eyed, defined cheekbones, strong feminine jawline, beauty mark above left side of upper lip, fiery dark brown eyes, elegant dominant mature presence, wearing black athletic one-piece swimsuit, standing at pool edge on left side of frame, one hand on hip, evaluating gaze looking down toward pool water, slight predatory confident smile, weight on one leg, tall posture, head slightly tilted

[SUBJECT 2 — ANDREY_JUNIOR]
Adult male (younger_andrey_adult), short compact build, slim physique, fair skin, bright blue eyes, light blonde messy hair, soft oval face, gentle narrow jawline, clean-shaven, natural pinkness in cheeks, in swimming pool water up to chest, positioned in lower right of frame, looking up toward pool edge with awe and slight intimidation, mouth slightly open, wet hair clinging to forehead, water droplets on face and shoulders, compact scale emphasizing height difference, neutral athletic swimwear

[ACTION / INTERACTION]
She towers over him from poolside, he looks up at her from below water level, spatial tension of significant height difference, her dominance through posture and downward gaze, his vulnerability through upward gaze and open expression, no physical contact, psychological power dynamic, first meeting moment, silent evaluation

[LIGHTING / CAMERA / ATMOSPHERE]
Soft diffused natural morning light from left-side windows, subtle water caustics on pool tiles, gentle rim light on her hair and shoulders, cool blue ambient from water, warm skin tones against cool environment, shallow depth of field f/2.0, 35mm lens, cinematic color grading, film grain, photorealistic, masterpiece, best quality, 8k uhd

---

## NEGATIVE PROMPT

nsfw, explicit, nude, lingerie, child, teen, boy, junior, son, age reference, young adult, youthful, distorted anatomy, extra limbs, deformed hands, blurry, low quality, deformed face, bad proportions, mutated, watermark, text, logo, cropped, worst quality

---

## GENERATION PARAMETERS

| Parameter | Value |
|-----------|-------|
| Model | SDXL (RunPod/ComfyUI) |
| Sampler | DPM++ 2M Karras |
| Steps | 30-40 |
| CFG Scale | 7-8 |
| Resolution | 1024x768 (landscape) or 768x1024 (portrait) |
| Seed | random / user-provided |
| IP-Adapter | Load REF_OLGA_FACE + REF_AJ_FACE for identity consistency |
| ControlNet | Optional: depth map for spatial composition |

---

## OUTPUT PATH

```
AI_CHARACTERS/OLGA/07_generated/canon_tests/07_pool_meet_andrey_junior/OLGA_test07_pool_meet_andrey_junior_v1.png
```

---

## APPROVAL CHECKLIST

- [ ] Face identity matches OLGA canon (beauty mark, cheekbones, jawline, fiery eyes)
- [ ] Face identity matches AJ canon (blue eyes, blonde hair, oval face, jawline)
- [ ] Height difference visible (tall vs compact)
- [ ] Body proportions match canon for both
- [ ] No age terms in image
- [ ] No romantic/sexual framing
- [ ] Family-neutral atmosphere
- [ ] Water reflections realistic
- [ ] Lighting consistent with morning pool
- [ ] No distorted anatomy

---

## DECISION_001

| Verdict | Action |
|---------|--------|
| **APPROVED** | Rename to `_APPROVED.png`, add to `OLGA_REFERENCE_PRESETS.json` as `pool_meet_andrey_junior` preset, commit |
| **REJECTED** | Note rejection reason, regenerate with adjusted prompt, keep v1 for comparison |

---

*OLGA Pool Scene Prompt | VNE Visual Bridge | 2026-07-09*
