# CURRENT_TASK

## Previous task

**Task ID:** `NCC-DALLE-17-GENERATION-2026-07-09`

**Final status:** `CLOSED_REDESIGNED`

**Closure reason:** The original blind 17-image generation list was found to duplicate existing approved visual coverage. It was replaced by a coverage-based workflow.

### Completed results from the redesigned work

- OLGA pool/wellness public-safe v1 deployed and pushed in commit `6229e0d`.
- OLGA swimsuit pool/wellness v2/v3 retained in `LOCAL_STORAGE` by human decision B.
- OLGA DALL-E evening embankment ALT deployed and pushed in commit `8e07904`.
- `01_evening_embankment` remains MAIN.
- `08_dalle_evening_embankment` is ALT / DALL-E backend variant.
- Empty duplicate `09_yoga_studio` folder was removed.

### Superseded rule

Do not continue the original 17-image count mechanically.

### Active workflow rule

Before every future generation:

1. Audit existing visual coverage.
2. Extract exact character anchors from repo canon files.
3. Select explicit reference images.
4. Prepare `prompt_id`, `reference_paths`, `output_path`, and storage tier.
5. Generate only after the scene is confirmed missing.
6. Record APPROVED / REJECTED / DRAFT result.

---

## Active task

**Task ID:** `NCC-OLGA-FORMAL-ELEGANT-REFERENCE-PREFLIGHT-2026-07-10`

**Status:** `READY_FOR_READONLY_PREFLIGHT`

### Goal

Determine whether OLGA formal/elegant coverage is truly missing and prepare the exact reference selection and canon anchor pack before any generation.

### Scope

- Read OLGA canon files.
- Inspect existing OLGA face/body/outfit/generated references.
- Inspect existing formal/elegant or adjacent scenes.
- Determine best reference images.
- Extract prompt compensation rules.
- Prepare recommended `prompt_id` and output path.
- Do not generate yet.

### Allowed next-step files to read

- `AI_CHARACTERS/OLGA/02_best_refs/`
- `AI_CHARACTERS/OLGA/02_refs_selected/`
- `AI_CHARACTERS/OLGA/03_face_sheet/`
- `AI_CHARACTERS/OLGA/04_body_sheet/`
- `AI_CHARACTERS/OLGA/05_outfits/`
- `AI_CHARACTERS/OLGA/06_prompts/`
- `AI_CHARACTERS/OLGA/07_generated/canon_tests/`
- `AI_CHARACTERS/OLGA/10_notes/`

### Forbidden in the next task

- No image generation.
- No new output folder.
- No repo asset deployment.
- No prompt log append.
- No `INVENTORY.md` update.
- No commit until the preflight report is approved by the human.

### Expected next report

`=== NCC OLGA FORMAL ELEGANT REFERENCE PREFLIGHT RESULT ===`
