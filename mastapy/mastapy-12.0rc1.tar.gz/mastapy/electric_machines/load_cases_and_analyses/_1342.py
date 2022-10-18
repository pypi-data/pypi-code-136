"""_1342.py

SpeedTorqueCurveLoadCase
"""


from mastapy._internal import constructor
from mastapy.electric_machines import _1252
from mastapy.electric_machines.load_cases_and_analyses import _1341, _1334
from mastapy._internal.python_net import python_net_import

_SPEED_TORQUE_CURVE_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'SpeedTorqueCurveLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('SpeedTorqueCurveLoadCase',)


class SpeedTorqueCurveLoadCase(_1334.NonLinearDQModelMultipleOperatingPointsLoadCase):
    """SpeedTorqueCurveLoadCase

    This is a mastapy class.
    """

    TYPE = _SPEED_TORQUE_CURVE_LOAD_CASE

    def __init__(self, instance_to_wrap: 'SpeedTorqueCurveLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_speed(self) -> 'float':
        """float: 'MaximumSpeed' is the original name of this property."""

        temp = self.wrapped.MaximumSpeed

        if temp is None:
            return 0.0

        return temp

    @maximum_speed.setter
    def maximum_speed(self, value: 'float'):
        self.wrapped.MaximumSpeed = float(value) if value else 0.0

    @property
    def minimum_speed(self) -> 'float':
        """float: 'MinimumSpeed' is the original name of this property."""

        temp = self.wrapped.MinimumSpeed

        if temp is None:
            return 0.0

        return temp

    @minimum_speed.setter
    def minimum_speed(self, value: 'float'):
        self.wrapped.MinimumSpeed = float(value) if value else 0.0

    @property
    def number_of_speed_values(self) -> 'int':
        """int: 'NumberOfSpeedValues' is the original name of this property."""

        temp = self.wrapped.NumberOfSpeedValues

        if temp is None:
            return 0

        return temp

    @number_of_speed_values.setter
    def number_of_speed_values(self, value: 'int'):
        self.wrapped.NumberOfSpeedValues = int(value) if value else 0

    def analysis_for(self, setup: '_1252.ElectricMachineSetup') -> '_1341.SpeedTorqueCurveAnalysis':
        """ 'AnalysisFor' is the original name of this method.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.SpeedTorqueCurveAnalysis
        """

        method_result = self.wrapped.AnalysisFor(setup.wrapped if setup else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None
