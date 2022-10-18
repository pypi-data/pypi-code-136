"""_401.py

KlingelnbergCycloPalloidSpiralBevelGearSetRating
"""


from typing import List

from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _968
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.klingelnberg_spiral_bevel import _400, _399
from mastapy.gears.rating.klingelnberg_conical import _407
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.KlingelnbergSpiralBevel', 'KlingelnbergCycloPalloidSpiralBevelGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearSetRating',)


class KlingelnbergCycloPalloidSpiralBevelGearSetRating(_407.KlingelnbergCycloPalloidConicalGearSetRating):
    """KlingelnbergCycloPalloidSpiralBevelGearSetRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_RATING

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_968.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'KlingelnbergCycloPalloidSpiralBevelGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_ratings(self) -> 'List[_400.KlingelnbergCycloPalloidSpiralBevelGearRating]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearRating]: 'KlingelnbergCycloPalloidSpiralBevelGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_mesh_ratings(self) -> 'List[_399.KlingelnbergCycloPalloidSpiralBevelGearMeshRating]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearMeshRating]: 'KlingelnbergCycloPalloidSpiralBevelMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
