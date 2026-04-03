from infomaniak.resource import AsyncResource, Resouce

from .subscribers import AsyncSegmentsSubscribers, SegmentsSubscribers


class Segments(Resouce):
    """Newsletter segments endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.subscribers = SegmentsSubscribers(client)

    def list(self) -> None:
        """List all segments."""
        raise NotImplementedError("Newsletter segments list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a segment."""
        raise NotImplementedError("Newsletter segments create endpoint is not implemented yet.")

    def delete_bulk(self) -> None:
        """Delete multiple segments."""
        raise NotImplementedError("Newsletter segments delete_bulk endpoint is not implemented yet.")

    def display(self) -> None:
        """Get a specific segment."""
        raise NotImplementedError("Newsletter segments display endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a segment."""
        raise NotImplementedError("Newsletter segments update endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a segment."""
        raise NotImplementedError("Newsletter segments delete endpoint is not implemented yet.")


class AsyncSegments(AsyncResource):
    """Async newsletter segments endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.subscribers = AsyncSegmentsSubscribers(client)

    async def list(self) -> None:
        """List all segments."""
        raise NotImplementedError("Newsletter segments list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a segment."""
        raise NotImplementedError("Newsletter segments create endpoint is not implemented yet.")

    async def delete_bulk(self) -> None:
        """Delete multiple segments."""
        raise NotImplementedError("Newsletter segments delete_bulk endpoint is not implemented yet.")

    async def display(self) -> None:
        """Get a specific segment."""
        raise NotImplementedError("Newsletter segments display endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a segment."""
        raise NotImplementedError("Newsletter segments update endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a segment."""
        raise NotImplementedError("Newsletter segments delete endpoint is not implemented yet.")


__all__ = ["Segments", "AsyncSegments", "SegmentsSubscribers", "AsyncSegmentsSubscribers"]
