from infomaniak.resource import AsyncResource, Resouce


class Simulcast(Resouce):
    """Video simulcast option endpoints."""

    def create(self) -> None:
        raise NotImplementedError("Video.options.simulcast.create is not implemented yet.")

    def list(self) -> None:
        raise NotImplementedError("Video.options.simulcast.list is not implemented yet.")

    def display(self) -> None:
        raise NotImplementedError("Video.options.simulcast.display is not implemented yet.")

    def update(self) -> None:
        raise NotImplementedError("Video.options.simulcast.update is not implemented yet.")

    def delete(self) -> None:
        raise NotImplementedError("Video.options.simulcast.delete is not implemented yet.")

    def disable(self) -> None:
        raise NotImplementedError("Video.options.simulcast.disable is not implemented yet.")


class AsyncSimulcast(AsyncResource):
    """Async video simulcast option endpoints."""

    async def create(self) -> None:
        raise NotImplementedError("AsyncVideo.options.simulcast.create is not implemented yet.")

    async def list(self) -> None:
        raise NotImplementedError("AsyncVideo.options.simulcast.list is not implemented yet.")

    async def display(self) -> None:
        raise NotImplementedError("AsyncVideo.options.simulcast.display is not implemented yet.")

    async def update(self) -> None:
        raise NotImplementedError("AsyncVideo.options.simulcast.update is not implemented yet.")

    async def delete(self) -> None:
        raise NotImplementedError("AsyncVideo.options.simulcast.delete is not implemented yet.")

    async def disable(self) -> None:
        raise NotImplementedError("AsyncVideo.options.simulcast.disable is not implemented yet.")
