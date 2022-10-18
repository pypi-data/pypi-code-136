"""_2094.py

AxialThrustNeedleRollerBearing
"""


from mastapy.bearings.bearing_designs.rolling import _2093
from mastapy._internal.python_net import python_net_import

_AXIAL_THRUST_NEEDLE_ROLLER_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'AxialThrustNeedleRollerBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('AxialThrustNeedleRollerBearing',)


class AxialThrustNeedleRollerBearing(_2093.AxialThrustCylindricalRollerBearing):
    """AxialThrustNeedleRollerBearing

    This is a mastapy class.
    """

    TYPE = _AXIAL_THRUST_NEEDLE_ROLLER_BEARING

    def __init__(self, instance_to_wrap: 'AxialThrustNeedleRollerBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
