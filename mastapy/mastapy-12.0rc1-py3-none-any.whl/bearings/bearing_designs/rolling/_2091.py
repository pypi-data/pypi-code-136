"""_2091.py

AngularContactThrustBallBearing
"""


from mastapy._internal import constructor
from mastapy.bearings.bearing_designs.rolling import _2090
from mastapy._internal.python_net import python_net_import

_ANGULAR_CONTACT_THRUST_BALL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'AngularContactThrustBallBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('AngularContactThrustBallBearing',)


class AngularContactThrustBallBearing(_2090.AngularContactBallBearing):
    """AngularContactThrustBallBearing

    This is a mastapy class.
    """

    TYPE = _ANGULAR_CONTACT_THRUST_BALL_BEARING

    def __init__(self, instance_to_wrap: 'AngularContactThrustBallBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def width(self) -> 'float':
        """float: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    def width(self, value: 'float'):
        self.wrapped.Width = float(value) if value else 0.0
