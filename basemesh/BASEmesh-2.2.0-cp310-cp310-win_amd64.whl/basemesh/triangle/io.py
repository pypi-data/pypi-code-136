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

"""Reader and writer functions for triangle input/output formats."""

import io
import pathlib
import warnings
from typing import (Collection, Iterable, Iterator, Optional, Tuple, TypeVar,
                    Union)

from .errors import ParserError
from ._geometry import Element, Node, Segment
from ._markers import HoleMarker, RegionMarker
from ._serialisers import Parser, Serialiser

__all__ = [
    'read_ele',
    'read_node',
    'write_node',
    'write_poly',
]

_T = TypeVar('_T')
_Path = Union[pathlib.Path, str]


def read_ele(path: _Path) -> Iterator[Tuple[int, Element]]:
    """Read an output ELE file and return its elements.

    :param path: The path to the file to process
    :type path: :class:`pathlib.Path` | :class:`str`
    :yield: A tuple consisting of an element ID and element
    :rtype: :class:`collections.abc.Iterator` [
        :class:`tuple` [:class:`int`, :class:`Element`]]
    """
    if not isinstance(path, pathlib.Path):
        path = pathlib.Path(path)
    parser = Parser()

    count_expected: int = -1
    num_nodes: int = -1
    count_actual: int = 0
    with open(path, 'r', encoding='utf-8') as file_:
        for line in _iter_triangle_file(file_):
            # Header
            if count_expected < 0:
                words = line.split()
                count_expected = int(words[0])
                num_nodes = int(words[1])
                continue
            # Contents
            element = parser.parse_element(line, num_nodes)
            yield element.id, element
            count_actual += 1

    if count_actual != count_expected:
        warnings.warn(
            f'Header of Triangle .ELE file promised {count_expected} '
            f'elements, but only {count_actual} were found. The file may be '
            f'corrupted: {path}', RuntimeWarning)


def read_node(path: _Path) -> Iterator[Tuple[int, Node]]:
    """Read an output NODE file and return its nodes.

    :param path: Path to the file to process
    :type path: :class:`pathlib.Path` | :class:`str`
    :yield: A tuple consisting of a node ID and node
    :rtype: :class:`collections.abc.Iterator` [
        :class:`tuple` [:class:`int`, :class:`Node`]]
    """
    if not isinstance(path, pathlib.Path):
        path = pathlib.Path(path)
    parser = Parser()

    count_expected: int = -1
    count_actual: int = 0
    has_marker: bool = False
    with open(path, 'r', encoding='utf-8') as file_:
        for line in _iter_triangle_file(file_):
            # Header
            if count_expected < 0:
                words = line.split()
                try:
                    count_expected = int(words[0])
                    has_marker = bool(int(words[3]))
                except (ValueError, IndexError) as err:
                    raise ParserError(
                        f'Invalid NODE header: "{words}"') from err
                continue
            # Contents
            node = parser.parse_node(line, has_marker=has_marker)
            yield node.id, node
            count_actual += 1

    if count_actual != count_expected:
        warnings.warn(
            f'Header of Triangle .NODE file promised {count_expected} nodes, '
            f'but only {count_actual} were found. The file may be corrupted: '
            f'{path}', RuntimeWarning)


def write_node(path: _Path, nodes: Collection[Node]) -> None:
    """Write an input NODE file from a set of nodes.

    The given nodes must be ordered starting with ID 0 or 1.

    The node collection must be homogenous, i.e. the attribute count
    must be the same across all nodes.

    :param path: Path to save the NODE file to. The extension will be
        replaced with `.node` if it is not already.
    :type path: :class:`pathlib.Path` | :class:`str`
    :param nodes: A sized iterable of nodes to write.
    :type nodes: :class:`collections.abc.Collection` [:class:`Node`]
    """
    with open(path, 'w', encoding='utf-8') as file_:
        _write_block_nodes(file_, nodes)


def write_poly(path: _Path, nodes: Collection[Node],
               segments: Collection[Segment],
               holes: Optional[Collection[HoleMarker]] = None,
               regions: Optional[Collection[RegionMarker]] = None,
               write_markers: bool = False) -> None:
    """Write an input POLY file from the given input geometry.

    The given input nodes must be ordered starting with 0 or 1.

    :param path: Path to save the POLY file to. The extension will be
        replaced with `.poly` if it is not already.
    :type path: :class:`pathlib.Path` | :class:`str`
    :param nodes: A sized iterable of nodes to write.
    :type nodes: :class:`collections.abc.Collection` [:class:`Node`]
    :param segments: A sized iterable of segments to write.
    :type segments: :class:`collections.abc.Collection` [
        :class:`Segment`]
    :param holes: A sized iterable of holes to write.
    :type holes: :class:`collections.abc.Collection` [
        :class:`HoleMarker`] | :obj:`None`
    :param regions: A sized iterable of regions to write.
    :type regions: :class:`collections.abc.Collection` [
        :class:`RegionMarker`] | :obj:`None`
    :param write_markers: Whether to write boundary markers.
    :type write_markers: :class:`bool`
    """
    with open(path, 'w', encoding='utf-8') as file_:
        _write_block_nodes(file_, nodes, write_markers)
        _write_block_segments(file_, segments, write_markers)
        # Holes must be written regardless, even if they are an empty list
        if holes is None:
            holes = []
        _write_block_holes(file_, holes)
        # Regions may be omitted if no regions are given
        if regions is not None:
            _write_block_regions(file_, regions)


