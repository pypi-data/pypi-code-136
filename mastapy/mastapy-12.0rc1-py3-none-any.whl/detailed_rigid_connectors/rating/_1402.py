"""_1402.py

ShaftHubConnectionRating
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.detailed_rigid_connectors import _1353
from mastapy.detailed_rigid_connectors.splines import (
    _1356, _1359, _1363, _1366,
    _1367, _1374, _1381, _1386
)
from mastapy._internal.cast_exception import CastException
from mastapy.detailed_rigid_connectors.keyed_joints import _1403
from mastapy.detailed_rigid_connectors.interference_fits import _1411
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_RATING = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Rating', 'ShaftHubConnectionRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionRating',)


class ShaftHubConnectionRating(_0.APIBase):
    """ShaftHubConnectionRating

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_RATING

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_rating_information(self) -> 'str':
        """str: 'AdditionalRatingInformation' is the original name of this property."""

        temp = self.wrapped.AdditionalRatingInformation

        if temp is None:
            return ''

        return temp

    @additional_rating_information.setter
    def additional_rating_information(self, value: 'str'):
        self.wrapped.AdditionalRatingInformation = str(value) if value else ''

    @property
    def joint_design(self) -> '_1353.DetailedRigidConnectorDesign':
        """DetailedRigidConnectorDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JointDesign

        if temp is None:
            return None

        if _1353.DetailedRigidConnectorDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast joint_design to DetailedRigidConnectorDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def joint_design_of_type_custom_spline_joint_design(self) -> '_1356.CustomSplineJointDesign':
        """CustomSplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JointDesign

        if temp is None:
            return None

        if _1356.CustomSplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast joint_design to CustomSplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def joint_design_of_type_din5480_spline_joint_design(self) -> '_1359.DIN5480SplineJointDesign':
        """DIN5480SplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JointDesign

        if temp is None:
            return None

        if _1359.DIN5480SplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast joint_design to DIN5480SplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def joint_design_of_type_gbt3478_spline_joint_design(self) -> '_1363.GBT3478SplineJointDesign':
        """GBT3478SplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JointDesign

        if temp is None:
            return None

        if _1363.GBT3478SplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast joint_design to GBT3478SplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def joint_design_of_type_iso4156_spline_joint_design(self) -> '_1366.ISO4156SplineJointDesign':
        """ISO4156SplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JointDesign

        if temp is None:
            return None

        if _1366.ISO4156SplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast joint_design to ISO4156SplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def joint_design_of_type_jisb1603_spline_joint_design(self) -> '_1367.JISB1603SplineJointDesign':
        """JISB1603SplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JointDesign

        if temp is None:
            return None

        if _1367.JISB1603SplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast joint_design to JISB1603SplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def joint_design_of_type_sae_spline_joint_design(self) -> '_1374.SAESplineJointDesign':
        """SAESplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JointDesign

        if temp is None:
            return None

        if _1374.SAESplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast joint_design to SAESplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def joint_design_of_type_spline_joint_design(self) -> '_1381.SplineJointDesign':
        """SplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JointDesign

        if temp is None:
            return None

        if _1381.SplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast joint_design to SplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def joint_design_of_type_standard_spline_joint_design(self) -> '_1386.StandardSplineJointDesign':
        """StandardSplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JointDesign

        if temp is None:
            return None

        if _1386.StandardSplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast joint_design to StandardSplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def joint_design_of_type_keyed_joint_design(self) -> '_1403.KeyedJointDesign':
        """KeyedJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JointDesign

        if temp is None:
            return None

        if _1403.KeyedJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast joint_design to KeyedJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def joint_design_of_type_interference_fit_design(self) -> '_1411.InterferenceFitDesign':
        """InterferenceFitDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JointDesign

        if temp is None:
            return None

        if _1411.InterferenceFitDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast joint_design to InterferenceFitDesign. Expected: {}.'.format(temp.__class__.__qualname__))

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
