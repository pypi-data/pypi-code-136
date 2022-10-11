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

"""String definition parsing and writing."""

from typing import Callable, Dict, List, Mapping, Optional
import warnings

from basemesh.errors import BasemeshWarning

from ._algorithms import dist_2d, point_on_line
from ._mesh import Mesh, MeshNode
from .types import LineString2D

__all__ = [
    'split_string_defs',
    'resolve_string_defs',
    'write_string_defs_sidecar',
]

# Type aliases
_Feedback = Callable[[float], None]


def _group_nodestrings(string_defs: Mapping[str, LineString2D],
                       mesh: Mesh, precision: float = 0.0, *,
                       feedback: Optional[_Feedback] = None,
                       ) -> Dict[str, List[MeshNode]]:
    """Return a mapping from string definition names to nodes.

    This processes all nodes in the input mesh, checking for
    coincidence with all node strings. It generates a dictionary
    mapping the string definition names to a list of nodes that are
    within range of the string definition line string.

    :param string_defs: A mapping of string definitions to line strings
    :type string_defs: dict [str, tuple [tuple [str, str], ...]]
    :param mesh: The mesh to process
    :type mesh: basemesh.Mesh
    :param precision: The maximum distance for a node to still be
        considered part of a line string, by default 0.0
    :type precision: float
    :feedback: A callable taking values between 0 and 1 indicating the
        progress of the operation, by default None
    :type feedback: typing.Callable [[float], None] | None
    :return: A mapping from string definitions to mesh nodes
    :rtype: dict [str, list [basemesh.MeshNode]]
    """
    total = len(mesh.nodes)
    interval = int(total / 100) if total > 100 else 1

    nodes_dict: Dict[str, List[MeshNode]] = {n: [] for n in string_defs}
    for index, node in enumerate(mesh.nodes):
        node_pos = node.pos[:2]
        for name, line_string in string_defs.items():

            # Check each subsegment
            for sub_index, point in enumerate(line_string[:-1]):
                line = point, line_string[sub_index+1]
                if point_on_line(line, node_pos, precision=precision):
                    nodes_dict[name].append(node)
                    break

        if feedback is not None and index % interval == 0:
            feedback(index/total)

    # Filter empty node strings
    nodes_map: Dict[str, List[MeshNode]] = {}
    for name, nodes in nodes_dict.items():
        if not nodes:
            warnings.warn(f'No nodes found for string definition "{name}", '
                          'no node string wil be written', BasemeshWarning)
        else:
            nodes_map[name] = nodes

    if feedback is not None:
        feedback(1.0)
    return nodes_map


def resolve_string_defs(string_defs: Dict[str, LineString2D],
                        mesh: Mesh, precision: float = 0.0,
                        feedback: Optional[_Feedback] = None,
                        ) -> Dict[str, List[int]]:
    """Resolve the string definitions for the given mesh.

    This returns the list of mesh nodes lying on the given string, in
    order of distance to the first point in the line string.

    :param string_defs: String definitions to resolve
    :type string_defs: :class:`dict` [
        :class:`str`, :class:`tuple` [
        :class:`tuple` [:class:`float`, :class:`float`], ...]]
    :param mesh: The mesh to process
    :type mesh: :class:`basemesh.Mesh`
    :param precision: The maximum distance for a node to still be
        considered part of a line string, by default 0.0
    :type precision: :class:`float`
    :feedback: A callable taking values between 0 and 1 indicating the
        progress of the operation, by default None
    :type feedback: :class:`collections.abc.Callable` [
        [:class:`float`], :obj:`None`] | :obj:`None`
    :return: A mapping from string definitions to mesh node indices
    :rtype: :class:`dict` [
        :class:`str`, :class:`list` [:class:`int`]]
    """
    # Group nodes by their matching string definition line string
    step_1: _Feedback = lambda x: feedback(x*0.5) if feedback else None
    nodes_dict: Dict[str, List[MeshNode]] = _group_nodestrings(
        string_defs, mesh, precision, feedback=step_1)

    # Sort string definition nodes based on distance to their start
    step_2: _Feedback = lambda x: feedback(0.5 + x*0.5) if feedback else None
    _sort_nodes(string_defs, nodes_dict, feedback=step_2)

    if feedback is not None:
        feedback(1.0)

    # Return string definition dict
    return {k: [n.id for n in v] for k, v in nodes_dict.items()}


