# NCC Git Safety

Before any write-capable operation, confirm all of the following:

- Current branch is `main`.
- Local `HEAD` matches the expected/tracked hash for the task and matches `origin/main`.
- The tracked working tree is clean (`git status --short` shows no modified/deleted tracked files).
- Nothing is staged (`git diff --cached` is empty).
- Untracked paths are limited to the protected set: `.claude/`, `.vscode/`, `UNIFIED_CANON_TESTS_TEMPLATE.md`, `repo_audit.txt`. Any other untracked path stops the task.

Stop before writing if any of these facts differ from what the task expects.

- Never run `git push`, `git push --force`, `git reset`, `git clean`, `git rebase`, `git checkout <ref>` (branch-switching or file-discarding forms), `git merge`, `git pull`, or `git commit --amend` unless the active task explicitly authorizes that exact operation.
- Cline tasks normally end with the working tree modified but **uncommitted**. Do not stage or commit unless the task is explicitly a staging/commit phase.
- Staging, committing, verification, and publication (push) are separate phases/tasks. Do not chain them together inside one task unless explicitly instructed.
- Stop immediately and report to the user if the worktree changes unexpectedly mid-task (a sign of a concurrent writer), or if any gate above fails after a re-check performed immediately before a write.
