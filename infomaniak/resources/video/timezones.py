from infomaniak.resource import AsyncResource, Resouce


class Timezones(Resouce):
    """Video timezones endpoints."""

    def list(self) -> None:
        raise NotImplementedError("Video.timezones.list is not implemented yet.")


class AsyncTimezones(AsyncResource):
    """Async video timezones endpoints."""

    async def list(self) -> None:
        raise NotImplementedError("AsyncVideo.timezones.list is not implemented yet.")
