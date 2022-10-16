"""class AODict."""
from __future__ import annotations

from typing import Dict
from typing import TypeVar


K = TypeVar("K")
V = TypeVar("V")


class AODict(Dict[K, V]):
    """AODict class."""

    def __setitem__(self, k: K, v: V) -> None:
        """Lets you add item to dict, but not if key exists.

        Args:
            k (K): the key of attempted addition
            v (V): the value
        """
        if k not in self.keys():
            super().__setitem__(k, v)
