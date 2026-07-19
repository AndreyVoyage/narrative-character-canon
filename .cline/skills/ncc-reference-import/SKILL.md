---
name: ncc-reference-import
description: Import owner-selected external visual references into narrative-character-canon from a JSON task spec. Use for SHA-verified copy-only reference imports that must stop uncommitted for human review.
---

# NCC Reference Import

Copies owner-selected external reference images into an existing character's
namespace under `AI_CHARACTERS/<CHARACTER_ID>/`, using a JSON task spec as the
only source of truth for what gets copied where. It is a deterministic,
copy-only operation — it never generates, edits, stages, commits, or pushes.

## Requirements before running

1. Exactly one JSON task-spec file path, supplied by the user (e.g. as an
   `@`-mentioned file or an explicit path). Do not proceed without it, and do
   not improvise a spec from a filename or a description.
2. The task spec must already satisfy the contract in
   `templates/reference-import-task.example.json` (see that file for the full
   field list and rules).

## Procedure

1. **Never hand-roll the operation in PowerShell or Python one-liners.** Always
   invoke the bundled script:
   `scripts/import_references.py`.
2. **Always start with dry-run** (no `--apply` flag):

   ```powershell
   py -3 -B .cline\skills\ncc-reference-import\scripts\import_references.py --repo-root <repo> --task-spec <json>
   ```

3. Show the full dry-run output to the user, unedited: every planned
   source → target action, the copy/reuse counts, and the
   `REPOSITORY_MODIFIED=NO` line.
4. Ask the user to review the dry-run and explicitly approve switching to
   Act mode to run the single apply command. Do not proceed on an implicit
   or assumed approval.
5. Only after explicit approval, run the same command with `--apply`:

   ```powershell
   py -3 -B .cline\skills\ncc-reference-import\scripts\import_references.py --repo-root <repo> --task-spec <json> --apply
   ```

6. **Stop uncommitted.** The script never stages, commits, or pushes. Report
   the final `=== NCC REFERENCE IMPORT RESULT ===` block to the user and end
   the task there — staging/commit/push are separate tasks under
   `.clinerules/30-ncc-task-discipline.md`.
7. **Never edit metadata** (`*_CANON_INDEX.md`, `*_REFERENCE_PRESETS.json`,
   registry files, etc.) as part of this skill, even if the task spec lists
   `authorized_metadata_files` — the MVP script requires that field to be
   empty and rejects anything else. Metadata closeout is a separate task.
8. **Never** stage, commit, push, generate images, write to SQLite, or read/
   write any path outside the task spec's declared `source_files` and their
   `target_relative_path` destinations.
9. If the script exits nonzero at any step (dry-run or apply), stop
   immediately and report the exact first failure line to the user. Do not
   retry with modified arguments and do not attempt a manual workaround.

## Slash invocation

```text
/ncc-reference-import
Task spec: C:\...\EGOR_REFERENCE_IMPORT_TASK.json
```
