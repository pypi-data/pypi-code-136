"""_1644.py

MagneticFluxDensity
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_MAGNETIC_FLUX_DENSITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'MagneticFluxDensity')


__docformat__ = 'restructuredtext en'
__all__ = ('MagneticFluxDensity',)


class MagneticFluxDensity(_1570.MeasurementBase):
    """MagneticFluxDensity

    This is a mastapy class.
    """

    TYPE = _MAGNETIC_FLUX_DENSITY

    def __init__(self, instance_to_wrap: 'MagneticFluxDensity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
