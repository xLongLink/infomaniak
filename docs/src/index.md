# Overview

Welcome to the Infomaniak SDK for Python documentation.

This documentation mirrors the SDK resource layout so you can navigate API domains the same way you use the client.

## Structure

The SDK documentation mirrors the resource tree in `infomaniak/resources`.

- `core/` contains shared endpoints for profile, locale, events, and user-related resources.
- `kmeet/` contains conference-planning and room-related resources.

Use the navigation sidebar to explore the available resources and their models.

## Quick start

```py
from infomaniak import Client

client = Client(token="<token>")

profile = client.core.profile.get_current_profile()
```
