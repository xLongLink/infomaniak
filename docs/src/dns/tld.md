# Top Level Domain

The `dns.tld` resource lets you browse TLD metadata and inspect a specific TLD.

## List Top Level Domains

- `length`: Include allowed domain length constraints when set to `True`.
- `periods`: Include lifecycle periods (`renew_grace`, `redemption`, `deletion`) when set to `True`.
- `group`: Include group metadata when set to `True`.
- `transfer_method`: Include transfer method details when set to `True`.
- `is_idn`: Include internationalized domain name support when set to `True`.
- `support`: Include support capability flags when set to `True`.
- `time`: Include registration and transfer timing details when set to `True`.
- `groups`: Restrict results to specific group identifiers.

```py
from infomaniak import Client
from infomaniak.models.dns.tld import Tld

client = Client()
tlds: list[Tld] = client.dns.tld.list(length=..., periods=..., support=...)
```

`list[Tld]`:

- `[]`: A list containing matching `Tld` objects.

## Show Top Level Domain

- `tld`: TLD code to retrieve (for example `ch` or `com`).
- `length`: Include allowed domain length constraints when set to `True`.
- `periods`: Include lifecycle periods when set to `True`.
- `group`: Include group metadata when set to `True`.
- `transfer_method`: Include transfer method details when set to `True`.
- `is_idn`: Include internationalized domain name support when set to `True`.
- `support`: Include support capability flags when set to `True`.
- `time`: Include registration and transfer timing details when set to `True`.

```py
from infomaniak import Client
from infomaniak.models.dns.tld import Tld

client = Client()
ch_tld: Tld = client.dns.tld.show("ch", length=..., support=..., time=...)
```

`Tld`:

- `tld`: TLD code.
- `label`: Human-readable TLD label.
- `group`: Group metadata (`TldGroup`).
- `periods`: Lifecycle periods (`TldPeriods`).
- `support`: Capability flags (`TldSupport`).
- `transfer_method`: Transfer method metadata.
- `is_idn`: Internationalized domain support metadata.
- `time`: Registration and transfer timing metadata.
