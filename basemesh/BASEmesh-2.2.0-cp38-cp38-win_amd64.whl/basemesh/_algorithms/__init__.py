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

"""Shared algorithms which could be reused or optimised.

This module dynamically retrieves algorithms from the C acceleration
module if available.
"""

import os
import sys
from ._algorithms_py import (dist_2d, dist_3d, distance_to_polygon,
                             get_intersections, half_plane_distance,
                             interpolate_line, interpolate_triangle,
                             line_intersection, line_segments_intersection,
                             point_in_polygon_concave, point_in_polygon_convex,
                             point_on_line, point_within_range,
                             rectangle_intersection, rotate_2d, split_line)

__all__ = [
    'dist_2d',
    'dist_3d',
    'distance_to_polygon',
    'get_intersections',
    'half_plane_distance',
    'interpolate_line',
    'interpolate_triangle',
    'line_intersection',
    'line_segments_intersection',
    'point_in_polygon_concave',
    'point_in_polygon_convex',
    'point_on_line',
    'point_within_range',
    'rectangle_intersection',
    'rotate_2d',
    'split_line',
]

sys.path.append(os.path.dirname(__file__))
implementation = 'py'

# NOTE: The potential name-shadowing from the wildcard import is by design. In
# fact, it is *only* supposed to overshadow the previously imported names.
# This solution still allows for introspection and offers clear references
# during development while making addition and removal of C implementations
# trivial.
#
# The developer of the C extensions is responsible for ensuring they are a
# perfect match for the native Python implementations.

try:
    # pylint: disable=import-error
    from _algorithms_c import *  # type: ignore
except ModuleNotFoundError:
    pass
else:
    implementation = 'c'
