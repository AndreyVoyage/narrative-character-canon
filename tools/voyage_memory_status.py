#!/usr/bin/env python3
"""Quick status report for Voyage-lite SQLite memory.

Stdlib only.
"""

import argparse
import sqlite3
from pathlib import Path

DEFAULT_DB = r"C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\voyage_memory\narrative_character_canon.sqlite"


def count(conn: sqlite3.Connection, table: str) -> int:
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table}")
    return cur.fetchone()[0]


def approved_count(conn: sqlite3.Connection) -> int:
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM artifacts WHERE is_approved = 1")
    return cur.fetchone()[0]


def rejected_count(conn: sqlite3.Connection) -> int:
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM artifacts WHERE is_rejected = 1")
    return cur.fetchone()[0]


def latest_task(conn: sqlite3.Connection) -> str:
    cur = conn.cursor()
    cur.execute("SELECT task_id, title, status FROM tasks ORDER BY updated_at DESC LIMIT 1")
    row = cur.fetchone()
    if row:
        return f"{row[0]} - {row[1]} ({row[2]})"
    return "none"


def main() -> None:
    parser = argparse.ArgumentParser(description="Show Voyage memory status.")
    parser.add_argument("--db", default=DEFAULT_DB, help="Path to SQLite DB.")
    args = parser.parse_args()

    db_path = Path(args.db).resolve()
    if not db_path.exists():
        print(f"DB not found: {db_path}")
        raise SystemExit(1)

    conn = sqlite3.connect(str(db_path))
    try:
        print("Voyage memory status")
        print(f"DB: {db_path}")
        print(f"Characters: {count(conn, 'characters')}")
        print(f"Pairs: {count(conn, 'pairs')}")
        print(f"Artifacts: {count(conn, 'artifacts')}")
        print(f"Approved artifacts: {approved_count(conn)}")
        print(f"Rejected artifacts: {rejected_count(conn)}")
        print(f"Tasks: {count(conn, 'tasks')}")
        print(f"Decisions: {count(conn, 'decisions')}")
        print(f"Events: {count(conn, 'events')}")
        print(f"Latest task: {latest_task(conn)}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
