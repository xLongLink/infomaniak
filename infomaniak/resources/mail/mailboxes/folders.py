from infomaniak.resource import AsyncResource, Resouce


class Folders(Resouce):
    """Mailbox folders endpoints."""

    def list(self) -> None:
        """List folders for a mailbox."""
        raise NotImplementedError("Mailbox folders list endpoint is not implemented yet.")

    def update(self) -> None:
        """Update folder mapping for a mailbox."""
        raise NotImplementedError("Mailbox folders update endpoint is not implemented yet.")

    def purge_spam(self) -> None:
        """Purge spam folder for a mailbox."""
        raise NotImplementedError("Mailbox folders purge_spam endpoint is not implemented yet.")

    def empty_trash(self) -> None:
        """Empty trash folder for a mailbox."""
        raise NotImplementedError("Mailbox folders empty_trash endpoint is not implemented yet.")


class AsyncFolders(AsyncResource):
    """Async mailbox folders endpoints."""

    async def list(self) -> None:
        """List folders for a mailbox."""
        raise NotImplementedError("Mailbox folders list endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update folder mapping for a mailbox."""
        raise NotImplementedError("Mailbox folders update endpoint is not implemented yet.")

    async def purge_spam(self) -> None:
        """Purge spam folder for a mailbox."""
        raise NotImplementedError("Mailbox folders purge_spam endpoint is not implemented yet.")

    async def empty_trash(self) -> None:
        """Empty trash folder for a mailbox."""
        raise NotImplementedError("Mailbox folders empty_trash endpoint is not implemented yet.")


__all__ = ["Folders", "AsyncFolders"]
