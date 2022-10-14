"""
Documentation du module subpkgB.mod.
"""

from ..subpkgA import modA1  # import relatif

version = 'sous-package B module' + ' + ' + modA1.version
print("Initialisation", version)