def _sort_nodes(string_defs: Dict[str, LineString2D],
                nodes_dict: Dict[str, List[MeshNode]], *,
                feedback: Optional[_Feedback] = None) -> None:
    """Sort the string definition nodes.

    When the nodes are assigned to their respective line strings(s),
    they are in an unsecified order as determined by the mesh node
    iterator.

    This function sorts them by distance from the first node in the
    string definition line string.

    This mutates the provided `nodes_dict` mapping.

    :param string_defs: Original, ungrouped string definitions
    :type string_defs: :class:`dict` [
        :class:`str`, :class:`tuple` [
        :class:`tuple` [:class:`float`, :class:`float`], ...]]
    :param nodes_dict: Grouped string definitions with associated mesh
        nodes
    :type nodes_dict: :class:`dict` [
        :class:`str`, :class:`list` [:class:`basemesh.MeshNode`]]
    :feedback: A callable taking values between 0 and 1 indicating the
        progress of the operation, by default None
    :type feedback: :class:`collections.abc.Callable` [
        [:class:`float`], :obj:`None`] | :obj:`None`
    """
    total = len(nodes_dict)
    interval = int(total / 100) if total > 100 else 1

    for index, element in enumerate(nodes_dict.items()):
        name, nodes = element

        def rel_dist(node: MeshNode, sd_name: str = name) -> float:
            return dist_2d(string_defs[sd_name][0], node.pos[:2])

        nodes_dict[name] = sorted(nodes, key=rel_dist)

        if feedback is not None and index % interval == 0:
            feedback(index/total)

    if feedback is not None:
        feedback(1.0)


def split_string_defs(string_defs: Dict[str, List[int]], max_nodes: int,
                      ) -> Dict[str, List[int]]:
    """Limit the string definitions to the given length.
    
    Stringdefs longer than the given number of nodes will be broken up
    into shorter subsegments, differentiated by a numeric suffix like
    ``stringdef_01``.

    :param string_defs: The string defs to split
    :type string_defs: :class:`dict` [
        :class:`str`, :class:`list` [:class:`int`]]
    :param max_nodes: Maximum number of nodes per stringdef
    :type max_nodes: :class:`int`
    """
    if max_nodes <= 0:
        return string_defs
    
    new_string_defs: Dict[str, List[int]] = {}
    for name, nodes in string_defs.items():
        if len(nodes) <= max_nodes:
            new_string_defs[name] = nodes
        else:
            # Split into subsegments
            for index, start in enumerate(range(0, len(nodes), max_nodes)):
                start -= index
                end = start + max_nodes
                subsegment = nodes[start:end]
                new_name = f'{name}_{index+1:02d}'
                new_string_defs[new_name] = subsegment
    
    return new_string_defs


def write_string_defs_sidecar(string_defs: Dict[str, List[int]],
                              file_path: str) -> None:
    """Write the string definitions into a separate text file.

    This format is required for BASEMENT 2.8.

    :param string_defs: The string definitions to write
    :type string_defs: :class:`dict` [
        :class:`str`, :class:`list` [:class:`int`]]
    :param file_path: The path to the file to write
    :type file_path: :class:`str`
    """
    # Write string defs
    with open(file_path, 'w', encoding='utf-8') as sd_file:
        for name, node_ids in string_defs.items():
            sd_file.write(f'STRINGDEF {{\n\tname = {name}\n\tnode_ids = (')
            sd_file.write(' '.join(map(str, node_ids)))
            sd_file.write(')\n\tupstream_direction = right\n}\n')
