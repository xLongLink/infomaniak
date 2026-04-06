# Pagination

Some SDK endpoints return paginated responses. These methods return a `plist[T]`, which is a list subclass that also includes pagination metadata.

## Paginated return type

`plist[T]` behaves like a normal list and exposes:

- `page`: Current page number.
- `pages`: Total number of available pages.
- `items`: Total number of items available across all pages.

## Example

```py
from infomaniak import Client
from infomaniak.models.dns.domain import Domain
from infomaniak.utils import plist

client = Client()
domains: plist[Domain] = client.dns.domain.list(
    account_id=..., 
    page=1,
    per_page=20,
)

print(domains.page)
print(domains.pages)
print(domains.items)

for domain in domains:
    print(domain.name)
```

::: tip
Use `page` and `per_page` in list methods that support pagination to navigate through results.
:::
