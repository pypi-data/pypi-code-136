"""_7452.py

VirtualComponentCompoundAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7323
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7407
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'VirtualComponentCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentCompoundAdvancedSystemDeflection',)


class VirtualComponentCompoundAdvancedSystemDeflection(_7407.MountableComponentCompoundAdvancedSystemDeflection):
    """VirtualComponentCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'VirtualComponentCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_7323.VirtualComponentAdvancedSystemDeflection]':
        """List[VirtualComponentAdvancedSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_7323.VirtualComponentAdvancedSystemDeflection]':
        """List[VirtualComponentAdvancedSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
