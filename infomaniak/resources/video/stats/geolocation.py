from infomaniak.resource import AsyncResource, Resouce


class StatsGeolocation(Resouce):
    """Video statistics geolocation endpoints."""

    def countries(self) -> None:
        raise NotImplementedError("Video.stats.*.geolocation.countries is not implemented yet.")

    def clusters(self) -> None:
        raise NotImplementedError("Video.stats.*.geolocation.clusters is not implemented yet.")


class AsyncStatsGeolocation(AsyncResource):
    """Async video statistics geolocation endpoints."""

    async def countries(self) -> None:
        raise NotImplementedError("AsyncVideo.stats.*.geolocation.countries is not implemented yet.")

    async def clusters(self) -> None:
        raise NotImplementedError("AsyncVideo.stats.*.geolocation.clusters is not implemented yet.")
