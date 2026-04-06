# Contributing

Thank you for contributing to the Infomaniak Python SDK.

## Branching model

This repository uses a simple two-branch workflow:

- `main`: production branch. Stable, release-ready code only.
- `dev`: development branch. Active integration branch for ongoing work.

### How to contribute

1. Start from `dev` and create a feature/fix branch.
2. Open a Pull Request targeting `dev`.
3. After validation and review, changes are merged into `dev`.
4. Production releases are promoted from `dev` to `main`.

## Codebase structure

The project is organized as follows:

- `infomaniak/`: main Python package.
  - `clients/`: API client implementations and base client logic.
  - `resources/`: API endpoint/resource groups (organized by product/domain).
  - `models/`: typed data models used by resources and clients.
  - `constants.py`, `pagination.py`, `resource.py`, `register.py`, `utils.py`: shared SDK utilities and core behaviors.
- `docs/`: documentation source files (VitePress-based site).
- `tests/`: test suite.
- `OpenApi.json`: API specification used as reference for SDK structure.
- `pyproject.toml`: package metadata, tooling, and dependency configuration.

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

Before committing, run:

```bash
isort .
```
