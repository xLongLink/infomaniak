from typing import Literal
from .teams import UserTeams, AsyncUserTeams
from .accounts import UserAccounts, AsyncUserAccounts
from infomaniak.resource import Resouce, AsyncResource


class User(Resouce):
    """Core user endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.accounts = UserAccounts(client)
        self.teams = UserTeams(client)

    def invite(
        self,
        account: int,
        email: str,
        first_name: str,
        last_name: str,
        locale: Literal["de_DE", "en_GB", "es_ES", "fr_FR", "it_IT"],
        role_type: Literal["admin", "normal", "owner"],
        *,
        notifications_billing: bool | None = None,
        notifications_products: bool | None = None,
        permissions_billing: bool | None = None,
        silent: bool | None = None,
        strict: bool | None = None,
        teams: list[int] | None = None,
        with_: str | None = None,
    ) -> None:
        """Invite a user in an account."""
        raise NotImplementedError("Core.user.invite is not implemented yet.")

    def cancel(self, account: int, invitation: int) -> bool:
        """Cancel an invitation to join an account."""
        raise NotImplementedError("Core.user.cancel is not implemented yet.")

    def revoke(self, account: int, invitation: int) -> bool:
        """Revoke an invitation to join an account."""
        raise NotImplementedError("Core.user.revoke is not implemented yet.")


class AsyncUser(AsyncResource):
    """Async core user endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.accounts = AsyncUserAccounts(client)
        self.teams = AsyncUserTeams(client)

    async def invite(
        self,
        account: int,
        email: str,
        first_name: str,
        last_name: str,
        locale: Literal["de_DE", "en_GB", "es_ES", "fr_FR", "it_IT"],
        role_type: Literal["admin", "normal", "owner"],
        *,
        notifications_billing: bool | None = None,
        notifications_products: bool | None = None,
        permissions_billing: bool | None = None,
        silent: bool | None = None,
        strict: bool | None = None,
        teams: list[int] | None = None,
        with_: str | None = None,
    ) -> None:
        """Invite a user in an account."""
        raise NotImplementedError("AsyncCore.user.invite is not implemented yet.")

    async def cancel(self, account: int, invitation: int) -> bool:
        """Cancel an invitation to join an account."""
        raise NotImplementedError("AsyncCore.user.cancel is not implemented yet.")

    async def revoke(self, account: int, invitation: int) -> bool:
        """Revoke an invitation to join an account."""
        raise NotImplementedError("AsyncCore.user.revoke is not implemented yet.")
