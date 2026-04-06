# Infomaniak SDK client for Python

- For the time being, do not write an test cases
- Target Python 3.11+ and use modern type-hint syntax everywhere, such as `str | None`, `list[str]`, and `dict[str, Any]`.
- Follow the API structure in `openapi.json` for the type hints, the docstrings, and the method signatures.
- Each function must include a Google-style docstring with a short summary plus explicit `Args:` and `Returns:` sections.
- For every paginated list function in resources, use `page` and `items` as pagination parameters.
- For `plist` pagination metadata, use `total` (not `items`) for the total number of records.

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


## Docs

Follow this structure for the documentation pages `docs/src/*.md`, for each function:

- Parameter: Description
- Example usage (with type hint)
- Return objet + parameters of the object

```md
# <Title>

<Small description>

## Get Config

- `account_id`: Unique identifier of the account.

```
from infomaniak import Client

client = Client()
config: PublicCloudConfig = client.cloud.config.get(account_id=...)
```

`PublicCloudConfig`:

- `free_tier`: Amount of free tier credit available for the account.
- `free_tier_used`: Amount of free tier credit already consumed.
- `account_resource_level`: Resource level assigned to the account.
- `valid_from`: Unix timestamp indicating when the configuration becomes valid.
- `valid_to`: Unix timestamp indicating when the configuration expires.
- `project_count`: Number of projects currently attached to the account.

```

## Pre commit

```
isort .
```
