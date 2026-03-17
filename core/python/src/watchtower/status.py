"""Read-only workspace status helpers for the WatchTower bootstrap CLI."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from watchtower.work_items import list_work_items
from watchtower.workspace import doctor_payload, resolve_repo_root


def status_payload(repo_root: Path | None = None) -> dict[str, object]:
    root = repo_root or resolve_repo_root()
    payload = doctor_payload(root)
    if payload["workspace_status"] == "missing":
        payload["work_item_count"] = 0
        payload["counts_by_status"] = {}
        payload["recent_work_items"] = []
        return payload

    work_items = list_work_items(root)
    counts_by_status = Counter(str(item["status"]) for item in work_items)
    payload["work_item_count"] = len(work_items)
    payload["counts_by_status"] = dict(sorted(counts_by_status.items()))
    payload["recent_work_items"] = [
        {
            "slug": str(item["slug"]),
            "title": str(item["title"]),
            "status": str(item["status"]),
            "updated_at": str(item["updated_at"]),
        }
        for item in sorted(
            work_items,
            key=lambda item: (str(item["updated_at"]), str(item["slug"])),
            reverse=True,
        )[:5]
    ]
    return payload
