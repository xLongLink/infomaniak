def _with(**fields: bool) -> str | None:
    """
    Build a comma-separated value for API `with` query parameters.

    Args:
        **fields (bool): Mapping of field names to inclusion flags.

    Returns:
        str | None: Comma-separated field names for truthy flags, or None if empty.
    """
    values = [key for key, include in fields.items() if include]
    return ",".join(values) if values else None
