# SERGEY Test Results

## Status
BASE_CANON_APPROVED / CONTROL_TESTS_APPROVED / PROMPT_PIPELINE_ACTIVE

## Base Canon Sheets

| Test | Name | Status | Verdict | Notes |
|---|---|---|---|---|
| base | face canon A | GENERATED | APPROVED | Approved face canon sheet. 8 expression panels, identity stable. Prompt ID: SERGEY_FACE_CANON_V1. |
| base | expressions A | GENERATED | APPROVED | Approved expression sheet. 6 expression panels, identity preserved. Prompt ID: SERGEY_EXPRESSIONS_V1. |
| base | body canon A | GENERATED | APPROVED_WITH_MINOR_NOTES | Approved body canon front/side/back. Consistent front, strict side and back technical sheet. SERGEY identity, stubble, hairstyle, outfit and realistic medium-tall athletic proportions are preserved. Shoulders and arms are slightly broader and more muscular than the intended strong-but-not-bulky guardian build, but the deviation is minor and accepted. Prompt ID: SERGEY_BODY_CANON_V1. Generation ID: c456ea0f-3ed7-45b9-b166-a2c5fd01b599. |
| base | body canon B | GENERATED | APPROVED_WITH_MINOR_NOTES | Approved body pose variations sheet B. Stable SERGEY identity, proportions, outfit and guardian presence across six poses. Walking pose is slightly model-like and shoulders remain mildly broader than intended, but deviations are minor and accepted. Prompt ID: SERGEY_BODY_CANON_POSES_V1. Generation ID: 86ac5cf1-5aea-4865-8a66-b050117ef5e7. |

## Approved Control Tests

| Test | Name | Variant | Status | Verdict | Notes |
|---|---|---|---|---|---|
| 01 | neutral portrait | MAIN | GENERATED | APPROVED_WITH_MINOR_NOTES | Stable facial identity, blue-grey eyes, dark ash-blond highlighted hair, permanent trimmed stubble and calm protective presence. Shoulders and arms appear slightly more muscular and the expression slightly more model-like than intended, but deviations are minor. Prompt ID: SERGEY_TEST01_NEUTRAL_PORTRAIT_V1. |
| 02 | evening embankment | MAIN | GENERATED | APPROVED_WITH_MINOR_NOTES | Stable SERGEY identity, realistic full-body proportions, natural walking motion and calm protective presence. Expression is slightly stricter and the jacket mildly emphasizes shoulder width, but deviations are minor. Prompt ID: SERGEY_TEST02_EVENING_EMBANKMENT_V1. Generation ID: bf4f8662-8199-414d-9658-e31bd89df1c7. |
| 03 | sports yoga | MAIN | GENERATED | APPROVED_WITH_MINOR_NOTES | Stable SERGEY facial identity, blue-grey eyes, highlighted ash-blond hair, permanent trimmed stubble, correct athletic outfit and believable shoulder stretch. Arms and shoulders appear slightly more muscular and the expression slightly stricter than intended, but deviations are minor. Prompt ID: SERGEY_TEST03_SPORTS_YOGA_V1. Generation ID: 974980f5-719e-446a-b509-740a9a393e59. |

## Approval Rules

* Only files explicitly approved by the user receive `_APPROVED`.
* Candidates without approval must not be treated as canon.
* Rejected images go to `07_generated/rejected/` or remain outside active canon.
* All approved generations must be recorded in `SERGEY_PROMPT_RUN_LOG.jsonl`.
* Minor notes on approved tests are preserved but do not block canon status.
* MAIN and ALT are variant metadata fields only; they do not appear in canonical prompt IDs.