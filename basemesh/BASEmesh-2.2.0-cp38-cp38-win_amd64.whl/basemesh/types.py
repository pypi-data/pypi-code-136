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

"""Custom typing shorthands."""

# NOTE: These shorten type hints and make it easy to find all references to a
# particular type if they need to be updated or replaced.

from typing import Tuple

Point2D = Tuple[float, float]
Point3D = Tuple[float, float, float]
Line2D = Tuple[Point2D, Point2D]
Line3D = Tuple[Point3D, Point3D]
LineString2D = Tuple[Point2D, ...]
LineString3D = Tuple[Point3D, ...]
Polygon2D = Tuple[Point2D, ...]
Polygon3D = Tuple[Point3D, ...]
Rectangle2D = Tuple[float, float, float, float]  # min_x, max_x, min_y, max_y
Triangle2D = Tuple[Point2D, Point2D, Point2D]
Triangle3D = Tuple[Point3D, Point3D, Point3D]
