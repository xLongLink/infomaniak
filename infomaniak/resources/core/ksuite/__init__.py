from infomaniak.resource import AsyncResource, Resouce

from .mailbox import AsyncKsuiteMailbox, KsuiteMailbox


class Ksuite(Resouce):
    """Core kSuite endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.mailbox = KsuiteMailbox(client)

    def show(self) -> None:
        """Show kSuite data."""
        raise NotImplementedError("Core.ksuite.show is not implemented yet.")

    def current(self) -> None:
        """Show current kSuite data."""
        raise NotImplementedError("Core.ksuite.current is not implemented yet.")


class AsyncKsuite(AsyncResource):
    """Async core kSuite endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.mailbox = AsyncKsuiteMailbox(client)

    async def show(self) -> None:
        """Show kSuite data."""
        raise NotImplementedError("AsyncCore.ksuite.show is not implemented yet.")

    async def current(self) -> None:
        """Show current kSuite data."""
        raise NotImplementedError("AsyncCore.ksuite.current is not implemented yet.")
