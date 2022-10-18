"""_1273.py

RegionID
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_REGION_ID = python_net_import('SMT.MastaAPI.ElectricMachines', 'RegionID')


__docformat__ = 'restructuredtext en'
__all__ = ('RegionID',)


class RegionID(Enum):
    """RegionID

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _REGION_ID

    STATOR_CORE = 0
    STATOR_SLOT = 1
    STATOR_WEDGE = 2
    REGION_BETWEEN_WEDGE_AND_AIR_GAP = 3
    AIR_GAP_STATOR_SIDE = 4
    ROTOR_CORE = 5
    ROTOR_AIR_REGION = 6
    MAGNET = 7
    AIR_GAP_ROTOR_SIDE = 8
    SHAFT = 9


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


RegionID.__setattr__ = __enum_setattr
RegionID.__delattr__ = __enum_delattr
