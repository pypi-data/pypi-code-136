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

"""A Python wrapper for Jonathan Shewchuk's "Triangle".

This module provides a Python API for the Triangle command line
interface, as well as Python representations of its input data types.
"""

from ._geometry import Element, Node, Segment
from ._markers import HoleMarker, RegionMarker
from ._triangulate import command, read_output, run_triangle, triangulate

__all__ = [
    'Element',
    'HoleMarker',
    'Node',
    'RegionMarker',
    'Segment',
    'command',
    'read_output',
    'run_triangle',
    'triangulate',
]

__version__ = '0.1.0'
