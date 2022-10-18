"""_4089.py

StraightBevelGearSetPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.gears import _2499
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6890
from mastapy.gears.rating.straight_bevel import _391
from mastapy.system_model.analyses_and_results.power_flows import _4088, _4087, _3994
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'StraightBevelGearSetPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetPowerFlow',)


class StraightBevelGearSetPowerFlow(_3994.BevelGearSetPowerFlow):
    """StraightBevelGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_POWER_FLOW

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2499.StraightBevelGearSet':
        """StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6890.StraightBevelGearSetLoadCase':
        """StraightBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_391.StraightBevelGearSetRating':
        """StraightBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_391.StraightBevelGearSetRating':
        """StraightBevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears_power_flow(self) -> 'List[_4088.StraightBevelGearPowerFlow]':
        """List[StraightBevelGearPowerFlow]: 'GearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gears_power_flow(self) -> 'List[_4088.StraightBevelGearPowerFlow]':
        """List[StraightBevelGearPowerFlow]: 'StraightBevelGearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes_power_flow(self) -> 'List[_4087.StraightBevelGearMeshPowerFlow]':
        """List[StraightBevelGearMeshPowerFlow]: 'MeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes_power_flow(self) -> 'List[_4087.StraightBevelGearMeshPowerFlow]':
        """List[StraightBevelGearMeshPowerFlow]: 'StraightBevelMeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
