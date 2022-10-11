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

"""Implementation of the internal mesh representation for BASEmesh."""

import os
import pathlib
import warnings
from typing import Dict, Iterable, List, Optional, Set, Tuple, Union

from .abc import ElevationSource, SpatialCollection, Spatial
from ._algorithms import (dist_2d, interpolate_triangle,
                          point_in_polygon_concave, point_in_polygon_convex,
                          distance_to_polygon)
from ._containers import SpatialSet
from .errors import BasemeshWarning
from .log import logger
from .types import Point2D, Point3D, Polygon2D, Triangle2D, Triangle3D

# Load Py2DM while suppressing its C extension warning
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    import py2dm


class MeshNode(Spatial):
    """A unique point in space, defined by its coordinates and ID.

    Nodes are specific to the mesh they were defined on and may not be
    shared between meshes.
    
    They additionally track all elements they are connected to,
    allowing for deletion of elements along with their defining nodes,
    as well as efficient iteration to neighbouring elements for 
    flood-fill algorithms.

    :ivar id: The unique ID of the node. May be changed by the user as
        element connectivity is stored in references, not by ID
    :vartype id: :class:`int`
    :ivar pos: The position of the node in space. May be updated using
        the :meth:`move` method
    :vartype pos: :class:`tuple` [
        :class:`float`, :class:`float`, :class:`float`]	
    """

    __slots__ = ('_attached_elements', 'id', '_mesh', 'pos')

    def __init__(self, mesh: 'Mesh', point: Point3D, id_: int) -> None:
        """Initialise a new mesh node.

        Note that the preferred means of creating mesh nodes is the
        :meth:`Mesh.add_node` method.
        """
        self._mesh = mesh
        self.id = id_
        self.pos = point
        self._attached_elements: Set['MeshElement'] = set()

    @property
    def elements(self) -> Set['MeshElement']:
        """Return a set of mesh elements defined using this node.

        These elements in this set are also the ones that will be
        removed if this node is deleted.
        
        :type: :class:`set` [:class:`MeshElement`]
        """
        return self._attached_elements

    @property
    def mesh(self) -> 'Mesh':
        """Return the mesh this node belongs to.
        
        :type: :class:`Mesh`
        """
        return self._mesh

    @property
    def spatial_marker(self) -> Point2D:
        """Return a 2D point representing this object.

        This point will be used by space-aware containers to optimise
        memory layout.

        :type: :class:`tuple` [:class:`float`, :class:`float`]
        """
        return self.pos[:2]

    def attach_element(self, element: 'MeshElement') -> None:
        """Attach a mesh element to the mesh node.

        This is usually done by the MeshElement initialiser to ensure
        the mesh element can be deleted when its defining node is.

        :param element: The element to attach
        :type element: MeshElement
        """
        self._attached_elements.add(element)

    def detach_element(self, element: 'MeshElement') -> None:
        """Detach a mesh element from the mesh node.

        This is used to remove all references to the mesh element upon
        its deletion, allowing the garbage collector to dispose of it.

        :param element: The element to detach
        :type element: MeshElement
        """
        self._attached_elements.discard(element)

    def move(self, x: Optional[float] = None, y: Optional[float] = None,
             z: Optional[float] = None) -> None:
        """Move the node to a new location.

        Any coordinate whos argument is left at :obj:`None` will keep
        its current value. Note that this also modifies any other mesh
        entities using this node, such as elements or node strings.

        :param x: The new x coordinate
        :type x: :class:`float` | :obj:`None`
        :param y: The new y coordinate
        :type y: :class:`float` | :obj:`None`
        :param z: The new z coordinate
        :type z: :class:`float` | :obj:`None`
        """
        pos_x, pos_y, pos_z = self.pos
        if x is not None:
            pos_x = x
        if y is not None:
            pos_y = y
        if z is not None:
            pos_z = z
        self.pos = pos_x, pos_y, pos_z


