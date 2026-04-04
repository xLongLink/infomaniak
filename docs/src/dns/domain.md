# Domain

The `dns.domain` resource provides methods to list domains and inspect one domain.

## List Domains

- `account_id`: Filter domains by account ID.
- `expires_after`: Filter domains expiring after the provided UNIX timestamp.
- `expires_before`: Filter domains expiring before the provided UNIX timestamp.
- `order_by`: Sorting field, either `"expiration"` or `"name"`.
- `order_dir`: Sorting direction, either `"asc"` or `"desc"`.
- `search`: Search text used to filter domains.
- `tld`: Restrict results to a specific top-level domain.
- `page`: Page number for paginated queries.
- `per_page`: Number of items returned per page.

**returns:** `DomainListResponse` containing the list of domains and pagination metadata.

```py
from infomaniak import Client

client = Client(token="<token>")
domains = client.dns.domain.list(account_id=12345)
```

## Show Domain

- `domain`: Domain name to retrieve.

**returns:** `Domain` with details for the requested domain.

```py
from infomaniak import Client

client = Client(token="<token>")
domain = client.dns.domain.show("example.com")
```
