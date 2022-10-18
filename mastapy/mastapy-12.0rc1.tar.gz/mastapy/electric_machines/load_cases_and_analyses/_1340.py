"""_1340.py

SpeedPointsDistribution
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_SPEED_POINTS_DISTRIBUTION = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'SpeedPointsDistribution')


__docformat__ = 'restructuredtext en'
__all__ = ('SpeedPointsDistribution',)


class SpeedPointsDistribution(Enum):
    """SpeedPointsDistribution

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SPEED_POINTS_DISTRIBUTION

    LINEAR = 0
    USER_DEFINED = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


SpeedPointsDistribution.__setattr__ = __enum_setattr
SpeedPointsDistribution.__delattr__ = __enum_delattr
