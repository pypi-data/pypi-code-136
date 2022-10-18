"""_2107.py

FatigueLoadLimitCalculationMethodEnum
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_FATIGUE_LOAD_LIMIT_CALCULATION_METHOD_ENUM = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'FatigueLoadLimitCalculationMethodEnum')


__docformat__ = 'restructuredtext en'
__all__ = ('FatigueLoadLimitCalculationMethodEnum',)


class FatigueLoadLimitCalculationMethodEnum(Enum):
    """FatigueLoadLimitCalculationMethodEnum

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FATIGUE_LOAD_LIMIT_CALCULATION_METHOD_ENUM

    BASIC = 0
    ADVANCED = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


FatigueLoadLimitCalculationMethodEnum.__setattr__ = __enum_setattr
FatigueLoadLimitCalculationMethodEnum.__delattr__ = __enum_delattr
