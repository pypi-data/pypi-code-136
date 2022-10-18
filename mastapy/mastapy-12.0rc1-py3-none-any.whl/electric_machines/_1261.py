"""_1261.py

MagnetConfiguration
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_MAGNET_CONFIGURATION = python_net_import('SMT.MastaAPI.ElectricMachines', 'MagnetConfiguration')


__docformat__ = 'restructuredtext en'
__all__ = ('MagnetConfiguration',)


class MagnetConfiguration(Enum):
    """MagnetConfiguration

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MAGNET_CONFIGURATION

    NO_MAGNETS = 0
    INNER_MAGNETS_ONLY = 1
    OUTER_MAGNETS_ONLY = 2
    INNER_AND_OUTER_MAGNETS = 3


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


MagnetConfiguration.__setattr__ = __enum_setattr
MagnetConfiguration.__delattr__ = __enum_delattr
