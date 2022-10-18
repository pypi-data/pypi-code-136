"""_1347.py

ForceDisplayOption
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_FORCE_DISPLAY_OPTION = python_net_import('SMT.MastaAPI.ElectricMachines.HarmonicLoadData', 'ForceDisplayOption')


__docformat__ = 'restructuredtext en'
__all__ = ('ForceDisplayOption',)


class ForceDisplayOption(Enum):
    """ForceDisplayOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FORCE_DISPLAY_OPTION

    INDIVIDUAL = 0
    ALL = 1
    SUM = 2


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


ForceDisplayOption.__setattr__ = __enum_setattr
ForceDisplayOption.__delattr__ = __enum_delattr
