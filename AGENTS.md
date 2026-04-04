# Infomaniak SDK client for Python

- For the time being, do not write an test cases
- Target Python 3.11+ and use modern type-hint syntax everywhere, such as `str | None`, `list[str]`, and `dict[str, Any]`.
- Follow the API structure in `openapi.json` for the type hints, the docstrings, and the method signatures.
- Each function must include a Google-style docstring with a short summary plus explicit `Args:` and `Returns:` sections.

Example:

```python
def example(self, foo: int, bar: float) -> bool:
    """
    Example function for demonstration purposes.

    Args:
        foo: The unique identifier of the foo.
        bar: The unique identifier of the bar.

    Returns:
        bool: True if the revocation was successful, False otherwise.
    """
```

## Pre commit

```
isort .
```
