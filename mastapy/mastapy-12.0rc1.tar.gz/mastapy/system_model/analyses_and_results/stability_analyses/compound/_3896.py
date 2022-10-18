"""_3896.py

FaceGearSetCompoundStabilityAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2480
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3764
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3894, _3895, _3901
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'FaceGearSetCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetCompoundStabilityAnalysis',)


class FaceGearSetCompoundStabilityAnalysis(_3901.GearSetCompoundStabilityAnalysis):
    """FaceGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_COMPOUND_STABILITY_ANALYSIS

    def __init__(self, instance_to_wrap: 'FaceGearSetCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2480.FaceGearSet':
        """FaceGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def assembly_analysis_cases_ready(self) -> 'List[_3764.FaceGearSetStabilityAnalysis]':
        """List[FaceGearSetStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gears_compound_stability_analysis(self) -> 'List[_3894.FaceGearCompoundStabilityAnalysis]':
        """List[FaceGearCompoundStabilityAnalysis]: 'FaceGearsCompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_compound_stability_analysis(self) -> 'List[_3895.FaceGearMeshCompoundStabilityAnalysis]':
        """List[FaceGearMeshCompoundStabilityAnalysis]: 'FaceMeshesCompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3764.FaceGearSetStabilityAnalysis]':
        """List[FaceGearSetStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
