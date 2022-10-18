"""_1646.py

MagnetomotiveForce
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_MAGNETOMOTIVE_FORCE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'MagnetomotiveForce')


__docformat__ = 'restructuredtext en'
__all__ = ('MagnetomotiveForce',)


class MagnetomotiveForce(_1570.MeasurementBase):
    """MagnetomotiveForce

    This is a mastapy class.
    """

    TYPE = _MAGNETOMOTIVE_FORCE

    def __init__(self, instance_to_wrap: 'MagnetomotiveForce.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
