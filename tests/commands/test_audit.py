"""Tests for DNS audit command."""

from infomaniak import output
from infomaniak.commands.audit import cmd_dns_audit


class TestDnsAudit:
    def _make_records(self, has_spf=True, has_dmarc=True, has_dkim=True, has_mx=True):
        """Helper to build a record set with optional features."""
        records = [
            {"type": "A", "source": ".", "target": "1.2.3.4", "ttl": 3600},
            {"type": "NS", "source": ".", "target": "ns1.example.com", "ttl": 3600},
        ]
        if has_spf:
            records.append({"type": "TXT", "source": ".", "target": '"v=spf1 include:example.com ~all"', "ttl": 3600})
        if has_dmarc:
            records.append({"type": "TXT", "source": "_dmarc", "target": '"v=DMARC1; p=reject"', "ttl": 3600})
        if has_dkim:
            records.append({"type": "CNAME", "source": "default._domainkey", "target": "dkim.example.com", "ttl": 3600})
        if has_mx:
            records.append({"type": "MX", "source": ".", "target": "10 mail.example.com", "ttl": 3600})
        return records

    def test_clean_domain(self, capsys, mock_token, mock_account_id, mock_api, fake_args, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)
        _, response = mock_api
        response.json.side_effect = [
            {"result": "success", "data": [{"customer_name": "clean.com"}]},
            {"result": "success", "data": self._make_records()},
        ]

        cmd_dns_audit(fake_args(domain="clean.com"))
        captured = capsys.readouterr()
        assert "1 clean" in captured.out

    def test_missing_spf(self, capsys, mock_token, mock_account_id, mock_api, fake_args, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)
        _, response = mock_api
        response.json.side_effect = [
            {"result": "success", "data": [{"customer_name": "nospf.com"}]},
            {"result": "success", "data": self._make_records(has_spf=False)},
        ]

        cmd_dns_audit(fake_args(domain="nospf.com"))
        captured = capsys.readouterr()
        assert "No SPF" in captured.out

    def test_missing_dmarc(self, capsys, mock_token, mock_account_id, mock_api, fake_args, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)
        _, response = mock_api
        response.json.side_effect = [
            {"result": "success", "data": [{"customer_name": "nodmarc.com"}]},
            {"result": "success", "data": self._make_records(has_dmarc=False)},
        ]

        cmd_dns_audit(fake_args(domain="nodmarc.com"))
        captured = capsys.readouterr()
        assert "No DMARC" in captured.out

    def test_missing_dkim(self, capsys, mock_token, mock_account_id, mock_api, fake_args, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)
        _, response = mock_api
        response.json.side_effect = [
            {"result": "success", "data": [{"customer_name": "nodkim.com"}]},
            {"result": "success", "data": self._make_records(has_dkim=False)},
        ]

        cmd_dns_audit(fake_args(domain="nodkim.com"))
        captured = capsys.readouterr()
        assert "No DKIM" in captured.out

    def test_multiple_issues(self, capsys, mock_token, mock_account_id, mock_api, fake_args, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)
        _, response = mock_api
        response.json.side_effect = [
            {"result": "success", "data": [{"customer_name": "bad.com"}]},
            {"result": "success", "data": self._make_records(has_spf=False, has_dmarc=False, has_mx=False)},
        ]

        cmd_dns_audit(fake_args(domain="bad.com"))
        captured = capsys.readouterr()
        assert "No SPF" in captured.out
        assert "No DMARC" in captured.out
