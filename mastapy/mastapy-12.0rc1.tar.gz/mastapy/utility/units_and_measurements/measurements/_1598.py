"""_1598.py

ElectricalResistance
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_ELECTRICAL_RESISTANCE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'ElectricalResistance')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricalResistance',)


class ElectricalResistance(_1570.MeasurementBase):
    """ElectricalResistance

    This is a mastapy class.
    """

    TYPE = _ELECTRICAL_RESISTANCE

    def __init__(self, instance_to_wrap: 'ElectricalResistance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
