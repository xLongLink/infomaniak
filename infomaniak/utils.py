from __future__ import annotations

from typing import TypeVar
from collections.abc import Iterable

T = TypeVar("T")


class PaginatedList(list[T]):
    """List container enriched with pagination metadata."""

    page: int
    pages: int
    items: int

    def __init__(self, values: Iterable[T], page: int, pages: int, items: int) -> None:
        """
        Initialize a paginated list.

        Args:
            values: Collection of items for the current page.
            page: Current page number.
            pages: Total number of pages.
            items: Total number of items.

        Returns:
            None: This constructor does not return a value.
        """
        super().__init__(values)
        self.page = page
        self.pages = pages
        self.items = items

    def __getitem__(self, item: int | slice) -> T | PaginatedList[T]:
        """
        Get an item or a slice from the list.

        Args:
            item: Index or slice to retrieve.

        Returns:
            T | PaginatedList[T]: The selected item or a sliced paginated list.
        """
        result = super().__getitem__(item)
        if isinstance(item, slice):
            return PaginatedList(result, self.page, self.pages, self.items)
        return result


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
