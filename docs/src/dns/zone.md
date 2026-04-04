# Zone

A DNS zone is the configuration for a domain’s DNS, and with it you can create, view, update, check, or delete all the DNS records that control how the domain works.

## Display Zone

- `zone`: Fully qualified domain name of the DNS zone to retrieve.
- `skel`: Include the raw zone skeleton text in the response when set to `True`.
- `records`: Include DNS records for the zone in the response when set to `True`.
- `records_description`: Include record-level descriptions in the response when set to `True`.
- `idn`: Return internationalized domain data when set to `True`.
- `label`: Include a human-readable label for the zone when set to `True`.

**returns:** `DNSZone` with the zone details returned by the API.

```py
from infomaniak import Client

client = Client()
zone = client.dns.zone.display("example.com", records=True)
```

## Update Zone

- `zone`: Fully qualified domain name of the DNS zone to update.
- `zone_skel`: New zone skeleton content to apply to the DNS zone.
- `skel`: Include the updated raw zone skeleton in the response when set to `True`.
- `records`: Include updated DNS records in the response when set to `True`.
- `records_description`: Include descriptions for updated records when set to `True`.
- `idn`: Return internationalized domain data when set to `True`.

**returns:** `DNSZone` with the updated zone data.

```py
from infomaniak import Client

client = Client()
updated = client.dns.zone.update("example.com", "$ORIGIN example.com.")
```

## Store Zone

- `zone`: Fully qualified domain name of the DNS zone to create.
- `zone_skel`: Initial zone skeleton content to create the zone, or `None` for defaults.
- `skel`: Include the created raw zone skeleton in the response when set to `True`.
- `records`: Include DNS records for the created zone in the response when set to `True`.
- `records_description`: Include descriptions for created records when set to `True`.
- `idn`: Return internationalized domain data when set to `True`.

**returns:** `DNSZone` with the newly created zone data.

```py
from infomaniak import Client

client = Client()
created = client.dns.zone.store("example.com", zone_skel="$ORIGIN example.com.")
```

## Delete Zone

- `zone`: Fully qualified domain name of the DNS zone to delete.

**returns:** `bool` indicating whether the zone deletion succeeded.

```py
from infomaniak import Client

client = Client()
removed = client.dns.zone.delete("example.com")
```

## Zone Exists

- `zone`: Fully qualified domain name of the DNS zone to check.

**returns:** `bool` indicating whether the DNS zone exists.

```py
from infomaniak import Client

client = Client()
exists = client.dns.zone.exists("example.com")
```
