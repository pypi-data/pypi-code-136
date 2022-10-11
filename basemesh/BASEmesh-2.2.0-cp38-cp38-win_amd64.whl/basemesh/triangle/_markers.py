# A component of the BASEmesh pre-processing toolkit.
# Copyright (C) 2020  ETH Zürich
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Hole and region marker definitions used for triangulation."""

from typing import Optional, Tuple

__all__ = [
    'HoleMarker',
    'RegionMarker',
]


class _Marker:
    """Base class for Triangle markers.

    :ivar pos_x: The x-coordinate of the hole.
    :vartype pos_x: :class:`float`
    :ivar pos_y: The y-coordinate of the hole.
    :vartype pos_y: :class:`float`
    """

    __slots__ = ['pos_x', 'pos_y']

    def __init__(self, pos_x: float, pos_y: float) -> None:
        self.pos_x: float = pos_x
        self.pos_y: float = pos_y

    def as_tuple(self) -> Tuple[float, float]:
        """Return the coordinates of the marker as a tuple."""
        return self.pos_x, self.pos_y


class HoleMarker(_Marker):
    """Marks a segment-bounded region as a hole.

    :ivar pos_x: The x-coordinate of the hole.
    :vartype pos_x: :class:`float`
    :ivar pos_y: The y-coordinate of the hole.
    :vartype pos_y: :class:`float`
    """


class RegionMarker(_Marker):
    """Defines meshing properties of a segment-bounded region.

    :ivar pos_x: The x-coordinate of the region marker.
    :vartype pos_x: :class:`float`
    :ivar pos_y: The y-coordinate of the region marker.
    :vartype pos_y: :class:`float`
    :ivar max_area: A maximum area constraint to apply to elements in
        this region. Negative values disable area constraints. By
        default -1.0.
    :vartype max_area: :class:`float`
    :ivar attribute: A regional attribute to associate with elements
        in this region. By default None.
    :vartype attribute: :class:`int` | :class:`None`
    """

    __slots__ = ['attribute', 'max_area']

    def __init__(self, pos_x: float, pos_y: float, *, max_area: float = -1.0,
                 attribute: Optional[int] = None) -> None:
        super().__init__(pos_x, pos_y)
        self.attribute: Optional[int] = attribute
        self.max_area: Optional[float] = max_area if max_area > 0.0 else -1.0
