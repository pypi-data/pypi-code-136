"""_2817.py

BoltedJointCompoundSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model import _2395
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2655
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2897
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'BoltedJointCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointCompoundSystemDeflection',)


class BoltedJointCompoundSystemDeflection(_2897.SpecialisedAssemblyCompoundSystemDeflection):
    """BoltedJointCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_COMPOUND_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'BoltedJointCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2395.BoltedJoint':
        """BoltedJoint: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2395.BoltedJoint':
        """BoltedJoint: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2655.BoltedJointSystemDeflection]':
        """List[BoltedJointSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2655.BoltedJointSystemDeflection]':
        """List[BoltedJointSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
