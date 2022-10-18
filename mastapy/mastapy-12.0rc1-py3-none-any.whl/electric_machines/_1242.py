"""_1242.py

CoolingDuctLayerSpecification
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines import _1243
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_COOLING_DUCT_LAYER_SPECIFICATION = python_net_import('SMT.MastaAPI.ElectricMachines', 'CoolingDuctLayerSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('CoolingDuctLayerSpecification',)


class CoolingDuctLayerSpecification(_0.APIBase):
    """CoolingDuctLayerSpecification

    This is a mastapy class.
    """

    TYPE = _COOLING_DUCT_LAYER_SPECIFICATION

    def __init__(self, instance_to_wrap: 'CoolingDuctLayerSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def distance_to_lower_arc(self) -> 'float':
        """float: 'DistanceToLowerArc' is the original name of this property."""

        temp = self.wrapped.DistanceToLowerArc

        if temp is None:
            return 0.0

        return temp

    @distance_to_lower_arc.setter
    def distance_to_lower_arc(self, value: 'float'):
        self.wrapped.DistanceToLowerArc = float(value) if value else 0.0

    @property
    def duct_diameter(self) -> 'float':
        """float: 'DuctDiameter' is the original name of this property."""

        temp = self.wrapped.DuctDiameter

        if temp is None:
            return 0.0

        return temp

    @duct_diameter.setter
    def duct_diameter(self, value: 'float'):
        self.wrapped.DuctDiameter = float(value) if value else 0.0

    @property
    def first_duct_angle(self) -> 'float':
        """float: 'FirstDuctAngle' is the original name of this property."""

        temp = self.wrapped.FirstDuctAngle

        if temp is None:
            return 0.0

        return temp

    @first_duct_angle.setter
    def first_duct_angle(self, value: 'float'):
        self.wrapped.FirstDuctAngle = float(value) if value else 0.0

    @property
    def length_in_radial_direction(self) -> 'float':
        """float: 'LengthInRadialDirection' is the original name of this property."""

        temp = self.wrapped.LengthInRadialDirection

        if temp is None:
            return 0.0

        return temp

    @length_in_radial_direction.setter
    def length_in_radial_direction(self, value: 'float'):
        self.wrapped.LengthInRadialDirection = float(value) if value else 0.0

    @property
    def lower_arc_length(self) -> 'float':
        """float: 'LowerArcLength' is the original name of this property."""

        temp = self.wrapped.LowerArcLength

        if temp is None:
            return 0.0

        return temp

    @lower_arc_length.setter
    def lower_arc_length(self, value: 'float'):
        self.wrapped.LowerArcLength = float(value) if value else 0.0

    @property
    def major_axis_length(self) -> 'float':
        """float: 'MajorAxisLength' is the original name of this property."""

        temp = self.wrapped.MajorAxisLength

        if temp is None:
            return 0.0

        return temp

    @major_axis_length.setter
    def major_axis_length(self, value: 'float'):
        self.wrapped.MajorAxisLength = float(value) if value else 0.0

    @property
    def minor_axis_length(self) -> 'float':
        """float: 'MinorAxisLength' is the original name of this property."""

        temp = self.wrapped.MinorAxisLength

        if temp is None:
            return 0.0

        return temp

    @minor_axis_length.setter
    def minor_axis_length(self, value: 'float'):
        self.wrapped.MinorAxisLength = float(value) if value else 0.0

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def number_of_ducts(self) -> 'int':
        """int: 'NumberOfDucts' is the original name of this property."""

        temp = self.wrapped.NumberOfDucts

        if temp is None:
            return 0

        return temp

    @number_of_ducts.setter
    def number_of_ducts(self, value: 'int'):
        self.wrapped.NumberOfDucts = int(value) if value else 0

    @property
    def radial_offset(self) -> 'float':
        """float: 'RadialOffset' is the original name of this property."""

        temp = self.wrapped.RadialOffset

        if temp is None:
            return 0.0

        return temp

    @radial_offset.setter
    def radial_offset(self, value: 'float'):
        self.wrapped.RadialOffset = float(value) if value else 0.0

    @property
    def rotation(self) -> 'float':
        """float: 'Rotation' is the original name of this property."""

        temp = self.wrapped.Rotation

        if temp is None:
            return 0.0

        return temp

    @rotation.setter
    def rotation(self, value: 'float'):
        self.wrapped.Rotation = float(value) if value else 0.0

    @property
    def shape(self) -> '_1243.CoolingDuctShape':
        """CoolingDuctShape: 'Shape' is the original name of this property."""

        temp = self.wrapped.Shape

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1243.CoolingDuctShape)(value) if value is not None else None

    @shape.setter
    def shape(self, value: '_1243.CoolingDuctShape'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Shape = value

    @property
    def upper_arc_length(self) -> 'float':
        """float: 'UpperArcLength' is the original name of this property."""

        temp = self.wrapped.UpperArcLength

        if temp is None:
            return 0.0

        return temp

    @upper_arc_length.setter
    def upper_arc_length(self, value: 'float'):
        self.wrapped.UpperArcLength = float(value) if value else 0.0

    @property
    def upper_fillet_radius(self) -> 'float':
        """float: 'UpperFilletRadius' is the original name of this property."""

        temp = self.wrapped.UpperFilletRadius

        if temp is None:
            return 0.0

        return temp

    @upper_fillet_radius.setter
    def upper_fillet_radius(self, value: 'float'):
        self.wrapped.UpperFilletRadius = float(value) if value else 0.0

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
