"""Tests for mail commands."""

import json

import pytest

from infomaniak.commands.mail import cmd_mail_list


class TestMailList:
    def test_displays_table(self, capsys, mock_token, mock_account_id, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [
                {"id": 1, "customer_name": "example.com", "service_name": "email_hosting",
                 "has_maintenance": False, "is_locked": False, "has_operation_in_progress": False},
            ],
            "pages": 1,
        }

        cmd_mail_list(fake_args())
        captured = capsys.readouterr()
        assert "example.com" in captured.out
        assert "Mail Hostings (1)" in captured.out

    def test_empty(self, capsys, mock_token, mock_account_id, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {"result": "success", "data": [], "pages": 1}

        cmd_mail_list(fake_args())
        captured = capsys.readouterr()
        assert "No mail hostings" in captured.out

    def test_json_output(self, capsys, mock_token, mock_account_id, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [{"id": 1, "customer_name": "test.com"}],
            "pages": 1,
        }

        with pytest.raises(SystemExit) as exc:
            cmd_mail_list(fake_args(json=True))
        assert exc.value.code == 0
        data = json.loads(capsys.readouterr().out)
        assert data[0]["customer_name"] == "test.com"
