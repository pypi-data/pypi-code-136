"""_1293.py

Windings
"""


from typing import List

from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines import (
    _1246, _1254, _1278, _1290,
    _1295, _1294, _1240, _1272,
    _1279
)
from mastapy.electric_machines.load_cases_and_analyses import _1329
from mastapy.utility_gui.charts import (
    _1827, _1813, _1820, _1822
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import
from mastapy.math_utility import _1476
from mastapy import _0

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_WINDINGS = python_net_import('SMT.MastaAPI.ElectricMachines', 'Windings')


__docformat__ = 'restructuredtext en'
__all__ = ('Windings',)


class Windings(_0.APIBase):
    """Windings

    This is a mastapy class.
    """

    TYPE = _WINDINGS

    def __init__(self, instance_to_wrap: 'Windings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def awg_selector(self) -> 'list_with_selected_item.ListWithSelectedItem_int':
        """list_with_selected_item.ListWithSelectedItem_int: 'AWGSelector' is the original name of this property."""

        temp = self.wrapped.AWGSelector

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_int)(temp) if temp is not None else 0

    @awg_selector.setter
    def awg_selector(self, value: 'list_with_selected_item.ListWithSelectedItem_int.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0)
        self.wrapped.AWGSelector = value

    @property
    def double_layer_winding_slot_positions(self) -> '_1246.DoubleLayerWindingSlotPositions':
        """DoubleLayerWindingSlotPositions: 'DoubleLayerWindingSlotPositions' is the original name of this property."""

        temp = self.wrapped.DoubleLayerWindingSlotPositions

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1246.DoubleLayerWindingSlotPositions)(value) if value is not None else None

    @double_layer_winding_slot_positions.setter
    def double_layer_winding_slot_positions(self, value: '_1246.DoubleLayerWindingSlotPositions'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.DoubleLayerWindingSlotPositions = value

    @property
    def end_winding_inductance_rosa_and_grover(self) -> 'float':
        """float: 'EndWindingInductanceRosaAndGrover' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EndWindingInductanceRosaAndGrover

        if temp is None:
            return 0.0

        return temp

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
    def end_winding_pole_pitch_factor(self) -> 'float':
        """float: 'EndWindingPolePitchFactor' is the original name of this property."""

        temp = self.wrapped.EndWindingPolePitchFactor

        if temp is None:
            return 0.0

        return temp

    @end_winding_pole_pitch_factor.setter
    def end_winding_pole_pitch_factor(self, value: 'float'):
        self.wrapped.EndWindingPolePitchFactor = float(value) if value else 0.0

    @property
    def factor_for_phase_circle_size(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FactorForPhaseCircleSize' is the original name of this property."""

        temp = self.wrapped.FactorForPhaseCircleSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @factor_for_phase_circle_size.setter
    def factor_for_phase_circle_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.FactorForPhaseCircleSize = value

    @property
    def fill_factor_specification_method(self) -> '_1254.FillFactorSpecificationMethod':
        """FillFactorSpecificationMethod: 'FillFactorSpecificationMethod' is the original name of this property."""

        temp = self.wrapped.FillFactorSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1254.FillFactorSpecificationMethod)(value) if value is not None else None

    @fill_factor_specification_method.setter
    def fill_factor_specification_method(self, value: '_1254.FillFactorSpecificationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FillFactorSpecificationMethod = value

    @property
    def iec60228_wire_gauge_selector(self) -> 'list_with_selected_item.ListWithSelectedItem_float':
        """list_with_selected_item.ListWithSelectedItem_float: 'IEC60228WireGaugeSelector' is the original name of this property."""

        temp = self.wrapped.IEC60228WireGaugeSelector

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_float)(temp) if temp is not None else 0.0

    @iec60228_wire_gauge_selector.setter
    def iec60228_wire_gauge_selector(self, value: 'list_with_selected_item.ListWithSelectedItem_float.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_float.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0)
        self.wrapped.IEC60228WireGaugeSelector = value

    @property
    def mmf(self) -> '_1827.TwoDChartDefinition':
        """TwoDChartDefinition: 'MMF' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MMF

        if temp is None:
            return None

        if _1827.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mmf to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mass(self) -> 'float':
        """float: 'Mass' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return temp

    @property
    def material_cost(self) -> 'float':
        """float: 'MaterialCost' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaterialCost

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_length_per_turn(self) -> 'float':
        """float: 'MeanLengthPerTurn' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanLengthPerTurn

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_electrical_orders_for_mmf_chart(self) -> 'int':
        """int: 'NumberOfElectricalOrdersForMMFChart' is the original name of this property."""

        temp = self.wrapped.NumberOfElectricalOrdersForMMFChart

        if temp is None:
            return 0

        return temp

    @number_of_electrical_orders_for_mmf_chart.setter
    def number_of_electrical_orders_for_mmf_chart(self, value: 'int'):
        self.wrapped.NumberOfElectricalOrdersForMMFChart = int(value) if value else 0

    @property
    def number_of_parallel_paths(self) -> 'int':
        """int: 'NumberOfParallelPaths' is the original name of this property."""

        temp = self.wrapped.NumberOfParallelPaths

        if temp is None:
            return 0

        return temp

    @number_of_parallel_paths.setter
    def number_of_parallel_paths(self, value: 'int'):
        self.wrapped.NumberOfParallelPaths = int(value) if value else 0

    @property
    def number_of_strands_per_turn(self) -> 'int':
        """int: 'NumberOfStrandsPerTurn' is the original name of this property."""

        temp = self.wrapped.NumberOfStrandsPerTurn

        if temp is None:
            return 0

        return temp

    @number_of_strands_per_turn.setter
    def number_of_strands_per_turn(self, value: 'int'):
        self.wrapped.NumberOfStrandsPerTurn = int(value) if value else 0

    @property
    def number_of_turns(self) -> 'int':
        """int: 'NumberOfTurns' is the original name of this property."""

        temp = self.wrapped.NumberOfTurns

        if temp is None:
            return 0

        return temp

    @number_of_turns.setter
    def number_of_turns(self, value: 'int'):
        self.wrapped.NumberOfTurns = int(value) if value else 0

    @property
    def number_of_turns_per_phase(self) -> 'int':
        """int: 'NumberOfTurnsPerPhase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfTurnsPerPhase

        if temp is None:
            return 0

        return temp

    @property
    def overall_fill_factor_windings(self) -> 'float':
        """float: 'OverallFillFactorWindings' is the original name of this property."""

        temp = self.wrapped.OverallFillFactorWindings

        if temp is None:
            return 0.0

        return temp

    @overall_fill_factor_windings.setter
    def overall_fill_factor_windings(self, value: 'float'):
        self.wrapped.OverallFillFactorWindings = float(value) if value else 0.0

    @property
    def overall_winding_material_area(self) -> 'float':
        """float: 'OverallWindingMaterialArea' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverallWindingMaterialArea

        if temp is None:
            return 0.0

        return temp

    @property
    def single_double_layer_windings(self) -> '_1278.SingleOrDoubleLayerWindings':
        """SingleOrDoubleLayerWindings: 'SingleDoubleLayerWindings' is the original name of this property."""

        temp = self.wrapped.SingleDoubleLayerWindings

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1278.SingleOrDoubleLayerWindings)(value) if value is not None else None

    @single_double_layer_windings.setter
    def single_double_layer_windings(self, value: '_1278.SingleOrDoubleLayerWindings'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.SingleDoubleLayerWindings = value

    @property
    def throw_for_automated_winding_generation(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'ThrowForAutomatedWindingGeneration' is the original name of this property."""

        temp = self.wrapped.ThrowForAutomatedWindingGeneration

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else 0

    @throw_for_automated_winding_generation.setter
    def throw_for_automated_winding_generation(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.ThrowForAutomatedWindingGeneration = value

    @property
    def total_length_of_conductors_in_phase(self) -> 'float':
        """float: 'TotalLengthOfConductorsInPhase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalLengthOfConductorsInPhase

        if temp is None:
            return 0.0

        return temp

    @property
    def total_slot_area(self) -> 'float':
        """float: 'TotalSlotArea' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalSlotArea

        if temp is None:
            return 0.0

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

    @property
    def winding_connection(self) -> '_1290.WindingConnection':
        """WindingConnection: 'WindingConnection' is the original name of this property."""

        temp = self.wrapped.WindingConnection

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1290.WindingConnection)(value) if value is not None else None

    @winding_connection.setter
    def winding_connection(self, value: '_1290.WindingConnection'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.WindingConnection = value

    @property
    def winding_factor(self) -> 'float':
        """float: 'WindingFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def winding_material_database(self) -> 'str':
        """str: 'WindingMaterialDatabase' is the original name of this property."""

        temp = self.wrapped.WindingMaterialDatabase.SelectedItemName

        if temp is None:
            return ''

        return temp

    @winding_material_database.setter
    def winding_material_database(self, value: 'str'):
        self.wrapped.WindingMaterialDatabase.SetSelectedItem(str(value) if value else '')

    @property
    def winding_material_diameter(self) -> 'float':
        """float: 'WindingMaterialDiameter' is the original name of this property."""

        temp = self.wrapped.WindingMaterialDiameter

        if temp is None:
            return 0.0

        return temp

    @winding_material_diameter.setter
    def winding_material_diameter(self, value: 'float'):
        self.wrapped.WindingMaterialDiameter = float(value) if value else 0.0

    @property
    def wire_size_specification_method(self) -> '_1295.WireSizeSpecificationMethod':
        """WireSizeSpecificationMethod: 'WireSizeSpecificationMethod' is the original name of this property."""

        temp = self.wrapped.WireSizeSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1295.WireSizeSpecificationMethod)(value) if value is not None else None

    @wire_size_specification_method.setter
    def wire_size_specification_method(self, value: '_1295.WireSizeSpecificationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.WireSizeSpecificationMethod = value

    @property
    def mmf_fourier_series_electrical(self) -> '_1476.FourierSeries':
        """FourierSeries: 'MMFFourierSeriesElectrical' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MMFFourierSeriesElectrical

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mmf_fourier_series_mechanical(self) -> '_1476.FourierSeries':
        """FourierSeries: 'MMFFourierSeriesMechanical' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MMFFourierSeriesMechanical

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def windings_viewer(self) -> '_1294.WindingsViewer':
        """WindingsViewer: 'WindingsViewer' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingsViewer

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coils(self) -> 'List[_1240.Coil]':
        """List[Coil]: 'Coils' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Coils

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def phases(self) -> 'List[_1272.Phase]':
        """List[Phase]: 'Phases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Phases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def slot_section_details(self) -> 'List[_1279.SlotSectionDetail]':
        """List[SlotSectionDetail]: 'SlotSectionDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlotSectionDetails

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

    def generate_default_winding_configuration_coils(self):
        """ 'GenerateDefaultWindingConfigurationCoils' is the original name of this method."""

        self.wrapped.GenerateDefaultWindingConfigurationCoils()

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
