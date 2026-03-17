"""Local-first workspace state helpers for the WatchTower bootstrap CLI."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

_REPO_ROOT_ENV = "WATCHTOWER_REPO_ROOT"
AVAILABLE_COMMANDS = (
    "doctor",
    "status",
    "init",
    "work start",
    "work list",
    "work next",
    "work show",
    "work note",
    "work complete",
)


def resolve_repo_root() -> Path:
    override = os.environ.get(_REPO_ROOT_ENV)
    if override:
        return Path(override).expanduser().resolve()
    return Path(__file__).resolve().parents[4]


def workspace_root(repo_root: Path | None = None) -> Path:
    root = repo_root or resolve_repo_root()
    return root / "core" / "python"


def state_root(repo_root: Path | None = None) -> Path:
    root = repo_root or resolve_repo_root()
    return root / ".watchtower"


def manifest_path(repo_root: Path | None = None) -> Path:
    return state_root(repo_root) / "workspace.json"


def utc_timestamp_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def load_workspace_manifest(repo_root: Path | None = None) -> dict[str, object] | None:
    path = manifest_path(repo_root)
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def ensure_workspace_manifest(repo_root: Path | None = None) -> tuple[dict[str, object], bool]:
    root = repo_root or resolve_repo_root()
    path = manifest_path(root)
    existing = load_workspace_manifest(root)
    if existing is not None:
        return existing, False

    timestamp = utc_timestamp_now()
    document = {
        "workspace_version": 1,
        "workspace_status": "initialized",
        "repo": "WatchTower",
        "repo_root": str(root),
        "workspace_root": str(workspace_root(root)),
        "state_root": str(state_root(root)),
        "manifest_path": str(path),
        "created_at": timestamp,
        "updated_at": timestamp,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"{json.dumps(document, indent=2)}\n", encoding="utf-8")
    return document, True


def doctor_payload(repo_root: Path | None = None) -> dict[str, object]:
    root = repo_root or resolve_repo_root()
    manifest = load_workspace_manifest(root)
    payload = {
        "status": "ok",
        "repo": "WatchTower",
        "repo_root": str(root),
        "workspace_root": str(workspace_root(root)),
        "state_root": str(state_root(root)),
        "workspace_manifest_path": str(manifest_path(root)),
        "available_commands": list(AVAILABLE_COMMANDS),
    }
    if manifest is None:
        payload["bootstrap_stage"] = "repo_bootstrap"
        payload["workspace_status"] = "missing"
        return payload

    payload["bootstrap_stage"] = "workspace_initialized"
    payload["workspace_status"] = str(manifest.get("workspace_status", "initialized"))
    payload["workspace_manifest"] = manifest
    return payload
