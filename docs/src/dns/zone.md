# Zone

The `dns.zone` resource manages DNS zones and basic zone lifecycle operations.

## Display Zone

- `zone`: Fully qualified domain name of the DNS zone to retrieve.
- `skel`: Include raw zone skeleton text when set to `True`.
- `records`: Include DNS records in the response when set to `True`.
- `description`: Include record-level descriptions when set to `True`.
- `idn`: Include IDN fields when set to `True`.
- `label`: Include a human-readable zone label when set to `True`.

```py
from infomaniak import Client
from infomaniak.models.dns.zone import DNSZone

client = Client()
zone: DNSZone = client.dns.zone.display("example.com", records=...)
```

`DNSZone`:

- `domain`: Zone domain name.
- `ttl`: Zone default TTL.
- `records`: DNS record list when requested.
- `idn`: IDN details when requested.
- `label`: Human-readable label when requested.

## Update Zone

- `zone`: Fully qualified domain name of the DNS zone to update.
- `zone_skel`: New zone skeleton content.
- `skel`: Include raw updated skeleton text when set to `True`.
- `records`: Include updated DNS records when set to `True`.
- `description`: Include record-level descriptions when set to `True`.
- `idn`: Include IDN fields when set to `True`.

```py
from infomaniak import Client
from infomaniak.models.dns.zone import DNSZone

client = Client()
updated: DNSZone = client.dns.zone.update("example.com", "$ORIGIN example.com.")
```

`DNSZone`:

- `domain`: Zone domain name.
- `ttl`: Zone default TTL.
- `records`: Updated DNS records when requested.
- `idn`: IDN details when requested.

## Store Zone

- `zone`: Fully qualified domain name of the DNS zone to create.
- `zone_skel`: Initial zone skeleton content, or `None` to use defaults.
- `skel`: Include raw created skeleton text when set to `True`.
- `records`: Include created DNS records when set to `True`.
- `description`: Include record-level descriptions when set to `True`.
- `idn`: Include IDN fields when set to `True`.

```py
from infomaniak import Client
from infomaniak.models.dns.zone import DNSZone

client = Client()
created: DNSZone = client.dns.zone.store("example.com", zone_skel=...)
```

`DNSZone`:

- `domain`: Zone domain name.
- `ttl`: Zone default TTL.
- `records`: Created DNS records when requested.
- `idn`: IDN details when requested.

## Delete Zone

- `zone`: Fully qualified domain name of the DNS zone to delete.

```py
from infomaniak import Client

client = Client()
removed: bool = client.dns.zone.delete("example.com")
```

`bool`:

- `True`: The zone deletion succeeded.
- `False`: The zone deletion did not succeed.

## Zone Exists

- `zone`: Fully qualified domain name of the DNS zone to check.

```py
from infomaniak import Client

client = Client()
exists: bool = client.dns.zone.exists("example.com")
```

`bool`:

- `True`: The zone exists.
- `False`: The zone does not exist.
