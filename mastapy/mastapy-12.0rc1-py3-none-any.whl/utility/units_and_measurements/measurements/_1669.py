"""_1669.py

PricePerUnitMass
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_PRICE_PER_UNIT_MASS = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'PricePerUnitMass')


__docformat__ = 'restructuredtext en'
__all__ = ('PricePerUnitMass',)


class PricePerUnitMass(_1570.MeasurementBase):
    """PricePerUnitMass

    This is a mastapy class.
    """

    TYPE = _PRICE_PER_UNIT_MASS

    def __init__(self, instance_to_wrap: 'PricePerUnitMass.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
