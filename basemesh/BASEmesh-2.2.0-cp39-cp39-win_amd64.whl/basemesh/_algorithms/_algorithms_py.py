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

"""Shared algorithms which could be reused or optimised."""

import math
from typing import List, NewType, TypeVar, Union

import numpy as np

from ..types import (Line2D, Line3D, LineString2D, LineString3D, Point2D,
                     Point3D, Polygon2D, Rectangle2D, Triangle3D)

T = TypeVar('T')

NDArray = NewType('NDArray', object)


def dist_2d(pt_a: Point2D, pt_b: Point2D) -> float:
    """Return the Euclidean 2D distance between two points.

    Parameters
    ----------
    pt_a : Tuple[float, float]
        The first input point
    pt_b : Tuple[float, float]
        The second input point

    Returns
    -------
    float
        The straight-line distance between the two points
    """
    dist_x = pt_a[0] - pt_b[0]
    dist_y = pt_a[1] - pt_b[1]
    return math.sqrt(dist_x**2 + dist_y**2)


def dist_3d(pt_a: Point3D, pt_b: Point3D) -> float:
    """Return the Euclidean 3D distance between two points.

    Like dist_2d, but this version also considers differences in
    elevation.

    Parameters
    ----------
    pt_a : Tuple[float, float, float]
        The first input point
    pt_b : Tuple[float, float, float]
        The second input point

    Returns
    -------
    float
        The straight-line distance between the two points
    """
    dist_x = pt_a[0] - pt_b[0]
    dist_y = pt_a[1] - pt_b[1]
    dist_z = pt_a[2] - pt_b[2]
    return math.sqrt(dist_x**2 + dist_y**2 + dist_z**2)


def get_intersections(line: Line2D, polygon: Polygon2D) -> List[Point2D]:
    """Find all intersections between the given line and polygon.

    This returns a list of all points where the given line intersects
    with the edges of the polygon. Coincident lines are not considered
    "real" intersections and will not be part of the return list.

    Parameters
    ----------
    line : Tuple[Tuple[float, float], Tuple[float, float]]
        The line to check for intersections
    polygon : Tuple[Tuple[float, float], ...]
        A polygon whos edges will be checked for intersections. This
        must have at least three vertices.

    Returns
    -------
    List[Tuple[float, float]]
        The list of intersections

    Raises
    ------
    ValueError: Raised if the given polygon has fewer than three
        vertices.
    """
    if len(polygon) < 3:
        raise ValueError('The polygon must have at least 3 vertices')
    intersections: List[Point2D] = []
    for index, vtx_1 in enumerate(polygon):
        try:
            vtx_2 = polygon[index+1]
        except IndexError:
            vtx_2 = polygon[0]
        edge = vtx_1, vtx_2
        # Check for an intersection with the given line
        if not line_segments_intersection(line, edge, False):
            continue
        # If an intersection was expected, calculated its coordinates
        intersect = line_intersection(line, edge)
        intersections.append(intersect)
    return intersections


def interpolate_line(point: Point2D, line: Line3D) -> float:
    """Interpolate the elevation of a line.

    The given point will be snapped onto the line, it does not have to
    be exactly on the line.

    Parameters
    ----------
    point : Tuple[float, float]
        The point at which to calculate the elevation of the 3D line
    line : Tuple[Tuple[float, float, float],
                 Tuple[float, float, float]]
        The 3D line to use for interpolation

    Returns
    -------
    float
        The elevation of the line at the point closest to the input
        point
    """
    # Project the point onto the line to get a relative distance along the line
    line_vec: NDArray = np.array(  # type: ignore
        (line[1][0]-line[0][0], line[1][1]-line[0][1]))
    point_vec: NDArray = np.array(  # type: ignore
        (point[0]-line[0][0], point[1]-line[0][1]))
    len_sq = dist_2d((line[1][0], line[1][1]), (line[0][0], line[0][1])) ** 2

    # Project the point
    rel_dist: float = line_vec @ point_vec / len_sq  # type: ignore
    # Interpolate the new height
    return float(line[0][2] + rel_dist * (line[1][2]-line[0][2]))


