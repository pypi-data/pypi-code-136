"""_6402.py

KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis
"""


from typing import List

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6273
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6368
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis',)


class KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis(_6368.ConicalGearMeshCompoundDynamicAnalysis):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_6273.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis]':
        """List[KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6273.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis]':
        """List[KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
