"""_3750.py

CVTBeltConnectionStabilityAnalysis
"""


from mastapy.system_model.connections_and_sockets import _2225
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3718
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'CVTBeltConnectionStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTBeltConnectionStabilityAnalysis',)


class CVTBeltConnectionStabilityAnalysis(_3718.BeltConnectionStabilityAnalysis):
    """CVTBeltConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_STABILITY_ANALYSIS

    def __init__(self, instance_to_wrap: 'CVTBeltConnectionStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2225.CVTBeltConnection':
        """CVTBeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
