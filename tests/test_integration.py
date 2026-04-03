"""Integration tests — run the CLI as a subprocess, no real API calls."""

import json
import subprocess
import sys

import pytest

CLI = [sys.executable, "-m", "infomaniak"]


def run(*args, env_override=None, input_text=None):
    """Run the CLI and return (returncode, stdout, stderr)."""
    import os
    env = os.environ.copy()
    # Set empty values so load_env_file() won't overwrite from .env
    env["INFOMANIAK_API_TOKEN"] = ""
    env["INFOMANIAK_ACCOUNT_ID"] = ""
    # Isolate from real config
    env["HOME"] = "/tmp/infomaniak-test-nonexistent"
    if env_override:
        env.update(env_override)
    result = subprocess.run(
        [*CLI, *args],
        capture_output=True,
        text=True,
        env=env,
        input=input_text,
        timeout=10,
        cwd="/tmp",  # avoid picking up .env from project dir
    )
    return result.returncode, result.stdout, result.stderr


class TestHelpAndVersion:
    def test_no_args_shows_help(self):
        code, out, err = run()
        combined = out + err
        assert code == 1
        assert "setup" in combined
        assert "dns" in combined
        assert "products" in combined
        assert "status" in combined

    def test_version(self):
        code, out, err = run("--version")
        assert code == 0
        assert "infomaniak" in out

    def test_help_flag(self):
        code, out, err = run("--help")
        assert code == 0
        combined = out + err
        assert "Manage Infomaniak services" in combined

    def test_dns_help(self):
        code, out, err = run("dns")
        combined = out + err
        assert "domains" in combined
        assert "records" in combined
        assert "export" in combined
        assert "import" in combined

    def test_dns_subcommand_help(self):
        code, out, err = run("dns", "add", "--help")
        assert code == 0
        combined = out + err
        assert "domain" in combined
        assert "type" in combined
        assert "source" in combined
        assert "target" in combined

    def test_mail_help(self):
        code, out, err = run("mail")
        combined = out + err
        assert "list" in combined

    def test_products_help(self):
        code, out, err = run("products", "--help")
        assert code == 0
        combined = out + err
        assert "--type" in combined
        assert "--json" in combined

    def test_status_help(self):
        code, out, err = run("status", "--help")
        assert code == 0
        combined = out + err
        assert "--json" in combined


class TestNoToken:
    """Verify graceful behavior when no token is configured."""

    def test_dns_domains_no_token(self):
        code, out, err = run("dns", "domains")
        combined = out + err
        assert code == 1
        assert "No API token" in combined or "token" in combined.lower()

    def test_products_no_token(self):
        code, out, err = run("products")
        combined = out + err
        assert code == 1
        assert "token" in combined.lower()

    def test_status_no_token(self):
        code, out, err = run("status")
        combined = out + err
        assert code == 1
        assert "token" in combined.lower()

    def test_suggests_setup(self):
        code, out, err = run("dns", "domains")
        combined = out + err
        assert "infomaniak setup" in combined


class TestInvalidArgs:
    def test_unknown_service(self):
        code, out, err = run("foobar")
        assert code != 0

    def test_dns_records_missing_domain(self):
        code, out, err = run("dns", "records")
        assert code != 0

    def test_dns_add_missing_args(self):
        code, out, err = run("dns", "add", "example.com")
        assert code != 0

    def test_dns_update_no_flags(self):
        code, out, err = run(
            "dns", "update", "example.com", "123",
            env_override={"INFOMANIAK_API_TOKEN": "fake"}
        )
        combined = out + err
        assert code == 1
        assert "target" in combined.lower() or "ttl" in combined.lower()


class TestDnsExportImport:
    def test_import_missing_file(self):
        code, out, err = run(
            "dns", "import", "example.com", "/nonexistent/file.json",
            env_override={"INFOMANIAK_API_TOKEN": "fake"}
        )
        combined = out + err
        assert code == 1
        assert "not found" in combined.lower() or "File not found" in combined

    def test_import_invalid_json(self, tmp_path):
        bad_file = tmp_path / "bad.json"
        bad_file.write_text("{not json at all")
        code, out, err = run(
            "dns", "import", "example.com", str(bad_file),
            env_override={"INFOMANIAK_API_TOKEN": "fake"}
        )
        combined = out + err
        assert code == 1
        assert "Invalid JSON" in combined


class TestModuleExecution:
    def test_python_m_infomaniak(self):
        """Verify python -m infomaniak works."""
        code, out, err = run("--version")
        assert code == 0
        assert "infomaniak" in out
