"""_1339.py

SpecifyTorqueOrCurrent
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_SPECIFY_TORQUE_OR_CURRENT = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'SpecifyTorqueOrCurrent')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecifyTorqueOrCurrent',)


class SpecifyTorqueOrCurrent(Enum):
    """SpecifyTorqueOrCurrent

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SPECIFY_TORQUE_OR_CURRENT

    TARGET_TORQUE = 0
    MAXIMUM_TORQUE = 1
    CURRENT_AND_CURRENT_ANGLE = 2


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


SpecifyTorqueOrCurrent.__setattr__ = __enum_setattr
SpecifyTorqueOrCurrent.__delattr__ = __enum_delattr