def _get_first(iterable: Iterable[_T]) -> Tuple[_T, Iterator[_T]]:
    """Extract the first element from an iterable.

    :param iterable: Iterable to extract the first element from
    :type iterable: :class:`collections.abc.Iterable` [T]
    :returns: A tuple consisting of the first element and an iterator
        over the rest of the given iterable.
    :rtype: :class:`tuple` [T, :class:`collections.abc.Iterator` [T]]
    """
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration as err:
        raise ValueError('Iterable is empty') from err
    return first, iterator


def _iter_triangle_file(iterable: Iterable[str]) -> Iterator[str]:
    """Iterate over the contents of a triangle file.

    This strips out any blanks lines or comments.
    """
    for line in iterable:
        # Strip comments
        line, *_ = line.split('#', maxsplit=1)
        # Ignore blank lines
        line = line.strip()
        if not line:
            continue
        yield line


def _write_block_nodes(file_: io.TextIOWrapper, nodes: Collection[Node],
                       write_markers: bool = False) -> int:
    node_count = len(nodes)
    file_.write('# Nodes\n')
    # If collection is empty, write empty header
    if node_count < 1:
        file_.write('0 2 0 0\n')
        return 0

    # Determine attribute count from the first node
    node, iterator = _get_first(nodes)
    attr_count = len(node.attributes)
    if node.id not in (0, 1):
        raise ValueError(f'Initial ID must be 0 or 1, got {node.id}')
    last_id = node.id

    # Write file header and first node
    serialiser = Serialiser()
    file_.write(f'{node_count} 2 {attr_count} 0\n')
    file_.writelines([serialiser.serialise(node, write_markers), '\n'])
    # Write remaining nodes
    nodes_written = 1
    for node in iterator:
        # Check ID
        if node.id != last_id + 1:
            raise ValueError('Node IDs must be consecutive '
                             f'(expected {last_id + 1}, got {node.id})')
        last_id = node.id
        # Check attribute count
        if len(node.attributes) != attr_count:
            raise ValueError(f'Invalid node with {node.id} '
                             f'(expected {attr_count} attributes, '
                             f'got {len(node.attributes)}')
        # Write node
        file_.writelines([serialiser.serialise(node, write_markers), '\n'])
        nodes_written += 1

    return nodes_written


def _write_block_segments(file_: io.TextIOWrapper,
                          segments: Collection[Segment],
                          write_markers: bool = False) -> int:
    segment_count = len(segments)
    file_.write('# Segments\n')
    # If collection is empty, write empty header
    if segment_count < 1:
        file_.write('0 0\n')
        return 0

    # Write file header
    serialiser = Serialiser()
    file_.write(f'{segment_count} {int(write_markers)}\n')
    # Write segments
    segments_written = 0
    for segment in segments:
        # Write segment
        file_.writelines([serialiser.serialise_segment(
            segment, marker=write_markers), '\n'])
        segments_written += 1

    return segments_written


def _write_block_holes(file_: io.TextIOWrapper,
                       holes: Collection[HoleMarker]) -> int:
    hole_count = len(holes)
    file_.write('# Holes\n')
    # If collection is empty, write empty header
    if hole_count < 1:
        file_.write('0\n')
        return 0

    # Write holes
    serialiser = Serialiser()
    file_.write(f'{hole_count}\n')
    holes_written = 0
    for hole in holes:
        file_.writelines([serialiser.serialise(hole), '\n'])
        holes_written += 1

    return holes_written


def _write_block_regions(file_: io.TextIOWrapper,
                         regions: Collection[RegionMarker]) -> int:
    region_count = len(regions)
    file_.write('# Regions\n')
    # If collection is empty, write empty header
    if region_count < 1:
        file_.write('0\n')
        return 0

    # Write regions
    serialiser = Serialiser()
    file_.write(f'{region_count}\n')
    regions_written = 0
    for region in regions:
        file_.writelines([serialiser.serialise(region), '\n'])
        regions_written += 1

    return regions_written
