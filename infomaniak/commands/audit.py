"""DNS audit — scan domains for common misconfigurations."""

import sys

from infomaniak.api import api_request
from infomaniak.config import get_account_id, get_token
from infomaniak.output import bold, cyan, dim, green, output_json, red, yellow


def _has_record(records, rtype, source=None, substring=None):
    """Check if records contain a specific type/source/substring match."""
    for r in records:
        if r.get("type") != rtype:
            continue
        if source is not None:
            rec_source = r.get("source", "@")
            if rec_source == ".":
                rec_source = "@"
            if rec_source != source:
                continue
        if substring is not None and substring.lower() not in r.get("target", "").lower():
            continue
        return True
    return False


def _get_targets(records, rtype, source=None):
    """Get all targets for a given type/source."""
    targets = []
    for r in records:
        if r.get("type") != rtype:
            continue
        if source is not None:
            rec_source = r.get("source", "@")
            if rec_source == ".":
                rec_source = "@"
            if rec_source != source:
                continue
        targets.append(r.get("target", ""))
    return targets


def cmd_dns_audit(args):
    """Audit DNS records across all domains for common issues."""
    token = get_token()
    account_id = get_account_id(token)

    # Get all domains
    data = api_request("GET", f"/1/domain/account/{account_id}", token)
    domains = data.get("data", [])

    if not domains:
        print(f"  {dim('No domains found.')}")
        return

    domain_filter = args.domain if hasattr(args, "domain") and args.domain else None
    if domain_filter:
        domains = [d for d in domains if d.get("customer_name") == domain_filter]
        if not domains:
            print(f"  {red('Domain not found:')} {domain_filter}")
            sys.exit(1)

    all_issues = []
    all_results = []
    total_checked = 0

    print(f"\n  {bold('DNS Audit')}")
    print(f"  {dim('────────')}\n")
    print(f"  Scanning {len(domains)} domain(s)...\n")

    for d in domains:
        domain_name = d.get("customer_name", "")
        try:
            rdata = api_request("GET", f"/2/zones/{domain_name}/records", token)
        except SystemExit:
            continue

        records = rdata.get("data", [])
        total_checked += 1
        domain_issues = []

        # Check 1: SPF record
        spf_targets = _get_targets(records, "TXT", "@")
        has_spf = any("v=spf1" in t.lower() for t in spf_targets)
        if not has_spf:
            domain_issues.append(("missing_spf", "No SPF record found", "Email spoofing protection"))

        # Check 2: DMARC record
        dmarc_sources = [r.get("source", "@") for r in records if r.get("type") == "TXT"]
        has_dmarc = _has_record(records, "TXT", "_dmarc")
        if not has_dmarc:
            domain_issues.append(("missing_dmarc", "No DMARC record found", "Email authentication policy"))

        # Check 3: DKIM (check common selectors)
        has_dkim = False
        for r in records:
            source = r.get("source", "")
            if r.get("type") == "TXT" and "._domainkey" in source:
                has_dkim = True
                break
            if r.get("type") == "CNAME" and "._domainkey" in source:
                has_dkim = True
                break
        if not has_dkim:
            domain_issues.append(("missing_dkim", "No DKIM record found", "Email signing verification"))

        # Check 4: MX record (if domain has mail hosting)
        has_mx = _has_record(records, "MX")
        a_targets = _get_targets(records, "A", "@")
        if not has_mx and a_targets:
            domain_issues.append(("missing_mx", "No MX record — mail won't be delivered", "Mail delivery"))

        # Check 5: Multiple SPF records (invalid per RFC)
        spf_count = sum(1 for t in spf_targets if "v=spf1" in t.lower())
        if spf_count > 1:
            domain_issues.append(("multiple_spf", f"Multiple SPF records found ({spf_count})", "RFC violation — only one SPF allowed"))

        # Check 6: Low TTL on root records
        for r in records:
            source = r.get("source", "@")
            if source in ("@", ".") and r.get("type") in ("A", "AAAA", "MX"):
                ttl = r.get("ttl", 3600)
                if ttl < 60:
                    domain_issues.append(("low_ttl", f"Very low TTL ({ttl}s) on {r.get('type')} record", "May cause excessive DNS queries"))
                    break

        # Check 7: CNAME at root (invalid per RFC)
        has_root_cname = _has_record(records, "CNAME", "@")
        if has_root_cname:
            domain_issues.append(("root_cname", "CNAME record at root (@)", "RFC violation — may break MX/NS"))

        result = {
            "domain": domain_name,
            "records": len(records),
            "issues": domain_issues,
        }
        all_results.append(result)

        if domain_issues:
            all_issues.extend([(domain_name, *issue) for issue in domain_issues])

    if getattr(args, "json", False):
        output_json(all_results)

    # Summary
    clean = sum(1 for r in all_results if not r["issues"])
    with_issues = sum(1 for r in all_results if r["issues"])

    if all_issues:
        # Group by issue type
        issue_types = {}
        for domain_name, code, desc, hint in all_issues:
            if code not in issue_types:
                issue_types[code] = []
            issue_types[code].append((domain_name, desc, hint))

        for code, issues in sorted(issue_types.items()):
            hint = issues[0][2]
            desc = issues[0][1]
            print(f"  {yellow('!')} {bold(desc)} {dim(f'— {hint}')}")
            for domain_name, _, _ in issues:
                print(f"    {dim('→')} {domain_name}")
            print()

    print(f"  {bold('Summary')}: {total_checked} domains scanned")
    if clean:
        print(f"    {green(str(clean))} clean")
    if with_issues:
        print(f"    {yellow(str(with_issues))} with issues ({len(all_issues)} total findings)")
    if not all_issues:
        print(f"    {green('All domains passed all checks.')}")
    print()
