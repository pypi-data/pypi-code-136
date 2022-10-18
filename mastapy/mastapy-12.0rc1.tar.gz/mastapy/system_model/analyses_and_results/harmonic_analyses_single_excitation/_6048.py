"""_6048.py

StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
"""


from typing import List

from mastapy.system_model.part_model.gears import _2499
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6890
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6046, _6047, _5955
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'StraightBevelGearSetHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetHarmonicAnalysisOfSingleExcitation',)


class StraightBevelGearSetHarmonicAnalysisOfSingleExcitation(_5955.BevelGearSetHarmonicAnalysisOfSingleExcitation):
    """StraightBevelGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2499.StraightBevelGearSet':
        """StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6890.StraightBevelGearSetLoadCase':
        """StraightBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_gears_harmonic_analysis_of_single_excitation(self) -> 'List[_6046.StraightBevelGearHarmonicAnalysisOfSingleExcitation]':
        """List[StraightBevelGearHarmonicAnalysisOfSingleExcitation]: 'StraightBevelGearsHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearsHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes_harmonic_analysis_of_single_excitation(self) -> 'List[_6047.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation]':
        """List[StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation]: 'StraightBevelMeshesHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshesHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
