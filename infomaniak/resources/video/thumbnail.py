from infomaniak.resource import AsyncResource, Resouce


class Thumbnail(Resouce):
    """Video thumbnail endpoints."""

    def show(self) -> None:
        raise NotImplementedError("Video.thumbnail.show is not implemented yet.")


class AsyncThumbnail(AsyncResource):
    """Async video thumbnail endpoints."""

    async def show(self) -> None:
        raise NotImplementedError("AsyncVideo.thumbnail.show is not implemented yet.")
