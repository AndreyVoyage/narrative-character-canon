# NIKA Test Results

## Status
BASE_CANON_APPROVED / CONTROL_TESTS_APPROVED / PROMPT_PIPELINE_ACTIVE

## Base Canon Sheets

| Test | Name | Status | Verdict | Notes |
|---|---|---|---|---|
| base | face canon A | GENERATED | APPROVED | Approved face canon sheet. 8 expression panels, identity stable. Prompt ID: NIKA_FACE_CANON_V1. |
| base | expressions A | GENERATED | APPROVED | Approved expression sheet. 6 expression panels, identity preserved. Prompt ID: NIKA_EXPRESSIONS_V1. |
| base | body canon A | GENERATED | APPROVED | Approved body canon front/side/back. Lean athletic hourglass silhouette preserved. Prompt ID: NIKA_BODY_CANON_V1. |
| base | body canon B | GENERATED | APPROVED | Approved body pose variations sheet B. 6 dynamic poses, identity preserved. Prompt ID: NIKA_BODY_CANON_POSES_V1. |

## Approved Control Tests

| Test | Name | Variant | Status | Verdict | Notes |
|---|---|---|---|---|---|
| 01 | neutral portrait | MAIN (v1) | GENERATED | APPROVED_WITH_MINOR_NOTES | Approved neutral controlled studio portrait. Identity and approved body proportions are stable. The original wrap-style dress draws the bust slightly toward the center; accepted as the MAIN variant. Prompt ID: NIKA_TEST01_NEUTRAL_PORTRAIT_V1. Generation ID: 49a4561b-d44e-4361-9dda-34e890360a46. |
| 01 | neutral portrait | ALT (v2) | GENERATED | APPROVED_WITH_MINOR_NOTES | Relaxed deep-V dress preserves approved bust volume with slightly wider natural separation and subtle outward orientation. The bust rests more independently without strong central compression. The deeper neckline is more sensual than MAIN but remains accepted. Prompt ID: NIKA_TEST01_NEUTRAL_PORTRAIT_V1. Generation ID: c79a2186-f655-4a3b-a512-189d3323e4ca. |
| 02 | evening embankment | MAIN | GENERATED | APPROVED_WITH_MINOR_NOTES | Approved NIKA identity and elongated silhouette preserved in a clear blue-hour waterfront scene. Walking step is slightly runway-like and the wrap neckline draws the bust somewhat toward the center, but both are acceptable. Prompt ID: NIKA_TEST02_EVENING_EMBANKMENT_V1. Generation ID: 4024945a-c982-4a61-b45b-825a0564ce03. |
| 03 | sports yoga | MAIN | GENERATED | APPROVED_WITH_MINOR_NOTES | Approved NIKA identity and elongated athletic silhouette preserved in a modern fitness-studio mobility scene. Supporting hand holds the wrist rather than the elbow. Shoulder and abdominal definition are slightly stronger than the refined canon, and the sports top mildly compresses visible bust volume. Deviations are minor and accepted. Prompt ID: NIKA_TEST03_SPORTS_YOGA_V1. Generation ID: 59854696-a32b-47ec-a80e-67ce6a828e69. |

## Approval Rules

* Only files explicitly approved by the user receive `_APPROVED`.
* Candidates without approval must not be treated as canon.
* Rejected images go to `07_generated/rejected/` or remain outside active canon.
* All approved generations must be recorded in `NIKA_PROMPT_RUN_LOG.jsonl`.
* Minor notes on approved tests are preserved but do not block canon status.
* MAIN and ALT are variant metadata fields only; they do not appear in canonical prompt IDs.