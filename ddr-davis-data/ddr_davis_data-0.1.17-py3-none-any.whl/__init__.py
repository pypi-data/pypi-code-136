# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:04:00 2021

@author: Darshan Rathod

This package has functionalities to manage, plot and handle davis ouput files. The major functionalities includes
- accessing *.im7* (image) files
- accessing *.vc7* (vector) files
- plotting vectors, streamlines and quiver plots
- calculation of $\omega$ from velocity vectors

The basic object are defined in *base.py* file. Other files are built upon the classes defined in *base.py* file.
All common functions are defined in *utils.py* file. Ther might be some functions in other filed which are specific to that module.

"""

from .base import *
from .PIV_2D import *
from .utils import *
from .plotting import *


from .version import version