# ANDREY 3D Reference Pack

## 1. Document status

- **Character:** ANDREY Senior
- **Purpose:** Source-of-truth reference bundle for future 3D production
- **Status:** `REFERENCE_PACK_V1_REQUIRED_BLOCKOUT_REFERENCES_READY`
- **REFERENCES FOR INITIAL 3D BLOCKOUT:** `READY`
- **MORE IMAGE GENERATION REQUIRED BEFORE BLOCKOUT:** `NO`
- **3D model status:** `NOT_CREATED`
- **Blender status:** `NOT_STARTED`
- **Owner decision:**
  - **D-3D-1 — OWNER_RATIFIED** — ANDREY Senior is the first 3D pilot character
- **Remaining decisions:**
  - **D-3D-2 through D-3D-17 — PENDING_OWNER**
- **This file does not authorize modelling, rigging, rendering, or runtime integration.**
- **This file is a Phase 1 deliverable per** `ROADMAP.md` §6 and `PHASE_1_CURRENT_LAPTOP_CLOUD_PIPELINE.md` §7.

---

## 2. Authority and source hierarchy

Source order for all facts and references in this document:

1. Approved ANDREY NCC canon assets and metadata under `AI_CHARACTERS/ANDREY/` — `AGENTS.md` §1 (L1 — NCC repository visual canon)
2. Current ANDREY canon index (`AI_CHARACTERS/ANDREY/10_notes/ANDREY_CANON_INDEX.md`) and identity description (`AI_CHARACTERS/ANDREY/10_notes/ANDREY_IDENTITY.txt`)
3. Approved control-test records (Decision D-0010, `.voyage/DECISIONS.md`; `AI_CHARACTERS/ANDREY/10_notes/ANDREY_TEST_RESULTS.md`)
4. Current repository decisions and registry (`.voyage/DECISIONS.md`, `.voyage/CHARACTER_REGISTRY.md`, `.voyage/PROJECT_STATE.md`)
5. No external sources without owner approval

---

## 3. Character identity summary

**REPOSITORY FACT** — All facts extracted from `AI_CHARACTERS/ANDREY/10_notes/ANDREY_IDENTITY.txt` and `AI_CHARACTERS/ANDREY/10_notes/ANDREY_CANON_INDEX.md`.

| Attribute | Value | Source |
|---|---|---|
| Full character identifier | ANDREY Senior | `ANDREY_IDENTITY.txt` L3 |
| Adult status | Adult man, 38 years old | `ANDREY_IDENTITY.txt` L44 |
| Height | 180 cm | `ANDREY_IDENTITY.txt` L48; `ANDREY_CANON_INDEX.md` L154 |
| Weight (visual range) | 85–90 kg | `ANDREY_IDENTITY.txt` L52 |
| Build | Athletic strong build, broad muscular shoulders, muscular chest, strong upper body, thick muscular neck, strong trapezius, visible Adam's apple, strong arms (not oversized), firm torso (not belly-heavy). NOT bulky, stocky, powerlifter, bodybuilder, skinny, or fragile. | `ANDREY_IDENTITY.txt` §BODY CANON |
| Face shape | Rounded oval broad face with soft contours and broad forehead | `ANDREY_IDENTITY.txt` L70 |
| Jaw | Soft rounded jawline, not square, not sharp | `ANDREY_IDENTITY.txt` L74 |
| Eyes | Bright blue almond-shaped eyes with subtle grey undertones. Clear and expressive. Medium-set / natural spacing. | `ANDREY_IDENTITY.txt` L78–82 |
| Nose | Straight bridge with subtle width. Rounded tip, slightly turned down. No prominent hump. | `ANDREY_IDENTITY.txt` L95–98 |
| Lips | Medium fullness, natural pale pink tone | `ANDREY_IDENTITY.txt` L105–106 |
| Skin | Fair smooth skin, fine realistic texture, faint barely visible freckles on cheeks and nose bridge, faint horizontal forehead wrinkles, faint crow's feet. NOT plastic, NOT CGI. | `ANDREY_IDENTITY.txt` L110–122 |
| Facial hair | Light stubble, 2–3 days growth. Covers jawline, upper lip, chin. Not full beard. Not clean-shaven. Not heavy beard. | `ANDREY_IDENTITY.txt` L126–130 |
| Hair colour | Short light blonde / dark blonde hair | `ANDREY_IDENTITY.txt` L142 |
| Hair style | Evenly cropped short hair. Natural male pattern. Slight natural temple recession. Short textured top. NOT bald, NOT shaved, NOT severe receding, NOT sparse, NOT dense thick model hair. | `ANDREY_IDENTITY.txt` §HAIR CANON |
| Ears | Medium-sized ears, close to head, well-defined helix | `ANDREY_IDENTITY.txt` L134 |
| Canonical posture | Upright, calm, confident, shoulders open, mature masculine stance | `ANDREY_IDENTITY.txt` §EXPRESSION CANON |
| Canonical expression baseline | Calm, confident, emotionally controlled. Neutral focused look with warm but focused gaze. | `ANDREY_IDENTITY.txt` L250–252 |
| **Identity non-negotiables** | 38 years old; adult man; 180 cm; 85–90 kg visual range; athletic strong build; broad shoulders; muscular chest; thick muscular neck; bright blue eyes; short light blonde/dark blonde hair; slight temple recession; light stubble 2–3 days; rounded oval broad face; soft rounded jawline; fair skin; faint freckles; subtle forehead lines; faint crow's feet | `ANDREY_IDENTITY.txt` §GENERATION RULES |

