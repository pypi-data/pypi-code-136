"""_1589.py

CarbonEmissionFactor
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_CARBON_EMISSION_FACTOR = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'CarbonEmissionFactor')


__docformat__ = 'restructuredtext en'
__all__ = ('CarbonEmissionFactor',)


class CarbonEmissionFactor(_1570.MeasurementBase):
    """CarbonEmissionFactor

    This is a mastapy class.
    """

    TYPE = _CARBON_EMISSION_FACTOR

    def __init__(self, instance_to_wrap: 'CarbonEmissionFactor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
