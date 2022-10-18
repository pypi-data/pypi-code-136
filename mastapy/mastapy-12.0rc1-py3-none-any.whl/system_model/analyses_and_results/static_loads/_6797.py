"""_6797.py

ElectricMachineHarmonicLoadData
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.electric_machines.harmonic_load_data import _1350, _1346
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.analyses_and_results.static_loads import _6902
from mastapy.math_utility import _1476
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ElectricMachineHarmonicLoadData')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadData',)


class ElectricMachineHarmonicLoadData(_1346.ElectricMachineHarmonicLoadDataBase):
    """ElectricMachineHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadData.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def apply_to_all_data_types(self) -> 'bool':
        """bool: 'ApplyToAllDataTypes' is the original name of this property."""

        temp = self.wrapped.ApplyToAllDataTypes

        if temp is None:
            return False

        return temp

    @apply_to_all_data_types.setter
    def apply_to_all_data_types(self, value: 'bool'):
        self.wrapped.ApplyToAllDataTypes = bool(value) if value else False

    @property
    def apply_to_all_speeds_for_selected_data_type(self) -> 'bool':
        """bool: 'ApplyToAllSpeedsForSelectedDataType' is the original name of this property."""

        temp = self.wrapped.ApplyToAllSpeedsForSelectedDataType

        if temp is None:
            return False

        return temp

    @apply_to_all_speeds_for_selected_data_type.setter
    def apply_to_all_speeds_for_selected_data_type(self, value: 'bool'):
        self.wrapped.ApplyToAllSpeedsForSelectedDataType = bool(value) if value else False

    @property
    def constant_torque(self) -> 'float':
        """float: 'ConstantTorque' is the original name of this property."""

        temp = self.wrapped.ConstantTorque

        if temp is None:
            return 0.0

        return temp

    @constant_torque.setter
    def constant_torque(self, value: 'float'):
        self.wrapped.ConstantTorque = float(value) if value else 0.0

    @property
    def data_type_for_scaling(self) -> 'enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType':
        """enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType: 'DataTypeForScaling' is the original name of this property."""

        temp = self.wrapped.DataTypeForScaling

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @data_type_for_scaling.setter
    def data_type_for_scaling(self, value: 'enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DataTypeForScaling = value

    @property
    def rotor_moment_from_stator_teeth_axial_loads_amplitude_cut_off(self) -> 'float':
        """float: 'RotorMomentFromStatorTeethAxialLoadsAmplitudeCutOff' is the original name of this property."""

        temp = self.wrapped.RotorMomentFromStatorTeethAxialLoadsAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @rotor_moment_from_stator_teeth_axial_loads_amplitude_cut_off.setter
    def rotor_moment_from_stator_teeth_axial_loads_amplitude_cut_off(self, value: 'float'):
        self.wrapped.RotorMomentFromStatorTeethAxialLoadsAmplitudeCutOff = float(value) if value else 0.0

    @property
    def rotor_x_force_amplitude_cut_off(self) -> 'float':
        """float: 'RotorXForceAmplitudeCutOff' is the original name of this property."""

        temp = self.wrapped.RotorXForceAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @rotor_x_force_amplitude_cut_off.setter
    def rotor_x_force_amplitude_cut_off(self, value: 'float'):
        self.wrapped.RotorXForceAmplitudeCutOff = float(value) if value else 0.0

    @property
    def rotor_y_force_amplitude_cut_off(self) -> 'float':
        """float: 'RotorYForceAmplitudeCutOff' is the original name of this property."""

        temp = self.wrapped.RotorYForceAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @rotor_y_force_amplitude_cut_off.setter
    def rotor_y_force_amplitude_cut_off(self, value: 'float'):
        self.wrapped.RotorYForceAmplitudeCutOff = float(value) if value else 0.0

    @property
    def rotor_z_force_amplitude_cut_off(self) -> 'float':
        """float: 'RotorZForceAmplitudeCutOff' is the original name of this property."""

        temp = self.wrapped.RotorZForceAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @rotor_z_force_amplitude_cut_off.setter
    def rotor_z_force_amplitude_cut_off(self, value: 'float'):
        self.wrapped.RotorZForceAmplitudeCutOff = float(value) if value else 0.0

    @property
    def scale(self) -> 'float':
        """float: 'Scale' is the original name of this property."""

        temp = self.wrapped.Scale

        if temp is None:
            return 0.0

        return temp

    @scale.setter
    def scale(self, value: 'float'):
        self.wrapped.Scale = float(value) if value else 0.0

    @property
    def torque_ripple_amplitude_cut_off(self) -> 'float':
        """float: 'TorqueRippleAmplitudeCutOff' is the original name of this property."""

        temp = self.wrapped.TorqueRippleAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @torque_ripple_amplitude_cut_off.setter
    def torque_ripple_amplitude_cut_off(self, value: 'float'):
        self.wrapped.TorqueRippleAmplitudeCutOff = float(value) if value else 0.0

    @property
    def torque_ripple_input_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_TorqueRippleInputType':
        """enum_with_selected_value.EnumWithSelectedValue_TorqueRippleInputType: 'TorqueRippleInputType' is the original name of this property."""

        temp = self.wrapped.TorqueRippleInputType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_TorqueRippleInputType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @torque_ripple_input_type.setter
    def torque_ripple_input_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_TorqueRippleInputType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_TorqueRippleInputType.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.TorqueRippleInputType = value

    @property
    def use_stator_radius_from_masta_model(self) -> 'bool':
        """bool: 'UseStatorRadiusFromMASTAModel' is the original name of this property."""

        temp = self.wrapped.UseStatorRadiusFromMASTAModel

        if temp is None:
            return False

        return temp

    @use_stator_radius_from_masta_model.setter
    def use_stator_radius_from_masta_model(self, value: 'bool'):
        self.wrapped.UseStatorRadiusFromMASTAModel = bool(value) if value else False

    @property
    def excitations(self) -> 'List[_1476.FourierSeries]':
        """List[FourierSeries]: 'Excitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