**Note on weight interpretation:** `ANDREY_IDENTITY.txt` L34–38 states that VNE visual anchors sometimes describe ANDREY as 92–95 kg, but NCC resolves to 85–90 kg visual range for generation. This NCC resolution is authoritative for 3D work per `AGENTS.md` §1 (L1 NCC visual canon wins over L2 VNE in visual appearance).

---

## 4. Approved face-modelling references

All paths are repository-relative. All files are Git-tracked (Git LFS). All are approved per `ANDREY_CANON_INDEX.md` and Decision D-0010.

### F1 — Face canon Sheet A (basic expressions)

| Field | Value |
|---|---|
| **Path** | `AI_CHARACTERS/ANDREY/03_face_sheet/ANDREY_face_canon_v1_sheet_A_basic.png` |
| **Tracked** | YES (Git LFS) |
| **Approval status** | APPROVED — ACTIVE FACE CANON / BASIC EXPRESSIONS |
| **Prompt ID** | `ANDREY_FACE_CANON_V1_A_BASIC` |
| **View / role** | **FACE_MAIN** — Front-view face canon sheet with multiple panels |
| **Modelling use** | Primary face identity reference. Frontal proportions, eye shape, nose shape, lip shape, jaw width, face width, ear placement, forehead height. |
| **Known limitation** | Multi-panel composition. Individual panels may be lower resolution than a dedicated single-view reference. |
| **SHA-256** | `cb6619388623abe8167787c3f2869470b9d8f4427ce6f0a0f53faca82e72f3d1` |
| **Provenance source** | AI-generated, cloud service. Registered in `ANDREY_PROMPT_RUN_LOG.jsonl`. |

### F2 — Face canon Sheet B (multi-angle)

| Field | Value |
|---|---|
| **Path** | `AI_CHARACTERS/ANDREY/03_face_sheet/ANDREY_face_canon_v1_sheet_B_angles.png` |
| **Tracked** | YES (Git LFS) |
| **Approval status** | APPROVED — ACTIVE FACE CANON / MULTI-ANGLE |
| **Prompt ID** | `ANDREY_FACE_CANON_V1_B_ANGLES` |
| **View / role** | **FACE_ANGLES** — Front, 3/4 left, 3/4 right, left profile, right profile, slight down/up gaze |
| **Modelling use** | Head profile and three-quarter views. Ear shape and placement. Hairline from multiple angles. Nose profile. Jawline contour from side. Neck thickness. |
| **Known limitation** | Multi-panel sheet. Profile views within a composed sheet, not isolated. |
| **SHA-256** | `b208514046049b38c90da1b5fafe4121c12dc22273c8dc4d6c61b11178f52b2a` |
| **Provenance source** | AI-generated, cloud service. Registered in `ANDREY_PROMPT_RUN_LOG.jsonl`. |

### F3 — Face closeup (raw reference, supporting)

