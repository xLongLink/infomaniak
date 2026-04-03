"""Service status overview."""

from infomaniak.api import api_request_paginated
from infomaniak.config import get_account_id, get_token
from infomaniak.output import bold, cyan, dim, green, output_json, print_table, red, yellow


def cmd_status(args):
    """Show service status overview."""
    token = get_token()
    account_id = get_account_id(token)

    products = api_request_paginated(
        "/1/products", token,
        params={"account_id": account_id},
    )

    if getattr(args, "json", False):
        output_json(products)

    if not products:
        print(f"  {dim('No products found.')}")
        return

    # Group by service
    services = {}
    for p in products:
        svc = p.get("service_name", "unknown")
        if svc not in services:
            services[svc] = {"total": 0, "active": 0, "issues": []}
        services[svc]["total"] += 1

        name = p.get("customer_name", p.get("internal_name", "?"))
        if p.get("has_maintenance"):
            services[svc]["issues"].append((name, "maintenance"))
        elif p.get("is_locked"):
            services[svc]["issues"].append((name, "locked"))
        elif p.get("has_operation_in_progress"):
            services[svc]["issues"].append((name, "in progress"))
        else:
            services[svc]["active"] += 1

    print(f"\n  {bold(f'Service Status — {len(products)} products')}\n")

    headers = ["Service", "Total", "Active", "Issues"]
    rows = []
    for svc, info in sorted(services.items()):
        issue_count = len(info["issues"])
        if issue_count == 0:
            issues = green("none")
        else:
            issues = yellow(str(issue_count))
        rows.append([
            cyan(svc),
            info["total"],
            green(str(info["active"])),
            issues,
        ])
    print_table(headers, rows)

    # Show details for any issues
    all_issues = []
    for svc, info in sorted(services.items()):
        for name, issue_type in info["issues"]:
            all_issues.append((svc, name, issue_type))

    if all_issues:
        print(f"\n  {bold('Issues:')}\n")
        for svc, name, issue_type in all_issues:
            icon = yellow("⚠") if issue_type == "maintenance" else red("✗")
            print(f"    {icon} {cyan(svc)} / {name}: {yellow(issue_type)}")
    else:
        print(f"\n  {green('✓')} All services operational.\n")

    print()
