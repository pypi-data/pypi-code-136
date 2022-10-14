# -*- coding: utf-8 -*-

"""

Package AmunPy is the Python interface to handle datasets produced by
the AMUN code (https://amuncode.org).

The package is released under GNU General Public License v3.
See file LICENSE for more details.

"""

from .amunxml import *
from .amunh5 import *
from .amunh5_deprecated import *
from .integrals import *
from .vtkio import *

__all__ = [ 'AmunXML', 'AmunH5', 'WriteVTK', \
        'amun_attribute', 'amun_coordinate', 'amun_dataset', 'amun_dataset_vtk', 'amun_integrals' ]

__author__ = "Grzegorz Kowal"
__copyright__ = "Copyright 2018-2022 Grzegorz Kowal <grzegorz@amuncode.org>"
__version__ = "0.9.8"
__maintainer__ = "Grzegorz Kowal"
__email__ = "grzegorz@amuncode.org"
