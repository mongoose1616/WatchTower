from __future__ import annotations

import json
from pathlib import Path

from watchtower.cli import main


def _prepare_repo_root(tmp_path: Path) -> Path:
    repo_root = tmp_path / "watchtower"
    (repo_root / "core" / "python").mkdir(parents=True)
    return repo_root


def test_doctor_json_reports_repo_bootstrap_status(
    capsys,
    monkeypatch,
    tmp_path: Path,
) -> None:
    repo_root = _prepare_repo_root(tmp_path)
    monkeypatch.setenv("WATCHTOWER_REPO_ROOT", str(repo_root))

    exit_code = main(["doctor", "--format", "json"])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["status"] == "ok"
    assert payload["repo"] == "WatchTower"
    assert payload["bootstrap_stage"] == "repo_bootstrap"
    assert payload["workspace_status"] == "missing"
    assert payload["available_commands"] == [
        "doctor",
        "status",
        "init",
        "work start",
        "work list",
        "work next",
        "work show",
        "work note",
        "work complete",
    ]


def test_init_json_creates_manifest_and_doctor_reports_initialized(
    capsys,
    monkeypatch,
    tmp_path: Path,
) -> None:
    repo_root = _prepare_repo_root(tmp_path)
    monkeypatch.setenv("WATCHTOWER_REPO_ROOT", str(repo_root))

    init_exit_code = main(["init", "--format", "json"])
    init_payload = json.loads(capsys.readouterr().out)

    manifest_path = repo_root / ".watchtower" / "workspace.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    assert init_exit_code == 0
    assert init_payload["action"] == "created"
    assert manifest["workspace_status"] == "initialized"
    assert manifest["repo_root"] == str(repo_root)

    doctor_exit_code = main(["doctor", "--format", "json"])
    doctor_payload = json.loads(capsys.readouterr().out)

    assert doctor_exit_code == 0
    assert doctor_payload["bootstrap_stage"] == "workspace_initialized"
    assert doctor_payload["workspace_status"] == "initialized"
    assert doctor_payload["workspace_manifest"]["manifest_path"] == str(manifest_path)

    second_init_exit_code = main(["init", "--format", "json"])
    second_init_payload = json.loads(capsys.readouterr().out)

    assert second_init_exit_code == 0
    assert second_init_payload["action"] == "exists"


def test_work_list_requires_initialized_workspace(
    capsys,
    monkeypatch,
    tmp_path: Path,
) -> None:
    repo_root = _prepare_repo_root(tmp_path)
    monkeypatch.setenv("WATCHTOWER_REPO_ROOT", str(repo_root))

    exit_code = main(["work", "list", "--format", "json"])
    payload = json.loads(capsys.readouterr().out)

    assert exit_code == 1
    assert payload["status"] == "error"
    assert "watchtower init" in payload["message"].lower()


def test_work_next_handles_missing_workspace_and_empty_queue(
    capsys,
    monkeypatch,
    tmp_path: Path,
) -> None:
    repo_root = _prepare_repo_root(tmp_path)
    monkeypatch.setenv("WATCHTOWER_REPO_ROOT", str(repo_root))

    exit_code = main(["work", "next", "--format", "json"])
    payload = json.loads(capsys.readouterr().out)

    assert exit_code == 1
    assert payload["status"] == "error"
    assert "watchtower init" in payload["message"].lower()

    assert main(["init", "--format", "json"]) == 0
    capsys.readouterr()

    empty_exit_code = main(["work", "next", "--format", "json"])
    empty_payload = json.loads(capsys.readouterr().out)

    assert empty_exit_code == 0
    assert empty_payload["action"] == "none_available"
    assert empty_payload["work_item"] is None


def test_status_json_reports_missing_workspace_and_zero_work_items(
    capsys,
    monkeypatch,
    tmp_path: Path,
) -> None:
    repo_root = _prepare_repo_root(tmp_path)
    monkeypatch.setenv("WATCHTOWER_REPO_ROOT", str(repo_root))

    exit_code = main(["status", "--format", "json"])
    payload = json.loads(capsys.readouterr().out)

    assert exit_code == 0
    assert payload["workspace_status"] == "missing"
    assert payload["work_item_count"] == 0
    assert payload["counts_by_status"] == {}
    assert payload["recent_work_items"] == []


def test_work_start_requires_initialized_workspace(
    capsys,
    monkeypatch,
    tmp_path: Path,
) -> None:
    repo_root = _prepare_repo_root(tmp_path)
    monkeypatch.setenv("WATCHTOWER_REPO_ROOT", str(repo_root))

    exit_code = main(
        [
            "work",
            "start",
            "--slug",
            "first_slice",
            "--title",
            "First Slice",
            "--format",
            "json",
        ]
    )
    payload = json.loads(capsys.readouterr().out)

    assert exit_code == 1
    assert payload["status"] == "error"
    assert "watchtower init" in payload["message"].lower()


def test_work_note_requires_initialized_workspace_and_existing_item(
    capsys,
    monkeypatch,
    tmp_path: Path,
) -> None:
    repo_root = _prepare_repo_root(tmp_path)
    monkeypatch.setenv("WATCHTOWER_REPO_ROOT", str(repo_root))

    exit_code = main(
        [
            "work",
            "note",
            "--slug",
            "first_slice",
            "--message",
            "Need context.",
            "--format",
            "json",
        ]
    )
    payload = json.loads(capsys.readouterr().out)

    assert exit_code == 1
    assert payload["status"] == "error"
    assert "watchtower init" in payload["message"].lower()

    assert main(["init", "--format", "json"]) == 0
    capsys.readouterr()

    missing_exit_code = main(
        [
            "work",
            "note",
            "--slug",
            "missing_slice",
            "--message",
            "Need context.",
            "--format",
            "json",
        ]
    )
    missing_payload = json.loads(capsys.readouterr().out)

    assert missing_exit_code == 1
    assert missing_payload["status"] == "error"
    assert "unknown work item" in missing_payload["message"].lower()


