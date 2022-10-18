"""_394.py

StraightBevelDiffGearSetRating
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.straight_bevel_diff import _960
from mastapy.gears.rating.straight_bevel_diff import _393, _392
from mastapy.gears.rating.conical import _535
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.StraightBevelDiff', 'StraightBevelDiffGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetRating',)


class StraightBevelDiffGearSetRating(_535.ConicalGearSetRating):
    """StraightBevelDiffGearSetRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_RATING

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> 'str':
        """str: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return ''

        return temp

    @property
    def straight_bevel_diff_gear_set(self) -> '_960.StraightBevelDiffGearSetDesign':
        """StraightBevelDiffGearSetDesign: 'StraightBevelDiffGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_diff_gear_ratings(self) -> 'List[_393.StraightBevelDiffGearRating]':
        """List[StraightBevelDiffGearRating]: 'StraightBevelDiffGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_mesh_ratings(self) -> 'List[_392.StraightBevelDiffGearMeshRating]':
        """List[StraightBevelDiffGearMeshRating]: 'StraightBevelDiffMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
