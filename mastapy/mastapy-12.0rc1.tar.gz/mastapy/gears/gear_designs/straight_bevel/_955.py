"""_955.py

StraightBevelGearMeshDesign
"""


from typing import List

from mastapy.gears.gear_designs.straight_bevel import _956, _954, _957
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.bevel import _1171
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.StraightBevel', 'StraightBevelGearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearMeshDesign',)


class StraightBevelGearMeshDesign(_1171.BevelGearMeshDesign):
    """StraightBevelGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_DESIGN

    def __init__(self, instance_to_wrap: 'StraightBevelGearMeshDesign.TYPE'):
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
    def straight_bevel_gears(self) -> 'List[_954.StraightBevelGearDesign]':
        """List[StraightBevelGearDesign]: 'StraightBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshed_gears(self) -> 'List[_957.StraightBevelMeshedGearDesign]':
        """List[StraightBevelMeshedGearDesign]: 'StraightBevelMeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
