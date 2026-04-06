from __future__ import annotations

import sys
import json
from dacite import from_dict
from typing import Any, TypeVar, Iterable
from dacite.exceptions import DaciteError

T = TypeVar("T")


class plist(list[T]):
    def __init__(self, values: Iterable[T] = (), *, page: int = 1, pages: int = 1, total: int = 0,) -> None:
        super().__init__(values)
        self.page = page
        self.pages = pages
        self.total = total


def parse(model: type[T], data: dict[str, Any]) -> T:
    """
    Parse an API payload into a typed dataclass instance.

    Args:
        model: The dataclass type to instantiate.
        data: The JSON payload to parse.

    Returns:
        T: The parsed dataclass instance.
    """
    try:
        return from_dict(model, data)
    except DaciteError as exc:
        print(
            f"Failed to parse {model.__name__}: {exc}\nPayload:\n"
            f"{json.dumps(data, indent=2, sort_keys=True)}",
            file=sys.stderr,
        )
        raise


def _with(**fields: bool) -> str | None:
    """
    Build a comma-separated value for API `with` query parameters.

    Args:
        **fields (bool): Mapping of field names to inclusion flags.

    Returns:
        str | None: Comma-separated field names for truthy flags, or None if empty.
    """
    values = [key for key, include in fields.items() if include]
    return ",".join(values) if values else None


def query_params(**parameters: Any) -> dict[str, Any] | None:
    """
    Build query parameters by dropping ``None`` values.

    Args:
        **parameters: Arbitrary query parameter values.

    Returns:
        dict[str, Any] | None: Dictionary containing only non-``None`` values, or ``None`` if empty.
    """
    cleaned_parameters = {
        key: value for key, value in parameters.items() if value is not None
    }
    return cleaned_parameters or None
