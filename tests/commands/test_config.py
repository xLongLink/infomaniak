"""Tests for config commands."""

from infomaniak import config
from infomaniak.commands.config import cmd_config_show


class TestConfigShow:
    def test_shows_token_from_env(self, capsys, mock_token):
        import argparse
        cmd_config_show(argparse.Namespace())
        captured = capsys.readouterr()
        assert "test-t" in captured.out  # masked token starts
        assert "environment variable" in captured.out

    def test_shows_no_token(self, capsys, monkeypatch, tmp_path):
        monkeypatch.delenv("INFOMANIAK_API_TOKEN", raising=False)
        monkeypatch.setattr(config, "CONFIG_FILE", tmp_path / "nope.ini")
        import argparse
        cmd_config_show(argparse.Namespace())
        captured = capsys.readouterr()
        assert "not set" in captured.out

    def test_shows_config_file_path(self, capsys, mock_token):
        import argparse
        cmd_config_show(argparse.Namespace())
        captured = capsys.readouterr()
        assert "config.ini" in captured.out

    def test_shows_account_id(self, capsys, mock_token, mock_account_id):
        import argparse
        cmd_config_show(argparse.Namespace())
        captured = capsys.readouterr()
        assert "12345" in captured.out
