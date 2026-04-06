# Domain

The `dns.domain` resource lets you list domains and inspect one domain.

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

```py
from infomaniak import Client

client = Client(token="<token>")
domains = client.dns.domain.list(account_id=12345, page=1, per_page=20)
```

`PaginatedList[Domain]`:

- `items`: List of `Domain` objects for the current page.
- `page`: Current page number.
- `pages`: Total number of pages.
- `total`: Total number of items across all pages.

## Show Domain

- `domain`: Domain name to retrieve.

```py
from infomaniak import Client

client = Client(token="<token>")
domain = client.dns.domain.show("example.com")
```

`Domain`:

- `name`: Domain name.
- `tld`: Top-level domain.
- `is_premium`: Whether the domain is a premium domain.
- `created_at`: Domain creation UNIX timestamp.
- `expires_at`: Domain expiration UNIX timestamp.
- `options`: Domain options (`DomainOptions`).
- `contacts`: Domain contacts grouped by role (`DomainContacts`).
- `status`: Current registry status flags.

## Request Models

This resource does not use dedicated request model classes. Parameters are passed directly as method arguments.

## Returned Models

- `Domain`: Main domain payload.
- `DomainOptions`: Domain option flags (`dns_anycast`, `renewal_warranty`, `domain_privacy`, `dnssec`).
- `DomainContacts`: Contact information grouped by role (`owner`, `admin`, `tech`, `billing`).
- `DomainContact`: Contact details for one role.
- `DomainAssociatedDomain`: Domain references attached to a contact.
- `DomainListResponse`: Raw API list response shape.

## Related Subresources

- `dns.domain.dnssec`
- `dns.domain.nameservers`
- `dns.domain.order`