def interpolate_triangle(point: Point2D, triangle: Triangle3D) -> float:
    """Interpolate the elevation of a triangle.

    This returns the elevation of the plane defined by the given
    triangle at the location of the point.

    This uses Barycentric coordinates; the point does not need to lie
    in or even near the triangle itself.

    Parameters
    ----------
    point : Tuple[float, float]
        The point to interpolate
    triangle : Tuple[Tuple[float, float, float],
                     Tuple[float, float, float],
                     Tuple[float, float, float]]
        The triangle to use for interpolation

    Returns
    -------
    float
        The interpolated elevation of the triangle at the point
    """
    # NOTE: Barycentric coordinates do support negative weights, which could be
    # used to check for point containment within triangles. Might be worth
    # looking into if we're chasing performance.

    vtx_1, vtx_2, vtx_3 = triangle

    # Calculate Barycentric weights for each vertex
    denom = ((vtx_2[1] - vtx_3[1]) * (vtx_1[0] - vtx_3[0])
             + ((vtx_3[0] - vtx_2[0]) * (vtx_1[1] - vtx_3[1])))

    weight_1 = ((vtx_2[1] - vtx_3[1]) * (point[0] - vtx_3[0])
                + ((vtx_3[0] - vtx_2[0]) * (point[1] - vtx_3[1]))) / denom

    weight_2 = ((vtx_3[1] - vtx_1[1]) * (point[0] - vtx_3[0])
                + ((vtx_1[0] - vtx_3[0]) * (point[1] - vtx_3[1]))) / denom

    weight_3 = 1 - weight_1 - weight_2

    # The interpolated value is now equal to the sum of all weights and their
    # corresponding input values
    return weight_1*vtx_1[2] + weight_2*vtx_2[2] + weight_3*vtx_3[2]


def half_plane_distance(line: Line2D, point: Point2D,
                        normalise: bool = True) -> float:
    """Return the signed distance from the point to the line.

    This returns the signed half plane distance of the point from the
    line.
    The line bisects 2D plane into two half-planes. If the point lies
    on this line, the distance returned is 0.0.
    If the point lies to the left of an observer sitting at the first
    point of the line and looking towards the second point, the
    distance returned will be negative. If the point lies to the right
    of this observer, the distance will be positive.

    By default, the returned distance is normalised; i.e. it will equal
    the actual Euclidean distance between the point and the line's
    closest approach.
    If the sign is more important than the actual value, you may set
    the normalise argument to False to save yourself a math.sqrt()
    call.

    Parameters
    ----------
    line : Tuple[Tuple[float, float], Tuple[float, float]]
        The line splitting the 2D plane
    point : Tuple[float, float]
        The point to calculate the half plane distance for
    normalise : bool, optional
        Whether to normalise the returned distance, by default True

    Returns
    -------
    float
        The signed distance from the point to the line
    """
    # NOTE: I cannot find any convention on which side of the 2D plane should
    # be represented by which sign.
    # I opted for this arrangement so that running this check for a polygon
    # with CCW vertex order returns sensible (i.e. positive) distances for
    # external points and negative distances for internal points.
    # The distance to an object the point is contained in seemed more deserving
    # of the negative sign.

    # Build a vector from the given input line
    vec: NDArray = np.array(  # type: ignore
        (line[1][0]-line[0][0], line[1][1]-line[0][1]))
    # Get the right-hand normal vector of the line
    norm_vec: NDArray = np.array((vec[1], -vec[0]))  # type: ignore
    # Get the unit vector (this preserves Euclidean distance in the output)
    if normalise:
        norm_vec = norm_vec / dist_2d(*line)  # type: ignore
    # Get a vector representing the input point
    check_vec: NDArray = np.array(  # type: ignore
        (point[0]-line[0][0], point[1]-line[0][1]))
    # Project the check-vector onto the edge normal vector. If the projection
    # is negative, the point lies on the "inside" of the edge.
    return float(norm_vec @ check_vec)  # type: ignore


