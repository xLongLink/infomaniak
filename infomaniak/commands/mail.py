"""Mail hosting commands."""

import sys

from infomaniak.api import api_request, api_request_paginated
from infomaniak.config import get_account_id, get_token
from infomaniak.output import bold, cyan, dim, green, output_json, print_table, red, yellow


def cmd_mail_list(args):
    """List mail hosting services."""
    token = get_token()
    account_id = get_account_id(token)

    products = api_request_paginated(
        "/1/products", token,
        params={"account_id": account_id, "service_name": "email_hosting"},
    )

    if getattr(args, "json", False):
        output_json(products)

    if not products:
        print(f"  {dim('No mail hostings found.')}")
        return

    headers = ["ID", "Domain", "Status"]
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
            p.get("customer_name", "?"),
            status,
        ])

    print(f"\n  {bold(f'Mail Hostings ({len(rows)})')}\n")
    print_table(headers, rows)
    print()


def cmd_mail_mailboxes(args):
    """List mailboxes for a mail hosting. Requires 'mail' scope."""
    token = get_token()
    mail_hosting_id = args.mail_hosting_id

    try:
        data = api_request("GET", f"/1/mail_hostings/{mail_hosting_id}/mailboxes", token)
    except SystemExit:
        print(f"\n  {yellow('Hint')}: This command requires the {bold('mail')} scope on your API token.")
        print(f"  Regenerate your token at https://manager.infomaniak.com/v3/infomaniak-api\n")
        sys.exit(1)

    mailboxes = data.get("data", [])

    if getattr(args, "json", False):
        output_json(mailboxes)

    if not mailboxes:
        print(f"  {dim('No mailboxes found.')}")
        return

    headers = ["Email", "Type"]
    rows = []
    for m in mailboxes:
        email = m.get("mailbox", m.get("mailbox_idn", "?"))
        mtype = m.get("type") or dim("standard")
        if m.get("is_free_mail"):
            mtype = dim("free")

        rows.append([email, mtype])

    print(f"\n  {bold(f'Mailboxes ({len(rows)})')}\n")
    print_table(headers, rows)
    print()
