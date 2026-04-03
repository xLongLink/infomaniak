from infomaniak.resource import AsyncResource, Resouce


class Posts(Resouce):
    """kChat resource for posts endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for posts endpoints."""
        raise NotImplementedError("kChat posts endpoints are not implemented yet.")


class AsyncPosts(AsyncResource):
    """Async kChat resource for posts endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for posts endpoints."""
        raise NotImplementedError("kChat posts endpoints are not implemented yet.")
