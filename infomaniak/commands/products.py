"""Products listing command."""

from infomaniak.api import api_request_paginated
from infomaniak.config import get_account_id, get_token
from infomaniak.output import bold, cyan, dim, green, output_json, print_table, red, yellow


def cmd_products(args):
    """List all products on the account."""
    token = get_token()
    account_id = get_account_id(token)

    params = {"account_id": account_id}
    if args.service_filter:
        params["service_name"] = args.service_filter

    products = api_request_paginated("/1/products", token, params=params)

    if getattr(args, "json", False):
        output_json(products)

    if not products:
        print(f"  {dim('No products found.')}")
        return

    headers = ["ID", "Service", "Name", "Status"]
    rows = []
    for p in products:
        if p.get("has_maintenance"):
            status = yellow("maintenance")
        elif p.get("is_locked"):
            status = red("locked")
        elif p.get("has_operation_in_progress"):
            status = yellow("in progress")
        else:
            status = green("active")

        rows.append([
            p.get("id", "?"),
            cyan(p.get("service_name", "?")),
            p.get("customer_name", p.get("internal_name", "?")),
            status,
        ])

    service_note = f" type={args.service_filter}" if args.service_filter else ""
    print(f"\n  {bold(f'Products ({len(rows)})')}{dim(service_note)}\n")
    print_table(headers, rows)
    print()
