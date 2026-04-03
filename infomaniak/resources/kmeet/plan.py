from infomaniak.resource import AsyncResource, Resouce


class Plan(Resouce):
    """kMeet resource for conference planning endpoints."""

    def plan_a_conference(self) -> None:
        """Placeholder for conference planning endpoints."""
        raise NotImplementedError("kMeet plan endpoints are not implemented yet.")


class AsyncPlan(AsyncResource):
    """Async kMeet resource for conference planning endpoints."""

    async def plan_a_conference(self) -> None:
        """Placeholder for conference planning endpoints."""
        raise NotImplementedError("kMeet plan endpoints are not implemented yet.")
