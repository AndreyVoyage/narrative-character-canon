# ANDREY — Canon Approval Worksheet

> **Status:** PENDING APPROVAL
> **Character:** ANDREY (Andrey Senior)
> **Current Canon:** v1 (face + body) — exists but NOT marked APPROVED
> **Action:** Evaluate existing canon sheets for APPROVAL or order regeneration
> **Date:** 2026-07-09

---

## EXISTING ASSETS INVENTORY

### Face Canon
| File | Path | Status | Notes |
|------|------|--------|-------|
| Sheet A Basic | `AI_CHARACTERS/ANDREY/03_face_sheet/ANDREY_face_canon_v1_sheet_A_basic.png` | ❌ NOT APPROVED | Basic face reference, 8 panels |
| Sheet B Angles | `AI_CHARACTERS/ANDREY/03_face_sheet/ANDREY_face_canon_v1_sheet_B_angles.png` | ❌ NOT APPROVED | Multi-angle variations |
| Sheet C Expressions | `AI_CHARACTERS/ANDREY/03_face_sheet/expressions/ANDREY_expressions_v1_sheet_C_refined.png` | ❌ NOT APPROVED | Expression range |

### Body Canon
| File | Path | Status | Notes |
|------|------|--------|-------|
| Sheet A Front/Side/Back | `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_A_front_side_back.png` | ❌ NOT APPROVED | 3-view body reference |
| Sheet B Pose Variations | `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_B_pose_variations.png` | ❌ NOT APPROVED | Dynamic poses |

### Control Tests (6 exists, none APPROVED)
| # | Scene | Path | Status |
|---|-------|------|--------|
| 01 | Neutral studio portrait | `.../01_neutral_studio_portrait/ANDREY_test01_...` | ❌ NOT APPROVED |
| 02 | Full body blue shirt | `.../02_full_body_blue_shirt/ANDREY_test02_...` | ❌ NOT APPROVED |
| 03 | Warm bar portrait | `.../03_warm_bar_portrait/ANDREY_test03_...` | ❌ NOT APPROVED |
| 04 | Formal evening look | `.../04_formal_evening_look/ANDREY_test04_...` | ❌ NOT APPROVED |
| 05 | Sports gym identity | `.../05_sports_gym_identity/ANDREY_test05_...` | ❌ NOT APPROVED |
| 06 | Sea yacht mood | `.../06_sea_yacht_mood/ANDREY_test06_...` | ❌ NOT APPROVED |

---

## APPROVAL CHECKLIST — Face Canon

### Identity Anchors (must match across all panels)
- [ ] **Bright blue almond-shaped eyes** with subtle grey undertones
- [ ] **Rounded oval broad face** with soft contours
- [ ] **Broad forehead**
- [ ] **Straight nose bridge** with subtle width and rounded tip slightly turned down
- [ ] **Medium full natural pale pink lips**
- [ ] **Soft rounded jawline**
- [ ] **Light stubble** 2-3 days
- [ ] **Short light blonde / dark blonde hair** — slight natural temple recession, NOT bald, NOT shaved head
- [ ] **Fair smooth skin** with realistic texture
- [ ] **Faint freckles** on cheeks and nose bridge
- [ ] **Faint forehead lines** and crow's feet (mature, not aged)
- [ ] **Medium-sized ears** close to head
- [ ] **Thick muscular neck**, visible Adam's apple
- [ ] **Blue dress shirt collar** visible in framing

### Consistency
- [ ] Same identity across all 8 panels (Sheet A)
- [ ] Same identity across all angles (Sheet B)
- [ ] Expression range distinct but identity stable (Sheet C)
- [ ] No distorted features
- [ ] No drift between panels

### Verdict
| Decision | Action |
|----------|--------|
| **APPROVE ALL** | Rename files to `_APPROVED.png`, update JSON, proceed to control tests |
| **APPROVE SOME** | Rename approved, note rejected, schedule regeneration for rejected |
| **REJECT ALL** | Keep as `v1` for reference, generate `v2` with adjusted prompt |

---

## APPROVAL CHECKLIST — Body Canon

### Proportion Anchors
- [ ] **180 cm scale** (tall, athletic, strong build)
- [ ] **Broad shoulders**, thick muscular neck
- [ ] **Athletic strong build** — mature masculine, not bulky/bodybuilder
- [ ] **Realistic adult proportions**
- [ ] **Consistent face** from canon sheets visible in body shots

### Pose Variations (Sheet B)
- [ ] Standing posture confident
- [ ] Walking posture natural
- [ ] Sports pose athletic
- [ ] Formal pose elegant
- [ ] Face identity consistent across all poses

### Verdict
| Decision | Action |
|----------|--------|
| **APPROVE ALL** | Rename to `_APPROVED`, update JSON |
| **REJECT** | Regenerate with adjusted body prompt |

---

## APPROVAL CHECKLIST — Control Tests

Evaluate each test against:
- [ ] Face identity matches canon (bright blue eyes, jawline, stubble, hair)
- [ ] Body proportions match canon (athletic, broad shoulders, 180cm scale)
- [ ] Outfit/context appropriate for scene
- [ ] No distorted anatomy
- [ ] Lighting consistent with scene type
- [ ] Character age appropriate (mature adult, 38+ visual cues)

| Test | Approve? | Notes |
|------|----------|-------|
| 01 Neutral studio | ☐ | |
| 02 Full body blue shirt | ☐ | |
| 03 Warm bar portrait | ☐ | |
| 04 Formal evening | ☐ | |
| 05 Sports gym | ☐ | |
| 06 Sea yacht | ☐ | |

---

## DECISION_001 — ANDREY

| Verdict | Action |
|---------|--------|
| **APPROVED** | Rename all selected files to `_APPROVED.png`, update `ANDREY_REFERENCE_PRESETS.json`, add `identity_summary`, commit |
| **REJECTED** | Note reasons, regenerate face/body canon v2, create new control tests |

---

## NEXT STEPS AFTER APPROVAL

1. [ ] Rename approved files to `_APPROVED.png`
2. [ ] Update `ANDREY_REFERENCE_PRESETS.json` with `identity_summary` + `active_canon` + `planned_canon_paths`
3. [ ] Update `control_tests` array with APPROVED paths
4. [ ] Update `scene_presets` (already has 7, mark with APPROVED refs)
5. [ ] Commit to NCC
6. [ ] Update IFPD `CHARACTER VISUAL REFERENCE MAP` with ANDREY identity_summary

---

*ANDREY Canon Approval Worksheet | VNE Visual Bridge | 2026-07-09*
