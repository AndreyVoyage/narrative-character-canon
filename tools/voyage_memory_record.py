#!/usr/bin/env python3
"""Record/update structured facts in Voyage-lite SQLite memory.

Stdlib only. Works with an existing DB created by voyage_memory_init.py.
"""

import argparse
import json
import sqlite3
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DB = r"C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\voyage_memory\narrative_character_canon.sqlite"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def short_uuid() -> str:
    return uuid.uuid4().hex[:8]


def event_id() -> str:
    now = datetime.now(timezone.utc)
    return f"EVT-{now.strftime('%Y%m%d-%H%M%S')}-{short_uuid()}"


def validate_json(value: str) -> str:
    if not value or not value.strip():
        return "{}"
    try:
        json.loads(value)
    except json.JSONDecodeError as exc:
        raise argparse.ArgumentTypeError(f"Invalid JSON: {exc}") from exc
    return value


def ensure_db(db_path: Path) -> sqlite3.Connection:
    if not db_path.exists():
        print(f"ERROR: DB not found: {db_path}")
        print("Run voyage_memory_init.py first.")
        sys.exit(2)

    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='meta'")
    if not cur.fetchone():
        print("ERROR: DB exists but schema is missing. Run voyage_memory_init.py first.")
        conn.close()
        sys.exit(2)
    return conn


def add_event(
    conn: sqlite3.Connection,
    event_type: str,
    subject_type: str,
    subject_id: str,
    summary: str,
    payload_json: str,
    commit_hash: str | None,
    dry_run: bool,
    verbose: bool,
) -> None:
    eid = event_id()
    now = utc_now()
    if dry_run:
        if verbose:
            print(f"DRY-RUN event: {eid} {event_type} {subject_type}:{subject_id}")
        return
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO events (event_id, event_type, subject_type, subject_id, summary, payload_json, commit_hash, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (eid, event_type, subject_type, subject_id, summary, payload_json, commit_hash, now),
    )
    conn.commit()
    if verbose:
        print(f"Recorded event: {eid} {event_type}")


def cmd_event(args: argparse.Namespace) -> int:
    conn = ensure_db(Path(args.db).resolve())
    try:
        add_event(
            conn,
            args.event_type,
            args.subject_type,
            args.subject_id,
            args.summary,
            args.payload_json,
            args.commit_hash,
            args.dry_run,
            args.verbose,
        )
        if not args.dry_run:
            print("Event recorded.")
        return 0
    finally:
        conn.close()


def cmd_task(args: argparse.Namespace) -> int:
    conn = ensure_db(Path(args.db).resolve())
    try:
        if not args.dry_run:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO tasks (task_id, title, status, current_stage, next_action, notes, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(task_id) DO UPDATE SET
                    title=excluded.title,
                    status=excluded.status,
                    current_stage=excluded.current_stage,
                    next_action=excluded.next_action,
                    notes=excluded.notes,
                    updated_at=excluded.updated_at
                """,
                (
                    args.task_id,
                    args.title,
                    args.status,
                    args.current_stage,
                    args.next_action,
                    args.notes,
                    utc_now(),
                ),
            )
            conn.commit()
        if args.verbose or args.dry_run:
            print(f"{'DRY-RUN ' if args.dry_run else ''}Task recorded: {args.task_id} -> {args.status}")
        add_event(
            conn,
            "TASK_RECORDED",
            "task",
            args.task_id,
            f"Task recorded/updated: {args.title}",
            json.dumps({"status": args.status}),
            args.commit_hash,
            args.dry_run,
            args.verbose,
        )
        if not args.dry_run:
            print("Task recorded.")
        return 0
    finally:
        conn.close()


def cmd_decision(args: argparse.Namespace) -> int:
    conn = ensure_db(Path(args.db).resolve())
    try:
        if not args.dry_run:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO decisions (decision_id, title, date, summary, commit_hash, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(decision_id) DO UPDATE SET
                    title=excluded.title,
                    date=excluded.date,
                    summary=excluded.summary,
                    commit_hash=excluded.commit_hash,
                    updated_at=excluded.updated_at
                """,
                (args.decision_id, args.title, args.date, args.summary, args.commit_hash, utc_now()),
            )
            conn.commit()
        if args.verbose or args.dry_run:
            print(f"{'DRY-RUN ' if args.dry_run else ''}Decision recorded: {args.decision_id}")
        add_event(
            conn,
            "DECISION_RECORDED",
            "decision",
            args.decision_id,
            f"Decision recorded: {args.title}",
            json.dumps({"date": args.date}),
            args.commit_hash,
            args.dry_run,
            args.verbose,
        )
        if not args.dry_run:
            print("Decision recorded.")
        return 0
    finally:
        conn.close()


