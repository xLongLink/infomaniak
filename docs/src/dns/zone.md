# Zone

The `dns.zone` resource provides methods to read, create, update, delete, and check the existence of DNS zones.

## Display Zone

**params:**
- `zone` (`str`): Fully qualified domain name of the DNS zone to retrieve.
- `skel` (`bool`, optional): Include the raw zone skeleton text in the response when set to `True`.
- `records` (`bool`, optional): Include DNS records for the zone in the response when set to `True`.
- `records_description` (`bool`, optional): Include record-level descriptions in the response when set to `True`.
- `idn` (`bool`, optional): Return internationalized domain data when set to `True`.
- `label` (`bool`, optional): Include a human-readable label for the zone when set to `True`.

**returns:** `DNSZone` with the zone details returned by the API.

```py
from infomaniak import Client

client = Client(token="<token>")
zone = client.dns.zone.display("example.com", records=True)
```

## Update Zone

**params:**
- `zone` (`str`): Fully qualified domain name of the DNS zone to update.
- `zone_skel` (`str`): New zone skeleton content to apply to the DNS zone.
- `skel` (`bool`, optional): Include the updated raw zone skeleton in the response when set to `True`.
- `records` (`bool`, optional): Include updated DNS records in the response when set to `True`.
- `records_description` (`bool`, optional): Include descriptions for updated records when set to `True`.
- `idn` (`bool`, optional): Return internationalized domain data when set to `True`.

**returns:** `DNSZone` with the updated zone data.

```py
from infomaniak import Client

client = Client(token="<token>")
updated = client.dns.zone.update("example.com", "$ORIGIN example.com.")
```

## Store Zone

**params:**
- `zone` (`str`): Fully qualified domain name of the DNS zone to create.
- `zone_skel` (`str | None`, optional): Initial zone skeleton content to create the zone, or `None` for defaults.
- `skel` (`bool`, optional): Include the created raw zone skeleton in the response when set to `True`.
- `records` (`bool`, optional): Include DNS records for the created zone in the response when set to `True`.
- `records_description` (`bool`, optional): Include descriptions for created records when set to `True`.
- `idn` (`bool`, optional): Return internationalized domain data when set to `True`.

**returns:** `DNSZone` with the newly created zone data.

```py
from infomaniak import Client

client = Client(token="<token>")
created = client.dns.zone.store("example.com", zone_skel="$ORIGIN example.com.")
```

## Delete Zone

**params:**
- `zone` (`str`): Fully qualified domain name of the DNS zone to delete.

**returns:** `bool` indicating whether the zone deletion succeeded.

```py
from infomaniak import Client

client = Client(token="<token>")
removed = client.dns.zone.delete("example.com")
```

## Zone Exists

**params:**
- `zone` (`str`): Fully qualified domain name of the DNS zone to check.

**returns:** `bool` indicating whether the DNS zone exists.

```py
from infomaniak import Client

client = Client(token="<token>")
exists = client.dns.zone.exists("example.com")
```
