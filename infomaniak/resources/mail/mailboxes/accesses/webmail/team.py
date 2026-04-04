from infomaniak.resource import AsyncResource, Resouce


class Team(Resouce):
    """Mailbox webmail team access endpoints."""

    def bulk_create(self) -> None:
        """Bulk create team webmail accesses."""
        raise NotImplementedError("Mailbox webmail team bulk_create endpoint is not implemented yet.")

    def list(self) -> None:
        """List team webmail accesses."""
        raise NotImplementedError("Mailbox webmail team list endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a team webmail access."""
        raise NotImplementedError("Mailbox webmail team delete endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a team webmail access."""
        raise NotImplementedError("Mailbox webmail team update endpoint is not implemented yet.")


class AsyncTeam(AsyncResource):
    """Async mailbox webmail team access endpoints."""

    async def bulk_create(self) -> None:
        """Bulk create team webmail accesses."""
        raise NotImplementedError("Mailbox webmail team bulk_create endpoint is not implemented yet.")

    async def list(self) -> None:
        """List team webmail accesses."""
        raise NotImplementedError("Mailbox webmail team list endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a team webmail access."""
        raise NotImplementedError("Mailbox webmail team delete endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a team webmail access."""
        raise NotImplementedError("Mailbox webmail team update endpoint is not implemented yet.")


__all__ = ["Team", "AsyncTeam"]
