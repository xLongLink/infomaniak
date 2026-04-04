# Infomaniak SDK client for Python

You are a senior Python developer tasked with implementing the Infomaniak SDK client for Python. The client should provide an easy-to-use interface for interacting with the Infomaniak API, allowing developers to perform various operations such as managing accounts, services, and users, strictly follow the guidelines:

- For the time being, do not write an test cases
- Target Python 3.11+ and use modern type-hint syntax everywhere, such as `str | None`, `list[str]`, and `dict[str, Any]` instead of `Optional[str]`, `List[str]`, or `Dict[str, Any]`.
- Follow the API structure in `openapi.json` for the type hints, the docstrings, and the method signatures.
- Each function must include a Google-style docstring with a short summary plus explicit `Args:` and `Returns:` sections.

Example:

```python
def revoke(self, account: int, invitation: int) -> bool:
    """
    Revoke an invitation associated with a specific account.

    Args:
        account (int): The unique identifier of the account.
        invitation (int): The unique identifier of the invitation to revoke.

    Returns:
        bool: True if the revocation was successful, False otherwise.
    """
    url = f"/1/accounts/{account}/invitations/{invitation}"
    response = self._client.delete(url)
    payload = response.json()
    return bool(payload.get("result") == "success")
```

## Structure

- Keep the SDK organized around three mirrored trees: `infomaniak/resources`, `infomaniak/models`, and `docs/src`.
- Resources define the public SDK navigation. Their directory tree is the source of truth for how domains and nested endpoints are grouped.
- Docs must follow the exact same tree as the resources so the docs side menu mirrors the SDK structure.
- When a resource exists at `infomaniak/resources/<domain>/<path>`, the documentation page must exist at `docs/src/<domain>/<path>.md`.
- Example: `infomaniak/resources/core/user` maps to `docs/src/core/user.md`.
- Example: `infomaniak/resources/core/user/teams` maps to `docs/src/core/user/teams.md`.
- Models should also be grouped by the same top-level domains as the resources whenever the schema belongs to that domain, for example `infomaniak/models/core/user.py` for models used by `infomaniak/resources/core/user`.
- If a resource requires several request or response models, keep them together in the matching domain module instead of creating unrelated flat files.
- Prefer one coherent nested tree per API area over a flat structure. If an endpoint is nested in resources, keep the same nesting logic in docs and in the related model placement.
- Doc pages should describe the corresponding resource, its methods, the expected request models, the returned models, and include short usage examples when useful.
- When adding a new resource, update all three layers together when applicable: the resource implementation, the related models, and the matching markdown page under `docs/src`.
