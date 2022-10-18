"""_6064.py

ZerolBevelGearHarmonicAnalysisOfSingleExcitation
"""


from mastapy.system_model.part_model.gears import _2504
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6911
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5953
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'ZerolBevelGearHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearHarmonicAnalysisOfSingleExcitation',)


class ZerolBevelGearHarmonicAnalysisOfSingleExcitation(_5953.BevelGearHarmonicAnalysisOfSingleExcitation):
    """ZerolBevelGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    def __init__(self, instance_to_wrap: 'ZerolBevelGearHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2504.ZerolBevelGear':
        """ZerolBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6911.ZerolBevelGearLoadCase':
        """ZerolBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
