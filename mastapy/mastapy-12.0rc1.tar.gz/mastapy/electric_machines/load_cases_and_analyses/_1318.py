"""_1318.py

DynamicForceLoadCase
"""


from typing import List

from mastapy._internal.implicit import enum_with_selected_value
from mastapy.nodal_analysis.elmer import _166
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.electric_machines.load_cases_and_analyses import (
    _1335, _1336, _1340, _1344,
    _1317, _1334
)
from mastapy.electric_machines import _1252
from mastapy._internal.python_net import python_net_import

_DOUBLE = python_net_import('System', 'Double')
_DYNAMIC_FORCE_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'DynamicForceLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicForceLoadCase',)


class DynamicForceLoadCase(_1334.NonLinearDQModelMultipleOperatingPointsLoadCase):
    """DynamicForceLoadCase

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_FORCE_LOAD_CASE

    def __init__(self, instance_to_wrap: 'DynamicForceLoadCase.TYPE'):
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
    def number_of_operating_points(self) -> 'int':
        """int: 'NumberOfOperatingPoints' is the original name of this property."""

        temp = self.wrapped.NumberOfOperatingPoints

        if temp is None:
            return 0

        return temp

    @number_of_operating_points.setter
    def number_of_operating_points(self, value: 'int'):
        self.wrapped.NumberOfOperatingPoints = int(value) if value else 0

    @property
    def number_of_steps_per_operating_point_specification_method(self) -> '_1335.NumberOfStepsPerOperatingPointSpecificationMethod':
        """NumberOfStepsPerOperatingPointSpecificationMethod: 'NumberOfStepsPerOperatingPointSpecificationMethod' is the original name of this property."""

        temp = self.wrapped.NumberOfStepsPerOperatingPointSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1335.NumberOfStepsPerOperatingPointSpecificationMethod)(value) if value is not None else None

    @number_of_steps_per_operating_point_specification_method.setter
    def number_of_steps_per_operating_point_specification_method(self, value: '_1335.NumberOfStepsPerOperatingPointSpecificationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.NumberOfStepsPerOperatingPointSpecificationMethod = value

    @property
    def number_of_steps_for_the_analysis_period(self) -> 'int':
        """int: 'NumberOfStepsForTheAnalysisPeriod' is the original name of this property."""

        temp = self.wrapped.NumberOfStepsForTheAnalysisPeriod

        if temp is None:
            return 0

        return temp

    @number_of_steps_for_the_analysis_period.setter
    def number_of_steps_for_the_analysis_period(self, value: 'int'):
        self.wrapped.NumberOfStepsForTheAnalysisPeriod = int(value) if value else 0

    @property
    def operating_points_specification_method(self) -> '_1336.OperatingPointsSpecificationMethod':
        """OperatingPointsSpecificationMethod: 'OperatingPointsSpecificationMethod' is the original name of this property."""

        temp = self.wrapped.OperatingPointsSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1336.OperatingPointsSpecificationMethod)(value) if value is not None else None

    @operating_points_specification_method.setter
    def operating_points_specification_method(self, value: '_1336.OperatingPointsSpecificationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.OperatingPointsSpecificationMethod = value

    @property
    def speed_points_distribution(self) -> '_1340.SpeedPointsDistribution':
        """SpeedPointsDistribution: 'SpeedPointsDistribution' is the original name of this property."""

        temp = self.wrapped.SpeedPointsDistribution

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1340.SpeedPointsDistribution)(value) if value is not None else None

    @speed_points_distribution.setter
    def speed_points_distribution(self, value: '_1340.SpeedPointsDistribution'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.SpeedPointsDistribution = value

    @property
    def operating_points(self) -> 'List[_1344.SpeedTorqueOperatingPoint]':
        """List[SpeedTorqueOperatingPoint]: 'OperatingPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OperatingPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def add_operating_point(self):
        """ 'AddOperatingPoint' is the original name of this method."""

        self.wrapped.AddOperatingPoint()

    def add_operating_point_with_torque_and_speed(self, torque: 'float', speed: 'float') -> '_1344.SpeedTorqueOperatingPoint':
        """ 'AddOperatingPoint' is the original name of this method.

        Args:
            torque (float)
            speed (float)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.SpeedTorqueOperatingPoint
        """

        torque = float(torque)
        speed = float(speed)
        method_result = self.wrapped.AddOperatingPoint.Overloads[_DOUBLE, _DOUBLE](torque if torque else 0.0, speed if speed else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def analysis_for(self, setup: '_1252.ElectricMachineSetup') -> '_1317.DynamicForceAnalysis':
        """ 'AnalysisFor' is the original name of this method.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.DynamicForceAnalysis
        """

        method_result = self.wrapped.AnalysisFor(setup.wrapped if setup else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def remove_operating_point(self, operating_point: '_1344.SpeedTorqueOperatingPoint'):
        """ 'RemoveOperatingPoint' is the original name of this method.

        Args:
            operating_point (mastapy.electric_machines.load_cases_and_analyses.SpeedTorqueOperatingPoint)
        """

        self.wrapped.RemoveOperatingPoint(operating_point.wrapped if operating_point else None)

    def set_speeds(self, values: 'List[float]'):
        """ 'SetSpeeds' is the original name of this method.

        Args:
            values (List[float])
        """

        values = conversion.mp_to_pn_list_float(values)
        self.wrapped.SetSpeeds(values)

    def set_speeds_in_si_units(self, values: 'List[float]'):
        """ 'SetSpeedsInSIUnits' is the original name of this method.

        Args:
            values (List[float])
        """

        values = conversion.mp_to_pn_list_float(values)
        self.wrapped.SetSpeedsInSIUnits(values)
