from infomaniak.resource import AsyncResource, Resouce

from .short import AsyncShort, Short


class Url(Resouce):
    """URL resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.short = Short(client)


class AsyncUrl(AsyncResource):
    """Async URL resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.short = AsyncShort(client)


__all__ = ["Url", "AsyncUrl", "Short", "AsyncShort"]
