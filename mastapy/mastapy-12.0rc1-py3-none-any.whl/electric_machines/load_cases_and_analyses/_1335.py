"""_1335.py

NumberOfStepsPerOperatingPointSpecificationMethod
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_NUMBER_OF_STEPS_PER_OPERATING_POINT_SPECIFICATION_METHOD = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'NumberOfStepsPerOperatingPointSpecificationMethod')


__docformat__ = 'restructuredtext en'
__all__ = ('NumberOfStepsPerOperatingPointSpecificationMethod',)


class NumberOfStepsPerOperatingPointSpecificationMethod(Enum):
    """NumberOfStepsPerOperatingPointSpecificationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _NUMBER_OF_STEPS_PER_OPERATING_POINT_SPECIFICATION_METHOD

    NUMBER_OF_STEPS_FOR_THE_ANALYSIS_PERIOD = 0
    AT_LEAST_ONE_STEP_PER_MECHANICAL_DEGREE = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


NumberOfStepsPerOperatingPointSpecificationMethod.__setattr__ = __enum_setattr
NumberOfStepsPerOperatingPointSpecificationMethod.__delattr__ = __enum_delattr
