import logging
from typing import List, Optional

import typer

_logger: logging.Logger = logging.getLogger(__name__)

app = typer.Typer()

if __name__ == "__main__":
    app()
