from infomaniak.resource import AsyncResource, Resouce


class Room(Resouce):
    """kMeet resource for room setting endpoints."""

    def get_room_settings(self) -> None:
        """Placeholder for room settings endpoints."""
        raise NotImplementedError("kMeet room endpoints are not implemented yet.")


class AsyncRoom(AsyncResource):
    """Async kMeet resource for room setting endpoints."""

    async def get_room_settings(self) -> None:
        """Placeholder for room settings endpoints."""
        raise NotImplementedError("kMeet room endpoints are not implemented yet.")
