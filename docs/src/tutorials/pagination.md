# Pagination

Use the shared pagination helper to iterate over all pages returned by list endpoints.

## Basic pagination

```py
from infomaniak import Client
from infomaniak.utils.pagination import paginate

client = Client(token="YOUR_API_TOKEN")

for item in paginate(client.mail.mailboxes.list, account_id=12345, per_page=50):
    print(item)
```

## Pagination with filtering (`functools.partial`)

You can pre-apply filters with `functools.partial` and keep using the same helper.

```py
from functools import partial

from infomaniak import Client
from infomaniak.utils.pagination import paginate

client = Client(token="YOUR_API_TOKEN")

active_domains = partial(
    client.domain.domains.list,
    account_id=12345,
    status="active",
)

for domain in paginate(active_domains, per_page=100):
    print(domain)
```
