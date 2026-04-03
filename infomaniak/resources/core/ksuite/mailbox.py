from infomaniak.resource import AsyncResource, Resouce


class KsuiteMailbox(Resouce):
    """Core kSuite mailbox endpoints."""

    def get(self) -> None:
        """Get a mailbox."""
        raise NotImplementedError("Core.ksuite.mailbox.get is not implemented yet.")

    def primary(self) -> None:
        """Set primary mailbox."""
        raise NotImplementedError("Core.ksuite.mailbox.primary is not implemented yet.")

    def password(self) -> None:
        """Update mailbox password."""
        raise NotImplementedError("Core.ksuite.mailbox.password is not implemented yet.")

    def unlink(self) -> None:
        """Unlink a mailbox."""
        raise NotImplementedError("Core.ksuite.mailbox.unlink is not implemented yet.")

    def attach(self) -> None:
        """Attach a mailbox."""
        raise NotImplementedError("Core.ksuite.mailbox.attach is not implemented yet.")


class AsyncKsuiteMailbox(AsyncResource):
    """Async core kSuite mailbox endpoints."""

    async def get(self) -> None:
        """Get a mailbox."""
        raise NotImplementedError("AsyncCore.ksuite.mailbox.get is not implemented yet.")

    async def primary(self) -> None:
        """Set primary mailbox."""
        raise NotImplementedError("AsyncCore.ksuite.mailbox.primary is not implemented yet.")

    async def password(self) -> None:
        """Update mailbox password."""
        raise NotImplementedError("AsyncCore.ksuite.mailbox.password is not implemented yet.")

    async def unlink(self) -> None:
        """Unlink a mailbox."""
        raise NotImplementedError("AsyncCore.ksuite.mailbox.unlink is not implemented yet.")

    async def attach(self) -> None:
        """Attach a mailbox."""
        raise NotImplementedError("AsyncCore.ksuite.mailbox.attach is not implemented yet.")
