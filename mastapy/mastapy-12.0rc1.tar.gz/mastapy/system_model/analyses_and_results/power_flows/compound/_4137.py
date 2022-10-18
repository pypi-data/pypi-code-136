"""_4137.py

ConceptCouplingHalfCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2533
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4003
from mastapy.system_model.analyses_and_results.power_flows.compound import _4148
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'ConceptCouplingHalfCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingHalfCompoundPowerFlow',)


class ConceptCouplingHalfCompoundPowerFlow(_4148.CouplingHalfCompoundPowerFlow):
    """ConceptCouplingHalfCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_COMPOUND_POWER_FLOW

    def __init__(self, instance_to_wrap: 'ConceptCouplingHalfCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2533.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4003.ConceptCouplingHalfPowerFlow]':
        """List[ConceptCouplingHalfPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4003.ConceptCouplingHalfPowerFlow]':
        """List[ConceptCouplingHalfPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
