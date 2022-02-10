import sys
from pathlib import Path

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol


class Parser(Protocol):
    """Protocol typing for a parsing function."""

    def __call__(self, filepath: Path) -> dict:
        """Open a file, parse the contents, construct a dict & return it."""
