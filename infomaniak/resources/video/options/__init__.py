from infomaniak.resource import AsyncResource, Resouce

from .record import AsyncRecord, Record
from .simulcast import AsyncSimulcast, Simulcast
from .timeshift import AsyncTimeshift, Timeshift
from .watermarking import AsyncWatermarking, Watermarking


class Options(Resouce):
    """Video options endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.record = Record(client)
        self.simulcast = Simulcast(client)
        self.timeshift = Timeshift(client)
        self.watermarking = Watermarking(client)

    def list(self) -> None:
        raise NotImplementedError("Video.options.list is not implemented yet.")

    def display(self) -> None:
        raise NotImplementedError("Video.options.display is not implemented yet.")

    def update(self) -> None:
        raise NotImplementedError("Video.options.update is not implemented yet.")

    def delete(self) -> None:
        raise NotImplementedError("Video.options.delete is not implemented yet.")


class AsyncOptions(AsyncResource):
    """Async video options endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.record = AsyncRecord(client)
        self.simulcast = AsyncSimulcast(client)
        self.timeshift = AsyncTimeshift(client)
        self.watermarking = AsyncWatermarking(client)

    async def list(self) -> None:
        raise NotImplementedError("AsyncVideo.options.list is not implemented yet.")

    async def display(self) -> None:
        raise NotImplementedError("AsyncVideo.options.display is not implemented yet.")

    async def update(self) -> None:
        raise NotImplementedError("AsyncVideo.options.update is not implemented yet.")

    async def delete(self) -> None:
        raise NotImplementedError("AsyncVideo.options.delete is not implemented yet.")


__all__ = [
    "Options",
    "AsyncOptions",
    "Record",
    "AsyncRecord",
    "Simulcast",
    "AsyncSimulcast",
    "Timeshift",
    "AsyncTimeshift",
    "Watermarking",
    "AsyncWatermarking",
]
