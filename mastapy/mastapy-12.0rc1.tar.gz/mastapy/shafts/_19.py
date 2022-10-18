"""_19.py

ShaftDamageResults
"""


from typing import List

from mastapy.math_utility import _1489
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._math.vector_3d import Vector3D
from mastapy.nodal_analysis import _81
from mastapy.shafts import _37, _40, _36
from mastapy.utility.report import _1751
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_SHAFT_DAMAGE_RESULTS = python_net_import('SMT.MastaAPI.Shafts', 'ShaftDamageResults')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftDamageResults',)


class ShaftDamageResults(_0.APIBase):
    """ShaftDamageResults

    This is a mastapy class.
    """

    TYPE = _SHAFT_DAMAGE_RESULTS

    def __init__(self, instance_to_wrap: 'ShaftDamageResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cyclic_degrees_of_utilisation(self) -> 'List[_1489.RealVector]':
        """List[RealVector]: 'CyclicDegreesOfUtilisation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CyclicDegreesOfUtilisation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def displacement_angular(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'DisplacementAngular' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DisplacementAngular

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def displacement_linear(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'DisplacementLinear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DisplacementLinear

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def displacement_maximum_radial_magnitude(self) -> 'float':
        """float: 'DisplacementMaximumRadialMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DisplacementMaximumRadialMagnitude

        if temp is None:
            return 0.0

        return temp

    @property
    def force_angular(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'ForceAngular' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceAngular

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def force_linear(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'ForceLinear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceLinear

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def load_case_name(self) -> 'str':
        """str: 'LoadCaseName' is the original name of this property."""

        temp = self.wrapped.LoadCaseName

        if temp is None:
            return ''

        return temp

    @load_case_name.setter
    def load_case_name(self, value: 'str'):
        self.wrapped.LoadCaseName = str(value) if value else ''

    @property
    def rating_type_for_shaft_reliability(self) -> '_81.RatingTypeForShaftReliability':
        """RatingTypeForShaftReliability: 'RatingTypeForShaftReliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingTypeForShaftReliability

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_81.RatingTypeForShaftReliability)(value) if value is not None else None

    @property
    def stress_highest_equivalent_fully_reversed(self) -> 'float':
        """float: 'StressHighestEquivalentFullyReversed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressHighestEquivalentFullyReversed

        if temp is None:
            return 0.0

        return temp

    @property
    def using_fkm_shaft_rating_method(self) -> 'bool':
        """bool: 'UsingFKMShaftRatingMethod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UsingFKMShaftRatingMethod

        if temp is None:
            return False

        return temp

    @property
    def worst_fatigue_damage(self) -> 'float':
        """float: 'WorstFatigueDamage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstFatigueDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_fatigue_safety_factor(self) -> 'float':
        """float: 'WorstFatigueSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstFatigueSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_fatigue_safety_factor_for_infinite_life(self) -> 'float':
        """float: 'WorstFatigueSafetyFactorForInfiniteLife' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstFatigueSafetyFactorForInfiniteLife

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_reliability_for_finite_life(self) -> 'float':
        """float: 'WorstReliabilityForFiniteLife' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstReliabilityForFiniteLife

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_reliability_for_infinite_life(self) -> 'float':
        """float: 'WorstReliabilityForInfiniteLife' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstReliabilityForInfiniteLife

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_static_safety_factor(self) -> 'float':
        """float: 'WorstStaticSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstStaticSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_section_end_with_worst_fatigue_safety_factor(self) -> '_37.ShaftSectionEndDamageResults':
        """ShaftSectionEndDamageResults: 'ShaftSectionEndWithWorstFatigueSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSectionEndWithWorstFatigueSafetyFactor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_section_end_with_worst_fatigue_safety_factor_for_infinite_life(self) -> '_37.ShaftSectionEndDamageResults':
        """ShaftSectionEndDamageResults: 'ShaftSectionEndWithWorstFatigueSafetyFactorForInfiniteLife' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSectionEndWithWorstFatigueSafetyFactorForInfiniteLife

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_section_end_with_worst_static_safety_factor(self) -> '_37.ShaftSectionEndDamageResults':
        """ShaftSectionEndDamageResults: 'ShaftSectionEndWithWorstStaticSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSectionEndWithWorstStaticSafetyFactor

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
    def shaft_section_damage_results(self) -> 'List[_36.ShaftSectionDamageResults]':
        """List[ShaftSectionDamageResults]: 'ShaftSectionDamageResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSectionDamageResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_section_end_results_by_offset_with_worst_safety_factor(self) -> 'List[_37.ShaftSectionEndDamageResults]':
        """List[ShaftSectionEndDamageResults]: 'ShaftSectionEndResultsByOffsetWithWorstSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSectionEndResultsByOffsetWithWorstSafetyFactor

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_damage_chart_items(self) -> 'List[str]':
        """List[str]: 'ShaftDamageChartItems' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftDamageChartItems

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
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

    def shaft_damage_chart(self, item: 'str', title: 'str') -> '_1751.SimpleChartDefinition':
        """ 'ShaftDamageChart' is the original name of this method.

        Args:
            item (str)
            title (str)

        Returns:
            mastapy.utility.report.SimpleChartDefinition
        """

        item = str(item)
        title = str(title)
        method_result = self.wrapped.ShaftDamageChart(item if item else '', title if title else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

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