class MeshElement(Spatial):
    """A triangular mesh element connecting three nodes.
    
    Elements are specific to the mesh they were defined on and may not
    be shared between meshes.
    
    Elements may have an arbitrary number of materials, which are
    general-purpose numeric attributes that can be changed at will.
    
    Canonically (and within QGIS), the first material index is used as
    the MATID of the element, with the second reserved for the
    element elevation in BASEMENT 3. Extra materials may be added and
    modified arbitrarily.

    .. note:: Note that BASEmesh requires elements to adhere to the CCW
        winding order, and will automatically flip elements that do not
        adhere to this rule.

    :ivar id: The unique ID of the element. May be changed by the user.
    :vartype id: :class:`int`
    :ivar materials: The materials tuple of the element. Immutable, but
        may be overridden by the user.
    :vartype materials: :class:`tuple` [
        :class:`float` | :class:`int`, ...]
    """

    __slots__ = ('id', 'materials', '_mesh', '_node_1', '_node_2', '_node_3')

    def __init__(self, mesh: 'Mesh',
                 nodes: Tuple[MeshNode, MeshNode, MeshNode],
                 id_: int, *materials: Union[int, float]) -> None:
        """Initialise a new mesh element.

        Note that the preferred means of creating mesh elements is the
        :meth:`Mesh.add_element` method, which will take care of
        attaching the element to its defining nodes.

        Any elements not adhering to CCW winding order will be
        reoriented as part of this call. The user should not rely on
        the node order when creating elements.
        """
        self.id = id_
        self.materials = tuple(materials)
        self._mesh = mesh
        self._node_1 = nodes[0]
        self._node_2 = nodes[1]
        self._node_3 = nodes[2]
        nodes[0].attach_element(self)
        nodes[1].attach_element(self)
        nodes[2].attach_element(self)

        # Conform the element
        # NOTE: calling point_in_polygon_convex for an inner point of the
        # triangle will only return True if the triangle uses CCW vertex order.
        if not point_in_polygon_convex(
                self.spatial_marker, self.as_triangle_2d):
            # Swapping two nodes effectively flips the entire element
            self._node_1 = nodes[1]
            self._node_2 = nodes[0]
            warnings.warn(f'Element {self.id} was flipped to ensure CCW '
                          'vertex order.', BasemeshWarning)

    @property
    def area(self) -> float:
        """Return the area of the element's 2D projection.
        
        :type: :class:`float`
        """
        p1, p2, p3 = self.as_triangle_2d
        return 0.5 * abs(p1[0] * (p2[1] - p3[1])
                         + p2[0] * (p3[1] - p1[1])
                         + p3[0] * (p1[1] - p2[1]))

    @property
    def center(self) -> Tuple[float, float, float]:
        """Return the center of mass of the mesh element.
        
        :type: :class:`tuple` [
            :class:`float`, :class:`float`, :class:`float`]
        """
        avg_x = (self.points[0][0] + self.points[1][0] + self.points[2][0]) / 3
        avg_y = (self.points[0][1] + self.points[1][1] + self.points[2][1]) / 3
        avg_z = (self.points[0][2] + self.points[1][2] + self.points[2][2]) / 3
        return avg_x, avg_y, avg_z

    @property
    def mesh(self) -> 'Mesh':
        """Return the mesh this element belongs to.
        
        :type: :class:`Mesh`
        """
        return self._mesh

    @property
    def nodes(self) -> Tuple[MeshNode, MeshNode, MeshNode]:
        """Return the nodes defining this element.
        
        :type: :class:`tuple` [
            :class:`MeshNode`, :class:`MeshNode`, :class:`MeshNode`]
        """
        return self._node_1, self._node_2, self._node_3

    @property
    def points(self) -> Triangle3D:
        """Return the tuple of points defining the mesh element.
        
        :type: :class:`tuple` [
            :class:`tuple` [:class:`float`, :class:`float`, :class:`float`],
            :class:`tuple` [:class:`float`, :class:`float`, :class:`float`],
            :class:`tuple` [:class:`float`, :class:`float`, :class:`float`]]
        """
        return tuple(n.pos for n in self.nodes)

    @property
    def as_triangle_2d(self) -> Triangle2D:
        """Return the tuple of 2D points representing this element.
        
        :type: :class:`tuple` [
            :class:`tuple` [:class:`float`, :class:`float`],
            :class:`tuple` [:class:`float`, :class:`float`],
            :class:`tuple` [:class:`float`, :class:`float`]]
        """
        return (self._node_1.spatial_marker, self._node_2.spatial_marker,
                self._node_3.spatial_marker)

    @property
    def spatial_marker(self) -> Point2D:
        """Return a 2D point representing this object.

        This point will be used by space-aware containers to optimise
        memory layout.

        :type: :class:`tuple` [:class:`float`, :class:`float`]
        """
        return self.center[0], self.center[1]

    def contains(self, point: Union[Point2D, Point3D]) -> bool:
        """Check whether the given point lies within the element.

        If a 3D point was passed, only the first two coordinates will
        be used for containment checking.

        :param point: The point to check for containment.
        :type point: :class:`tuple` [:class:`float`, :class:`float`, ...]
        :return: Whether the point lies within the element.
        :rtype: :class:`bool`
        """
        return point_in_polygon_convex(
            (point[0], point[1]), self.as_triangle_2d)

    def interpolate(self, point: Tuple[float, ...]) -> float:
        """Return the interpolated height at a given point.

        Note that the point does not have to lie within the mesh
        element for this. The element's nodes are used to define an
        infinite plane onto which the point is projected. Use the
        :meth:`contains` method to check whether a given point lies
        within the element.

        If a 3D point was passed, its elevation will be ignored. It is
        only available as an input for convenience.

        :param point: The point to interpolate at.
        :type point: :class:`tuple` [:class:`float`, :class:`float`, ...]
        :return: The interpolated height at the given point.
        """
        return interpolate_triangle((point[0], point[1]), self.points)


