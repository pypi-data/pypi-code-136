# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
import abc
from typing import Tuple, Any

from .. import _util


__all__ = ["Rules"]


class _Rule(abc.ABC):
    """_Rule is an abstract base to represent a rule. Functionality of a rule
    need to be implemented in the subclasses.
    """
    @abc.abstractmethod
    def __init__(self): # pragma: no cover
        pass

    @abc.abstractmethod
    def __eq__(self, other: object) -> bool:
        raise TypeError("subclasses of _Rule need to implement __eq__()")

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __bool__(self):
        raise ValueError("Rule can't be converted to 'bool'")

    @abc.abstractmethod
    def __hash__(self):
        raise TypeError("subclasses of _Rule need to implement __hash__()")


class Rules(_util.TypedList[_Rule]):
    @property
    def _elem_type_(self):
        return _Rule


class _Condition(_Rule):
    """_Condition is a _Rule subclass that represent a contraint on an object.

    _Condition is an abstract base class that needs to be subclassed.

    _Condition objects are immputable. For convenience the __init__() of this base class
    allows to specify the elements which make this object unique so the subclass does
    not need implement the __eq__() and __hash__() method. Objects of different
    subclasses from each other are considered unequal even if one is subclass of the
    other.
    """
    @abc.abstractmethod
    def __init__(self, *, elements: Tuple[Any, ...]):
        self._elements = elements

    def __hash__(self):
        return hash(self._elements)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, _Condition):
            return False
        else:
            return (
                (self.__class__ is other.__class__)
                and (self._elements == other._elements)
            )

    @abc.abstractmethod
    def __repr__(self): # pragma: no cover
        raise RuntimeError("_Condition subclass needs to implement __repr__() method")
