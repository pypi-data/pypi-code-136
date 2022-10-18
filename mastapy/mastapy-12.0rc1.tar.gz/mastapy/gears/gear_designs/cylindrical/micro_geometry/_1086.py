"""_1086.py

CylindricalGearCommonFlankMicroGeometry
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.cylindrical import _1018
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_COMMON_FLANK_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearCommonFlankMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearCommonFlankMicroGeometry',)


class CylindricalGearCommonFlankMicroGeometry(_0.APIBase):
    """CylindricalGearCommonFlankMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_COMMON_FLANK_MICRO_GEOMETRY

    def __init__(self, instance_to_wrap: 'CylindricalGearCommonFlankMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def profile_factor_for_0_bias_relief(self) -> 'float':
        """float: 'ProfileFactorFor0BiasRelief' is the original name of this property."""

        temp = self.wrapped.ProfileFactorFor0BiasRelief

        if temp is None:
            return 0.0

        return temp

    @profile_factor_for_0_bias_relief.setter
    def profile_factor_for_0_bias_relief(self, value: 'float'):
        self.wrapped.ProfileFactorFor0BiasRelief = float(value) if value else 0.0

    @property
    def read_micro_geometry_from_an_external_file_using_file_name(self) -> 'str':
        """str: 'ReadMicroGeometryFromAnExternalFileUsingFileName' is the original name of this property."""

        temp = self.wrapped.ReadMicroGeometryFromAnExternalFileUsingFileName

        if temp is None:
            return ''

        return temp

    @read_micro_geometry_from_an_external_file_using_file_name.setter
    def read_micro_geometry_from_an_external_file_using_file_name(self, value: 'str'):
        self.wrapped.ReadMicroGeometryFromAnExternalFileUsingFileName = str(value) if value else ''

    @property
    def use_measured_map_data(self) -> 'bool':
        """bool: 'UseMeasuredMapData' is the original name of this property."""

        temp = self.wrapped.UseMeasuredMapData

        if temp is None:
            return False

        return temp

    @use_measured_map_data.setter
    def use_measured_map_data(self, value: 'bool'):
        self.wrapped.UseMeasuredMapData = bool(value) if value else False

    @property
    def zero_bias_relief(self) -> '_1018.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'ZeroBiasRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZeroBiasRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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

    def read_micro_geometry_from_an_external_file(self):
        """ 'ReadMicroGeometryFromAnExternalFile' is the original name of this method."""

        self.wrapped.ReadMicroGeometryFromAnExternalFile()

    def switch_measured_data_direction_with_respect_to_face_width(self):
        """ 'SwitchMeasuredDataDirectionWithRespectToFaceWidth' is the original name of this method."""

        self.wrapped.SwitchMeasuredDataDirectionWithRespectToFaceWidth()

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
