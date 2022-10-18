"""_2726.py

MeasurementComponentSystemDeflection
"""


from mastapy.system_model.part_model import _2415
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6848
from mastapy.system_model.analyses_and_results.power_flows import _4053
from mastapy.system_model.analyses_and_results.system_deflections import _2781
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'MeasurementComponentSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentSystemDeflection',)


class MeasurementComponentSystemDeflection(_2781.VirtualComponentSystemDeflection):
    """MeasurementComponentSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'MeasurementComponentSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2415.MeasurementComponent':
        """MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6848.MeasurementComponentLoadCase':
        """MeasurementComponentLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4053.MeasurementComponentPowerFlow':
        """MeasurementComponentPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
