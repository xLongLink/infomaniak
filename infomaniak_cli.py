#!/usr/bin/env python3
"""
infomaniak-cli — CLI tool for managing DNS records via the Infomaniak API.

Usage:
    infomaniak-cli domains                                   # List all domains
    infomaniak-cli records <domain>                          # List DNS records
    infomaniak-cli check <domain> <record_id>                # Check record health
    infomaniak-cli add <domain> <type> <source> <target>     # Create record
    infomaniak-cli update <domain> <record_id> --target X    # Update record
    infomaniak-cli delete <domain> <record_id>               # Delete record

Configuration:
    Set INFOMANIAK_API_TOKEN as an environment variable or in a .env file.
    Get your token at: https://manager.infomaniak.com/v3/infomaniak-api
    Required scopes: domain:read, dns:read, dns:write
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: 'requests' is required. Install it with: pip install requests")
    sys.exit(1)


__version__ = "0.1.0"
API_BASE = "https://api.infomaniak.com"


# ── Config & Auth ─────────────────────────────────────────────────────────────


def load_env_file():
    """Load variables from .env file if it exists."""
    for env_path in [Path(".env"), Path(__file__).parent / ".env"]:
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, _, value = line.partition("=")
                        key = key.strip()
                        value = value.strip().strip("'\"")
                        if key and key not in os.environ:
                            os.environ[key] = value


def get_token():
    """Get API token from env or .env file."""
    token = os.environ.get("INFOMANIAK_API_TOKEN")
    if token:
        return token

    print("Error: INFOMANIAK_API_TOKEN is not set.\n")
    print("Setup:")
    print("  1. Go to https://manager.infomaniak.com/v3/infomaniak-api")
    print("  2. Create a token with scopes: domain:read, dns:read, dns:write")
    print("  3. Copy .env.example to .env and paste your token")
    sys.exit(1)


def get_account_id(token):
    """Get account ID from env or auto-discover it."""
    account_id = os.environ.get("INFOMANIAK_ACCOUNT_ID")
    if account_id:
        return account_id

    data = api_request("GET", "/1/accounts", token)
    accounts = data.get("data", [])
    if not accounts:
        print("Error: No accounts found for this token.")
        sys.exit(1)
    if len(accounts) == 1:
        return accounts[0]["id"]

    print("Multiple accounts found:\n")
    for i, acc in enumerate(accounts):
        print(f"  [{i+1}] {acc['name']} (ID: {acc['id']})")
    print()
    choice = input(f"Select account [1-{len(accounts)}]: ")
    try:
        idx = int(choice) - 1
        return accounts[idx]["id"]
    except (ValueError, IndexError):
        print("Invalid choice.")
        sys.exit(1)


def api_request(method, path, token, params=None, json_data=None):
    """Make an authenticated request to the Infomaniak API."""
    url = f"{API_BASE}{path}"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    resp = requests.request(
        method, url, headers=headers, params=params, json=json_data, timeout=30
    )

    if resp.status_code == 204:
        return {"result": "success", "data": None}

    try:
        data = resp.json()
    except ValueError:
        print(f"Error: Non-JSON response (HTTP {resp.status_code})")
        print(resp.text[:500])
        sys.exit(1)

    if data.get("result") == "error":
        err = data.get("error", {})
        code = err.get("code", "unknown")
        desc = err.get("description", resp.text[:200])
        print(f"API Error [{code}]: {desc}")
        sys.exit(1)

    if resp.status_code >= 400:
        print(f"HTTP Error {resp.status_code}: {resp.text[:300]}")
        sys.exit(1)

    return data


# ── Table formatting ──────────────────────────────────────────────────────────


def print_table(headers, rows):
    """Print a simple aligned table."""
    if not rows:
        print("  (no results)")
        return

    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    header_line = "  ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    separator = "  ".join("─" * col_widths[i] for i in range(len(headers)))
    print(f"  {header_line}")
    print(f"  {separator}")

    for row in rows:
        line = "  ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))
        print(f"  {line}")


# ── Commands ──────────────────────────────────────────────────────────────────


def cmd_domains(args):
    """List all domains on the account."""
    token = get_token()
    account_id = get_account_id(token)

    data = api_request("GET", f"/1/domain/account/{account_id}", token)
    domains = data.get("data", [])

    if not domains:
        print("No domains found.")
        return

    headers = ["ID", "Domain", "DNSSEC", "DNS@IK"]
    rows = []
    for d in domains:
        rows.append([
            d.get("id", "?"),
            d.get("customer_name", "?"),
            "yes" if d.get("has_dnssec") else "no",
            "yes" if d.get("is_dns_managed_by_infomaniak") else "no",
        ])

    print(f"\nDomains ({len(rows)}):\n")
    print_table(headers, rows)


def cmd_records(args):
    """List DNS records for a domain."""
    token = get_token()
    domain = args.domain

    data = api_request("GET", f"/2/zones/{domain}/records", token)
    records = data.get("data", [])

    if not records:
        print(f"No DNS records found for {domain}.")
        return

    if args.type:
        filter_type = args.type.upper()
        records = [r for r in records if r.get("type") == filter_type]

    records.sort(key=lambda r: (r.get("type", ""), r.get("source", "")))

    headers = ["ID", "Type", "Name", "Target", "TTL"]
    rows = []
    for r in records:
        source = r.get("source", "@")
        if source == ".":
            source = "@"
        target = r.get("target", "?")
        if len(str(target)) > 60:
            target = str(target)[:57] + "..."
        rows.append([
            r.get("id", "?"),
            r.get("type", "?"),
            source,
            target,
            r.get("ttl", "?"),
        ])

    type_note = f" (type={args.type.upper()})" if args.type else ""
    print(f"\nDNS records for {domain}{type_note} — {len(rows)} records:\n")
    print_table(headers, rows)


def cmd_check(args):
    """Check if a DNS record resolves correctly."""
    token = get_token()
    data = api_request("GET", f"/2/zones/{args.domain}/records/{args.record_id}/check", token)
    result = data.get("data", {})
    print(f"\nDNS check for record {args.record_id} in {args.domain}:\n")
    print(json.dumps(result, indent=2))


def cmd_add(args):
    """Create a new DNS record."""
    token = get_token()

    source = args.source
    if source == "@":
        source = ""

    body = {
        "type": args.type.upper(),
        "source": source,
        "target": args.target,
        "ttl": args.ttl,
    }

    display_name = args.source if args.source != "@" else args.domain
    print(f"Creating {body['type']} record: {display_name}.{args.domain} -> {body['target']} (TTL: {body['ttl']})")
    data = api_request("POST", f"/2/zones/{args.domain}/records", token, json_data=body)

    record = data.get("data", {})
    print(f"  Created record ID: {record.get('id')}")


def cmd_update(args):
    """Update an existing DNS record."""
    token = get_token()

    body = {}
    if args.target:
        body["target"] = args.target
    if args.ttl:
        body["ttl"] = args.ttl

    if not body:
        print("Error: Specify at least one of --target or --ttl to update.")
        sys.exit(1)

    print(f"Updating record {args.record_id} in {args.domain}: {body}")
    api_request("PUT", f"/2/zones/{args.domain}/records/{args.record_id}", token, json_data=body)
    print(f"  Record {args.record_id} updated.")


def cmd_delete(args):
    """Delete a DNS record."""
    token = get_token()

    if not args.yes:
        data = api_request("GET", f"/2/zones/{args.domain}/records", token)
        records = data.get("data", [])
        target_rec = next((r for r in records if str(r.get("id")) == str(args.record_id)), None)
        if target_rec:
            source = target_rec.get("source", "@")
            if source == ".":
                source = "@"
            print(f"  Record: {target_rec.get('type')} {source} -> {target_rec.get('target')}")

        confirm = input(f"Delete record {args.record_id} from {args.domain}? [y/N] ")
        if confirm.lower() not in ("y", "yes"):
            print("Aborted.")
            return

    api_request("DELETE", f"/2/zones/{args.domain}/records/{args.record_id}", token)
    print(f"  Record {args.record_id} deleted from {args.domain}.")


# ── CLI setup ─────────────────────────────────────────────────────────────────


def main():
    load_env_file()

    parser = argparse.ArgumentParser(
        prog="infomaniak-cli",
        description="Manage Infomaniak services from the command line.",
        epilog="Token setup: https://manager.infomaniak.com/v3/infomaniak-api",
    )
    parser.add_argument("--version", "-V", action="version", version=f"%(prog)s {__version__}")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # domains
    sp_domains = subparsers.add_parser("domains", help="List all domains on your account")
    sp_domains.set_defaults(func=cmd_domains)

    # records
    sp_records = subparsers.add_parser("records", help="List DNS records for a domain")
    sp_records.add_argument("domain", help="Domain name (e.g. example.com)")
    sp_records.add_argument("--type", "-t", help="Filter by record type (A, AAAA, CNAME, MX, TXT, etc.)")
    sp_records.set_defaults(func=cmd_records)

    # check
    sp_check = subparsers.add_parser("check", help="Check if a DNS record resolves correctly")
    sp_check.add_argument("domain", help="Domain name")
    sp_check.add_argument("record_id", help="Record ID to check")
    sp_check.set_defaults(func=cmd_check)

    # add
    sp_add = subparsers.add_parser("add", help="Create a DNS record")
    sp_add.add_argument("domain", help="Domain name (e.g. example.com)")
    sp_add.add_argument("type", help="Record type (A, AAAA, CNAME, MX, TXT, SRV, NS)")
    sp_add.add_argument("source", help="Record name (e.g. 'www', 'api', '@' for root)")
    sp_add.add_argument("target", help="Record value (e.g. IP address, hostname)")
    sp_add.add_argument("--ttl", type=int, default=3600, help="TTL in seconds (default: 3600)")
    sp_add.set_defaults(func=cmd_add)

    # update
    sp_update = subparsers.add_parser("update", help="Update a DNS record")
    sp_update.add_argument("domain", help="Domain name")
    sp_update.add_argument("record_id", help="Record ID to update")
    sp_update.add_argument("--target", help="New target value")
    sp_update.add_argument("--ttl", type=int, help="New TTL in seconds")
    sp_update.set_defaults(func=cmd_update)

    # delete
    sp_delete = subparsers.add_parser("delete", help="Delete a DNS record")
    sp_delete.add_argument("domain", help="Domain name")
    sp_delete.add_argument("record_id", help="Record ID to delete")
    sp_delete.add_argument("--yes", "-y", action="store_true", help="Skip confirmation")
    sp_delete.set_defaults(func=cmd_delete)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
