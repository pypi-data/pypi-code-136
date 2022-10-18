"""_1909.py

LoadedBearingResults
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.bearings.bearing_results import _1920
from mastapy.bearings.bearing_designs import (
    _2085, _2086, _2087, _2088,
    _2089
)
from mastapy._internal.cast_exception import CastException
from mastapy.bearings.bearing_designs.rolling import (
    _2090, _2091, _2092, _2093,
    _2094, _2095, _2097, _2103,
    _2104, _2105, _2109, _2114,
    _2115, _2116, _2117, _2120,
    _2121, _2124, _2125, _2126,
    _2127, _2128, _2129
)
from mastapy.bearings.bearing_designs.fluid_film import (
    _2142, _2144, _2146, _2148,
    _2149, _2150
)
from mastapy.bearings.bearing_designs.concept import _2152, _2153, _2154
from mastapy.math_utility.measured_vectors import _1528
from mastapy.bearings.bearing_results.rolling import _2024
from mastapy.bearings import _1836
from mastapy._internal.python_net import python_net_import

_LOADED_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBearingResults',)


class LoadedBearingResults(_1836.BearingLoadCaseResultsLightweight):
    """LoadedBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_BEARING_RESULTS

    def __init__(self, instance_to_wrap: 'LoadedBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_of_gravity_from_z_axis(self) -> 'float':
        """float: 'AngleOfGravityFromZAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngleOfGravityFromZAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_displacement_preload(self) -> 'float':
        """float: 'AxialDisplacementPreload' is the original name of this property."""

        temp = self.wrapped.AxialDisplacementPreload

        if temp is None:
            return 0.0

        return temp

    @axial_displacement_preload.setter
    def axial_displacement_preload(self, value: 'float'):
        self.wrapped.AxialDisplacementPreload = float(value) if value else 0.0

    @property
    def duration(self) -> 'float':
        """float: 'Duration' is the original name of this property."""

        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @duration.setter
    def duration(self, value: 'float'):
        self.wrapped.Duration = float(value) if value else 0.0

    @property
    def force_results_are_overridden(self) -> 'bool':
        """bool: 'ForceResultsAreOverridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceResultsAreOverridden

        if temp is None:
            return False

        return temp

    @property
    def inner_ring_angular_velocity(self) -> 'float':
        """float: 'InnerRingAngularVelocity' is the original name of this property."""

        temp = self.wrapped.InnerRingAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @inner_ring_angular_velocity.setter
    def inner_ring_angular_velocity(self, value: 'float'):
        self.wrapped.InnerRingAngularVelocity = float(value) if value else 0.0

    @property
    def orientation(self) -> '_1920.Orientations':
        """Orientations: 'Orientation' is the original name of this property."""

        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1920.Orientations)(value) if value is not None else None

    @orientation.setter
    def orientation(self, value: '_1920.Orientations'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Orientation = value

    @property
    def outer_ring_angular_velocity(self) -> 'float':
        """float: 'OuterRingAngularVelocity' is the original name of this property."""

        temp = self.wrapped.OuterRingAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @outer_ring_angular_velocity.setter
    def outer_ring_angular_velocity(self, value: 'float'):
        self.wrapped.OuterRingAngularVelocity = float(value) if value else 0.0

    @property
    def relative_angular_velocity(self) -> 'float':
        """float: 'RelativeAngularVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_axial_displacement(self) -> 'float':
        """float: 'RelativeAxialDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeAxialDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_radial_displacement(self) -> 'float':
        """float: 'RelativeRadialDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeRadialDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_relative_angular_velocity(self) -> 'float':
        """float: 'SignedRelativeAngularVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SignedRelativeAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def specified_axial_internal_clearance(self) -> 'float':
        """float: 'SpecifiedAxialInternalClearance' is the original name of this property."""

        temp = self.wrapped.SpecifiedAxialInternalClearance

        if temp is None:
            return 0.0

        return temp

    @specified_axial_internal_clearance.setter
    def specified_axial_internal_clearance(self, value: 'float'):
        self.wrapped.SpecifiedAxialInternalClearance = float(value) if value else 0.0

    @property
    def specified_radial_internal_clearance(self) -> 'float':
        """float: 'SpecifiedRadialInternalClearance' is the original name of this property."""

        temp = self.wrapped.SpecifiedRadialInternalClearance

        if temp is None:
            return 0.0

        return temp

    @specified_radial_internal_clearance.setter
    def specified_radial_internal_clearance(self, value: 'float'):
        self.wrapped.SpecifiedRadialInternalClearance = float(value) if value else 0.0

    @property
    def bearing(self) -> '_2085.BearingDesign':
        """BearingDesign: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2085.BearingDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to BearingDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_detailed_bearing(self) -> '_2086.DetailedBearing':
        """DetailedBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2086.DetailedBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to DetailedBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_dummy_rolling_bearing(self) -> '_2087.DummyRollingBearing':
        """DummyRollingBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2087.DummyRollingBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to DummyRollingBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_linear_bearing(self) -> '_2088.LinearBearing':
        """LinearBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2088.LinearBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to LinearBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_non_linear_bearing(self) -> '_2089.NonLinearBearing':
        """NonLinearBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2089.NonLinearBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to NonLinearBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_angular_contact_ball_bearing(self) -> '_2090.AngularContactBallBearing':
        """AngularContactBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2090.AngularContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to AngularContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_angular_contact_thrust_ball_bearing(self) -> '_2091.AngularContactThrustBallBearing':
        """AngularContactThrustBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2091.AngularContactThrustBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to AngularContactThrustBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_asymmetric_spherical_roller_bearing(self) -> '_2092.AsymmetricSphericalRollerBearing':
        """AsymmetricSphericalRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2092.AsymmetricSphericalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to AsymmetricSphericalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_axial_thrust_cylindrical_roller_bearing(self) -> '_2093.AxialThrustCylindricalRollerBearing':
        """AxialThrustCylindricalRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2093.AxialThrustCylindricalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to AxialThrustCylindricalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_axial_thrust_needle_roller_bearing(self) -> '_2094.AxialThrustNeedleRollerBearing':
        """AxialThrustNeedleRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2094.AxialThrustNeedleRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to AxialThrustNeedleRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_ball_bearing(self) -> '_2095.BallBearing':
        """BallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2095.BallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to BallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_barrel_roller_bearing(self) -> '_2097.BarrelRollerBearing':
        """BarrelRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2097.BarrelRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to BarrelRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_crossed_roller_bearing(self) -> '_2103.CrossedRollerBearing':
        """CrossedRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2103.CrossedRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to CrossedRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_cylindrical_roller_bearing(self) -> '_2104.CylindricalRollerBearing':
        """CylindricalRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2104.CylindricalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to CylindricalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_deep_groove_ball_bearing(self) -> '_2105.DeepGrooveBallBearing':
        """DeepGrooveBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2105.DeepGrooveBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to DeepGrooveBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_four_point_contact_ball_bearing(self) -> '_2109.FourPointContactBallBearing':
        """FourPointContactBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2109.FourPointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to FourPointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_multi_point_contact_ball_bearing(self) -> '_2114.MultiPointContactBallBearing':
        """MultiPointContactBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2114.MultiPointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to MultiPointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_needle_roller_bearing(self) -> '_2115.NeedleRollerBearing':
        """NeedleRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2115.NeedleRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to NeedleRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_non_barrel_roller_bearing(self) -> '_2116.NonBarrelRollerBearing':
        """NonBarrelRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2116.NonBarrelRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to NonBarrelRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_roller_bearing(self) -> '_2117.RollerBearing':
        """RollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2117.RollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to RollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_rolling_bearing(self) -> '_2120.RollingBearing':
        """RollingBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2120.RollingBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to RollingBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_self_aligning_ball_bearing(self) -> '_2121.SelfAligningBallBearing':
        """SelfAligningBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2121.SelfAligningBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to SelfAligningBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_spherical_roller_bearing(self) -> '_2124.SphericalRollerBearing':
        """SphericalRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2124.SphericalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to SphericalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_spherical_roller_thrust_bearing(self) -> '_2125.SphericalRollerThrustBearing':
        """SphericalRollerThrustBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2125.SphericalRollerThrustBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to SphericalRollerThrustBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_taper_roller_bearing(self) -> '_2126.TaperRollerBearing':
        """TaperRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2126.TaperRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to TaperRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_three_point_contact_ball_bearing(self) -> '_2127.ThreePointContactBallBearing':
        """ThreePointContactBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2127.ThreePointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to ThreePointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_thrust_ball_bearing(self) -> '_2128.ThrustBallBearing':
        """ThrustBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2128.ThrustBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to ThrustBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_toroidal_roller_bearing(self) -> '_2129.ToroidalRollerBearing':
        """ToroidalRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2129.ToroidalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to ToroidalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_pad_fluid_film_bearing(self) -> '_2142.PadFluidFilmBearing':
        """PadFluidFilmBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2142.PadFluidFilmBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to PadFluidFilmBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_plain_grease_filled_journal_bearing(self) -> '_2144.PlainGreaseFilledJournalBearing':
        """PlainGreaseFilledJournalBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2144.PlainGreaseFilledJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to PlainGreaseFilledJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_plain_journal_bearing(self) -> '_2146.PlainJournalBearing':
        """PlainJournalBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2146.PlainJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to PlainJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_plain_oil_fed_journal_bearing(self) -> '_2148.PlainOilFedJournalBearing':
        """PlainOilFedJournalBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2148.PlainOilFedJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to PlainOilFedJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_tilting_pad_journal_bearing(self) -> '_2149.TiltingPadJournalBearing':
        """TiltingPadJournalBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2149.TiltingPadJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to TiltingPadJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_tilting_pad_thrust_bearing(self) -> '_2150.TiltingPadThrustBearing':
        """TiltingPadThrustBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2150.TiltingPadThrustBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to TiltingPadThrustBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_concept_axial_clearance_bearing(self) -> '_2152.ConceptAxialClearanceBearing':
        """ConceptAxialClearanceBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2152.ConceptAxialClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to ConceptAxialClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_concept_clearance_bearing(self) -> '_2153.ConceptClearanceBearing':
        """ConceptClearanceBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2153.ConceptClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to ConceptClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_of_type_concept_radial_clearance_bearing(self) -> '_2154.ConceptRadialClearanceBearing':
        """ConceptRadialClearanceBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        if _2154.ConceptRadialClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing to ConceptRadialClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def force_on_inner_race(self) -> '_1528.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'ForceOnInnerRace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceOnInnerRace

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_results(self) -> 'List[_2024.RingForceAndDisplacement]':
        """List[RingForceAndDisplacement]: 'RingResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
