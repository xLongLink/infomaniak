from infomaniak.resource import AsyncResource, Resouce


class Files(Resouce):
    """kChat resource for files endpoints."""

    def upload(self) -> None:
        """Upload a file."""
        raise NotImplementedError("kChat files.upload endpoint is not implemented yet.")

    def get(self) -> None:
        """Get a file by ID."""
        raise NotImplementedError("kChat files.get endpoint is not implemented yet.")

    def thumbnail(self) -> None:
        """Get a file's thumbnail."""
        raise NotImplementedError("kChat files.thumbnail endpoint is not implemented yet.")

    def preview(self) -> None:
        """Get a file's preview."""
        raise NotImplementedError("kChat files.preview endpoint is not implemented yet.")

    def metadata(self) -> None:
        """Get metadata for a file."""
        raise NotImplementedError("kChat files.metadata endpoint is not implemented yet.")


class AsyncFiles(AsyncResource):
    """Async kChat resource for files endpoints."""

    async def upload(self) -> None:
        """Upload a file."""
        raise NotImplementedError("kChat files.upload endpoint is not implemented yet.")

    async def get(self) -> None:
        """Get a file by ID."""
        raise NotImplementedError("kChat files.get endpoint is not implemented yet.")

    async def thumbnail(self) -> None:
        """Get a file's thumbnail."""
        raise NotImplementedError("kChat files.thumbnail endpoint is not implemented yet.")

    async def preview(self) -> None:
        """Get a file's preview."""
        raise NotImplementedError("kChat files.preview endpoint is not implemented yet.")

    async def metadata(self) -> None:
        """Get metadata for a file."""
        raise NotImplementedError("kChat files.metadata endpoint is not implemented yet.")
