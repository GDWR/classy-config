import sys
from abc import abstractmethod
from pathlib import Path
from typing import Any, MutableMapping

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol


class Parser(Protocol):
    """Protocol typing for a parsing function."""

    @abstractmethod
    def __call__(self, filepath: Path) -> MutableMapping[str, Any]:
        """Open a file, parse the contents, construct a dict & return it."""
