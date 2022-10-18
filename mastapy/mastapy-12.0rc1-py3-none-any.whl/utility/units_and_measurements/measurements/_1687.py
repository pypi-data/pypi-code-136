"""_1687.py

Time
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_TIME = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Time')


__docformat__ = 'restructuredtext en'
__all__ = ('Time',)


class Time(_1570.MeasurementBase):
    """Time

    This is a mastapy class.
    """

    TYPE = _TIME

    def __init__(self, instance_to_wrap: 'Time.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
