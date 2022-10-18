"""_1249.py

ElectricMachineDetail
"""


from typing import List

from mastapy.electric_machines import (
    _1244, _1253, _1252, _1274,
    _1237, _1258, _1271, _1284,
    _1233, _1238, _1280
)
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import
from mastapy.electric_machines.results import _1313, _1314
from mastapy._internal.cast_exception import CastException
from mastapy.shafts import _24
from mastapy.math_utility import _1485
from mastapy.utility import _1557
from mastapy import _7483, _0

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_ELECTRIC_MACHINE_DETAIL = python_net_import('SMT.MastaAPI.ElectricMachines', 'ElectricMachineDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineDetail',)


class ElectricMachineDetail(_0.APIBase):
    """ElectricMachineDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_DETAIL

    def __init__(self, instance_to_wrap: 'ElectricMachineDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def core_loss_build_factor_specification_method(self) -> '_1244.CoreLossBuildFactorSpecificationMethod':
        """CoreLossBuildFactorSpecificationMethod: 'CoreLossBuildFactorSpecificationMethod' is the original name of this property."""

        temp = self.wrapped.CoreLossBuildFactorSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1244.CoreLossBuildFactorSpecificationMethod)(value) if value is not None else None

    @core_loss_build_factor_specification_method.setter
    def core_loss_build_factor_specification_method(self, value: '_1244.CoreLossBuildFactorSpecificationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.CoreLossBuildFactorSpecificationMethod = value

    @property
    def dc_bus_voltage(self) -> 'float':
        """float: 'DCBusVoltage' is the original name of this property."""

        temp = self.wrapped.DCBusVoltage

        if temp is None:
            return 0.0

        return temp

    @dc_bus_voltage.setter
    def dc_bus_voltage(self, value: 'float'):
        self.wrapped.DCBusVoltage = float(value) if value else 0.0

    @property
    def eddy_current_core_loss_build_factor(self) -> 'float':
        """float: 'EddyCurrentCoreLossBuildFactor' is the original name of this property."""

        temp = self.wrapped.EddyCurrentCoreLossBuildFactor

        if temp is None:
            return 0.0

        return temp

    @eddy_current_core_loss_build_factor.setter
    def eddy_current_core_loss_build_factor(self, value: 'float'):
        self.wrapped.EddyCurrentCoreLossBuildFactor = float(value) if value else 0.0

    @property
    def effective_machine_length(self) -> 'float':
        """float: 'EffectiveMachineLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EffectiveMachineLength

        if temp is None:
            return 0.0

        return temp

    @property
    def electric_machine_type(self) -> '_1253.ElectricMachineType':
        """ElectricMachineType: 'ElectricMachineType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1253.ElectricMachineType)(value) if value is not None else None

    @property
    def enclosing_volume(self) -> 'float':
        """float: 'EnclosingVolume' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EnclosingVolume

        if temp is None:
            return 0.0

        return temp

    @property
    def excess_core_loss_build_factor(self) -> 'float':
        """float: 'ExcessCoreLossBuildFactor' is the original name of this property."""

        temp = self.wrapped.ExcessCoreLossBuildFactor

        if temp is None:
            return 0.0

        return temp

    @excess_core_loss_build_factor.setter
    def excess_core_loss_build_factor(self, value: 'float'):
        self.wrapped.ExcessCoreLossBuildFactor = float(value) if value else 0.0

    @property
    def has_non_linear_dq_model(self) -> 'bool':
        """bool: 'HasNonLinearDQModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasNonLinearDQModel

        if temp is None:
            return False

        return temp

    @property
    def hysteresis_core_loss_build_factor(self) -> 'float':
        """float: 'HysteresisCoreLossBuildFactor' is the original name of this property."""

        temp = self.wrapped.HysteresisCoreLossBuildFactor

        if temp is None:
            return 0.0

        return temp

    @hysteresis_core_loss_build_factor.setter
    def hysteresis_core_loss_build_factor(self, value: 'float'):
        self.wrapped.HysteresisCoreLossBuildFactor = float(value) if value else 0.0

    @property
    def include_default_results_locations(self) -> 'bool':
        """bool: 'IncludeDefaultResultsLocations' is the original name of this property."""

        temp = self.wrapped.IncludeDefaultResultsLocations

        if temp is None:
            return False

        return temp

    @include_default_results_locations.setter
    def include_default_results_locations(self, value: 'bool'):
        self.wrapped.IncludeDefaultResultsLocations = bool(value) if value else False

    @property
    def include_shaft(self) -> 'bool':
        """bool: 'IncludeShaft' is the original name of this property."""

        temp = self.wrapped.IncludeShaft

        if temp is None:
            return False

        return temp

    @include_shaft.setter
    def include_shaft(self, value: 'bool'):
        self.wrapped.IncludeShaft = bool(value) if value else False

    @property
    def line_line_supply_voltage_rms(self) -> 'float':
        """float: 'LineLineSupplyVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineLineSupplyVoltageRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def magnet_loss_build_factor(self) -> 'float':
        """float: 'MagnetLossBuildFactor' is the original name of this property."""

        temp = self.wrapped.MagnetLossBuildFactor

        if temp is None:
            return 0.0

        return temp

    @magnet_loss_build_factor.setter
    def magnet_loss_build_factor(self, value: 'float'):
        self.wrapped.MagnetLossBuildFactor = float(value) if value else 0.0

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def number_of_phases(self) -> 'int':
        """int: 'NumberOfPhases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfPhases

        if temp is None:
            return 0

        return temp

    @property
    def number_of_slots_per_pole_per_phase(self) -> 'float':
        """float: 'NumberOfSlotsPerPolePerPhase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfSlotsPerPolePerPhase

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_supply_voltage_peak(self) -> 'float':
        """float: 'PhaseSupplyVoltagePeak' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseSupplyVoltagePeak

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_supply_voltage_rms(self) -> 'float':
        """float: 'PhaseSupplyVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseSupplyVoltageRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_air_gap(self) -> 'float':
        """float: 'RadialAirGap' is the original name of this property."""

        temp = self.wrapped.RadialAirGap

        if temp is None:
            return 0.0

        return temp

    @radial_air_gap.setter
    def radial_air_gap(self, value: 'float'):
        self.wrapped.RadialAirGap = float(value) if value else 0.0

    @property
    def rated_inverter_current_peak(self) -> 'float':
        """float: 'RatedInverterCurrentPeak' is the original name of this property."""

        temp = self.wrapped.RatedInverterCurrentPeak

        if temp is None:
            return 0.0

        return temp

    @rated_inverter_current_peak.setter
    def rated_inverter_current_peak(self, value: 'float'):
        self.wrapped.RatedInverterCurrentPeak = float(value) if value else 0.0

    @property
    def rated_inverter_phase_current_peak(self) -> 'float':
        """float: 'RatedInverterPhaseCurrentPeak' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatedInverterPhaseCurrentPeak

        if temp is None:
            return 0.0

        return temp

    @property
    def rotor_core_loss_build_factor(self) -> 'float':
        """float: 'RotorCoreLossBuildFactor' is the original name of this property."""

        temp = self.wrapped.RotorCoreLossBuildFactor

        if temp is None:
            return 0.0

        return temp

    @rotor_core_loss_build_factor.setter
    def rotor_core_loss_build_factor(self, value: 'float'):
        self.wrapped.RotorCoreLossBuildFactor = float(value) if value else 0.0

    @property
    def select_setup(self) -> 'list_with_selected_item.ListWithSelectedItem_ElectricMachineSetup':
        """list_with_selected_item.ListWithSelectedItem_ElectricMachineSetup: 'SelectSetup' is the original name of this property."""

        temp = self.wrapped.SelectSetup

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_ElectricMachineSetup)(temp) if temp is not None else None

    @select_setup.setter
    def select_setup(self, value: 'list_with_selected_item.ListWithSelectedItem_ElectricMachineSetup.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_ElectricMachineSetup.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_ElectricMachineSetup.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.SelectSetup = value

    @property
    def shaft_diameter(self) -> 'float':
        """float: 'ShaftDiameter' is the original name of this property."""

        temp = self.wrapped.ShaftDiameter

        if temp is None:
            return 0.0

        return temp

    @shaft_diameter.setter
    def shaft_diameter(self, value: 'float'):
        self.wrapped.ShaftDiameter = float(value) if value else 0.0

    @property
    def shaft_material_database(self) -> 'str':
        """str: 'ShaftMaterialDatabase' is the original name of this property."""

        temp = self.wrapped.ShaftMaterialDatabase.SelectedItemName

        if temp is None:
            return ''

        return temp

    @shaft_material_database.setter
    def shaft_material_database(self, value: 'str'):
        self.wrapped.ShaftMaterialDatabase.SetSelectedItem(str(value) if value else '')

    @property
    def stator_core_loss_build_factor(self) -> 'float':
        """float: 'StatorCoreLossBuildFactor' is the original name of this property."""

        temp = self.wrapped.StatorCoreLossBuildFactor

        if temp is None:
            return 0.0

        return temp

    @stator_core_loss_build_factor.setter
    def stator_core_loss_build_factor(self, value: 'float'):
        self.wrapped.StatorCoreLossBuildFactor = float(value) if value else 0.0

    @property
    def non_linear_dq_model(self) -> '_1313.NonLinearDQModel':
        """NonLinearDQModel: 'NonLinearDQModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonLinearDQModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def non_linear_dq_model_generator_settings(self) -> '_1314.NonLinearDQModelSettings':
        """NonLinearDQModelSettings: 'NonLinearDQModelGeneratorSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonLinearDQModelGeneratorSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor(self) -> '_1274.Rotor':
        """Rotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rotor

        if temp is None:
            return None

        if _1274.Rotor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rotor to Rotor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor_of_type_cad_rotor(self) -> '_1237.CADRotor':
        """CADRotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rotor

        if temp is None:
            return None

        if _1237.CADRotor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rotor to CADRotor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor_of_type_interior_permanent_magnet_and_synchronous_reluctance_rotor(self) -> '_1258.InteriorPermanentMagnetAndSynchronousReluctanceRotor':
        """InteriorPermanentMagnetAndSynchronousReluctanceRotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rotor

        if temp is None:
            return None

        if _1258.InteriorPermanentMagnetAndSynchronousReluctanceRotor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rotor to InteriorPermanentMagnetAndSynchronousReluctanceRotor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor_of_type_permanent_magnet_rotor(self) -> '_1271.PermanentMagnetRotor':
        """PermanentMagnetRotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rotor

        if temp is None:
            return None

        if _1271.PermanentMagnetRotor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rotor to PermanentMagnetRotor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor_of_type_surface_permanent_magnet_rotor(self) -> '_1284.SurfacePermanentMagnetRotor':
        """SurfacePermanentMagnetRotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rotor

        if temp is None:
            return None

        if _1284.SurfacePermanentMagnetRotor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rotor to SurfacePermanentMagnetRotor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_setup(self) -> '_1252.ElectricMachineSetup':
        """ElectricMachineSetup: 'SelectedSetup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedSetup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_material(self) -> '_24.ShaftMaterial':
        """ShaftMaterial: 'ShaftMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator(self) -> '_1233.AbstractStator':
        """AbstractStator: 'Stator' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Stator

        if temp is None:
            return None

        if _1233.AbstractStator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast stator to AbstractStator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_of_type_cad_stator(self) -> '_1238.CADStator':
        """CADStator: 'Stator' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Stator

        if temp is None:
            return None

        if _1238.CADStator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast stator to CADStator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_of_type_stator(self) -> '_1280.Stator':
        """Stator: 'Stator' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Stator

        if temp is None:
            return None

        if _1280.Stator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast stator to Stator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results_locations(self) -> 'List[_1485.Named2DLocation]':
        """List[Named2DLocation]: 'ResultsLocations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsLocations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def setups(self) -> 'List[_1252.ElectricMachineSetup]':
        """List[ElectricMachineSetup]: 'Setups' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Setups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def generate_cad_geometry_model(self):
        """ 'GenerateCADGeometryModel' is the original name of this method."""

        self.wrapped.GenerateCADGeometryModel()

    def add_results_location(self, name: 'str'):
        """ 'AddResultsLocation' is the original name of this method.

        Args:
            name (str)
        """

        name = str(name)
        self.wrapped.AddResultsLocation(name if name else '')

    def add_setup(self) -> '_1252.ElectricMachineSetup':
        """ 'AddSetup' is the original name of this method.

        Returns:
            mastapy.electric_machines.ElectricMachineSetup
        """

        method_result = self.wrapped.AddSetup()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def duplicate_setup(self, setup: '_1252.ElectricMachineSetup') -> '_1252.ElectricMachineSetup':
        """ 'DuplicateSetup' is the original name of this method.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)

        Returns:
            mastapy.electric_machines.ElectricMachineSetup
        """

        method_result = self.wrapped.DuplicateSetup(setup.wrapped if setup else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def export_to_smt_format(self, file_name: 'str'):
        """ 'ExportToSMTFormat' is the original name of this method.

        Args:
            file_name (str)
        """

        file_name = str(file_name)
        self.wrapped.ExportToSMTFormat(file_name if file_name else '')

    def generate_design_without_non_linear_dq_model(self) -> '_1557.MethodOutcomeWithResult[ElectricMachineDetail]':
        """ 'GenerateDesignWithoutNonLinearDQModel' is the original name of this method.

        Returns:
            mastapy.utility.MethodOutcomeWithResult[mastapy.electric_machines.ElectricMachineDetail]
        """

        method_result = self.wrapped.GenerateDesignWithoutNonLinearDQModel()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def remove_results_location(self, name: 'str'):
        """ 'RemoveResultsLocation' is the original name of this method.

        Args:
            name (str)
        """

        name = str(name)
        self.wrapped.RemoveResultsLocation(name if name else '')

    def remove_setup(self, setup: '_1252.ElectricMachineSetup'):
        """ 'RemoveSetup' is the original name of this method.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)
        """

        self.wrapped.RemoveSetup(setup.wrapped if setup else None)

    def setup_named(self, name: 'str') -> '_1252.ElectricMachineSetup':
        """ 'SetupNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.electric_machines.ElectricMachineSetup
        """

        name = str(name)
        method_result = self.wrapped.SetupNamed(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def try_generate_non_linear_dq_model(self) -> '_1557.MethodOutcomeWithResult[ElectricMachineDetail]':
        """ 'TryGenerateNonLinearDQModel' is the original name of this method.

        Returns:
            mastapy.utility.MethodOutcomeWithResult[mastapy.electric_machines.ElectricMachineDetail]
        """

        method_result = self.wrapped.TryGenerateNonLinearDQModel()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def try_generate_non_linear_dq_model_with_task_progress(self, progress: '_7483.TaskProgress') -> '_1557.MethodOutcomeWithResult[ElectricMachineDetail]':
        """ 'TryGenerateNonLinearDQModelWithTaskProgress' is the original name of this method.

        Args:
            progress (mastapy.TaskProgress)

        Returns:
            mastapy.utility.MethodOutcomeWithResult[mastapy.electric_machines.ElectricMachineDetail]
        """

        method_result = self.wrapped.TryGenerateNonLinearDQModelWithTaskProgress(progress.wrapped if progress else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def write_dxf_to(self, file_name: 'str'):
        """ 'WriteDxfTo' is the original name of this method.

        Args:
            file_name (str)
        """

        file_name = str(file_name)
        self.wrapped.WriteDxfTo(file_name if file_name else '')

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result
