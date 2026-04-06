from __future__ import annotations

from typing import TypeVar
from collections.abc import Callable, Iterator

TPage = TypeVar("TPage")


def pages(
    fetch_page: Callable[..., TPage],
    *,
    page: int = 1,
    items: int | None = None,
) -> Iterator[TPage]:
    """Iterate over all pages returned by a paginated SDK list function.

    Args:
        fetch_page: Function that accepts ``page`` and optional ``items`` keyword
            arguments, and returns a page payload (typically ``plist[T]``).
        page: First page number to request.
        items: Optional number of items per page.

    Yields:
        TPage: Each page payload returned by ``fetch_page``.
    """
    current_page = page

    while True:
        page_data = fetch_page(page=current_page, items=items)

        if not page_data:
            break

        yield page_data

        current = getattr(page_data, "page", current_page)
        total_pages = getattr(page_data, "pages", current)

        if current >= total_pages:
            break

        current_page = current + 1
