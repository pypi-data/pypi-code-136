"""_1319.py

EfficiencyMapAnalysis
"""


from mastapy._internal import constructor
from mastapy.electric_machines.results import _1297
from mastapy.electric_machines.load_cases_and_analyses import _1320, _1321
from mastapy._internal.python_net import python_net_import

_EFFICIENCY_MAP_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'EfficiencyMapAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('EfficiencyMapAnalysis',)


class EfficiencyMapAnalysis(_1321.ElectricMachineAnalysis):
    """EfficiencyMapAnalysis

    This is a mastapy class.
    """

    TYPE = _EFFICIENCY_MAP_ANALYSIS

    def __init__(self, instance_to_wrap: 'EfficiencyMapAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def permanent_magnet_flux_linkage_at_reference_temperature(self) -> 'float':
        """float: 'PermanentMagnetFluxLinkageAtReferenceTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermanentMagnetFluxLinkageAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_resistance(self) -> 'float':
        """float: 'PhaseResistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseResistance

        if temp is None:
            return 0.0

        return temp

    @property
    def efficiency_map_results(self) -> '_1297.EfficiencyResults':
        """EfficiencyResults: 'EfficiencyMapResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EfficiencyMapResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def load_case(self) -> '_1320.EfficiencyMapLoadCase':
        """EfficiencyMapLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
