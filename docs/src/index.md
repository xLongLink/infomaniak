# Overview

```bash
pip install xinfomaniak
```

## Goals

- Provide a simple and intuitive interface to interact with the Infomaniak API.
- Support both synchronous and asynchronous programming paradigms.
- Type annotations for better developer experience and code quality.


## Usage

The SDK supports two clients a `synchronous` and a `asynchronous`

```python
from infomaniak import Client

client = Client()
```


```python
import asyncio
from infomaniak import AsyncClient

async def main() -> None:
    client = AsyncClient()
    await client.domain.list()

asyncio.run(main())
```

If the `INFOMANIAK_API_TOKEN` environment variable is set, the token is automatically parsed


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