def distance_to_polygon(point: Point2D, polygon: Polygon2D) -> float:
    """Calculate the distance from a convex polygon to a given point.

    The return value will be negative if the point lies within the
    polygon.

    Due to the multiple reprojections used, this algorithm is highly
    susceptible to floating point errors. This means that points lying
    on the edge of the polygon will hardly ever return 0.0, but rather
    something like +/- 1.0e-16.
    It is recommended to run a separate point-on-line test for these
    values if you are interested in the precise value.

    Note that this algorithm does not check whether the given polygon
    is actually convex. It also does not check for self-intersections
    or verifies whether the vertices are ordered in counter-clockwise
    order.

    Parameters
    ----------
    point : Tuple[float, float]
        The point to calculate the distance for
    polygon : Tuple[Tuple[float, float], ...]
        Any number of vertices forming a convex polygon; at least three
        vertices are required

    Returns
    -------
    float
        The shortest distance from the point to any polygon edge; will
        be nagative if the point lies within the polygon

    Raises
    ------
    ValueError
        Raised if the given polygon has fewer than three vertices
    """
    if len(polygon) < 3:
        raise ValueError('A valid polygon must have at least three '
                         f'vertices (got {len(polygon)})')

    # NOTE: This is identical in principle to the point_in_polygon_convex
    # algorithm, but the loop doesn't end once the point is deemed to lie
    # outside the polygon.
    # Instead, every point is projected back onto the edge it was checked
    # against and constrained onto its length. This also implicitly checks the
    # vertices.

    # Used to keep track of the minimum distance encountered
    min_dist = None

    # Iterate over the vertices of the polygon
    for index, vtx_1 in enumerate(polygon):
        # Find a second, neighbouring vertex
        try:
            vtx_2 = polygon[index+1]
        except IndexError:
            # Connect the last vertex to the first, closing the ring
            vtx_2 = polygon[0]

        # Build a vector from the given edge
        edge_vec: NDArray = np.array(  # type: ignore
            (vtx_2[0]-vtx_1[0], vtx_2[1]-vtx_1[1]))
        # Build a vector from the first vertex to the point in question
        check_vec: NDArray = np.array(  # type: ignore
            (point[0]-vtx_1[0], point[1]-vtx_1[1]))

        # Calculate the squared length of the edge (this avoids a sqrt later)
        len_sq = dist_2d(vtx_1, vtx_2) ** 2

        # Project the check-vector onto the edge vector and calculate the
        # relative distance (i.e. distance along the edge)
        rel_dist: float = edge_vec @ check_vec / len_sq  # type: ignore

        # Clamp the relative distance. This ensures that a point too far along
        # the vector end sup being closest to one of the two end points of the
        # edge
        if rel_dist < 0.0:
            rel_dist = 0.0
        elif rel_dist > 1.0:
            rel_dist = 1.0

        # Interpolate the point along the edge that is closest to the input
        # point
        pos_x: float = vtx_1[0] + edge_vec[0] * rel_dist  # type: ignore
        pos_y: float = vtx_1[1] + edge_vec[1] * rel_dist  # type: ignore

        # Finally, calculate the distance between the input point and the
        # clamped, projected point
        dist = dist_2d(point, (pos_x, pos_y))

        if min_dist is None or dist < min_dist:
            min_dist = dist

    # At this point of the loop, min_dist has been set to a float
    assert min_dist is not None

    # If the point lies inside the polygon, return a negative number
    if point_in_polygon_convex(point, polygon):
        min_dist = - float(min_dist)
    return min_dist


def line_intersection(line_1: Line2D, line_2: Line2D) -> Point2D:
    """Return the intersection point of two intersecting lines.

    Note that this treats both lines as infinite rays, the intersection
    may not lie on either input line.

    Parameters
    ----------
    line_1 : Tuple[Tuple[float, float], Tuple[float, float]]
        The first input line
    line_2 : Tuple[Tuple[float, float], Tuple[float, float]]
        The second input line

    Returns
    -------
    Tuple[float, float]
        The point of intersection

    Raises
    ------
    ValueError
        Raised if the two lines are parellel or collinear
    """
    pt_a, pt_b = line_1
    pt_c, pt_d = line_2

    # Succeed early if the lines share an endpoint
    if pt_a in line_2:
        return pt_a
    if pt_b in line_2:
        return pt_b

    # Convert the lines to the implicit form
    a_1, b_1 = pt_b[1]-pt_a[1], -(pt_b[0]-pt_a[0])
    a_2, b_2 = pt_d[1]-pt_c[1], -(pt_d[0]-pt_c[0])
    d_1 = a_1*pt_a[0] + b_1*pt_a[1]
    d_2 = a_2*pt_c[0] + b_2*pt_c[1]

    # Calculate intersection
    denom = a_1*b_2 - a_2*b_1

    if denom == 0:
        raise ValueError('No intersection found, lines are parallel')

    pos_x = (b_2*d_1 - b_1*d_2) / denom
    pos_y = (a_1*d_2 - a_2*d_1) / denom

    return pos_x, pos_y


