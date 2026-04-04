from infomaniak.resource import AsyncResource, Resouce

from .templates import AsyncTemplates, Templates


class Signatures(Resouce):
    """Mailbox signature endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.templates = Templates(client)

    def list(self) -> None:
        """List signatures for a mailbox."""
        raise NotImplementedError("Mailbox signatures list endpoint is not implemented yet.")

    def set_defaults(self) -> None:
        """Set default send and reply signatures."""
        raise NotImplementedError("Mailbox signatures set_defaults endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a mailbox signature."""
        raise NotImplementedError("Mailbox signatures create endpoint is not implemented yet.")

    def upload_image(self) -> None:
        """Upload an image for a mailbox signature."""
        raise NotImplementedError("Mailbox signatures upload_image endpoint is not implemented yet.")

    def show(self) -> None:
        """Show a mailbox signature."""
        raise NotImplementedError("Mailbox signatures show endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a mailbox signature."""
        raise NotImplementedError("Mailbox signatures delete endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a mailbox signature."""
        raise NotImplementedError("Mailbox signatures update endpoint is not implemented yet.")


class AsyncSignatures(AsyncResource):
    """Async mailbox signature endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.templates = AsyncTemplates(client)

    async def list(self) -> None:
        """List signatures for a mailbox."""
        raise NotImplementedError("Mailbox signatures list endpoint is not implemented yet.")

    async def set_defaults(self) -> None:
        """Set default send and reply signatures."""
        raise NotImplementedError("Mailbox signatures set_defaults endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a mailbox signature."""
        raise NotImplementedError("Mailbox signatures create endpoint is not implemented yet.")

    async def upload_image(self) -> None:
        """Upload an image for a mailbox signature."""
        raise NotImplementedError("Mailbox signatures upload_image endpoint is not implemented yet.")

    async def show(self) -> None:
        """Show a mailbox signature."""
        raise NotImplementedError("Mailbox signatures show endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a mailbox signature."""
        raise NotImplementedError("Mailbox signatures delete endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a mailbox signature."""
        raise NotImplementedError("Mailbox signatures update endpoint is not implemented yet.")


__all__ = ["Signatures", "AsyncSignatures", "Templates", "AsyncTemplates"]
