"""Tests for domains command."""

import json
import time

import pytest
from infomaniak import output
from infomaniak.commands.domains import cmd_domains


class TestDomains:
    def test_shows_expiry(self, capsys, mock_token, mock_account_id, mock_api, fake_args, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)
        _, response = mock_api
        future_ts = int(time.time()) + 86400 * 60  # 60 days from now
        response.json.return_value = {
            "result": "success",
            "data": [
                {"customer_name": "example.com", "expired_at": future_ts,
                 "has_maintenance": False, "is_locked": False, "has_operation_in_progress": False},
            ],
            "pages": 1,
        }

        cmd_domains(fake_args(warn=30))
        captured = capsys.readouterr()
        assert "example.com" in captured.out
        assert "active" in captured.out

    def test_warns_expiring(self, capsys, mock_token, mock_account_id, mock_api, fake_args, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)
        _, response = mock_api
        soon_ts = int(time.time()) + 86400 * 10  # 10 days from now
        response.json.return_value = {
            "result": "success",
            "data": [
                {"customer_name": "expiring.com", "expired_at": soon_ts,
                 "has_maintenance": False, "is_locked": False, "has_operation_in_progress": False},
            ],
            "pages": 1,
        }

        cmd_domains(fake_args(warn=30))
        captured = capsys.readouterr()
        assert "expiring" in captured.out
        assert "Warning" in captured.out

    def test_json_output(self, capsys, mock_token, mock_account_id, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [{"customer_name": "test.com", "expired_at": 9999999999}],
            "pages": 1,
        }

        with pytest.raises(SystemExit) as exc:
            cmd_domains(fake_args(warn=30, json=True))
        assert exc.value.code == 0
