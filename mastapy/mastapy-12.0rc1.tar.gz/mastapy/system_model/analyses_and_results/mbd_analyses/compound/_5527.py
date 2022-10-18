"""_5527.py

HypoidGearCompoundMultibodyDynamicsAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2485
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5380
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5469
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'HypoidGearCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearCompoundMultibodyDynamicsAnalysis',)


class HypoidGearCompoundMultibodyDynamicsAnalysis(_5469.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis):
    """HypoidGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    def __init__(self, instance_to_wrap: 'HypoidGearCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2485.HypoidGear':
        """HypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5380.HypoidGearMultibodyDynamicsAnalysis]':
        """List[HypoidGearMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5380.HypoidGearMultibodyDynamicsAnalysis]':
        """List[HypoidGearMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
