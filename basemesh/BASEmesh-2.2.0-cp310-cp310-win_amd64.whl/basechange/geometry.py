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

"""Channel geometry components and supporting code.

This module defines the Vertex, CrossSection, and ChannelGeometry
classes used by the channel generation utility.
"""

import collections
import copy
import warnings
from typing import Any, Dict, Iterable, List, Optional, Tuple

from basemesh import (Mesh, elevation_mesh, interpolate_mesh, quality_mesh,
                      triangle)
from basemesh._algorithms import rotate_2d
from basemesh.errors import BasemeshWarning
from basemesh.types import Line3D, Point2D, Point3D


class Vertex:
    """A single vertex used to define a channel cross section.

    Vertices live in the cross section's local coordinate system, with
    the X axis pointing right and the Y axis pointing up for an
    observer facing downstream. The origin lies in the leftmost vertex
    for a given cross section.

    In addition to its relative location, a vertex also may have a
    constraint associated with it. This can be any object supporting
    equality checks and will be used to dynamically create break lines
    between two cross sections.

    See the :meth:`CrossSection.process_constraints()` method for
    details on the constraint system.

    Attributes
    ----------
    pos : Tuple[Tuple[float, float], Tuple[float, float]]
        The cross-section-relative position of the vertex.
    constraint : Any
        An object used to generate break lines to neighbouring cross
        sections.

    """

    def __init__(self, pos_x: float, pos_y: float,
                 constraint: Any = None) -> None:
        self.pos: Point2D = (pos_x, pos_y)
        self.constraint: Any = constraint

    def __repr__(self) -> str:
        return f'<Vertex at {self.pos}>'

    def to_world_coords(self, anchor: Point3D, angle: float = 0.0) -> Point3D:
        """Convert the vertex position to world space coordinates.

        This performs the translation between the local cross section
        coordinate system and the global coordinate system.

        Parameters
        ----------
        anchor : Point3D
            The leftmost point in the cross section. This point acts as
            the origin for the cross section's local CRS. Any height
            offsets for the cross sections should be included in this
            point's Z offset.
        angle : float, optional
            The global angle of the given cross section, by default
            0.0.

        Returns
        -------
        Tuple[float, float, float]
            The global world space position of the vertex.
        """
        pos = anchor[0] + self.pos[0], anchor[1]
        # Rotate the vertex around the anchor, if needed
        if angle != 0.0:
            pos = rotate_2d(pos, angle, (anchor[0], anchor[1]))
        # Calculate the elevation of the vertex
        elevation = anchor[2] + self.pos[1]
        return tuple(round(f, 12) for f in (*pos, elevation))