class Mesh(ElevationSource):
    """A two dimensional mesh with 3D nodes (aka. a 2.5D mesh).
    
    Note that this datatype currently does not verify whether a given
    pair of points is distinct in 2D space. This means that two nodes
    only differing in their elevation will be considered distinct,
    potentially leading to unexpected behaviour in downstream code.
    
    After instantiation, the mesh can be populated with nodes and
    elements using the :meth:`add_node` and :meth:`add_element`
    methods.
    
    Alternatively, a 2DM file can be loaded using the :meth:`open`
    method.
    
    :ivar node_strings: A dictionary mapping node string names to their
        respective list of nodes. May be modified by the user to udpate
        node string definitions.
    :vartype node_strings: :class:`dict` [
        :class:`str`, :class:`list` [:class:`MeshNode`]]
    """

    __slots__ = ('_elements', '_nodes', 'node_strings')

    def __init__(self) -> None:
        """Initialise a new mesh.

        A mesh instantiated manually is always empty. Use the
        :meth:`add_node` and :meth:`add_element` methods to populate
        it.
        """
        self._nodes: SpatialSet[MeshNode] = SpatialSet()
        self._elements: SpatialSet[MeshElement] = SpatialSet()
        self.node_strings: Dict[str, List[MeshNode]] = {}

    @classmethod
    def open(cls, filename: Union[str, pathlib.Path]) -> 'Mesh':
        """Read a 2DM mesh file and instantiate a mesh.

        Only ``ND``, ``E3T`` and ``NS`` mesh entities are supported.
        Any other element types are ignored with a warning.

        If no ``NUM_MATERIALS_PER_ELEMENT`` card is specified in the
        file, the material count will be inferred from the first
        element encountered and a warning will be emitted.

        :param filename: The path to the 2DM file to read.
        :type filename: :class:`str` | :class:`pathlib.Path`
        :return: The mesh defined in the file.
        :rtype: :class:`Mesh`
        """
        # Determine whether the mesh is zero-based or one-based
        zero_indexed = _is_2dm_zero_indexed(filename)
        # Some utilities do not write the "NUM_MATERIALS_PER_ELEM <NUM>" line
        # into the 2DM file. For these cases, we need to infer the material
        # count from the first element found
        try:
            material_count, nmpe_provided = _get_2dm_material_count(filename)
        except ValueError:
            material_count, nmpe_provided = 0, False
        if not nmpe_provided:
            warnings.warn('2DM file did not contain a NUM_MATERIALS_PER_ELEM '
                          'line. Material count was inferred from first '
                          f'element encountered: {material_count}',
                          BasemeshWarning)

        mesh = cls()
        # Py2DM only allows one-based, consecutive ID orderings for the default
        # reader, so we can use a list to store references to the created
        # objects.
        nodes: List[MeshNode] = []
        with py2dm.Reader(str(filename), materials=material_count,
                          zero_index=zero_indexed) as reader:

            for node in reader.iter_nodes():
                nodes.append(mesh.add_node(node.pos, id_=node.id))

            for element in reader.iter_elements():
                if not isinstance(element, py2dm.Element3T):
                    warnings.warn(
                        f'Ignoring unsupported element type {element.card} '
                        'in 2DM file', BasemeshWarning)
                    continue

                ele_nodes = tuple((nodes[node_id-int(not zero_indexed)]
                                   for node_id in element.nodes))
                mesh.add_element(ele_nodes, element.id, *element.materials)

            for node_string in reader.iter_node_strings():
                if node_string.name is None:
                    starting_nodes = ','.join(map(str, node_string.nodes[:3]))
                    warnings.warn(
                        f'Node string starting with node IDs {starting_nodes} '
                        'does not have a named identifier after its final '
                        'node. The node string will be skipped.',
                        BasemeshWarning)
                    continue

                node_string_nodes = [nodes[n - int(not zero_indexed)]
                                     for n in node_string.nodes]
                mesh.add_node_string(node_string.name, node_string_nodes)

        # Bump all IDs up by one if the mesh is zero-based
        if zero_indexed:
            for node in mesh.nodes:
                node.id += 1
            for element in mesh.elements:
                element.id += 1
            warnings.warn(f'Zero-indexed 2DM file encountered: {filename}\n'
                          'All node and element IDs in the  mesh have been '
                          'shifted up by 1', BasemeshWarning)
        return mesh

    @property
    def elements(self) -> SpatialCollection[MeshElement]:
        """Return the mesh elements making up the mesh.
        
        :return: A spatial container over the mesh elements.
        :rtype: :class:`abc.SpatialCollection` [:class:`MeshElement`]
        """
        return self._elements

    @property
    def nodes(self) -> SpatialCollection[MeshNode]:
        """Return the mesh nodes defining its elements.

        Note that the mesh nodes are also available through the mesh
        elements via :attr:`MeshElement.nodes`, which may be faster
        than manually associating nodes and elements.
        """
        return self._nodes

    def add_node(self, point: Point3D, id_: Optional[int] = None) -> MeshNode:
        """Create a new node for the mesh.

        If no mesh ID was provided, a new mesh ID will be chosen based
        on existing nodes in the mesh.

        :param point: The 3D point defining the node.
        :type point: :class:`tuple` [
            :class:`float`, :class:`float`, :class:`float`]]
        :param id_: The mesh ID of the node.
        :type id_: :class:`int` | :class:`None`
        :return: The newly created node that was added to the mesh.
        :rtype: :class:`MeshNode`
        """
        if id_ is None:
            id_ = self._get_node_id()
        node = MeshNode(self, point, id_)
        self._nodes.add(node)
        return node

    def add_element(self,
                    nodes: Union[Tuple['MeshNode', 'MeshNode', 'MeshNode'],
                                 Tuple[Point3D, Point3D, Point3D]],
                    id_: Optional[int], *materials: Union[int, float]
                    ) -> MeshElement:
        """Add a new element using the given mesh nodes.

        If the given nodes are points, the mesh will be searched for
        existing nodes that match the given points. If no matching
        nodes are found, new nodes will be created.

        If no element ID has been provided, one will be selected based
        on existing elements.

        :param nodes: The nodes defining the element.
        :type nodes: :class:`tuple` [
            :class:`MeshNode`, :class:`MeshNode`, :class:`MeshNode`]
        :param id_: The mesh ID of the element.
        :type id_: :class:`int` | :class:`None`
        :param \\*materials: The material IDs of the element.
        :type \\*materials: :class:`int` | :class:`float`
        :return: The newly created element that was added to the mesh.
        :rtype: :class:`MeshElement`
        :raises ValueError: If the given nodes are node instances
            belonging to a different mesh.
        """
        element_nodes: List[MeshNode] = []
        for node in nodes:
            if isinstance(node, MeshNode):
                # If the node is part of the mesh, re-use it
                if node in self.nodes:
                    element_nodes.append(node)
                # If it isn't, raise an error (no cross-meshing yet)
                else:
                    raise ValueError(
                        f'Attempted to define element {id_} using nodes from '
                        'a different mesh instance')
            else:
                # If the node is a tuple of floats, look for an existing node
                # with the same coordinates
                try:
                    found_node = self.node_at(node)
                except ValueError:
                    # If it doesn't exist yet, create a new node
                    new_node = MeshNode(self, node, self._get_node_id())
                    self._nodes.add(new_node)
                    element_nodes.append(new_node)
                else:
                    # If it does, add the existing mesh node instead
                    element_nodes.append(found_node)

        # Ensure our three nodes span a triangle (i.e. don't coincide)
        if len(set(n.spatial_marker for n in element_nodes)) < 3:
            warnings.warn(
                f'At least two of the nodes of element {id_} coincide. The '
                'element has no effective area.', BasemeshWarning)

        # Create a new element
        if id_ is None:
            id_ = self._get_element_id()
        nodes_tuple: Tuple[MeshNode, MeshNode, MeshNode] = (
            tuple(element_nodes))
        element = MeshElement(self, nodes_tuple, id_, *materials)
        self._elements.add(element)
        return element

    def add_node_string(self, name: str, nodes: Iterable[MeshNode]) -> None:
        """Add a new node string using the given mesh nodes.

        If the given nodes are not part of the current mesh, an error
        will be raised.

        :param name: The name of the node string.
        :type name: :class:`str`
        :param nodes: The nodes defining the node string.
        :type nodes: :class:`collections.abc.Iterable` [
            :class:`MeshNode`]
        :raises KeyError: If the given node string name is already in
            use in this mesh.
        :raises ValueError: If the given nodes are not part of the
            current mesh.
        """
        if name in self.node_strings:
            raise KeyError(f'A node string with name "{name}" already exists '
                           'for this mesh')
        for node in nodes:
            if node.mesh != self:
                raise ValueError(
                    f'Attempted to define node string "{name}" using nodes '
                    'from a different mesh instance')
        self.node_strings[name] = list(nodes)

    def element_at(self, point: Union[Point2D, Point3D]) -> MeshElement:
        """Return the element containing the given point.

        If the point lies outside of any mesh elements, a
        :class:`ValueError` is raised.

        If a 3D point is passed, only the first two coordinates will be
        used for containment checking.

        :param point: The point to find the containing element for.
        :type point: :class:`tuple` [
            :class:`float`, :class:`float`, ...]
        :return: The element containing the given point.
        :rtype: :class:`MeshElement`
        :raises ValueError: If the point is not contained in any mesh
            element.
        """
        for element in self.elements.iter_spatial((point[0], point[1])):
            if element.contains(point):
                return element
        raise ValueError(f'Point {point} does not lie within any mesh element')

    def elements_by_polygon(self, polygon: Polygon2D,
                            check_midpoints: bool = True) -> List[MeshElement]:
        """Return any elements contained in the given polygon.

        Disabling the `check_midpoints` flag will cause every corner
        point of the element to be checked instead, which will triple
        the workload.

        :param polygon: The polygon to check for element containment.
        :type polygon: :class:`tuple` [
            :class:`tuple` [:class:`float`, :class:`float`], ...]
        :param check_midpoints: Whether to check the midpoint of each
            element instead of its corners.
        :type check_midpoints: :class:`bool`
        :return: The elements contained in the given polygon.
        :rtype: :class:`list` [:class:`MeshElement`]
        """
        # Simple check: centroids only
        if check_midpoints:
            return [e for e in self.elements if point_in_polygon_concave(
                    (e.center[0], e.center[1]), polygon)]
        # Advanced check: all element vertices must be contained
        return [e for e in self.elements
                if all(point_in_polygon_concave(n.pos[:2], polygon)
                       for n in e.nodes)]

    def elevation_at(self, point: Union[Point2D, Point3D]) -> float:
        """Return the interpolated elevation at the given point.

        If no mesh element contains the point exactly, it will be
        re-checked using a maximum distance of ``1.0e-1``.

        If a 3D point is passed, only the first two coordinates will be
        used for containment checking.

        :param point: The point to find the elevation for.
        :type point: :class:`tuple` [
            :class:`float`, :class:`float`, ...]
        :return: The elevation at the given point.
        :rtype: :class:`float`
        :raises ValueError: If the point is not contained in any mesh
            element.
        """
        # TODO: This parameter should be accessible somehow - maybe via Mesh?
        precision = 1.0e-1  # Maximum distance for non-exact point matches
        try:
            # Try to find an element containing this point
            element = self.element_at(point)
        except ValueError as err:
            # If this fails, try to find the closest element instead. This is
            # necessary as the element_at check fails early and does not check
            # for floating point errors around mesh element edges.
            logger.debug('Unable to find containing element for point %s, '
                         'searching for closest element instead...', point[:2])
            element = self.get_element(point)

            # Calculate the minimum distance between the closest element and
            # the point to check
            triangle_2d: Triangle2D = tuple(
                (p[0], p[1]) for p in element.points)
            dist = distance_to_polygon((point[0], point[1]), triangle_2d)

            if dist < precision:
                # If the point is within the precision tolerance of the
                # element, the element may still be used for interpolation.
                logger.debug('Closest element %s within tolerance (%f <= %f)',
                             element.spatial_marker, dist, precision)
            else:
                # The point is too far away from any element,
                # re-raise the error and try another interpolation source.
                logger.debug('Closest element %s outside of tolerance (%f > '
                             '%f)', element.spatial_marker, dist, precision)
                raise err
        return element.interpolate(point)

    def get_element(self, point: Union[Point2D, Point3D], *,
                    search_effort: float = 1.0) -> MeshElement:
        """Return the element closest to the given point.

        By default, this exhaustively searches the entire mesh. In this
        case, the search is guaranteed to return the closest element.

        The search_effort argument may be used to reduce search effort
        by quitting after X ratio of all elements have been checked,
        then picking the closest one found.
        This is only useful with space-aware containers where only
        searching ~10% of the entire data set might give sufficiently
        high confidence.

        If a 3D point is passed, only the first two coordinates will be
        used for containment checking.

        :param point: The point to find the closest element for.
        :type point: :class:`tuple` [
            :class:`float`, :class:`float`, ...]
        :param search_effort: The search effort ratio to use.
        :type search_effort: :class:`float`
        :return: The element closest to the given point.
        :rtype: :class:`MeshElement`
        :raises ValueError: If the search_effort argument value is
            equal to or less than 0, or if it is greater than 1
        :raises ValueError: If the mesh is empty
        """
        if search_effort <= 0.0 or search_effort > 1.0:
            raise ValueError('Search effort must fall within the (0.0, 1.0] '
                             f'range (current: {search_effort}')
        if not self.elements:
            raise ValueError('Mesh does not contain any element')

        point_2d: Point2D = (point[0], point[1])
        lowest_dist = -1.0
        closest_element: Optional[MeshElement] = None

        for index, element in enumerate(self.elements.iter_spatial(point_2d)):
            # Calculate the distance between the element and the point
            triangle_2d = tuple((p[0], p[1]) for p in element.points)
            dist = distance_to_polygon(point_2d, triangle_2d)

            # Exit early if the point is contained within an element
            if dist < 0.0:
                logger.info('Found containing element %s for point %s',
                            element.spatial_marker, point_2d)
                return element

            # Update closest element
            if lowest_dist < 0.0 or dist < lowest_dist:
                lowest_dist = dist
                closest_element = element

            # Check search effort
            if (index+1) / len(self.elements) > search_effort:
                logger.info(
                    'Exceeded search effort of %f: %d of %d elements checked',
                    search_effort, index+1, len(self.elements))
                break

        assert closest_element is not None
        return closest_element

    def get_element_by_id(self, id_: int) -> MeshElement:
        """Return the element with the givenID.

        :param id_: ID of the element to return
        :type id_: :class:`int`
        :return: The element with the given ID
        :rtype: :class:`MeshElement`
        :raises KeyError: Raised if no element with this ID exists.
        """
        for element in self._elements:
            if element.id == id_:
                return element
        raise KeyError(f'Mesh does not contain an element with ID {id_}')

    def _get_element_id(self) -> int:
        """Return a valid element ID.

        This does not check for holes in the element numbering.
        """
        return len(self.elements) + 1

    def get_node_by_id(self, id_: int) -> MeshNode:
        """Return the node with the given ID.

        :param id_: ID of the node to return
        :type id_: :class:`int`
        :return: The node with the given ID
        :rtype: :class:`MeshNode`
        :raises KeyError: Raised if no node with this ID exists.
        """
        for node in self._nodes:
            if node.id == id_:
                return node
        raise KeyError(f'Mesh does not contain a node with ID {id_}')

    def get_node(self, point: Union[Point2D, Point3D], *,
                 search_effort: float = 1.0) -> MeshNode:
        """Return the node closest to the given point.

        By default, this exhaustively searches the entire mesh. In this
        case, the search is guaranteed to return the closest node.

        The search_effort argument may be used to reduce search effort
        by quitting after X ratio of all nodes have been checked, then
        picking the closest one found.
        This is only useful with space-aware containers where only
        searching ~10% of the entire data set might give sufficiently
        high confidence.

        If a 3D point is passed, only the first two coordinates will be
        used for containment checking.

        :param point: The point to find the closest node for.
        :type point: :class:`tuple` [
            :class:`float`, :class:`float`, ...]
        :param search_effort: The search effort ratio to use.
        :type search_effort: :class:`float`
        :return: The node closest to the given point.
        :rtype: :class:`MeshNode`
        :raises ValueError: If the search_effort argument value is
            equal to or less than 0, or if it is greater than 1
        :raises ValueError: If the mesh is empty
        """
        if search_effort <= 0.0 or search_effort > 1.0:
            raise ValueError('Search effort must fall within the (0.0, 1.0] '
                             f'range (current: {search_effort}')
        if not self.nodes:
            raise ValueError('Mesh does not contain any nodes')

        point_2d: Point2D = (point[0], point[1])
        lowest_dist = -1.0
        closest_node: Optional[MeshNode] = None
        for index, node in enumerate(self.nodes.iter_spatial(point_2d)):
            dist = dist_2d(node.spatial_marker, point_2d)
            if lowest_dist < 0.0 or dist < lowest_dist:
                lowest_dist = dist
                closest_node = node
            if (index+1) / len(self.nodes) > search_effort:
                logger.info('Exceeded search effort of %f: %d of %d nodes '
                            'checked', search_effort, index+1, len(self.nodes))
                break

        assert closest_node is not None
        return closest_node

    def _get_node_id(self) -> int:
        """Return a valid node ID.

        This does not check for holes in the node numbering.
        """
        return len(self.nodes) + 1

    def node_at(self, point: Union[Point2D, Point3D]) -> MeshNode:
        """Return the node at the given point.

        If no node is found at the given point, a :class:`ValueError`
        is raised.

        This performs an exact check, be wary of floating-point errors.

        To get the closest node to a given point without an exact
        check, use the :meth:`get_node` method instead.

        If a 3D point is passed, only the first two coordinates will be
        used for containment checking.

        :param point: The point to find the node for.
        :type point: :class:`tuple` [
            :class:`float`, :class:`float`, ...]
        :return: The node at the given point.
        :rtype: :class:`MeshNode`
        :raises ValueError: If no node is found at the given point.
        """
        for node in self.nodes.iter_spatial((point[0], point[1])):
            if node.spatial_marker == point[:2]:
                return node
        raise ValueError(f'No node found at {point}')

    def purge_nodes(self) -> List[MeshNode]:
        """Delete any disjoint nodes from the mesh.

        Disjoint nodes are nodes that are not referenced by any mesh
        elements.

        :return: The list of deleted nodes.
        :rtype: :class:`list` [:class:`MeshNode`]
        """
        purged = [n for n in self.nodes if not n.elements]
        _ = (self.remove_node(n) for n in purged)
        return purged

    def remove_element(self, element: MeshElement) -> None:
        """Remove an element from the mesh.

        This does not delete the element's defining nodes, only the
        element itself is removed and detached from its defining nodes.

        :param element: The element to remove.
        :type element: :class:`MeshElement`
        :raises ValueError: If the element is not part of the mesh.
        """
        try:
            self._elements.remove(element)
        except KeyError as err:
            raise ValueError(
                f'The MeshElement instance {element} with ID {element.id} is '
                'not part of this mesh instance') from err
        else:
            for node in list(element.nodes):
                node.detach_element(element)

    def remove_node(self, node: MeshNode) -> None:
        """Remove a node from the mesh.

        This also deletes any elements that were defined using the
        deleted node.

        :param node: The node to remove.
        :type node: :class:`MeshNode`
        :raises ValueError: If the node is not part of the mesh.
        """
        logger.debug('Deleted node with ID %d, also deleted %d associated '
                     'elements.', node.id, len(node.elements))
        for element in list(node.elements):
            self.remove_element(element)
        try:
            self._nodes.remove(node)
        except KeyError as err:
            raise ValueError(
                f'The MeshNode instance {node} with ID {node.id} is not part '
                'of this mesh instance') from err

    def save(self, filename: Union[str, pathlib.Path],
             num_materials: Optional[int] = None) -> None:
        """Save the current mesh as a 2DM mesh file.

        :param filename: The file to save the mesh to.
        :type filename: :class:`str` or :class:`pathlib.Path`
        :param num_materials: The number of materials to use.
        :type num_materials: :class:`int` | :obj:`None`
        """
        # Read the num_materials field from the first element if not provided
        if num_materials is None:
            if self.elements:
                num_materials = len(next(iter(self.elements)).materials)
            else:
                num_materials = 0
        with py2dm.Writer(str(filename), materials=num_materials) as writer:
            # Write nodes
            nodes = sorted(self.nodes, key=lambda n: n.id)
            for index, node in enumerate(nodes):
                writer.node(node.id, *node.pos)
                if index % 10_000 == 0:
                    writer.flush_nodes(compact=True)
            writer.flush_nodes(compact=True)
            # Write elements
            elements = sorted(self.elements, key=lambda e: e.id)
            for index, element in enumerate(elements):
                writer.element('E3T', element.id,
                               *[n.id for n in element.nodes],
                               materials=element.materials[:num_materials])
                if index % 10_000 == 0:
                    writer.flush_elements(compact=True)
            writer.flush_elements(compact=True)
            # Write node strings
            for name, ns_nodes in self.node_strings.items():
                if not ns_nodes:
                    warnings.warn(f'Node string {name} is empty and was '
                                  'ignored', BasemeshWarning)
                    continue
                first, *others = tuple(n.id for n in ns_nodes)
                writer.node_string(first, *others, name=name)
            # The "fold_after" flag forces all nodestrings into a single line
            writer.flush_node_strings(fold_after=0)
        # BASEMENT 3 compatibility: Remove trailing whitespace
        self._strip_trailing_newline(filename)

    @staticmethod
    def _strip_trailing_newline(filename: Union[str, pathlib.Path]) -> None:
        """Remove any trailing newlines in the given file.

        This is necessary for compatibility with BASEMENT 3. The file
        is truncated in-place.
        """
        with open(filename, 'rb+') as file_:
            # Jump to the end of the file
            file_.seek(0, os.SEEK_END)
            # This loop reads char by char from the back of the file as long as
            # the characters returned are considered whitespace.
            while not file_.read(1).strip():
                file_.seek(-2, os.SEEK_CUR)
            # The last read bit was non-whitespace; truncate the file
            file_.truncate()


