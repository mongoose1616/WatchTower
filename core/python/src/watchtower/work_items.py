"""Local-first work-item helpers for the WatchTower bootstrap CLI."""

from __future__ import annotations

import json
import re
from pathlib import Path

from watchtower.workspace import load_workspace_manifest, resolve_repo_root, state_root, utc_timestamp_now

_SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")


def work_items_root(repo_root: Path | None = None) -> Path:
    root = repo_root or resolve_repo_root()
    return state_root(root) / "work_items"


def work_item_path(slug: str, repo_root: Path | None = None) -> Path:
    return work_items_root(repo_root) / f"{slug}.json"


def load_work_item(slug: str, repo_root: Path | None = None) -> dict[str, object]:
    root = repo_root or resolve_repo_root()
    _require_workspace_manifest(root)
    return _load_existing_work_item(slug, root)


def list_work_items(repo_root: Path | None = None) -> list[dict[str, object]]:
    root = repo_root or resolve_repo_root()
    _require_workspace_manifest(root)
    items: list[dict[str, object]] = []
    for path in sorted(work_items_root(root).glob("*.json")):
        items.append(json.loads(path.read_text(encoding="utf-8")))
    return items


def select_next_work_item(
    repo_root: Path | None = None,
) -> tuple[dict[str, object] | None, dict[str, object] | None]:
    root = repo_root or resolve_repo_root()
    work_items = list_work_items(root)
    unfinished = [
        item for item in work_items if str(item.get("status")) != "completed"
    ]
    if not unfinished:
        return None, None

    work_item = sorted(
        unfinished,
        key=lambda item: (
            str(item.get("updated_at", "")),
            str(item.get("slug", "")),
        ),
        reverse=True,
    )[0]
    notes = work_item.get("notes", [])
    latest_note = notes[-1] if notes else None
    return work_item, latest_note


def create_work_item(
    slug: str,
    title: str,
    repo_root: Path | None = None,
) -> tuple[dict[str, object], bool]:
    if not _SLUG_PATTERN.fullmatch(slug):
        raise ValueError("Work item slug must use lower-case letters, numbers, and underscores only.")

    root = repo_root or resolve_repo_root()
    manifest = _require_workspace_manifest(root)

    path = work_item_path(slug, root)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8")), False

    timestamp = utc_timestamp_now()
    document = {
        "work_item_id": f"work_item.{slug}",
        "slug": slug,
        "title": title,
        "status": "planned",
        "created_at": timestamp,
        "updated_at": timestamp,
        "workspace_manifest_path": str(manifest["manifest_path"]),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"{json.dumps(document, indent=2)}\n", encoding="utf-8")
    return document, True


def complete_work_item(
    slug: str,
    summary: str | None = None,
    repo_root: Path | None = None,
) -> tuple[dict[str, object], bool]:
    root = repo_root or resolve_repo_root()
    _require_workspace_manifest(root)

    path = work_item_path(slug, root)
    document = _load_existing_work_item(slug, root)
    if document.get("status") == "completed":
        return document, False

    timestamp = utc_timestamp_now()
    document["status"] = "completed"
    document["updated_at"] = timestamp
    document["completed_at"] = timestamp
    if summary:
        document["completion_summary"] = summary

    path.write_text(f"{json.dumps(document, indent=2)}\n", encoding="utf-8")
    return document, True


def append_work_item_note(
    slug: str,
    message: str,
    repo_root: Path | None = None,
) -> tuple[dict[str, object], dict[str, object]]:
    normalized_message = message.strip()
    if not normalized_message:
        raise ValueError("Work item note message must not be empty.")

    root = repo_root or resolve_repo_root()
    _require_workspace_manifest(root)

    path = work_item_path(slug, root)
    document = _load_existing_work_item(slug, root)
    timestamp = utc_timestamp_now()
    notes = list(document.get("notes", []))
    note = {
        "note_id": f"work_item_note.{slug}.{len(notes) + 1:04d}",
        "created_at": timestamp,
        "message": normalized_message,
    }
    notes.append(note)
    document["notes"] = notes
    document["updated_at"] = timestamp

    path.write_text(f"{json.dumps(document, indent=2)}\n", encoding="utf-8")
    return document, note


def _require_workspace_manifest(repo_root: Path) -> dict[str, object]:
    manifest = load_workspace_manifest(repo_root)
    if manifest is None:
        raise RuntimeError("WatchTower workspace is not initialized. Run `watchtower init` first.")
    return manifest


def _load_existing_work_item(slug: str, repo_root: Path) -> dict[str, object]:
    path = work_item_path(slug, repo_root)
    if not path.exists():
        raise ValueError(f"Unknown work item: {slug}")
    return json.loads(path.read_text(encoding="utf-8"))