| Field | Value |
|---|---|
| **Path** | `AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_01_face_closeup_blue_shirt.png` |
| **Tracked** | YES (Git LFS) |
| **Approval status** | APPROVED as supporting reference per `ANDREY_CANON_INDEX.md` |
| **View / role** | **FACE_DETAIL_SUPPORT** — Close-up face detail, skin texture, eye colour, stubble |
| **Known limitation** | RAW status. Dirty worktree — hash not computed. |
| **SHA-256** | **NOT COMPUTED** — Dirty worktree. |
| **Provenance source** | AI-generated, cloud service. Listed in `ANDREY_RAW_FILE_MAP.md`. |

### F4 — Identity anchor (raw reference)

| Field | Value |
|---|---|
| **Path** | `AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_05_main_identity_sheet_blue_shirt.png` |
| **Tracked** | YES (Git LFS) |
| **Approval status** | APPROVED as core identity reference per `ANDREY_IDENTITY.txt` §RAW REFERENCE PRIORITY |
| **View / role** | **IDENTITY_ANCHOR** — Face + upper body with blue shirt |
| **Known limitation** | RAW status. Dirty worktree — hash not computed. |
| **SHA-256** | **NOT COMPUTED** — Dirty worktree. |
| **Provenance source** | AI-generated, cloud service. Listed in `ANDREY_RAW_FILE_MAP.md`. |

---

## 5. Approved body-modelling references

### B1 — Body canon Sheet A (technical views)

| Field | Value |
|---|---|
| **Path** | `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_A_front_side_back.png` |
| **Tracked** | YES (Git LFS) |
| **Approval status** | APPROVED — ACTIVE BODY CANON / TECHNICAL FRONT SIDE BACK 3Q |
| **Prompt ID** | `ANDREY_BODY_CANON_V1_A_FRONT_SIDE_BACK` |
| **Role** | **BODY_MAIN** — Front, side, back, 3/4 views |
| **Modelling use** | Primary body proportion reference. Shoulder width, chest, waist-to-shoulder ratio, torso-to-leg ratio, neck thickness, posture, silhouette. |
| **Clothing obstruction** | Blue dress shirt covers torso, shoulders, upper arms. No bare torso anatomy. |
| **Known limitation** | Arms at sides — not A-pose or T-pose. |
| **SHA-256** | `062bf9408576d61b727907aaee786e7b9518e7f849a76a0b2cb74aabf10318e0` |
| **Provenance source** | AI-generated, cloud service. Registered in `ANDREY_PROMPT_RUN_LOG.jsonl`. |

### B2 — Body canon Sheet B (pose variations)

| Field | Value |
|---|---|
| **Path** | `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_B_pose_variations.png` |
| **Tracked** | YES (Git LFS) |
| **Approval status** | APPROVED — ACTIVE BODY CANON / POSE VARIATIONS |
| **Prompt ID** | `ANDREY_BODY_CANON_V1_B_POSE_VARIATIONS` |
| **Role** | **POSE_MAIN** — Standing, walking stride, seated, 3/4 turn |
| **Modelling use** | Pose reference for rig testing. Walking stride for gait analysis. Limb proportions. |
| **Known limitation** | Static poses only. No frame-by-frame motion. Clothing obscures joints. |
| **SHA-256** | `6daa00c2d54f9dc7f708b2dbfac91ec775c06792de2d34c792deec8e1b7963cf` |
| **Provenance source** | AI-generated, cloud service. Registered in `ANDREY_PROMPT_RUN_LOG.jsonl`. |

### B3 — Body identity (raw reference, supporting)

| Field | Value |
|---|---|
| **Path** | `AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_11_body_identity_sheet_blue_shirt.png` |
| **Tracked** | YES (Git LFS) |
| **Approval status** | APPROVED as supporting reference per `ANDREY_CANON_INDEX.md` |
| **Role** | **BODY_SUPPORT** — Full-body blue-shirt identity reference |
| **Known limitation** | RAW status. Dirty worktree — hash not computed. |
| **SHA-256** | **NOT COMPUTED** — Dirty worktree. |
| **Provenance source** | AI-generated, cloud service. Listed in `ANDREY_RAW_FILE_MAP.md`. |

### B4 — ANDREY 3D A-pose turnaround

