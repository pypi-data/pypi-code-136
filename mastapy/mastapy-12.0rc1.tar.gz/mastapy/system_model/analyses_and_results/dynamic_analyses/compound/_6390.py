"""_6390.py

FaceGearSetCompoundDynamicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2480
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6261
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6388, _6389, _6395
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'FaceGearSetCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetCompoundDynamicAnalysis',)


class FaceGearSetCompoundDynamicAnalysis(_6395.GearSetCompoundDynamicAnalysis):
    """FaceGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'FaceGearSetCompoundDynamicAnalysis.TYPE'):
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
    def assembly_analysis_cases_ready(self) -> 'List[_6261.FaceGearSetDynamicAnalysis]':
        """List[FaceGearSetDynamicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gears_compound_dynamic_analysis(self) -> 'List[_6388.FaceGearCompoundDynamicAnalysis]':
        """List[FaceGearCompoundDynamicAnalysis]: 'FaceGearsCompoundDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_compound_dynamic_analysis(self) -> 'List[_6389.FaceGearMeshCompoundDynamicAnalysis]':
        """List[FaceGearMeshCompoundDynamicAnalysis]: 'FaceMeshesCompoundDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6261.FaceGearSetDynamicAnalysis]':
        """List[FaceGearSetDynamicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
