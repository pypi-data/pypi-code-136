"""_1336.py

OperatingPointsSpecificationMethod
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_OPERATING_POINTS_SPECIFICATION_METHOD = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'OperatingPointsSpecificationMethod')


__docformat__ = 'restructuredtext en'
__all__ = ('OperatingPointsSpecificationMethod',)


class OperatingPointsSpecificationMethod(Enum):
    """OperatingPointsSpecificationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _OPERATING_POINTS_SPECIFICATION_METHOD

    USER_DEFINED = 0
    ALONG_MAXIMUM_SPEED_TORQUE_CURVE = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


OperatingPointsSpecificationMethod.__setattr__ = __enum_setattr
OperatingPointsSpecificationMethod.__delattr__ = __enum_delattr