| Field | Value |
|---|---|
| **Path** | `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_3D_reference_v1_sheet_A_apose_turnaround.png` |
| **Tracked** | UNTRACKED_PENDING_CONTROLLED_COMMIT (new file, 2026-07-31) |
| **Approval status** | APPROVED_WITH_MINOR_NOTES |
| **Owner approval** | true |
| **Prompt ID** | `ANDREY_3D_REF_V1_A_APOSE_TURNAROUND_V2_CORRECTED` |
| **Gen ID** | `967b1c13-0980-4634-ab7c-0518030b7d92` |
| **Role** | **BODY_SUPPORT_3D_REFERENCE** |
| **Dimensions** | 1672 × 941 |
| **SHA-256** | `5b94f25d724966c8d5abcee9510a5aaeb76015960f74fafa335e77f71aa4cde4` |
| **Modelling use** | Primary A-pose reference for 3D blockout: front, strict side profile, and rear views with arms separated ~30° from torso. Shoulder articulation, armpit topology, arm circumference, waist silhouette, and body proportions visible. |
| **Known minor notes** | Height readability accepted. Lower body and glute proportions accepted. A-pose is usable for 3D modelling. |
| **Important** | Technical grey clothing is NOT outfit canon. Does NOT replace B1 or B2. This is a 3D modelling reference only. |
| **Gap** | GAP-002 — CLOSED_READY |
| **Provenance source** | AI-generated, 2026-07-31. OpenAI via ChatGPT. Registered in `ANDREY_PROMPT_RUN_LOG.jsonl`. |

### H1 — ANDREY hand reference sheet

| Field | Value |
|---|---|
| **Path** | `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_3D_reference_v1_sheet_B_hands.png` |
| **Tracked** | UNTRACKED_PENDING_CONTROLLED_COMMIT (new file, 2026-07-31) |
| **Approval status** | APPROVED_WITH_MINOR_NOTES |
| **Owner approval** | true |
| **Prompt ID** | `ANDREY_3D_REF_V1_B_HANDS` |
| **Gen ID** | `fe8f2aee-df42-4fef-b36d-424bca0a4131` |
| **Role** | **HAND_SUPPORT_3D_REFERENCE** |
| **Dimensions** | 1448 × 1086 |
| **SHA-256** | `ffb62b3d4e9f62d24edc1ee1d86d7317ca9f4e1579f6a88bdb53db02d1cbbff0` |
| **Visible coverage** | Palms, backs, spread fingers, side views |
| **Modelling use** | Hand anatomy reference for 3D sculpting: finger proportions, knuckle placement, nail shape, palm structure. |
| **Known limitation** | Exact physical hand scale not established. Derive from A-pose body reference (B4). Avoid exaggerating veins and tendons. |
| **Gap** | GAP-001 — CLOSED_READY |
| **Provenance source** | AI-generated, 2026-07-31. OpenAI via ChatGPT. Registered in `ANDREY_PROMPT_RUN_LOG.jsonl`. |

---

## 6. Approved expression references

### E1 — Expression canon Sheet C (refined)

| Field | Value |
|---|---|
| **Path** | `AI_CHARACTERS/ANDREY/03_face_sheet/expressions/ANDREY_expressions_v1_sheet_C_refined.png` |
| **Tracked** | YES (Git LFS) |
| **Approval status** | APPROVED — ACTIVE EXPRESSIONS CANON / REFINED |
| **Prompt ID** | `ANDREY_EXPRESSIONS_V1_C_REFINED` |
| **Role** | **EXPRESSIONS_MAIN** — Head-and-shoulders multi-panel sheet |
| **SHA-256** | `a781686454245ef19d7a260bddad2b9bed81f86d82ff1bca0e39400433675b44` |
| **Provenance source** | AI-generated, cloud service. Registered in `ANDREY_PROMPT_RUN_LOG.jsonl`. |

### Expression-to-blendshape map

**RECOMMENDATION — NOT OWNER-RATIFIED** — D-3D-9 PENDING_OWNER.

| Expression | Proposed blendshape name | Ratified? |
|---|---|---|
| Neutral | `neutral` | NO |
| Warm smile | `warm_smile` | NO |
| Confident smirk | `confident_smirk` | NO |
| Serious | `serious` | NO |
| Protective | `protective` | NO |
| Surprise | `surprise` | NO |

