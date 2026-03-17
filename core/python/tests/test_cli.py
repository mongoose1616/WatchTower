from __future__ import annotations

import json

from watchtower.cli import main


def test_doctor_json_reports_bootstrap_status(capsys) -> None:
    exit_code = main(["doctor", "--format", "json"])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["status"] == "ok"
    assert payload["repo"] == "WatchTower"
    assert payload["bootstrap_stage"] == "initialized"
    assert payload["available_commands"] == ["doctor"]
