import sys
from abc import abstractmethod
from pathlib import Path
from typing import Any, MutableMapping

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol


class Loader(Protocol):
    """Protocol typing for a loading function."""

    @abstractmethod
    def __call__(self, filepath: Path) -> MutableMapping[str, Any]:
        """Open a file & load the contents in a dict."""
