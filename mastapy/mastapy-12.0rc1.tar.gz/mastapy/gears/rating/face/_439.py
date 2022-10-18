"""_439.py

FaceGearDutyCycleRating
"""


from mastapy.gears.rating import _353, _352
from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical import _450, _451
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Face', 'FaceGearDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearDutyCycleRating',)


class FaceGearDutyCycleRating(_352.GearDutyCycleRating):
    """FaceGearDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_DUTY_CYCLE_RATING

    def __init__(self, instance_to_wrap: 'FaceGearDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank_rating(self) -> '_353.GearFlankRating':
        """GearFlankRating: 'LeftFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankRating

        if temp is None:
            return None

        if _353.GearFlankRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast left_flank_rating to GearFlankRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank_rating(self) -> '_353.GearFlankRating':
        """GearFlankRating: 'RightFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankRating

        if temp is None:
            return None

        if _353.GearFlankRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast right_flank_rating to GearFlankRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
