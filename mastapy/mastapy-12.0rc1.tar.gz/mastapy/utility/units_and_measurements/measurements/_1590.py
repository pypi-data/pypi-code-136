"""_1590.py

CurrentDensity
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_CURRENT_DENSITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'CurrentDensity')


__docformat__ = 'restructuredtext en'
__all__ = ('CurrentDensity',)


class CurrentDensity(_1570.MeasurementBase):
    """CurrentDensity

    This is a mastapy class.
    """

    TYPE = _CURRENT_DENSITY

    def __init__(self, instance_to_wrap: 'CurrentDensity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
