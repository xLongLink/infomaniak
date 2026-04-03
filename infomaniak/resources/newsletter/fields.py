from infomaniak.resource import AsyncResource, Resouce


class Fields(Resouce):
    """Newsletter fields endpoints."""

    def list(self) -> None:
        """List all fields."""
        raise NotImplementedError("Newsletter fields list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a new field."""
        raise NotImplementedError("Newsletter fields create endpoint is not implemented yet.")

    def delete_bulk(self) -> None:
        """Delete multiple fields."""
        raise NotImplementedError("Newsletter fields delete_bulk endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a field."""
        raise NotImplementedError("Newsletter fields update endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a field."""
        raise NotImplementedError("Newsletter fields delete endpoint is not implemented yet.")


class AsyncFields(AsyncResource):
    """Async newsletter fields endpoints."""

    async def list(self) -> None:
        """List all fields."""
        raise NotImplementedError("Newsletter fields list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a new field."""
        raise NotImplementedError("Newsletter fields create endpoint is not implemented yet.")

    async def delete_bulk(self) -> None:
        """Delete multiple fields."""
        raise NotImplementedError("Newsletter fields delete_bulk endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a field."""
        raise NotImplementedError("Newsletter fields update endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a field."""
        raise NotImplementedError("Newsletter fields delete endpoint is not implemented yet.")


__all__ = ["Fields", "AsyncFields"]
