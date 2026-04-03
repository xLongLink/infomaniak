from infomaniak.resource import AsyncResource, Resouce


class Operations(Resouce):
    """Newsletter operations endpoints."""

    def cancel(self) -> None:
        """Cancel an operation."""
        raise NotImplementedError("Newsletter operations cancel endpoint is not implemented yet.")


class AsyncOperations(AsyncResource):
    """Async newsletter operations endpoints."""

    async def cancel(self) -> None:
        """Cancel an operation."""
        raise NotImplementedError("Newsletter operations cancel endpoint is not implemented yet.")


__all__ = ["Operations", "AsyncOperations"]
