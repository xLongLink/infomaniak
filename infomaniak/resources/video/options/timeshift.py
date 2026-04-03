from infomaniak.resource import AsyncResource, Resouce


class Timeshift(Resouce):
    """Video timeshift option endpoints."""

    def show(self) -> None:
        raise NotImplementedError("Video.options.timeshift.show is not implemented yet.")

    def create(self) -> None:
        raise NotImplementedError("Video.options.timeshift.create is not implemented yet.")

    def update(self) -> None:
        raise NotImplementedError("Video.options.timeshift.update is not implemented yet.")


class AsyncTimeshift(AsyncResource):
    """Async video timeshift option endpoints."""

    async def show(self) -> None:
        raise NotImplementedError("AsyncVideo.options.timeshift.show is not implemented yet.")

    async def create(self) -> None:
        raise NotImplementedError("AsyncVideo.options.timeshift.create is not implemented yet.")

    async def update(self) -> None:
        raise NotImplementedError("AsyncVideo.options.timeshift.update is not implemented yet.")
