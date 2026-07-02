#!/usr/bin/env python3
"""Export Voyage-lite SQLite memory to tracked markdown/json/jsonl files.

Stdlib only.
"""

import argparse
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DB = r"C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\voyage_memory\narrative_character_canon.sqlite"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def fetch_all(conn: sqlite3.Connection, table: str) -> list[dict]:
    cur = conn.cursor()
    cur.row_factory = sqlite3.Row
    cur.execute(f"SELECT * FROM {table}")
    return [dict(row) for row in cur.fetchall()]


def build_context_snapshot(state: dict) -> str:
    lines = []
    lines.append("# CONTEXT_SNAPSHOT")
    lines.append("")
    lines.append(f"Generated at: {state.get('generated_at')}")
    lines.append("")
    lines.append(f"Project: {state.get('project', 'narrative-character-canon')}")
    lines.append("")
    lines.append("## Current recommended task")
    lines.append("")
    lines.append("NCC-VOYAGE-SQLITE-MEMORY complete. Choose next direction from options below.")
    lines.append("")
    lines.append("## Character statuses")
    lines.append("")
    for char in state.get("characters", []):
        height = f", height {char.get('height_cm')} cm" if char.get("height_cm") else ""
        lines.append(f"- {char['character_id']}: {char['status']}{height}")
    lines.append("")
    lines.append("## Pair statuses")
    lines.append("")
    for pair in state.get("pairs", []):
        lines.append(f"- {pair['pair_id']}: {pair['status']}")
    lines.append("")
    lines.append("## Approved KIRA + ANDREY joint tests")
    lines.append("")
    idx = 1
    for art in state.get("artifacts", []):
        if art.get("pair_id") == "KIRA_ANDREY" and art.get("artifact_type") == "joint_control_test" and art.get("is_approved"):
            lines.append(f"{idx}. {art['artifact_id']} — {art['file_path']}")
            idx += 1
    lines.append("")
    lines.append("## Important rules")
    lines.append("")
    lines.append("- Do not use rejected/wrong-scene outputs as canon.")
    lines.append("- Do not overwrite approved joint tests.")
    lines.append("- Kira barefoot height remains 168 cm even when heels make her appear taller.")
    lines.append("- Andrey remains 180 cm.")
    lines.append("- Kira canon docs exist as .md.txt, not missing.")
    lines.append("- SQLite DB is local runtime memory and must not be committed.")
    lines.append("")
    lines.append("## Recent decisions")
    lines.append("")
    for dec in state.get("decisions", []):
        lines.append(f"- {dec['decision_id']} — {dec['title']}")
    lines.append("")
    lines.append("## Recent commits")
    lines.append("")
    for commit in state.get("commits", []):
        lines.append(f"- {commit['commit_hash']} — {commit['title']}")
    lines.append("")
    lines.append("## Next safe options")
    lines.append("")
    lines.append("1. Duo scene packs for KIRA_ANDREY")
    lines.append("2. ANDREY 3D reference pack")
    lines.append("3. KIRA 3D reference pack")
    lines.append("4. Next character canon pack")
    lines.append("5. Continue SQLite memory automation")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Export Voyage memory to tracked files.")
    parser.add_argument("--repo-root", default=".", help="Repository root directory.")
    parser.add_argument("--db", default=DEFAULT_DB, help="Path to SQLite DB.")
    parser.add_argument("--out-dir", default=".voyage", help="Output directory for exports.")
    args = parser.parse_args()

    db_path = Path(args.db).resolve()
    if not db_path.exists():
        print(f"DB not found: {db_path}")
        raise SystemExit(1)

    out_dir = Path(args.repo_root) / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(str(db_path))
    try:
        state = {
            "project": "narrative-character-canon",
            "generated_at": utc_now(),
            "meta": fetch_all(conn, "meta"),
            "characters": fetch_all(conn, "characters"),
            "pairs": fetch_all(conn, "pairs"),
            "artifacts": fetch_all(conn, "artifacts"),
            "tasks": fetch_all(conn, "tasks"),
            "decisions": fetch_all(conn, "decisions"),
            "commits": fetch_all(conn, "commits"),
            "events": fetch_all(conn, "events"),
        }
    finally:
        conn.close()

    snapshot_path = out_dir / "CONTEXT_SNAPSHOT.md"
    snapshot_path.write_text(build_context_snapshot(state), encoding="utf-8")

    state_path = out_dir / "STATE_EXPORT.json"
    state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    events_path = out_dir / "EVENTS_EXPORT.jsonl"
    with events_path.open("w", encoding="utf-8") as f:
        if state["events"]:
            for event in state["events"]:
                f.write(json.dumps(event, ensure_ascii=False) + "\n")
        else:
            f.write(
                json.dumps(
                    {
                        "event_id": "MEMORY_EXPORT_CREATED",
                        "event_type": "MEMORY_EXPORT_CREATED",
                        "subject_type": "project",
                        "subject_id": "narrative-character-canon",
                        "summary": "Memory export created.",
                        "payload_json": json.dumps({"source": "voyage_memory_export.py"}),
                        "commit_hash": None,
                        "created_at": utc_now(),
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

    print(f"Exported to {out_dir}")


if __name__ == "__main__":
    main()
