"""_551.py

AGMASpiralBevelMeshSingleFlankRating
"""


from typing import List

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.bevel.standards import _550, _555
from mastapy._internal.python_net import python_net_import

_AGMA_SPIRAL_BEVEL_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Bevel.Standards', 'AGMASpiralBevelMeshSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMASpiralBevelMeshSingleFlankRating',)


class AGMASpiralBevelMeshSingleFlankRating(_555.SpiralBevelMeshSingleFlankRating):
    """AGMASpiralBevelMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _AGMA_SPIRAL_BEVEL_MESH_SINGLE_FLANK_RATING

    def __init__(self, instance_to_wrap: 'AGMASpiralBevelMeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CrowningFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CrowningFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @property
    def rating_standard_name(self) -> 'str':
        """str: 'RatingStandardName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ''

        return temp

    @property
    def gear_single_flank_ratings(self) -> 'List[_550.AGMASpiralBevelGearSingleFlankRating]':
        """List[AGMASpiralBevelGearSingleFlankRating]: 'GearSingleFlankRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def agma_bevel_gear_single_flank_ratings(self) -> 'List[_550.AGMASpiralBevelGearSingleFlankRating]':
        """List[AGMASpiralBevelGearSingleFlankRating]: 'AGMABevelGearSingleFlankRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AGMABevelGearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