def line_segments_intersection(line_1: Line2D, line_2: Line2D,
                               allow_collinear: bool = True) -> bool:
    """Return whether the two given lines intersect.

    This returns a Boolean value. Use line_intersection to retrieve the
    actual point of intersection if this succeeds.

    Parameters
    ----------
    line_1 : Tuple[Tuple[float, float], Tuple[float, float]]
        The first line segment
    line_2 : Tuple[Tuple[float, float], Tuple[float, float]]
        The second line segment
    allow_collinear : bool, optional
        Whether collinear lines count as an intersection, by default
        True

    Returns
    -------
    bool
        Whether the two line segments intersect
    """
    pt_a, pt_b = line_1
    pt_c, pt_d = line_2

    # Fail early if the two lines' bounding rectangles don't overlap
    min_x_a, max_x_a = ((pt_a[0], pt_b[0]) if pt_a[0] <= pt_b[0]
                        else (pt_b[0], pt_a[0]))
    min_y_a, max_y_a = ((pt_a[1], pt_b[1]) if pt_a[1] <= pt_b[1]
                        else (pt_b[1], pt_a[1]))
    min_x_b, max_x_b = ((pt_c[0], pt_d[0]) if pt_c[0] <= pt_d[0]
                        else (pt_d[0], pt_c[0]))
    min_y_b, max_y_b = ((pt_c[1], pt_d[1]) if pt_c[1] <= pt_d[1]
                        else (pt_d[1], pt_c[1]))
    rect_a = min_x_a, max_x_a, min_y_a, max_y_a
    rect_b = min_x_b, max_x_b, min_y_b, max_y_b
    if not rectangle_intersection(rect_a, rect_b):
        return False

    # Succeed early if the two lines share a point
    if (pt_a in line_2 or pt_b in line_2) and allow_collinear:
        return True

    # Calculate the vectors for each line
    vec_1: NDArray = np.array(  # type: ignore
        (pt_b[0]-pt_a[0], pt_b[1]-pt_a[1]))
    vec_2: NDArray = np.array(  # type: ignore
        (pt_d[0]-pt_c[0], pt_d[1]-pt_c[1]))
    vec_3: NDArray = np.array(  # type: ignore
        (pt_c[0]-pt_a[0], pt_c[1]-pt_a[1]))

    vec_3cross1: NDArray = np.cross(vec_3, vec_1)  # type: ignore
    vec_3cross2: NDArray = np.cross(vec_3, vec_2)  # type: ignore
    vec_1cross2: NDArray = np.cross(vec_1, vec_2)  # type: ignore
    # Check for collinearity
    if vec_3cross1 == np.zeros(vec_3cross1.shape):  # type: ignore
        if allow_collinear:
            # Return whether there is any overlap betweeen the two lines
            return ((pt_c[0]-pt_a[0] < 0) != (pt_c[0]-pt_b[0])
                    or (pt_c[1]-pt_a[1] < 0) != (pt_c[1]-pt_b[1]))
        return False
    # Check whether the two lines are parallel (but not collinear)
    if vec_1cross2 == np.zeros(vec_1cross2.shape):   # type: ignore
        return False
    # Express the intersection using each line's parametric representation
    scalar = 1 / vec_1cross2  # type: ignore
    para_1: float = vec_3cross1 * scalar  # type: ignore
    para_2: float = vec_3cross2 * scalar  # type: ignore
    # The intersection lies on the two lines only if the parameter falls within
    # the [0, 1] range for both lines
    return bool(0 <= para_1 <= 1 and 0 <= para_2 <= 1)


