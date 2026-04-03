from infomaniak.resource import AsyncResource, Resouce


class Watermarking(Resouce):
    """Video watermark option endpoints."""

    def display(self) -> None:
        raise NotImplementedError("Video.options.watermarking.display is not implemented yet.")

    def update(self) -> None:
        raise NotImplementedError("Video.options.watermarking.update is not implemented yet.")

    def enable(self) -> None:
        raise NotImplementedError("Video.options.watermarking.enable is not implemented yet.")

    def disable(self) -> None:
        raise NotImplementedError("Video.options.watermarking.disable is not implemented yet.")


class AsyncWatermarking(AsyncResource):
    """Async video watermark option endpoints."""

    async def display(self) -> None:
        raise NotImplementedError("AsyncVideo.options.watermarking.display is not implemented yet.")

    async def update(self) -> None:
        raise NotImplementedError("AsyncVideo.options.watermarking.update is not implemented yet.")

    async def enable(self) -> None:
        raise NotImplementedError("AsyncVideo.options.watermarking.enable is not implemented yet.")

    async def disable(self) -> None:
        raise NotImplementedError("AsyncVideo.options.watermarking.disable is not implemented yet.")
