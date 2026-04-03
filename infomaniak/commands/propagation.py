"""DNS propagation checking via public resolvers."""

import socket
import sys

from infomaniak.api import api_request
from infomaniak.config import get_token
from infomaniak.output import bold, cyan, dim, green, output_json, print_table, red, yellow

# Public DNS resolvers to check
RESOLVERS = [
    ("Google", "8.8.8.8"),
    ("Google 2", "8.8.4.4"),
    ("Cloudflare", "1.1.1.1"),
    ("Quad9", "9.9.9.9"),
    ("OpenDNS", "208.67.222.222"),
]


def _resolve(domain, record_type, resolver_ip):
    """Resolve a DNS record using a specific resolver. Returns list of answers or error string."""
    try:
        import dns.resolver
        import dns.rdatatype
    except ImportError:
        return _resolve_fallback(domain, resolver_ip)

    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [resolver_ip]
        resolver.timeout = 5
        resolver.lifetime = 5
        answers = resolver.resolve(domain, record_type)
        return sorted([str(rdata) for rdata in answers])
    except dns.resolver.NXDOMAIN:
        return ["NXDOMAIN"]
    except dns.resolver.NoAnswer:
        return ["no answer"]
    except dns.resolver.NoNameservers:
        return ["no nameservers"]
    except Exception as e:
        return [f"error: {e}"]


def _resolve_fallback(domain, resolver_ip):
    """Fallback resolution using socket (A records only)."""
    try:
        results = socket.getaddrinfo(domain, None)
        ips = sorted(set(addr[4][0] for addr in results))
        return ips if ips else ["no results"]
    except socket.gaierror:
        return ["lookup failed"]


def cmd_dns_propagation(args):
    """Check DNS propagation across public resolvers."""
    domain = args.domain
    record_type = (args.type or "A").upper()

    # Build the full query name
    if args.name and args.name != "@":
        query_name = f"{args.name}.{domain}"
    else:
        query_name = domain

    print(f"\n  {bold(f'DNS Propagation: {record_type} {query_name}')}\n")

    results = []
    for resolver_name, resolver_ip in RESOLVERS:
        answers = _resolve(query_name, record_type, resolver_ip)
        answer_str = ", ".join(answers)
        results.append({
            "resolver": resolver_name,
            "ip": resolver_ip,
            "answers": answers,
            "answer_str": answer_str,
        })

    if getattr(args, "json", False):
        output_json(results)

    # Check if all resolvers agree
    all_answers = [r["answer_str"] for r in results]
    all_agree = len(set(all_answers)) == 1

    headers = ["Resolver", "IP", "Result"]
    rows = []
    for r in results:
        if all_agree:
            status = green(r["answer_str"])
        elif r["answer_str"] == all_answers[0]:
            status = green(r["answer_str"])
        else:
            status = yellow(r["answer_str"])

        rows.append([
            r["resolver"],
            dim(r["ip"]),
            status,
        ])

    print_table(headers, rows)

    if all_agree:
        print(f"\n  {green('All resolvers agree.')} DNS is fully propagated.\n")
    else:
        unique = len(set(all_answers))
        print(f"\n  {yellow(f'Inconsistent results ({unique} different answers).')} DNS may still be propagating.\n")