def point_in_polygon_concave(point: Point2D, polygon: Polygon2D) -> bool:
    """Return whether the given point lies within the polygon.

    Note that this algorithm does not check for self-intersection.

    Parameters
    ----------
    point : Tuple[float, float]
        The point to check
    polygon : Tuple[Tuple[float, float], ...]
        The polygon to check against, this must have at least three
        vertices

    Returns
    -------
    bool
        Whether the point lies within the polygon

    Raises
    ------
    ValueError
        Raised if the polygon has fewer than three vertices
    """
    # NOTE: The following uses a ray-casting algorithm, i.e. works by casting a
    # horizontal ray from the point in question and counting the number of
    # intersections with the polygon boundary.
    if len(polygon) < 3:
        raise ValueError('A valid polygon must have at least three '
                         f'vertices (got {len(polygon)})')
    is_inside = False
    for index, vtx_1 in enumerate(polygon):
        try:
            vtx_2 = polygon[index+1]
        except IndexError:
            vtx_2 = polygon[0]
        # NOTE: The rest of the algorithm cannot handle points sitting on an
        # edge and will return arbitrary values
        if point_on_line((vtx_1, vtx_2), point):
            return True
        # If the edge crosses the ray (either direction)
        if (vtx_1[1] < point[1] <= vtx_2[1]
                or vtx_2[1] < point[1] <= vtx_1[1]):
            # If the point of intersection lies to the left of the point, flip
            # the output flag
            if (vtx_2[0] + (point[1]-vtx_2[1]) / (vtx_1[1]-vtx_2[1])
                    * (vtx_1[0]-vtx_2[0]) < point[0]):
                is_inside = not is_inside
    return is_inside


def point_in_polygon_convex(point: Point2D, polygon: Polygon2D) -> bool:
    """Return whether the given point lies within the polygon.

    Note that this algorithm does not check whether the polygon is
    actually convex, whether it has any self-intersection or whether
    its vertices are ordered in counter-clockwise order.

    Parameters
    ----------
    point : Tuple[float, float]
        The point to check
    polygon : Tuple[Tuple[float, float], ...]
        The polygon to check against, this must have at least three
        vertices

    Returns
    -------
    bool
        Whether the point lies within the given polygon

    Raises
    ------
    ValueError
        Raised if the polygon has fewer than three vertices
    """
    if len(polygon) < 3:
        raise ValueError('A valid polygon must have at least three '
                         f'vertices (got {len(polygon)})')

    # Iterate over the vertices of the polygon
    for index, vtx_1 in enumerate(polygon):
        # Find a second, neighbouring vertex
        try:
            vtx_2 = polygon[index+1]
        except IndexError:
            # Connect the last vertex to the first, closing the ring
            vtx_2 = polygon[0]

        # Get the signed distance of the current edge and point. If it is
        # positive, the point lies on the outside half plane for this edge and
        # can therefore not be part of the polygon any more.
        if half_plane_distance((vtx_1, vtx_2), point, normalise=False) > 0.0:
            return False

    # If the point lies on the "inside" of all edges of a convex polygon, it
    # lies within the polygon
    return True


def point_on_line(line: Line2D, point: Point2D,
                  precision: float = 0.0) -> bool:
    """Return whether the given point lies on the line.

    Due to floating point inaccuracies, you may want to set the
    precision argument to a sensible value when working with diagonal
    lines.

    Parameters
    ----------
    line : Tuple[Tuple[float, float], Tuple[float, float]]
        The input line to check against
    point : Tuple[float, float]
        The point to check
    precision : float, optional
        The maximum distance the point may be from the line to still be
        considered on the line, by default 0.0

    Returns
    -------
    bool
        Whether the point lies on the line, within tolerance
    """
    # Fail early if the point lies outside the line's bounding rectangle
    if not ((line[0][0] <= point[0] <= line[1][0]
             or line[1][0] <= point[0] <= line[0][0])
            and (line[0][1] <= point[1] <= line[1][1]
                 or line[1][1] <= point[1] <= line[0][1])):
        return False
    line_vec: NDArray = np.array(  # type: ignore
        (line[1][0]-line[0][0], line[1][1]-line[0][1]))
    point_vec: NDArray = np.array(  # type: ignore
        (point[0]-line[0][0], point[1]-line[0][1]))
    # Project the point onto the line
    proj: float = line_vec @ point_vec  # type: ignore
    # The span of two parallel vectors must be one-dimensional
    if proj != 0 and abs(np.cross(line_vec, point_vec)) / proj > precision:  # type: ignore
        return False
    # If the projection is negative, the point lies before the line
    return bool(-precision <= proj <= dist_2d(*line) ** 2 + precision)


