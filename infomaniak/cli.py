"""CLI entry point built with Click."""

import argparse

import click

from infomaniak import __version__
from infomaniak.commands.account import cmd_account
from infomaniak.commands.audit import cmd_dns_audit
from infomaniak.commands.config import cmd_config_show
from infomaniak.commands.dns import (
    cmd_dns_add,
    cmd_dns_backup,
    cmd_dns_check,
    cmd_dns_clone,
    cmd_dns_delete,
    cmd_dns_diff,
    cmd_dns_domains,
    cmd_dns_export,
    cmd_dns_import,
    cmd_dns_records,
    cmd_dns_search,
    cmd_dns_sync,
    cmd_dns_update,
)
from infomaniak.commands.domains import cmd_domains
from infomaniak.commands.drive import cmd_drive_list
from infomaniak.commands.hosting import cmd_hosting_list
from infomaniak.commands.mail import cmd_mail_list, cmd_mail_mailboxes
from infomaniak.commands.products import cmd_products
from infomaniak.commands.propagation import cmd_dns_propagation
from infomaniak.commands.setup import cmd_setup
from infomaniak.commands.status import cmd_status
from infomaniak.commands.zone import cmd_dns_zone
from infomaniak.config import load_env_file
from infomaniak.output import bold


def _args(**kwargs):
    return argparse.Namespace(**kwargs)


def _invoke(handler, **kwargs):
    return handler(_args(**kwargs))


@click.group(
    invoke_without_command=True,
    help="Manage Infomaniak services from the command line.",
    epilog=f"Get started: {bold('infomaniak setup')}",
)
@click.version_option(__version__, "--version", "-V", prog_name="infomaniak", message="%(prog)s %(version)s")
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit(1)


@cli.command(help="Configure your API token")
def setup():
    _invoke(cmd_setup)


