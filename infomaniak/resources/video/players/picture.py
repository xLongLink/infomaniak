from infomaniak.resource import AsyncResource, Resouce


class Picture(Resouce):
    """Video player picture endpoints."""

    def show(self) -> None:
        raise NotImplementedError("Video.players.picture.show is not implemented yet.")


class AsyncPicture(AsyncResource):
    """Async video player picture endpoints."""

    async def show(self) -> None:
        raise NotImplementedError("AsyncVideo.players.picture.show is not implemented yet.")
