"""_4101.py

UnbalancedMassPowerFlow
"""


from mastapy.system_model.part_model import _2429
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6906
from mastapy.system_model.analyses_and_results.power_flows import _4102
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'UnbalancedMassPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassPowerFlow',)


class UnbalancedMassPowerFlow(_4102.VirtualComponentPowerFlow):
    """UnbalancedMassPowerFlow

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_POWER_FLOW

    def __init__(self, instance_to_wrap: 'UnbalancedMassPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2429.UnbalancedMass':
        """UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6906.UnbalancedMassLoadCase':
        """UnbalancedMassLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
