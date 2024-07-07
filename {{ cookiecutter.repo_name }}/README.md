# {{ cookiecutter.repo_name }}

[![Python](https://img.shields.io/badge/python-3.11+-informational.svg)](https://www.python.org)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org)
[![documentation formatter: docformatter](https://img.shields.io/badge/%20formatter-docformatter-fedcba.svg)](https://github.com/PyCQA/docformatter)
[![documentation style: google](https://img.shields.io/badge/%20style-google-3666d6.svg)](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://mkdocstrings.github.io)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Hydra](https://img.shields.io/badge/Config-Hydra-89b8cd)](https://hydra.cc)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](https://commitizen-tools.github.io/commitizen/)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-brightgreen.svg)](https://conventionalcommits.org)

{{ cookiecutter.description}}

{{ cookiecutter.project_name }} follows semantic versioning in its version
number. This means that any 1.x release will be backwards compatible with an
earlier 1.y release. By "backward compatible", we mean that correct code that
works on a 1.y version will work on a future 1.x version.

## Overview

This project is comprised of the following languages and libraries:

- Language: Python 3.10+
- Package management: `Poetry`
- Web framework: `FastAPI`
- Production web server: `Uvicorn`
- Relational database: `Postgres`, `MongoDB`
- Relational database async support: [`databases`](https://www.encode.io/databases/), [`motor`](https://github.com/mongodb/motor)
- Relational database migrations: `Alembic`
- Relational ORM: `SQLAlchemy`, `SQLModel`
- Formatter: `ruff`, `isort`
- Linter: `ruff`
- Static type checker: `Mypy`
- Testing: `Pytest`

## Documentation

The documentation is automatically generated from the content of the
[`docs`](docs) directory and from the docstrings of the public signatures of
the source code.

## Development

See the [Developer](docs/DEVELOPER.md) guidelines for more information.

## Contributing

Contributions of any kind are welcome. Please read
[CONTRIBUTING.md](docs/CONTRIBUTING.md) for details and the process for
submitting pull requests to us.

## Changelog

See the [Changelog](CHANGELOG.md) for more information.

## Security

Thank you for improving the security of the project, please see the
[Security Policy](docs/SECURITY.md) for more information.