def cmd_commit(args: argparse.Namespace) -> int:
    conn = ensure_db(Path(args.db).resolve())
    try:
        created_at = args.created_at or utc_now()
        if not args.dry_run:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO commits (commit_hash, title, summary, created_at)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(commit_hash) DO UPDATE SET
                    title=excluded.title,
                    summary=excluded.summary,
                    created_at=excluded.created_at
                """,
                (args.commit_hash, args.title, args.summary, created_at),
            )
            conn.commit()
        if args.verbose or args.dry_run:
            print(f"{'DRY-RUN ' if args.dry_run else ''}Commit recorded: {args.commit_hash}")
        add_event(
            conn,
            "COMMIT_RECORDED",
            "commit",
            args.commit_hash,
            f"Commit recorded: {args.title}",
            json.dumps({"summary": args.summary}),
            args.commit_hash,
            args.dry_run,
            args.verbose,
        )
        if not args.dry_run:
            print("Commit recorded.")
        return 0
    finally:
        conn.close()


def cmd_character(args: argparse.Namespace) -> int:
    conn = ensure_db(Path(args.db).resolve())
    try:
        if not args.dry_run:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO characters (character_id, display_name, status, canon_status, height_cm, notes, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(character_id) DO UPDATE SET
                    display_name=excluded.display_name,
                    status=excluded.status,
                    canon_status=excluded.canon_status,
                    height_cm=excluded.height_cm,
                    notes=excluded.notes,
                    updated_at=excluded.updated_at
                """,
                (
                    args.character_id,
                    args.display_name,
                    args.status,
                    args.canon_status,
                    args.height_cm,
                    args.notes,
                    utc_now(),
                ),
            )
            conn.commit()
        if args.verbose or args.dry_run:
            print(f"{'DRY-RUN ' if args.dry_run else ''}Character recorded: {args.character_id} -> {args.status}")
        add_event(
            conn,
            "CHARACTER_STATUS_RECORDED",
            "character",
            args.character_id,
            f"Character recorded/updated: {args.display_name} -> {args.status}",
            json.dumps({"status": args.status}),
            args.commit_hash,
            args.dry_run,
            args.verbose,
        )
        if not args.dry_run:
            print("Character recorded.")
        return 0
    finally:
        conn.close()


