"""_1623.py

Inductance
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_INDUCTANCE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Inductance')


__docformat__ = 'restructuredtext en'
__all__ = ('Inductance',)


class Inductance(_1570.MeasurementBase):
    """Inductance

    This is a mastapy class.
    """

    TYPE = _INDUCTANCE

    def __init__(self, instance_to_wrap: 'Inductance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
