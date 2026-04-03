"""Tests for DNS propagation command."""

from unittest.mock import patch

from infomaniak import output
from infomaniak.commands.propagation import cmd_dns_propagation


class TestDnsPropagation:
    def test_all_agree(self, capsys, fake_args, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)

        with patch("infomaniak.commands.propagation._resolve") as mock_resolve:
            mock_resolve.return_value = ["1.2.3.4"]

            cmd_dns_propagation(fake_args(domain="example.com", name="@", type="A"))
            captured = capsys.readouterr()
            assert "All resolvers agree" in captured.out
            assert "1.2.3.4" in captured.out

    def test_inconsistent(self, capsys, fake_args, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)

        call_count = [0]
        def mock_resolve(domain, rtype, resolver_ip):
            call_count[0] += 1
            if call_count[0] <= 3:
                return ["1.2.3.4"]
            return ["5.6.7.8"]

        with patch("infomaniak.commands.propagation._resolve", side_effect=mock_resolve):
            cmd_dns_propagation(fake_args(domain="example.com", name="@", type="A"))
            captured = capsys.readouterr()
            assert "Inconsistent" in captured.out

    def test_with_subdomain(self, capsys, fake_args, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)

        with patch("infomaniak.commands.propagation._resolve") as mock_resolve:
            mock_resolve.return_value = ["1.2.3.4"]

            cmd_dns_propagation(fake_args(domain="example.com", name="www", type="A"))
            captured = capsys.readouterr()
            assert "www.example.com" in captured.out
