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

"""1D channel generator and processor for BASEmesh.

This module adds support for 1D channels to BASEmesh. These channels
are represented through the :class:`ChannelGeometry` class, which is in
turn made up of :class:`CrossSection` instances.

It also features a number of built-in factories used to simplify the
generation of arbitrary cross sections.

Additionally, 1D geometries may be exported to 2D meshes via the
:meth:`ChannelGeometry.to_mesh()` method.
"""

from .geometry import ChannelGeometry, CrossSection, Vertex
from .io import BaseChainReader, BaseChainWriter

__all__ = [
    'BaseChainReader',
    'BaseChainWriter',
    'ChannelGeometry',
    'CrossSection',
    'Vertex'
]

__version__ = '0.1.0a4'
