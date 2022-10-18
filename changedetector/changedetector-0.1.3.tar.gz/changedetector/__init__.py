"""
CHANGE DETECTOR
~~~~~~~~~~~~~~~
This module detect all the change in a selected directory.
And execute a program chosen on saved changes. (Python, Ruby, C++)
Two modes of execution are available to you:
    * Based on observing a specific file for changes and executing another file. (Watch and Run Other) `WRO`
    * Observing a certain file and using the same file to conduct the test. (Watch and Run Self) `WRS`


:copyright (c) 2022 LuxLuth
:license: MIT, see LICENSE for more details.
"""
import os

__title__ = 'changedetector'
__author__ = 'LuxLuth'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2022 LuxLuth'
__version__ = '0.1.3'


from . import detectchange
from . import colors
from . import purcent
from . import menu
from . import wrapperComponents
from . import wrs
from . import wro
