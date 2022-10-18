"""_6022.py

PlanetaryGearSetHarmonicAnalysisOfSingleExcitation
"""


from mastapy.system_model.part_model.gears import _2493
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5986
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'PlanetaryGearSetHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryGearSetHarmonicAnalysisOfSingleExcitation',)


class PlanetaryGearSetHarmonicAnalysisOfSingleExcitation(_5986.CylindricalGearSetHarmonicAnalysisOfSingleExcitation):
    """PlanetaryGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    def __init__(self, instance_to_wrap: 'PlanetaryGearSetHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2493.PlanetaryGearSet':
        """PlanetaryGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
