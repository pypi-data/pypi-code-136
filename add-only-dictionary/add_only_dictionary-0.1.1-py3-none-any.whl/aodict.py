"""class AODict."""
from __future__ import annotations

from typing import Dict
from typing import TypeVar


K = TypeVar("K")
V = TypeVar("V")


class AODict(Dict[K, V]):
    """AODict class."""

    def __setitem__(self, k: K, v: V) -> None:
        """__setitem__."""
        super().__setitem__(k, v)
