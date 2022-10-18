"""_1889.py

ProfileSet
"""


from typing import List

from mastapy.bearings import _1852
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.bearings.roller_bearing_profiles import (
    _1897, _1891, _1892, _1893,
    _1894, _1895, _1896, _1898
)
from mastapy._internal.cast_exception import CastException
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_PROFILE_SET = python_net_import('SMT.MastaAPI.Bearings.RollerBearingProfiles', 'ProfileSet')


__docformat__ = 'restructuredtext en'
__all__ = ('ProfileSet',)


class ProfileSet(_0.APIBase):
    """ProfileSet

    This is a mastapy class.
    """

    TYPE = _PROFILE_SET

    def __init__(self, instance_to_wrap: 'ProfileSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_profile_type(self) -> '_1852.RollerBearingProfileTypes':
        """RollerBearingProfileTypes: 'ActiveProfileType' is the original name of this property."""

        temp = self.wrapped.ActiveProfileType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1852.RollerBearingProfileTypes)(value) if value is not None else None

    @active_profile_type.setter
    def active_profile_type(self, value: '_1852.RollerBearingProfileTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ActiveProfileType = value

    @property
    def active_profile(self) -> '_1897.RollerBearingProfile':
        """RollerBearingProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveProfile

        if temp is None:
            return None

        if _1897.RollerBearingProfile.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_profile to RollerBearingProfile. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_profile_of_type_roller_bearing_conical_profile(self) -> '_1891.RollerBearingConicalProfile':
        """RollerBearingConicalProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveProfile

        if temp is None:
            return None

        if _1891.RollerBearingConicalProfile.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_profile to RollerBearingConicalProfile. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_profile_of_type_roller_bearing_crowned_profile(self) -> '_1892.RollerBearingCrownedProfile':
        """RollerBearingCrownedProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveProfile

        if temp is None:
            return None

        if _1892.RollerBearingCrownedProfile.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_profile to RollerBearingCrownedProfile. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_profile_of_type_roller_bearing_din_lundberg_profile(self) -> '_1893.RollerBearingDinLundbergProfile':
        """RollerBearingDinLundbergProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveProfile

        if temp is None:
            return None

        if _1893.RollerBearingDinLundbergProfile.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_profile to RollerBearingDinLundbergProfile. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_profile_of_type_roller_bearing_flat_profile(self) -> '_1894.RollerBearingFlatProfile':
        """RollerBearingFlatProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveProfile

        if temp is None:
            return None

        if _1894.RollerBearingFlatProfile.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_profile to RollerBearingFlatProfile. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_profile_of_type_roller_bearing_johns_gohar_profile(self) -> '_1895.RollerBearingJohnsGoharProfile':
        """RollerBearingJohnsGoharProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveProfile

        if temp is None:
            return None

        if _1895.RollerBearingJohnsGoharProfile.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_profile to RollerBearingJohnsGoharProfile. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_profile_of_type_roller_bearing_lundberg_profile(self) -> '_1896.RollerBearingLundbergProfile':
        """RollerBearingLundbergProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveProfile

        if temp is None:
            return None

        if _1896.RollerBearingLundbergProfile.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_profile to RollerBearingLundbergProfile. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_profile_of_type_roller_bearing_user_specified_profile(self) -> '_1898.RollerBearingUserSpecifiedProfile':
        """RollerBearingUserSpecifiedProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveProfile

        if temp is None:
            return None

        if _1898.RollerBearingUserSpecifiedProfile.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_profile to RollerBearingUserSpecifiedProfile. Expected: {}.'.format(temp.__class__.__qualname__))

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
