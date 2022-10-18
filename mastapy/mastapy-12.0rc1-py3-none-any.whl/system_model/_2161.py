"""_2161.py

DesignSettings
"""


from typing import List

from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis import _50
from mastapy.bearings import _1842
from mastapy.gears.gear_designs import _934, _936, _939
from mastapy.gears.gear_designs.cylindrical import _1007, _1015
from mastapy.gears.rating.cylindrical import _448
from mastapy.materials import _267
from mastapy.shafts import _40
from mastapy import _0

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_DESIGN_SETTINGS = python_net_import('SMT.MastaAPI.SystemModel', 'DesignSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('DesignSettings',)


class DesignSettings(_0.APIBase):
    """DesignSettings

    This is a mastapy class.
    """

    TYPE = _DESIGN_SETTINGS

    def __init__(self, instance_to_wrap: 'DesignSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_settings_database_item(self) -> 'str':
        """str: 'AnalysisSettingsDatabaseItem' is the original name of this property."""

        temp = self.wrapped.AnalysisSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ''

        return temp

    @analysis_settings_database_item.setter
    def analysis_settings_database_item(self, value: 'str'):
        self.wrapped.AnalysisSettingsDatabaseItem.SetSelectedItem(str(value) if value else '')

    @property
    def analysis_settings_for_new_designs(self) -> 'str':
        """str: 'AnalysisSettingsForNewDesigns' is the original name of this property."""

        temp = self.wrapped.AnalysisSettingsForNewDesigns.SelectedItemName

        if temp is None:
            return ''

        return temp

    @analysis_settings_for_new_designs.setter
    def analysis_settings_for_new_designs(self, value: 'str'):
        self.wrapped.AnalysisSettingsForNewDesigns.SetSelectedItem(str(value) if value else '')

    @property
    def bearing_settings_database_item(self) -> 'str':
        """str: 'BearingSettingsDatabaseItem' is the original name of this property."""

        temp = self.wrapped.BearingSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ''

        return temp

    @bearing_settings_database_item.setter
    def bearing_settings_database_item(self, value: 'str'):
        self.wrapped.BearingSettingsDatabaseItem.SetSelectedItem(str(value) if value else '')

    @property
    def bearing_settings_for_new_designs(self) -> 'str':
        """str: 'BearingSettingsForNewDesigns' is the original name of this property."""

        temp = self.wrapped.BearingSettingsForNewDesigns.SelectedItemName

        if temp is None:
            return ''

        return temp

    @bearing_settings_for_new_designs.setter
    def bearing_settings_for_new_designs(self, value: 'str'):
        self.wrapped.BearingSettingsForNewDesigns.SetSelectedItem(str(value) if value else '')

    @property
    def bevel_hypoid_gear_design_settings_database_item(self) -> 'str':
        """str: 'BevelHypoidGearDesignSettingsDatabaseItem' is the original name of this property."""

        temp = self.wrapped.BevelHypoidGearDesignSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ''

        return temp

    @bevel_hypoid_gear_design_settings_database_item.setter
    def bevel_hypoid_gear_design_settings_database_item(self, value: 'str'):
        self.wrapped.BevelHypoidGearDesignSettingsDatabaseItem.SetSelectedItem(str(value) if value else '')

    @property
    def bevel_hypoid_gear_design_settings_for_new_designs_database_item(self) -> 'str':
        """str: 'BevelHypoidGearDesignSettingsForNewDesignsDatabaseItem' is the original name of this property."""

        temp = self.wrapped.BevelHypoidGearDesignSettingsForNewDesignsDatabaseItem.SelectedItemName

        if temp is None:
            return ''

        return temp

    @bevel_hypoid_gear_design_settings_for_new_designs_database_item.setter
    def bevel_hypoid_gear_design_settings_for_new_designs_database_item(self, value: 'str'):
        self.wrapped.BevelHypoidGearDesignSettingsForNewDesignsDatabaseItem.SetSelectedItem(str(value) if value else '')

    @property
    def bevel_hypoid_gear_rating_settings_database_item(self) -> 'str':
        """str: 'BevelHypoidGearRatingSettingsDatabaseItem' is the original name of this property."""

        temp = self.wrapped.BevelHypoidGearRatingSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ''

        return temp

    @bevel_hypoid_gear_rating_settings_database_item.setter
    def bevel_hypoid_gear_rating_settings_database_item(self, value: 'str'):
        self.wrapped.BevelHypoidGearRatingSettingsDatabaseItem.SetSelectedItem(str(value) if value else '')

    @property
    def bevel_hypoid_gear_rating_settings_for_new_designs_database_item(self) -> 'str':
        """str: 'BevelHypoidGearRatingSettingsForNewDesignsDatabaseItem' is the original name of this property."""

        temp = self.wrapped.BevelHypoidGearRatingSettingsForNewDesignsDatabaseItem.SelectedItemName

        if temp is None:
            return ''

        return temp

    @bevel_hypoid_gear_rating_settings_for_new_designs_database_item.setter
    def bevel_hypoid_gear_rating_settings_for_new_designs_database_item(self, value: 'str'):
        self.wrapped.BevelHypoidGearRatingSettingsForNewDesignsDatabaseItem.SetSelectedItem(str(value) if value else '')

    @property
    def cylindrical_gear_design_constraints_settings_database_item(self) -> 'str':
        """str: 'CylindricalGearDesignConstraintsSettingsDatabaseItem' is the original name of this property."""

        temp = self.wrapped.CylindricalGearDesignConstraintsSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ''

        return temp

    @cylindrical_gear_design_constraints_settings_database_item.setter
    def cylindrical_gear_design_constraints_settings_database_item(self, value: 'str'):
        self.wrapped.CylindricalGearDesignConstraintsSettingsDatabaseItem.SetSelectedItem(str(value) if value else '')

    @property
    def cylindrical_gear_design_constraints_settings_for_new_designs(self) -> 'str':
        """str: 'CylindricalGearDesignConstraintsSettingsForNewDesigns' is the original name of this property."""

        temp = self.wrapped.CylindricalGearDesignConstraintsSettingsForNewDesigns.SelectedItemName

        if temp is None:
            return ''

        return temp

    @cylindrical_gear_design_constraints_settings_for_new_designs.setter
    def cylindrical_gear_design_constraints_settings_for_new_designs(self, value: 'str'):
        self.wrapped.CylindricalGearDesignConstraintsSettingsForNewDesigns.SetSelectedItem(str(value) if value else '')

    @property
    def cylindrical_gear_design_and_rating_settings_database_item(self) -> 'str':
        """str: 'CylindricalGearDesignAndRatingSettingsDatabaseItem' is the original name of this property."""

        temp = self.wrapped.CylindricalGearDesignAndRatingSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ''

        return temp

    @cylindrical_gear_design_and_rating_settings_database_item.setter
    def cylindrical_gear_design_and_rating_settings_database_item(self, value: 'str'):
        self.wrapped.CylindricalGearDesignAndRatingSettingsDatabaseItem.SetSelectedItem(str(value) if value else '')

    @property
    def cylindrical_gear_design_and_rating_settings_for_new_designs(self) -> 'str':
        """str: 'CylindricalGearDesignAndRatingSettingsForNewDesigns' is the original name of this property."""

        temp = self.wrapped.CylindricalGearDesignAndRatingSettingsForNewDesigns.SelectedItemName

        if temp is None:
            return ''

        return temp

    @cylindrical_gear_design_and_rating_settings_for_new_designs.setter
    def cylindrical_gear_design_and_rating_settings_for_new_designs(self, value: 'str'):
        self.wrapped.CylindricalGearDesignAndRatingSettingsForNewDesigns.SetSelectedItem(str(value) if value else '')

    @property
    def cylindrical_gear_micro_geometry_settings_database_item(self) -> 'str':
        """str: 'CylindricalGearMicroGeometrySettingsDatabaseItem' is the original name of this property."""

        temp = self.wrapped.CylindricalGearMicroGeometrySettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ''

        return temp

    @cylindrical_gear_micro_geometry_settings_database_item.setter
    def cylindrical_gear_micro_geometry_settings_database_item(self, value: 'str'):
        self.wrapped.CylindricalGearMicroGeometrySettingsDatabaseItem.SetSelectedItem(str(value) if value else '')

    @property
    def cylindrical_gear_micro_geometry_settings_for_new_designs(self) -> 'str':
        """str: 'CylindricalGearMicroGeometrySettingsForNewDesigns' is the original name of this property."""

        temp = self.wrapped.CylindricalGearMicroGeometrySettingsForNewDesigns.SelectedItemName

        if temp is None:
            return ''

        return temp

    @cylindrical_gear_micro_geometry_settings_for_new_designs.setter
    def cylindrical_gear_micro_geometry_settings_for_new_designs(self, value: 'str'):
        self.wrapped.CylindricalGearMicroGeometrySettingsForNewDesigns.SetSelectedItem(str(value) if value else '')

    @property
    def design_constraints_settings_database_item(self) -> 'str':
        """str: 'DesignConstraintsSettingsDatabaseItem' is the original name of this property."""

        temp = self.wrapped.DesignConstraintsSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ''

        return temp

    @design_constraints_settings_database_item.setter
    def design_constraints_settings_database_item(self, value: 'str'):
        self.wrapped.DesignConstraintsSettingsDatabaseItem.SetSelectedItem(str(value) if value else '')

    @property
    def design_constraints_settings_for_new_designs(self) -> 'str':
        """str: 'DesignConstraintsSettingsForNewDesigns' is the original name of this property."""

        temp = self.wrapped.DesignConstraintsSettingsForNewDesigns.SelectedItemName

        if temp is None:
            return ''

        return temp

    @design_constraints_settings_for_new_designs.setter
    def design_constraints_settings_for_new_designs(self, value: 'str'):
        self.wrapped.DesignConstraintsSettingsForNewDesigns.SetSelectedItem(str(value) if value else '')

    @property
    def materials_settings_database_item(self) -> 'str':
        """str: 'MaterialsSettingsDatabaseItem' is the original name of this property."""

        temp = self.wrapped.MaterialsSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ''

        return temp

    @materials_settings_database_item.setter
    def materials_settings_database_item(self, value: 'str'):
        self.wrapped.MaterialsSettingsDatabaseItem.SetSelectedItem(str(value) if value else '')

    @property
    def materials_settings_for_new_designs(self) -> 'str':
        """str: 'MaterialsSettingsForNewDesigns' is the original name of this property."""

        temp = self.wrapped.MaterialsSettingsForNewDesigns.SelectedItemName

        if temp is None:
            return ''

        return temp

    @materials_settings_for_new_designs.setter
    def materials_settings_for_new_designs(self, value: 'str'):
        self.wrapped.MaterialsSettingsForNewDesigns.SetSelectedItem(str(value) if value else '')

    @property
    def shaft_settings_database_item(self) -> 'str':
        """str: 'ShaftSettingsDatabaseItem' is the original name of this property."""

        temp = self.wrapped.ShaftSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ''

        return temp

    @shaft_settings_database_item.setter
    def shaft_settings_database_item(self, value: 'str'):
        self.wrapped.ShaftSettingsDatabaseItem.SetSelectedItem(str(value) if value else '')

    @property
    def shaft_settings_for_new_designs(self) -> 'str':
        """str: 'ShaftSettingsForNewDesigns' is the original name of this property."""

        temp = self.wrapped.ShaftSettingsForNewDesigns.SelectedItemName

        if temp is None:
            return ''

        return temp

    @shaft_settings_for_new_designs.setter
    def shaft_settings_for_new_designs(self, value: 'str'):
        self.wrapped.ShaftSettingsForNewDesigns.SetSelectedItem(str(value) if value else '')

    @property
    def analysis_settings(self) -> '_50.AnalysisSettingsItem':
        """AnalysisSettingsItem: 'AnalysisSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_settings(self) -> '_1842.BearingSettingsItem':
        """BearingSettingsItem: 'BearingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_hypoid_gear_design_settings(self) -> '_934.BevelHypoidGearDesignSettingsItem':
        """BevelHypoidGearDesignSettingsItem: 'BevelHypoidGearDesignSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelHypoidGearDesignSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_hypoid_gear_rating_settings(self) -> '_936.BevelHypoidGearRatingSettingsItem':
        """BevelHypoidGearRatingSettingsItem: 'BevelHypoidGearRatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelHypoidGearRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_design_constraints_settings(self) -> '_1007.CylindricalGearDesignConstraints':
        """CylindricalGearDesignConstraints: 'CylindricalGearDesignConstraintsSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDesignConstraintsSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_design_and_rating_settings(self) -> '_448.CylindricalGearDesignAndRatingSettingsItem':
        """CylindricalGearDesignAndRatingSettingsItem: 'CylindricalGearDesignAndRatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDesignAndRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_micro_geometry_settings(self) -> '_1015.CylindricalGearMicroGeometrySettingsItem':
        """CylindricalGearMicroGeometrySettingsItem: 'CylindricalGearMicroGeometrySettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMicroGeometrySettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_constraints_settings(self) -> '_939.DesignConstraintsCollection':
        """DesignConstraintsCollection: 'DesignConstraintsSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignConstraintsSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def materials_settings(self) -> '_267.MaterialsSettingsItem':
        """MaterialsSettingsItem: 'MaterialsSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaterialsSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_settings(self) -> '_40.ShaftSettingsItem':
        """ShaftSettingsItem: 'ShaftSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSettings

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

    def copy_settings_from_file(self, file_name: 'str'):
        """ 'CopySettingsFromFile' is the original name of this method.

        Args:
            file_name (str)
        """

        file_name = str(file_name)
        self.wrapped.CopySettingsFromFile(file_name if file_name else '')

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
