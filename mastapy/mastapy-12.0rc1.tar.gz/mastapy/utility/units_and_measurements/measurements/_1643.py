"""_1643.py

MagneticFlux
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_MAGNETIC_FLUX = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'MagneticFlux')


__docformat__ = 'restructuredtext en'
__all__ = ('MagneticFlux',)


class MagneticFlux(_1570.MeasurementBase):
    """MagneticFlux

    This is a mastapy class.
    """

    TYPE = _MAGNETIC_FLUX

    def __init__(self, instance_to_wrap: 'MagneticFlux.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