---

## 7. Approved outfit references

### A. APPROVED CANON FOR PILOT

| ID | Path | Role | SHA-256 |
|---|---|---|---|
| **O1** | `AI_CHARACTERS/ANDREY/07_generated/canon_tests/02_full_body_blue_shirt/ANDREY_test02_full_body_blue_shirt_studio_v1.png` | **CASUAL_OUTFIT_MAIN** | `1800ec8a11a51d5a026c99ccb537a552552c2d9b7a7c7bd880c12dce3ef0cfbc` |

**Base outfit:** Blue dress shirt, rolled-up sleeves, slightly open collar, dark navy trousers, brown leather belt, brown leather shoes. Casual elegant masculine.

### B. CANDIDATE — NOT AUTHORIZED FOR 3D

| ID | Path | Role | SHA-256 |
|---|---|---|---|
| **O2** | `AI_CHARACTERS/ANDREY/07_generated/canon_tests/04_formal_evening_look/ANDREY_test04_formal_evening_look_v1.png` | Formal evening (dark navy suit) | `d010d2be14c7d5ce956ebbb1d52180ba85ccd42267f11679a2cf9c8b08a7bf5a` |
| **O3** | `AI_CHARACTERS/ANDREY/07_generated/canon_tests/05_sports_gym_identity/ANDREY_test05_sports_gym_identity_v1.png` | Sports/gym (black athletic) | `c6c88c866b0b61e562e004527ed40759395e97d9990a91a63e6add733bf5301d` |

### C. REJECTED OR OBSOLETE — MUST NOT USE

| Path | Reason |
|---|---|
| `AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_12_kling_face_closeup_REFERENCE_ONLY.jpg` | REFERENCE_ONLY / NOT CANON |
| `AI_CHARACTERS/ANDREY/04_body_sheet/candidates/ANDREY_body_canon_v1_sheet_A_front_side_back_candidate_02.png` | CANDIDATE — duplicate |

---

## 8. Hair reference

**REPOSITORY FACT** — All hair facts from `ANDREY_IDENTITY.txt` §HAIR CANON.

| Attribute | Value |
|---|---|
| Colour | Short light blonde / dark blonde |
| Style | Evenly cropped short hair, natural male pattern, short textured top |
| Hairline | Slight natural temple recession — key identity feature |
| Density | Natural density. NOT bald, NOT shaved, NOT severe receding, NOT sparse, NOT dense model hair |
| Approved source paths | F1, F2 (profile views show hairline), E1 |
| Missing close-up | Hairline close-up DEFERRED — existing F2 coverage accepted for pilot (GAP-003) |

**PENDING_OWNER:** D-3D-12 (hair strategy).

---

## 9. Materials and texture references

| Surface | Status | Source |
|---|---|---|
| Face skin | **PARTIAL** | `ANDREY_IDENTITY.txt` + visual in F1, F2, E1, V1. Skin close-up DEFERRED_UNTIL_TEXTURING (GAP-004). |
| Body skin | **PARTIAL** | Clothed in B1, B2. |
| Eyes | **PARTIAL** | F1, F2, F4, V1. |
| Hair | **PARTIAL** | §8. |
| Shirt (blue dress) | **PARTIAL** | O1, B1, B2, V2. |
| Trousers (dark navy) | **PARTIAL** | B1, B2, V2, O1. |
| Belt (brown leather) | **MISSING** | Described, not detailed. |
| Shoes (brown leather) | **MISSING** | Described, not detailed. |

---

## 10. Hands and feet

| Coverage | Status | Evidence |
|---|---|---|
| Hand close-ups | **READY** | H1 — palms, backs, spread fingers, side views. APPROVED_WITH_MINOR_NOTES. GAP-001 CLOSED_READY. |
| Finger anatomy | **READY_FOR_BLOCKOUT** | H1. Exact physical scale not established — derive from B4. |
| Feet visibility | **MISSING** | Shoes described. No bare foot reference. Feet DEFERRED for pilot. |
| Shoe obstruction | **YES** | Shoes cover feet. Bare foot anatomy not referenced. |

---

## 11. Neutral modelling pose

