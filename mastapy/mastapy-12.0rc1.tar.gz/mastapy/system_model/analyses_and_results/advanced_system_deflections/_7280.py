"""_7280.py

PartToPartShearCouplingAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2539
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6857
from mastapy.system_model.analyses_and_results.system_deflections import _2734
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7235
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'PartToPartShearCouplingAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingAdvancedSystemDeflection',)


class PartToPartShearCouplingAdvancedSystemDeflection(_7235.CouplingAdvancedSystemDeflection):
    """PartToPartShearCouplingAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self) -> '_6857.PartToPartShearCouplingLoadCase':
        """PartToPartShearCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2734.PartToPartShearCouplingSystemDeflection]':
        """List[PartToPartShearCouplingSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
