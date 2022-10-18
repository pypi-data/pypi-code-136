"""_1255.py

FluxBarrierOrWeb
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_FLUX_BARRIER_OR_WEB = python_net_import('SMT.MastaAPI.ElectricMachines', 'FluxBarrierOrWeb')


__docformat__ = 'restructuredtext en'
__all__ = ('FluxBarrierOrWeb',)


class FluxBarrierOrWeb(Enum):
    """FluxBarrierOrWeb

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FLUX_BARRIER_OR_WEB

    FLUX_BARRIER = 0
    WEB = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


FluxBarrierOrWeb.__setattr__ = __enum_setattr
FluxBarrierOrWeb.__delattr__ = __enum_delattr
