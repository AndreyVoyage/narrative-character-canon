#!/usr/bin/env python3
"""Initialize Voyage-lite SQLite memory for narrative-character-canon.

Stdlib only. Idempotent.
"""

import argparse
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DB = r"C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\voyage_memory\narrative_character_canon.sqlite"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def ensure_db_parent(db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)


def create_schema(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.executescript(
        """
        CREATE TABLE IF NOT EXISTS meta (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS characters (
            character_id TEXT PRIMARY KEY,
            display_name TEXT NOT NULL,
            status TEXT NOT NULL,
            canon_status TEXT,
            height_cm INTEGER,
            notes TEXT,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS pairs (
            pair_id TEXT PRIMARY KEY,
            character_a TEXT NOT NULL,
            character_b TEXT NOT NULL,
            status TEXT NOT NULL,
            notes TEXT,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS artifacts (
            artifact_id TEXT PRIMARY KEY,
            character_id TEXT,
            pair_id TEXT,
            artifact_type TEXT NOT NULL,
            file_path TEXT NOT NULL,
            status TEXT NOT NULL,
            verdict TEXT,
            is_active_canon INTEGER NOT NULL DEFAULT 0,
            is_approved INTEGER NOT NULL DEFAULT 0,
            is_rejected INTEGER NOT NULL DEFAULT 0,
            notes TEXT,
            commit_hash TEXT,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS decisions (
            decision_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            date TEXT NOT NULL,
            summary TEXT NOT NULL,
            commit_hash TEXT,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS tasks (
            task_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            status TEXT NOT NULL,
            current_stage TEXT,
            next_action TEXT,
            notes TEXT,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS events (
            event_id TEXT PRIMARY KEY,
            event_type TEXT NOT NULL,
            subject_type TEXT NOT NULL,
            subject_id TEXT NOT NULL,
            summary TEXT NOT NULL,
            payload_json TEXT,
            commit_hash TEXT,
            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS commits (
            commit_hash TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            summary TEXT,
            created_at TEXT NOT NULL
        );
        """
    )
    conn.commit()


def upsert_meta(conn: sqlite3.Connection, key: str, value: str) -> None:
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO meta (key, value, updated_at) VALUES (?, ?, ?) "
        "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
        (key, value, utc_now()),
    )
    conn.commit()


def upsert_character(conn: sqlite3.Connection, data: dict) -> None:
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO characters
        (character_id, display_name, status, canon_status, height_cm, notes, updated_at)
        VALUES (:character_id, :display_name, :status, :canon_status, :height_cm, :notes, :updated_at)
        ON CONFLICT(character_id) DO UPDATE SET
            display_name=excluded.display_name,
            status=excluded.status,
            canon_status=excluded.canon_status,
            height_cm=excluded.height_cm,
            notes=excluded.notes,
            updated_at=excluded.updated_at
        """,
        {**data, "updated_at": utc_now()},
    )
    conn.commit()


def upsert_pair(conn: sqlite3.Connection, data: dict) -> None:
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO pairs
        (pair_id, character_a, character_b, status, notes, updated_at)
        VALUES (:pair_id, :character_a, :character_b, :status, :notes, :updated_at)
        ON CONFLICT(pair_id) DO UPDATE SET
            character_a=excluded.character_a,
            character_b=excluded.character_b,
            status=excluded.status,
            notes=excluded.notes,
            updated_at=excluded.updated_at
        """,
        {**data, "updated_at": utc_now()},
    )
    conn.commit()


