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

"""Mesh interpolation tool."""

from typing import Callable, Dict, Optional

from .abc import ElevationSource
from ._mesh import Mesh
from .types import Triangle2D, Point2D

# Type aliases
_Feedback = Callable[[float], None]
_TriangleSampler = Callable[[Triangle2D], Point2D]


def calculate_element_elevation(mesh: Mesh, *args: ElevationSource,
                                default: Optional[float] = None,
                                sampler: Optional[_TriangleSampler] = None,
                                feedback: Optional[_Feedback] = None,
                                ) -> Dict[int, float]:
    """Calculate and add the element elevation attributes to the mesh.

    This calculates mesh element elevations using a given element
    sampler. The mesh is only used to retrieve the 2D element
    positions, the node elevation is ignored when determining the
    element elevation.

    :param mesh: The mesh to calculate the element elevations for
    :type mesh: :class:`Mesh`
    :param \\*args: Any number of elevation sources to use in
        descending order of priority, at least one is required
    :type \\*args: :class:`basemesh.abc.ElevationSource`
    :param default: A fallback value used when no elevation source
        could produce a value for a given point, defaults to None
    :type default: :class:`float` | :obj:`None`
    :param sampler: A callable taking a triangle and returning a point
        within that triangle, defaults to center of mass
    :type sampler: ((pt1, pt2, pt3)) -> pt | :obj:`None`
    :param feedback: A callable taking values between 0 and 1
        indicating the progress of the operation, defaults to None
    :type feedback: (float) -> None | :obj:`None`
    :return: A dictionary mapping element IDs to their elevation
    :rtype: :class:`dict` [:class:`int`, :class:`float`]
    :raises ValueError: Raised if every elevation source has failed and
        no default value was provided
    """
    if not args:
        return {e.id: 0.0 for e in mesh.elements}

    def triangle_com(triangle: Triangle2D) -> Point2D:
        """Calculate a 2D triangle's centre of mass."""
        avg_x = (triangle[0][0] + triangle[1][0] + triangle[2][0]) / 3.0
        avg_y = (triangle[0][1] + triangle[1][1] + triangle[2][1]) / 3.0
        return avg_x, avg_y

    if sampler is None:
        sampler = triangle_com

    total = len(mesh.elements)
    interval = int(total / 100) if total > 100 else 1

    # Iterate over all elements in the input mesh
    result_dict: Dict[int, float] = {}
    for index, element in enumerate(mesh.elements):
        sample_point: Point2D = sampler(element.as_triangle_2d)
        elevation = _get_elevation(sample_point, *args, default=default)
        if elevation is None:
            raise ValueError(
                'No elevation source could provide a height value for '
                f'element {element.id} at {sample_point} and no default '
                'value was given.')

        # NOTE: It would be possible to introduce an elevation attribute to the
        # Element object, but this would be confusing considering that node and
        # element elevations are not directly linked or inferrable.
        # To resolve this ambiguity, we would have to add a custom mesh
        # sub class that has only elevation attributes and no node elevation.
        #
        # However, due to the sampler system, this would tie the mesh object to
        # its defining elevation sources, so those would have to stick around
        # as long as the mesh does so we can re-calculate the elevations if the
        # nodes are moved.
        #
        # That too could be mitigated by making this mesh type immutable, but
        # at that point we'd lose mesh editing capability and add a lot of
        # complexity to the object model for no justifiable reason. Therefore,
        # we just calculate the element elevations into a dict and sprinkle
        # them into the 2DM during export.
        #
        # -- LS

        # Record the elevation for this point
        result_dict[element.id] = elevation

        if feedback is not None and index % interval == 0:
            feedback(index/total)

    if feedback is not None:
        feedback(1.0)
    return result_dict


def interpolate_mesh(mesh: Mesh, *args: ElevationSource,
                     default: Optional[float] = None,
                     feedback: Optional[_Feedback] = None) -> None:
    """Interpolate a mesh using the provided elevation sources.

    This operation modifies the input mesh.

    :param mesh: The mesh to interpolate
    :type mesh: :class:`Mesh`
    :param \\*args: Any number of elevation sources to use in descending
        order of priority, at least one is required
    :type \\*args: :class:`basemesh.abc.ElevationSource`
    :param default: A fallback value used when no elevation source
        could produce a value for a given point, defaults to None
    :type default: :class:`float` | :obj:`None`
    :param feedback: A callable taking values between 0 and 1
        indicating the progress of the operation, defaults to None
    :type feedback: (float) -> None | :obj:`None`
    :raises ValueError: Raised if every elevation source has failed and
        no default value was provided
    """
    if not args:
        return None

    total = len(mesh.nodes)
    interval = int(total / 100) if total > 100 else 1

    # Iterate over all nodes in the input mesh
    for index, node in enumerate(mesh.nodes):
        sample_point = node.pos[:2]
        elevation = _get_elevation(sample_point, *args, default=default)
        if elevation is None:
            raise ValueError(
                'No elevation source could provide a height value for '
                f'node {node.id} at {sample_point} and no default value '
                'was given.')

        # Move the node to the new elevation
        node.move(z=elevation)
        if feedback is not None and index % interval == 0:
            feedback(index/total)

    if feedback is not None:
        feedback(1.0)


def _get_elevation(point: Point2D, *args: ElevationSource,
                   default: Optional[float] = None) -> Optional[float]:
    height: Optional[float] = None
    # Loop over all elevation sources
    for source in args:
        try:
            # Try to get an elevation from the current source. The
            # ElevationSource ABC requires that a ValueError be raised if
            # the source is unable to produce a value.
            height = source.elevation_at(point)
        except ValueError:
            # If no value could be returned, move on to the next elevation
            # source
            pass
        else:
            # The elevation source provided a height value, quit the loop
            break
    if height is None and default is not None:
        height = default
    return height
