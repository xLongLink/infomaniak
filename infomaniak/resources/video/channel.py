from infomaniak.resource import AsyncResource, Resouce


class Channel(Resouce):
    """Video channel endpoints."""

    def list(self) -> None:
        raise NotImplementedError("Video.channel.list is not implemented yet.")

    def create(self) -> None:
        raise NotImplementedError("Video.channel.create is not implemented yet.")

    def display(self) -> None:
        raise NotImplementedError("Video.channel.display is not implemented yet.")

    def update(self) -> None:
        raise NotImplementedError("Video.channel.update is not implemented yet.")

    def delete(self) -> None:
        raise NotImplementedError("Video.channel.delete is not implemented yet.")

    def config(self) -> None:
        raise NotImplementedError("Video.channel.config is not implemented yet.")


class AsyncChannel(AsyncResource):
    """Async video channel endpoints."""

    async def list(self) -> None:
        raise NotImplementedError("AsyncVideo.channel.list is not implemented yet.")

    async def create(self) -> None:
        raise NotImplementedError("AsyncVideo.channel.create is not implemented yet.")

    async def display(self) -> None:
        raise NotImplementedError("AsyncVideo.channel.display is not implemented yet.")

    async def update(self) -> None:
        raise NotImplementedError("AsyncVideo.channel.update is not implemented yet.")

    async def delete(self) -> None:
        raise NotImplementedError("AsyncVideo.channel.delete is not implemented yet.")

    async def config(self) -> None:
        raise NotImplementedError("AsyncVideo.channel.config is not implemented yet.")
