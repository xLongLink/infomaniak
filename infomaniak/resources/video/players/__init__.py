from infomaniak.resource import AsyncResource, Resouce

from .ads import AsyncAds, Ads
from .embeds import AsyncEmbeds, Embeds
from .picture import AsyncPicture, Picture


class Players(Resouce):
    """Video player endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.ads = Ads(client)
        self.embeds = Embeds(client)
        self.picture = Picture(client)

    def list(self) -> None:
        raise NotImplementedError("Video.players.list is not implemented yet.")

    def create(self) -> None:
        raise NotImplementedError("Video.players.create is not implemented yet.")

    def display(self) -> None:
        raise NotImplementedError("Video.players.display is not implemented yet.")

    def update(self) -> None:
        raise NotImplementedError("Video.players.update is not implemented yet.")

    def copy(self) -> None:
        raise NotImplementedError("Video.players.copy is not implemented yet.")

    def delete(self) -> None:
        raise NotImplementedError("Video.players.delete is not implemented yet.")


class AsyncPlayers(AsyncResource):
    """Async video player endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.ads = AsyncAds(client)
        self.embeds = AsyncEmbeds(client)
        self.picture = AsyncPicture(client)

    async def list(self) -> None:
        raise NotImplementedError("AsyncVideo.players.list is not implemented yet.")

    async def create(self) -> None:
        raise NotImplementedError("AsyncVideo.players.create is not implemented yet.")

    async def display(self) -> None:
        raise NotImplementedError("AsyncVideo.players.display is not implemented yet.")

    async def update(self) -> None:
        raise NotImplementedError("AsyncVideo.players.update is not implemented yet.")

    async def copy(self) -> None:
        raise NotImplementedError("AsyncVideo.players.copy is not implemented yet.")

    async def delete(self) -> None:
        raise NotImplementedError("AsyncVideo.players.delete is not implemented yet.")


__all__ = ["Players", "AsyncPlayers", "Ads", "AsyncAds", "Embeds", "AsyncEmbeds", "Picture", "AsyncPicture"]
