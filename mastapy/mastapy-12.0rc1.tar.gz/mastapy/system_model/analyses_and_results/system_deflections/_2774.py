"""_2774.py

TorqueConverterConnectionSystemDeflection
"""


from mastapy.system_model.connections_and_sockets.couplings import _2304
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6898
from mastapy.system_model.analyses_and_results.power_flows import _4097
from mastapy.system_model.analyses_and_results.system_deflections import _2675
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'TorqueConverterConnectionSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterConnectionSystemDeflection',)


class TorqueConverterConnectionSystemDeflection(_2675.CouplingConnectionSystemDeflection):
    """TorqueConverterConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'TorqueConverterConnectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2304.TorqueConverterConnection':
        """TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6898.TorqueConverterConnectionLoadCase':
        """TorqueConverterConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4097.TorqueConverterConnectionPowerFlow':
        """TorqueConverterConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
