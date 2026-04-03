from infomaniak.resource import AsyncResource, Resouce


class Stream(Resouce):
    """Video stream endpoints."""

    def generate_key(self) -> None:
        raise NotImplementedError("Video.stream.generate_key is not implemented yet.")


class AsyncStream(AsyncResource):
    """Async video stream endpoints."""

    async def generate_key(self) -> None:
        raise NotImplementedError("AsyncVideo.stream.generate_key is not implemented yet.")
