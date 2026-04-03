"""Tests for products command."""

import json

import pytest

from infomaniak.commands.products import cmd_products


class TestProducts:
    def test_displays_table(self, capsys, mock_token, mock_account_id, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [
                {"id": 1, "service_name": "domain", "customer_name": "example.com",
                 "has_maintenance": False, "is_locked": False, "has_operation_in_progress": False},
            ],
            "pages": 1,
        }

        cmd_products(fake_args(service_filter=None))
        captured = capsys.readouterr()
        assert "example.com" in captured.out
        assert "domain" in captured.out

    def test_with_type_filter(self, mock_token, mock_account_id, mock_api, fake_args, capsys):
        mock_req, response = mock_api
        response.json.return_value = {"result": "success", "data": [], "pages": 1}

        cmd_products(fake_args(service_filter="email_hosting"))
        # Verify the API was called with the filter
        call_params = mock_req.call_args[1].get("params", {})
        assert call_params.get("service_name") == "email_hosting"

    def test_status_indicators(self, capsys, mock_token, mock_account_id, mock_api, fake_args, monkeypatch):
        from infomaniak import output
        monkeypatch.setattr(output, "_COLOR", False)

        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [
                {"id": 1, "service_name": "domain", "customer_name": "ok.com",
                 "has_maintenance": False, "is_locked": False, "has_operation_in_progress": False},
                {"id": 2, "service_name": "domain", "customer_name": "maint.com",
                 "has_maintenance": True, "is_locked": False, "has_operation_in_progress": False},
                {"id": 3, "service_name": "domain", "customer_name": "locked.com",
                 "has_maintenance": False, "is_locked": True, "has_operation_in_progress": False},
            ],
            "pages": 1,
        }

        cmd_products(fake_args(service_filter=None))
        captured = capsys.readouterr()
        assert "active" in captured.out
        assert "maintenance" in captured.out
        assert "locked" in captured.out

    def test_json_output(self, capsys, mock_token, mock_account_id, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [{"id": 1, "service_name": "domain"}],
            "pages": 1,
        }

        with pytest.raises(SystemExit) as exc:
            cmd_products(fake_args(service_filter=None, json=True))
        assert exc.value.code == 0
        data = json.loads(capsys.readouterr().out)
        assert data[0]["service_name"] == "domain"
