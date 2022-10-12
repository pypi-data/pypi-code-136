from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import str
from builtins import *
from j5test.IterativeTester import Dimension

class ArrayDim(Dimension):
    """This is a very simple Dimension which just gives the members of an array"""
    def __init__(self, initarray):
        self._resources = {}
        self._failed_conditions = {}
        for num, member in enumerate(initarray):
            self._resources[str(num)] = member

