"""class AODict."""
from __future__ import annotations

from typing import Any
from typing import List


try:
    from typing_extensions import SupportsIndex
except ImportError:
    from typing import SupportsIndex


class AOList(List[Any]):
    """AOList class."""

    def __init__(self, initial_list: list[Any] | None = None):
        """Create new AOList. If list is given, convert it."""
        if initial_list is not None:
            super().extend(initial_list)

    def __delitem__(self, key: Any) -> None:
        """No op on AOList."""
        pass

    def remove(self, item: Any) -> None:
        """No op on AOList."""
        pass

    def pop(self, idx: SupportsIndex = ...) -> Any:
        """No op on AOList."""
        pass

    def clear(self) -> None:
        """No op on AOList."""
        pass
