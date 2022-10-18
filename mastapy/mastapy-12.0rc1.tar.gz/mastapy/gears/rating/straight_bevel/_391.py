"""_391.py

StraightBevelGearSetRating
"""


from typing import List

from mastapy.gears.gear_designs.straight_bevel import _956
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.straight_bevel import _390, _389
from mastapy.gears.rating.bevel import _549
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.StraightBevel', 'StraightBevelGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetRating',)


class StraightBevelGearSetRating(_549.BevelGearSetRating):
    """StraightBevelGearSetRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_RATING

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def straight_bevel_gear_set(self) -> '_956.StraightBevelGearSetDesign':
        """StraightBevelGearSetDesign: 'StraightBevelGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_gear_ratings(self) -> 'List[_390.StraightBevelGearRating]':
        """List[StraightBevelGearRating]: 'StraightBevelGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_mesh_ratings(self) -> 'List[_389.StraightBevelGearMeshRating]':
        """List[StraightBevelGearMeshRating]: 'StraightBevelMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
