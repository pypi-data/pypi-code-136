# -*- coding: utf-8 -*-
# Copyright 2006 St James Software

"""Really simple dimension for wrapping a dictionary of resources."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from future import standard_library
standard_library.install_aliases()
from builtins import *
from j5test.IterativeTester import Dimension

class DictDim(Dimension):
    """A *really* simple dimension object for iterating over a dictionary.
       The keys of the dictionary given to __init__ are the resource names,
       the values are the resources.
       """

    def __init__(self,dct):
        self._resources = dct.copy()
