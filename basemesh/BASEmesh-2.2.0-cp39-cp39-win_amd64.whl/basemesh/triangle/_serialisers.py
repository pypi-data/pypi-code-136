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

"""(De-)Serializers for Triangle data structures.

This module contains the converters turning Triangle entities such as
nodes or segments into text and vice versa.
"""

from typing import Any, List, Optional

from .errors import ParserError
from ._geometry import Element, Segment, Node
from ._markers import HoleMarker, RegionMarker


class Parser:
    """Parser object for Triangle objects.

    Defines the logic required to validate Triangle output files and
    convert them into their Python representations.
    """

    @classmethod
    def parse_node(cls, string: str, has_marker: bool) -> 'Node':
        """Parse a Triangle output line and return a node.

        :param string: The line to parse.
        :type string: str
        :param has_marker: Whether the line contains a boundary marker.
        :type has_marker: bool
        :return: The parsed node.
        :rtype: Node
        """
        # NOTE: Node table format:
        # <Node ID> <X> <Y> [<Attr 1> <Attr 2> ...] [<boundary>]
        marker: Optional[int] = None
        words = string.split()
        try:
            id_ = int(words[0])
            pos_x, pos_y = map(float, words[1:3])
            marker = int(words[-1]) if has_marker else None
            attributes = map(float, words[3: -1] if has_marker else words[3:])
        except (ValueError, IndexError) as err:
            raise ParserError(f'Invalid node line: "{words}"') from err

        return Node(id_, pos_x, pos_y, *attributes, marker=marker)

    @classmethod
    def parse_element(cls, string: str, num_nodes: int) -> 'Element':
        """Parse a Triangle output line and return an element.

        If `use_matid` is True, a MATID column is expected at the end
        of the line.

        :param string: The line to parse.
        :type string: str
        :param num_nodes: The number of nodes in the element, 3 or 6
        :type num_nodes: int
        :return: The parsed element.
        :rtype: Element
        """
        # NOTE: Element table format:
        # <Element ID> <N1> <N2> <3> [<N4> <N5> <N6>] [<Attrs>]
        words = string.split()
        try:
            id_ = int(words[0])
            nodes = map(int, words[1: 1 + num_nodes])
            attributes = map(int, words[1 + num_nodes:])
        except (ValueError, IndexError) as err:
            raise ParserError(f'Invalid element line: "{words}"') from err
        return Element(id_, nodes, *attributes)


class Serialiser:
    """Serialisation class for Triangle data structures.

    This class keeps track of past entities. A new instance of the
    serialised must be used for each file written.
    """

    def __init__(self, zero_index: bool = False) -> None:
        self.zero_index: bool = zero_index
        self._hole_index: int = 0
        self._region_index: int = 0

    def serialise(self, entity: object, write_markers: bool = False) -> str:
        """Helper utility for serialising entities.

        :param entity: The entity to serialise.
        :type entity: object
        :param write_markers: Whether to write boundary markers.
        :type write_markers: bool
        :return: Text representation of the entity.
        :rtype: str
        :raises ValueError: If the entity is not supported.
        """
        if isinstance(entity, Node):
            return self.serialise_node(entity, write_markers)
        elif isinstance(entity, Segment):
            return self.serialise_segment(entity, write_markers)
        elif isinstance(entity, HoleMarker):
            self._hole_index += 1
            return self.serialise_hole_marker(self._hole_index, entity)
        elif isinstance(entity, RegionMarker):
            self._region_index += 1
            return self.serialise_region_marker(self._region_index, entity)
        else:
            raise ValueError(f"Cannot serialise {type(entity)}")

    @staticmethod
    def serialise_node(node: Node, marker: bool = False) -> str:
        """Convert a node to the .NODE text format.

        This format is also used for the nodes section of .POLY files.

        :param node: The node to serialise.
        :type node: Node
        :param marker: Whether to write the node boundary marker. Requires
            the node to have a non-None marker. False by default.
        :type marker: bool
        :return: .NODE format representation of the node.
        :rtype: str
        """
        words: List[Any] = [node.id, node.pos_x, node.pos_y]
        words.extend(node.attributes)
        if marker:
            words.append(node.marker if node.marker is not None else 0)
        return ' '.join(map(str, words))

    @staticmethod
    def serialise_segment(segment: Segment, marker: bool = False) -> str:
        """Convert a segment to the .POLY format.

        """
        words: List[Any] = [segment.id, segment.start, segment.end]
        if marker:
            words.append(segment.marker if segment.marker is not None else 0)
        return ' '.join(map(str, words))

    @staticmethod
    def serialise_hole_marker(id_: int, hole: HoleMarker) -> str:
        return ' '.join(map(str, [id_, hole.pos_x, hole.pos_y]))

    @staticmethod
    def serialise_region_marker(id_: int, region: RegionMarker) -> str:
        words: List[Any] = [id_, region.pos_x, region.pos_y]
        if region.attribute is not None:
            words.append(region.attribute)
        words.append(region.max_area or -1)
        return ' '.join(map(str, words))
