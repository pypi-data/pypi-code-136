"""_4086.py

StraightBevelDiffGearSetPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.gears import _2497
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6887
from mastapy.gears.rating.straight_bevel_diff import _394
from mastapy.system_model.analyses_and_results.power_flows import _4085, _4084, _3994
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'StraightBevelDiffGearSetPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetPowerFlow',)


class StraightBevelDiffGearSetPowerFlow(_3994.BevelGearSetPowerFlow):
    """StraightBevelDiffGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_POWER_FLOW

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2497.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6887.StraightBevelDiffGearSetLoadCase':
        """StraightBevelDiffGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_394.StraightBevelDiffGearSetRating':
        """StraightBevelDiffGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_394.StraightBevelDiffGearSetRating':
        """StraightBevelDiffGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears_power_flow(self) -> 'List[_4085.StraightBevelDiffGearPowerFlow]':
        """List[StraightBevelDiffGearPowerFlow]: 'GearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_gears_power_flow(self) -> 'List[_4085.StraightBevelDiffGearPowerFlow]':
        """List[StraightBevelDiffGearPowerFlow]: 'StraightBevelDiffGearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes_power_flow(self) -> 'List[_4084.StraightBevelDiffGearMeshPowerFlow]':
        """List[StraightBevelDiffGearMeshPowerFlow]: 'MeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_meshes_power_flow(self) -> 'List[_4084.StraightBevelDiffGearMeshPowerFlow]':
        """List[StraightBevelDiffGearMeshPowerFlow]: 'StraightBevelDiffMeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
