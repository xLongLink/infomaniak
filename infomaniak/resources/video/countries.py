from infomaniak.resource import AsyncResource, Resouce


class Countries(Resouce):
    """Video countries endpoints."""

    def list(self) -> None:
        raise NotImplementedError("Video.countries.list is not implemented yet.")


class AsyncCountries(AsyncResource):
    """Async video countries endpoints."""

    async def list(self) -> None:
        raise NotImplementedError("AsyncVideo.countries.list is not implemented yet.")
