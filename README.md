<div align="center">

# Infomaniak Python SDK

[![PyPI version](https://img.shields.io/pypi/v/xinfomaniak)](https://pypi.org/project/xinfomaniak/)
[![Tests](https://github.com/XLongLink/infomaniak/actions/workflows/test.yml/badge.svg)](https://github.com/XLongLink/infomaniak/actions/workflows/test.yml)
[![Python versions](https://img.shields.io/pypi/pyversions/xinfomaniak)](https://pypi.org/project/xinfomaniak/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[Documentation](https://xlonglink.github.io/infomaniak/) &nbsp; - &nbsp; [Get the Token](https://manager.infomaniak.com/v3/infomaniak-api) &nbsp; - &nbsp; [API Reference](https://developer.infomaniak.com/)

</div>

<br />
<br />

> [!CAUTION]
> Currently in development.

```bash
pip install xinfomaniak
```

<br />

## Goals

- Provide a simple and intuitive interface to interact with the Infomaniak API.
- Support both synchronous and asynchronous programming paradigms.
- Type annotations for better developer experience and code quality.

<br />

## Usage

```python
from infomaniak import Client

client = Client(token="your-token")
```

### Async client example

```python
import asyncio
from infomaniak import AsyncClient

async def main() -> None:
    client = AsyncClient(token="your-token")
    await client.domain.list()

asyncio.run(main())
```
