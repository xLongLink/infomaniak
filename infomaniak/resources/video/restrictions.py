from infomaniak.resource import AsyncResource, Resouce


class Restrictions(Resouce):
    """Video restriction endpoints."""

    def show(self) -> None:
        raise NotImplementedError("Video.restrictions.show is not implemented yet.")

    def update_channels(self) -> None:
        raise NotImplementedError("Video.restrictions.update_channels is not implemented yet.")

    def geographical(self) -> None:
        raise NotImplementedError("Video.restrictions.geographical is not implemented yet.")

    def update_password(self) -> None:
        raise NotImplementedError("Video.restrictions.update_password is not implemented yet.")


class AsyncRestrictions(AsyncResource):
    """Async video restriction endpoints."""

    async def show(self) -> None:
        raise NotImplementedError("AsyncVideo.restrictions.show is not implemented yet.")

    async def update_channels(self) -> None:
        raise NotImplementedError("AsyncVideo.restrictions.update_channels is not implemented yet.")

    async def geographical(self) -> None:
        raise NotImplementedError("AsyncVideo.restrictions.geographical is not implemented yet.")

    async def update_password(self) -> None:
        raise NotImplementedError("AsyncVideo.restrictions.update_password is not implemented yet.")
