from infomaniak.resource import AsyncResource, Resouce


class Short(Resouce):
    """URL shortener resource."""

    def list(self) -> None:
        """List short URLs."""
        raise NotImplementedError("Url.short.list is not implemented yet.")

    def create(self) -> None:
        """Create a short URL."""
        raise NotImplementedError("Url.short.create is not implemented yet.")

    def update(self) -> None:
        """Update a short URL."""
        raise NotImplementedError("Url.short.update is not implemented yet.")

    def quota(self) -> None:
        """Get short URL quota."""
        raise NotImplementedError("Url.short.quota is not implemented yet.")


class AsyncShort(AsyncResource):
    """Async URL shortener resource."""

    async def list(self) -> None:
        """List short URLs."""
        raise NotImplementedError("AsyncUrl.short.list is not implemented yet.")

    async def create(self) -> None:
        """Create a short URL."""
        raise NotImplementedError("AsyncUrl.short.create is not implemented yet.")

    async def update(self) -> None:
        """Update a short URL."""
        raise NotImplementedError("AsyncUrl.short.update is not implemented yet.")

    async def quota(self) -> None:
        """Get short URL quota."""
        raise NotImplementedError("AsyncUrl.short.quota is not implemented yet.")
