from infomaniak.resource import AsyncResource, Resouce


class UserAccounts(Resouce):
    """Core user accounts endpoints."""

    def list(self) -> None:
        """List user accounts."""
        raise NotImplementedError("Core.user.accounts.list is not implemented yet.")

    def display(self) -> None:
        """Display one user account."""
        raise NotImplementedError("Core.user.accounts.display is not implemented yet.")

    def products(self) -> None:
        """List account products."""
        raise NotImplementedError("Core.user.accounts.products is not implemented yet.")

    def tags(self) -> None:
        """List account tags."""
        raise NotImplementedError("Core.user.accounts.tags is not implemented yet.")

    def services(self) -> None:
        """List account services."""
        raise NotImplementedError("Core.user.accounts.services is not implemented yet.")

    def apps(self) -> None:
        """List account apps."""
        raise NotImplementedError("Core.user.accounts.apps is not implemented yet.")

    def teams(self) -> None:
        """List account teams."""
        raise NotImplementedError("Core.user.accounts.teams is not implemented yet.")

    def users(self) -> None:
        """List account users."""
        raise NotImplementedError("Core.user.accounts.users is not implemented yet.")


class AsyncUserAccounts(AsyncResource):
    """Async core user accounts endpoints."""

    async def list(self) -> None:
        """List user accounts."""
        raise NotImplementedError("AsyncCore.user.accounts.list is not implemented yet.")

    async def display(self) -> None:
        """Display one user account."""
        raise NotImplementedError("AsyncCore.user.accounts.display is not implemented yet.")

    async def products(self) -> None:
        """List account products."""
        raise NotImplementedError("AsyncCore.user.accounts.products is not implemented yet.")

    async def tags(self) -> None:
        """List account tags."""
        raise NotImplementedError("AsyncCore.user.accounts.tags is not implemented yet.")

    async def services(self) -> None:
        """List account services."""
        raise NotImplementedError("AsyncCore.user.accounts.services is not implemented yet.")

    async def apps(self) -> None:
        """List account apps."""
        raise NotImplementedError("AsyncCore.user.accounts.apps is not implemented yet.")

    async def teams(self) -> None:
        """List account teams."""
        raise NotImplementedError("AsyncCore.user.accounts.teams is not implemented yet.")

    async def users(self) -> None:
        """List account users."""
        raise NotImplementedError("AsyncCore.user.accounts.users is not implemented yet.")
