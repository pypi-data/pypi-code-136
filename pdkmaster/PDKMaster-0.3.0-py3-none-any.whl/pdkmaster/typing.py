# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
from typing import Generic, Iterable, Tuple, Dict, Optional, Union, TypeVar, cast

"""This is a module for typing support for PDKMaster.

Type aliases:
    MultiT: generic type to represent singleton or an iterable of a certain type.
    OptMultiT: generic type to represent None, singleton or an iterable of a certain type.
"""

T = TypeVar("T")
MultiT = Union[T, Iterable[T]]
OptMultiT = Optional[MultiT[T]]

def cast_MultiT(vs: MultiT[T]) -> Tuple[T, ...]:
    """cast a MultiT[T] object to tuple[T, ...].

    contrary to `typing.cast` this function is not pure type annotation but actually
    generated the tuple object that is returned.
    """
    try:
        iter(vs) # type: ignore
    except TypeError:
        return (cast(T, vs),)
    else:
        if isinstance(vs, str):
            return (cast(T, vs),)
        else:
            return tuple(cast(Iterable[T], vs))

def cast_OptMultiT(vs: OptMultiT[T]) -> Optional[Tuple[T, ...]]:
    """cast a MultiT[T] object to tuple[T, ...].

    contrary to `typing.cast` this function is not pure type annotation but actually
    generated the tuple object that is returned.
    """
    if vs is None:
        return None
    else:
        return cast_MultiT(vs)


# TODO: replace SingleOrMulti with MultiT
class SingleOrMulti(Generic[T]): # pragma: no cover
    """Type to represent a single value or an iterable of a value of
    a given type.

    Example:
        `SingleOrMulti[int].T` == `Union[int, Interable[int]]`

    API Notes:
        This class is deprecated and is planned to be removed before v1.0.0
    """
    # TODO: Investigate if we have solution not needing ignore type error
    T = Union[T, Iterable[T]] # type: ignore

    @staticmethod
    def cast(obj: "SingleOrMulti[T].T") -> Tuple[T, ...]:
        if _util.is_iterable(obj):
            return tuple(cast(Iterable[T], obj))
        else:
            return (cast(T, obj),)


# TODO: replace OptSingleOrMulti with OptMultiT
class OptSingleOrMulti(Generic[T]): # pragma: no cover
    """`OptSingleOrMulti[T].T` == `Optional[SingleOrMulti[T].T]`

    API Notes:
        This class is deprecated and is planned to be removed before v1.0.0
    """
    # TODO: Investigate if we have solution not needing ignore type error
    T = Optional[Union[T, Iterable[T]]] # type: ignore

    @staticmethod
    def cast(obj: "OptSingleOrMulti[T].T") -> Optional[Tuple[T, ...]]:
        if obj is None:
            return None
        elif _util.is_iterable(obj):
            return tuple(cast(Iterable[T], obj))
        else:
            return (cast(T, obj),)

IntFloat = Union[int, float]
GDSLayerSpec = Union[int, Tuple[int, int]]
# We define the gds_layer lookup table by str,
# Doing it directly by DesignMask would be preferred but this leads
# to complicated recursive imports
GDSLayerSpecDict = Dict[str, GDSLayerSpec]


# Include after class definition to avoid circular import problems.
from . import _util
