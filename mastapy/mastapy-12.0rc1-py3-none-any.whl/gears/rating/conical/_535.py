"""_535.py

ConicalGearSetRating
"""


from mastapy.gears.gear_designs import _936
from mastapy._internal import constructor
from mastapy.gears.rating import _357
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetRating',)


class ConicalGearSetRating(_357.GearSetRating):
    """ConicalGearSetRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_RATING

    def __init__(self, instance_to_wrap: 'ConicalGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating_settings(self) -> '_936.BevelHypoidGearRatingSettingsItem':
        """BevelHypoidGearRatingSettingsItem: 'RatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
