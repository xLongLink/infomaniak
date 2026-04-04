# Top Level Domain

The `dns.tld` resource provides access to top-level domain (TLD) metadata, including lifecycle, support capabilities, transfer details, and optional registration fields.

## List Top Level Domains

- `length`: Include allowed domain length constraints for each TLD when set to `True`.
- `periods`: Include lifecycle periods (`renew_grace`, `redemption`, `deletion`) when set to `True`.
- `group`: Include TLD group information when set to `True`.
- `transfer_method`: Include transfer method details when set to `True`.
- `is_idn`: Include internationalized-domain support data when set to `True`.
- `support`: Include support capability flags (for example DNSSEC and transfer lock) when set to `True`.
- `time`: Include registration and transfer timing information when set to `True`.
- `groups`: Restrict the returned list to specific group identifiers.

**returns:** `list[Tld]` with matching top-level domains.

```py
from infomaniak import Client

client = Client(token="<token>")
tlds = client.dns.tld.list(length=True, periods=True, support=True)
```

## Show Top Level Domain

- `tld`: TLD code to retrieve, for example `ch` or `com`.
- `length`: Include allowed domain length constraints when set to `True`.
- `periods`: Include lifecycle periods when set to `True`.
- `group`: Include TLD group information when set to `True`.
- `transfer_method`: Include transfer method details when set to `True`.
- `is_idn`: Include internationalized-domain support data when set to `True`.
- `support`: Include support capability flags when set to `True`.
- `time`: Include registration and transfer timing information when set to `True`.

**returns:** `Tld` for the requested top-level domain.

```py
from infomaniak import Client

client = Client(token="<token>")
ch_tld = client.dns.tld.show("ch", length=True, support=True, time=True)
```

## Request Models

This resource does not use dedicated request model classes. Parameters are passed directly as method arguments.

## Returned Models

- `Tld`: Main TLD payload.
- `TldGroup`: TLD group metadata.
- `TldPeriods`: Lifecycle periods.
- `TldSupport`: Supported capabilities.
- `TldOutgoingTransferNeed`: Outgoing transfer requirements.
- `TldFields`: Additional registration/transfer fields.
- `TldField`, `TldFieldOption`, `TldFieldCondition`, `TldContactField`: Field definitions and constraints.
- `IDNTable`: Internationalized domain name tables.
