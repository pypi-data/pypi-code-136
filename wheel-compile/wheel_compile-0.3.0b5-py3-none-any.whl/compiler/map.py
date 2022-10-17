from collections import OrderedDict
from contextlib import suppress
from typing import OrderedDict as OrderedDictType, Type

from .abc import AbstractPackageCompiler
from .native import NativePackageCompiler

__all__ = [
    'COMPILATOR_MAP',
]

COMPILATOR_MAP: OrderedDictType[
    str, Type[AbstractPackageCompiler],
] = OrderedDict((
    ('py_compile', NativePackageCompiler),
))


with suppress(ImportError):
    from .cython import CythonPackageCompiler

    COMPILATOR_MAP['cython'] = CythonPackageCompiler
