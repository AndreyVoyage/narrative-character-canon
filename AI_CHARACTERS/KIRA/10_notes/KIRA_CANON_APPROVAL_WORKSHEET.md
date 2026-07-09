# KIRA — Canon Approval Worksheet

> **Status:** PENDING APPROVAL
> **Character:** KIRA
> **Current Canon:** v4 (body) + face sheets — exists but NOT marked APPROVED
> **Action:** Evaluate existing canon sheets for APPROVAL or order regeneration
> **Date:** 2026-07-09
> **Critical Note:** 0 control tests exist. After canon APPROVAL, minimum 3 control tests REQUIRED.

---

## EXISTING ASSETS INVENTORY

### Face Canon
| File | Path | Status | Notes |
|------|------|--------|-------|
| Sheet A | `AI_CHARACTERS/KIRA/03_face_sheet/KIRA_face_canon_sheet_A.png` | ❌ NOT APPROVED | Primary face reference |
| Sheet B | `AI_CHARACTERS/KIRA/03_face_sheet/KIRA_face_canon_sheet_B.png` | ❌ NOT APPROVED | Secondary angles |
| Sheet C Emotional | `AI_CHARACTERS/KIRA/03_face_sheet/expressions/KIRA_expressions_v1_sheet_A_emotional.png` | ❌ NOT APPROVED | Expression range |

### Body Canon
| File | Path | Status | Notes |
|------|------|--------|-------|
| Sheet A 4views | `AI_CHARACTERS/KIRA/04_body_sheet/KIRA_BODY_CANON_v4_sheet_A_4views.png` | ❌ NOT APPROVED | 4-view body reference |
| Sheet B 4views | `AI_CHARACTERS/KIRA/04_body_sheet/KIRA_BODY_CANON_v4_sheet_B_4views.png` | ❌ NOT APPROVED | 4-view body reference |

### Outfits
| File | Path | Notes |
|------|------|-------|
| Sports Look A | `AI_CHARACTERS/KIRA/05_outfits/sports_look/KIRA_sports_look_v1_sheet_A_front_side_back.png` | Sports outfit |
| Sports Look B | `AI_CHARACTERS/KIRA/05_outfits/sports_look/KIRA_sports_look_v1_sheet_B_3q_action_portrait.png` | Action portrait |
| Evening Dress A | `AI_CHARACTERS/KIRA/05_outfits/evening_dress/KIRA_evening_dress_FINAL_sheet_A_fullbody.png` | Full body evening |
| Evening Dress B | `AI_CHARACTERS/KIRA/05_outfits/evening_dress/KIRA_evening_dress_FINAL_sheet_B_portraits.png` | Evening portraits |

### Control Tests
| # | Scene | Path | Status |
|---|-------|------|--------|
| — | **NONE EXIST** | — | ❌ MISSING |

---

## APPROVAL CHECKLIST — Face Canon

### Identity Anchors (must match across all panels)
- [ ] **Oval face with high cheekbones**
- [ ] **Slightly angular but feminine jawline**
- [ ] **Expressive brown almond eyes** with warm amber undertones
- [ ] **Double eyelids** with natural crease
- [ ] **Natural arched medium-thickness eyebrows**
- [ ] **Straight refined nose** with rounded tip
- [ ] **Full lower lip, defined cupid's bow**
- [ ] **Natural pink-peach lips**
- [ ] **Smooth skin** with natural texture
- [ ] **Light freckles** across nose and cheekbones
- [ ] **Small beauty mark above left side of upper lip**
- [ ] **Slightly asymmetrical smile** (right corner lifts higher)
- [ ] **Warm, emotionally expressive gaze** — "steel butterfly energy"

### Consistency
- [ ] Same identity across all panels (Sheet A, B)
- [ ] Expression range distinct but identity stable (Sheet C)
- [ ] No distorted features
- [ ] No drift between panels
- [ ] Beauty mark consistently on LEFT side of upper lip

### Verdict
| Decision | Action |
|----------|--------|
| **APPROVE ALL** | Rename to `_APPROVED.png`, update JSON, generate 3+ control tests |
| **APPROVE SOME** | Rename approved, note rejected, schedule regeneration |
| **REJECT ALL** | Generate new face canon v5 with adjusted prompt |

---

## APPROVAL CHECKLIST — Body Canon

### Proportion Anchors
- [ ] **168 cm scale** (medium-tall, athletic slender)
- [ ] **Former hurdler / track athlete** build
- [ ] **Narrow waist, strong athletic legs, firm glutes, developed feminine hips**
- [ ] **Toned but not bulky** — functional athletic beauty
- [ ] **Graceful posture**
- [ ] **Natural medium-full bust** — proportional, natural (NOT exaggerated)
- [ ] **Realistic adult proportions**
- [ ] **Consistent face** from canon sheets visible in body shots

### 4-View Consistency
- [ ] Front view: proportions symmetrical, face matches
- [ ] Side view: profile consistent, nose/lips/chin match face canon
- [ ] Back view: body proportions natural, hair visible
- [ ] 3/4 view: face angle natural, body proportions maintained

### Verdict
| Decision | Action |
|----------|--------|
| **APPROVE ALL** | Rename to `_APPROVED`, update JSON |
| **REJECT** | Regenerate body canon v5 |

---

## REQUIRED CONTROL TESTS (Generate after Canon APPROVAL)

Minimum 3 control tests needed:

| # | Scene | Purpose | Refs |
|---|-------|---------|------|
| 01 | Evening embankment | Cinematic outdoor, warm light | Face canon + evening outfit |
| 02 | Sports / yoga | Athletic context, body in motion | Face canon + sports outfit + body canon |
| 03 | Portrait expression | Head-and-shoulders, emotional range | Face canon + expression canon |

Optional additional tests:
| 04 | Bar / lounge | Warm interior, social context | Face canon + evening outfit |
| 05 | Sauna / spa | Relaxed body, natural proportions | Face canon + body canon |
| 06 | Outdoor walk | Natural light, full body | Face canon + body canon + casual outfit |

---

## DECISION_001 — KIRA

| Verdict | Action |
|---------|--------|
| **APPROVED** | Rename canon files to `_APPROVED.png`, generate 3+ control tests, update `KIRA_REFERENCE_PRESETS.json`, commit |
| **REJECTED** | Note reasons, regenerate face/body canon v5, create new control tests |

---

## NEXT STEPS AFTER APPROVAL

1. [ ] Rename approved canon files to `_APPROVED.png`
2. [ ] Generate 3+ control tests using approved canon as IP-Adapter reference
3. [ ] Evaluate control tests → APPROVE or REJECT
4. [ ] Update `KIRA_REFERENCE_PRESETS.json` with:
   - `identity_summary`
   - `active_canon` + `planned_canon_paths`
   - `control_tests` array (APPROVED paths)
   - `scene_presets` (mark with APPROVED refs)
5. [ ] Commit to NCC
6. [ ] Update IFPD `CHARACTER VISUAL REFERENCE MAP` with KIRA identity_summary

---

*KIRA Canon Approval Worksheet | VNE Visual Bridge | 2026-07-09*
