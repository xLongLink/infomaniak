from infomaniak.resource import AsyncResource, Resouce


class Invitations(Resouce):
    """Mailbox access invitation endpoints."""

    def create_webmail_access_link(self) -> None:
        """Create a webmail access link."""
        raise NotImplementedError(
            "Mailbox invitations create_webmail_access_link endpoint is not implemented yet."
        )

    def send_webmail_access_link(self) -> None:
        """Send a webmail access link by email."""
        raise NotImplementedError(
            "Mailbox invitations send_webmail_access_link endpoint is not implemented yet."
        )


class AsyncInvitations(AsyncResource):
    """Async mailbox access invitation endpoints."""

    async def create_webmail_access_link(self) -> None:
        """Create a webmail access link."""
        raise NotImplementedError(
            "Mailbox invitations create_webmail_access_link endpoint is not implemented yet."
        )

    async def send_webmail_access_link(self) -> None:
        """Send a webmail access link by email."""
        raise NotImplementedError(
            "Mailbox invitations send_webmail_access_link endpoint is not implemented yet."
        )


__all__ = ["Invitations", "AsyncInvitations"]
