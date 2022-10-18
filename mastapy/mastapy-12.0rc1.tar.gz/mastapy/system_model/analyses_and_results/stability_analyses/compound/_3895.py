"""_3895.py

FaceGearMeshCompoundStabilityAnalysis
"""


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2263
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3763
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3900
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'FaceGearMeshCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshCompoundStabilityAnalysis',)


class FaceGearMeshCompoundStabilityAnalysis(_3900.GearMeshCompoundStabilityAnalysis):
    """FaceGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS

    def __init__(self, instance_to_wrap: 'FaceGearMeshCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2263.FaceGearMesh':
        """FaceGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2263.FaceGearMesh':
        """FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3763.FaceGearMeshStabilityAnalysis]':
        """List[FaceGearMeshStabilityAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3763.FaceGearMeshStabilityAnalysis]':
        """List[FaceGearMeshStabilityAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
