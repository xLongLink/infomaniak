"""Sample usage against the installed ``infomaniak`` package."""

from unittest.mock import patch

import infomaniak
from infomaniak.api import api_request
from infomaniak.cli import main


def run_sample():
    print(f"Loaded package: infomaniak {infomaniak.__version__}")
    print(f"API base: {infomaniak.API_BASE}")
    print(f"api_request imported from: {api_request.__module__}")

    with patch("sys.argv", ["infomaniak", "--version"]):
        try:
            main()
        except SystemExit as exc:
            if exc.code not in (0, None):
                raise


if __name__ == "__main__":
    run_sample()
