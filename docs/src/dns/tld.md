# Top Level Domain

The `dns.tld` resource provides methods to list available TLDs and show one TLD.

## List Top Level Domains

**params:**
- `length` (`bool`, optional): Include allowed domain length constraints for each TLD when set to `True`.
- `periods` (`bool`, optional): Include supported registration periods for each TLD when set to `True`.
- `group` (`bool`, optional): Include group metadata for each TLD when set to `True`.
- `transfer_method` (`bool`, optional): Include supported transfer methods for each TLD when set to `True`.
- `is_idn` (`bool`, optional): Include internationalized-domain support information when set to `True`.
- `support` (`bool`, optional): Include support-level details for each TLD when set to `True`.
- `time` (`bool`, optional): Include timing metadata (for example activation delays) when set to `True`.
- `groups` (`list[int] | None`, optional): Filter the returned TLDs to the provided group identifiers.

**returns:** `list[Tld]` containing all matching top-level domains.

```py
from infomaniak import Client

client = Client(token="<token>")
tlds = client.dns.tld.list(length=True, periods=True)
```

## Show Top Level Domain

**params:**
- `tld` (`str`): TLD code to retrieve, for example `ch` or `com`.
- `length` (`bool`, optional): Include allowed domain length constraints when set to `True`.
- `periods` (`bool`, optional): Include supported registration periods when set to `True`.
- `group` (`bool`, optional): Include group metadata when set to `True`.
- `transfer_method` (`bool`, optional): Include supported transfer methods when set to `True`.
- `is_idn` (`bool`, optional): Include internationalized-domain support information when set to `True`.
- `support` (`bool`, optional): Include support-level details when set to `True`.
- `time` (`bool`, optional): Include timing metadata (for example activation delays) when set to `True`.

**returns:** `Tld` with details for the requested top-level domain.

```py
from infomaniak import Client

client = Client(token="<token>")
ch_tld = client.dns.tld.show("ch", length=True, support=True)
```
