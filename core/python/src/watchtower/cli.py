"""Bootstrap CLI for the WatchTower product repo."""

from __future__ import annotations

import argparse
import json
from typing import Sequence
from watchtower.workspace import doctor_payload, ensure_workspace_manifest


def _run_doctor(args: argparse.Namespace) -> int:
    payload = doctor_payload()
    if args.format == "json":
        print(json.dumps(payload, indent=2))
        return 0

    print("WatchTower bootstrap status: ok")
    print(f"repo_root: {payload['repo_root']}")
    print(f"workspace_root: {payload['workspace_root']}")
    print(f"state_root: {payload['state_root']}")
    print(f"bootstrap_stage: {payload['bootstrap_stage']}")
    print(f"workspace_status: {payload['workspace_status']}")
    print("available_commands: doctor, init")
    return 0


def _run_init(args: argparse.Namespace) -> int:
    manifest, created = ensure_workspace_manifest()
    payload = {
        "status": "ok",
        "action": "created" if created else "exists",
        "workspace_manifest": manifest,
        "available_commands": ["doctor", "init"],
    }
    if args.format == "json":
        print(json.dumps(payload, indent=2))
        return 0

    action = "initialized" if created else "already initialized"
    print(f"WatchTower workspace {action}")
    print(f"state_root: {manifest['state_root']}")
    print(f"workspace_manifest_path: {manifest['manifest_path']}")
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

    init = subparsers.add_parser(
        "init",
        help="Create the local WatchTower workspace manifest.",
    )
    init.add_argument(
        "--format",
        choices=("human", "json"),
        default="human",
        help="Select human-readable or JSON output.",
    )
    init.set_defaults(handler=_run_init)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    handler = getattr(args, "handler", None)
    if handler is None:
        parser.print_help()
        return 0
    return int(handler(args))
