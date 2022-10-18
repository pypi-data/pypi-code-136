"""_1268.py

NotchShape
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_NOTCH_SHAPE = python_net_import('SMT.MastaAPI.ElectricMachines', 'NotchShape')


__docformat__ = 'restructuredtext en'
__all__ = ('NotchShape',)


class NotchShape(Enum):
    """NotchShape

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _NOTCH_SHAPE

    TYPE_1 = 0
    TYPE_2 = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


NotchShape.__setattr__ = __enum_setattr
NotchShape.__delattr__ = __enum_delattr
