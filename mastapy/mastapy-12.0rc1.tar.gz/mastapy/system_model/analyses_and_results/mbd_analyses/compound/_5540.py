"""_5540.py

MassDiscCompoundMultibodyDynamicsAnalysis
"""


from typing import List

from mastapy.system_model.part_model import _2414
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5396
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5587
from mastapy._internal.python_net import python_net_import

_MASS_DISC_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'MassDiscCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscCompoundMultibodyDynamicsAnalysis',)


class MassDiscCompoundMultibodyDynamicsAnalysis(_5587.VirtualComponentCompoundMultibodyDynamicsAnalysis):
    """MassDiscCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    def __init__(self, instance_to_wrap: 'MassDiscCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2414.MassDisc':
        """MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5396.MassDiscMultibodyDynamicsAnalysis]':
        """List[MassDiscMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[MassDiscCompoundMultibodyDynamicsAnalysis]':
        """List[MassDiscCompoundMultibodyDynamicsAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5396.MassDiscMultibodyDynamicsAnalysis]':
        """List[MassDiscMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
