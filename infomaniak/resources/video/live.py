from infomaniak.resource import AsyncResource, Resouce


class Live(Resouce):
    """Video live control endpoints."""

    def resume(self) -> None:
        raise NotImplementedError("Video.live.resume is not implemented yet.")

    def interrupt(self) -> None:
        raise NotImplementedError("Video.live.interrupt is not implemented yet.")


class AsyncLive(AsyncResource):
    """Async video live control endpoints."""

    async def resume(self) -> None:
        raise NotImplementedError("AsyncVideo.live.resume is not implemented yet.")

    async def interrupt(self) -> None:
        raise NotImplementedError("AsyncVideo.live.interrupt is not implemented yet.")
