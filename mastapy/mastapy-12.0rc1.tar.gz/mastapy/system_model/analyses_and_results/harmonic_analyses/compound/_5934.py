"""_5934.py

ZerolBevelGearCompoundHarmonicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2504
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5770
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5824
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'ZerolBevelGearCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearCompoundHarmonicAnalysis',)


class ZerolBevelGearCompoundHarmonicAnalysis(_5824.BevelGearCompoundHarmonicAnalysis):
    """ZerolBevelGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_COMPOUND_HARMONIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'ZerolBevelGearCompoundHarmonicAnalysis.TYPE'):
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
    def component_analysis_cases_ready(self) -> 'List[_5770.ZerolBevelGearHarmonicAnalysis]':
        """List[ZerolBevelGearHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5770.ZerolBevelGearHarmonicAnalysis]':
        """List[ZerolBevelGearHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
