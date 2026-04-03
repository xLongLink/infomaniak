from infomaniak.resource import AsyncResource, Resouce


class Roles(Resouce):
    """kChat resource for roles endpoints."""

    def list(self) -> None:
        """List all roles."""
        raise NotImplementedError("kChat roles.list endpoint is not implemented yet.")

    def display(self) -> None:
        """Get a role by ID."""
        raise NotImplementedError("kChat roles.display endpoint is not implemented yet.")

    def by_name(self) -> None:
        """Get a role by name."""
        raise NotImplementedError("kChat roles.by_name endpoint is not implemented yet.")

    def by_names(self) -> None:
        """Get roles by a list of names."""
        raise NotImplementedError("kChat roles.by_names endpoint is not implemented yet.")


class AsyncRoles(AsyncResource):
    """Async kChat resource for roles endpoints."""

    async def list(self) -> None:
        """List all roles."""
        raise NotImplementedError("kChat roles.list endpoint is not implemented yet.")

    async def display(self) -> None:
        """Get a role by ID."""
        raise NotImplementedError("kChat roles.display endpoint is not implemented yet.")

    async def by_name(self) -> None:
        """Get a role by name."""
        raise NotImplementedError("kChat roles.by_name endpoint is not implemented yet.")

    async def by_names(self) -> None:
        """Get roles by a list of names."""
        raise NotImplementedError("kChat roles.by_names endpoint is not implemented yet.")
