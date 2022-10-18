"""_1688.py

TimeShort
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_TIME_SHORT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'TimeShort')


__docformat__ = 'restructuredtext en'
__all__ = ('TimeShort',)


class TimeShort(_1570.MeasurementBase):
    """TimeShort

    This is a mastapy class.
    """

    TYPE = _TIME_SHORT

    def __init__(self, instance_to_wrap: 'TimeShort.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
