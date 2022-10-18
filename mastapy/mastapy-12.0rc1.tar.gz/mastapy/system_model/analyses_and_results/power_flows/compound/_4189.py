"""_4189.py

PartToPartShearCouplingCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2539
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4059
from mastapy.system_model.analyses_and_results.power_flows.compound import _4146
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'PartToPartShearCouplingCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingCompoundPowerFlow',)


class PartToPartShearCouplingCompoundPowerFlow(_4146.CouplingCompoundPowerFlow):
    """PartToPartShearCouplingCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_COMPOUND_POWER_FLOW

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2539.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2539.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4059.PartToPartShearCouplingPowerFlow]':
        """List[PartToPartShearCouplingPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4059.PartToPartShearCouplingPowerFlow]':
        """List[PartToPartShearCouplingPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
