from infomaniak.resource import AsyncResource, Resouce


class Domains(Resouce):
    """Newsletter domains endpoints."""

    def display(self) -> None:
        """Display a domain."""
        raise NotImplementedError("Newsletter domains display endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a domain."""
        raise NotImplementedError("Newsletter domains delete endpoint is not implemented yet.")


class AsyncDomains(AsyncResource):
    """Async newsletter domains endpoints."""

    async def display(self) -> None:
        """Display a domain."""
        raise NotImplementedError("Newsletter domains display endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a domain."""
        raise NotImplementedError("Newsletter domains delete endpoint is not implemented yet.")


__all__ = ["Domains", "AsyncDomains"]
