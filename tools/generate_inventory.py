#!/usr/bin/env python3
"""Generate INVENTORY.md for the repository."""
from __future__ import annotations

import datetime
import os
import pathlib
import sys
from collections import Counter


def human_tree(root: pathlib.Path, prefix: str = "", exclude: set[str] | None = None) -> list[str]:
    """Return tree lines similar to the `tree` command."""
    if exclude is None:
        exclude = {".git", "LOCAL_STORAGE", "voyage_memory"}
    lines: list[str] = []
    try:
        entries = [e for e in root.iterdir() if e.name not in exclude]
    except PermissionError:
        return lines
    dirs = sorted([e for e in entries if e.is_dir()], key=lambda x: x.name.lower())
    files = sorted([e for e in entries if e.is_file()], key=lambda x: x.name.lower())
    entries_ordered = dirs + files
    for i, entry in enumerate(entries_ordered):
        is_last = i == len(entries_ordered) - 1
        connector = "└── " if is_last else "├── "
        if entry.is_dir():
            lines.append(f"{prefix}{connector}{entry.name}/")
            extension = "    " if is_last else "│   "
            lines.extend(human_tree(entry, prefix + extension, exclude=exclude))
        else:
            lines.append(f"{prefix}{connector}{entry.name}")
    return lines


def format_size(size: int) -> str:
    return str(size)


def format_time(ts: float) -> str:
    dt = datetime.datetime.fromtimestamp(ts)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def main() -> int:
    repo_root = pathlib.Path(".")
    inventory_path = repo_root / "INVENTORY.md"
    exclude = {".git", "LOCAL_STORAGE", "voyage_memory"}

    # Gather all tracked-ish files (everything on disk under repo root, excluding .git and local storage)
    all_files: list[pathlib.Path] = []
    for dirpath, dirnames, filenames in os.walk(repo_root):
        dp = pathlib.Path(dirpath)
        # Prune excluded directories
        dirnames[:] = [d for d in dirnames if d not in exclude]
        for fn in filenames:
            all_files.append(dp / fn)

    all_files.sort(key=lambda p: str(p).lower())

    # Tree
    tree_lines = human_tree(repo_root, exclude=exclude)

    # Counts
    total_files = len(all_files)
    ext_counter: Counter[str] = Counter()
    for f in all_files:
        ext = f.suffix
        if not ext:
            ext = "(no extension)"
        ext_counter[ext] += 1

    # File list rows
    rows: list[tuple[str, str, str]] = []
    for f in all_files:
        rel = f.relative_to(repo_root).as_posix()
        stat = f.stat()
        rows.append((rel, format_size(stat.st_size), format_time(stat.st_mtime)))

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    repo_path = repo_root.resolve().as_posix().replace("/c/", "C:\\").replace("/", "\\")

    lines: list[str] = []
    lines.append("# INVENTORY.md")
    lines.append("")
    lines.append("Repository:")
    lines.append("")
    lines.append(repo_path)
    lines.append("")
    lines.append("Generated:")
    lines.append("")
    lines.append(now)
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("# Folder and file tree")
    lines.append("")
    lines.append("```text")
    for tree_line in tree_lines:
        lines.append(tree_line)
    lines.append("```")
    lines.append("")
    lines.append("# Total file count")
    lines.append("")
    lines.append(str(total_files))
    lines.append("")
    lines.append("# File type summary")
    lines.append("")
    lines.append("| Extension | Count |")
    lines.append("|---|---:|")
    for ext, count in sorted(ext_counter.items(), key=lambda x: (x[0] != "(no extension)", x[0].lower())):
        display = ext if ext != "(no extension)" else "(no extension)"
        lines.append(f"| {display} | {count} |")
    lines.append("")
    lines.append("# File list")
    lines.append("")
    lines.append("| Path | Size bytes | Modified |")
    lines.append("|---|---:|---|")
    for rel, size, mtime in rows:
        lines.append(f"| {rel} | {size} | {mtime} |")
    lines.append("")

    inventory_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated {inventory_path} ({total_files} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
