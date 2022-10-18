"""_5156.py

SpiralBevelGearSetModalAnalysisAtASpeed
"""


from typing import List

from mastapy.system_model.part_model.gears import _2495
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6881
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5155, _5154, _5073
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'SpiralBevelGearSetModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetModalAnalysisAtASpeed',)


class SpiralBevelGearSetModalAnalysisAtASpeed(_5073.BevelGearSetModalAnalysisAtASpeed):
    """SpiralBevelGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2495.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6881.SpiralBevelGearSetLoadCase':
        """SpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spiral_bevel_gears_modal_analysis_at_a_speed(self) -> 'List[_5155.SpiralBevelGearModalAnalysisAtASpeed]':
        """List[SpiralBevelGearModalAnalysisAtASpeed]: 'SpiralBevelGearsModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearsModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_meshes_modal_analysis_at_a_speed(self) -> 'List[_5154.SpiralBevelGearMeshModalAnalysisAtASpeed]':
        """List[SpiralBevelGearMeshModalAnalysisAtASpeed]: 'SpiralBevelMeshesModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelMeshesModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
