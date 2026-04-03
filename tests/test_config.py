"""Tests for configuration management."""

import os

import pytest

from infomaniak import config


class TestLoadConfig:
    def test_missing_file(self, tmp_path, monkeypatch):
        monkeypatch.setattr(config, "CONFIG_FILE", tmp_path / "nonexistent.ini")
        cfg = config.load_config()
        assert not cfg.has_section("default")

    def test_existing_file(self, tmp_path, monkeypatch):
        cfg_file = tmp_path / "config.ini"
        cfg_file.write_text("[default]\ntoken = abc123\n")
        monkeypatch.setattr(config, "CONFIG_FILE", cfg_file)

        cfg = config.load_config()
        assert cfg.get("default", "token") == "abc123"


class TestSaveConfig:
    def test_creates_file(self, tmp_path, monkeypatch):
        cfg_dir = tmp_path / "infomaniak"
        cfg_file = cfg_dir / "config.ini"
        monkeypatch.setattr(config, "CONFIG_DIR", cfg_dir)
        monkeypatch.setattr(config, "CONFIG_FILE", cfg_file)

        config.save_config("mytoken")

        assert cfg_file.exists()
        content = cfg_file.read_text()
        assert "mytoken" in content
        assert (cfg_file.stat().st_mode & 0o777) == 0o600

    def test_with_account_id(self, tmp_path, monkeypatch):
        cfg_dir = tmp_path / "infomaniak"
        cfg_file = cfg_dir / "config.ini"
        monkeypatch.setattr(config, "CONFIG_DIR", cfg_dir)
        monkeypatch.setattr(config, "CONFIG_FILE", cfg_file)

        config.save_config("tok", account_id=99)

        content = cfg_file.read_text()
        assert "99" in content


class TestLoadEnvFile:
    def test_loads_env_vars(self, tmp_path, monkeypatch):
        env_file = tmp_path / ".env"
        env_file.write_text("TEST_VAR=hello\n")
        monkeypatch.chdir(tmp_path)
        monkeypatch.delenv("TEST_VAR", raising=False)

        config.load_env_file()
        assert os.environ.get("TEST_VAR") == "hello"

        # Cleanup
        monkeypatch.delenv("TEST_VAR", raising=False)

    def test_ignores_comments(self, tmp_path, monkeypatch):
        env_file = tmp_path / ".env"
        env_file.write_text("# comment\n\nVALID_VAR=yes\n")
        monkeypatch.chdir(tmp_path)
        monkeypatch.delenv("VALID_VAR", raising=False)

        config.load_env_file()
        assert os.environ.get("VALID_VAR") == "yes"

        monkeypatch.delenv("VALID_VAR", raising=False)


class TestGetToken:
    def test_from_env(self, mock_token):
        assert config.get_token() == "test-token-abc123"

    def test_from_config_file(self, tmp_path, monkeypatch):
        monkeypatch.delenv("INFOMANIAK_API_TOKEN", raising=False)
        cfg_file = tmp_path / "config.ini"
        cfg_file.write_text("[default]\ntoken = config-token\n")
        monkeypatch.setattr(config, "CONFIG_FILE", cfg_file)

        assert config.get_token() == "config-token"

    def test_missing_exits(self, tmp_path, monkeypatch):
        monkeypatch.delenv("INFOMANIAK_API_TOKEN", raising=False)
        monkeypatch.setattr(config, "CONFIG_FILE", tmp_path / "nope.ini")

        with pytest.raises(SystemExit):
            config.get_token()


class TestGetAccountId:
    def test_from_env(self, mock_account_id):
        assert config.get_account_id("tok") == "12345"

    def test_from_config(self, tmp_path, monkeypatch):
        monkeypatch.delenv("INFOMANIAK_ACCOUNT_ID", raising=False)
        cfg_file = tmp_path / "config.ini"
        cfg_file.write_text("[default]\ntoken = x\naccount_id = 999\n")
        monkeypatch.setattr(config, "CONFIG_FILE", cfg_file)

        assert config.get_account_id("tok") == "999"
