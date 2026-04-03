from infomaniak.resource import AsyncResource, Resouce


class Passwords(Resouce):
    """Swiss Backup password retrieval endpoints."""

    def administrator(self) -> None:
        """Request the administrator backup password."""
        raise NotImplementedError("Backup.passwords.administrator is not implemented yet.")

    def slot(self) -> None:
        """Request the password for a specific backup slot."""
        raise NotImplementedError("Backup.passwords.slot is not implemented yet.")


class AsyncPasswords(AsyncResource):
    """Async Swiss Backup password retrieval endpoints."""

    async def administrator(self) -> None:
        """Request the administrator backup password."""
        raise NotImplementedError("AsyncBackup.passwords.administrator is not implemented yet.")

    async def slot(self) -> None:
        """Request the password for a specific backup slot."""
        raise NotImplementedError("AsyncBackup.passwords.slot is not implemented yet.")


__all__ = ["Passwords", "AsyncPasswords"]
