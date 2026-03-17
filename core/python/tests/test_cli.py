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
    assert payload["available_commands"] == ["doctor", "init"]


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
