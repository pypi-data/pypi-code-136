"""class AODict."""
from __future__ import annotations

from typing import Any
from typing import Dict


class AODict(Dict[Any, Any]):
    """AODict class."""

    def __init__(self, d: dict[Any, Any] | None = None):
        """Create new AODict. If dict is given, convert it."""
        if d is not None:
            super().update(d)

    def __setitem__(self, k: Any, v: Any) -> None:
        """Lets you add item to dict, but not if key exists.

        If the item being added is of type Dict, then first
        convert it to an AODict before adding it.

        Args:
            k (Any): the key of attempted addition
            v (Any): the value
        """
        if k not in self.keys():
            if not isinstance(v, dict):
                super().__setitem__(k, v)
            else:
                ao_v: AODict = AODict(v)
                super().__setitem__(k, ao_v)
