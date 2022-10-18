"""_5757.py

SynchroniserHarmonicAnalysis
"""


from mastapy.system_model.part_model.couplings import _2553
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6894
from mastapy.system_model.analyses_and_results.system_deflections import _2770
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5740
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'SynchroniserHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHarmonicAnalysis',)


class SynchroniserHarmonicAnalysis(_5740.SpecialisedAssemblyHarmonicAnalysis):
    """SynchroniserHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HARMONIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'SynchroniserHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2553.Synchroniser':
        """Synchroniser: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6894.SynchroniserLoadCase':
        """SynchroniserLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2770.SynchroniserSystemDeflection':
        """SynchroniserSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