@cli.group(invoke_without_command=True, help="Manage DNS records and domains")
@click.pass_context
def dns(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit(1)


@dns.command("domains", help="List all domains on your account")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def dns_domains(as_json):
    _invoke(cmd_dns_domains, json=as_json)


@dns.command("records", help="List DNS records for a domain")
@click.argument("domain")
@click.option("--type", "record_type", "-t", help="Filter by record type (A, AAAA, CNAME, MX, TXT, etc.)")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def dns_records(domain, record_type, as_json):
    _invoke(cmd_dns_records, domain=domain, type=record_type, json=as_json)


@dns.command("check", help="Check if a DNS record resolves correctly")
@click.argument("domain")
@click.argument("record_id")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def dns_check(domain, record_id, as_json):
    _invoke(cmd_dns_check, domain=domain, record_id=record_id, json=as_json)


@dns.command("add", help="Create a DNS record")
@click.argument("domain")
@click.argument("record_type")
@click.argument("source")
@click.argument("target")
@click.option("--ttl", type=int, default=3600, show_default=True, help="TTL in seconds")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def dns_add(domain, record_type, source, target, ttl, as_json):
    _invoke(cmd_dns_add, domain=domain, type=record_type, source=source, target=target, ttl=ttl, json=as_json)


@dns.command("update", help="Update a DNS record")
@click.argument("domain")
@click.argument("record_id")
@click.option("--target", help="New target value")
@click.option("--ttl", type=int, help="New TTL in seconds")
def dns_update(domain, record_id, target, ttl):
    _invoke(cmd_dns_update, domain=domain, record_id=record_id, target=target, ttl=ttl)


@dns.command("delete", help="Delete a DNS record")
@click.argument("domain")
@click.argument("record_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation")
def dns_delete(domain, record_id, yes):
    _invoke(cmd_dns_delete, domain=domain, record_id=record_id, yes=yes)


@dns.command("export", help="Export DNS records as JSON or CSV")
@click.argument("domain")
@click.option("--format", "export_format", "-f", type=click.Choice(["json", "csv"]), default="json", show_default=True, help="Output format")
@click.option("--output", "-o", help="Output file path (default: stdout)")
def dns_export(domain, export_format, output):
    _invoke(cmd_dns_export, domain=domain, format=export_format, output=output)


@dns.command("import", help="Import DNS records from JSON or CSV file")
@click.argument("domain")
@click.argument("file")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation")
def dns_import(domain, file, yes):
    _invoke(cmd_dns_import, domain=domain, file=file, yes=yes)


@dns.command("diff", help="Compare live DNS records against a local file")
@click.argument("domain")
@click.argument("file")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def dns_diff(domain, file, as_json):
    _invoke(cmd_dns_diff, domain=domain, file=file, json=as_json)


@dns.command("clone", help="Clone DNS records from one domain to another")
@click.argument("source_domain")
@click.argument("target_domain")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation")
def dns_clone(source_domain, target_domain, yes):
    _invoke(cmd_dns_clone, source_domain=source_domain, target_domain=target_domain, yes=yes)


@dns.command("search", help="Search DNS records across all domains")
@click.argument("query")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def dns_search(query, as_json):
    _invoke(cmd_dns_search, query=query, json=as_json)


@dns.command("backup", help="Backup DNS records for all domains")
@click.option("--output", "-o", default="dns-backup", show_default=True, help="Output directory")
@click.option("--format", "backup_format", "-f", type=click.Choice(["json", "csv"]), default="json", show_default=True, help="Output format")
def dns_backup(output, backup_format):
    _invoke(cmd_dns_backup, output=output, format=backup_format)


@dns.command("sync", help="Sync DNS records from file to live (like terraform apply)")
@click.argument("domain")
@click.argument("file")
@click.option("--dry-run", is_flag=True, help="Show plan without applying changes")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation")
def dns_sync(domain, file, dry_run, yes):
    _invoke(cmd_dns_sync, domain=domain, file=file, dry_run=dry_run, yes=yes)


@dns.command("audit", help="Audit DNS for misconfigurations (SPF, DMARC, DKIM, etc.)")
@click.argument("domain", required=False)
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def dns_audit(domain, as_json):
    _invoke(cmd_dns_audit, domain=domain, json=as_json)


@dns.command("zone", help="Generate BIND-format zone file")
@click.argument("domain")
@click.option("--output", "-o", help="Output file path (default: stdout)")
def dns_zone(domain, output):
    _invoke(cmd_dns_zone, domain=domain, output=output)


@dns.command("propagation", help="Check DNS propagation across public resolvers")
@click.argument("domain")
@click.option("--name", "record_name", "-n", default="@", show_default=True, help="Record name")
@click.option("--type", "record_type", "-t", default="A", show_default=True, help="Record type")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def dns_propagation(domain, record_name, record_type, as_json):
    _invoke(cmd_dns_propagation, domain=domain, name=record_name, type=record_type, json=as_json)


@cli.command(help="List domains with expiry tracking")
@click.option("--warn", type=int, default=30, show_default=True, help="Warn if expiring within N days")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def domains(warn, as_json):
    _invoke(cmd_domains, warn=warn, json=as_json)


@cli.group(invoke_without_command=True, help="View configuration")
@click.pass_context
def config(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit(1)


@config.command("show", help="Show current configuration")
def config_show():
    _invoke(cmd_config_show)


@cli.command(help="Show account overview")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def account(as_json):
    _invoke(cmd_account, json=as_json)


@cli.command(help="List all products on your account")
@click.option("--type", "service_filter", "-t", help="Filter by service type (e.g. domain, email_hosting)")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def products(service_filter, as_json):
    _invoke(cmd_products, service_filter=service_filter, json=as_json)


@cli.group(invoke_without_command=True, help="Manage web hosting services")
@click.pass_context
def hosting(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit(1)


@hosting.command("list", help="List web hosting services")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def hosting_list(as_json):
    _invoke(cmd_hosting_list, json=as_json)


@cli.group(invoke_without_command=True, help="Manage kDrive instances")
@click.pass_context
def drive(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit(1)


@drive.command("list", help="List kDrive instances")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def drive_list(as_json):
    _invoke(cmd_drive_list, json=as_json)


@cli.group(invoke_without_command=True, help="Manage mail services")
@click.pass_context
def mail(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit(1)


@mail.command("list", help="List mail hosting services")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def mail_list(as_json):
    _invoke(cmd_mail_list, json=as_json)


@mail.command("mailboxes", help="List mailboxes (requires 'mail' scope)")
@click.argument("mail_hosting_id")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def mail_mailboxes(mail_hosting_id, as_json):
    _invoke(cmd_mail_mailboxes, mail_hosting_id=mail_hosting_id, json=as_json)


@cli.command(help="Service status overview")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def status(as_json):
    _invoke(cmd_status, json=as_json)


def main():
    load_env_file()
    cli(prog_name="infomaniak")