def point_within_range(point_a: Point2D, point_b: Point2D,
                       max_dist: float) -> bool:
    """Return whether two points lie within a given distance.

    This uses a two step search, first evaluating the X and Y
    coordinates individually before performing the actual Euclidean
    distance calculation, which allows it to fail early for faraway
    points.

    Parameters
    ----------
    point_a : Tuple[float, float]
        The first point
    point_b : Tuple[float, float]
        The second point
    max_dist : float
        The maximum distance between the two points

    Returns
    -------
    bool
        Whether the distance between the two points is within range
    """
    # Step 1: coordinate comparison (square search area)
    if abs(point_a[0]-point_b[0]) > max_dist:
        return False
    if abs(point_a[1]-point_b[1]) > max_dist:
        return False
    # Step 2: Euclidean distance (circular search area)
    return dist_2d(point_a, point_b) <= max_dist


def rectangle_intersection(rect_a: Rectangle2D, rect_b: Rectangle2D) -> bool:
    """Return whether the two rectangles overlap each other."""
    # NOTE: Rectangle2D : Tuple[min_x, max_x, min_y, max_y]
    return (rect_b[0] <= rect_a[1]
            and rect_b[1] >= rect_a[0]
            and rect_b[2] <= rect_a[3]
            and rect_b[3] >= rect_a[2])


def rotate_2d(point: Point2D, angle: float, anchor: Point2D) -> Point2D:
    """Rotate the given point around an anchor point."""
    radians = angle * (math.pi/180)
    dist_x = point[0] - anchor[0]
    dist_y = point[1] - anchor[1]
    new_x = math.cos(radians) * dist_x - math.sin(radians) * dist_y + anchor[0]
    new_y = math.sin(radians) * dist_x + math.cos(radians) * dist_y + anchor[1]
    return new_x, new_y


def split_line(line_string: Union[LineString2D, LineString3D],
               num_segments: int) -> Union[LineString2D, LineString3D]:
    """Split the given line string into a number of segments.

    The start and end point remain unchanged, but additional
    equidistant points are inserted to achieve the desired number of
    subsegments.

    Note that for line strings with more than two points, this will
    split each of the lines. A line string with three points with a
    num_segments of 2 will result in an output line string with five
    points.

    If the input line is 3D, the inserted points will be interpolated
    to match the line's elevation.

    Parameters
    ----------
    line_string : Tuple[Union[Tuple[float, float],
                              Tuple[float, float, float]], ...]
        A line string consisting of 2D or 3D points
    num_segments : int
        The number of subsegments to split each line into, must be at
        least 1

    Returns
    -------
    Tuple[Union[Tuple[float, float], Tuple[float, float, float]], ...]
        The input line string, with additional vertices added

    Raises
    ------
    ValueError
        Raised if num_segments is less than 1
    """
    if num_segments < 1:
        raise ValueError('num_segments must greater or equal to one')
    assert len(line_string) >= 2, 'Line strings require at least two points'

    # Process each line individually
    out_string: List[Union[Point2D, Point3D]] = []
    for index, start_point in enumerate(line_string[:-1]):
        end_point = line_string[index+1]

        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]

        # Add the start point and any other inner points
        for cut_idx in range(num_segments):
            pos_x = start_point[0] + delta_x * (cut_idx/num_segments)
            pos_y = start_point[1] + delta_y * (cut_idx/num_segments)
            new_pt: Union[Point2D, Point3D] = (pos_x, pos_y)

            # Add elevation if needed
            if len(start_point) >= 3:
                pt_2d: Point2D = (new_pt[0], new_pt[1])
                # NOTE: If the code gets here, start_point and end_point are
                # going to be 3D points.
                pos_z = interpolate_line(
                    pt_2d, (start_point, end_point))  # type: ignore
                new_pt = *pt_2d, pos_z

            out_string.append(new_pt)

        # If we're at the end of the line string, add the end point as well
        if end_point == line_string[-1]:
            out_string.append(end_point)

    return tuple(out_string)  # type: ignore
