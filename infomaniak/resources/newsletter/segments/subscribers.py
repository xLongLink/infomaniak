from infomaniak.resource import AsyncResource, Resouce


class SegmentsSubscribers(Resouce):
    """Newsletter segment subscribers endpoints."""

    def list(self) -> None:
        """List subscribers in a segment."""
        raise NotImplementedError(
            "Newsletter segments subscribers list endpoint is not implemented yet."
        )


class AsyncSegmentsSubscribers(AsyncResource):
    """Async newsletter segment subscribers endpoints."""

    async def list(self) -> None:
        """List subscribers in a segment."""
        raise NotImplementedError(
            "Newsletter segments subscribers list endpoint is not implemented yet."
        )


__all__ = ["SegmentsSubscribers", "AsyncSegmentsSubscribers"]
