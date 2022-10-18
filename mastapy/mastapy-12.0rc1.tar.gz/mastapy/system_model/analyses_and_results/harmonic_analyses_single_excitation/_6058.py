"""_6058.py

TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
"""


from mastapy.system_model.part_model.couplings import _2561
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6901
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5975
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation',)


class TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation(_5975.CouplingHalfHarmonicAnalysisOfSingleExcitation):
    """TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2561.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6901.TorqueConverterTurbineLoadCase':
        """TorqueConverterTurbineLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
