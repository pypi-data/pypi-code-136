"""_1274.py

Rotor
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy.electric_machines import _1247, _1276
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import
from mastapy import _0

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_ROTOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'Rotor')


__docformat__ = 'restructuredtext en'
__all__ = ('Rotor',)


class Rotor(_0.APIBase):
    """Rotor

    This is a mastapy class.
    """

    TYPE = _ROTOR

    def __init__(self, instance_to_wrap: 'Rotor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bore(self) -> 'float':
        """float: 'Bore' is the original name of this property."""

        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return temp

    @bore.setter
    def bore(self, value: 'float'):
        self.wrapped.Bore = float(value) if value else 0.0

    @property
    def d_axis_angle(self) -> 'float':
        """float: 'DAxisAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_and_q_axis_convention(self) -> 'overridable.Overridable_DQAxisConvention':
        """overridable.Overridable_DQAxisConvention: 'DAxisAndQAxisConvention' is the original name of this property."""

        temp = self.wrapped.DAxisAndQAxisConvention

        if temp is None:
            return None

        value = overridable.Overridable_DQAxisConvention.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @d_axis_and_q_axis_convention.setter
    def d_axis_and_q_axis_convention(self, value: 'overridable.Overridable_DQAxisConvention.implicit_type()'):
        wrapper_type = overridable.Overridable_DQAxisConvention.wrapper_type()
        enclosed_type = overridable.Overridable_DQAxisConvention.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.DAxisAndQAxisConvention = value

    @property
    def initial_angle(self) -> 'float':
        """float: 'InitialAngle' is the original name of this property."""

        temp = self.wrapped.InitialAngle

        if temp is None:
            return 0.0

        return temp

    @initial_angle.setter
    def initial_angle(self, value: 'float'):
        self.wrapped.InitialAngle = float(value) if value else 0.0

    @property
    def is_skewed(self) -> 'bool':
        """bool: 'IsSkewed' is the original name of this property."""

        temp = self.wrapped.IsSkewed

        if temp is None:
            return False

        return temp

    @is_skewed.setter
    def is_skewed(self, value: 'bool'):
        self.wrapped.IsSkewed = bool(value) if value else False

    @property
    def kair(self) -> 'float':
        """float: 'Kair' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Kair

        if temp is None:
            return 0.0

        return temp

    @property
    def magnet_flux_barrier_length(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MagnetFluxBarrierLength' is the original name of this property."""

        temp = self.wrapped.MagnetFluxBarrierLength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @magnet_flux_barrier_length.setter
    def magnet_flux_barrier_length(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MagnetFluxBarrierLength = value

    @property
    def number_of_magnet_segments_in_axial_direction(self) -> 'int':
        """int: 'NumberOfMagnetSegmentsInAxialDirection' is the original name of this property."""

        temp = self.wrapped.NumberOfMagnetSegmentsInAxialDirection

        if temp is None:
            return 0

        return temp

    @number_of_magnet_segments_in_axial_direction.setter
    def number_of_magnet_segments_in_axial_direction(self, value: 'int'):
        self.wrapped.NumberOfMagnetSegmentsInAxialDirection = int(value) if value else 0

    @property
    def number_of_poles(self) -> 'int':
        """int: 'NumberOfPoles' is the original name of this property."""

        temp = self.wrapped.NumberOfPoles

        if temp is None:
            return 0

        return temp

    @number_of_poles.setter
    def number_of_poles(self, value: 'int'):
        self.wrapped.NumberOfPoles = int(value) if value else 0

    @property
    def number_of_slices(self) -> 'int':
        """int: 'NumberOfSlices' is the original name of this property."""

        temp = self.wrapped.NumberOfSlices

        if temp is None:
            return 0

        return temp

    @number_of_slices.setter
    def number_of_slices(self, value: 'int'):
        self.wrapped.NumberOfSlices = int(value) if value else 0

    @property
    def outer_diameter(self) -> 'float':
        """float: 'OuterDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_radius(self) -> 'float':
        """float: 'OuterRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def polar_inertia(self) -> 'float':
        """float: 'PolarInertia' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PolarInertia

        if temp is None:
            return 0.0

        return temp

    @property
    def rotor_length(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RotorLength' is the original name of this property."""

        temp = self.wrapped.RotorLength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @rotor_length.setter
    def rotor_length(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RotorLength = value

    @property
    def rotor_material_database(self) -> 'str':
        """str: 'RotorMaterialDatabase' is the original name of this property."""

        temp = self.wrapped.RotorMaterialDatabase.SelectedItemName

        if temp is None:
            return ''

        return temp

    @rotor_material_database.setter
    def rotor_material_database(self, value: 'str'):
        self.wrapped.RotorMaterialDatabase.SetSelectedItem(str(value) if value else '')

    @property
    def use_same_material_as_stator(self) -> 'bool':
        """bool: 'UseSameMaterialAsStator' is the original name of this property."""

        temp = self.wrapped.UseSameMaterialAsStator

        if temp is None:
            return False

        return temp

    @use_same_material_as_stator.setter
    def use_same_material_as_stator(self, value: 'bool'):
        self.wrapped.UseSameMaterialAsStator = bool(value) if value else False

    @property
    def skew_slices(self) -> 'List[_1276.RotorSkewSlice]':
        """List[RotorSkewSlice]: 'SkewSlices' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SkewSlices

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
