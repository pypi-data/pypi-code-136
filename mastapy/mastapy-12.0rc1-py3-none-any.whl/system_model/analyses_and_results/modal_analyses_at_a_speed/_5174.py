"""_5174.py

TorqueConverterPumpModalAnalysisAtASpeed
"""


from mastapy.system_model.part_model.couplings import _2559
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6900
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5093
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'TorqueConverterPumpModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpModalAnalysisAtASpeed',)


class TorqueConverterPumpModalAnalysisAtASpeed(_5093.CouplingHalfModalAnalysisAtASpeed):
    """TorqueConverterPumpModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_MODAL_ANALYSIS_AT_A_SPEED

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2559.TorqueConverterPump':
        """TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6900.TorqueConverterPumpLoadCase':
        """TorqueConverterPumpLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
