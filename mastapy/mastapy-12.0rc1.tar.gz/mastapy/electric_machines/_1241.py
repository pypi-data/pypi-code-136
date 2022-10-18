"""_1241.py

CoilPositionInSlot
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_COIL_POSITION_IN_SLOT = python_net_import('SMT.MastaAPI.ElectricMachines', 'CoilPositionInSlot')


__docformat__ = 'restructuredtext en'
__all__ = ('CoilPositionInSlot',)


class CoilPositionInSlot(Enum):
    """CoilPositionInSlot

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _COIL_POSITION_IN_SLOT

    CENTRE = 0
    LEFT = 1
    RIGHT = 2
    TOP = 3
    BOTTOM = 4


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


CoilPositionInSlot.__setattr__ = __enum_setattr
CoilPositionInSlot.__delattr__ = __enum_delattr
