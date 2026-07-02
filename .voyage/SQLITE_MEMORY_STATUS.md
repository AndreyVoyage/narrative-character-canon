# SQLITE_MEMORY_STATUS

Status:
SETUP_DONE / RECORD_COMMAND_READY

DB location:
C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\voyage_memory\narrative_character_canon.sqlite

Git policy:
SQLite DB is local runtime memory and must not be committed.

Tools:

* tools/voyage_memory_init.py
* tools/voyage_memory_status.py
* tools/voyage_memory_export.py
* tools/voyage_memory_record.py

Exports:

* .voyage/CONTEXT_SNAPSHOT.md
* .voyage/STATE_EXPORT.json
* .voyage/EVENTS_EXPORT.jsonl

Current known facts:

* KIRA = CANON_READY_2D
* ANDREY = CANON_READY_2D
* KIRA_ANDREY = JOINT_CONTROL_TESTS_APPROVED
* Record command is available for future workflow updates.

Next:
Use voyage_memory_record.py after every major approved/rejected workflow, then export snapshot.
