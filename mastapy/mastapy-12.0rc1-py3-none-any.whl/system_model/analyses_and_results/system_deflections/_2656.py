"""_2656.py

BoltSystemDeflection
"""


from mastapy.system_model.part_model import _2394
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6758
from mastapy.system_model.analyses_and_results.power_flows import _3996
from mastapy.system_model.analyses_and_results.system_deflections import _2661
from mastapy._internal.python_net import python_net_import

_BOLT_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BoltSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltSystemDeflection',)


class BoltSystemDeflection(_2661.ComponentSystemDeflection):
    """BoltSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BOLT_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'BoltSystemDeflection.TYPE'):
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
    def power_flow_results(self) -> '_3996.BoltPowerFlow':
        """BoltPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
