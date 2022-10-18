"""_1287.py

ToothSlotStyle
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_TOOTH_SLOT_STYLE = python_net_import('SMT.MastaAPI.ElectricMachines', 'ToothSlotStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('ToothSlotStyle',)


class ToothSlotStyle(Enum):
    """ToothSlotStyle

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TOOTH_SLOT_STYLE

    PARALLEL_TOOTH = 0
    PARALLEL_SLOT = 1
    USER_DEFINED = 2


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


ToothSlotStyle.__setattr__ = __enum_setattr
ToothSlotStyle.__delattr__ = __enum_delattr
