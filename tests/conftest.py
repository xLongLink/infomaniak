"""Shared test fixtures."""

import argparse
from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture
def mock_token(monkeypatch):
    """Provide a fake token via environment variable."""
    monkeypatch.setenv("INFOMANIAK_API_TOKEN", "test-token-abc123")
    return "test-token-abc123"


@pytest.fixture
def mock_account_id(monkeypatch):
    """Provide a fake account ID via environment variable."""
    monkeypatch.setenv("INFOMANIAK_ACCOUNT_ID", "12345")
    return "12345"


@pytest.fixture
def fake_args():
    """Factory for creating argparse.Namespace objects."""
    def _make(**kwargs):
        defaults = {"json": False}
        defaults.update(kwargs)
        return argparse.Namespace(**defaults)
    return _make


@pytest.fixture
def mock_api():
    """Mock the requests.request call used by api_request."""
    with patch("infomaniak.api.requests.request") as mock_req:
        response = MagicMock()
        response.status_code = 200
        response.text = ""
        response.json.return_value = {"result": "success", "data": []}
        mock_req.return_value = response
        yield mock_req, response
