"""Configuration management commands."""

import os

from infomaniak.config import CONFIG_FILE, load_config
from infomaniak.output import bold, cyan, dim, green, red


def cmd_config_show(args):
    """Show current configuration."""
    print(f"\n  {bold('Configuration')}\n")

    # Check env var
    env_token = os.environ.get("INFOMANIAK_API_TOKEN")
    env_account = os.environ.get("INFOMANIAK_ACCOUNT_ID")

    # Check config file
    config = load_config()
    file_token = config.get("default", "token", fallback=None)
    file_account = config.get("default", "account_id", fallback=None)

    # Determine active source
    if env_token:
        active_source = "environment variable"
        active_token = env_token
    elif file_token:
        active_source = str(CONFIG_FILE)
        active_token = file_token
    else:
        active_source = None
        active_token = None

    active_account = env_account or file_account

    if active_token:
        masked = active_token[:6] + "..." + active_token[-4:]
        print(f"  {cyan('Token')}:      {masked}")
        print(f"  {cyan('Source')}:     {active_source}")
    else:
        print(f"  {cyan('Token')}:      {red('not set')}")

    if active_account:
        print(f"  {cyan('Account ID')}: {active_account}")
    else:
        print(f"  {cyan('Account ID')}: {dim('auto-detect')}")

    print(f"  {cyan('Config file')}: {CONFIG_FILE}")

    if CONFIG_FILE.exists():
        print(f"  {cyan('File status')}: {green('exists')}")
    else:
        print(f"  {cyan('File status')}: {dim('not created')}")

    print()
