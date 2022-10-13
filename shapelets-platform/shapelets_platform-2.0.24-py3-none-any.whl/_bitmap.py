# Copyright (c) 2022 Shapelets.io
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from __future__ import annotations

import typing

import numpy

from . import _shapelets
from ._shapelets import Bitmap, empty_bitmap


class Bitmap:
    """
    A compressed bitmap structure.

    Bitmaps are a generalization of [Roaring Bitmaps](https://roaringbitmap.readthedocs.io/en/latest/),
    ([Apache License 2.0](https://github.com/RoaringBitmap/RoaringBitmap/blob/master/LICENSE)), working
    on a 64 bit addressing space.
    """

    # def __init__(self) -> None:
    #     """
    #     Builds an empty bitmap

    #     See Also
    #     --------
    #     of: Creates a new bitmap, whose set positions are indicated by an array.
    #     """
    #     ...

    @property
    def cardinality(self) -> int:
        """
        Returns the number of bit set.
        """
        ...

    #     @property
    #     def empty(self) -> bool:
    #         """
    #         Returns True if the bitmap has not bits set to one; otherwise, it returns False.
    #         """
    #         ...

    #     @property
    #     def first(self) -> typing.Optional[int]:
    #         """
    #         Returns None if the bitmap is empty; otherwise, it returns the position of the first
    #         bit set to one.
    #         """
    #         ...

    #     @property
    #     def last(self) -> typing.Optional[int]:
    #         """
    #         Returns None if the bitmap is empty; otherwise, it returns the position of the last
    #         bit set to one.
    #         """
    #         ...

    #     @property
    #     def in_memory_size(self) -> int:
    #         """
    #         Returns an approximate number of bytes representing the current amount of memory
    #         consumed by this instance.
    #         """
    #         ...

    #     @property
    #     def persisted_size(self) -> int:
    #         """
    #         Returns the amount of bytes required to store this instance in a durable store.
    #         """
    #         ...

    #     def copy(self) -> Bitmap:
    #         """
    #         Clones this instance, returning a new bitmap with the same bits set as the
    #         current.
    #         """
    #         ...

    #     @staticmethod
    #     def of(array: numpy.ndarray[numpy.uint64]) -> Bitmap:
    #         """
    #         Initializes a new instance of a bitmap
    #         """
    #         ...

    #     def set(self, position: int, endEx: typing.Optional[int] = None) -> None:
    #         """
    #         Sets to one either an individual position or a range of consecutive positions.

    #         Parameters
    #         ----------
    #         position: required, unsigned integer
    #             Position to set or, when parameter endEx is given, the starting point of the
    #             range whose positions are to be set to one.
    #         endEx: optional, defaults to None
    #             When set, it determines an exclusive end for the range that starts at position.

    #         """
    #         ...

    #     def unset(self, position: int, endEx: typing.Optional[int]) -> None:
    #         """
    #         Sets to zero either an individual position or a range of consecutive positions.

    #         Parameters
    #         ----------
    #         position: required, unsigned integer
    #             Position to reset or, when parameter endEx is given, the starting point of the
    #             range whose positions are to be set to zero.
    #         endEx: optional, defaults to None
    #             When set, it determines an exclusive end for the range that starts at position.

    #         """
    #         ...

    #     def flip(self, position: int, endEx: typing.Optional[int]) -> None:
    #         """
    #         Inverts the current value of a position or a range of consecutive positions.

    #         Parameters
    #         ----------
    #         position: required, unsigned integer
    #             Position whose value is to be inverted or, when parameter endEx is given,
    #             the starting point of the range whose positions are to be inverted.
    #         endEx: optional, defaults to None
    #             When set, it determines an exclusive end for the range that starts at position.

    #         """
    #         ...

    #     def contract(self, position: int, by: int) -> None:
    #         """
    #         Shifts left a bitmap, by a number of positions, at a particular location.
    #         """
    #         ...

    #     def expand(self, position: int, by: int) -> None:
    #         """
    #         Expands a bitmap, by adding a number of positions set to zero, at a particular location
    #         """
    #         ...

    #     def lower_cardinality(self, position: int) -> int:
    #         """
    #         Returns the number of bits set before the given position
    #         """
    #         ...

    #     def upper_cardinality(self, position: int) -> int:
    #         """
    #         Returns the number of bits set above the given position
    #         """
    #         ...

    #     def nth(self, ordinal: int) -> int:
    #         """
    #         Returns the position of the nth bit set.

    #         Parameters
    #         ----------
    #         nth: required, unsigned integer
    #             Ordinal bit whose position is to be returned.

    #         """
    #         ...

    #     def self_or_next(self, position: int) -> typing.Optional[int]:
    #         """
    #         Returns either the given position if set; otherwise, it will return the next
    #         set position found after `position`

    #         Parameters
    #         ----------
    #         position: required unsigned integer
    #             Position to test

    #         """
    #         ...

    #     def self_or_previous(self, position: int) -> typing.Optional[int]:
    #         """
    #         Returns either the given position when set; otherwise, looks for the previous
    #         position set (whose index is less than the given position.)

    #         Parameters
    #         ----------
    #         position: required unsigned integer
    #             Position to test

    #         """
    #         ...

    #     def slice(self, startInc: int, endInc: int) -> Bitmap:
    #         """
    #         Creates a new bitmap from the bits between a range.

    #         Parameters
    #         ----------
    #         startInc: required unsigned integer
    #             Starting point (included) of the slice

    #         endInc: required, unsigned integer
    #             End point (included) of the slice

    #         """
    #         ...

    #     def bool_array(self, *, invert: bool = True, relative: bool = True) -> numpy.ndarray[bool]:
    #         """
    #         Returns a boolean array.

    #         Parameters
    #         ----------
    #         invert: boolean, defaults to True
    #             When invert is set, flags currently unset in the bitmap will be reported as True in the
    #             output array; otherwise, there will be no translation in the conversion process.

    #         relative: boolean, defaults to True
    #             When relative is set, the first position of the output array (zero) would refer to the
    #             first position set in the bitmap.  When relative is set to false, the extraction
    #             process will start at bitmap's position zero.
    #         """
    #         ...

    #     def index_array(self) -> numpy.ndarray[numpy.uint64]:
    #         """
    #         Returns an array with whose contents are the indices currently set in this bitmap.
    #         """
    #         ...

    #     def contains(self, position: int) -> bool:
    #         """
    #         Checks if a given position is set or unset.

    #         Parameters
    #         ----------
    #         position: required, unsigned integer
    #             Position to test

    #         Returns
    #         -------
    #         bool: True if the bit at the given position is set; otherwise, False.

    #         """
    #         ...

    #     def all(self, startInc: int, endEx: int) -> bool:
    #         """
    #         Checks if a range of positions on the bitmap are all set.

    #         Parameters
    #         ----------
    #         startInc: required, unsigned integer
    #             Starting point of the range (included)
    #         endEx: required, unsigned integer
    #             End of the range (excluded)

    #         """
    #         ...

    #     def any(self, startInc: int, endEx: int) -> bool:
    #         """
    #         Checks if at least one position in a range is set.

    #         Parameters
    #         ----------
    #         startInc: required, unsigned integer
    #             Starting point of the range (included)
    #         endEx: required, unsigned integer
    #             End of the range (excluded)
    #         """
    #         ...

    #     def has_shared_positions(self, other: Bitmap) -> bool:
    #         """
    #         Returns True if this bitmap has at least one bit set in common with
    #         another bitmap (intersection is not empty.)
    #         """
    #         ...

    #     def strict_subset_of(self, other: Bitmap) -> bool:
    #         """
    #         Returns True if all bits set in this bitmap are also set in another
    #         bitmap (that is, the intersection has the same bits as this instance)
    #         """
    #         ...

    #     def subset_of(self, other: Bitmap) -> bool:
    #         """
    #         TODO
    #         """
    #         ...

    #     def difference(self, other: Bitmap) -> Bitmap:
    #         """
    #         Returns a new Bitmap with the difference between this bitmap and another.

    #         The difference is defined by those bits set in this bitmap which are
    #         not set in the other bitmap.
    #         """
    #         ...

    #     def intersect(self, other: Bitmap) -> Bitmap:
    #         """
    #         Returns a new bitmap with the intersection between this bitmap and another.
    #         """
    #         ...

    #     def symmetric_difference(self, other: Bitmap) -> Bitmap:
    #         """
    #         Returns a new bitmap, whose positions set correspond to all those bits set
    #         in either sets with exception of the common ones.
    #         """
    #         ...

    #     def union(self, other: Bitmap) -> Bitmap:
    #         """
    #         Returns a new bitmap, with all positions set from either bitmap instance.
    #         """
    #         ...

    #     def inplace_difference(self, other: Bitmap) -> Bitmap: ...
    #     def inplace_intersect(self, other: Bitmap) -> Bitmap: ...
    #     def inplace_symmetric_difference(self, other: Bitmap) -> Bitmap: ...
    #     def inplace_union(self, other: Bitmap) -> Bitmap: ...

    #     def __and__(self, other: Bitmap) -> Bitmap: ...
    #     def __contains__(self, position: int) -> bool: ...
    #     def __eq__(self, other: Bitmap) -> bool: ...
    #     def __iand__(self, other: Bitmap) -> Bitmap: ...
    #     def __ior__(self, other: Bitmap) -> Bitmap: ...
    #     def __isub__(self, other: Bitmap) -> Bitmap: ...
    #     def __iter__(self) -> typing.Iterator: ...
    #     def __ixor__(self, other: Bitmap) -> Bitmap: ...
    #     def __len__(self) -> int: ...
    #     def __or__(self, other: Bitmap) -> Bitmap: ...
    #     def __sub__(self, other: Bitmap) -> Bitmap: ...
    #     def __xor__(self, other: Bitmap) -> Bitmap: ...

    __hash__ = None
    pass


def empty_bitmap() -> _shapelets.Bitmap:
    ...


__all__ = ["Bitmap", "empty_bitmap"]
