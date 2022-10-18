"""_3764.py

FaceGearSetStabilityAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2480
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6812
from mastapy.system_model.analyses_and_results.stability_analyses import _3765, _3763, _3769
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'FaceGearSetStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetStabilityAnalysis',)


class FaceGearSetStabilityAnalysis(_3769.GearSetStabilityAnalysis):
    """FaceGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_STABILITY_ANALYSIS

    def __init__(self, instance_to_wrap: 'FaceGearSetStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2480.FaceGearSet':
        """FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6812.FaceGearSetLoadCase':
        """FaceGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_gears_stability_analysis(self) -> 'List[_3765.FaceGearStabilityAnalysis]':
        """List[FaceGearStabilityAnalysis]: 'FaceGearsStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_stability_analysis(self) -> 'List[_3763.FaceGearMeshStabilityAnalysis]':
        """List[FaceGearMeshStabilityAnalysis]: 'FaceMeshesStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
