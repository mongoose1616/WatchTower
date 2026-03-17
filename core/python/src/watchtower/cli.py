"""Bootstrap CLI for the WatchTower product repo."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def _doctor_payload() -> dict[str, object]:
    repo_root = _repo_root()
    workspace_root = repo_root / "core" / "python"
    return {
        "status": "ok",
        "repo": "WatchTower",
        "repo_root": str(repo_root),
        "workspace_root": str(workspace_root),
        "bootstrap_stage": "initialized",
        "available_commands": ["doctor"],
    }


def _run_doctor(args: argparse.Namespace) -> int:
    payload = _doctor_payload()
    if args.format == "json":
        print(json.dumps(payload, indent=2))
        return 0

    print("WatchTower bootstrap status: ok")
    print(f"repo_root: {payload['repo_root']}")
    print(f"workspace_root: {payload['workspace_root']}")
    print(f"bootstrap_stage: {payload['bootstrap_stage']}")
    print("available_commands: doctor")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="watchtower",
        description="Bootstrap CLI for the WatchTower product repo.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor = subparsers.add_parser(
        "doctor",
        help="Report the current bootstrap status.",
    )
    doctor.add_argument(
        "--format",
        choices=("human", "json"),
        default="human",
        help="Select human-readable or JSON output.",
    )
    doctor.set_defaults(handler=_run_doctor)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    handler = getattr(args, "handler", None)
    if handler is None:
        parser.print_help()
        return 0
    return int(handler(args))
