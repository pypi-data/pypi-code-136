"""_5949.py

BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation
"""


from mastapy.system_model.connections_and_sockets.gears import _2253
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6750
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5954
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation',)


class BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation(_5954.BevelGearMeshHarmonicAnalysisOfSingleExcitation):
    """BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2253.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6750.BevelDifferentialGearMeshLoadCase':
        """BevelDifferentialGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
