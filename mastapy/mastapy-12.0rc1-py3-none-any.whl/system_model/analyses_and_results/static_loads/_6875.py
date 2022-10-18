"""_6875.py

ShaftHubConnectionLoadCase
"""


from typing import List

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.couplings import _2549, _2550, _2544
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results.static_loads import _6776

_ARRAY = python_net_import('System', 'Array')
_SHAFT_HUB_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ShaftHubConnectionLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionLoadCase',)


class ShaftHubConnectionLoadCase(_6776.ConnectorLoadCase):
    """ShaftHubConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_LOAD_CASE

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_tilt_stiffness(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AdditionalTiltStiffness' is the original name of this property."""

        temp = self.wrapped.AdditionalTiltStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @additional_tilt_stiffness.setter
    def additional_tilt_stiffness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AdditionalTiltStiffness = value

    @property
    def angular_backlash(self) -> 'float':
        """float: 'AngularBacklash' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def application_factor(self) -> 'float':
        """float: 'ApplicationFactor' is the original name of this property."""

        temp = self.wrapped.ApplicationFactor

        if temp is None:
            return 0.0

        return temp

    @application_factor.setter
    def application_factor(self, value: 'float'):
        self.wrapped.ApplicationFactor = float(value) if value else 0.0

    @property
    def axial_preload(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AxialPreload' is the original name of this property."""

        temp = self.wrapped.AxialPreload

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @axial_preload.setter
    def axial_preload(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AxialPreload = value

    @property
    def axial_stiffness(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AxialStiffness' is the original name of this property."""

        temp = self.wrapped.AxialStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @axial_stiffness.setter
    def axial_stiffness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AxialStiffness = value

    @property
    def load_distribution_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'LoadDistributionFactor' is the original name of this property."""

        temp = self.wrapped.LoadDistributionFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @load_distribution_factor.setter
    def load_distribution_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.LoadDistributionFactor = value

    @property
    def load_distribution_factor_single_key(self) -> 'float':
        """float: 'LoadDistributionFactorSingleKey' is the original name of this property."""

        temp = self.wrapped.LoadDistributionFactorSingleKey

        if temp is None:
            return 0.0

        return temp

    @load_distribution_factor_single_key.setter
    def load_distribution_factor_single_key(self, value: 'float'):
        self.wrapped.LoadDistributionFactorSingleKey = float(value) if value else 0.0

    @property
    def major_diameter_diametral_clearance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MajorDiameterDiametralClearance' is the original name of this property."""

        temp = self.wrapped.MajorDiameterDiametralClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @major_diameter_diametral_clearance.setter
    def major_diameter_diametral_clearance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MajorDiameterDiametralClearance = value

    @property
    def normal_clearance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NormalClearance' is the original name of this property."""

        temp = self.wrapped.NormalClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @normal_clearance.setter
    def normal_clearance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NormalClearance = value

    @property
    def number_of_torque_peaks(self) -> 'float':
        """float: 'NumberOfTorquePeaks' is the original name of this property."""

        temp = self.wrapped.NumberOfTorquePeaks

        if temp is None:
            return 0.0

        return temp

    @number_of_torque_peaks.setter
    def number_of_torque_peaks(self, value: 'float'):
        self.wrapped.NumberOfTorquePeaks = float(value) if value else 0.0

    @property
    def number_of_torque_reversals(self) -> 'float':
        """float: 'NumberOfTorqueReversals' is the original name of this property."""

        temp = self.wrapped.NumberOfTorqueReversals

        if temp is None:
            return 0.0

        return temp

    @number_of_torque_reversals.setter
    def number_of_torque_reversals(self, value: 'float'):
        self.wrapped.NumberOfTorqueReversals = float(value) if value else 0.0

    @property
    def override_design_specified_stiffness_matrix(self) -> 'bool':
        """bool: 'OverrideDesignSpecifiedStiffnessMatrix' is the original name of this property."""

        temp = self.wrapped.OverrideDesignSpecifiedStiffnessMatrix

        if temp is None:
            return False

        return temp

    @override_design_specified_stiffness_matrix.setter
    def override_design_specified_stiffness_matrix(self, value: 'bool'):
        self.wrapped.OverrideDesignSpecifiedStiffnessMatrix = bool(value) if value else False

    @property
    def radial_clearance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RadialClearance' is the original name of this property."""

        temp = self.wrapped.RadialClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @radial_clearance.setter
    def radial_clearance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RadialClearance = value

    @property
    def radial_stiffness(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RadialStiffness' is the original name of this property."""

        temp = self.wrapped.RadialStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @radial_stiffness.setter
    def radial_stiffness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RadialStiffness = value

    @property
    def specified_application_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SpecifiedApplicationFactor' is the original name of this property."""

        temp = self.wrapped.SpecifiedApplicationFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @specified_application_factor.setter
    def specified_application_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SpecifiedApplicationFactor = value

    @property
    def specified_backlash_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SpecifiedBacklashFactor' is the original name of this property."""

        temp = self.wrapped.SpecifiedBacklashFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @specified_backlash_factor.setter
    def specified_backlash_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SpecifiedBacklashFactor = value

    @property
    def specified_load_distribution_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SpecifiedLoadDistributionFactor' is the original name of this property."""

        temp = self.wrapped.SpecifiedLoadDistributionFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @specified_load_distribution_factor.setter
    def specified_load_distribution_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SpecifiedLoadDistributionFactor = value

    @property
    def specified_load_sharing_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SpecifiedLoadSharingFactor' is the original name of this property."""

        temp = self.wrapped.SpecifiedLoadSharingFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @specified_load_sharing_factor.setter
    def specified_load_sharing_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SpecifiedLoadSharingFactor = value

    @property
    def tilt_clearance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'TiltClearance' is the original name of this property."""

        temp = self.wrapped.TiltClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @tilt_clearance.setter
    def tilt_clearance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.TiltClearance = value

    @property
    def tilt_stiffness(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'TiltStiffness' is the original name of this property."""

        temp = self.wrapped.TiltStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @tilt_stiffness.setter
    def tilt_stiffness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.TiltStiffness = value

    @property
    def torsional_stiffness(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'TorsionalStiffness' is the original name of this property."""

        temp = self.wrapped.TorsionalStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @torsional_stiffness.setter
    def torsional_stiffness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.TorsionalStiffness = value

    @property
    def torsional_twist_preload(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'TorsionalTwistPreload' is the original name of this property."""

        temp = self.wrapped.TorsionalTwistPreload

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @torsional_twist_preload.setter
    def torsional_twist_preload(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.TorsionalTwistPreload = value

    @property
    def component_design(self) -> '_2549.ShaftHubConnection':
        """ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_flank_lead_relief(self) -> '_2550.SplineLeadRelief':
        """SplineLeadRelief: 'LeftFlankLeadRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankLeadRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank_lead_relief(self) -> '_2550.SplineLeadRelief':
        """SplineLeadRelief: 'RightFlankLeadRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankLeadRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_reliefs(self) -> 'List[_2550.SplineLeadRelief]':
        """List[SplineLeadRelief]: 'LeadReliefs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadReliefs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[ShaftHubConnectionLoadCase]':
        """List[ShaftHubConnectionLoadCase]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def tooth_locations_external_spline_half(self) -> 'List[_2544.RigidConnectorToothLocation]':
        """List[RigidConnectorToothLocation]: 'ToothLocationsExternalSplineHalf' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothLocationsExternalSplineHalf

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def specified_stiffness_for_shaft_hub_connection_in_local_coordinate_system(self) -> 'List[List[float]]':
        """List[List[float]]: 'SpecifiedStiffnessForShaftHubConnectionInLocalCoordinateSystem' is the original name of this property."""

        temp = self.wrapped.SpecifiedStiffnessForShaftHubConnectionInLocalCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_list_float_2d(temp)
        return value

    @specified_stiffness_for_shaft_hub_connection_in_local_coordinate_system.setter
    def specified_stiffness_for_shaft_hub_connection_in_local_coordinate_system(self, value: 'List[List[float]]'):
        value = value if value else None
        value = conversion.mp_to_pn_list_float_2d(value)
        self.wrapped.SpecifiedStiffnessForShaftHubConnectionInLocalCoordinateSystem = value