| Pose type | Status | Evidence |
|---|---|---|
| Standing neutral (front) | **READY** | B1 front panel. |
| Standing neutral (side) | **READY** | B1 side panel. |
| Standing neutral (back) | **READY** | B1 back panel. |
| A-pose (arms separated ~30°) | **READY** | B4 — A-pose turnaround. Front, side, rear views. Arms separated from torso. GAP-002 CLOSED_READY. |
| T-pose (arms horizontal) | **NOT REQUIRED** | A-pose sufficient. T-pose not generated. |
| Arms separated from torso | **READY** | B4. |

---

## 12. Height and scale specification

| Property | Value | Source |
|---|---|---|
| Height | 180 cm | `ANDREY_IDENTITY.txt` L48 |
| Weight (visual range) | 85–90 kg | `ANDREY_IDENTITY.txt` L52 |
| Body type | Athletic strong build | `ANDREY_IDENTITY.txt` L56 |
| Joint scale reference | KIRA = 168 cm barefoot (D-0013). ANDREY ≈ 1.07× KIRA. | `.voyage/DECISIONS.md` |

**RECOMMENDATION — NOT OWNER-RATIFIED:** 1 Blender unit = 1 metre. ANDREY = 1.80 BU.

---

## 13. Identity-validation reference set

| ID | Path | SHA-256 | Purpose |
|---|---|---|---|
| **V1** | `AI_CHARACTERS/ANDREY/07_generated/canon_tests/01_neutral_studio_portrait/ANDREY_test01_neutral_studio_portrait_v1.png` | `fceb311bde72fbaac422d622e22480669e48dc123b5826c74d48ba83476f96a9` | Face-identity validation |
| **V2** | `AI_CHARACTERS/ANDREY/07_generated/canon_tests/02_full_body_blue_shirt/ANDREY_test02_full_body_blue_shirt_studio_v1.png` | `1800ec8a11a51d5a026c99ccb537a552552c2d9b7a7c7bd880c12dce3ef0cfbc` | Full-body casual outfit validation |
| **V3** | `AI_CHARACTERS/ANDREY/07_generated/canon_tests/03_warm_bar_portrait/ANDREY_test03_warm_bar_portrait_v1.png` | `4433bcd918dbd99bbdf66bac351992383bdf68fc4f8e2a0bd85385e9eccf7f32` | Environmental face validation |
| **V4** | `AI_CHARACTERS/ANDREY/07_generated/canon_tests/06_sea_yacht_mood/ANDREY_test06_sea_yacht_mood_scene_v1.png` | `be478a950085b4b9ee123c21787153300d7b991caa7d3c290b65c11c7c32addc` | Outdoor identity validation |

**PENDING_OWNER:** D-3D-16 (identity acceptance test method).

---

## 14. Excluded sources

| Path / Class | Exclusion reason |
|---|---|
| `AI_CHARACTERS/ANDREY/01_refs_raw/ANDREY_RAW_12_kling_face_closeup_REFERENCE_ONLY.jpg` | REJECTED / NOT CANON |
| `AI_CHARACTERS/ANDREY/04_body_sheet/candidates/` | CANDIDATE — NOT ACTIVE CANON |
| `AI_CHARACTERS/ANDREY/07_generated/drafts/` | DRAFT — NOT APPROVED |
| `AI_CHARACTERS/ANDREY/07_generated/rejected/` | REJECTED |
| `AI_CHARACTERS/ANDREY/05_outfits/candidates/` | CANDIDATE |
| Untracked files in `AI_CHARACTERS/ANDREY/` (except B4 and H1) | UNTRACKED — NOT APPROVED |
| Any asset from another character folder | CROSS-CONTAMINATION |

---

## 15. Coverage matrix

