"""_1253.py

ElectricMachineType
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_TYPE = python_net_import('SMT.MastaAPI.ElectricMachines', 'ElectricMachineType')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineType',)


class ElectricMachineType(Enum):
    """ElectricMachineType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ELECTRIC_MACHINE_TYPE

    INTERIOR_PERMANENT_MAGNET = 0
    PERMANENT_MAGNET_ASSISTED_SYNCHRONOUS_RELUCTANCE = 1
    SYNCHRONOUS_RELUCTANCE = 2
    SURFACE_PERMANENT_MAGNET = 3


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


ElectricMachineType.__setattr__ = __enum_setattr
ElectricMachineType.__delattr__ = __enum_delattr
