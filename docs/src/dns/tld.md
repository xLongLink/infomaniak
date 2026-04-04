# Top Level Domain

The `dns.tld` resource provides methods to list available TLDs and show one TLD.

## List Top Level Domains

- params
  - `length` (`bool`, optional)
  - `periods` (`bool`, optional)
  - `group` (`bool`, optional)
  - `transfer_method` (`bool`, optional)
  - `is_idn` (`bool`, optional)
  - `support` (`bool`, optional)
  - `time` (`bool`, optional)
  - `groups` (`list[int] | None`, optional)
- returns
  - `list[Tld]`

```py
from infomaniak import Client

client = Client(token="<token>")
tlds = client.dns.tld.list(length=True, periods=True)
```

## Show Top Level Domain

- params
  - `tld` (`str`)
  - `length` (`bool`, optional)
  - `periods` (`bool`, optional)
  - `group` (`bool`, optional)
  - `transfer_method` (`bool`, optional)
  - `is_idn` (`bool`, optional)
  - `support` (`bool`, optional)
  - `time` (`bool`, optional)
- returns
  - `Tld`

```py
from infomaniak import Client

client = Client(token="<token>")
ch_tld = client.dns.tld.show("ch", length=True, support=True)
```
