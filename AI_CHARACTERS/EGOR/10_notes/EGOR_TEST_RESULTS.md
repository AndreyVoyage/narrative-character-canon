# EGOR Test Results

## Status
CONTROL_TESTS_APPROVED / PROMPT_PIPELINE_ACTIVE

## Base Canon Sheets

| Test | Name | Status | Verdict | Notes |
|---|---|---|---|---|
| base | face canon A | GENERATED | APPROVED | Approved face canon sheet. Identity stable across panels. Prompt ID: EGOR_FACE_CANON_V1. |
| base | expressions A | GENERATED | APPROVED | Approved expression sheet. Human review: APPROVED_WITH_MINOR_NOTES. Expression range and identity preserved. Prompt ID: EGOR_EXPRESSIONS_V1. |
| base | body canon A | GENERATED | APPROVED | Approved body canon front/side/back. Human review: APPROVED_WITH_MINOR_NOTES. Proportions realistic and athletic. Prompt ID: EGOR_BODY_CANON_V1. |

## Approved Control Tests

| Test | Name | Status | Verdict | Notes |
|---|---|---|---|---|
| 01 | neutral portrait | GENERATED | APPROVED | Approved neutral portrait control test. Prompt ID: EGOR_TEST01_NEUTRAL_PORTRAIT_V1. |
| 02 | evening embankment | GENERATED | APPROVED | Approved evening embankment control test. Hands remain in pockets, acceptable for this environmental identity test. Prompt ID: EGOR_TEST02_EVENING_EMBANKMENT_V1. |
| 03 | sports yoga | GENERATED | APPROVED_WITH_MINOR_NOTES | Extended hand is closed into a fist; supporting arm position is slightly posed; face is slightly harder and more massive than the face canon; drift remains minor and acceptable. Prompt ID: EGOR_TEST03_SPORTS_YOGA_V1. |

## Approval Rules

* Only files explicitly approved by the user receive `_APPROVED`.
* Candidates without approval must not be treated as canon.
* Rejected images go to `08_rejected` or remain outside active canon.
* All approved generations must be recorded in `EGOR_PROMPT_RUN_LOG.jsonl`.
* Minor notes on approved tests are preserved but do not block canon status.