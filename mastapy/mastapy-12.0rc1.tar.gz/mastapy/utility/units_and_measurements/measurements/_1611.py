"""_1611.py

FractionMeasurementBase
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_FRACTION_MEASUREMENT_BASE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'FractionMeasurementBase')


__docformat__ = 'restructuredtext en'
__all__ = ('FractionMeasurementBase',)


class FractionMeasurementBase(_1570.MeasurementBase):
    """FractionMeasurementBase

    This is a mastapy class.
    """

    TYPE = _FRACTION_MEASUREMENT_BASE

    def __init__(self, instance_to_wrap: 'FractionMeasurementBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
