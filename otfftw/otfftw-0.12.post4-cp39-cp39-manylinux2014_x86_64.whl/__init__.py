"""
    otfftw --- An OpenTURNS module
    ===================================================

    Contents
    --------
      'otfftw' is python module for OpenTURNS

"""

import sys
if sys.platform.startswith('win'):
    # this ensures OT dll is loaded
    import openturns

from .otfftw import *

__version__ = '0.12.post4'
