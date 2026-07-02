# VOYAGE_SQLITE_MEMORY_WORKFLOW

## Purpose

Voyage-lite SQLite memory layer — это локальная runtime-память проекта `narrative-character-canon`. Она хранит структурированные факты о персонажах, approved/rejected outputs, decisions, commits и текущих задачах.

SQLite DB не коммитится в GitHub. В GitHub попадают только инструменты, документация и компактные exports.

## What SQLite stores

* статусы персонажей;
* active canon files;
* approved control tests;
* rejected/wrong-scene outputs;
* pair/joint statuses;
* decisions;
* commits;
* current/next tasks;
* events.

## What Git stores

* Python tools: `tools/voyage_memory_init.py`, `tools/voyage_memory_export.py`, `tools/voyage_memory_status.py`;
* docs: `docs/VOYAGE_SQLITE_MEMORY_WORKFLOW.md`;
* exports: `.voyage/CONTEXT_SNAPSHOT.md`, `.voyage/STATE_EXPORT.json`, `.voyage/EVENTS_EXPORT.jsonl`;
* обновлённые `.voyage/*.md` файлы;
* `INVENTORY.md`.

## What must never be committed

```text
*.sqlite
*.sqlite3
*.db
LOCAL_STORAGE/
voyage_memory/
```

## Default local DB path

```text
C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\voyage_memory\narrative_character_canon.sqlite
```

## Standard commands

### Initialize / update memory

```powershell
python .\tools\voyage_memory_init.py --repo-root . --db "C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\voyage_memory\narrative_character_canon.sqlite"
```

### Show status

```powershell
python .\tools\voyage_memory_status.py --db "C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\voyage_memory\narrative_character_canon.sqlite"
```

### Export to tracked files

```powershell
python .\tools\voyage_memory_export.py --repo-root . --db "C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\voyage_memory\narrative_character_canon.sqlite" --out-dir .\.voyage
```

## When to update memory

* после approved control tests;
* после rejected outputs;
* после decisions;
* после commits;
* перед стартом 3D packs;
* перед стартом нового персонажа.

## Current project facts

* KIRA = CANON_READY_2D
* ANDREY = CANON_READY_2D
* KIRA_ANDREY = JOINT_CONTROL_TESTS_APPROVED
* Kira barefoot height remains 168 cm
* Andrey height remains 180 cm
* rejected/wrong-scene outputs must not be used as canon
* Kira canon docs exist as `.md.txt`, not missing

## Workflow with ChatGPT

1. Local agent updates SQLite.
2. Local agent exports snapshot.
3. User pastes `CONTEXT_SNAPSHOT.md` or final report into ChatGPT.
4. ChatGPT uses snapshot as compact project memory.
