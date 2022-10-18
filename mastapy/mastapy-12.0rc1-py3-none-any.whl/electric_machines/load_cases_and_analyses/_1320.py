"""_1320.py

EfficiencyMapLoadCase
"""


from mastapy.electric_machines.load_cases_and_analyses import _1324, _1319, _1334
from mastapy._internal import constructor
from mastapy.electric_machines import _1252
from mastapy._internal.python_net import python_net_import

_EFFICIENCY_MAP_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'EfficiencyMapLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('EfficiencyMapLoadCase',)


class EfficiencyMapLoadCase(_1334.NonLinearDQModelMultipleOperatingPointsLoadCase):
    """EfficiencyMapLoadCase

    This is a mastapy class.
    """

    TYPE = _EFFICIENCY_MAP_LOAD_CASE

    def __init__(self, instance_to_wrap: 'EfficiencyMapLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def efficiency_map_settings(self) -> '_1324.ElectricMachineEfficiencyMapSettings':
        """ElectricMachineEfficiencyMapSettings: 'EfficiencyMapSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EfficiencyMapSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def analysis_for(self, setup: '_1252.ElectricMachineSetup') -> '_1319.EfficiencyMapAnalysis':
        """ 'AnalysisFor' is the original name of this method.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.EfficiencyMapAnalysis
        """

        method_result = self.wrapped.AnalysisFor(setup.wrapped if setup else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None