def test_work_start_json_creates_work_item_record(
    capsys,
    monkeypatch,
    tmp_path: Path,
) -> None:
    repo_root = _prepare_repo_root(tmp_path)
    monkeypatch.setenv("WATCHTOWER_REPO_ROOT", str(repo_root))
    assert main(["init", "--format", "json"]) == 0
    capsys.readouterr()

    exit_code = main(
        [
            "work",
            "start",
            "--slug",
            "first_slice",
            "--title",
            "First Slice",
            "--format",
            "json",
        ]
    )
    payload = json.loads(capsys.readouterr().out)
    record_path = repo_root / ".watchtower" / "work_items" / "first_slice.json"
    record = json.loads(record_path.read_text(encoding="utf-8"))

    assert exit_code == 0
    assert payload["action"] == "created"
    assert record["work_item_id"] == "work_item.first_slice"
    assert record["status"] == "planned"

    second_exit_code = main(
        [
            "work",
            "start",
            "--slug",
            "first_slice",
            "--title",
            "First Slice",
            "--format",
            "json",
        ]
    )
    second_payload = json.loads(capsys.readouterr().out)

    assert second_exit_code == 0
    assert second_payload["action"] == "exists"


def test_work_list_show_and_complete_manage_local_work_item_lifecycle(
    capsys,
    monkeypatch,
    tmp_path: Path,
) -> None:
    repo_root = _prepare_repo_root(tmp_path)
    monkeypatch.setenv("WATCHTOWER_REPO_ROOT", str(repo_root))
    assert main(["init", "--format", "json"]) == 0
    capsys.readouterr()

    assert (
        main(
            [
                "work",
                "start",
                "--slug",
                "first_slice",
                "--title",
                "First Slice",
                "--format",
                "json",
            ]
        )
        == 0
    )
    capsys.readouterr()
    assert (
        main(
            [
                "work",
                "start",
                "--slug",
                "second_slice",
                "--title",
                "Second Slice",
                "--format",
                "json",
            ]
        )
        == 0
    )
    capsys.readouterr()

    note_exit_code = main(
        [
            "work",
            "note",
            "--slug",
            "first_slice",
            "--message",
            "Resume with the local-first CLI follow-up.",
            "--format",
            "json",
        ]
    )
    note_payload = json.loads(capsys.readouterr().out)

    assert note_exit_code == 0
    assert note_payload["action"] == "noted"
    assert note_payload["note"]["note_id"] == "work_item_note.first_slice.0001"
    assert note_payload["work_item"]["notes"][0]["message"] == (
        "Resume with the local-first CLI follow-up."
    )

    list_exit_code = main(["work", "list", "--format", "json"])
    list_payload = json.loads(capsys.readouterr().out)

    assert list_exit_code == 0
    assert list_payload["work_item_count"] == 2
    assert [item["slug"] for item in list_payload["work_items"]] == [
        "first_slice",
        "second_slice",
    ]

    show_exit_code = main(["work", "show", "--slug", "first_slice", "--format", "json"])
    show_payload = json.loads(capsys.readouterr().out)

    assert show_exit_code == 0
    assert show_payload["work_item"]["title"] == "First Slice"
    assert show_payload["work_item"]["status"] == "planned"

    next_exit_code = main(["work", "next", "--format", "json"])
    next_payload = json.loads(capsys.readouterr().out)

    assert next_exit_code == 0
    assert next_payload["action"] == "selected"
    assert next_payload["work_item"]["slug"] == "first_slice"
    assert next_payload["latest_note"]["message"] == (
        "Resume with the local-first CLI follow-up."
    )

    missing_exit_code = main(["work", "show", "--slug", "missing_slice", "--format", "json"])
    missing_payload = json.loads(capsys.readouterr().out)

    assert missing_exit_code == 1
    assert missing_payload["status"] == "error"
    assert "unknown work item" in missing_payload["message"].lower()

    complete_exit_code = main(
        [
            "work",
            "complete",
            "--slug",
            "first_slice",
            "--summary",
            "Closed after the first delivery.",
            "--format",
            "json",
        ]
    )
    complete_payload = json.loads(capsys.readouterr().out)
    record = json.loads(
        (repo_root / ".watchtower" / "work_items" / "first_slice.json").read_text(
            encoding="utf-8"
        )
    )

    assert complete_exit_code == 0
    assert complete_payload["action"] == "completed"
    assert record["status"] == "completed"
    assert record["completion_summary"] == "Closed after the first delivery."
    assert "completed_at" in record
    assert record["notes"][0]["message"] == "Resume with the local-first CLI follow-up."

    second_complete_exit_code = main(
        [
            "work",
            "complete",
            "--slug",
            "first_slice",
            "--format",
            "json",
        ]
    )
    second_complete_payload = json.loads(capsys.readouterr().out)

    assert second_complete_exit_code == 0
    assert second_complete_payload["action"] == "already_completed"

    status_exit_code = main(["status", "--format", "json"])
    status_payload = json.loads(capsys.readouterr().out)

    assert status_exit_code == 0
    assert status_payload["workspace_status"] == "initialized"
    assert status_payload["work_item_count"] == 2
    assert status_payload["counts_by_status"] == {"completed": 1, "planned": 1}
    assert {item["slug"] for item in status_payload["recent_work_items"]} == {
        "first_slice",
        "second_slice",
    }
    assert any(
        item["slug"] == "first_slice" and item["status"] == "completed"
        for item in status_payload["recent_work_items"]
    )
