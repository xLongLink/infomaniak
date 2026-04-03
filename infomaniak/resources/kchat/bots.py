from infomaniak.resource import AsyncResource, Resouce


class Bots(Resouce):
    """kChat resource for bots endpoints."""

    def create(self) -> None:
        """Create a bot."""
        raise NotImplementedError("kChat bots.create endpoint is not implemented yet.")

    def list(self) -> None:
        """List bots."""
        raise NotImplementedError("kChat bots.list endpoint is not implemented yet.")

    def update(self) -> None:
        """Patch or update a bot."""
        raise NotImplementedError("kChat bots.update endpoint is not implemented yet.")

    def display(self) -> None:
        """Get a single bot."""
        raise NotImplementedError("kChat bots.display endpoint is not implemented yet.")

    def disable(self) -> None:
        """Disable a bot."""
        raise NotImplementedError("kChat bots.disable endpoint is not implemented yet.")

    def enable(self) -> None:
        """Enable a bot."""
        raise NotImplementedError("kChat bots.enable endpoint is not implemented yet.")


class AsyncBots(AsyncResource):
    """Async kChat resource for bots endpoints."""

    async def create(self) -> None:
        """Create a bot."""
        raise NotImplementedError("kChat bots.create endpoint is not implemented yet.")

    async def list(self) -> None:
        """List bots."""
        raise NotImplementedError("kChat bots.list endpoint is not implemented yet.")

    async def update(self) -> None:
        """Patch or update a bot."""
        raise NotImplementedError("kChat bots.update endpoint is not implemented yet.")

    async def display(self) -> None:
        """Get a single bot."""
        raise NotImplementedError("kChat bots.display endpoint is not implemented yet.")

    async def disable(self) -> None:
        """Disable a bot."""
        raise NotImplementedError("kChat bots.disable endpoint is not implemented yet.")

    async def enable(self) -> None:
        """Enable a bot."""
        raise NotImplementedError("kChat bots.enable endpoint is not implemented yet.")
