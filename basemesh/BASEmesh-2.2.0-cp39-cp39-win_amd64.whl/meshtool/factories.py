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

"""Helper mesh factories.

These factories are still abstract, but provide simplified endpoints
for common factory designs.
"""

import math
from typing import List, Sequence, Tuple

from basemesh.types import Point2D

from .core import BasicFactory, Node, Segment

__all__ = [
    'CircularMeshFactory',
    'RectangularMeshFactory',
    'segments_from_perimeter',
]


class CircularMeshFactory(BasicFactory):
    """A factory for meshes with circular domains.

    This is a subclass of BasicFactory that also generates a circular
    mesh domain as part of its initialiser.

    The user can either subclass this factory to define their elevation
    function or use the :class:`elevation_func <meshtool.BasicFactory>`
    method to set the function for an initialised factory.
    """

    def __init__(self, radius: float, segments: int = 20,
                 midpoint_offset: Point2D = (0.0, 0.0)) -> None:
        """Initialise a mesh factory with a circular domain.

        Note that the domain cannot actually be perfectly circular due
        to the triangulation. Use the segments argument to specify the
        number of edges of the polygon used to approximate a circle to
        the accuracy your model requires.

        :param radius: The radius of the circular domain.
        :type radius: :class:`float`
        :param segments: The number of edges of the polygon used to
            approximate a circle.
        :type segments: :class:`int`
        :param midpoint_offset: The offset of the midpoint of the
            domain from the origin.
        :type midpoint_offset: :class:`tuple` [
            :class:`float`, :class:`float`]
        :raises ValueError: If the radius is negative or zero.
        """
        super().__init__()
        if radius <= 0.0:
            raise ValueError('Domain radius must be greater than zero')
        # Create a polygon approximating the given input circle
        vertices = self._polygonise_circle(radius, segments, *midpoint_offset)
        self.nodes = [Node(p) for p in vertices]
        # Add breaklines around the perimeter of the circle
        self.segments = segments_from_perimeter(self.nodes)

    @staticmethod
    def _polygonise_circle(radius: float, sides: int = 12,
                           offset_x: float = 0.0,
                           offset_y: float = 0.0) -> List[Point2D]:
        """Return a regular polygon approximating the given circle.

        The polygon's vertices will lie on the circle, its edges will
        therefore intersect the circle.

        :param radius: The radius of the circle.
        :type radius: :class:`float`
        :param sides: The number of sides of the polygon.
        :type sides: :class:`int`
        :param offset_x: The x-offset of the circle's midpoint.
        :type offset_x: :class:`float`
        :param offset_y: The y-offset of the circle's midpoint.
        :type offset_y: :class:`float`
        :return: The vertices of the polygon approximating the circle.
        :rtype: :class:`list` [
            :class:`tuple` [:class:`float`, :class:`float`]]
        """
        vertices: List[Point2D] = []
        for index in range(0, sides):
            # Calculate the angle of the given point
            angle = index/sides * 2 * math.pi
            # Get the x and y coordinates for the given angle
            pos_x = (math.sin(angle) * radius) + offset_x
            pos_y = (math.cos(angle) * radius) + offset_y
            # Add the vertex
            vertices.append((pos_x, pos_y))
        return vertices


class RectangularMeshFactory(BasicFactory):
    """A factory for meshes with rectangular domains.

    This is a subclass of BasicFactory that also generates a
    rectangular mesh domain as part of its initialiser.

    The user can either subclass this factory to define their elevation
    function or use the :class:`elevation_func <meshtool.BasicFactory>`
    method to set the function for an initialised factory.
    """

    def __init__(self, width: float, height: float,
                 midpoint_offset: Tuple[float, float] = (0.0, 0.0)) -> None:
        """Initialise the mesh factory.

        :param width: The width of the rectangular domain.
        :type width: :class:`float`
        :param height: The height of the rectangular domain.
        :type height: :class:`float`
        :param midpoint_offset: The offset of the midpoint of the
            domain from the origin.
        :type midpoint_offset: :class:`tuple` [
            :class:`float`, :class:`float`]
        :raises ValueError: If the width or height is negative or zero.
        """
        super().__init__()
        if width <= 0.0 or height <= 0.0:
            raise ValueError('Domain edge length must be greater than zero')
        # Calculate corner vertices
        offset_x, offset_y = midpoint_offset
        min_x = offset_x - width/2
        max_x = offset_x + width/2
        min_y = offset_y - height/2
        max_y = offset_y + height/2
        # Set mesh nodes
        self.nodes = [Node((min_x, min_y)), Node((max_x, min_y)),
                      Node((max_x, max_y)), Node((min_x, max_y))]
        # Add breaklines around the perimeter
        self.segments = segments_from_perimeter(self.nodes)


def segments_from_perimeter(nodes: Sequence[Node]) -> List[Segment]:
    """Create a permieter boudnary from the given nodes.

    The nodes are expected to represent an ordered loop, such as the
    boundary nodes of a rectangle or circle.
    """
    segments: List[Segment] = []
    for index, node in enumerate(nodes[1:]):
        segments.append(Segment(nodes[index], node))
    segments.append(Segment(nodes[-1], nodes[0]))
    return segments
