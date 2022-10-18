"""_6021.py

PlanetaryConnectionHarmonicAnalysisOfSingleExcitation
"""


from mastapy.system_model.connections_and_sockets import _2239
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6858
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6035
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'PlanetaryConnectionHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryConnectionHarmonicAnalysisOfSingleExcitation',)


class PlanetaryConnectionHarmonicAnalysisOfSingleExcitation(_6035.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation):
    """PlanetaryConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    def __init__(self, instance_to_wrap: 'PlanetaryConnectionHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2239.PlanetaryConnection':
        """PlanetaryConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6858.PlanetaryConnectionLoadCase':
        """PlanetaryConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
