"""_2644.py

BearingSystemDeflection
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_2d import Vector2D
from mastapy._math.vector_3d import Vector3D
from mastapy.utility_gui.charts import (
    _1827, _1813, _1820, _1822
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model import _2392, _2393
from mastapy.bearings.bearing_results import (
    _1909, _1911, _1912, _1913,
    _1914, _1915, _1917, _1902
)
from mastapy.bearings.bearing_results.rolling import (
    _1939, _1942, _1945, _1950,
    _1953, _1958, _1961, _1965,
    _1968, _1973, _1977, _1980,
    _1985, _1989, _1992, _1996,
    _1999, _2004, _2007, _2010,
    _2013
)
from mastapy.bearings.bearing_results.fluid_film import (
    _2074, _2075, _2076, _2077,
    _2079, _2082, _2083
)
from mastapy.system_model.analyses_and_results.static_loads import _6746
from mastapy.system_model.analyses_and_results.power_flows import _3984
from mastapy.math_utility.measured_vectors import _1525
from mastapy.system_model.analyses_and_results.system_deflections import _2674
from mastapy._internal.python_net import python_net_import

_BEARING_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BearingSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingSystemDeflection',)


class BearingSystemDeflection(_2674.ConnectorSystemDeflection):
    """BearingSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEARING_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'BearingSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_stiffness(self) -> 'float':
        """float: 'AxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def component_angular_displacements(self) -> 'List[Vector2D]':
        """List[Vector2D]: 'ComponentAngularDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAngularDisplacements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_axial_displacements(self) -> 'List[float]':
        """List[float]: 'ComponentAxialDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAxialDisplacements

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def component_radial_displacements(self) -> 'List[Vector2D]':
        """List[Vector2D]: 'ComponentRadialDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentRadialDisplacements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def element_axial_displacements(self) -> 'List[float]':
        """List[float]: 'ElementAxialDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementAxialDisplacements

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def element_radial_displacements(self) -> 'List[float]':
        """List[float]: 'ElementRadialDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementRadialDisplacements

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def element_tilts(self) -> 'List[float]':
        """List[float]: 'ElementTilts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementTilts

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elements_in_contact(self) -> 'int':
        """int: 'ElementsInContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementsInContact

        if temp is None:
            return 0

        return temp

    @property
    def inner_left_mounting_axial_stiffness(self) -> 'float':
        """float: 'InnerLeftMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerLeftMountingAxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_left_mounting_displacement(self) -> 'Vector3D':
        """Vector3D: 'InnerLeftMountingDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerLeftMountingDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def inner_left_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'InnerLeftMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerLeftMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_left_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'InnerLeftMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerLeftMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def inner_radial_mounting_linear_displacement(self) -> 'Vector2D':
        """Vector2D: 'InnerRadialMountingLinearDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRadialMountingLinearDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def inner_radial_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'InnerRadialMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRadialMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_radial_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'InnerRadialMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRadialMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def inner_right_mounting_axial_stiffness(self) -> 'float':
        """float: 'InnerRightMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRightMountingAxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_right_mounting_displacement(self) -> 'Vector3D':
        """Vector3D: 'InnerRightMountingDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRightMountingDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def inner_right_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'InnerRightMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRightMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_right_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'InnerRightMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRightMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def internal_force(self) -> 'Vector3D':
        """Vector3D: 'InternalForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InternalForce

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def internal_moment(self) -> 'Vector3D':
        """Vector3D: 'InternalMoment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InternalMoment

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def is_loaded(self) -> 'bool':
        """bool: 'IsLoaded' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

    @property
    def maximum_radial_stiffness(self) -> 'float':
        """float: 'MaximumRadialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumRadialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_tilt_stiffness(self) -> 'float':
        """float: 'MaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_left_mounting_axial_stiffness(self) -> 'float':
        """float: 'OuterLeftMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterLeftMountingAxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_left_mounting_displacement(self) -> 'Vector3D':
        """Vector3D: 'OuterLeftMountingDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterLeftMountingDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def outer_left_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'OuterLeftMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterLeftMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_left_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'OuterLeftMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterLeftMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def outer_radial_mounting_linear_displacement(self) -> 'Vector2D':
        """Vector2D: 'OuterRadialMountingLinearDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRadialMountingLinearDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def outer_radial_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'OuterRadialMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRadialMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_radial_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'OuterRadialMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRadialMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def outer_right_mounting_axial_stiffness(self) -> 'float':
        """float: 'OuterRightMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRightMountingAxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_right_mounting_displacement(self) -> 'Vector3D':
        """Vector3D: 'OuterRightMountingDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRightMountingDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def outer_right_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'OuterRightMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRightMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_right_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'OuterRightMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRightMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def percentage_preload_spring_compression(self) -> 'float':
        """float: 'PercentagePreloadSpringCompression' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PercentagePreloadSpringCompression

        if temp is None:
            return 0.0

        return temp

    @property
    def preload_spring_compression(self) -> 'float':
        """float: 'PreloadSpringCompression' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PreloadSpringCompression

        if temp is None:
            return 0.0

        return temp

    @property
    def spring_preload_chart(self) -> '_1827.TwoDChartDefinition':
        """TwoDChartDefinition: 'SpringPreloadChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpringPreloadChart

        if temp is None:
            return None

        if _1827.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spring_preload_chart to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design(self) -> '_2392.Bearing':
        """Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_1909.LoadedBearingResults':
        """LoadedBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1909.LoadedBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_concept_axial_clearance_bearing_results(self) -> '_1911.LoadedConceptAxialClearanceBearingResults':
        """LoadedConceptAxialClearanceBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1911.LoadedConceptAxialClearanceBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedConceptAxialClearanceBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_concept_clearance_bearing_results(self) -> '_1912.LoadedConceptClearanceBearingResults':
        """LoadedConceptClearanceBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1912.LoadedConceptClearanceBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedConceptClearanceBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_concept_radial_clearance_bearing_results(self) -> '_1913.LoadedConceptRadialClearanceBearingResults':
        """LoadedConceptRadialClearanceBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1913.LoadedConceptRadialClearanceBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedConceptRadialClearanceBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_detailed_bearing_results(self) -> '_1914.LoadedDetailedBearingResults':
        """LoadedDetailedBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1914.LoadedDetailedBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedDetailedBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_linear_bearing_results(self) -> '_1915.LoadedLinearBearingResults':
        """LoadedLinearBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1915.LoadedLinearBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedLinearBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_non_linear_bearing_results(self) -> '_1917.LoadedNonLinearBearingResults':
        """LoadedNonLinearBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1917.LoadedNonLinearBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedNonLinearBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_angular_contact_ball_bearing_results(self) -> '_1939.LoadedAngularContactBallBearingResults':
        """LoadedAngularContactBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1939.LoadedAngularContactBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedAngularContactBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_angular_contact_thrust_ball_bearing_results(self) -> '_1942.LoadedAngularContactThrustBallBearingResults':
        """LoadedAngularContactThrustBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1942.LoadedAngularContactThrustBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedAngularContactThrustBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_asymmetric_spherical_roller_bearing_results(self) -> '_1945.LoadedAsymmetricSphericalRollerBearingResults':
        """LoadedAsymmetricSphericalRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1945.LoadedAsymmetricSphericalRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedAsymmetricSphericalRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_axial_thrust_cylindrical_roller_bearing_results(self) -> '_1950.LoadedAxialThrustCylindricalRollerBearingResults':
        """LoadedAxialThrustCylindricalRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1950.LoadedAxialThrustCylindricalRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedAxialThrustCylindricalRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_axial_thrust_needle_roller_bearing_results(self) -> '_1953.LoadedAxialThrustNeedleRollerBearingResults':
        """LoadedAxialThrustNeedleRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1953.LoadedAxialThrustNeedleRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedAxialThrustNeedleRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_ball_bearing_results(self) -> '_1958.LoadedBallBearingResults':
        """LoadedBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1958.LoadedBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_crossed_roller_bearing_results(self) -> '_1961.LoadedCrossedRollerBearingResults':
        """LoadedCrossedRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1961.LoadedCrossedRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedCrossedRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_cylindrical_roller_bearing_results(self) -> '_1965.LoadedCylindricalRollerBearingResults':
        """LoadedCylindricalRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1965.LoadedCylindricalRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedCylindricalRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_deep_groove_ball_bearing_results(self) -> '_1968.LoadedDeepGrooveBallBearingResults':
        """LoadedDeepGrooveBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1968.LoadedDeepGrooveBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedDeepGrooveBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_four_point_contact_ball_bearing_results(self) -> '_1973.LoadedFourPointContactBallBearingResults':
        """LoadedFourPointContactBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1973.LoadedFourPointContactBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedFourPointContactBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_needle_roller_bearing_results(self) -> '_1977.LoadedNeedleRollerBearingResults':
        """LoadedNeedleRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1977.LoadedNeedleRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedNeedleRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_non_barrel_roller_bearing_results(self) -> '_1980.LoadedNonBarrelRollerBearingResults':
        """LoadedNonBarrelRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1980.LoadedNonBarrelRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedNonBarrelRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_roller_bearing_results(self) -> '_1985.LoadedRollerBearingResults':
        """LoadedRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1985.LoadedRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_rolling_bearing_results(self) -> '_1989.LoadedRollingBearingResults':
        """LoadedRollingBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1989.LoadedRollingBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedRollingBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_self_aligning_ball_bearing_results(self) -> '_1992.LoadedSelfAligningBallBearingResults':
        """LoadedSelfAligningBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1992.LoadedSelfAligningBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedSelfAligningBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_spherical_roller_radial_bearing_results(self) -> '_1996.LoadedSphericalRollerRadialBearingResults':
        """LoadedSphericalRollerRadialBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1996.LoadedSphericalRollerRadialBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedSphericalRollerRadialBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_spherical_roller_thrust_bearing_results(self) -> '_1999.LoadedSphericalRollerThrustBearingResults':
        """LoadedSphericalRollerThrustBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _1999.LoadedSphericalRollerThrustBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedSphericalRollerThrustBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_taper_roller_bearing_results(self) -> '_2004.LoadedTaperRollerBearingResults':
        """LoadedTaperRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _2004.LoadedTaperRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedTaperRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_three_point_contact_ball_bearing_results(self) -> '_2007.LoadedThreePointContactBallBearingResults':
        """LoadedThreePointContactBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _2007.LoadedThreePointContactBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedThreePointContactBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_thrust_ball_bearing_results(self) -> '_2010.LoadedThrustBallBearingResults':
        """LoadedThrustBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _2010.LoadedThrustBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedThrustBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_toroidal_roller_bearing_results(self) -> '_2013.LoadedToroidalRollerBearingResults':
        """LoadedToroidalRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _2013.LoadedToroidalRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedToroidalRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_fluid_film_bearing_results(self) -> '_2074.LoadedFluidFilmBearingResults':
        """LoadedFluidFilmBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _2074.LoadedFluidFilmBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedFluidFilmBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_grease_filled_journal_bearing_results(self) -> '_2075.LoadedGreaseFilledJournalBearingResults':
        """LoadedGreaseFilledJournalBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _2075.LoadedGreaseFilledJournalBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedGreaseFilledJournalBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_pad_fluid_film_bearing_results(self) -> '_2076.LoadedPadFluidFilmBearingResults':
        """LoadedPadFluidFilmBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _2076.LoadedPadFluidFilmBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedPadFluidFilmBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_plain_journal_bearing_results(self) -> '_2077.LoadedPlainJournalBearingResults':
        """LoadedPlainJournalBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _2077.LoadedPlainJournalBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedPlainJournalBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_plain_oil_fed_journal_bearing(self) -> '_2079.LoadedPlainOilFedJournalBearing':
        """LoadedPlainOilFedJournalBearing: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _2079.LoadedPlainOilFedJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedPlainOilFedJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_tilting_pad_journal_bearing_results(self) -> '_2082.LoadedTiltingPadJournalBearingResults':
        """LoadedTiltingPadJournalBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _2082.LoadedTiltingPadJournalBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedTiltingPadJournalBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_tilting_pad_thrust_bearing_results(self) -> '_2083.LoadedTiltingPadThrustBearingResults':
        """LoadedTiltingPadThrustBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        if _2083.LoadedTiltingPadThrustBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedTiltingPadThrustBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6746.BearingLoadCase':
        """BearingLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_left_mounting_stiffness(self) -> '_1902.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'InnerLeftMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerLeftMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_radial_mounting_stiffness(self) -> '_1902.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'InnerRadialMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRadialMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_right_mounting_stiffness(self) -> '_1902.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'InnerRightMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRightMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_left_mounting_stiffness(self) -> '_1902.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'OuterLeftMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterLeftMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_radial_mounting_stiffness(self) -> '_1902.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'OuterRadialMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRadialMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_right_mounting_stiffness(self) -> '_1902.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'OuterRightMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRightMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_3984.BearingPowerFlow':
        """BearingPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def preload_spring_stiffness(self) -> '_1902.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'PreloadSpringStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PreloadSpringStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stiffness_between_rings(self) -> '_1902.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'StiffnessBetweenRings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessBetweenRings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stiffness_matrix(self) -> '_1902.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'StiffnessMatrix' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessMatrix

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def forces_at_zero_displacement_for_inner_and_outer_nodes(self) -> 'List[_1525.ForceResults]':
        """List[ForceResults]: 'ForcesAtZeroDisplacementForInnerAndOuterNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForcesAtZeroDisplacementForInnerAndOuterNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[BearingSystemDeflection]':
        """List[BearingSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def race_mounting_options_for_analysis(self) -> 'List[_2393.BearingRaceMountingOptions]':
        """List[BearingRaceMountingOptions]: 'RaceMountingOptionsForAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RaceMountingOptionsForAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def stiffness_between_each_ring(self) -> 'List[_1902.BearingStiffnessMatrixReporter]':
        """List[BearingStiffnessMatrixReporter]: 'StiffnessBetweenEachRing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessBetweenEachRing

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
