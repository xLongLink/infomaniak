from infomaniak.resource import Resouce, AsyncResource


class Core(Resouce):
    """Core resources for Infomaniak services."""

    def __new__(cls) -> Self:
        return super().__new__()


class AsyncCore(AsyncResource):
    """Async core resources for Infomaniak services."""
