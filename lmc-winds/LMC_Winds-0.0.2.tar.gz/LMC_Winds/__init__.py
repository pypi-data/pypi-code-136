"""
LMC_Winds is a python package written to analyze HST galactic wind data.

Written by TCU Students.
"""

__author__ = 'TCU Students'

from os import path
from sys import version_info

# import warnings
# import matplotlib
# # The native MacOSX backend doesn't work for all:
# with warnings.catch_warnings():
#     warnings.simplefilter("ignore")
#     matplotlib.use('TkAgg')

from .example import *
from .whichLSF import *
from .def_norm_guesses import *
from .def_velocity_conversions import *
from .fitting import *
from .def_read_line_transitions import *
from .def_read_STSCI import *
#from .def_normalize import *
from .Jo_Codes.wakker_read_in import *
#from .April_codes import norm_testing
#from .April_codes.primary_fits_header import *
#from .April_codes.read_STSCI_testing import *
#from .April_codes.simple_normalization import *




#code_dir = path.dirname(path.abspath(__file__))
#with open(path.join(code_dir, 'VERSION')) as version_file:
#   version = version_file.read().strip()
#   if version_info[0] >= 3:
#        v_items = version.split('.')
#        v_items[0] = '3'
#        version = '.'.join(v_items)
#   __version__ = version
