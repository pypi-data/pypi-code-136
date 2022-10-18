"""_1828.py

ColourMapOption
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_COLOUR_MAP_OPTION = python_net_import('SMT.MastaAPI.UtilityGUI.Charts.Colour', 'ColourMapOption')


__docformat__ = 'restructuredtext en'
__all__ = ('ColourMapOption',)


class ColourMapOption(Enum):
    """ColourMapOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _COLOUR_MAP_OPTION

    MORGENSTEMNING = 0
    KINDLMANN = 1
    JET = 2
    GREYSCALE = 3


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


ColourMapOption.__setattr__ = __enum_setattr
ColourMapOption.__delattr__ = __enum_delattr
