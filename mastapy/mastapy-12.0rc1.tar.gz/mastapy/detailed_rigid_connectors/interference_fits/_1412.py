"""_1412.py

InterferenceFitHalfDesign
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.detailed_rigid_connectors.interference_fits import _1413
from mastapy.bearings.tolerances import _1883, _1868, _1874
from mastapy._internal.cast_exception import CastException
from mastapy.detailed_rigid_connectors import _1354
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_FIT_HALF_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits', 'InterferenceFitHalfDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('InterferenceFitHalfDesign',)


class InterferenceFitHalfDesign(_1354.DetailedRigidConnectorHalfDesign):
    """InterferenceFitHalfDesign

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_FIT_HALF_DESIGN

    def __init__(self, instance_to_wrap: 'InterferenceFitHalfDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_joint_diameter(self) -> 'float':
        """float: 'AverageJointDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageJointDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def average_surface_roughness(self) -> 'float':
        """float: 'AverageSurfaceRoughness' is the original name of this property."""

        temp = self.wrapped.AverageSurfaceRoughness

        if temp is None:
            return 0.0

        return temp

    @average_surface_roughness.setter
    def average_surface_roughness(self, value: 'float'):
        self.wrapped.AverageSurfaceRoughness = float(value) if value else 0.0

    @property
    def designation(self) -> 'str':
        """str: 'Designation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Designation

        if temp is None:
            return ''

        return temp

    @property
    def diameter_ratio(self) -> 'float':
        """float: 'DiameterRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiameterRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def joint_pressure_for_fully_plastic_part(self) -> 'float':
        """float: 'JointPressureForFullyPlasticPart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JointPressureForFullyPlasticPart

        if temp is None:
            return 0.0

        return temp

    @property
    def lower_deviation(self) -> 'float':
        """float: 'LowerDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LowerDeviation

        if temp is None:
            return 0.0

        return temp

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
    def nominal_joint_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NominalJointDiameter' is the original name of this property."""

        temp = self.wrapped.NominalJointDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @nominal_joint_diameter.setter
    def nominal_joint_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NominalJointDiameter = value

    @property
    def permissible_joint_pressure_for_fully_elastic_part(self) -> 'float':
        """float: 'PermissibleJointPressureForFullyElasticPart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleJointPressureForFullyElasticPart

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_relative_interference_for_fully_elastic_part(self) -> 'float':
        """float: 'PermissibleRelativeInterferenceForFullyElasticPart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleRelativeInterferenceForFullyElasticPart

        if temp is None:
            return 0.0

        return temp

    @property
    def required_safety_against_plastic_strain(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RequiredSafetyAgainstPlasticStrain' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyAgainstPlasticStrain

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @required_safety_against_plastic_strain.setter
    def required_safety_against_plastic_strain(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RequiredSafetyAgainstPlasticStrain = value

    @property
    def stress_region(self) -> '_1413.StressRegions':
        """StressRegions: 'StressRegion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressRegion

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1413.StressRegions)(value) if value is not None else None

    @property
    def upper_deviation(self) -> 'float':
        """float: 'UpperDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UpperDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def tolerance(self) -> '_1883.SupportTolerance':
        """SupportTolerance: 'Tolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Tolerance

        if temp is None:
            return None

        if _1883.SupportTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast tolerance to SupportTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tolerance_of_type_inner_support_tolerance(self) -> '_1868.InnerSupportTolerance':
        """InnerSupportTolerance: 'Tolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Tolerance

        if temp is None:
            return None

        if _1868.InnerSupportTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast tolerance to InnerSupportTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tolerance_of_type_outer_support_tolerance(self) -> '_1874.OuterSupportTolerance':
        """OuterSupportTolerance: 'Tolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Tolerance

        if temp is None:
            return None

        if _1874.OuterSupportTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast tolerance to OuterSupportTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
