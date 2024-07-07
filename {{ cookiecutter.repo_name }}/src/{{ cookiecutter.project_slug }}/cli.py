import logging
from typing import List, Optional

import click

_logger: logging.Logger = logging.getLogger(__name__)


@click.group()
def cli() -> None:
    """CLI interface"""
    pass


if __name__ == "__main__":
    cli()
