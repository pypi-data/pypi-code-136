"""_6236.py

ConceptGearSetDynamicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2473
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6769
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6234, _6235, _6266
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'ConceptGearSetDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetDynamicAnalysis',)


class ConceptGearSetDynamicAnalysis(_6266.GearSetDynamicAnalysis):
    """ConceptGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_DYNAMIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'ConceptGearSetDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2473.ConceptGearSet':
        """ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6769.ConceptGearSetLoadCase':
        """ConceptGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gears_dynamic_analysis(self) -> 'List[_6234.ConceptGearDynamicAnalysis]':
        """List[ConceptGearDynamicAnalysis]: 'ConceptGearsDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes_dynamic_analysis(self) -> 'List[_6235.ConceptGearMeshDynamicAnalysis]':
        """List[ConceptGearMeshDynamicAnalysis]: 'ConceptMeshesDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
