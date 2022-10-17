"""class AODict."""
from __future__ import annotations

from typing import Any
from typing import Dict

from add_only_dictionary.aolist import AOList


class AODict(Dict[Any, Any]):
    """AODict class."""

    def __init__(self, d: dict[Any, Any] | None = None) -> None:
        """Create new AODict. If dict is given, convert it."""
        if d is not None:
            self.init_load(d)

    def init_load(self, d: dict[Any, Any]) -> None:
        """Insert each item from d into AODict.

        Args:
            d (dict[Any, Any]): dictionary to insert items from
        """
        for k in d:
            self.__setitem__(k, d[k])

    def __setitem__(self, k: Any, v: Any) -> None:
        """Lets you add item to dict, but not if key exists.

        If the item being added is of type Dict, then first
        convert it to an AODict before adding it.

        Args:
            k (Any): the key of attempted addition
            v (Any): the value
        """
        if k not in self.keys():
            if isinstance(v, dict):
                ao_d: AODict = AODict(v)
                super().__setitem__(k, ao_d)

            elif isinstance(v, list):
                ao_l: AOList = AOList(v)
                super().__setitem__(k, ao_l)

            else:
                super().__setitem__(k, v)

    def __delitem__(self, k: Any) -> None:
        """Override the __delitem__ method, and prevent it.

        Args:
            k (Any): the key that would normally be removed
        """
        pass
