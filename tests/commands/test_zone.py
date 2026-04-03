"""Tests for zone file generation."""

from infomaniak.commands.zone import cmd_dns_zone


class TestDnsZone:
    def test_generates_zone(self, capsys, mock_token, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [
                {"type": "A", "source": ".", "target": "1.2.3.4", "ttl": 3600},
                {"type": "CNAME", "source": "www", "target": "example.com", "ttl": 300},
                {"type": "MX", "source": ".", "target": "10 mail.example.com", "ttl": 3600},
            ],
        }

        cmd_dns_zone(fake_args(domain="example.com", output=None))
        captured = capsys.readouterr()
        assert "$ORIGIN example.com." in captured.out
        assert "IN  A" in captured.out
        assert "IN  CNAME" in captured.out
        assert "example.com." in captured.out  # trailing dot on CNAME target

    def test_writes_to_file(self, tmp_path, capsys, mock_token, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [{"type": "A", "source": ".", "target": "1.2.3.4", "ttl": 3600}],
        }

        outfile = str(tmp_path / "zone.txt")
        cmd_dns_zone(fake_args(domain="example.com", output=outfile))

        content = (tmp_path / "zone.txt").read_text()
        assert "$ORIGIN" in content
        assert "1.2.3.4" in content
