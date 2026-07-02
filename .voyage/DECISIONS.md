# DECISIONS

## DECISION-0001 — Use GitHub-first reference workflow

Date: 2026-07-01

Context: Manual reference upload caused friction and risk of wrong files.

Decision: Use GitHub-first reference packs with raw links and embedded text canon.

Affected files: `tools/build_scene_reference_pack.py`, `tools/build_scene_reference_pack.ps1`, `docs/GITHUB_REFERENCE_PACK_WORKFLOW.md`.

Reason: Reduces manual upload errors and keeps reference packs reproducible from tracked repo state.

Next action: Extend presets to remaining characters once their canon packs exist.

## DECISION-0002 — Scene examples are not generation tasks

Date: 2026-07-01

Context: "Kira and Andrey in sauna" was used as an example of how the reference-pack tool should work, not as a real request.

Decision: Example scenes must not be treated as approved generation tasks.

Affected files: none (workflow rule).

Reason: Prevents accidental generation/commit of images based on illustrative examples rather than explicit user requests.

Next action: Sauna scene should not be generated unless the user explicitly requests it. Rule enforced in [.voyage/SCENE_REQUEST_RULES.md](SCENE_REQUEST_RULES.md).

## DECISION-0003 — Voyage-lite memory layer

Date: 2026-07-02

Context: Project will grow with more characters, locations, 3D models and scenes; without a memory layer it's easy to confuse examples, drafts, approved canon, and placeholders across sessions and tools (ChatGPT, Kimi, Codex, Claude Code).

Decision: Add `.voyage/` memory/control files to preserve context and avoid confusion, plus `docs/VOYAGE_INTEGRATION_WORKFLOW.md` explaining the layer.

Affected files: `docs/VOYAGE_INTEGRATION_WORKFLOW.md`, `.voyage/README.md`, `.voyage/PROJECT_STATE.md`, `.voyage/CHARACTER_REGISTRY.md`, `.voyage/LOCATION_REGISTRY.md`, `.voyage/SCENE_REQUEST_RULES.md`, `.voyage/DECISIONS.md`, `.voyage/CURRENT_TASK.md`, `README.md`, `INVENTORY.md`.

Reason: Preserve project context; distinguish example vs task, draft vs approved, local-only vs GitHub-tracked, raw ref vs active canon.

Next action: Keep `.voyage/PROJECT_STATE.md` and `.voyage/CHARACTER_REGISTRY.md` updated as character canon packs progress.

## DECISION-0004 — KIRA_REFERENCE_PRESETS.json audit result

Date: 2026-07-02

Context: `AGENTS.md`/`ROADMAP.md` described KIRA as "canon-ready / needs repo verification." A `.backup_20260702_082208` of `KIRA_REFERENCE_PRESETS.json` exists, indicating the file was already edited earlier today.

Decision: Audited `AI_CHARACTERS/KIRA/10_notes/KIRA_REFERENCE_PRESETS.json` against the actual file tree. All `text_sources` paths and all `reference_images` in all 7 `scene_presets` (portrait, body_canon, sports, evening, bar, sauna, outdoor) exist in the repository. The file is valid and working — no fix was needed.

Affected files: none (verification only).

Reason: Avoid duplicating work or fabricating a "fix" for a file that is already correct.

Next action: Update `CHARACTER_REGISTRY.md` to reflect KIRA as verified; treat ANDREY body canon as the next actionable roadmap item instead.
