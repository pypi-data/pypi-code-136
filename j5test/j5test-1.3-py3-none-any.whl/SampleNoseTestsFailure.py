# -*- coding: utf-8 -*-

"""Helper module for nose tests helper"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from future import standard_library
standard_library.install_aliases()
from builtins import *
def test_must_fail():
    """check that failures are caught"""
    assert False


