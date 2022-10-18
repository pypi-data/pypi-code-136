"""_1458.py

ComplexMatrix
"""


from mastapy.math_utility import _1477
from mastapy._internal.python_net import python_net_import

_COMPLEX_MATRIX = python_net_import('SMT.MastaAPI.MathUtility', 'ComplexMatrix')


__docformat__ = 'restructuredtext en'
__all__ = ('ComplexMatrix',)


class ComplexMatrix(_1477.GenericMatrix['complex', 'ComplexMatrix']):
    """ComplexMatrix

    This is a mastapy class.
    """

    TYPE = _COMPLEX_MATRIX

    def __init__(self, instance_to_wrap: 'ComplexMatrix.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
