"""_1247.py

DQAxisConvention
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_DQ_AXIS_CONVENTION = python_net_import('SMT.MastaAPI.ElectricMachines', 'DQAxisConvention')


__docformat__ = 'restructuredtext en'
__all__ = ('DQAxisConvention',)


class DQAxisConvention(Enum):
    """DQAxisConvention

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _DQ_AXIS_CONVENTION

    PERMANENT_MAGNET = 0
    SYNCHRONOUS_RELUCTANCE = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


DQAxisConvention.__setattr__ = __enum_setattr
DQAxisConvention.__delattr__ = __enum_delattr
