"""_1714.py

SMTChartPointShape
"""


from enum import Enum

from mastapy._internal.python_net import python_net_import

_SMT_CHART_POINT_SHAPE = python_net_import('SMT.MastaAPI.Utility.Report', 'SMTChartPointShape')


__docformat__ = 'restructuredtext en'
__all__ = ('SMTChartPointShape',)


class SMTChartPointShape(Enum):
    """SMTChartPointShape

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SMT_CHART_POINT_SHAPE

    CIRCLE = 0
    ARROW_UP = 1
    ARROW_DOWN = 2
    SQUARE_OPEN = 3
    SQUARE_FILL = 4
    DIAGONAL_CROSS = 5


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


SMTChartPointShape.__setattr__ = __enum_setattr
SMTChartPointShape.__delattr__ = __enum_delattr
