"""_6214.py

BeltConnectionDynamicAnalysis
"""


from mastapy.system_model.connections_and_sockets import _2220, _2225
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6747, _6780
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6271
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'BeltConnectionDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltConnectionDynamicAnalysis',)


class BeltConnectionDynamicAnalysis(_6271.InterMountableComponentConnectionDynamicAnalysis):
    """BeltConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_DYNAMIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'BeltConnectionDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2220.BeltConnection':
        """BeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2220.BeltConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to BeltConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6747.BeltConnectionLoadCase':
        """BeltConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        if _6747.BeltConnectionLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_load_case to BeltConnectionLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
