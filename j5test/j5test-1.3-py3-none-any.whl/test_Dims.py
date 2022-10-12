from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *
from j5test import ArrayDim, BrowserDim, DictDim

def test_array_dim():
    array_dim = ArrayDim.ArrayDim(['A', 'B', 'C'])
    browser_dim = BrowserDim.BrowserDim()
    dict_dim = DictDim.DictDim({'A': 1, 'B': 2, 'C': 3})
