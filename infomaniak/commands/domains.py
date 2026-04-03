"""Domain overview with expiry tracking."""

from datetime import datetime, timezone

from infomaniak.api import api_request_paginated
from infomaniak.config import get_account_id, get_token
from infomaniak.output import bold, cyan, dim, green, output_json, print_table, red, yellow


def cmd_domains(args):
    """List all domains with registration and expiry info."""
    token = get_token()
    account_id = get_account_id(token)

    products = api_request_paginated(
        "/1/products", token,
        params={"account_id": account_id, "service_name": "domain"},
    )

    if getattr(args, "json", False):
        output_json(products)

    if not products:
        print(f"  {dim('No domains found.')}")
        return

    now = datetime.now(timezone.utc)
    warn_days = args.warn or 30

    headers = ["Domain", "Expires", "Days Left", "Status"]
    rows = []
    expiring_soon = []

    for p in products:
        name = p.get("customer_name", "?")
        expired_at = p.get("expired_at")

        if expired_at:
            try:
                exp_date = datetime.fromtimestamp(int(expired_at), tz=timezone.utc)
                days_left = (exp_date - now).days
                exp_display = exp_date.strftime("%Y-%m-%d")

                if days_left < 0:
                    days_display = red(f"EXPIRED ({abs(days_left)}d ago)")
                    status = red("expired")
                    expiring_soon.append((name, days_left))
                elif days_left <= warn_days:
                    days_display = yellow(str(days_left))
                    status = yellow("expiring")
                    expiring_soon.append((name, days_left))
                else:
                    days_display = green(str(days_left))
                    status = green("active")
            except (ValueError, TypeError):
                exp_display = dim("unknown")
                days_display = dim("?")
                status = dim("unknown")
        else:
            exp_display = dim("n/a")
            days_display = dim("n/a")
            status = green("active")

        rows.append([name, exp_display, days_display, status])

    # Sort by days left (soonest first)
    rows.sort(key=lambda r: r[1])

    print(f"\n  {bold(f'Domains ({len(rows)})')}\n")
    print_table(headers, rows)

    if expiring_soon:
        print(f"\n  {yellow(f'Warning: {len(expiring_soon)} domain(s) expiring within {warn_days} days:')}\n")
        for name, days in sorted(expiring_soon, key=lambda x: x[1]):
            if days < 0:
                print(f"    {red('!')} {bold(name)} — expired {abs(days)} days ago")
            else:
                print(f"    {yellow('!')} {bold(name)} — {days} days remaining")

    print()
