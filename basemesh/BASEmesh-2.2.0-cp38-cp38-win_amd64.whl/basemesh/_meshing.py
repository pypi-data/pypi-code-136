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

"""Mesh generation utility."""

import pathlib
from typing import Any, Collection, Dict, Iterator, Optional, Union
from .triangle import (Element, HoleMarker, Node, RegionMarker, Segment,
                       command, read_output, triangulate)
from ._mesh import Mesh, MeshNode


def elevation_mesh(nodes: Collection[Node],
                   segments: Optional[Collection[Segment]] = None,
                   *, move_tempfiles: Optional[str] = None,
                   **kwargs: Any) -> Mesh:
    """Triangulate the given input vertices and break lines.

    Generate a TIN mesh from the given 3D input nodes and break lines.
    No mesh quality constraints are applied. The output mesh will
    contain elevation data. Any nodes generated during the meshing
    process will be assigned an interpolated elevation value.

    Any keyword arguments are forwarded to the
    :func:`basemesh.triangle.command` function.

    :param nodes: The nodes to mesh
    :type nodes: :class:`collections.abc.Collection` [
        :class:`basemesh.triangle.Node` ]
    :param segments: Optional line segments connecting the given nodes
    :type segments: :class:`collections.abc.Collection` [
        :class:`basemesh.triangle.Segment` ]
    :param move_tempfiles: Directory to perform the meshing in. If not
        provided, the meshing is performed in a temporary directory
        which is deleted automatically.
    :type move_tempfiles: :class:`str` | :obj:`None`
    :param \\*\\*kwargs: Extra keyword arguments to forward to the
        :func:`basemesh.triangle.command` function
    :type \\*\\*kwargs: :class:`dict` [:class:`str`, :obj:`typing.Any`]
    :return: The triangulated mesh
    :rtype: :class:`basemesh.Mesh`
    """
    triangle_cmd = command(**kwargs)
    if move_tempfiles is not None:
        move_tempfiles = move_tempfiles + '/triangle_tempfiles'
    output = triangulate(nodes, segments or [],
                         triangle_cmd=triangle_cmd,
                         triangle_io_dir=move_tempfiles)
    return mesh_from_triangle(output, elevation=1)


def quality_mesh(nodes: Collection[Node],
                 segments: Optional[Collection[Segment]] = None,
                 holes: Optional[Collection[HoleMarker]] = None,
                 regions: Optional[Collection[RegionMarker]] = None,
                 *,
                 min_angle: Optional[float] = None,
                 max_area: Optional[float] = None,
                 move_tempfiles: Optional[str] = None,
                 **kwargs: Any) -> Mesh:
    """Advanced Meshing with mesh quality constraints applied.

    Generate a 2D mesh from the given 2D input nodes and break lines.
    Any elevation data in the input nodes is ignored. The output mesh
    will not contain any elevation data and must be interpolated
    separately.

    Any keyword arguments are forwarded to the
    :func:`basemesh.triangle.command` function.

    :param nodes: The nodes to mesh
    :type nodes: :class:`collections.abc.Collection` [
        :class:`basemesh.triangle.Node`]
    :param segments: Optional line segments connecting the given nodes
    :type segments: :class:`collections.abc.Collection` [
        :class:`basemesh.triangle.Segment`]
    :param holes: Optional hole markers
    :type holes: :class:`collections.abc.Collection` [
        :class:`basemesh.triangle.HoleMarker`]
    :param regions: Optional region markers
    :type regions: :class:`collections.abc.Collection` [
        :class:`basemesh.triangle.RegionMarker`]
    :param min_angle: Minimum angle constraint in degrees
    :type min_angle: :class:`float` | :obj:`None`
    :param max_area: Global maximum area constraint in square units.
        Will be overridden by any region markers' area constraints.
    :type max_area: :class:`float` | :obj:`None`
    :param move_tempfiles: Directory to perform the meshing in. If not
        provided, the meshing is performed in a temporary directory
        which is deleted automatically.
    :type move_tempfiles: :class:`str` | :obj:`None`
    :param \\*\\*kwargs: Extra keyword arguments to forward to the
        :func:`basemesh.triangle.command` function
    :type \\*\\*kwargs: :class:`dict` [:class:`str`, :obj:`typing.Any`]
    :return: The triangulated 2D mesh
    :rtype: :class:`basemesh.Mesh`
    """
    # Set up triangle flags
    if max_area is not None:
        kwargs['max_area'] = max_area
    if min_angle is not None:
        kwargs['min_angle'] = min_angle
    if regions is not None:
        kwargs['use_region_attributes'] = True
        kwargs['use_region_areas'] = True
    # Ensure at least some break lines have been provided
    extra_args = kwargs.pop('custom_args', '')
    triangle_cmd = command(**kwargs) + extra_args
    if move_tempfiles is not None:
        move_tempfiles = move_tempfiles + '/triangle_tempfiles'
    output = triangulate(nodes, segments or (), holes, regions,
                         triangle_io_dir=move_tempfiles,
                         triangle_cmd=triangle_cmd)
    return mesh_from_triangle(output, elevation=False)


def mesh_from_triangle(output: Union[str, pathlib.Path],
                       elevation: Union[int, bool] = False) -> Mesh:
    """Convert a Triangle triangulation to a BASEmesh Mesh instance.

    The path provided is expected to be the stem of the Triangle
    output, without extension.

    If `elevation` is either False or zero, the triangulation is
    assumed to be two-dimensional, and the generated mesh will have an
    elevation of zero everywhere.

    If `elevation` is a positive integer (with a boolean True being
    interpreted as a 1), the Nth node attribute is used as the node
    elevation (1 being the first attribute, these are not indices).

    :param output: Triangle output to process
    :type output: :class:`str` | :class:`pathlib.Path`
    :param elevation: Position of the node elevation in the node's
        attribute list. A value less than 1 or False are interpreted as
        the node being 2D and not having any elevation.
    :type elevation: :class:`int` | :class:`bool`
    :return: Mesh instance
    :rtype: :class:`Mesh`
    """
    if not isinstance(output, pathlib.Path):
        output = pathlib.Path(output)
    # Convert elevation to a non-negative integer if necessary
    if isinstance(elevation, bool):
        elevation = 1 if elevation else 0
    if elevation < 1:
        elevation = 0
    node_gen, element_gen = read_output(output)
    return _mesh_from_triangle_results(node_gen, element_gen, elevation)


def _mesh_from_triangle_results(node_gen: Iterator[Node],
                                element_gen: Iterator[Element],
                                elevation: int) -> Mesh:
    # Map of Triangle node IDs to mesh node instancse
    nodes: Dict[int, MeshNode] = {}
    mesh = Mesh()
    for node in node_gen:
        # Get node elevation if specified and available
        if elevation and len(node.attributes) >= elevation:
            elev = node.attributes[elevation - 1]
        else:
            elev = 0.0
        nodes[node.id] = mesh.add_node((node.pos_x, node.pos_y, elev), None)
    for element in element_gen:
        element_nodes = tuple(nodes[nid] for nid in element.nodes)
        mesh.add_element(element_nodes, None, *element.attributes)
    return mesh
