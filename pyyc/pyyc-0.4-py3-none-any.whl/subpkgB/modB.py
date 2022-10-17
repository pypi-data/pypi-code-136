"""
Documentation for module `subpkgB.modB`.
"""

from ..subpkgA import modA1  # relative import

version = 'sub-package B module' + ' + ' + modA1.version
print("Initialization", version)