def _get_2dm_material_count(
        filename: Union[str, pathlib.Path]) -> Tuple[int, bool]:
    """Determine the material count for a given 2DM file.

    This will check the first 100 lines for a NUM_MATERIALS_PER_ELEM
    field. If found, this value will be returned. If not, the entire
    file is scanned until an element is encountered. The material count
    is then inferred from that first element's list of MATIDs.

    For meshes without any elements, 0 is returned.

    :param filename: The 2DM file to scan
    :type filename: str | pathlib.Path
    :return: A tuple consisting of the material count and a Boolean
        indicating whether the value was provided via the
        NUM_MATERIALS_PER_ELEM tag (True) or inferred from an element
        (False)
    :rtype: tuple [int, bool]
    """
    with open(filename, 'r', encoding='utf-8') as file:
        iterator = iter(file)
        element: Optional[str] = None

        # For the first 100 lines, look for either the NUM_MATERIALS_PER_ELEM
        # field or an element (E**) card
        for _ in range(100):
            line = next(iterator)
            if line.startswith('NUM_MATERIALS_PER_ELEM'):
                try:
                    return int(line.split()[-1]), True
                except ValueError as err:
                    raise ValueError('Malformed NUM_MATERIALS_PER_ELEM '
                                     'card in 2DM file') from err
            if line.startswith('E'):
                element = line
                break

        # If no element was found yet, scan the rest of the file until an
        # element is encountered
        if element is None:
            for line in iterator:
                if line.startswith('E'):
                    element = line
                    break

        # If no element was found in the entire file, return 0 materials
        if element is None:
            return 0, False

        # If an element was found, infer the material count from the element
        # line's length (minus any node IDs and the E** card itself)
        words = element.split()
        node_count = int(words[0][1])
        return len(words) - node_count - 1, False


def _is_2dm_zero_indexed(filename: Union[str, pathlib.Path]) -> bool:
    """Return whether the mesh is zero-indexed.

    This will check the first 100 lines until either a node or element
    card is found. If the first ID encountered is neither 0 nor 1, an
    exception is raised.

    :param filename: The 2DM file to scan
    :type filename: str | pathlib.Path
    :return: Whether the mesh is zero-indexed
    :rtype: bool
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line, _ in zip(file, range(100)):
            if line.startswith(('ND', 'E')):
                words = line.split()
                try:
                    id_ = int(words[1])
                except ValueError as err:
                    raise ValueError(
                        f'Unable to read ID from line {line}') from err
                if id_ not in (0, 1):
                    raise ValueError(
                        'Meshes IDs must be ordered and start with 0 or 1, '
                        f'found {id_}')
                return id_ == 0
    # Fallback for empty meshes
    return False
