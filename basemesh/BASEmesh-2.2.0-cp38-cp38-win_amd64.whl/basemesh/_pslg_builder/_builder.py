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

import array
import collections
import itertools
import warnings
from typing import Deque, Iterable, List, Optional, Tuple, Union

from .._algorithms import (dist_2d, interpolate_line, line_intersection,
                           line_segments_intersection, point_on_line)
from ..errors import BasemeshWarning, TopologyError
from ..triangle import Node as TriangleNode, Segment as TriangleSegment

from ._geometry import Vertex, Segment

__all__ = [
    'PSLGBuilder',
]


class PSLGBuilder:
    """Builder class for Triangle input geometries.

    Add input data using :meth:`add_vertex` and :meth:`add_segment` to
    define the geometry.
    
    Optionall call one of the following methods to clean the geometry
    in place:

    - :meth:`merge_vertices`
    - :meth:`merge_coincident_segments`
    - :meth:`insert_intersection_vertices`
    - :meth:`remove_singular_segments`
    - :meth:`split_segments`
    
    Finally, call :meth:`build` to generate the Triangle input nodes
    and segments from the updated geometry.
    """

    def __init__(self) -> None:
        self._vertices: Deque[Vertex] = collections.deque()
        self._segments: Deque[Segment] = collections.deque()

    def __contains__(self, value: Union[Vertex, Segment]) -> bool:
        if isinstance(value, Vertex):
            return value in self._vertices
        return value in self._segments

    @property
    def vertex_count(self) -> int:
        """Number of vertices in the lattice.
        
        :type: :class:`int`
        """
        return len(self._vertices)

    @property
    def segment_count(self) -> int:
        """Number of segments in the lattice.
        
        :type: :class:`int`
        """
        return len(self._segments)

    def add_vertex(self, vertex: Vertex) -> None:
        """Add a vertex to the lattice.

        .. seealso:: :meth:`add_vertices`
        """
        self._vertices.append(vertex)

    def add_segment(self, segment: Segment) -> None:
        """Add a segment to the lattice.

        .. seealso:: :meth:`add_segments`
        """
        self._segments.append(segment)

    def add_vertices(self, vertices: Iterable[Vertex]) -> None:
        """Add vertices to the lattice.

        This is recommended over :meth:`add_vertex` for sequences as
        it extends the list all at once, rather than one at a time.
        """
        self._vertices.extend(vertices)

    def add_segments(self, segments: Iterable[Segment]) -> None:
        """Add segments to the lattice.

        This is recommended over :meth:`add_segment` for sequences as
        it extends the list all at once, rather than one at a time.
        """
        self._segments.extend(segments)

    def build(self) -> Tuple[List[TriangleNode], List[TriangleSegment]]:
        """Generate Triangle input nodes and segment from lattice data.

        Triangle node and segment IDs are assigned automatically in
        ascending order.

        No validation or cleaning is performed by this method. If
        cleaning is required, run the corresponding cleanup methods
        first. See the :class:`PSLGBuilder` class's docstring for a
        list of available cleanup procedures.

        The Z coordinate of any vertices will be converted into an
        attribute of the corresponding Triangle node.

        :return: A tuple of (nodes, segments)
        :rtype: :class:`tuple` [
            :class:`list` [:class:`triangle.Node`],
            :class:`list` [:class:`triangle.Segment`]]
        """
        vertices = {v: TriangleNode(i+1, v.x, v.y, v.z)
                    for i, v in enumerate(self._vertices)}

        segments: List[TriangleSegment] = []
        for index, segment in enumerate(self._segments):
            node_ids = [vertices[v].id for v in segment.vertices]
            segments.append(TriangleSegment(index+1, *node_ids))

        return list(vertices.values()), segments

    def clear(self) -> None:
        """Remove all vertices and segments from the lattice."""
        self._vertices.clear()
        self._segments.clear()

    def merge_vertices(self, tol: float) -> int:
        """Remove duplicate vertices from the builder.

        The earlier vertex will always be kept. Segments are
        automatically reconnected to the remaining vertex.
        
        :param tol: The maximum distance between two vertices to be
            considered a duplicate.
        :type tol: :class:`float`
        :return: The number of vertices removed.
        :rtype: :class:`int`
        """
        vertices = self._vertices
        removed = array.array('L')

        for i in range(len(vertices)):
            # Skip if this vertex has already been removed as a duplicate in a
            # previous iteration
            if i in removed:
                continue

            # Check any later vertices for duplicates
            for j in range(i+1, len(vertices)):
                # Skip any already removed vertices
                if j in removed:
                    continue

                if _dist(vertices[i], vertices[j]) <= tol:
                    removed.append(j)
                    # Reconnect any segments that use the duplicate vertex
                    for segment in vertices[j].segments:
                        segment.replace_vertex(vertices[j], vertices[i])
            
        # Remove the duplicate vertices
        self._vertices = collections.deque(
            v for i, v in enumerate(vertices) if i not in removed)

        return len(removed)            

    def merge_coincident_segments(self) -> int:
        """Deduplicate segments describing the same connection.
        
        For any pair of two segments with the same start and end point
        (order is not relevant), only one will be kept. The earlier
        segment will always be kept.

        This only considers exactly coincident segments. It is
        recommended to run :meth:`merge_vertices` first to snap
        similar segments together prior to calling this method.

        :return: The number of segments removed.
        :rtype: :class:`int`
        """
        segments = self._segments
        removed = array.array('L')

        for i in range(len(segments)):
            # Skip if this segment has already been removed as a duplicate in a
            # previous iteration
            if i in removed:
                continue
            i_set = set(segments[i].as_pair())

            # Check any later segments for duplicates
            for j in range(i+1, len(segments)):
                # Skip any already removed segments
                if j in removed:
                    continue
                j_set = set(segments[j].as_pair())
            
                if i_set == j_set:
                    removed.append(j)
                    for vertex in segments[j].vertices:
                        vertex.segments.discard(segments[j])

        # Remove the duplicate segments
        self._segments = collections.deque(
            s for i, s in enumerate(segments) if i not in removed)

        return len(removed)

    def insert_intersection_vertices(self, tol: float) -> int:
        """Insert new vertices at any segment intersection points.
        
        This will leave vertices on the middle of continuous segments,
        which is not permitted in Triangle. Run :meth:`split_segments`
        after this method to break the segments up at the inserted
        vertices, which eliminates intersections.
        
        :param tol: Minimum distance an intersection must be from one
            of the endpoints of the segment.
        :type tol: :class:`float`
        :return: The number of vertices inserted.
        :rtype: :class:`int`
        """
        vertices = self._vertices
        segments = self._segments
        inserted = 0

        for i, segment in enumerate(segments):
            for j in range(i+1, len(segments)):
                intersection = _segment_intersection(segment, segments[j], tol)
                if intersection is not None:
                    inserted += 1
                    vertices.append(intersection)

        return inserted

    def remove_singular_segments(self) -> int:
        """Remove any zero-length segments.

        :return: The number of segments removed.
        :rtype: :class:`int`
        """
        segments = self._segments
        removed = array.array('L')

        for i, segment in enumerate(segments):
            if _dist(*segment.vertices) == 0:
                removed.append(i)
                for vertex in segment.vertices:
                    vertex.segments.discard(segment)

        # Remove the zero-length segments
        self._segments = collections.deque(
            s for i, s in enumerate(segments) if i not in removed)

        return len(removed)

    def split_segments(self, tol: float) -> int:
        """Split any segments that are intersected by a vertex.
        
        The old segments will be deleted.
        
        :param tol: Maximum distance a node may be from a segment to
            still be considered intersecting.
        :type tol: :class:`float`
        :return: The number of segments that were split. Note that one
            segment may be split multiple times if it is intersected by
            more than one node.
        :rtype: :class:`int`
        """
        segments = self._segments
        to_remove = array.array('L')

        for i in itertools.count():
            try:
                segment = segments[i]
            except IndexError:
                break

            line = segment.as_pair()
            for vertex in self._vertices:
                # Ignore the segment's defining vertices
                if vertex in segment.vertices:
                    continue

                # Ignore vertices that are outside the segment's bounding box
                vertex_pos = vertex.x, vertex.y
                if not segment.bbox_contains(vertex_pos, tol):
                    continue

                # Check for line intersection
                if point_on_line(line, vertex_pos, tol):
                    # Create new segments for each side of the intersection
                    segments.extend(segment.split_at_vertex(vertex))
                    # Schedule the old segment for removal
                    to_remove.append(i)
                    break
        
        self._segments = collections.deque(
            s for i, s in enumerate(segments) if i not in to_remove)

        return len(to_remove)
        

