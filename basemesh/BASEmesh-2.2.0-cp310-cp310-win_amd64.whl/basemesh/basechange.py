"""Dummy for the BASEchange module.

BASEchange will be relocated to the BASEtools package in the near
future, which will make it available as its own top-level module. This
module only serves to maintain the API established in BASEmesh v2.1 and
will always print a FutureWarning.
"""

import subprocess
import sys

import basechange

__all__ = [
    'basechange',
]

# TODO: Remove this module in BASEmesh v2.2.

# NOTE: Now using the "warnings.warn" module as we would have to monkey-patch
# the "formatwarning" function to hide the source line info, which is of no use
# to the user.
print('FutureWarning: The BASEchange module will be removed from the BASEmesh '
      'package in the future. Please target the BASEchange module directly, '
      'without the "basemesh." prefix.')


if __name__ == '__main__':
    subprocess.run([sys.executable, '-m', 'basechange'] + sys.argv[1:])
