from typing import Literal

from dacite import from_dict

from infomaniak.models.core.user import AccountInvitation
from infomaniak.resource import AsyncResource, Resouce

from .accounts import AsyncUserAccounts, UserAccounts
from .teams import AsyncUserTeams, UserTeams


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
    ) -> AccountInvitation:
        """Invite a user in an account."""
        url = f"/1/accounts/{account}/invitations"
        params = {"with": with_} if with_ is not None else None

        payload: dict[str, object] = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "locale": locale,
            "role_type": role_type,
        }

        notifications: dict[str, bool] = {}
        if notifications_billing is not None:
            notifications["billing"] = notifications_billing
        if notifications_products is not None:
            notifications["products"] = notifications_products
        if notifications:
            payload["notifications"] = notifications

        permissions: dict[str, bool] = {}
        if permissions_billing is not None:
            permissions["billing"] = permissions_billing
        if permissions:
            payload["permissions"] = permissions

        if silent is not None:
            payload["silent"] = silent
        if strict is not None:
            payload["strict"] = strict
        if teams is not None:
            payload["teams"] = teams

        response = self._client.post(url, json=payload, params=params)
        return from_dict(AccountInvitation, response.json()["data"])

    def cancel(self, account: int, invitation: int) -> bool:
        """Cancel an invitation to join an account."""
        return self.revoke(account, invitation)

    def revoke(self, account: int, invitation: int) -> bool:
        """Revoke an invitation to join an account."""
        url = f"/1/accounts/{account}/invitations/{invitation}"
        response = self._client.delete(url)
        payload = response.json()
        return bool(payload.get("result") == "success")


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
    ) -> AccountInvitation:
        """Invite a user in an account."""
        url = f"/1/accounts/{account}/invitations"
        params = {"with": with_} if with_ is not None else None

        payload: dict[str, object] = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "locale": locale,
            "role_type": role_type,
        }

        notifications: dict[str, bool] = {}
        if notifications_billing is not None:
            notifications["billing"] = notifications_billing
        if notifications_products is not None:
            notifications["products"] = notifications_products
        if notifications:
            payload["notifications"] = notifications

        permissions: dict[str, bool] = {}
        if permissions_billing is not None:
            permissions["billing"] = permissions_billing
        if permissions:
            payload["permissions"] = permissions

        if silent is not None:
            payload["silent"] = silent
        if strict is not None:
            payload["strict"] = strict
        if teams is not None:
            payload["teams"] = teams

        response = await self._client.post(url, json=payload, params=params)
        return from_dict(AccountInvitation, response.json()["data"])

    async def cancel(self, account: int, invitation: int) -> bool:
        """Cancel an invitation to join an account."""
        return await self.revoke(account, invitation)

    async def revoke(self, account: int, invitation: int) -> bool:
        """Revoke an invitation to join an account."""
        url = f"/1/accounts/{account}/invitations/{invitation}"
        response = await self._client.delete(url)
        payload = response.json()
        return bool(payload.get("result") == "success")
