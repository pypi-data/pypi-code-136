# NB: this module should never be loaded, since we'll see the subpkg_with_init package dir first
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


def thingtocall():
    raise Exception('this should never be called (loaded discrete module instead of package module)')


def anotherthingtocall():
    raise Exception('this should never be called (loaded discrete module instead of package module)')
