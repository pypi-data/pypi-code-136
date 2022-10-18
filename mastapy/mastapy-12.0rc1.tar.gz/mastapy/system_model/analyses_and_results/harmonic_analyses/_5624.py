"""_5624.py

BeltConnectionHarmonicAnalysis
"""


from mastapy.system_model.connections_and_sockets import _2220, _2225
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6747, _6780
from mastapy.system_model.analyses_and_results.system_deflections import _2645, _2678
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5704
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'BeltConnectionHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltConnectionHarmonicAnalysis',)


class BeltConnectionHarmonicAnalysis(_5704.InterMountableComponentConnectionHarmonicAnalysis):
    """BeltConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_HARMONIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'BeltConnectionHarmonicAnalysis.TYPE'):
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

    @property
    def system_deflection_results(self) -> '_2645.BeltConnectionSystemDeflection':
        """BeltConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2645.BeltConnectionSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BeltConnectionSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
