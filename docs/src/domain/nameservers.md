# Domain Nameservers

Manage `client.domain.nameservers` endpoints.

## Methods

- `update(domain, *, nameservers=None, use_infomaniak_ns=None, verify_ns_availability=False)`

## `update`

Update a domain nameserver configuration using `PUT /2/domains/domains/{domain}/nameservers`.

### Request model

`UpdateNameserversRequest` (`infomaniak.models.domain.nameservers`):

- `nameservers: list[str] | None`  
  Custom nameservers. Must contain at least 2 values when provided.
- `use_infomaniak_ns: bool | None`  
  Use Infomaniak nameservers. Required when `nameservers` is omitted.
- `verify_ns_availability: bool` (default `False`)  
  Verify nameserver availability before applying the change.

### Response model

`UpdateNameserversResponse` (`infomaniak.models.domain.nameservers`):

- `result: Literal["success", "error", "asynchronous"]`
- `data: bool`

### Example

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
response = client.domain.nameservers.update(
    "example.com",
    nameservers=["ns1.mydomain.ch", "ns2.mydomain.ch"],
    verify_ns_availability=True,
)

print(response.result)
print(response.data)
```
