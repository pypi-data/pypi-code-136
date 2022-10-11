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

"""Core components of the mesh generator."""

from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Dict, List, Tuple

from basemesh import (Mesh, Segment, Vertex, interpolate_mesh, quality_mesh,
                      resolve_string_defs, triangle)
from basemesh.abc import ElevationSource
from basemesh.types import Point2D


class Node(Vertex):
    """Alias for :class:`basemesh.Vertex`."""


class AbstractFactory(ElevationSource, metaclass=ABCMeta):
    """Base class for mesh factories.

    This provides two main endpoints for generating meshes. The first
    is to subclass this method and override the :meth:`elevation_at`
    name with a custom method.

    The second is to assign any callable as the elevation function
    using the set_elevation_func method. The callable provided must
    have the same signature as the :meth:`elevation_at`
    method itself: ``(float, float) -> float``.
    """

    def __init__(self) -> None:
        self.nodes: List[Node] = []
        self.segments: List[Segment] = []

        self.holes: List[triangle.HoleMarker] = []
        self.regions: List[triangle.RegionMarker] = []
        self.string_defs: Dict[str, List[Node]] = {}

    def build(self, max_area: float = -1.0, min_angle: float = 28.0,
              **kwargs: Any) -> Tuple[Mesh, Dict[str, List[int]]]:
        """Generate and return a mesh using the given inputs.

        This first calls 'Triangle' to generate quality mesh before
        repeatedly calling the elevation function and interpolating
        the mesh nodes.

        :param max_area: Global maximum area constraint.
        :type max_area: :class:`float`
        :param min_angle: Global minimum angle constraint.
        :type min_angle: :class:`float`
        :param \\*\\*kwargs: Additional keyword arguments to forward to
            the :func:`basemesh.quality_mesh` function.
        :type \\*\\*kwargs: :obj:`typing.Any`
        :return: A tuple containing the mesh and a dictionary of
            string definitions.
        :rtype: :class:`tuple` [
            :class:`basemesh.Mesh`,
            :class:`dict` [:class:`str`, :class:`list` [:class:`int`]]]
        """
        triangle_nodes: Dict[Tuple[float, float], triangle.Node] = {
            n.pos[:2]: triangle.Node(i+1, *n.pos[:2])
            for i, n in enumerate(self.nodes)}
        triangle_segments: List[triangle.Segment] = []
        for index, segment in enumerate(self.segments):
            node_ids = [
                triangle_nodes[v.pos[:2]].id for v in segment.vertices]
            triangle_segments.append(triangle.Segment(index+1, *node_ids))

        # Run triangle
        mesh = quality_mesh(triangle_nodes.values(), triangle_segments,
                            self.holes, self.regions,
                            min_angle=min_angle, max_area=max_area, **kwargs)

        # Process string definitions
        if self.string_defs:
            # NOTE: The string defs are provided by the user as named lists of
            # nodes, but the parser expects point tuples.
            # This is converted here.
            sd_points = {name: tuple(n.pos[:2] for n in line_string)
                         for name, line_string in self.string_defs.items()}
            string_defs = resolve_string_defs(sd_points, mesh, 1e-6)
        else:
            string_defs = {}

        # Interpolate mesh
        # NOTE: This works because the MeshFactory class itself supports the
        # ElevationSource ABC requried for interpolation
        interpolate_mesh(mesh, self, default=-999.0)
        return mesh, string_defs

    @abstractmethod
    def elevation_at(self, point: Point2D) -> float:
        """Return the elevation of the given point.

        This method must be overridden by the user.

        :param point: The point to query.
        :type point: :class:`tuple` [:class:`float`, :class:`float`]
        :return: The elevation at the given point.
        :rtype: :class:`float`
        """
        raise NotImplementedError


class BasicFactory(AbstractFactory):
    """Basic mesh factory.

    This is a helper factory that allows the user to inject a custom
    elevation function at runtime using the :meth:`set_elevation_func`
    method.

    Overriding the original :meth:`elevation_at` method is still
    supported.

    :ivar elevation_func: The elevation function to use.
    :vartype elevation_func: :class:`collections.abc.Callable` [
        :class:`tuple` [:class:`float`, :class:`float`],
        :class:`float`]
    """

    def __init__(self) -> None:
        """Initialise the mesh factory.

        This initialiser is provided for neatness and type analysis,
        but actually calling it is not required.
        """
        super().__init__()
        self.elevation_func: Callable[[Point2D], float]

    def elevation_at(self, point: Point2D) -> float:
        """Return the elevation at a given point.

        This calls the elevation function specified using the
        :meth:`set_elevation_func` decorator.

        :param point: The point to query.
        :type point: :class:`tuple` [:class:`float`, :class:`float`]
        :return: The elevation at the given point.
        :rtype: :class:`float`
        :raises RuntimeError: If the elevation function has not been
            set.
        """
        try:
            return self.elevation_func(point)
        except AttributeError as err:
            raise RuntimeError('No elevation function defined') from err

    def set_elevation_func(self, func: Callable[[Point2D], float]) -> None:
        """Set the elevation function to use for this factory.

        This is mostly a syntactic shorthand; the following two
        statements are effectively identical:

        .. code-block:: python

           # Regular function assignment assignment
           factory = MeshFactory()
           def foo(point):
               return abs(point[0] + point[1])
           factory.set_elevation_func(foo)

           # Decorator shorthand
           factory = MeshFactory()
           @factory.set_elevation_func
           def foo(point):
               return abs(point[0] + point[1])

        :param func: The elevation function to use.
        :type func: :class:`collections.abc.Callable` [
            [:class:`tuple` [:class:`float`, :class:`float`]],
            :class:`float`]
        """
        self.elevation_func = func
