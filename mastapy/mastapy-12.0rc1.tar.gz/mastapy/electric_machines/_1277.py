"""_1277.py

RotorType
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_ROTOR_TYPE = python_net_import('SMT.MastaAPI.ElectricMachines', 'RotorType')


__docformat__ = 'restructuredtext en'
__all__ = ('RotorType',)


class RotorType(Enum):
    """RotorType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ROTOR_TYPE

    VSHAPED = 0
    USHAPED = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


RotorType.__setattr__ = __enum_setattr
RotorType.__delattr__ = __enum_delattr
