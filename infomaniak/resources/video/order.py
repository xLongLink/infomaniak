from infomaniak.resource import AsyncResource, Resouce


class Order(Resouce):
    """Video order endpoints."""

    def list(self) -> None:
        raise NotImplementedError("Video.order.list is not implemented yet.")

    def display(self) -> None:
        raise NotImplementedError("Video.order.display is not implemented yet.")

    def update(self) -> None:
        raise NotImplementedError("Video.order.update is not implemented yet.")


class AsyncOrder(AsyncResource):
    """Async video order endpoints."""

    async def list(self) -> None:
        raise NotImplementedError("AsyncVideo.order.list is not implemented yet.")

    async def display(self) -> None:
        raise NotImplementedError("AsyncVideo.order.display is not implemented yet.")

    async def update(self) -> None:
        raise NotImplementedError("AsyncVideo.order.update is not implemented yet.")
