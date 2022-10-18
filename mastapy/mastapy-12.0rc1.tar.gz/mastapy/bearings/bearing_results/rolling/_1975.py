"""_1975.py

LoadedMultiPointContactBallBearingElement
"""


from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _1956
from mastapy._internal.python_net import python_net_import

_LOADED_MULTI_POINT_CONTACT_BALL_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedMultiPointContactBallBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedMultiPointContactBallBearingElement',)


class LoadedMultiPointContactBallBearingElement(_1956.LoadedBallBearingElement):
    """LoadedMultiPointContactBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_MULTI_POINT_CONTACT_BALL_BEARING_ELEMENT

    def __init__(self, instance_to_wrap: 'LoadedMultiPointContactBallBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def approximate_percentage_of_friction_used_inner_left(self) -> 'float':
        """float: 'ApproximatePercentageOfFrictionUsedInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApproximatePercentageOfFrictionUsedInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def approximate_percentage_of_friction_used_inner_right(self) -> 'float':
        """float: 'ApproximatePercentageOfFrictionUsedInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApproximatePercentageOfFrictionUsedInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_angle_inner_left(self) -> 'float':
        """float: 'ContactAngleInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactAngleInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_angle_inner_right(self) -> 'float':
        """float: 'ContactAngleInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactAngleInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def curvature_moment_inner_left(self) -> 'float':
        """float: 'CurvatureMomentInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurvatureMomentInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def curvature_moment_inner_right(self) -> 'float':
        """float: 'CurvatureMomentInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurvatureMomentInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_major_dimension_inner_left(self) -> 'float':
        """float: 'HertzianSemiMajorDimensionInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMajorDimensionInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_major_dimension_inner_right(self) -> 'float':
        """float: 'HertzianSemiMajorDimensionInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMajorDimensionInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_inner_left(self) -> 'float':
        """float: 'HertzianSemiMinorDimensionInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMinorDimensionInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_inner_right(self) -> 'float':
        """float: 'HertzianSemiMinorDimensionInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMinorDimensionInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_rolling_resistance_force_inner_left(self) -> 'float':
        """float: 'HydrodynamicRollingResistanceForceInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HydrodynamicRollingResistanceForceInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_rolling_resistance_force_inner_right(self) -> 'float':
        """float: 'HydrodynamicRollingResistanceForceInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HydrodynamicRollingResistanceForceInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_inner_left(self) -> 'float':
        """float: 'MaximumNormalStressInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStressInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_inner_right(self) -> 'float':
        """float: 'MaximumNormalStressInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStressInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_inner(self) -> 'float':
        """float: 'MaximumNormalStressInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_inner_left(self) -> 'float':
        """float: 'MaximumShearStressInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_inner_right(self) -> 'float':
        """float: 'MaximumShearStressInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_smearing_intensity_inner(self) -> 'float':
        """float: 'MaximumSmearingIntensityInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumSmearingIntensityInner

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_inner_left(self) -> 'float':
        """float: 'MinimumLubricatingFilmThicknessInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricatingFilmThicknessInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_inner_right(self) -> 'float':
        """float: 'MinimumLubricatingFilmThicknessInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricatingFilmThicknessInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_inner(self) -> 'float':
        """float: 'MinimumLubricatingFilmThicknessInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricatingFilmThicknessInner

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_load_inner_left(self) -> 'float':
        """float: 'NormalLoadInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalLoadInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_load_inner_right(self) -> 'float':
        """float: 'NormalLoadInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalLoadInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def pivoting_moment_inner_left(self) -> 'float':
        """float: 'PivotingMomentInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PivotingMomentInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def pivoting_moment_inner_right(self) -> 'float':
        """float: 'PivotingMomentInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PivotingMomentInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_inner_left(self) -> 'float':
        """float: 'PowerLossInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_inner_right(self) -> 'float':
        """float: 'PowerLossInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_elastic_rolling_resistance_inner_left(self) -> 'float':
        """float: 'PowerLossDueToElasticRollingResistanceInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossDueToElasticRollingResistanceInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_elastic_rolling_resistance_inner_right(self) -> 'float':
        """float: 'PowerLossDueToElasticRollingResistanceInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossDueToElasticRollingResistanceInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_hydrodynamic_rolling_resistance_inner_left(self) -> 'float':
        """float: 'PowerLossDueToHydrodynamicRollingResistanceInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossDueToHydrodynamicRollingResistanceInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_hydrodynamic_rolling_resistance_inner_right(self) -> 'float':
        """float: 'PowerLossDueToHydrodynamicRollingResistanceInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossDueToHydrodynamicRollingResistanceInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_major_axis_inner_left(self) -> 'float':
        """float: 'PowerLossParallelToMajorAxisInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossParallelToMajorAxisInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_major_axis_inner_right(self) -> 'float':
        """float: 'PowerLossParallelToMajorAxisInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossParallelToMajorAxisInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_minor_axis_inner_left(self) -> 'float':
        """float: 'PowerLossParallelToMinorAxisInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossParallelToMinorAxisInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_minor_axis_inner_right(self) -> 'float':
        """float: 'PowerLossParallelToMinorAxisInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossParallelToMinorAxisInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_inner_left(self) -> 'float':
        """float: 'SlidingForceParallelToTheMajorAxisInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMajorAxisInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_inner_right(self) -> 'float':
        """float: 'SlidingForceParallelToTheMajorAxisInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMajorAxisInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_inner_left(self) -> 'float':
        """float: 'SlidingForceParallelToTheMinorAxisInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMinorAxisInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_inner_right(self) -> 'float':
        """float: 'SlidingForceParallelToTheMinorAxisInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMinorAxisInnerRight

        if temp is None:
            return 0.0

        return temp
