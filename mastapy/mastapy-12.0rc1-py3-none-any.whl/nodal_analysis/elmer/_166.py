"""_166.py

ElectricMachineAnalysisPeriod
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_ANALYSIS_PERIOD = python_net_import('SMT.MastaAPI.NodalAnalysis.Elmer', 'ElectricMachineAnalysisPeriod')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineAnalysisPeriod',)


class ElectricMachineAnalysisPeriod(Enum):
    """ElectricMachineAnalysisPeriod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ELECTRIC_MACHINE_ANALYSIS_PERIOD

    ELECTRICAL_PERIOD = 0
    HALF_ELECTRICAL_PERIOD = 1
    MECHANICAL_PERIOD = 2
    SLOT_PASSING_PERIOD = 3


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


ElectricMachineAnalysisPeriod.__setattr__ = __enum_setattr
ElectricMachineAnalysisPeriod.__delattr__ = __enum_delattr
