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

"""Helper module for generating flat, non-intersecting PSLGs.

The Triangle library requires flat input PSLGs for its triangulation.
While it has some built-in functionality for cleaning up geometries
(such as removing exactly coincident vertices), it cannot handle
GIS-based input data and the resulting errors are near impossible to
troubleshoot efficiently.

This module exposes the :class:`PSLGBuilder` class, which can be used
to clean up and prepare PSLGs for use with Triangle.

To differentiate between the unique, ID-based mesh nodes and the
anonymous points used for the input data, this module uses the term
:class:`Vertex`, whereas the term ``Node`` is reserved for unique nodes
with IDs.

After instantiating a :class:`PSLGBuilder` object, geometry can be
added using the :meth:`PSLGBuilder.add_vertex` and
:meth:`PSLGBuilder.add_segment` methods. Optionally,
:meth:`PSLGBuilder.clean_geometry` can be called to simplify and clean
the geometry prior to generating the input data. This is always
recommended as it ensures Triangle compatibility, but it is an
expensive operation that may not be feasible for input geometries with
hundreds of thousands of vertices or segments, as may be the case when
generating a mesh including building outlines.

Finally, call :meth:`PSLGBuilder.build` to generate the input data for
the :mod:`basemesh.triangle` module.
"""

from ._geometry import Vertex, Segment
from ._builder import PSLGBuilder

__all__ = [
    'PSLGBuilder',
    'Segment',
    'Vertex',
]

__version__ = '0.1.0'