class CrossSection:
    """A cross section making up a channel geometry.

    A cross section's vertices are defined relative to its origin. When
    looking at a cross section from the front (i.e. in river flow
    direction), the first coordinate (X) will point to the right, with
    the second (Y) pointing up.
    This means that the Y coordinate in the cross section's coordinate
    system will map to the Z coordinate (elevation) in the global
    coordinate system.

    Depending on the data provided to the :class:`CrossSection`
    instance, there exist multiple ways to convert its local coordinate
    system into the global CRS.

    :meth:`position_relative()` will position the cross section
    relative to a previous cross section using the difference in the
    :attr:`distance_coord` attribute for distance, as well as the
    respective cross sections' :attr:`angle` attributes.

    For cross sections with absolute positioning information available
    through their :attr:`anchor` attribute, you can alternatively use
    :meth:`position_absolute()`, which will use the global position
    to position the cross section while ignoring :attr:`distance_coord`
    altogether. This is analogous to the ``left_point_global_coord``
    field in the BASEchain geometry (BMG) format.

    Attributes
    ----------
    name : str
        A unique name used to identify this cross section.
    vertices : List[Vertex]
        The list of vertices defined for this cross section.
    flow_axis_coord : float
        The absolute downstream positioning of the cross section along
        the river flow axis

        .. seealso::
            :attr:`distance_coord`
    flow_axis_shift : float, optional
        Relative position of the river flow axis within the cross
        section as a real value between 0.0 and 1.0. This is used to
        generate the river flow axis polyline, as well as to improve
        the relative positioning of cross sections, by default 0.5
    anchor : Optional[Point2D], optional
        The absolute position of the first (i.e. leftmost) vertex in
        the cross section, used as the origin of the cross section's
        local coordinate system. This value is used for absolute
        positioning of the cross section.

        .. seealso::
            :attr:`angle`
    reference_height : float, optional
        An elevation offset applied to all node elevations, by default
        0.0
    angle : float, optional
        The angle of the cross section as measured counter-clockwise
        with the cross section anchor point as the pivot. This angle is
        relative to the global coordinate system, with an angle of 0°
        corresponding to a cross section facing the global ``(0, 1)``
        vector, by default 0.0
    sternberg : float, optional
        Sternberg factor for the reduction of volume by abrasion, by
        default 0.0
    bed_form_factor : float, optional
        Factor considering the influence of bed forms on bottom shear
        stress (ripple factor). This factor reduces the bottom shear
        stress due to bedforms with a constant value. If this factor is
        set to 1.0 (default), there is no influence and the standard
        shear stress is used, by default 1.0
        .. seealso:: :attr:`theta_critic`
    theta_critic : float, optional
        User-defined dimensionless critical bottom shear stress
        (Shields parameter) for this cross section. If specified, this
        local theta critic is used for this cross section. Permissible
        values range from 0.0 to 1.0. Set to a negative value to use
        the standard theta critical as defined in the
        ``BEDLOAD_PARAMETER`` block, by default -1.0
        .. seealso:: :attr:`bed_form_factor`
    friction_calibration_factor : float, optional
        Calibration factor between 0.0 and 10.0 to locally modify the
        friction value for this cross section, by default 1.0
    default_friction : Optional[float], optional
        Default Strickler friction value to use for this cross section,
        by default None
    friction_slices : Optional[List[Tuple[int, int]]], optional
        The edge indices to which to apply the coefficients defined
        in :attr:`friction_coefficients`, by default None
    friction_coefficients : Optional[List[float]], optional
        Strickler values to apply to the segments in the groups defined
        in :attr:`friction_ranges` or :attr:`friction_slice_indexes`
        respectively, by default None
    interpolation_fixpoints : List[int], optional
        The interpolation fixpoints are used to specify break lines
        in-between existing cross sections. This can be used to insert
        new cross sections, as well as to improve the quality of a 2D
        mesh export.

        The first and last node in a cross section are always
        connected. Nodes are numbered starting at 1, by default None
    table_fixed_points : List[float], optional
        Fixed points which should be included in the table calculation.
        Note that these values are only used if you use lookup tables
        for hydraulic properties (see ``SECTION_COMPUTATION`` in the
        BASEMENT command file documentation for details), by default
        None
    table_fixed_lower_limit : float, optional
        Allows to fix the lowest water surface elevation used in the
        lookup table for ``A(z)`` to a different value than the lowest
        elevation in the cross section. This option is useful if you
        include a deep lake in your model containing a large water
        volume not participating in the dynamics of your river system,
        by default None
    active_slice : Optional[Tuple[int, int]], optional
        This range defines the active part of the cross section and
        must span from the left to the right dike. If not specified,
        the whole cross section is assumed to be active, and the
        elevation of the first and last point will be assumed to
        correspond to the dike elevation, by default None
    bottom_slice : Optional[Tuple[int, int]], optional
        Range defining the span of the bottom/bedload active zone, by
        default None
    main_channel_slice : Optional[Tuple[int, int]], optional
        Range defining the span of the main channel. Everything outside
        of the main channel is treated as floodplain. If not defined,
        the whole cross section is assumed to belong to the main
        channel, by default None
    water_flow_slice : Optional[Tuple[int, int]], optional
        Used to limit the part of the part of the cross section that
        will be used for solving of the momentum equation, the rest of
        the cross section is considered to be only storage area in the
        continuity equation. By default, the whole cross section area
        is flowing.

        Avoid defining storage areas in the main channel as this can
        cause instability if only the non-flowing part of the channel
        is wetted.

        Additionally, the non-flowing areas are not taken into account
        for sediment deposition and erosion, by default None
    soil_defs : Dict[int, Tuple[int, int]], optional
        A dictionary mapping soil definition indices to their edge's
        slice index.

    """

    def __init__(self, name: str,
                 vertices: Optional[Iterable[Vertex]] = None) -> None:
        self.name = name
        self.vertices: List[Vertex] = (
            [] if vertices is None else list(vertices))
        self.flow_axis_coord: float = 0.0
        self.flow_axis_shift: float = 0.5

        self.anchor: Optional[Point2D] = None
        self.reference_height: float = 0.0
        self.angle: float = 0.0

        self.sternberg: float = 0.0
        self.bed_form_factor: float = 1.0
        self.theta_critic: float = -1.0

        self.friction_calibration_factor: float = 1.0
        self.default_friction: Optional[float] = None
        self.friction_slices: Optional[List[Tuple[int, int]]] = None
        self.friction_coefficients: Optional[List[float]] = None

        self.interpolation_fixpoints: Optional[List[int]] = None
        self.table_fixed_points: Optional[List[float]] = None
        self.table_fixed_lower_limit: Optional[float] = None

        self.active_slice: Optional[Tuple[int, int]] = None
        self.bottom_slice: Optional[Tuple[int, int]] = None
        self.main_channel_slice: Optional[Tuple[int, int]] = None
        self.water_flow_slice: Optional[Tuple[int, int]] = None

        self.soil_defs: Dict[int, Tuple[int, int]] = {}

    @property
    def distance_coord(self) -> float:
        """Distance coord of the cross section.

        Measured up- to downstream, the unit is kilometres.

        .. seealso::
            :attr:`flow_axis_coord`

        """
        return self.flow_axis_coord / 1000.0

    @distance_coord.setter
    def distance_coord(self, value: float) -> None:
        """Setter for :attr:`distance_coord`."""
        self.flow_axis_coord = value * 1000.0

    @property
    def flow_axis(self) -> Point2D:
        """Return the 2D point defining the cross section's flow axis.

        The returned point is given in the local coordinate system.
        """
        origin = self.vertices[0].pos
        return origin[0] + self.length*self.flow_axis_shift, 0.0

    @property
    def geo_referenced(self) -> bool:
        """Whether the cross section is georeferenced.

        If True, the cross section can be converted back into a list of
        3D coordinates using the :meth:`position_absolute()` method.
        """
        return self.anchor is not None

    @property
    def length(self) -> float:
        """Return the length of the cross section."""
        return self.vertices[-1].pos[0] - self.vertices[0].pos[0]

    @property
    def span(self) -> float:
        """Like :attr:`length` but includes first point offset.

        If the first point in the cross section has a non-zero X
        coordinate, this will be included in the cross section's span,
        but not its length.
        """
        return self.vertices[-1].pos[0]

    def clone(self, deep_copy: bool = False) -> 'CrossSection':
        """Return a duplicate of the current cross section.

        Since cross sections also define their relative location in the
        global world space, re-using them is prone to cause issues as
        they both refer to the same reference.

        You can use this method to create a clone of a cross section,
        which will copy the set of vertices and distance constraints.

        By default, this will keep the same vertex objects and only
        update the mutable list containing them. For a proper deep
        copy, set the "deep_copy" argument to True.

        Parameters
        ----------
        deep_copy : bool, optional
            By default, internal objects like the Vertex instances or
            their constraints are not copied, only referenced in a new
            list. Set this flag to True to perform a deep copy instead.

        Returns
        -------
        CrossSection
            A copy of the current cross section.

        """
        if deep_copy:
            return copy.deepcopy(self)
        return copy.copy(self)

    def position_absolute(self) -> List[Point3D]:
        """Position the cross section in 3D space.

        This method positions cross sections using their absolute
        position information.

        .. seealso::
            :meth:`position_relative`

        Raises
        ------
        RuntimeError
            Raised if no absolute positioning information has been
            provided for this cross section.

        Returns
        -------
        List[Tuple[float, float, float]]
            The converted vertices in the global coordinate system.

        """
        if self.anchor is None:
            raise RuntimeError(
                'Unable to generate absolute position for Cross section '
                f'{self.name}: no anchor defined; this likely means that '
                'left_point_global_coords is not defined for the associated '
                'BMG')
        anchor_3d = *self.anchor, self.reference_height
        return [v.to_world_coords(anchor_3d, self.angle)
                for v in self.vertices]

    def position_relative(self) -> List[Point3D]:
        """Position the cross section in 3D space.

        This method positions cross sections relative to a previous
        cross section.

        .. seealso::
            :meth:`position_absolute`

        Returns
        -------
        List[Tuple[float, float, float]]
            The converted vertices in the global coordinate system.

        """
        # Get the flow axis position for the current section
        flow_axis = self.flow_axis_coord, 0.0
        # Get the current section's anchor point
        offset = self.span - self.length + self.length*self.flow_axis_shift
        anchor = flow_axis[0], flow_axis[1] - offset
        # Position the current section's vertices based on this anchor
        return [v.to_world_coords((*anchor, self.reference_height), 90.0)
                for v in self.vertices]

    def limit_coordinate_precision(self, decimals: int) -> None:
        """Limit all coordinates to `decimals` decimal places.

        This function is destructive and mutates the vertices in-place.

        Paramters
        ---------
        decimals : int
            The number of decimal places to round coordinates to.
        """
        # Round vertices
        for vertex in self.vertices:
            pos_x, pos_y = vertex.pos
            vertex.pos = round(pos_x, decimals), round(pos_y, decimals)
        # Round anchor point
        if self.anchor is not None:
            pos_x, pos_y = self.anchor
            self.anchor = round(pos_x, decimals), round(pos_y, decimals)

    def process_constraints(self, other: 'CrossSection'
                            ) -> List[Tuple[int, int]]:
        """Generate the break lines between two cross sections.

        This will find any vertices that have matching constraints
        across the two cross sections. These vertices are then returned
        as pairs of indices representing the vertex in the first and
        second cross section.

        Parameters
        ----------
        other : CrossSection
            The next cross section in the channel. The break lines will
            be generated between that cross section and the current
            instance (i.e. self).

        Returns
        -------
        List[Tuple[int, int]]
            A list of pairs of indices representing the vertices to
            connect via break lines.
        """
        connections: List[Tuple[int, int]] = []
        for idx_a, vtx_a in enumerate(self.vertices):
            try:
                constraints_a = set(vtx_a.constraint)
            except TypeError:
                constraints_a = {vtx_a.constraint}
            for idx_b, vtx_b in enumerate(other.vertices):
                try:
                    constraints_b = set(vtx_b.constraint)
                except TypeError:
                    constraints_b = {vtx_b.constraint}
                if vtx_a.constraint != vtx_b.constraint:
                    if not set(constraints_a).intersection(set(constraints_b)):
                        continue
                if vtx_a.constraint is None or vtx_b.constraint is None:
                    continue
                connections.append((idx_a, idx_b))
        return connections

    def range_to_slice(self, range_: Tuple[float, float]) -> Tuple[int, int]:
        """Convert a range into explicit slice indices."""
        x_coords = [v.pos[0] for v in self.vertices]
        return x_coords.index(range_[0]), x_coords.index(range_[1])


