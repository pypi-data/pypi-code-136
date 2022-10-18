"""_1295.py

WireSizeSpecificationMethod
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_WIRE_SIZE_SPECIFICATION_METHOD = python_net_import('SMT.MastaAPI.ElectricMachines', 'WireSizeSpecificationMethod')


__docformat__ = 'restructuredtext en'
__all__ = ('WireSizeSpecificationMethod',)


class WireSizeSpecificationMethod(Enum):
    """WireSizeSpecificationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _WIRE_SIZE_SPECIFICATION_METHOD

    AWG = 0
    IEC_60228 = 1
    USER_SPECIFIED = 2


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


WireSizeSpecificationMethod.__setattr__ = __enum_setattr
WireSizeSpecificationMethod.__delattr__ = __enum_delattr
