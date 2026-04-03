"""Tests for status command."""

import json

import pytest

from infomaniak import output
from infomaniak.commands.status import cmd_status


class TestStatus:
    def test_groups_by_service(self, capsys, mock_token, mock_account_id, mock_api, fake_args, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [
                {"service_name": "domain", "customer_name": "a.com",
                 "has_maintenance": False, "is_locked": False, "has_operation_in_progress": False},
                {"service_name": "domain", "customer_name": "b.com",
                 "has_maintenance": False, "is_locked": False, "has_operation_in_progress": False},
                {"service_name": "email_hosting", "customer_name": "a.com",
                 "has_maintenance": False, "is_locked": False, "has_operation_in_progress": False},
            ],
            "pages": 1,
        }

        cmd_status(fake_args())
        captured = capsys.readouterr()
        assert "domain" in captured.out
        assert "email_hosting" in captured.out
        assert "3 products" in captured.out

    def test_shows_issues(self, capsys, mock_token, mock_account_id, mock_api, fake_args, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [
                {"service_name": "domain", "customer_name": "broken.com",
                 "has_maintenance": True, "is_locked": False, "has_operation_in_progress": False},
            ],
            "pages": 1,
        }

        cmd_status(fake_args())
        captured = capsys.readouterr()
        assert "maintenance" in captured.out
        assert "broken.com" in captured.out

    def test_all_healthy(self, capsys, mock_token, mock_account_id, mock_api, fake_args, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [
                {"service_name": "domain", "customer_name": "ok.com",
                 "has_maintenance": False, "is_locked": False, "has_operation_in_progress": False},
            ],
            "pages": 1,
        }

        cmd_status(fake_args())
        captured = capsys.readouterr()
        assert "All services operational" in captured.out

    def test_json_output(self, capsys, mock_token, mock_account_id, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [{"service_name": "domain", "id": 1}],
            "pages": 1,
        }

        with pytest.raises(SystemExit) as exc:
            cmd_status(fake_args(json=True))
        assert exc.value.code == 0
        data = json.loads(capsys.readouterr().out)
        assert data[0]["service_name"] == "domain"
