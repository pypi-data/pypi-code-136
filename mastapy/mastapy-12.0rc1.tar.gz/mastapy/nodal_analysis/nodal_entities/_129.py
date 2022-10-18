"""_129.py

ShearAreaFactorMethod
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_SHEAR_AREA_FACTOR_METHOD = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'ShearAreaFactorMethod')


__docformat__ = 'restructuredtext en'
__all__ = ('ShearAreaFactorMethod',)


class ShearAreaFactorMethod(Enum):
    """ShearAreaFactorMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SHEAR_AREA_FACTOR_METHOD

    _109 = 0
    LINEAR_BETWEEN_109_SOLID_AND_2_THIN_WALLED = 1
    LINEAR_BETWEEN_1089_SOLID_AND_1053_THIN_WALLED = 2
    HOOGENBOOM_PAPER = 3
    EULERBERNOULLI = 4
    _1 = 5
    _2 = 6
    STEINBOECK = 7


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


ShearAreaFactorMethod.__setattr__ = __enum_setattr
ShearAreaFactorMethod.__delattr__ = __enum_delattr
