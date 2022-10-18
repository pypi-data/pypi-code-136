"""_2549.py

ShaftHubConnection
"""


from typing import List

from PIL.Image import Image

from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import
from mastapy.detailed_rigid_connectors.splines import (
    _1376, _1361, _1381, _1356,
    _1359, _1363, _1366, _1367,
    _1374, _1386
)
from mastapy.system_model.part_model.couplings import (
    _2542, _2543, _2545, _2546,
    _2550, _2544
)
from mastapy.detailed_rigid_connectors.interference_fits import _1411
from mastapy.detailed_rigid_connectors.keyed_joints import _1403
from mastapy._internal.cast_exception import CastException
from mastapy.nodal_analysis import _57
from mastapy.system_model.part_model import _2399

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_ARRAY = python_net_import('System', 'Array')
_SHAFT_HUB_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ShaftHubConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnection',)


class ShaftHubConnection(_2399.Connector):
    """ShaftHubConnection

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION

    def __init__(self, instance_to_wrap: 'ShaftHubConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_spline_drawing(self) -> 'Image':
        """Image: 'TwoDSplineDrawing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TwoDSplineDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def additional_tilt_stiffness(self) -> 'float':
        """float: 'AdditionalTiltStiffness' is the original name of this property."""

        temp = self.wrapped.AdditionalTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @additional_tilt_stiffness.setter
    def additional_tilt_stiffness(self, value: 'float'):
        self.wrapped.AdditionalTiltStiffness = float(value) if value else 0.0

    @property
    def angle_of_first_connection_point(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AngleOfFirstConnectionPoint' is the original name of this property."""

        temp = self.wrapped.AngleOfFirstConnectionPoint

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @angle_of_first_connection_point.setter
    def angle_of_first_connection_point(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AngleOfFirstConnectionPoint = value

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
    def angular_extent_of_external_teeth(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AngularExtentOfExternalTeeth' is the original name of this property."""

        temp = self.wrapped.AngularExtentOfExternalTeeth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @angular_extent_of_external_teeth.setter
    def angular_extent_of_external_teeth(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AngularExtentOfExternalTeeth = value

    @property
    def axial_preload(self) -> 'float':
        """float: 'AxialPreload' is the original name of this property."""

        temp = self.wrapped.AxialPreload

        if temp is None:
            return 0.0

        return temp

    @axial_preload.setter
    def axial_preload(self, value: 'float'):
        self.wrapped.AxialPreload = float(value) if value else 0.0

    @property
    def axial_stiffness_shaft_hub_connection(self) -> 'float':
        """float: 'AxialStiffnessShaftHubConnection' is the original name of this property."""

        temp = self.wrapped.AxialStiffnessShaftHubConnection

        if temp is None:
            return 0.0

        return temp

    @axial_stiffness_shaft_hub_connection.setter
    def axial_stiffness_shaft_hub_connection(self, value: 'float'):
        self.wrapped.AxialStiffnessShaftHubConnection = float(value) if value else 0.0

    @property
    def centre_angle_of_first_external_tooth(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CentreAngleOfFirstExternalTooth' is the original name of this property."""

        temp = self.wrapped.CentreAngleOfFirstExternalTooth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @centre_angle_of_first_external_tooth.setter
    def centre_angle_of_first_external_tooth(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CentreAngleOfFirstExternalTooth = value

    @property
    def coefficient_of_friction(self) -> 'float':
        """float: 'CoefficientOfFriction' is the original name of this property."""

        temp = self.wrapped.CoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @coefficient_of_friction.setter
    def coefficient_of_friction(self, value: 'float'):
        self.wrapped.CoefficientOfFriction = float(value) if value else 0.0

    @property
    def contact_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ContactDiameter' is the original name of this property."""

        temp = self.wrapped.ContactDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @contact_diameter.setter
    def contact_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ContactDiameter = value

    @property
    def flank_contact_stiffness(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FlankContactStiffness' is the original name of this property."""

        temp = self.wrapped.FlankContactStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @flank_contact_stiffness.setter
    def flank_contact_stiffness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.FlankContactStiffness = value

    @property
    def helix_angle(self) -> 'float':
        """float: 'HelixAngle' is the original name of this property."""

        temp = self.wrapped.HelixAngle

        if temp is None:
            return 0.0

        return temp

    @helix_angle.setter
    def helix_angle(self, value: 'float'):
        self.wrapped.HelixAngle = float(value) if value else 0.0

    @property
    def inner_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerDiameter' is the original name of this property."""

        temp = self.wrapped.InnerDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @inner_diameter.setter
    def inner_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerDiameter = value

    @property
    def inner_half_material(self) -> 'str':
        """str: 'InnerHalfMaterial' is the original name of this property."""

        temp = self.wrapped.InnerHalfMaterial.SelectedItemName

        if temp is None:
            return ''

        return temp

    @inner_half_material.setter
    def inner_half_material(self, value: 'str'):
        self.wrapped.InnerHalfMaterial.SetSelectedItem(str(value) if value else '')

    @property
    def left_flank_helix_angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'LeftFlankHelixAngle' is the original name of this property."""

        temp = self.wrapped.LeftFlankHelixAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @left_flank_helix_angle.setter
    def left_flank_helix_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.LeftFlankHelixAngle = value

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value else 0.0

    @property
    def major_diameter_contact_stiffness(self) -> 'float':
        """float: 'MajorDiameterContactStiffness' is the original name of this property."""

        temp = self.wrapped.MajorDiameterContactStiffness

        if temp is None:
            return 0.0

        return temp

    @major_diameter_contact_stiffness.setter
    def major_diameter_contact_stiffness(self, value: 'float'):
        self.wrapped.MajorDiameterContactStiffness = float(value) if value else 0.0

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
    def normal_clearance(self) -> 'float':
        """float: 'NormalClearance' is the original name of this property."""

        temp = self.wrapped.NormalClearance

        if temp is None:
            return 0.0

        return temp

    @normal_clearance.setter
    def normal_clearance(self, value: 'float'):
        self.wrapped.NormalClearance = float(value) if value else 0.0

    @property
    def number_of_connection_points(self) -> 'int':
        """int: 'NumberOfConnectionPoints' is the original name of this property."""

        temp = self.wrapped.NumberOfConnectionPoints

        if temp is None:
            return 0

        return temp

    @number_of_connection_points.setter
    def number_of_connection_points(self, value: 'int'):
        self.wrapped.NumberOfConnectionPoints = int(value) if value else 0

    @property
    def number_of_contacts_per_direction(self) -> 'int':
        """int: 'NumberOfContactsPerDirection' is the original name of this property."""

        temp = self.wrapped.NumberOfContactsPerDirection

        if temp is None:
            return 0

        return temp

    @number_of_contacts_per_direction.setter
    def number_of_contacts_per_direction(self, value: 'int'):
        self.wrapped.NumberOfContactsPerDirection = int(value) if value else 0

    @property
    def outer_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterDiameter' is the original name of this property."""

        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @outer_diameter.setter
    def outer_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterDiameter = value

    @property
    def outer_half_material(self) -> 'str':
        """str: 'OuterHalfMaterial' is the original name of this property."""

        temp = self.wrapped.OuterHalfMaterial.SelectedItemName

        if temp is None:
            return ''

        return temp

    @outer_half_material.setter
    def outer_half_material(self, value: 'str'):
        self.wrapped.OuterHalfMaterial.SetSelectedItem(str(value) if value else '')

    @property
    def pressure_angle(self) -> 'float':
        """float: 'PressureAngle' is the original name of this property."""

        temp = self.wrapped.PressureAngle

        if temp is None:
            return 0.0

        return temp

    @pressure_angle.setter
    def pressure_angle(self, value: 'float'):
        self.wrapped.PressureAngle = float(value) if value else 0.0

    @property
    def radial_clearance(self) -> 'float':
        """float: 'RadialClearance' is the original name of this property."""

        temp = self.wrapped.RadialClearance

        if temp is None:
            return 0.0

        return temp

    @radial_clearance.setter
    def radial_clearance(self, value: 'float'):
        self.wrapped.RadialClearance = float(value) if value else 0.0

    @property
    def radial_stiffness_shaft_hub_connection(self) -> 'float':
        """float: 'RadialStiffnessShaftHubConnection' is the original name of this property."""

        temp = self.wrapped.RadialStiffnessShaftHubConnection

        if temp is None:
            return 0.0

        return temp

    @radial_stiffness_shaft_hub_connection.setter
    def radial_stiffness_shaft_hub_connection(self, value: 'float'):
        self.wrapped.RadialStiffnessShaftHubConnection = float(value) if value else 0.0

    @property
    def right_flank_helix_angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RightFlankHelixAngle' is the original name of this property."""

        temp = self.wrapped.RightFlankHelixAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @right_flank_helix_angle.setter
    def right_flank_helix_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RightFlankHelixAngle = value

    @property
    def spline_type(self) -> '_1376.SplineDesignTypes':
        """SplineDesignTypes: 'SplineType' is the original name of this property."""

        temp = self.wrapped.SplineType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1376.SplineDesignTypes)(value) if value is not None else None

    @spline_type.setter
    def spline_type(self, value: '_1376.SplineDesignTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.SplineType = value

    @property
    def stiffness_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_RigidConnectorStiffnessType':
        """enum_with_selected_value.EnumWithSelectedValue_RigidConnectorStiffnessType: 'StiffnessType' is the original name of this property."""

        temp = self.wrapped.StiffnessType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_RigidConnectorStiffnessType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @stiffness_type.setter
    def stiffness_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_RigidConnectorStiffnessType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_RigidConnectorStiffnessType.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.StiffnessType = value

    @property
    def tangential_stiffness(self) -> 'float':
        """float: 'TangentialStiffness' is the original name of this property."""

        temp = self.wrapped.TangentialStiffness

        if temp is None:
            return 0.0

        return temp

    @tangential_stiffness.setter
    def tangential_stiffness(self, value: 'float'):
        self.wrapped.TangentialStiffness = float(value) if value else 0.0

    @property
    def tilt_clearance(self) -> 'float':
        """float: 'TiltClearance' is the original name of this property."""

        temp = self.wrapped.TiltClearance

        if temp is None:
            return 0.0

        return temp

    @tilt_clearance.setter
    def tilt_clearance(self, value: 'float'):
        self.wrapped.TiltClearance = float(value) if value else 0.0

    @property
    def tilt_stiffness_shaft_hub_connection(self) -> 'float':
        """float: 'TiltStiffnessShaftHubConnection' is the original name of this property."""

        temp = self.wrapped.TiltStiffnessShaftHubConnection

        if temp is None:
            return 0.0

        return temp

    @tilt_stiffness_shaft_hub_connection.setter
    def tilt_stiffness_shaft_hub_connection(self, value: 'float'):
        self.wrapped.TiltStiffnessShaftHubConnection = float(value) if value else 0.0

    @property
    def tilt_stiffness_type(self) -> '_2543.RigidConnectorTiltStiffnessTypes':
        """RigidConnectorTiltStiffnessTypes: 'TiltStiffnessType' is the original name of this property."""

        temp = self.wrapped.TiltStiffnessType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_2543.RigidConnectorTiltStiffnessTypes)(value) if value is not None else None

    @tilt_stiffness_type.setter
    def tilt_stiffness_type(self, value: '_2543.RigidConnectorTiltStiffnessTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.TiltStiffnessType = value

    @property
    def tooth_spacing_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_RigidConnectorToothSpacingType':
        """enum_with_selected_value.EnumWithSelectedValue_RigidConnectorToothSpacingType: 'ToothSpacingType' is the original name of this property."""

        temp = self.wrapped.ToothSpacingType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_RigidConnectorToothSpacingType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @tooth_spacing_type.setter
    def tooth_spacing_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_RigidConnectorToothSpacingType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_RigidConnectorToothSpacingType.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ToothSpacingType = value

    @property
    def torsional_stiffness_shaft_hub_connection(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'TorsionalStiffnessShaftHubConnection' is the original name of this property."""

        temp = self.wrapped.TorsionalStiffnessShaftHubConnection

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @torsional_stiffness_shaft_hub_connection.setter
    def torsional_stiffness_shaft_hub_connection(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.TorsionalStiffnessShaftHubConnection = value

    @property
    def torsional_twist_preload(self) -> 'float':
        """float: 'TorsionalTwistPreload' is the original name of this property."""

        temp = self.wrapped.TorsionalTwistPreload

        if temp is None:
            return 0.0

        return temp

    @torsional_twist_preload.setter
    def torsional_twist_preload(self, value: 'float'):
        self.wrapped.TorsionalTwistPreload = float(value) if value else 0.0

    @property
    def type_(self) -> 'enum_with_selected_value.EnumWithSelectedValue_RigidConnectorTypes':
        """enum_with_selected_value.EnumWithSelectedValue_RigidConnectorTypes: 'Type' is the original name of this property."""

        temp = self.wrapped.Type

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_RigidConnectorTypes.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @type_.setter
    def type_(self, value: 'enum_with_selected_value.EnumWithSelectedValue_RigidConnectorTypes.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_RigidConnectorTypes.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Type = value

    @property
    def type_of_fit(self) -> 'enum_with_selected_value.EnumWithSelectedValue_FitTypes':
        """enum_with_selected_value.EnumWithSelectedValue_FitTypes: 'TypeOfFit' is the original name of this property."""

        temp = self.wrapped.TypeOfFit

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_FitTypes.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @type_of_fit.setter
    def type_of_fit(self, value: 'enum_with_selected_value.EnumWithSelectedValue_FitTypes.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_FitTypes.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.TypeOfFit = value

    @property
    def interference_fit_design(self) -> '_1411.InterferenceFitDesign':
        """InterferenceFitDesign: 'InterferenceFitDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InterferenceFitDesign

        if temp is None:
            return None

        if _1411.InterferenceFitDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast interference_fit_design to InterferenceFitDesign. Expected: {}.'.format(temp.__class__.__qualname__))

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
    def nonlinear_stiffness(self) -> '_57.DiagonalNonlinearStiffness':
        """DiagonalNonlinearStiffness: 'NonlinearStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonlinearStiffness

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
    def spline_joint_design(self) -> '_1381.SplineJointDesign':
        """SplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign

        if temp is None:
            return None

        if _1381.SplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to SplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spline_joint_design_of_type_custom_spline_joint_design(self) -> '_1356.CustomSplineJointDesign':
        """CustomSplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign

        if temp is None:
            return None

        if _1356.CustomSplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to CustomSplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spline_joint_design_of_type_din5480_spline_joint_design(self) -> '_1359.DIN5480SplineJointDesign':
        """DIN5480SplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign

        if temp is None:
            return None

        if _1359.DIN5480SplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to DIN5480SplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spline_joint_design_of_type_gbt3478_spline_joint_design(self) -> '_1363.GBT3478SplineJointDesign':
        """GBT3478SplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign

        if temp is None:
            return None

        if _1363.GBT3478SplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to GBT3478SplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spline_joint_design_of_type_iso4156_spline_joint_design(self) -> '_1366.ISO4156SplineJointDesign':
        """ISO4156SplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign

        if temp is None:
            return None

        if _1366.ISO4156SplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to ISO4156SplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spline_joint_design_of_type_jisb1603_spline_joint_design(self) -> '_1367.JISB1603SplineJointDesign':
        """JISB1603SplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign

        if temp is None:
            return None

        if _1367.JISB1603SplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to JISB1603SplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spline_joint_design_of_type_sae_spline_joint_design(self) -> '_1374.SAESplineJointDesign':
        """SAESplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign

        if temp is None:
            return None

        if _1374.SAESplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to SAESplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spline_joint_design_of_type_standard_spline_joint_design(self) -> '_1386.StandardSplineJointDesign':
        """StandardSplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign

        if temp is None:
            return None

        if _1386.StandardSplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to StandardSplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

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
    def full_stiffness_matrix(self) -> 'List[List[float]]':
        """List[List[float]]: 'FullStiffnessMatrix' is the original name of this property."""

        temp = self.wrapped.FullStiffnessMatrix

        if temp is None:
            return None

        value = conversion.pn_to_mp_list_float_2d(temp)
        return value

    @full_stiffness_matrix.setter
    def full_stiffness_matrix(self, value: 'List[List[float]]'):
        value = value if value else None
        value = conversion.mp_to_pn_list_float_2d(value)
        self.wrapped.FullStiffnessMatrix = value