def cmd_pair(args: argparse.Namespace) -> int:
    conn = ensure_db(Path(args.db).resolve())
    try:
        if not args.dry_run:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO pairs (pair_id, character_a, character_b, status, notes, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(pair_id) DO UPDATE SET
                    character_a=excluded.character_a,
                    character_b=excluded.character_b,
                    status=excluded.status,
                    notes=excluded.notes,
                    updated_at=excluded.updated_at
                """,
                (
                    args.pair_id,
                    args.character_a,
                    args.character_b,
                    args.status,
                    args.notes,
                    utc_now(),
                ),
            )
            conn.commit()
        if args.verbose or args.dry_run:
            print(f"{'DRY-RUN ' if args.dry_run else ''}Pair recorded: {args.pair_id} -> {args.status}")
        add_event(
            conn,
            "PAIR_STATUS_RECORDED",
            "pair",
            args.pair_id,
            f"Pair recorded/updated: {args.pair_id} -> {args.status}",
            json.dumps({"status": args.status}),
            args.commit_hash,
            args.dry_run,
            args.verbose,
        )
        if not args.dry_run:
            print("Pair recorded.")
        return 0
    finally:
        conn.close()


def cmd_artifact(args: argparse.Namespace) -> int:
    if not args.character_id and not args.pair_id:
        print("ERROR: artifact requires --character-id or --pair-id")
        return 1
    if args.is_approved and args.is_rejected:
        print("ERROR: artifact cannot be both approved and rejected")
        return 1

    repo_root = Path(args.repo_root).resolve()
    file_path = args.file_path
    if file_path.startswith("AI_CHARACTERS/"):
        full_path = repo_root / file_path
        if not full_path.exists() and not args.allow_missing_file:
            print(f"ERROR: repo file not found: {file_path}")
            print("Use --allow-missing-file for logical-only records.")
            return 2

    conn = ensure_db(Path(args.db).resolve())
    try:
        if not args.dry_run:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO artifacts
                (artifact_id, character_id, pair_id, artifact_type, file_path, status, verdict,
                 is_active_canon, is_approved, is_rejected, notes, commit_hash, updated_at)
                VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                (
                    args.artifact_id,
                    args.character_id,
                    args.pair_id,
                    args.artifact_type,
                    file_path,
                    args.status,
                    args.verdict,
                    args.is_active_canon,
                    args.is_approved,
                    args.is_rejected,
                    args.notes,
                    args.commit_hash,
                    utc_now(),
                ),
            )
            conn.commit()
        if args.verbose or args.dry_run:
            print(f"{'DRY-RUN ' if args.dry_run else ''}Artifact recorded: {args.artifact_id} -> {args.status}")
        add_event(
            conn,
            "ARTIFACT_RECORDED",
            "artifact",
            args.artifact_id,
            f"Artifact recorded/updated: {args.artifact_id} -> {args.status}",
            json.dumps({"status": args.status, "file_path": file_path}),
            args.commit_hash,
            args.dry_run,
            args.verbose,
        )
        if not args.dry_run:
            print("Artifact recorded.")
        return 0
    finally:
        conn.close()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Record/update Voyage memory facts.")
    parser.add_argument("--db", default=DEFAULT_DB, help="Path to SQLite DB.")
    parser.add_argument("--repo-root", default=".", help="Repository root directory.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be recorded.")
    parser.add_argument("--verbose", action="store_true", help="Verbose output.")
    sub = parser.add_subparsers(dest="command", required=True)

    event_p = sub.add_parser("event", help="Record an event")
    event_p.add_argument("--event-type", required=True)
    event_p.add_argument("--subject-type", required=True)
    event_p.add_argument("--subject-id", required=True)
    event_p.add_argument("--summary", required=True)
    event_p.add_argument("--payload-json", type=validate_json, default="{}")
    event_p.add_argument("--commit-hash", default=None)

    task_p = sub.add_parser("task", help="Record/update a task")
    task_p.add_argument("--task-id", required=True)
    task_p.add_argument("--title", required=True)
    task_p.add_argument("--status", required=True)
    task_p.add_argument("--current-stage", default=None)
    task_p.add_argument("--next-action", default=None)
    task_p.add_argument("--notes", default=None)
    task_p.add_argument("--commit-hash", default=None)

    decision_p = sub.add_parser("decision", help="Record/update a decision")
    decision_p.add_argument("--decision-id", required=True)
    decision_p.add_argument("--title", required=True)
    decision_p.add_argument("--date", required=True)
    decision_p.add_argument("--summary", required=True)
    decision_p.add_argument("--commit-hash", default=None)

    commit_p = sub.add_parser("commit", help="Record/update a commit")
    commit_p.add_argument("--commit-hash", required=True)
    commit_p.add_argument("--title", required=True)
    commit_p.add_argument("--summary", default=None)
    commit_p.add_argument("--created-at", default=None)

    char_p = sub.add_parser("character", help="Record/update a character")
    char_p.add_argument("--character-id", required=True)
    char_p.add_argument("--display-name", required=True)
    char_p.add_argument("--status", required=True)
    char_p.add_argument("--canon-status", default=None)
    char_p.add_argument("--height-cm", type=int, default=None)
    char_p.add_argument("--notes", default=None)
    char_p.add_argument("--commit-hash", default=None)

    pair_p = sub.add_parser("pair", help="Record/update a pair")
    pair_p.add_argument("--pair-id", required=True)
    pair_p.add_argument("--character-a", required=True)
    pair_p.add_argument("--character-b", required=True)
    pair_p.add_argument("--status", required=True)
    pair_p.add_argument("--notes", default=None)
    pair_p.add_argument("--commit-hash", default=None)

    art_p = sub.add_parser("artifact", help="Record/update an artifact")
    art_p.add_argument("--artifact-id", required=True)
    art_p.add_argument("--character-id", default=None)
    art_p.add_argument("--pair-id", default=None)
    art_p.add_argument("--artifact-type", required=True)
    art_p.add_argument("--file-path", required=True)
    art_p.add_argument("--status", required=True)
    art_p.add_argument("--verdict", default=None)
    art_p.add_argument("--is-active-canon", type=int, default=0, choices=[0, 1])
    art_p.add_argument("--is-approved", type=int, default=0, choices=[0, 1])
    art_p.add_argument("--is-rejected", type=int, default=0, choices=[0, 1])
    art_p.add_argument("--notes", default=None)
    art_p.add_argument("--commit-hash", default=None)
    art_p.add_argument("--allow-missing-file", action="store_true", help="Allow missing AI_CHARACTERS/ file path.")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    command_map = {
        "event": cmd_event,
        "task": cmd_task,
        "decision": cmd_decision,
        "commit": cmd_commit,
        "character": cmd_character,
        "pair": cmd_pair,
        "artifact": cmd_artifact,
    }
    return command_map[args.command](args)


if __name__ == "__main__":
    raise SystemExit(main())
