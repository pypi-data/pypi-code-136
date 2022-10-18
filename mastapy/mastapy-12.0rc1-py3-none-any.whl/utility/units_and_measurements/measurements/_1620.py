"""_1620.py

HeatTransferResistance
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_HEAT_TRANSFER_RESISTANCE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'HeatTransferResistance')


__docformat__ = 'restructuredtext en'
__all__ = ('HeatTransferResistance',)


class HeatTransferResistance(_1570.MeasurementBase):
    """HeatTransferResistance

    This is a mastapy class.
    """

    TYPE = _HEAT_TRANSFER_RESISTANCE

    def __init__(self, instance_to_wrap: 'HeatTransferResistance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
