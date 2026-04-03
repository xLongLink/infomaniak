"""Tests for CLI argument parsing."""

import pytest
from unittest.mock import patch

from infomaniak.cli import main


class TestCli:
    def test_no_args_exits(self):
        with patch("sys.argv", ["infomaniak"]):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 1

    def test_version_flag(self, capsys):
        with patch("sys.argv", ["infomaniak", "--version"]):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 0
        captured = capsys.readouterr()
        assert "infomaniak" in captured.out

    def test_dns_no_subcommand_exits(self):
        with patch("sys.argv", ["infomaniak", "dns"]):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 1

    def test_mail_no_subcommand_exits(self):
        with patch("sys.argv", ["infomaniak", "mail"]):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 1
