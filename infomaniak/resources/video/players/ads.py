from infomaniak.resource import AsyncResource, Resouce


class Ads(Resouce):
    """Video player ads endpoints."""

    def list(self) -> None:
        raise NotImplementedError("Video.players.ads.list is not implemented yet.")

    def create(self) -> None:
        raise NotImplementedError("Video.players.ads.create is not implemented yet.")

    def copy(self) -> None:
        raise NotImplementedError("Video.players.ads.copy is not implemented yet.")

    def display(self) -> None:
        raise NotImplementedError("Video.players.ads.display is not implemented yet.")

    def update(self) -> None:
        raise NotImplementedError("Video.players.ads.update is not implemented yet.")

    def delete(self) -> None:
        raise NotImplementedError("Video.players.ads.delete is not implemented yet.")


class AsyncAds(AsyncResource):
    """Async video player ads endpoints."""

    async def list(self) -> None:
        raise NotImplementedError("AsyncVideo.players.ads.list is not implemented yet.")

    async def create(self) -> None:
        raise NotImplementedError("AsyncVideo.players.ads.create is not implemented yet.")

    async def copy(self) -> None:
        raise NotImplementedError("AsyncVideo.players.ads.copy is not implemented yet.")

    async def display(self) -> None:
        raise NotImplementedError("AsyncVideo.players.ads.display is not implemented yet.")

    async def update(self) -> None:
        raise NotImplementedError("AsyncVideo.players.ads.update is not implemented yet.")

    async def delete(self) -> None:
        raise NotImplementedError("AsyncVideo.players.ads.delete is not implemented yet.")
