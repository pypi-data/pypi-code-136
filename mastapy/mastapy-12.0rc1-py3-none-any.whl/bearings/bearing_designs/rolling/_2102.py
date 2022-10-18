"""_2102.py

CageBridgeShape
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_CAGE_BRIDGE_SHAPE = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'CageBridgeShape')


__docformat__ = 'restructuredtext en'
__all__ = ('CageBridgeShape',)


class CageBridgeShape(Enum):
    """CageBridgeShape

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CAGE_BRIDGE_SHAPE

    FLAT = 0
    CURVED = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


CageBridgeShape.__setattr__ = __enum_setattr
CageBridgeShape.__delattr__ = __enum_delattr
