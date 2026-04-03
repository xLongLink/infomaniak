from infomaniak.resource import AsyncResource, Resouce


class Event(Resouce):
    """Video event endpoints."""

    def list(self) -> None:
        raise NotImplementedError("Video.event.list is not implemented yet.")

    def create(self) -> None:
        raise NotImplementedError("Video.event.create is not implemented yet.")

    def display(self) -> None:
        raise NotImplementedError("Video.event.display is not implemented yet.")

    def update(self) -> None:
        raise NotImplementedError("Video.event.update is not implemented yet.")

    def delete(self) -> None:
        raise NotImplementedError("Video.event.delete is not implemented yet.")


class AsyncEvent(AsyncResource):
    """Async video event endpoints."""

    async def list(self) -> None:
        raise NotImplementedError("AsyncVideo.event.list is not implemented yet.")

    async def create(self) -> None:
        raise NotImplementedError("AsyncVideo.event.create is not implemented yet.")

    async def display(self) -> None:
        raise NotImplementedError("AsyncVideo.event.display is not implemented yet.")

    async def update(self) -> None:
        raise NotImplementedError("AsyncVideo.event.update is not implemented yet.")

    async def delete(self) -> None:
        raise NotImplementedError("AsyncVideo.event.delete is not implemented yet.")
