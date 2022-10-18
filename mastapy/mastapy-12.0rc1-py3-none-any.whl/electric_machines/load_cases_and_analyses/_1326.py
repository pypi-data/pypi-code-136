"""_1326.py

ElectricMachineLoadCase
"""


from mastapy._internal.implicit import enum_with_selected_value
from mastapy.nodal_analysis.elmer import _166
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.electric_machines.load_cases_and_analyses import (
    _1329, _1333, _1325, _1327
)
from mastapy.electric_machines import _1252
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineLoadCase',)


class ElectricMachineLoadCase(_1327.ElectricMachineLoadCaseBase):
    """ElectricMachineLoadCase

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_LOAD_CASE

    def __init__(self, instance_to_wrap: 'ElectricMachineLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_period(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod':
        """enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod: 'AnalysisPeriod' is the original name of this property."""

        temp = self.wrapped.AnalysisPeriod

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @analysis_period.setter
    def analysis_period(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.AnalysisPeriod = value

    @property
    def core_loss_minor_loop_hysteresis_loss_factor(self) -> 'float':
        """float: 'CoreLossMinorLoopHysteresisLossFactor' is the original name of this property."""

        temp = self.wrapped.CoreLossMinorLoopHysteresisLossFactor

        if temp is None:
            return 0.0

        return temp

    @core_loss_minor_loop_hysteresis_loss_factor.setter
    def core_loss_minor_loop_hysteresis_loss_factor(self, value: 'float'):
        self.wrapped.CoreLossMinorLoopHysteresisLossFactor = float(value) if value else 0.0

    @property
    def current_angle(self) -> 'float':
        """float: 'CurrentAngle' is the original name of this property."""

        temp = self.wrapped.CurrentAngle

        if temp is None:
            return 0.0

        return temp

    @current_angle.setter
    def current_angle(self, value: 'float'):
        self.wrapped.CurrentAngle = float(value) if value else 0.0

    @property
    def end_winding_inductance_method(self) -> '_1329.EndWindingInductanceMethod':
        """EndWindingInductanceMethod: 'EndWindingInductanceMethod' is the original name of this property."""

        temp = self.wrapped.EndWindingInductanceMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1329.EndWindingInductanceMethod)(value) if value is not None else None

    @end_winding_inductance_method.setter
    def end_winding_inductance_method(self, value: '_1329.EndWindingInductanceMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.EndWindingInductanceMethod = value

    @property
    def include_iron_and_eddy_current_losses(self) -> 'bool':
        """bool: 'IncludeIronAndEddyCurrentLosses' is the original name of this property."""

        temp = self.wrapped.IncludeIronAndEddyCurrentLosses

        if temp is None:
            return False

        return temp

    @include_iron_and_eddy_current_losses.setter
    def include_iron_and_eddy_current_losses(self, value: 'bool'):
        self.wrapped.IncludeIronAndEddyCurrentLosses = bool(value) if value else False

    @property
    def include_open_circuit_calculation(self) -> 'bool':
        """bool: 'IncludeOpenCircuitCalculation' is the original name of this property."""

        temp = self.wrapped.IncludeOpenCircuitCalculation

        if temp is None:
            return False

        return temp

    @include_open_circuit_calculation.setter
    def include_open_circuit_calculation(self, value: 'bool'):
        self.wrapped.IncludeOpenCircuitCalculation = bool(value) if value else False

    @property
    def minimum_number_of_steps_for_voltages_and_losses_calculation(self) -> 'int':
        """int: 'MinimumNumberOfStepsForVoltagesAndLossesCalculation' is the original name of this property."""

        temp = self.wrapped.MinimumNumberOfStepsForVoltagesAndLossesCalculation

        if temp is None:
            return 0

        return temp

    @minimum_number_of_steps_for_voltages_and_losses_calculation.setter
    def minimum_number_of_steps_for_voltages_and_losses_calculation(self, value: 'int'):
        self.wrapped.MinimumNumberOfStepsForVoltagesAndLossesCalculation = int(value) if value else 0

    @property
    def motoring_or_generating(self) -> '_1333.MotoringOrGenerating':
        """MotoringOrGenerating: 'MotoringOrGenerating' is the original name of this property."""

        temp = self.wrapped.MotoringOrGenerating

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1333.MotoringOrGenerating)(value) if value is not None else None

    @motoring_or_generating.setter
    def motoring_or_generating(self, value: '_1333.MotoringOrGenerating'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.MotoringOrGenerating = value

    @property
    def non_linear_system_convergence_tolerance(self) -> 'float':
        """float: 'NonLinearSystemConvergenceTolerance' is the original name of this property."""

        temp = self.wrapped.NonLinearSystemConvergenceTolerance

        if temp is None:
            return 0.0

        return temp

    @non_linear_system_convergence_tolerance.setter
    def non_linear_system_convergence_tolerance(self, value: 'float'):
        self.wrapped.NonLinearSystemConvergenceTolerance = float(value) if value else 0.0

    @property
    def number_of_cycles(self) -> 'int':
        """int: 'NumberOfCycles' is the original name of this property."""

        temp = self.wrapped.NumberOfCycles

        if temp is None:
            return 0

        return temp

    @number_of_cycles.setter
    def number_of_cycles(self, value: 'int'):
        self.wrapped.NumberOfCycles = int(value) if value else 0

    @property
    def number_of_steps_per_cycle(self) -> 'int':
        """int: 'NumberOfStepsPerCycle' is the original name of this property."""

        temp = self.wrapped.NumberOfStepsPerCycle

        if temp is None:
            return 0

        return temp

    @number_of_steps_per_cycle.setter
    def number_of_steps_per_cycle(self, value: 'int'):
        self.wrapped.NumberOfStepsPerCycle = int(value) if value else 0

    @property
    def override_design_end_winding_inductance_method(self) -> 'bool':
        """bool: 'OverrideDesignEndWindingInductanceMethod' is the original name of this property."""

        temp = self.wrapped.OverrideDesignEndWindingInductanceMethod

        if temp is None:
            return False

        return temp

    @override_design_end_winding_inductance_method.setter
    def override_design_end_winding_inductance_method(self, value: 'bool'):
        self.wrapped.OverrideDesignEndWindingInductanceMethod = bool(value) if value else False

    @property
    def peak_line_current(self) -> 'float':
        """float: 'PeakLineCurrent' is the original name of this property."""

        temp = self.wrapped.PeakLineCurrent

        if temp is None:
            return 0.0

        return temp

    @peak_line_current.setter
    def peak_line_current(self, value: 'float'):
        self.wrapped.PeakLineCurrent = float(value) if value else 0.0

    @property
    def rms_line_current(self) -> 'float':
        """float: 'RMSLineCurrent' is the original name of this property."""

        temp = self.wrapped.RMSLineCurrent

        if temp is None:
            return 0.0

        return temp

    @rms_line_current.setter
    def rms_line_current(self, value: 'float'):
        self.wrapped.RMSLineCurrent = float(value) if value else 0.0

    @property
    def speed(self) -> 'float':
        """float: 'Speed' is the original name of this property."""

        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @speed.setter
    def speed(self, value: 'float'):
        self.wrapped.Speed = float(value) if value else 0.0

    @property
    def total_number_of_time_steps(self) -> 'int':
        """int: 'TotalNumberOfTimeSteps' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalNumberOfTimeSteps

        if temp is None:
            return 0

        return temp

    @property
    def user_specified_end_winding_inductance(self) -> 'float':
        """float: 'UserSpecifiedEndWindingInductance' is the original name of this property."""

        temp = self.wrapped.UserSpecifiedEndWindingInductance

        if temp is None:
            return 0.0

        return temp

    @user_specified_end_winding_inductance.setter
    def user_specified_end_winding_inductance(self, value: 'float'):
        self.wrapped.UserSpecifiedEndWindingInductance = float(value) if value else 0.0

    def analysis_for(self, setup: '_1252.ElectricMachineSetup') -> '_1325.ElectricMachineFEAnalysis':
        """ 'AnalysisFor' is the original name of this method.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.ElectricMachineFEAnalysis
        """

        method_result = self.wrapped.AnalysisFor(setup.wrapped if setup else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None
