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

"""Geometry classes for the PSLG builder module."""

from typing import Set, Tuple, Union

_Vec2 = Tuple[float, float]
_Vec3 = Tuple[float, float, float]

__class__ = [
    'Segment',
    'Vertex',
]


class Vertex:
    """An arbitrary point in 3D space.

    Note that the vertex coordinate attributes x, y, and z may not
    be modified directly as they are used in bounding box calculations
    for connected segments. If vertices are moved, the user must ensure
    that :meth:`Segment.update_bbox` is called on any connected
    segments afterwards.
    """

    __slots__ = ['_segments', 'x', 'y', 'z']

    def __init__(self, pos: Union[_Vec2, _Vec3]) -> None:
        # NOTE: We *could* wrap these coordinates in @property decorators, but
        # that would be a lot of overhead during the geometry clean-up process.
        #
        # So we'll keep these as public attributes and hope that users read the
        # class docstring.
        self.x: float = pos[0]
        self.y: float = pos[1]
        self.z: float
        if len(pos) == 2:
            self.z = 0.0
        else:
            self.z = pos[2]
        self._segments: Set[Segment] = set()

    @property
    def pos(self) -> _Vec3:
        """The vertex position as a 3D vector.
        
        :type: :class:`tuple` [
            :class:`float`, :class:`float`, :class:`float`]
        """
        return self.x, self.y, self.z
    
    @property
    def segments(self) -> Set['Segment']:
        """Return the set of segments connected to this vertex.

        This is a read-only property only intended for internal use by
        the geometry cleaning routines.

        :type: :class:`set` [:class:`Segment`]
        """
        return self._segments


class Segment:
    """A segment connecting two vertices.

    This class makes mo assumptions about the validity of the
    connection. Segments shorter than a given tolerance can be removed
    as part of the geometry cleaning process, which also removes any
    singularities or vertical segments that may be present.
    """

    __slots__ = ['start', 'end', '_bbox']

    def __init__(self, start: Vertex, end: Vertex) -> None:
        self.start: Vertex = start
        self.end: Vertex = end
        for vertex in (start, end):
            vertex.segments.add(self)
        self._bbox: Tuple[float, float, float, float] = self._calc_bbox()

    @property
    def vertices(self) -> Tuple[Vertex, Vertex]:
        """Return the start and end vertices of the segment.
        
        :type: :class:`tuple` [
            :class:`Vertex`, :class:`Vertex`]
        """
        return self.start, self.end

    def __contains__(self, value: Vertex) -> bool:
        return self.start == value or self.end == value

    def as_pair(self) -> Tuple[_Vec2, _Vec2]:
        """Return the segment as a pair of 2D points.
        
        :type: :class:`tuple` [
            :class:`tuple` [:class:`float`, :class:`float`],
            :class:`tuple` [:class:`float`, :class:`float`]]
        """
        return ((self.start.x, self.start.y), (self.end.x, self.end.y))

    def bbox_contains(
            self, point: Union[_Vec2, Vertex], tol: float = 0.0) -> bool:
        """Check whether the given point lies within the bounding box.

        The bounding box is expanded by the given tolerance in all
        directions.

        :param point: The point to check
        :type point: :class:`tuple` [:class:`float`, :class:`float`] |
            :class:`Vertex`
        :param tol: Maximum error tolerance
        :type tol: :class:`float`
        :return: True if the point lies within the bounding box
        :rtype: :class:`bool`
        """
        x_min, y_min, x_max, y_max = self._bbox
        if isinstance(point, Vertex):
            x, y = point.x, point.y
        else:
            x, y = point
        return (x_min - tol <= x <= x_max + tol
                and y_min - tol <= y <= y_max + tol)

    def bboxes_intersect(self, other: 'Segment', tol: float = 0.0) -> bool:
        """Check whether this segment's bbox intersects with another.

        This can be used as a fail-early check for segment
        intersection tests.

        :param other: The other segment
        :type other: :class:`Segment`
        :param tol: Maximum error tolerance
        :type tol: :class:`float`
        :return: True if the bounding boxes intersect
        :rtype: :class:`bool`
        """
        x_min, y_min, x_max, y_max = self._bbox
        other_x_min, other_y_min, other_x_max, other_y_max = other._bbox
        return (x_min - tol <= other_x_max
                and x_max + tol >= other_x_min
                and y_min - tol <= other_y_max
                and y_max + tol >= other_y_min)

    def replace_vertex(self, old: Vertex, new: Vertex) -> None:
        """Replace one of the segment's vertices with a new one.

        This will update the bounding box of the segment.

        :param old: The vertex to replace
        :type old: :class:`Vertex`
        :param new: The new vertex
        :type new: :class:`Vertex`
        """
        if self.start == old:
            self.start = new
        elif self.end == old:
            self.end = new
        else:
            raise ValueError(
                'The vertex to replace is not part of this segment.')
        self.update_bbox()

    def update_bbox(self) -> None:
        """Update bounding box.
        
        Call after moving or replacing vertices.
        """
        self._bbox = self._calc_bbox()

    def split_at_vertex(self, vertex: Vertex) -> Tuple['Segment', 'Segment']:
        """Create two segments from the given segment.

        The original segment is not modified.
        
        :param vertex: The vertex to split at
        :type vertex: :class:`Vertex`
        :return: The two new segments
        :rtype: :class:`tuple` [:class:`Segment`, :class:`Segment`]
        """
        return Segment(self.start, vertex), Segment(vertex, self.end)

    def _calc_bbox(self) -> Tuple[float, float, float, float]:
        return (min(self.start.x, self.end.x),
                min(self.start.y, self.end.y),
                max(self.start.x, self.end.x),
                max(self.start.y, self.end.y))