| Category | Status | Source IDs | Blocks modelling | Owner action required |
|---|---|---|---|---|
| Face front | **READY** | F1, F4 | NO | None |
| Face three-quarter | **READY** | F2 | NO | None |
| Side profile | **PARTIAL** | F2 | NO | Accept or generate head-only profile |
| Neutral face | **READY** | F1, E1 | NO | None |
| Expression range | **READY** | E1 | NO | Ratify D-3D-9 |
| Body front | **READY** | B1, B4 | NO | None |
| Body side | **READY** | B1, B4 | NO | None |
| Body rear | **READY** | B1, B4 | NO | None |
| Height | **READY** | Text canon | NO | None |
| Body proportions | **READY** | B1, B2, B4 | NO | None |
| Hands | **READY** | H1 | NO | None |
| Feet | **MISSING** | — | NO | Deferred |
| Hairline | **PARTIAL** | F1, F2 | NO | Deferred (GAP-003) |
| Skin close-up | **PARTIAL** | F1, V1 | NO | Deferred (GAP-004) |
| Base outfit | **READY** | O1 | NO | Ratify D-3D-11 |
| Motion reference | **MISSING** | — | PARTIAL | Generate or accept B2 static poses |
| Identity-validation set | **READY** | V1–V4 | NO | Ratify D-3D-16 |
| Neutral A-pose | **READY** | B4 | NO | None |

**Summary:** 13 READY, 3 PARTIAL, 2 MISSING.

---

## 16. Missing-reference queue

### GAP-001 — Hand close-up
**Status:** `CLOSED_READY` — Owner-approved reference: H1 (`ANDREY_3D_reference_v1_sheet_B_hands.png`)

### GAP-002 — Neutral A-pose reference
**Status:** `CLOSED_READY` — Owner-approved reference: B4 (`ANDREY_3D_reference_v1_sheet_A_apose_turnaround.png`)

### GAP-003 — Hairline close-up
**Status:** `DEFERRED` — Existing F2 coverage accepted for initial pilot. Dedicated hairline close-up not required before blockout.

### GAP-004 — Skin texture close-up
**Status:** `DEFERRED_UNTIL_TEXTURING` — Existing F1/V1 coverage accepted for initial pilot. Dedicated skin macro deferred until texture/material authoring phase.

---

## 17. Proposed future 3D outputs

**ALL ITEMS: NOT_CREATED / NOT_AUTHORIZED.**

| Output | Status |
|---|---|
| Canonical `.blend` | `NOT_CREATED / NOT_AUTHORIZED` |
| Blockout | `NOT_CREATED / NOT_AUTHORIZED` |
| Sculpt | `NOT_CREATED / NOT_AUTHORIZED` |
| Retopologized mesh | `NOT_CREATED / NOT_AUTHORIZED` |
| UV layout | `NOT_CREATED / NOT_AUTHORIZED` |
| Textures | `NOT_CREATED / NOT_AUTHORIZED` |
| Materials | `NOT_CREATED / NOT_AUTHORIZED` |
| Rig | `NOT_CREATED / NOT_AUTHORIZED` |
| Facial controls | `NOT_CREATED / NOT_AUTHORIZED` |
| Animation tests | `NOT_CREATED / NOT_AUTHORIZED` |
| GLB/FBX exports | `NOT_CREATED / NOT_AUTHORIZED` |
| Turntable renders | `NOT_CREATED / NOT_AUTHORIZED` |
| Identity-comparison report | `NOT_CREATED / NOT_AUTHORIZED` |

---

## 18. Decision gates

### RATIFIED
- **D-3D-1** — OWNER_RATIFIED — ANDREY Senior pilot character

### PENDING_OWNER
D-3D-2 through D-3D-17.

### Minimum ratification before modelling
1. D-3D-2 (modelling route)
2. D-3D-14 (local vs. cloud)
3. D-3D-13 (realism level)
4. D-3D-5 (target topology)
5. D-3D-4 (tool chain boundary)
6. D-3D-15 (licensing)
7. D-3D-3 (base-mesh source)

---

## 19. Exact next action

**REFERENCES FOR INITIAL 3D BLOCKOUT: READY**
**MORE IMAGE GENERATION REQUIRED BEFORE BLOCKOUT: NO**

**Recommendation:** Ratify the minimum modelling decisions required before the first Blender blockout, beginning with **D-3D-2 — modelling route**.

GAP-001 and GAP-002 are closed. GAP-003 and GAP-004 are deferred. No additional 2D reference generation is required before initial 3D blockout of ANDREY Senior.

---

## Appendix A — SHA-256 reference summary

