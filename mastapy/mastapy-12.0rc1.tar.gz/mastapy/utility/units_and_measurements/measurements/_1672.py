"""_1672.py

RescaledMeasurement
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_RESCALED_MEASUREMENT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'RescaledMeasurement')


__docformat__ = 'restructuredtext en'
__all__ = ('RescaledMeasurement',)


class RescaledMeasurement(_1570.MeasurementBase):
    """RescaledMeasurement

    This is a mastapy class.
    """

    TYPE = _RESCALED_MEASUREMENT

    def __init__(self, instance_to_wrap: 'RescaledMeasurement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