def upsert_artifact(conn: sqlite3.Connection, data: dict) -> None:
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO artifacts
        (artifact_id, character_id, pair_id, artifact_type, file_path, status, verdict,
         is_active_canon, is_approved, is_rejected, notes, commit_hash, updated_at)
        VALUES
        (:artifact_id, :character_id, :pair_id, :artifact_type, :file_path, :status, :verdict,
         :is_active_canon, :is_approved, :is_rejected, :notes, :commit_hash, :updated_at)
        ON CONFLICT(artifact_id) DO UPDATE SET
            character_id=excluded.character_id,
            pair_id=excluded.pair_id,
            artifact_type=excluded.artifact_type,
            file_path=excluded.file_path,
            status=excluded.status,
            verdict=excluded.verdict,
            is_active_canon=excluded.is_active_canon,
            is_approved=excluded.is_approved,
            is_rejected=excluded.is_rejected,
            notes=excluded.notes,
            commit_hash=excluded.commit_hash,
            updated_at=excluded.updated_at
        """,
        {**data, "updated_at": utc_now()},
    )
    conn.commit()


def upsert_decision(conn: sqlite3.Connection, data: dict) -> None:
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO decisions
        (decision_id, title, date, summary, commit_hash, updated_at)
        VALUES (:decision_id, :title, :date, :summary, :commit_hash, :updated_at)
        ON CONFLICT(decision_id) DO UPDATE SET
            title=excluded.title,
            date=excluded.date,
            summary=excluded.summary,
            commit_hash=excluded.commit_hash,
            updated_at=excluded.updated_at
        """,
        {**data, "updated_at": utc_now()},
    )
    conn.commit()


def upsert_task(conn: sqlite3.Connection, data: dict) -> None:
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO tasks
        (task_id, title, status, current_stage, next_action, notes, updated_at)
        VALUES (:task_id, :title, :status, :current_stage, :next_action, :notes, :updated_at)
        ON CONFLICT(task_id) DO UPDATE SET
            title=excluded.title,
            status=excluded.status,
            current_stage=excluded.current_stage,
            next_action=excluded.next_action,
            notes=excluded.notes,
            updated_at=excluded.updated_at
        """,
        {**data, "updated_at": utc_now()},
    )
    conn.commit()


def upsert_commit(conn: sqlite3.Connection, data: dict) -> None:
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO commits
        (commit_hash, title, summary, created_at)
        VALUES (:commit_hash, :title, :summary, :created_at)
        ON CONFLICT(commit_hash) DO UPDATE SET
            title=excluded.title,
            summary=excluded.summary,
            created_at=excluded.created_at
        """,
        data,
    )
    conn.commit()


