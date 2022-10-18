"""_1908.py

LoadedBearingDutyCycle
"""


from typing import List

from mastapy._internal import constructor, conversion
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
from mastapy.utility.property import _1801
from mastapy.bearings import _1836
from mastapy.bearings.bearing_results import _1909
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_LOADED_BEARING_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedBearingDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBearingDutyCycle',)


class LoadedBearingDutyCycle(_0.APIBase):
    """LoadedBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_BEARING_DUTY_CYCLE

    def __init__(self, instance_to_wrap: 'LoadedBearingDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duration(self) -> 'float':
        """float: 'Duration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @property
    def duty_cycle_name(self) -> 'str':
        """str: 'DutyCycleName' is the original name of this property."""

        temp = self.wrapped.DutyCycleName

        if temp is None:
            return ''

        return temp

    @duty_cycle_name.setter
    def duty_cycle_name(self, value: 'str'):
        self.wrapped.DutyCycleName = str(value) if value else ''

    @property
    def bearing_design(self) -> '_2085.BearingDesign':
        """BearingDesign: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2085.BearingDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to BearingDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_detailed_bearing(self) -> '_2086.DetailedBearing':
        """DetailedBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2086.DetailedBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to DetailedBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_dummy_rolling_bearing(self) -> '_2087.DummyRollingBearing':
        """DummyRollingBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2087.DummyRollingBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to DummyRollingBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_linear_bearing(self) -> '_2088.LinearBearing':
        """LinearBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2088.LinearBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to LinearBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_non_linear_bearing(self) -> '_2089.NonLinearBearing':
        """NonLinearBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2089.NonLinearBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to NonLinearBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_angular_contact_ball_bearing(self) -> '_2090.AngularContactBallBearing':
        """AngularContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2090.AngularContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AngularContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_angular_contact_thrust_ball_bearing(self) -> '_2091.AngularContactThrustBallBearing':
        """AngularContactThrustBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2091.AngularContactThrustBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AngularContactThrustBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_asymmetric_spherical_roller_bearing(self) -> '_2092.AsymmetricSphericalRollerBearing':
        """AsymmetricSphericalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2092.AsymmetricSphericalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AsymmetricSphericalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_axial_thrust_cylindrical_roller_bearing(self) -> '_2093.AxialThrustCylindricalRollerBearing':
        """AxialThrustCylindricalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2093.AxialThrustCylindricalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AxialThrustCylindricalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_axial_thrust_needle_roller_bearing(self) -> '_2094.AxialThrustNeedleRollerBearing':
        """AxialThrustNeedleRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2094.AxialThrustNeedleRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AxialThrustNeedleRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_ball_bearing(self) -> '_2095.BallBearing':
        """BallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2095.BallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to BallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_barrel_roller_bearing(self) -> '_2097.BarrelRollerBearing':
        """BarrelRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2097.BarrelRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to BarrelRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_crossed_roller_bearing(self) -> '_2103.CrossedRollerBearing':
        """CrossedRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2103.CrossedRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to CrossedRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_cylindrical_roller_bearing(self) -> '_2104.CylindricalRollerBearing':
        """CylindricalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2104.CylindricalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to CylindricalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_deep_groove_ball_bearing(self) -> '_2105.DeepGrooveBallBearing':
        """DeepGrooveBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2105.DeepGrooveBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to DeepGrooveBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_four_point_contact_ball_bearing(self) -> '_2109.FourPointContactBallBearing':
        """FourPointContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2109.FourPointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to FourPointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_multi_point_contact_ball_bearing(self) -> '_2114.MultiPointContactBallBearing':
        """MultiPointContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2114.MultiPointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to MultiPointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_needle_roller_bearing(self) -> '_2115.NeedleRollerBearing':
        """NeedleRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2115.NeedleRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to NeedleRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_non_barrel_roller_bearing(self) -> '_2116.NonBarrelRollerBearing':
        """NonBarrelRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2116.NonBarrelRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to NonBarrelRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_roller_bearing(self) -> '_2117.RollerBearing':
        """RollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2117.RollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to RollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_rolling_bearing(self) -> '_2120.RollingBearing':
        """RollingBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2120.RollingBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to RollingBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_self_aligning_ball_bearing(self) -> '_2121.SelfAligningBallBearing':
        """SelfAligningBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2121.SelfAligningBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to SelfAligningBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_spherical_roller_bearing(self) -> '_2124.SphericalRollerBearing':
        """SphericalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2124.SphericalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to SphericalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_spherical_roller_thrust_bearing(self) -> '_2125.SphericalRollerThrustBearing':
        """SphericalRollerThrustBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2125.SphericalRollerThrustBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to SphericalRollerThrustBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_taper_roller_bearing(self) -> '_2126.TaperRollerBearing':
        """TaperRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2126.TaperRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to TaperRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_three_point_contact_ball_bearing(self) -> '_2127.ThreePointContactBallBearing':
        """ThreePointContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2127.ThreePointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ThreePointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_thrust_ball_bearing(self) -> '_2128.ThrustBallBearing':
        """ThrustBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2128.ThrustBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ThrustBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_toroidal_roller_bearing(self) -> '_2129.ToroidalRollerBearing':
        """ToroidalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2129.ToroidalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ToroidalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_pad_fluid_film_bearing(self) -> '_2142.PadFluidFilmBearing':
        """PadFluidFilmBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2142.PadFluidFilmBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PadFluidFilmBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_plain_grease_filled_journal_bearing(self) -> '_2144.PlainGreaseFilledJournalBearing':
        """PlainGreaseFilledJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2144.PlainGreaseFilledJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PlainGreaseFilledJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_plain_journal_bearing(self) -> '_2146.PlainJournalBearing':
        """PlainJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2146.PlainJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PlainJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_plain_oil_fed_journal_bearing(self) -> '_2148.PlainOilFedJournalBearing':
        """PlainOilFedJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2148.PlainOilFedJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PlainOilFedJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_tilting_pad_journal_bearing(self) -> '_2149.TiltingPadJournalBearing':
        """TiltingPadJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2149.TiltingPadJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to TiltingPadJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_tilting_pad_thrust_bearing(self) -> '_2150.TiltingPadThrustBearing':
        """TiltingPadThrustBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2150.TiltingPadThrustBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to TiltingPadThrustBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_concept_axial_clearance_bearing(self) -> '_2152.ConceptAxialClearanceBearing':
        """ConceptAxialClearanceBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2152.ConceptAxialClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ConceptAxialClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_concept_clearance_bearing(self) -> '_2153.ConceptClearanceBearing':
        """ConceptClearanceBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2153.ConceptClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ConceptClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_concept_radial_clearance_bearing(self) -> '_2154.ConceptRadialClearanceBearing':
        """ConceptRadialClearanceBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign

        if temp is None:
            return None

        if _2154.ConceptRadialClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ConceptRadialClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def radial_load_summary(self) -> '_1801.DutyCyclePropertySummaryForce[_1836.BearingLoadCaseResultsLightweight]':
        """DutyCyclePropertySummaryForce[BearingLoadCaseResultsLightweight]: 'RadialLoadSummary' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialLoadSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1836.BearingLoadCaseResultsLightweight](temp) if temp is not None else None

    @property
    def z_thrust_reaction_summary(self) -> '_1801.DutyCyclePropertySummaryForce[_1836.BearingLoadCaseResultsLightweight]':
        """DutyCyclePropertySummaryForce[BearingLoadCaseResultsLightweight]: 'ZThrustReactionSummary' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZThrustReactionSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1836.BearingLoadCaseResultsLightweight](temp) if temp is not None else None

    @property
    def bearing_load_case_results(self) -> 'List[_1909.LoadedBearingResults]':
        """List[LoadedBearingResults]: 'BearingLoadCaseResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingLoadCaseResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
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
