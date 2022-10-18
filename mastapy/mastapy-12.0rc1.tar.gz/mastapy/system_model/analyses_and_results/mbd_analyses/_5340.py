"""_5340.py

CoaxialConnectionMultibodyDynamicsAnalysis
"""


from mastapy.system_model.connections_and_sockets import _2221
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.cycloidal import _2287
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6762, _6784
from mastapy.system_model.analyses_and_results.mbd_analyses import _5423
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'CoaxialConnectionMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionMultibodyDynamicsAnalysis',)


class CoaxialConnectionMultibodyDynamicsAnalysis(_5423.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis):
    """CoaxialConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS

    def __init__(self, instance_to_wrap: 'CoaxialConnectionMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2221.CoaxialConnection':
        """CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2221.CoaxialConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CoaxialConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6762.CoaxialConnectionLoadCase':
        """CoaxialConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        if _6762.CoaxialConnectionLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_load_case to CoaxialConnectionLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
