"""_1652.py

MomentPerUnitPressure
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_MOMENT_PER_UNIT_PRESSURE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'MomentPerUnitPressure')


__docformat__ = 'restructuredtext en'
__all__ = ('MomentPerUnitPressure',)


class MomentPerUnitPressure(_1570.MeasurementBase):
    """MomentPerUnitPressure

    This is a mastapy class.
    """

    TYPE = _MOMENT_PER_UNIT_PRESSURE

    def __init__(self, instance_to_wrap: 'MomentPerUnitPressure.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
