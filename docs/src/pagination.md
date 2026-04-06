# Pagination

Some endpoints are paginated. To keep it simple and pythonic, all the functions retuns a 


## Basic pagination

```py
from infomaniak import Client
from infomaniak.utils.pagination import paginate

client = Client()

for item in paginate(client.mail.mailboxes.list, account_id=..., per_page=...):
    print(item)
```

## Pagination with filtering (`functools.partial`)

You can pre-apply filters with `functools.partial` and keep using the same helper.

```py
from functools import partial

from infomaniak import Client
from infomaniak.utils.pagination import paginate

client = Client()

active_domains = partial(
    client.domain.domains.list,
    account_id=...,
    status=...,
)

for domain in paginate(active_domains, per_page=...):
    print(domain)
```
