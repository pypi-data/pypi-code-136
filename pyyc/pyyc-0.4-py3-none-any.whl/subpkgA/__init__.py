"""
Documentation for sub-package `subpkgA`.
"""

__all__ = ['modA1', 'modA2']  # modules imported by `import *`

for _mod in __all__:
    __import__(__name__ + '.' + _mod, fromlist=[None])  # ≈ 'from __name__ import _mod'
