# DNS Zone

Manage `client.dns.zone` endpoints.

## Methods

- `display(zone, *, skel=False, records=False, records_description=False, idn=False, label=False) -> DNSZone`
- `update(zone, zone_skel, *, skel=False, records=False, records_description=False, idn=False) -> DNSZone`
- `store(zone, *, zone_skel=None, skel=False, records=False, records_description=False, idn=False) -> DNSZone`
- `delete(zone) -> bool`
- `exists(zone) -> bool`

## Nested Resources

- `records`

## Request models

- `update` body fields:
  - `zone_skel: str` (required, sent as API field `skel`)
- `store` body fields:
  - `zone_skel: str | None` (optional, sent as API field `skel`)

## Query parameters

- `display`: `skel`, `records`, `records_description`, `idn`, `label`
- `update`: `skel`, `records`, `records_description`, `idn`
- `store`: `skel`, `records`, `records_description`, `idn`

## Returned models

- `DNSZone` from `infomaniak.models.dns.zone`
- `bool` for `delete` and `exists`

## Example

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")

zone = client.dns.zone.display("example.com", records=True)
print(zone.id, zone.fqdn, zone.nameservers)

exists = client.dns.zone.exists("example.com")
print(exists)
```
