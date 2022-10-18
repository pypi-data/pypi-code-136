"""_7216.py

BoltAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model import _2394
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6758
from mastapy.system_model.analyses_and_results.system_deflections import _2656
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7222
from mastapy._internal.python_net import python_net_import

_BOLT_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'BoltAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltAdvancedSystemDeflection',)


class BoltAdvancedSystemDeflection(_7222.ComponentAdvancedSystemDeflection):
    """BoltAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BOLT_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'BoltAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2394.Bolt':
        """Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6758.BoltLoadCase':
        """BoltLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2656.BoltSystemDeflection]':
        """List[BoltSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
