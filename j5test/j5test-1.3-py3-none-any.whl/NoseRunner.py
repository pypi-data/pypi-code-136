from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *
import nose
import sys

if __name__ == '__main__':
    sys.path.append('.')
    nose.core.main()
