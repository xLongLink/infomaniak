from infomaniak.resource import AsyncResource, Resouce


class Users(Resouce):
    """Mailbox users endpoints."""

    def delete_invitation(self) -> None:
        """Delete an invitation to a mailbox."""
        raise NotImplementedError("Mailbox users delete_invitation endpoint is not implemented yet.")

    def update_invitation_permission(self) -> None:
        """Update permissions of a mailbox invitation."""
        raise NotImplementedError(
            "Mailbox users update_invitation_permission endpoint is not implemented yet."
        )


class AsyncUsers(AsyncResource):
    """Async mailbox users endpoints."""

    async def delete_invitation(self) -> None:
        """Delete an invitation to a mailbox."""
        raise NotImplementedError("Mailbox users delete_invitation endpoint is not implemented yet.")

    async def update_invitation_permission(self) -> None:
        """Update permissions of a mailbox invitation."""
        raise NotImplementedError(
            "Mailbox users update_invitation_permission endpoint is not implemented yet."
        )


__all__ = ["Users", "AsyncUsers"]
