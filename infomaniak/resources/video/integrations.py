from infomaniak.resource import AsyncResource, Resouce


class Integrations(Resouce):
    """Video integration endpoints."""

    def code(self) -> None:
        raise NotImplementedError("Video.integrations.code is not implemented yet.")


class AsyncIntegrations(AsyncResource):
    """Async video integration endpoints."""

    async def code(self) -> None:
        raise NotImplementedError("AsyncVideo.integrations.code is not implemented yet.")
