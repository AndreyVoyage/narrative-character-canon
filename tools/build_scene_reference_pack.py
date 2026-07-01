#!/usr/bin/env python3
"""Build a GitHub-first scene reference pack for image generation."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


GITHUB_BLOB_BASE = "https://github.com/AndreyVoyage/narrative-character-canon/blob/main/"
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/AndreyVoyage/narrative-character-canon/main/"
DEFAULT_REPO_ROOT = r"C:\DEV\Narrative\narrative-character-canon"
DEFAULT_OUTPUT_ROOT = r"C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\scene_packs"
FALLBACK_PRESETS = {
    "evening_walk": ["evening", "portrait"],
    "yoga": ["sports", "body_canon"],
    "beach": ["body_canon", "portrait"],
    "expression_test": ["portrait"],
    "sauna": ["body_canon", "portrait"],
    "bar": ["evening", "portrait"],
    "formal": ["portrait"],
    "sports": ["body_canon", "portrait"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a local scene reference pack with GitHub paths, raw links, and an embedded prompt."
    )
    parser.add_argument("--characters", required=True, help="Comma-separated character IDs, e.g. KIRA,ANDREY")
    parser.add_argument("--scene", required=True, help="Scene preset name, e.g. sauna")
    parser.add_argument("--description", required=True, help="Short user scene description")
    parser.add_argument("--repo-root", default=DEFAULT_REPO_ROOT, help="Repository root")
    parser.add_argument("--output-root", default=DEFAULT_OUTPUT_ROOT, help="Local output root for scene packs")
    return parser.parse_args()


def normalize_character(value: str) -> str:
    return value.strip().upper()


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9а-яё_-]+", "_", value, flags=re.IGNORECASE)
    value = re.sub(r"_+", "_", value).strip("_")
    return value or "scene"


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8", newline="\n")


def rel_to_path(repo_root: Path, rel_path: str) -> Path:
    return repo_root / Path(rel_path.replace("/", "\\"))


def link_for(rel_path: str, raw: bool = False) -> str:
    safe = rel_path.replace("\\", "/")
    return (GITHUB_RAW_BASE if raw else GITHUB_BLOB_BASE) + safe


def is_git_tracked(repo_root: Path, rel_path: str) -> bool | None:
    git_dir = repo_root / ".git"
    if not git_dir.exists():
        return None
    try:
        result = subprocess.run(
            ["git", "ls-files", "--error-unmatch", rel_path.replace("\\", "/")],
            cwd=str(repo_root),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        return result.returncode == 0
    except OSError:
        return None


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(read_text(path))


def select_preset(scene: str, presets: dict[str, Any]) -> tuple[str | None, dict[str, Any] | None, str | None]:
    if scene in presets:
        return scene, presets[scene], None
    for candidate in FALLBACK_PRESETS.get(scene, []):
        if candidate in presets:
            return candidate, presets[candidate], f"Requested scene '{scene}' not found; used fallback preset '{candidate}'."
    for candidate in ("portrait", "body_canon"):
        if candidate in presets:
            return candidate, presets[candidate], f"Requested scene '{scene}' not found; used generic fallback preset '{candidate}'."
    return None, None, f"Requested scene '{scene}' not found and no fallback preset is available."


def compact_canon(label: str, text: str, limit: int = 1800) -> str:
    cleaned_lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.lower().startswith(("path:", "version:", "last updated:", "local visual update:")):
            continue
        cleaned_lines.append(stripped)
    compact = " ".join(cleaned_lines)
    compact = re.sub(r"\s+", " ", compact).strip()
    if len(compact) > limit:
        compact = compact[:limit].rsplit(" ", 1)[0] + "..."
    return f"{label}: {compact}" if compact else f"{label}: no readable canon text found."


def scene_hints(scene: str, description: str) -> dict[str, str]:
    lowered = f"{scene} {description}".lower()
    hints = {
        "environment": "cinematic realistic environment matching the user description",
        "composition": "clear two-character composition, stable identities, readable faces, natural body proportions",
        "clothing": "clothing must follow the requested scene and remain tasteful, non-explicit, and production-safe",
        "mood": "natural, emotionally believable, cinematic, warm human interaction",
    }
    if "sauna" in lowered or "саун" in lowered or "бан" in lowered:
        hints.update(
            {
                "environment": "warm wooden sauna or bathhouse interior, soft steam, warm practical light, towels, spa atmosphere",
                "composition": "Kira and Andrey together in a calm conversational moment, seated or standing naturally, both visible enough to preserve identity",
                "clothing": "both adults wrapped in towels up to the waist or chest as appropriate, tasteful non-explicit framing, no nudity",
                "mood": "intimate but calm conversation, relaxed trust, warm steam, cinematic realism",
            }
        )
    elif "bar" in lowered or "бар" in lowered:
        hints.update(
            {
                "environment": "warm evening bar or lounge interior with cinematic practical lights",
                "composition": "natural conversation, close but readable framing, both identities clear",
                "clothing": "elegant evening or smart casual clothing based on references",
                "mood": "warm, private, romantic or thoughtful conversation",
            }
        )
    elif "sport" in lowered or "yoga" in lowered or "спорт" in lowered or "йог" in lowered:
        hints.update(
            {
                "environment": "clean athletic studio, gym, yoga room, or outdoor sports setting",
                "composition": "full-body or three-quarter pose preserving body canon",
                "clothing": "athletic clothing suitable for the selected activity",
                "mood": "focused, energetic, natural movement",
            }
        )
    return hints


def suggested_filename(characters: list[str], scene: str, description: str) -> str:
    base = "_".join(characters)
    detail = slugify(description)
    if len(detail) > 42:
        detail = detail[:42].rstrip("_")
    return f"{base}_test01_{slugify(scene)}_{detail}_v1.png"


def build_prompt(
    scene: str,
    description: str,
    characters: list[str],
    selected: list[dict[str, Any]],
    filename: str,
) -> str:
    hints = scene_hints(scene, description)
    parts = [
        "FINAL IMAGE GENERATION PROMPT",
        "",
        f"Scene: {scene}",
        f"User description: {description}",
        "",
        "Create a cinematic realistic image based on the uploaded reference images and the embedded character canon below.",
        "",
        "Scene environment:",
        hints["environment"],
        "",
        "Composition:",
        hints["composition"],
        "",
        "Clothing / styling:",
        hints["clothing"],
        "",
        "Pose / body language:",
        "Natural body language that fits the scene. Preserve each character's age, proportions, facial structure, hair, and expression canon. Avoid identity drift.",
        "",
        "Mood / light / atmosphere:",
        hints["mood"],
        "",
        "Embedded character canon:",
    ]
    for item in selected:
        parts.append("")
        parts.append(f"--- {item['character']} ---")
        parts.append(f"Selected preset: {item.get('selected_preset')}")
        parts.append(f"Preset goal: {item.get('prompt_goal')}")
        for source_name, summary in item.get("canon_summaries", {}).items():
            parts.append(compact_canon(source_name, summary, limit=1600))
    parts.extend(
        [
            "",
            "Reference image instructions:",
            "Use the uploaded images only as identity, body, outfit, expression, and proportion references. Do not copy layout artifacts, sheet borders, labels, or collage formatting.",
            "",
            "Constraints:",
            "- adult characters only;",
            "- tasteful, non-explicit, production-safe framing;",
            "- preserve face canon and body canon for every character;",
            "- avoid changing age, body type, hair color, eye color, facial structure, or character ethnicity;",
            "- no extra people unless explicitly requested;",
            "- no distorted hands, duplicate faces, mismatched eye color, plastic skin, oversexualized posing, or random costume drift;",
            "",
            "Negative notes:",
            "No nudity, no explicit sexual content, no underage appearance, no identity swap, no face merge, no overly muscular drift, no mannequin skin, no low-detail faces, no watermark, no text, no logo.",
            "",
            f"Suggested save filename: {filename}",
        ]
    )
    return "\n".join(parts) + "\n"


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    output_root = Path(args.output_root).resolve()
    scene = slugify(args.scene)
    characters = [normalize_character(c) for c in args.characters.split(",") if c.strip()]
    if not characters:
        print("ERROR: no characters provided", file=sys.stderr)
        return 2

    missing: list[str] = []
    warnings: list[str] = []
    selected: list[dict[str, Any]] = []

    for character in characters:
        preset_rel = f"AI_CHARACTERS/{character}/10_notes/{character}_REFERENCE_PRESETS.json"
        preset_path = rel_to_path(repo_root, preset_rel)
        if not preset_path.exists():
            missing.append(preset_rel)
            continue
        preset_doc = load_json(preset_path)
        selected_name, preset, warning = select_preset(scene, preset_doc.get("scene_presets", {}))
        if warning:
            warnings.append(f"{character}: {warning}")
        if not preset or not selected_name:
            continue

        image_entries = []
        for rel_path in preset.get("reference_images", []):
            exists = rel_to_path(repo_root, rel_path).exists()
            if not exists:
                missing.append(rel_path)
            tracked = is_git_tracked(repo_root, rel_path)
            if exists and tracked is False:
                missing.append(f"{rel_path} (not tracked by git; GitHub raw link may not work)")
            image_entries.append(
                {
                    "path": rel_path,
                    "exists": exists,
                    "git_tracked": tracked,
                    "github": link_for(rel_path),
                    "raw": link_for(rel_path, raw=True),
                }
            )

        canon_summaries: dict[str, str] = {}
        text_sources = preset_doc.get("text_sources", {})
        text_source_entries = []
        for source_name, rel_path in text_sources.items():
            exists = rel_to_path(repo_root, rel_path).exists()
            if not exists:
                missing.append(rel_path)
                content = ""
            else:
                content = read_text(rel_to_path(repo_root, rel_path))
            tracked = is_git_tracked(repo_root, rel_path)
            if exists and tracked is False:
                warnings.append(f"{character}: text source is local but not tracked by git: {rel_path}")
            text_source_entries.append(
                {
                    "name": source_name,
                    "path": rel_path,
                    "exists": exists,
                    "git_tracked": tracked,
                    "github": link_for(rel_path),
                    "raw": link_for(rel_path, raw=True),
                }
            )
            if content:
                canon_summaries[source_name] = content

        selected.append(
            {
                "character": character,
                "selected_preset": selected_name,
                "requested_scene": scene,
                "description": preset.get("description", ""),
                "prompt_goal": preset.get("prompt_goal", ""),
                "reference_images": image_entries,
                "text_sources": text_source_entries,
                "canon_summaries": canon_summaries,
            }
        )

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    output_dir = output_root / f"{timestamp}_{scene}_{'_'.join(characters)}"
    output_dir.mkdir(parents=True, exist_ok=True)

    status = "COMPLETE" if not missing else "INCOMPLETE"
    filename = suggested_filename(characters, scene, args.description)

    pack = {
        "status": status,
        "scene": scene,
        "characters": characters,
        "user_description": args.description,
        "generated_at": timestamp,
        "repo_root": str(repo_root),
        "output_dir": str(output_dir),
        "suggested_save_filename": filename,
        "warnings": warnings,
        "missing_files": sorted(set(missing)),
        "selected": selected,
    }

    md_lines = [
        "# Scene Reference Pack",
        "",
        f"Status: {status}",
        f"Scene: {scene}",
        f"Characters: {', '.join(characters)}",
        f"User description: {args.description}",
        f"Suggested save filename: `{filename}`",
        "",
        "## Selected Presets",
    ]
    for item in selected:
        md_lines.extend(
            [
                "",
                f"### {item['character']}",
                f"Requested scene: `{item['requested_scene']}`",
                f"Selected preset: `{item['selected_preset']}`",
                f"Preset description: {item['description']}",
                f"Prompt goal: {item['prompt_goal']}",
                "",
                "Image references to upload manually:",
            ]
        )
        for image in item["reference_images"]:
            tracked_note = "" if image.get("git_tracked") in (True, None) else " / NOT TRACKED"
            mark = "OK" if image["exists"] and image.get("git_tracked") is not False else "MISSING"
            md_lines.append(f"- [{mark}] `{image['path']}`")
            if tracked_note:
                md_lines.append(f"  - Git tracking: {tracked_note.strip(' / ')}")
            md_lines.append(f"  - GitHub: {image['github']}")
            md_lines.append(f"  - Raw: {image['raw']}")
        md_lines.extend(["", "Text sources embedded in prompt:"])
        for source in item["text_sources"]:
            mark = "OK" if source["exists"] else "MISSING"
            md_lines.append(f"- [{mark}] {source['name']}: `{source['path']}`")

    md_lines.extend(["", "## Suggested Upload List"])
    for item in selected:
        md_lines.append("")
        md_lines.append(f"### {item['character']}")
        for image in item["reference_images"]:
            md_lines.append(f"- `{image['path']}`")

    if warnings:
        md_lines.extend(["", "## Warnings"])
        md_lines.extend(f"- {warning}" for warning in warnings)
    if missing:
        md_lines.extend(["", "## Missing Files"])
        md_lines.extend(f"- `{path}`" for path in sorted(set(missing)))
    md_lines.extend(["", "## Completion Status", status, ""])

    raw_lines = ["# Scene Raw Links", ""]
    for item in selected:
        raw_lines.append(f"## {item['character']}")
        raw_lines.append("")
        for image in item["reference_images"]:
            raw_lines.append(f"- {image['raw']}")
        raw_lines.append("")

    write_text(output_dir / "SCENE_REFERENCE_PACK.md", "\n".join(md_lines))
    write_text(output_dir / "SCENE_RAW_LINKS.md", "\n".join(raw_lines))
    write_text(output_dir / "SCENE_PROMPT.txt", build_prompt(scene, args.description, characters, selected, filename))
    write_text(output_dir / "SCENE_PACK.json", json.dumps(pack, ensure_ascii=False, indent=2))

    print(f"Status: {status}")
    print(f"Output: {output_dir}")
    if missing:
        print("Missing files:")
        for path in sorted(set(missing)):
            print(f"- {path}")
    return 0 if status == "COMPLETE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
