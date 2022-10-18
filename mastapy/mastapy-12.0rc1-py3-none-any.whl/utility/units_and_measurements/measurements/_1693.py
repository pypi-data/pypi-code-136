"""_1693.py

TorquePerCurrent
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_TORQUE_PER_CURRENT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'TorquePerCurrent')


__docformat__ = 'restructuredtext en'
__all__ = ('TorquePerCurrent',)


class TorquePerCurrent(_1570.MeasurementBase):
    """TorquePerCurrent

    This is a mastapy class.
    """

    TYPE = _TORQUE_PER_CURRENT

    def __init__(self, instance_to_wrap: 'TorquePerCurrent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
