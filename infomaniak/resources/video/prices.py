from infomaniak.resource import AsyncResource, Resouce


class Prices(Resouce):
    """Video pricing endpoints."""

    def price(self) -> None:
        raise NotImplementedError("Video.prices.price is not implemented yet.")

    def description(self) -> None:
        raise NotImplementedError("Video.prices.description is not implemented yet.")


class AsyncPrices(AsyncResource):
    """Async video pricing endpoints."""

    async def price(self) -> None:
        raise NotImplementedError("AsyncVideo.prices.price is not implemented yet.")

    async def description(self) -> None:
        raise NotImplementedError("AsyncVideo.prices.description is not implemented yet.")
