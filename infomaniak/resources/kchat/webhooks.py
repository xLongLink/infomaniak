from infomaniak.resource import AsyncResource, Resouce


class Webhooks(Resouce):
    """kChat resource for webhooks endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for webhooks endpoints."""
        raise NotImplementedError("kChat webhooks endpoints are not implemented yet.")


class AsyncWebhooks(AsyncResource):
    """Async kChat resource for webhooks endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for webhooks endpoints."""
        raise NotImplementedError("kChat webhooks endpoints are not implemented yet.")
