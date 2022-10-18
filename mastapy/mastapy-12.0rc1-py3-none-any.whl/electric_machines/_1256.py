"""_1256.py

FluxBarrierStyle
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_FLUX_BARRIER_STYLE = python_net_import('SMT.MastaAPI.ElectricMachines', 'FluxBarrierStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('FluxBarrierStyle',)


class FluxBarrierStyle(Enum):
    """FluxBarrierStyle

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FLUX_BARRIER_STYLE

    BRIDGE = 0
    CIRCULAR = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


FluxBarrierStyle.__setattr__ = __enum_setattr
FluxBarrierStyle.__delattr__ = __enum_delattr
