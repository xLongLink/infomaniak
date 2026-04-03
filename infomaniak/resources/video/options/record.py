from infomaniak.resource import AsyncResource, Resouce


class RecordStorage(Resouce):
    """Video recording storage endpoints."""

    def show(self) -> None:
        raise NotImplementedError("Video.options.record.storage.show is not implemented yet.")

    def create(self) -> None:
        raise NotImplementedError("Video.options.record.storage.create is not implemented yet.")

    def update(self) -> None:
        raise NotImplementedError("Video.options.record.storage.update is not implemented yet.")


class AsyncRecordStorage(AsyncResource):
    """Async video recording storage endpoints."""

    async def show(self) -> None:
        raise NotImplementedError("AsyncVideo.options.record.storage.show is not implemented yet.")

    async def create(self) -> None:
        raise NotImplementedError("AsyncVideo.options.record.storage.create is not implemented yet.")

    async def update(self) -> None:
        raise NotImplementedError("AsyncVideo.options.record.storage.update is not implemented yet.")


class Record(Resouce):
    """Video recording option endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.storage = RecordStorage(client)

    def start(self) -> None:
        raise NotImplementedError("Video.options.record.start is not implemented yet.")

    def stop(self) -> None:
        raise NotImplementedError("Video.options.record.stop is not implemented yet.")


class AsyncRecord(AsyncResource):
    """Async video recording option endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.storage = AsyncRecordStorage(client)

    async def start(self) -> None:
        raise NotImplementedError("AsyncVideo.options.record.start is not implemented yet.")

    async def stop(self) -> None:
        raise NotImplementedError("AsyncVideo.options.record.stop is not implemented yet.")
