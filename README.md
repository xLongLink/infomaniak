# infomaniak-cli

CLI tool for managing your [Infomaniak](https://www.infomaniak.com) services from the terminal.

Currently supports **DNS management** — more features planned.

## Features

- List all domains on your account
- List, filter, and inspect DNS records
- Create, update, and delete records (A, AAAA, CNAME, MX, TXT, SRV, NS, etc.)
- Check if a record resolves correctly on Infomaniak's nameservers
- Auto-detects your account ID
- Simple `.env` or environment variable configuration

## Install

### With pipx (recommended)

```bash
pipx install infomaniak
```

### With pip

```bash
pip install infomaniak
```

### From source

```bash
git clone https://github.com/peaktwilight/infomaniak-cli.git
cd infomaniak-cli
pip install .
```

## Configuration

### 1. Get an API token

1. Go to [Infomaniak API tokens](https://manager.infomaniak.com/v3/infomaniak-api)
2. Create a new token with these scopes:
   - `domain:read`
   - `dns:read`
   - `dns:write`
3. Copy the token

### 2. Set the token

**Option A** — environment variable:

```bash
export INFOMANIAK_API_TOKEN=your-token-here
```

**Option B** — `.env` file:

```bash
cp .env.example .env
# Edit .env and paste your token
```

## Usage

```bash
# List all domains
infomaniak-cli domains

# List DNS records for a domain
infomaniak-cli records example.com

# Filter by record type
infomaniak-cli records example.com --type CNAME

# Check if a record resolves correctly
infomaniak-cli check example.com 12345

# Create a new record
infomaniak-cli add example.com A blog 93.184.216.34
infomaniak-cli add example.com CNAME app target.example.net --ttl 300

# Update a record
infomaniak-cli update example.com 12345 --target 93.184.216.35
infomaniak-cli update example.com 12345 --ttl 300

# Delete a record (with confirmation)
infomaniak-cli delete example.com 12345

# Delete without confirmation
infomaniak-cli delete example.com 12345 --yes

# Show version
infomaniak-cli --version
```

### Example output

```
$ infomaniak-cli domains

Domains (2):

  ID       Domain           DNSSEC  DNS@IK
  ───────  ───────────────  ──────  ──────
  100001   example.com      yes     yes
  100002   example.org      yes     yes

$ infomaniak-cli records example.com --type A

DNS records for example.com (type=A) — 2 records:

  ID      Type  Name  Target          TTL
  ──────  ────  ────  ──────────────  ────
  200001  A     @     93.184.216.34   3600
  200002  A     www   93.184.216.34   3600
```

## Why not OAuth?

Infomaniak's OAuth2 apps only support `openid`, `profile`, `email`, and `phone` scopes. The DNS management scopes (`domain:read`, `dns:read`, `dns:write`) are only available through API tokens — so there's no way to implement a browser-based login flow.

## API reference

Built on the [Infomaniak API](https://developer.infomaniak.com/docs/api):

| Endpoint | Description |
|---|---|
| `GET /1/domain/account/{id}` | List domains |
| `GET /2/zones/{zone}/records` | List DNS records |
| `POST /2/zones/{zone}/records` | Create record |
| `PUT /2/zones/{zone}/records/{id}` | Update record |
| `DELETE /2/zones/{zone}/records/{id}` | Delete record |
| `GET /2/zones/{zone}/records/{id}/check` | Check record health |

## License

MIT
