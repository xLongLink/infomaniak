# Overview

::: warning
This SDK and its documentation are currently in active development. Endpoints, method signatures, and coverage can change without notice.
:::

## How to install

```bash
pip install xinfomaniak
```

## Pagination example

Use the shared pagination helper to iterate through all pages for a list endpoint.

```py
from infomaniak import Client
from infomaniak.utils.pagination import paginate

client = Client(token="YOUR_API_TOKEN")

for item in paginate(client.mail.mailboxes.list, account_id=12345, per_page=50):
    print(item)
```

## Pagination with filtering (`functools.partial`)

You can pre-apply filters with `functools.partial` and still paginate with the same helper.

```py
from functools import partial

from infomaniak import Client
from infomaniak.utils.pagination import paginate

client = Client(token="YOUR_API_TOKEN")

active_domains = partial(
    client.domain.domains.list,
    account_id=12345,
    status="active",
)

for domain in paginate(active_domains, per_page=100):
    print(domain)
```

## API Resources

Infomaniak OpenAPI v3.1.0

| Resource                     | Infomaniak Reference                      | Status                                        |
| ---------------------------- | ----------------------------------------- | --------------------------------------------- |
| `ai`                         | AI Tools                                  | <span style="color:red">Low priority</span>   |
| `backup`                     | Swiss Backup                              | <span style="color:red">Low priority</span>   |
| [`cloud`](/cloud/)           | Cloud Overview                            | <span style="color:orange">Planned</span>     |
| `core`                       | Core Resources                            | <span style="color:red">Low priority</span>   |
| [`dns`](/dns/)               | Domain and Zones                          | <span style="color:yellow">In progress</span> |
| `domain`                     | Domain Overview                           | <span style="color:red">Low priority</span>   |
| `etickets`                   | [ETickets](https://chk.me/kOM6ZoO)        | <span style="color:red">Low priority</span>   |
| `kchat`                      | [kChat](https://chk.me/sXgWvJp)           | <span style="color:red">Low priority</span>   |
| `kdrive`                     | [kDrive](https://chk.me/qlJozmn)          | <span style="color:red">Low priority</span>   |
| `kmeet`                      | [kMeet](https://chk.me/xgAjld6)           | <span style="color:red">Low priority</span>   |
| `mail`                       | Mail Services                             | <span style="color:red">Low priority</span>   |
| `newsletter`                 | Newsletter Overview                       | <span style="color:red">Low priority</span>   |
| `radio`                      | [Streaming Radio](https://chk.me/u4XqnUZ) | <span style="color:red">Low priority</span>   |
| `tickets`                    | Tickets Overview                          | <span style="color:red">Low priority</span>   |
| `url`                        | URL Overview                              | <span style="color:red">Low priority</span>   |
| `video`                      | [Streaming Video](https://chk.me/BWbluEg) | <span style="color:red">Low priority</span>   |
| `vod`                        | [VOD](https://chk.me/MRAj6ne)             | <span style="color:red">Low priority</span>   |
