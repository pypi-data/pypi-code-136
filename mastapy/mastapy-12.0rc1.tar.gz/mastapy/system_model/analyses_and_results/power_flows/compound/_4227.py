"""_4227.py

TorqueConverterConnectionCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2304
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4097
from mastapy.system_model.analyses_and_results.power_flows.compound import _4147
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'TorqueConverterConnectionCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterConnectionCompoundPowerFlow',)


class TorqueConverterConnectionCompoundPowerFlow(_4147.CouplingConnectionCompoundPowerFlow):
    """TorqueConverterConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_COMPOUND_POWER_FLOW

    def __init__(self, instance_to_wrap: 'TorqueConverterConnectionCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2304.TorqueConverterConnection':
        """TorqueConverterConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def connection_analysis_cases_ready(self) -> 'List[_4097.TorqueConverterConnectionPowerFlow]':
        """List[TorqueConverterConnectionPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4097.TorqueConverterConnectionPowerFlow]':
        """List[TorqueConverterConnectionPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
