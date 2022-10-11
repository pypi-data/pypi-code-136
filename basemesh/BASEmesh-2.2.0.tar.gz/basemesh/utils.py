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

"""Tools and utilities for advanced mesh processing."""

import typing
import warnings

from py2dm.utils import convert_random_nodes

from basemesh.errors import BasemeshWarning

from ._mesh import Mesh, MeshNode

__all__ = [
    'Matids',
    'inherit_2dm_data',
    'inject_matid',
    'renumber_mesh',
]

Matids = typing.Tuple[typing.Union[int, float], ...]

renumber_mesh = convert_random_nodes


def inherit_2dm_data(source: Mesh, edited: Mesh) -> Mesh:
    """Apply any 2DM-specific data in `source` to `edited`.

    This function is intended to be used after editing a mesh in QGIS
    or other standalone software that may not preserve 2DM-specific
    features such as materials or node strings.

    This requries node IDs to remain unchanged.

    Rules:

    - The nodes from `edited` are used without modification.
    - The elements from `edited` are used, but will use the material
      from the corresponding element in `source` if it exists.
    - The node strings from `source` are used, any missing nodes are
      silently ignored, potentially resulting in a shorter node string.

    THis returns a new mesh object, the original meshes are not
    modified.
    """

    # Copy nodes
    output = Mesh()
    for node in edited.nodes:
        output.add_node(node.pos, node.id)

    # Copy elements
    for element in edited.elements:
        # Attempt to find the corresponding element in the source mesh
        try:
            ref_element = source.get_element_by_id(element.id)
        except KeyError:
            warnings.warn(
                f'Element {element.id} in edited mesh not found in source '
                'mesh. Unable to inherit material IDs from source mesh, '
                'using edited mesh\'s materials instead.', BasemeshWarning)
            materials = element.materials
        else:
            materials = ref_element.materials
        # Find the new mesh's nodes for the element IDs
        output.add_element(
            tuple(output.get_node_by_id(n.id) for n in element.nodes),
            element.id, *materials)

    # Copy node strings
    for name, ref_nodes in source.node_strings.items():
        # Find the new mesh's nodes for the node string's IDs
        nodes: typing.List[MeshNode] = []
        for ref_node in ref_nodes:
            try:
                node = output.get_node_by_id(ref_node.id)
            except KeyError:
                warnings.warn(
                    f'Node {ref_node.id} in node string "{name}" in source '
                    'mesh was not found in the edited mesh. Was it deleted?\n'
                    'The node has been removed from the node string.',
                    BasemeshWarning)
            else:
                nodes.append(node)
        output.add_node_string(name, nodes)

    return output


def _append(a: Matids, b: Matids) -> Matids:
    """Append the second tuple to the first."""
    return a + b


def inject_matid(source: Mesh, other: Mesh,
                 query: typing.Callable[[Matids, Matids], Matids] = _append,
                 ) -> Mesh:
    """Add one or more MATIDs to a given mesh.

    .. note::

       This utility is considered a pre-release and should not be
       relied on in larger workflows as changes are likely in upcoming
       versions.

    For every element in `source`, the element containing it is looked
    up in `other`. If it exists, the MATIDs are passed to the `query`
    function, which decides how the material indices are combined into
    a single materials list. The result is then written to the output
    mesh's element.

    The default behaviour is to append the MATIDs from `other` to the
    MATIDs from `source`. Below are several examples of other common
    query functions:

    .. code-block:: python

       def append_first(a, b):
           # Append the first MATID from `other` to the MATID list of
           # `source`.
           return a + b[:1]

       def replace_matid(a, b):
           # Replace the first MATID in `source` with the one from
           # `other`. This avoids interpolation after changing MATIDs.
           return b[:1] + a[1:]

    The node and element IDs of the resulting mesh are the same as the
    `source` mesh.

    :param source: The mesh to inject MATIDs into.
    :type source: :class:`basemesh.Mesh`
    :param other: The mesh to look up MATIDs in.
    :type other: :class:`basemesh.Mesh`
    :param query: The function to use to combine MATIDs.
    :type query: :class:`collections.abc.Callable` [
        [:class:`tuple` [:class:`int` | :class:`float`], ...],
        [:class:`tuple` [:class:`int` | :class:`float`], ...]
        ] -> [:class:`tuple` [:class:`int` | :class:`float`], ...]
    :return: A new mesh with MATIDs injected.
    :rtype: :class:`basemesh.Mesh`
    """
    output = Mesh()
    # Copy mesh nodes
    for node in source.nodes:
        output.add_node(node.pos, node.id)

    # Copy mesh node strings
    for name, nodes in source.node_strings.items():
        new_nodes = tuple(output.get_node_by_id(n.id) for n in nodes)
        output.add_node_string(name, new_nodes)

    # Copy mesh elements
    for element in source.elements:
        new_nodes = tuple(output.get_node_by_id(n.id) for n in element.nodes)

        # Find the corresponding element in the other mesh
        try:
            other_ele = other.element_at(element.center)
        except ValueError:
            # Element not found in other mesh, use source's MATIDs
            materials = element.materials
        else:
            # Element found, combine MATIDs
            materials = query(element.materials, other_ele.materials)

        output.add_element(new_nodes, element.id, *materials)

    return output