def seed(conn: sqlite3.Connection) -> None:
    upsert_meta(conn, "project_name", "narrative-character-canon")
    upsert_meta(conn, "memory_version", "1.0.0")
    upsert_meta(conn, "db_role", "local_runtime_memory_not_git_tracked")

    upsert_character(
        conn,
        {
            "character_id": "KIRA",
            "display_name": "Kira",
            "status": "CANON_READY_2D",
            "canon_status": "ACTIVE",
            "height_cm": 168,
            "notes": (
                "Kira canon confirmed by repo. Kira docs exist as .md.txt files. "
                "Reference presets valid with 7 scene presets."
            ),
        },
    )

    upsert_character(
        conn,
        {
            "character_id": "ANDREY",
            "display_name": "Andrey Senior",
            "status": "CANON_READY_2D",
            "canon_status": "ACTIVE",
            "height_cm": 180,
            "notes": (
                "Andrey face canon, body canon and 6 solo control tests approved."
            ),
        },
    )

    upsert_pair(
        conn,
        {
            "pair_id": "KIRA_ANDREY",
            "character_a": "KIRA",
            "character_b": "ANDREY",
            "status": "JOINT_CONTROL_TESTS_APPROVED",
            "notes": (
                "Four approved joint control tests committed. "
                "Kira barefoot height remains 168 cm; heels may make apparent height 176-178 cm. "
                "Andrey remains 180 cm."
            ),
        },
    )

    for commit_hash, title in [
        ("317ade9", "Fix Kira test result filename reference"),
        ("75f7aba", "Add Kira Andrey joint control test setup"),
        ("e6df873", "Add approved Kira Andrey joint tests"),
        ("2a23e6c", "Add approved Andrey control tests"),
    ]:
        upsert_commit(
            conn,
            {
                "commit_hash": commit_hash,
                "title": title,
                "summary": "",
                "created_at": utc_now(),
            },
        )

    upsert_task(
        conn,
        {
            "task_id": "NCC-VOYAGE-SQLITE-MEMORY",
            "title": "Voyage-lite SQLite memory layer",
            "status": "IN_PROGRESS",
            "current_stage": "SETUP",
            "next_action": "Create local SQLite DB and exports",
            "notes": "Build structured local memory without committing DB file.",
        },
    )

    decisions = [
        (
            "DECISION-0010",
            "Andrey control tests approved",
            "2026-07-02",
            "Approved all six Andrey solo control tests and marked Andrey as CANON_READY_2D.",
            "2a23e6c",
        ),
        (
            "DECISION-0011",
            "Run Kira and Andrey joint control tests before 3D stage",
            "2026-07-02",
            "Created KIRA + ANDREY joint control test structure and prompts before 3D stage.",
            "75f7aba",
        ),
        (
            "DECISION-0012",
            "Fix Kira test result filename reference",
            "2026-07-02",
            "Replaced outdated Kira TEST 3 image filename reference to match tracked file.",
            "317ade9",
        ),
        (
            "DECISION-0013",
            "Approve Kira and Andrey joint control tests",
            "2026-07-02",
            "Approved four KIRA + ANDREY joint control tests.",
            "e6df873",
        ),
    ]
    for decision_id, title, date, summary, commit_hash in decisions:
        upsert_decision(
            conn,
            {
                "decision_id": decision_id,
                "title": title,
                "date": date,
                "summary": summary,
                "commit_hash": commit_hash,
            },
        )

    joint_tests = [
        (
            "KIRA_ANDREY_JOINT_TEST_01",
            "AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/01_neutral_studio_duo/KIRA_ANDREY_joint_test01_neutral_studio_duo_v2_APPROVED.png",
            "e6df873",
            "Neutral studio duo. First version rejected due to Kira identity drift.",
        ),
        (
            "KIRA_ANDREY_JOINT_TEST_02",
            "AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/02_evening_embankment_duo/KIRA_ANDREY_joint_test02_evening_embankment_duo_v1_APPROVED.png",
            "e6df873",
            "Evening embankment duo. Kira heels make her appear taller; barefoot height remains 168 cm.",
        ),
        (
            "KIRA_ANDREY_JOINT_TEST_03",
            "AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/03_warm_bar_conversation/KIRA_ANDREY_joint_test03_warm_bar_conversation_v1_APPROVED.png",
            "e6df873",
            "Warm bar conversation. Earlier gym-scene outputs rejected.",
        ),
        (
            "KIRA_ANDREY_JOINT_TEST_04",
            "AI_CHARACTERS/_JOINT_SCENES/KIRA_ANDREY/07_generated/canon_tests/04_sea_yacht_mood_duo/KIRA_ANDREY_joint_test04_sea_yacht_mood_duo_v1_APPROVED.png",
            "e6df873",
            "Sea/yacht mood duo. Earlier living room output rejected.",
        ),
    ]
    for artifact_id, file_path, commit_hash, notes in joint_tests:
        upsert_artifact(
            conn,
            {
                "artifact_id": artifact_id,
                "character_id": None,
                "pair_id": "KIRA_ANDREY",
                "artifact_type": "joint_control_test",
                "file_path": file_path,
                "status": "APPROVED",
                "verdict": "APPROVE",
                "is_active_canon": 1,
                "is_approved": 1,
                "is_rejected": 0,
                "notes": notes,
                "commit_hash": commit_hash,
            },
        )

    rejected_outputs = [
        (
            "KIRA_ANDREY_JOINT_TEST_01_REJECTED_V1",
            "LOCAL_STORAGE/rejected_joint_tests/KIRA_ANDREY_joint_test01_neutral_studio_duo_v1_rejected.png",
            "first JOINT TEST 01 version rejected because of Kira identity drift",
        ),
        (
            "KIRA_ANDREY_JOINT_TEST_03_WRONG_GYM",
            "LOCAL_STORAGE/rejected_joint_tests/KIRA_ANDREY_joint_test03_wrong_gym_outputs.png",
            "wrong gym outputs generated for JOINT TEST 03",
        ),
        (
            "KIRA_ANDREY_JOINT_TEST_04_WRONG_LIVING_ROOM",
            "LOCAL_STORAGE/rejected_joint_tests/KIRA_ANDREY_joint_test04_wrong_living_room.png",
            "wrong living room output generated for JOINT TEST 04",
        ),
    ]
    for artifact_id, file_path, notes in rejected_outputs:
        upsert_artifact(
            conn,
            {
                "artifact_id": artifact_id,
                "character_id": None,
                "pair_id": "KIRA_ANDREY",
                "artifact_type": "rejected_joint_output",
                "file_path": file_path,
                "status": "REJECTED_OR_IGNORED",
                "verdict": "REJECT",
                "is_active_canon": 0,
                "is_approved": 0,
                "is_rejected": 1,
                "notes": notes,
                "commit_hash": None,
            },
        )

    andrey_solo_tests = [
        "AI_CHARACTERS/ANDREY/07_generated/canon_tests/01_neutral_studio_portrait/ANDREY_test01_neutral_studio_portrait_v1.png",
        "AI_CHARACTERS/ANDREY/07_generated/canon_tests/02_full_body_blue_shirt/ANDREY_test02_full_body_blue_shirt_studio_v1.png",
        "AI_CHARACTERS/ANDREY/07_generated/canon_tests/03_warm_bar_portrait/ANDREY_test03_warm_bar_portrait_v1.png",
        "AI_CHARACTERS/ANDREY/07_generated/canon_tests/04_formal_evening_look/ANDREY_test04_formal_evening_look_v1.png",
        "AI_CHARACTERS/ANDREY/07_generated/canon_tests/05_sports_gym_identity/ANDREY_test05_sports_gym_identity_v1.png",
        "AI_CHARACTERS/ANDREY/07_generated/canon_tests/06_sea_yacht_mood/ANDREY_test06_sea_yacht_mood_scene_v1.png",
    ]
    for idx, file_path in enumerate(andrey_solo_tests, start=1):
        upsert_artifact(
            conn,
            {
                "artifact_id": f"ANDREY_SOLO_CONTROL_TEST_{idx:02d}",
                "character_id": "ANDREY",
                "pair_id": None,
                "artifact_type": "solo_control_test",
                "file_path": file_path,
                "status": "APPROVED",
                "verdict": "APPROVE",
                "is_active_canon": 1,
                "is_approved": 1,
                "is_rejected": 0,
                "notes": f"Andrey solo control test {idx}.",
                "commit_hash": "2a23e6c",
            },
        )

    kira_docs = [
        (
            "KIRA_REFERENCE_PRESETS_JSON",
            "AI_CHARACTERS/KIRA/10_notes/KIRA_REFERENCE_PRESETS.json",
            "Kira reference presets JSON. Valid with 7 scene presets.",
        ),
        (
            "KIRA_CANON_INDEX_MD_TXT",
            "AI_CHARACTERS/KIRA/10_notes/KIRA_CANON_INDEX.md.txt",
            "Kira canon index in .md.txt form. Not missing, just .md.txt naming.",
        ),
        (
            "KIRA_TEST_RESULTS_MD_TXT",
            "AI_CHARACTERS/KIRA/10_notes/KIRA_TEST_RESULTS.md.txt",
            "Kira test results in .md.txt form. Not missing, just .md.txt naming.",
        ),
    ]
    for artifact_id, file_path, notes in kira_docs:
        upsert_artifact(
            conn,
            {
                "artifact_id": artifact_id,
                "character_id": "KIRA",
                "pair_id": None,
                "artifact_type": "canon_document",
                "file_path": file_path,
                "status": "VALID / TRACKED",
                "verdict": "APPROVE",
                "is_active_canon": 1,
                "is_approved": 1,
                "is_rejected": 0,
                "notes": notes,
                "commit_hash": None,
            },
        )

    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO events (event_id, event_type, subject_type, subject_id, summary, payload_json, commit_hash, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(event_id) DO UPDATE SET
            event_type=excluded.event_type,
            subject_type=excluded.subject_type,
            subject_id=excluded.subject_id,
            summary=excluded.summary,
            payload_json=excluded.payload_json,
            commit_hash=excluded.commit_hash,
            created_at=excluded.created_at
        """,
        (
            "MEMORY_INIT",
            "MEMORY_INIT",
            "project",
            "narrative-character-canon",
            "Voyage memory initialized with current known facts.",
            json.dumps({"source": "voyage_memory_init.py"}),
            None,
            utc_now(),
        ),
    )
    conn.commit()


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize Voyage-lite SQLite memory.")
    parser.add_argument("--repo-root", default=".", help="Repository root directory.")
    parser.add_argument("--db", default=DEFAULT_DB, help="Path to SQLite DB.")
    args = parser.parse_args()

    db_path = Path(args.db).resolve()
    ensure_db_parent(db_path)

    conn = sqlite3.connect(str(db_path))
    try:
        create_schema(conn)
        seed(conn)
        print(f"Voyage memory initialized: {db_path}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
