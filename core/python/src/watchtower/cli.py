"""Bootstrap CLI for the WatchTower product repo."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Sequence
from watchtower.work_items import (
    append_work_item_note,
    begin_work_item,
    complete_work_item,
    create_work_item,
    list_work_items,
    load_work_item,
    select_next_work_item,
    work_item_path,
)
from watchtower.status import status_payload
from watchtower.workspace import AVAILABLE_COMMANDS, doctor_payload, ensure_workspace_manifest


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
    print(f"available_commands: {', '.join(AVAILABLE_COMMANDS)}")
    return 0


def _run_init(args: argparse.Namespace) -> int:
    manifest, created = ensure_workspace_manifest()
    payload = {
        "status": "ok",
        "action": "created" if created else "exists",
        "workspace_manifest": manifest,
        "available_commands": list(AVAILABLE_COMMANDS),
    }
    if args.format == "json":
        print(json.dumps(payload, indent=2))
        return 0

    action = "initialized" if created else "already initialized"
    print(f"WatchTower workspace {action}")
    print(f"state_root: {manifest['state_root']}")
    print(f"workspace_manifest_path: {manifest['manifest_path']}")
    return 0


def _run_status(args: argparse.Namespace) -> int:
    payload = status_payload()
    if args.format == "json":
        print(json.dumps(payload, indent=2))
        return 0

    print("WatchTower status")
    print(f"bootstrap_stage: {payload['bootstrap_stage']}")
    print(f"workspace_status: {payload['workspace_status']}")
    print(f"work_item_count: {payload['work_item_count']}")
    counts_by_status = payload["counts_by_status"]
    rendered_counts = (
        ", ".join(f"{status}={count}" for status, count in counts_by_status.items())
        if counts_by_status
        else "none"
    )
    print(f"counts_by_status: {rendered_counts}")
    recent_items = payload["recent_work_items"]
    if recent_items:
        print("recent_work_items:")
        for item in recent_items:
            print(f"- {item['slug']}: {item['status']} :: {item['title']}")
    return 0


def _run_work_start(args: argparse.Namespace) -> int:
    try:
        work_item, created = create_work_item(args.slug, args.title)
    except (RuntimeError, ValueError) as error:
        if args.format == "json":
            print(json.dumps({"status": "error", "message": str(error)}, indent=2))
        else:
            print(str(error), file=sys.stderr)
        return 1

    payload = {
        "status": "ok",
        "action": "created" if created else "exists",
        "work_item": work_item,
        "work_item_path": str(work_item_path(args.slug)),
    }
    if args.format == "json":
        print(json.dumps(payload, indent=2))
        return 0

    action = "created" if created else "already exists"
    print(f"WatchTower work item {action}")
    print(f"work_item_id: {work_item['work_item_id']}")
    print(f"work_item_path: {payload['work_item_path']}")
    return 0


def _run_work_begin(args: argparse.Namespace) -> int:
    try:
        work_item, changed = begin_work_item(args.slug)
    except (RuntimeError, ValueError) as error:
        if args.format == "json":
            print(json.dumps({"status": "error", "message": str(error)}, indent=2))
        else:
            print(str(error), file=sys.stderr)
        return 1

    payload = {
        "status": "ok",
        "action": "begun" if changed else "already_in_progress",
        "work_item": work_item,
        "work_item_path": str(work_item_path(args.slug)),
    }
    if args.format == "json":
        print(json.dumps(payload, indent=2))
        return 0

    action = "begun" if changed else "already in progress"
    print(f"WatchTower work item {action}")
    print(f"work_item_id: {work_item['work_item_id']}")
    print(f"work_item_path: {payload['work_item_path']}")
    return 0


def _run_work_list(args: argparse.Namespace) -> int:
    try:
        work_items = list_work_items()
    except (RuntimeError, ValueError) as error:
        if args.format == "json":
            print(json.dumps({"status": "error", "message": str(error)}, indent=2))
        else:
            print(str(error), file=sys.stderr)
        return 1

    payload = {
        "status": "ok",
        "work_item_count": len(work_items),
        "work_items": work_items,
    }
    if args.format == "json":
        print(json.dumps(payload, indent=2))
        return 0

    print(f"WatchTower work items: {len(work_items)}")
    for work_item in work_items:
        print(f"- {work_item['slug']}: {work_item['status']} :: {work_item['title']}")
    return 0


def _run_work_next(args: argparse.Namespace) -> int:
    try:
        work_item, latest_note = select_next_work_item()
    except (RuntimeError, ValueError) as error:
        if args.format == "json":
            print(json.dumps({"status": "error", "message": str(error)}, indent=2))
        else:
            print(str(error), file=sys.stderr)
        return 1

    payload = {"status": "ok"}
    if work_item is None:
        payload["action"] = "none_available"
        payload["work_item"] = None
        payload["latest_note"] = None
        if args.format == "json":
            print(json.dumps(payload, indent=2))
            return 0
        print("WatchTower next work: none available")
        return 0

    payload["action"] = "selected"
    payload["work_item"] = work_item
    payload["latest_note"] = latest_note
    payload["work_item_path"] = str(work_item_path(str(work_item["slug"])))
    if args.format == "json":
        print(json.dumps(payload, indent=2))
        return 0

    print("WatchTower next work")
    print(f"slug: {work_item['slug']}")
    print(f"title: {work_item['title']}")
    print(f"status: {work_item['status']}")
    if latest_note is not None:
        print(f"latest_note: {latest_note['message']}")
    print(f"work_item_path: {payload['work_item_path']}")
    return 0


def _run_work_show(args: argparse.Namespace) -> int:
    try:
        work_item = load_work_item(args.slug)
    except (RuntimeError, ValueError) as error:
        if args.format == "json":
            print(json.dumps({"status": "error", "message": str(error)}, indent=2))
        else:
            print(str(error), file=sys.stderr)
        return 1

    payload = {
        "status": "ok",
        "work_item": work_item,
        "work_item_path": str(work_item_path(args.slug)),
    }
    if args.format == "json":
        print(json.dumps(payload, indent=2))
        return 0

    print(f"WatchTower work item: {work_item['slug']}")
    print(f"title: {work_item['title']}")
    print(f"status: {work_item['status']}")
    notes = work_item.get("notes", [])
    print(f"note_count: {len(notes)}")
    if notes:
        print("notes:")
        for note in notes:
            print(f"- {note['created_at']}: {note['message']}")
    print(f"work_item_path: {payload['work_item_path']}")
    return 0


def _run_work_note(args: argparse.Namespace) -> int:
    try:
        work_item, note = append_work_item_note(args.slug, args.message)
    except (RuntimeError, ValueError) as error:
        if args.format == "json":
            print(json.dumps({"status": "error", "message": str(error)}, indent=2))
        else:
            print(str(error), file=sys.stderr)
        return 1

    payload = {
        "status": "ok",
        "action": "noted",
        "note": note,
        "work_item": work_item,
        "work_item_path": str(work_item_path(args.slug)),
    }
    if args.format == "json":
        print(json.dumps(payload, indent=2))
        return 0

    print("WatchTower work item note recorded")
    print(f"work_item_id: {work_item['work_item_id']}")
    print(f"note_id: {note['note_id']}")
    print(f"work_item_path: {payload['work_item_path']}")
    return 0


def _run_work_complete(args: argparse.Namespace) -> int:
    try:
        work_item, changed = complete_work_item(args.slug, summary=args.summary)
    except (RuntimeError, ValueError) as error:
        if args.format == "json":
            print(json.dumps({"status": "error", "message": str(error)}, indent=2))
        else:
            print(str(error), file=sys.stderr)
        return 1

    payload = {
        "status": "ok",
        "action": "completed" if changed else "already_completed",
        "work_item": work_item,
        "work_item_path": str(work_item_path(args.slug)),
    }
    if args.format == "json":
        print(json.dumps(payload, indent=2))
        return 0

    action = "completed" if changed else "already completed"
    print(f"WatchTower work item {action}")
    print(f"work_item_id: {work_item['work_item_id']}")
    print(f"work_item_path: {payload['work_item_path']}")
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

    status = subparsers.add_parser(
        "status",
        help="Report the current workspace and work-item snapshot.",
    )
    status.add_argument(
        "--format",
        choices=("human", "json"),
        default="human",
        help="Select human-readable or JSON output.",
    )
    status.set_defaults(handler=_run_status)

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

    work = subparsers.add_parser(
        "work",
        help="Manage local WatchTower work-item records.",
    )
    work_subparsers = work.add_subparsers(dest="work_command", required=True)

    work_start = work_subparsers.add_parser(
        "start",
        help="Create a local work-item record inside the initialized workspace.",
    )
    work_start.add_argument("--slug", required=True, help="Stable work-item slug.")
    work_start.add_argument("--title", required=True, help="Human-readable work-item title.")
    work_start.add_argument(
        "--format",
        choices=("human", "json"),
        default="human",
        help="Select human-readable or JSON output.",
    )
    work_start.set_defaults(handler=_run_work_start)

    work_begin = work_subparsers.add_parser(
        "begin",
        help="Mark one local work-item record in progress.",
    )
    work_begin.add_argument("--slug", required=True, help="Stable work-item slug.")
    work_begin.add_argument(
        "--format",
        choices=("human", "json"),
        default="human",
        help="Select human-readable or JSON output.",
    )
    work_begin.set_defaults(handler=_run_work_begin)

    work_list = work_subparsers.add_parser(
        "list",
        help="List local work-item records from the initialized workspace.",
    )
    work_list.add_argument(
        "--format",
        choices=("human", "json"),
        default="human",
        help="Select human-readable or JSON output.",
    )
    work_list.set_defaults(handler=_run_work_list)

    work_next = work_subparsers.add_parser(
        "next",
        help="Select the next unfinished local work-item record to resume.",
    )
    work_next.add_argument(
        "--format",
        choices=("human", "json"),
        default="human",
        help="Select human-readable or JSON output.",
    )
    work_next.set_defaults(handler=_run_work_next)

    work_show = work_subparsers.add_parser(
        "show",
        help="Show one local work-item record from the initialized workspace.",
    )
    work_show.add_argument("--slug", required=True, help="Stable work-item slug.")
    work_show.add_argument(
        "--format",
        choices=("human", "json"),
        default="human",
        help="Select human-readable or JSON output.",
    )
    work_show.set_defaults(handler=_run_work_show)

    work_note = work_subparsers.add_parser(
        "note",
        help="Append one note to an existing local work-item record.",
    )
    work_note.add_argument("--slug", required=True, help="Stable work-item slug.")
    work_note.add_argument(
        "--message",
        required=True,
        help="Note text to append to the work-item record.",
    )
    work_note.add_argument(
        "--format",
        choices=("human", "json"),
        default="human",
        help="Select human-readable or JSON output.",
    )
    work_note.set_defaults(handler=_run_work_note)

    work_complete = work_subparsers.add_parser(
        "complete",
        help="Mark one local work-item record completed.",
    )
    work_complete.add_argument("--slug", required=True, help="Stable work-item slug.")
    work_complete.add_argument(
        "--summary",
        help="Optional closeout summary recorded on the completed work item.",
    )
    work_complete.add_argument(
        "--format",
        choices=("human", "json"),
        default="human",
        help="Select human-readable or JSON output.",
    )
    work_complete.set_defaults(handler=_run_work_complete)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    handler = getattr(args, "handler", None)
    if handler is None:
        parser.print_help()
        return 0
    return int(handler(args))
