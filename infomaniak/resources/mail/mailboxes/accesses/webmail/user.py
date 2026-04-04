from infomaniak.resource import AsyncResource, Resouce


class User(Resouce):
    """Mailbox webmail user access endpoints."""

    def list_access_and_invitations(self) -> None:
        """List user accesses, team accesses, and invitations."""
        raise NotImplementedError(
            "Mailbox webmail user list_access_and_invitations endpoint is not implemented yet."
        )

    def set_primary_mailbox(self) -> None:
        """Set the primary mailbox for current user."""
        raise NotImplementedError("Mailbox webmail user set_primary_mailbox endpoint is not implemented yet.")

    def list_users(self) -> None:
        """List users having access to a mailbox."""
        raise NotImplementedError("Mailbox webmail user list_users endpoint is not implemented yet.")

    def get_team_accesses_for_user(self) -> None:
        """Get team accesses for a user."""
        raise NotImplementedError(
            "Mailbox webmail user get_team_accesses_for_user endpoint is not implemented yet."
        )

    def get_user_accesses_for_team(self) -> None:
        """Get user accesses for a team."""
        raise NotImplementedError(
            "Mailbox webmail user get_user_accesses_for_team endpoint is not implemented yet."
        )

    def list_accesses_for_current_user(self) -> None:
        """List accesses for current user."""
        raise NotImplementedError(
            "Mailbox webmail user list_accesses_for_current_user endpoint is not implemented yet."
        )

    def list_accesses_for_account_and_user(self) -> None:
        """List accesses for an account and a user."""
        raise NotImplementedError(
            "Mailbox webmail user list_accesses_for_account_and_user endpoint is not implemented yet."
        )

    def delete_access_for_current_user(self) -> None:
        """Delete access to a mailbox for current user."""
        raise NotImplementedError(
            "Mailbox webmail user delete_access_for_current_user endpoint is not implemented yet."
        )


class AsyncUser(AsyncResource):
    """Async mailbox webmail user access endpoints."""

    async def list_access_and_invitations(self) -> None:
        """List user accesses, team accesses, and invitations."""
        raise NotImplementedError(
            "Mailbox webmail user list_access_and_invitations endpoint is not implemented yet."
        )

    async def set_primary_mailbox(self) -> None:
        """Set the primary mailbox for current user."""
        raise NotImplementedError("Mailbox webmail user set_primary_mailbox endpoint is not implemented yet.")

    async def list_users(self) -> None:
        """List users having access to a mailbox."""
        raise NotImplementedError("Mailbox webmail user list_users endpoint is not implemented yet.")

    async def get_team_accesses_for_user(self) -> None:
        """Get team accesses for a user."""
        raise NotImplementedError(
            "Mailbox webmail user get_team_accesses_for_user endpoint is not implemented yet."
        )

    async def get_user_accesses_for_team(self) -> None:
        """Get user accesses for a team."""
        raise NotImplementedError(
            "Mailbox webmail user get_user_accesses_for_team endpoint is not implemented yet."
        )

    async def list_accesses_for_current_user(self) -> None:
        """List accesses for current user."""
        raise NotImplementedError(
            "Mailbox webmail user list_accesses_for_current_user endpoint is not implemented yet."
        )

    async def list_accesses_for_account_and_user(self) -> None:
        """List accesses for an account and a user."""
        raise NotImplementedError(
            "Mailbox webmail user list_accesses_for_account_and_user endpoint is not implemented yet."
        )

    async def delete_access_for_current_user(self) -> None:
        """Delete access to a mailbox for current user."""
        raise NotImplementedError(
            "Mailbox webmail user delete_access_for_current_user endpoint is not implemented yet."
        )


__all__ = ["User", "AsyncUser"]
