from infomaniak.resource import AsyncResource, Resouce


class Embeds(Resouce):
    """Video player embed endpoints."""

    def code(self) -> None:
        raise NotImplementedError("Video.players.embeds.code is not implemented yet.")

    def url(self) -> None:
        raise NotImplementedError("Video.players.embeds.url is not implemented yet.")


class AsyncEmbeds(AsyncResource):
    """Async video player embed endpoints."""

    async def code(self) -> None:
        raise NotImplementedError("AsyncVideo.players.embeds.code is not implemented yet.")

    async def url(self) -> None:
        raise NotImplementedError("AsyncVideo.players.embeds.url is not implemented yet.")
