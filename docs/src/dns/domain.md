# Domain

The `dns.domain` resource lists domains and retrieves one domain.

## List Domains

- `account_id`: Filter by account identifier.
- `expires_after`: Filter domains expiring after this UNIX timestamp.
- `expires_before`: Filter domains expiring before this UNIX timestamp.
- `order_by`: Sort field (`"expiration"` or `"name"`).
- `order_dir`: Sort direction (`"asc"` or `"desc"`).
- `search`: Search text filter.
- `tld`: Restrict results to one TLD.
- `page`: Page number.
- `per_page`: Number of items per page.

```py
from infomaniak import Client
from infomaniak.pagination import PaginatedList
from infomaniak.models.dns.domain import Domain

client = Client()
domains: PaginatedList[Domain] = client.dns.domain.list(account_id=..., page=..., per_page=...)
```

`PaginatedList[Domain]`:

- `items`: Domain items for the current page.
- `page`: Current page number.
- `pages`: Total page count.
- `total`: Total domain count.

## Show Domain

- `domain`: Domain name to retrieve.

```py
from infomaniak import Client
from infomaniak.models.dns.domain import Domain

client = Client()
domain: Domain = client.dns.domain.show("example.com")
```

`Domain`:

- `name`: Domain name.
- `tld`: Top-level domain.
- `is_premium`: Premium flag.
- `created_at`: Creation UNIX timestamp.
- `expires_at`: Expiration UNIX timestamp.
- `options`: Domain options (`DomainOptions`).
- `contacts`: Contact details (`DomainContacts`).
- `status`: Registry status values.
