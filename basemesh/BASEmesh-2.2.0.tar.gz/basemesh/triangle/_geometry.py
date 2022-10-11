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

"""Triangle-specific 2D geometries.

This covers the 2D nodes and segments used to constrain the
triangulation, as well as the generated 2D elements.
"""

from typing import Iterable, Optional, Tuple

__all__ = [
    'Element',
    'Node',
    'Segment',
]


class Node:
    """A two-dimensional PSLG node for use in Triangle.

    :ivar id_: The node ID.
    :vartype id_: :class:`int`
    :ivar pos_x: The x-coordinate of the node.
    :vartype pos_x: :class:`float`
    :ivar pos_y: The y-coordinate of the node.
    :vartype pos_y: :class:`float`
    :ivar marker: A special marker optionally created during the
        triangulation process, used to mark nodes' associativity with
        segments.
    :ivar marker: :class:`int` | :obj:`None`
    :ivar \\*attributes: Additional attributes to store with the node.
        During triangulation, these attributes will be linearly
        interpolated for any new nodes created. This can be used to
        retain and interpolate elevation data when triangulating 3D
        points.
    :vartype \\*attributes: float
    """

    __slots__ = ['attributes', 'id', 'marker', 'pos_x', 'pos_y']

    def __init__(self, id_: int, pos_x: float, pos_y: float,
                 *attributes: float, marker: Optional[int] = None) -> None:
        self.id: int = id_
        self.pos_x: float = pos_x
        self.pos_y: float = pos_y
        self.attributes: Tuple[float, ...] = attributes
        self.marker: Optional[int] = marker

    def as_tuple(self) -> Tuple[float, float]:
        """Return the coordinates of the node as a tuple of floats.
        
        :type: :class:`tuple` [:class:`float`, :class:`float`]
        """
        return self.pos_x, self.pos_y


class Segment:
    """A two-dimensional PSLG segment for use in Triangle.

    :ivar id_: The segment ID.
    :vartype id_: :class:`int`
    :ivar start: Starting node id of the segment.
    :vartype start: :class:`int`
    :ivar end: Ending node id of the segment.
    :vartype end: :class:`int`
    :ivar marker: A special marker allowing to flag nodes and elements
        created during the triangulation process that are connected to
        this segment.
    :vartype marker: :class:`int` | :obj:`None`
    """

    __slots__ = ['end', 'id', 'marker', 'start']

    def __init__(self, id_: int, start: int, end: int, *,
                 marker: Optional[int] = None) -> None:
        self.id: int = id_
        self.start: int = start
        self.end: int = end
        self.marker: Optional[int] = marker


class Element:
    """A two-dimensional PSLG element for use in Triangle.

    :ivar id_: The element ID.
    :vartype id_: :class:`int`
    :ivar nodes: An iterable containing three or six integers
    :vartype nodes: :class:`collections.abc.Iterable` [:class:`int`]
    :ivar \\*attributes: The region attribute of the element, if any.
    :vartype \\*attributes: :class:`int` | :obj:`None`
    """

    __slots__ = ['attributes', 'id', 'nodes']

    def __init__(self, id_: int, nodes: Iterable[int],
                 *attributes: int) -> None:
        self.id: int = id_
        self.nodes: Tuple[int, ...] = tuple(nodes)
        if len(self.nodes) not in (3, 6):
            raise ValueError(f'Invalid number of nodes: {len(self.nodes)}, '
                             'expected 3 or 6')
        self.attributes: Tuple[int, ...] = attributes