| ID | Path | SHA-256 |
|---|---|---|
| F1 | `AI_CHARACTERS/ANDREY/03_face_sheet/ANDREY_face_canon_v1_sheet_A_basic.png` | `cb6619388623abe8167787c3f2869470b9d8f4427ce6f0a0f53faca82e72f3d1` |
| F2 | `AI_CHARACTERS/ANDREY/03_face_sheet/ANDREY_face_canon_v1_sheet_B_angles.png` | `b208514046049b38c90da1b5fafe4121c12dc22273c8dc4d6c61b11178f52b2a` |
| E1 | `AI_CHARACTERS/ANDREY/03_face_sheet/expressions/ANDREY_expressions_v1_sheet_C_refined.png` | `a781686454245ef19d7a260bddad2b9bed81f86d82ff1bca0e39400433675b44` |
| B1 | `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_A_front_side_back.png` | `062bf9408576d61b727907aaee786e7b9518e7f849a76a0b2cb74aabf10318e0` |
| B2 | `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_body_canon_v1_sheet_B_pose_variations.png` | `6daa00c2d54f9dc7f708b2dbfac91ec775c06792de2d34c792deec8e1b7963cf` |
| **B4** | `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_3D_reference_v1_sheet_A_apose_turnaround.png` | `5b94f25d724966c8d5abcee9510a5aaeb76015960f74fafa335e77f71aa4cde4` |
| **H1** | `AI_CHARACTERS/ANDREY/04_body_sheet/ANDREY_3D_reference_v1_sheet_B_hands.png` | `ffb62b3d4e9f62d24edc1ee1d86d7317ca9f4e1579f6a88bdb53db02d1cbbff0` |
| V1 | `.../01_neutral_studio_portrait/ANDREY_test01_neutral_studio_portrait_v1.png` | `fceb311bde72fbaac422d622e22480669e48dc123b5826c74d48ba83476f96a9` |
| V2/O1 | `.../02_full_body_blue_shirt/ANDREY_test02_full_body_blue_shirt_studio_v1.png` | `1800ec8a11a51d5a026c99ccb537a552552c2d9b7a7c7bd880c12dce3ef0cfbc` |
| V3 | `.../03_warm_bar_portrait/ANDREY_test03_warm_bar_portrait_v1.png` | `4433bcd918dbd99bbdf66bac351992383bdf68fc4f8e2a0bd85385e9eccf7f32` |
| O2 | `.../04_formal_evening_look/ANDREY_test04_formal_evening_look_v1.png` | `d010d2be14c7d5ce956ebbb1d52180ba85ccd42267f11679a2cf9c8b08a7bf5a` |
| O3 | `.../05_sports_gym_identity/ANDREY_test05_sports_gym_identity_v1.png` | `c6c88c866b0b61e562e004527ed40759395e97d9990a91a63e6add733bf5301d` |
| V4 | `.../06_sea_yacht_mood/ANDREY_test06_sea_yacht_mood_scene_v1.png` | `be478a950085b4b9ee123c21787153300d7b991caa7d3c290b65c11c7c32addc` |

---

## Appendix B — Source document index

| Document | Path |
|---|---|
| ANDREY Identity | `AI_CHARACTERS/ANDREY/10_notes/ANDREY_IDENTITY.txt` |
| ANDREY Canon Index | `AI_CHARACTERS/ANDREY/10_notes/ANDREY_CANON_INDEX.md` |
| ANDREY Reference Presets | `AI_CHARACTERS/ANDREY/10_notes/ANDREY_REFERENCE_PRESETS.json` |
| ANDREY Prompt Run Log | `AI_CHARACTERS/ANDREY/06_prompts/ANDREY_PROMPT_RUN_LOG.jsonl` |
| ANDREY Working Scene Prompts | `AI_CHARACTERS/ANDREY/06_prompts/ANDREY_WORKING_SCENE_PROMPTS.md` |
| ROADMAP.md | `ROADMAP.md` |
| Phase 1 Pipeline | `PHASE_1_CURRENT_LAPTOP_CLOUD_PIPELINE.md` |
| Phase 2 Pipeline | `PHASE_2_LOCAL_AI_WORKSTATION_PIPELINE.md` |
| CHARACTER_REGISTRY | `.voyage/CHARACTER_REGISTRY.md` |
| DECISIONS | `.voyage/DECISIONS.md` |