def _dist(a: Vertex, b: Vertex) -> float:
    return dist_2d((a.x, a.y), (b.x, b.y))


def _segment_intersection(
        a: Segment, b: Segment, tol: float) -> Optional[Vertex]:
    """Multi-step test for segment intersections.
    
    First, the segment bounding boxes are compared. If they intersect,
    a ray intersection algorithm is used to identify the intersection
    point. Finally, the intersection point is checked to ensure it is
    both on the line segments and far enough away from the endpoints.
    
    :param a: First segment to check.
    :type a: :class:`Segment`
    :param b: Second segment to check.
    :param b: :class:`Segment`
    :param tol: Minimum distance from the endpoints of both segments.
    :type tol: :class:`float`
    :return: A new Vertex at the intersection of the two segments, or
        None if the segments do not meet the above criteria.
    :rtype: :class:`Vertex` | :onj:`None`
    """
    # Check if the bounding boxes intersect
    if not a.bboxes_intersect(b):
        return None
    
    # Ray intersection & check if the intersection is on the segments
    line_a = a.as_pair()
    line_b = b.as_pair()
    if not line_segments_intersection(line_a, line_b, allow_collinear=False):
        return None
    
    # Get coordinates of intersection point
    try:
        intersection = line_intersection(line_a, line_b)
    except ValueError as err:
        raise TopologyError(f'Collinear line segments found: {line_a} '
                            f'and {line_b}') from err

    # Interpolate line segments to create 3D intersection point
    height_a = interpolate_line(intersection, (a.start.pos, a.end.pos))
    height_b = interpolate_line(intersection, (b.start.pos, b.end.pos))
    # Warn if the intersection point's height is significantly different
    if abs(height_a - height_b) > tol:
        warnings.warn('Elevation mismatch of segment intersection at '
                      f'{intersection}: ignoring conflicting height '
                      f'{height_b}, new height is {height_a}', BasemeshWarning)
    vertex = Vertex((*intersection, height_a))
    
    # Check if the intersection point is far enough away from the endpoints of
    # both segments
    if (_dist(vertex, a.start) <= tol
            or _dist(vertex, a.end) <= tol
            or _dist(vertex, b.start) <= tol
            or _dist(vertex, b.end) <= tol):
        return None

    return vertex
