"""_5009.py

PlanetaryConnectionCompoundModalAnalysisAtAStiffness
"""


from typing import List

from mastapy.system_model.connections_and_sockets import _2239
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4880
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5023
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'PlanetaryConnectionCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryConnectionCompoundModalAnalysisAtAStiffness',)


class PlanetaryConnectionCompoundModalAnalysisAtAStiffness(_5023.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness):
    """PlanetaryConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    def __init__(self, instance_to_wrap: 'PlanetaryConnectionCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2239.PlanetaryConnection':
        """PlanetaryConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2239.PlanetaryConnection':
        """PlanetaryConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4880.PlanetaryConnectionModalAnalysisAtAStiffness]':
        """List[PlanetaryConnectionModalAnalysisAtAStiffness]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4880.PlanetaryConnectionModalAnalysisAtAStiffness]':
        """List[PlanetaryConnectionModalAnalysisAtAStiffness]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
