"""
infomaniak — CLI for managing Infomaniak services.

Usage:
    infomaniak setup                                         # Configure your API token
    infomaniak account                                       # Account overview
    infomaniak dns domains                                   # List all domains
    infomaniak dns records <domain>                          # List DNS records
    infomaniak dns add <domain> <type> <source> <target>     # Create record
    infomaniak dns update <domain> <record_id> --target X    # Update record
    infomaniak dns delete <domain> <record_id>               # Delete record
    infomaniak dns export <domain>                           # Export records
    infomaniak dns import <domain> <file>                    # Import records
    infomaniak dns diff <domain> <file>                      # Compare live vs file
    infomaniak dns sync <domain> <file>                      # Sync live to match file
    infomaniak dns clone <source> <target>                   # Clone between domains
    infomaniak dns search <query>                            # Search all domains
    infomaniak dns backup                                    # Backup all domains
    infomaniak products [--type <name>]                      # List all products
    infomaniak hosting list                                  # List web hostings
    infomaniak drive list                                    # List kDrive instances
    infomaniak mail list                                     # List mail hostings
    infomaniak mail mailboxes <id>                           # List mailboxes
    infomaniak status                                        # Service status
    infomaniak config show                                   # Show configuration
"""

__version__ = "0.7.0"
API_BASE = "https://api.infomaniak.com"
