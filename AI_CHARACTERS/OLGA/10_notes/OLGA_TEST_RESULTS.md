# OLGA Test Results

## Status
BASE_CANON_APPROVED / CONTROL_TESTS_APPROVED_LOCALLY

| Test | Name | Status | Verdict | Notes |
|---|---|---|---|---|
| 01 | evening embankment | GENERATED | APPROVE | Approved environment test; identity and scale stable |
| 02 | sports yoga | GENERATED | APPROVE | Approved athletic-curvy realism; legs proportionate |
| 03 | portrait expression | GENERATED | APPROVE | Approved portrait; face identity and expression stable |
| 04 | outdoor walk with ANDREY_JUNIOR | GENERATED | APPROVE | Approved joint walk; shoulder-guiding contact safer than hand-holding |
| 05 | business interior | GENERATED | APPROVE | Approved business/interior test; face identity stable, mature business styling |
| 06 | indoor lounge conversation with ANDREY_JUNIOR | GENERATED | APPROVE | Approved indoor joint conversation; safe shoulder-guiding contact, scale contrast clear |
| 07 | confident outdoor lifestyle | NOT GENERATED | PENDING | future natural lifestyle scene |
| 08 | character poster | NOT GENERATED | PENDING | final poster-like reference |
| 09 | formal elegant cultural foyer | GENERATED | APPROVED_AS_TEST | Selected V4; indoor formal/elegant full-body MAIN scene reference |

## Approval Rules

* Only files explicitly approved by the user receive `_APPROVED`.
* Candidates without approval must not be treated as canon.
* Rejected images go to `08_rejected` or remain outside active canon.
* All approved generations must be recorded in `OLGA_PROMPT_RUN_LOG.jsonl`.

## Test 07 — pool wellness solo (public-safe)

| Test | Name | Status | Verdict | Notes |
|---|---|---|---|---|
| 07 | pool wellness solo | GENERATED | APPROVED_AS_TEST | Public-safe indoor pool/wellness solo coverage. Fully clothed athleisure version. Indoor pool/wellness environment visible. Approved as repo-safe visual coverage. Swimsuit variants v2/v3 are local-only and not repo-tracked. |

**File:** `AI_CHARACTERS/OLGA/07_generated/canon_tests/07_pool_wellness_solo/OLGA_test07_pool_wellness_solo_v1_APPROVED.png`

---

## Test 08 — DALL-E evening embankment ALT/backend variant

| Test | Name | Status | Verdict | Notes |
|---|---|---|---|---|
| 08 | dalle evening embankment | GENERATED | APPROVED_AS_TEST | Ordinary SFW evening embankment photo. Approved as DALL-E backend variant / comparison reference. Does not replace 01_evening_embankment MAIN test. |

**Test ID:** `OLGA_TEST08_DALLE_EVENING_EMBANKMENT_V1`

**Filename:** `OLGA_test08_dalle_evening_embankment_v1_APPROVED.png`

**Path:** `AI_CHARACTERS/OLGA/07_generated/canon_tests/08_dalle_evening_embankment/OLGA_test08_dalle_evening_embankment_v1_APPROVED.png`

**Verdict:** `APPROVED_AS_TEST`

**Role:** `ALT / DALL-E backend variant for evening embankment`

**Notes:**

- Ordinary SFW evening embankment photo.
- Use as DALL-E backend variant / comparison reference.
- Does not replace 01_evening_embankment MAIN test.

---

## Test 09 — formal/elegant cultural foyer

## Test 10 — neutral height scale check

**Test ID:** `OLGA_TEST10_NEUTRAL_HEIGHT_SCALE_CHECK_V1`

**Scene ID:** `neutral_height_scale_check`

**Filename:** `OLGA_test10_neutral_height_scale_check_v1_APPROVED.png`

**Path:** `AI_CHARACTERS/OLGA/07_generated/canon_tests/10_neutral_height_scale_check/OLGA_test10_neutral_height_scale_check_v1_APPROVED.png`

**Verdict:** `APPROVED_AS_TEST`

**Role:** Approved neutral full-body height/scale check MAIN scene reference.

**Coverage:** Solo OLGA full-body neutral height/environment scale check; neutral tailored dark blouse, straight dark trousers, flat shoes or minimal low heels, neutral camera.

**Difference from Test01/Test09:** Neutral full-body height calibration without evening/formal context.


**Test ID:** `OLGA_TEST09_FORMAL_ELEGANT`

**Selected Prompt ID:** `OLGA_TEST09_FORMAL_ELEGANT_V4`

**Variant label:** `REFINED`

**Scene ID:** `formal_elegant_cultural_foyer`

**Selected filename:** `OLGA_test09_formal_elegant_v4_APPROVED.png`

**Output path:** `AI_CHARACTERS/OLGA/07_generated/canon_tests/09_formal_elegant/OLGA_test09_formal_elegant_v4_APPROVED.png`

**Verdict:** `APPROVED_AS_TEST`

**Role:** Approved indoor formal/elegant full-body MAIN scene reference.

**Coverage:** Solo OLGA in an upscale indoor cultural venue, full-body formal/elegant presentation, refined dark burgundy knee-length wrap-style dress, mature face, very tall presence, preserved full mature bust, proportionate hips, natural defined waist, and elegant commanding posture.

**Difference from Test01:** Indoor cultural venue rather than outdoor evening embankment.

**Difference from Test05:** Formal cultural/event styling rather than office/business interior.

### Attempt history

- V1 — `REJECTED_BODY_CANON`: bust/chest below canon; not deployed.
- V2 — `REJECTED_PROPORTION_DRIFT`: hips and waist-to-hip contrast exaggerated; not deployed.
- V3 — `ACCEPTABLE_CANDIDATE_SUPERSEDED`: acceptable candidate but superseded; not deployed.
- V4 — `APPROVED_AS_TEST`: selected and approved for repo deployment.
