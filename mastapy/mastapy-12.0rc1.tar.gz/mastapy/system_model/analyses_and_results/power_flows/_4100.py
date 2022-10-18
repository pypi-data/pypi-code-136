"""_4100.py

TorqueConverterTurbinePowerFlow
"""


from mastapy.system_model.part_model.couplings import _2561
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6901
from mastapy.system_model.analyses_and_results.power_flows import _4014
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'TorqueConverterTurbinePowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbinePowerFlow',)


class TorqueConverterTurbinePowerFlow(_4014.CouplingHalfPowerFlow):
    """TorqueConverterTurbinePowerFlow

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_POWER_FLOW

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbinePowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2561.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6901.TorqueConverterTurbineLoadCase':
        """TorqueConverterTurbineLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
