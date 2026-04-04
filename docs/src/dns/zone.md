# Zone

The `dns.zone` resource provides methods to read, create, update, delete, and check the existence of DNS zones.

## Display Zone

- params
  - `zone` (`str`)
  - `skel` (`bool`, optional)
  - `records` (`bool`, optional)
  - `records_description` (`bool`, optional)
  - `idn` (`bool`, optional)
  - `label` (`bool`, optional)
- returns
  - `DNSZone`

```py
from infomaniak import Client

client = Client(token="<token>")
zone = client.dns.zone.display("example.com", records=True)
```

## Update Zone

- params
  - `zone` (`str`)
  - `zone_skel` (`str`)
  - `skel` (`bool`, optional)
  - `records` (`bool`, optional)
  - `records_description` (`bool`, optional)
  - `idn` (`bool`, optional)
- returns
  - `DNSZone`

```py
from infomaniak import Client

client = Client(token="<token>")
updated = client.dns.zone.update("example.com", "$ORIGIN example.com.")
```

## Store Zone

- params
  - `zone` (`str`)
  - `zone_skel` (`str | None`, optional)
  - `skel` (`bool`, optional)
  - `records` (`bool`, optional)
  - `records_description` (`bool`, optional)
  - `idn` (`bool`, optional)
- returns
  - `DNSZone`

```py
from infomaniak import Client

client = Client(token="<token>")
created = client.dns.zone.store("example.com", zone_skel="$ORIGIN example.com.")
```

## Delete Zone

- params
  - `zone` (`str`)
- returns
  - `bool`

```py
from infomaniak import Client

client = Client(token="<token>")
removed = client.dns.zone.delete("example.com")
```

## Zone Exists

- params
  - `zone` (`str`)
- returns
  - `bool`

```py
from infomaniak import Client

client = Client(token="<token>")
exists = client.dns.zone.exists("example.com")
```
