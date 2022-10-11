"""Pre-processing and mesh generation toolkit for BASEMENT.

This package contains utilities for generating and processing 1D and 2D
mesh geometries for use with the numerical simulation software such as
BASEMENT (https://basement.ethz.ch/).

It features standalone mesh generation utilities leveraging Jonathan
Shewchunk's Triangle (https://www.cs.cmu.edu/~quake/triangle.html), as
well as mesh editing and interpolation utilities.

BASEmesh can also be installed as a plugin for QGIS
(https://qgis.org/en/site/), allowing usage of its functionality via
the plugin interface.

For additional information, refer to the BASEMENT website linked above
or visit the project repository at
https://gitlab.ethz.ch/vaw/public/basemesh-v2/.


Copyright (C) 2020  ETH Zürich

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from . import abc, triangle
from ._algorithms import implementation
from ._pslg_builder import PSLGBuilder, Segment, Vertex
from ._interpolation import calculate_element_elevation, interpolate_mesh
from ._mesh import Mesh, MeshElement, MeshNode
from ._meshing import elevation_mesh, mesh_from_triangle, quality_mesh
from ._stringdefs import (resolve_string_defs, split_string_defs,
                          write_string_defs_sidecar)

__version__ = '2.2.0'

__all__ = [
    'Mesh',
    'MeshElement',
    'MeshNode',
    'PSLGBuilder',
    'Segment',
    'Vertex',
    'abc',
    'calculate_element_elevation',
    'elevation_mesh',
    'implementation',
    'interpolate_mesh',
    'mesh_from_triangle',
    'quality_mesh',
    'resolve_string_defs',
    'split_string_defs',
    'triangle',
    'write_string_defs_sidecar',
]
