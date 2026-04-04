# DNS Zone Records

Manage `client.dns.zone.records` endpoints.

## Methods

- `list(zone, *, source=None, types=None, search=None, with_=None, page=None, per_page=None, order_by=None, order=None) -> list[DNSRecord]`
- `store(zone, target, ttl, type_, *, source=None, with_=None) -> DNSRecord`
- `display(zone, record) -> DNSRecord`
- `update(zone, record, target, ttl, *, with_=None) -> DNSRecord`
- `delete(zone, record) -> bool`
- `check(zone, record) -> bool`
- `match(zone, source, type_, target, ttl=3600) -> DNSRecord`

## Request models

- `store` body fields:
  - `target: str` (required)
  - `ttl: int` (required)
  - `type_: DNSRecordType` (required)
  - `source: str | None` (optional)
- `update` body fields:
  - `target: str`
  - `ttl: int`

## Returned models

- `DNSRecord` from `infomaniak.models.dns.zone`
- `bool` for `delete` and `check`

## Example

```py
from infomaniak import Client

client = Client(token="...")

record = client.dns.zone.records.match(
    zone="example.com",
    source="www.example.com",
    type_="A",
    target="203.0.113.10",
    ttl=3600,
)

print(record.id, record.source, record.target)
```
