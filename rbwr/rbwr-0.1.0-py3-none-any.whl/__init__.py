"""
Rather be writing Rust

A small Python library providing sum types that play well with existing typechecking
PEPs and should work out-of-the-box with any good typechecker, such as Pyright.
"""

from . import either, result
from .either import Either
from .result import Result

# Keep this list sorted lexicographically
__all__ = [
    "Either",
    "Result",
    "either",
    "result",
]