class ChannelGeometry:
    """A BASEchange channel geometry.

    Channel geometries consist of any number of flat, two-dimensional
    cross sections. These cross sections use a local coordinate system
    for their nodes, which is translated into world coordinate system
    as needed.

    Attributes
    ----------
    name : str
        The name of the model. Used to generate custom file names;
        helpful when working with multiple geometries.
    cross_sections : List[CrossSection]
        The list of cross sections defining the channel geometry.
    """

    def __init__(self, name: str = 'Unnamed model',
                 cross_sections: Optional[Iterable[CrossSection]] = None
                 ) -> None:
        self.name = name
        self.cross_sections: List[CrossSection] = (
            [] if cross_sections is None else list(cross_sections))

    def add_cross_section(self, cross_section: CrossSection,
                          insert_at: int = -1) -> None:
        """Add an existing cross section to the channel.

        The optional index argument may be used to specify the index to
        insert the channel at. An insertion index of 2 means that the
        new index 2 will be the inserted element, with all following
        sections (including the original index 2) being shifted by 1.

        Parameters
        ----------
        section : CrossSection
            An existing cross section to add to the channel.
        insert_at : int, optional
            The index to insert the section at, by default -1.
        """
        if insert_at < 0:
            self.cross_sections.append(cross_section)
        else:
            self.cross_sections.insert(insert_at, cross_section)

    def new_cross_section(self, name: str, nodes: Iterable[Vertex],
                          insert_at: int = -1) -> CrossSection:
        """Create and add a new cross section to the channel.

        The optional index argument may be used to specify the index to
        insert the channel at. An insertion index of 2 means that the
        new index 2 will be the inserted element, with all following
        sections (including the original index 2) being shifted by 1.

        Parameters
        ----------
        name : str
            The unique name of the cross section
        nodes : Iterable[Vertex]
            Any number of vertices to create the cross section from.
        insert_at : int, optional
            The index to insert the section at, by default -1.
        """
        cs_ = CrossSection(name, nodes)
        self.cross_sections.insert(insert_at, cs_)
        return cs_

    def remove_cross_section(self, index: int) -> CrossSection:
        """Remove and return a cross section from the channel.

        Parameters
        ----------
        index : int
            The index of the cross section to remove.
        """
        return self.cross_sections.pop(index)

    def to_mesh(self, absolute_pos: bool = False, **kwargs: Any) -> Mesh:
        """Export the channel geometry as a mesh object.

        This converts the channel geometry into a BASEmesh Mesh
        instance that can then be saved for use in BASEMENT.
        """
        # Convert cross sections to 3D line strings
        nodes: List[List[Point3D]] = []
        discarded = 0

        section_nodes: Dict[Point2D, float] = collections.OrderedDict()
        for cs_ in self.cross_sections:
            if absolute_pos:
                section_pos = cs_.position_absolute()
            else:
                section_pos = cs_.position_relative()

            for *vtx, elev in section_pos:
                pos: Point2D = tuple(vtx)
                if pos in section_nodes:
                    discarded += 1
                    other_elev = section_nodes[pos]
                    if elev > other_elev:
                        section_nodes[pos] = elev
                else:
                    section_nodes[pos] = elev

            nodes.append([(*k, v) for k, v in section_nodes.items()])
            section_nodes.clear()
        if discarded > 0:
            warnings.warn(f'{discarded} nodes were discarded; note that 2D '
                          'meshes cannot describe vertical walls',
                          BasemeshWarning)
        # Process constraints
        break_lines: List[Line3D] = []
        for index, this_cs in enumerate(self.cross_sections[:-1]):
            # Add cross section break line
            for vtx_i in range(len(nodes[index])-1):
                break_lines.append(
                    (nodes[index][vtx_i], nodes[index][vtx_i+1]))
            # Add side borders
            break_lines.append((nodes[index][0], nodes[index+1][0]))
            break_lines.append((nodes[index][-1], nodes[index+1][-1]))
            # Process constraints
            next_cs = self.cross_sections[index+1]
            constraints = this_cs.process_constraints(next_cs)
            for con_a, con_b in constraints:
                line = nodes[index][con_a], nodes[index+1][con_b]
                break_lines.append(line)
        break_lines.append((nodes[-1][0], nodes[-1][-1]))

        # Generate Triangle input geometries
        channel_nodes = [n for c in nodes for n in c]
        triangle_nodes: Dict[Tuple[float, float], triangle.Node] = {
            n[:2]: triangle.Node(i+1, *n)
            for i, n in enumerate(channel_nodes)}
        triangle_segments: List[triangle.Segment] = []
        for index, points in enumerate(break_lines):
            node_ids = [triangle_nodes[p[:2]].id for p in points]
            triangle_segments.append(
                triangle.Segment(index+1, node_ids[0], node_ids[1]))

        # Generate meshes
        em_ = elevation_mesh(
            triangle_nodes.values(), segments=triangle_segments)
        qm_ = quality_mesh(
            triangle_nodes.values(), segments=triangle_segments, **kwargs)
        interpolate_mesh(qm_, em_)
        return qm_
