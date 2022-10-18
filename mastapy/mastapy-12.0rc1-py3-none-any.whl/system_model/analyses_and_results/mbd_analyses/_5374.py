"""_5374.py

GearMeshMultibodyDynamicsAnalysis
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.nodal_analysis import _69
from mastapy.system_model.connections_and_sockets.gears import (
    _2265, _2251, _2253, _2255,
    _2257, _2259, _2261, _2263,
    _2267, _2270, _2271, _2272,
    _2275, _2277, _2279, _2281,
    _2283
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.mbd_analyses import _5386
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'GearMeshMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshMultibodyDynamicsAnalysis',)


class GearMeshMultibodyDynamicsAnalysis(_5386.InterMountableComponentConnectionMultibodyDynamicsAnalysis):
    """GearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS

    def __init__(self, instance_to_wrap: 'GearMeshMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_sliding_velocity_left_flank(self) -> 'float':
        """float: 'AverageSlidingVelocityLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageSlidingVelocityLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def average_sliding_velocity_right_flank(self) -> 'float':
        """float: 'AverageSlidingVelocityRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageSlidingVelocityRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def coefficient_of_friction_left_flank(self) -> 'float':
        """float: 'CoefficientOfFrictionLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoefficientOfFrictionLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def coefficient_of_friction_right_flank(self) -> 'float':
        """float: 'CoefficientOfFrictionRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoefficientOfFrictionRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_status(self) -> '_69.GearMeshContactStatus':
        """GearMeshContactStatus: 'ContactStatus' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactStatus

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_69.GearMeshContactStatus)(value) if value is not None else None

    @property
    def equivalent_misalignment_left_flank(self) -> 'float':
        """float: 'EquivalentMisalignmentLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EquivalentMisalignmentLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def equivalent_misalignment_right_flank(self) -> 'float':
        """float: 'EquivalentMisalignmentRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EquivalentMisalignmentRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def force_normal_to_left_flank(self) -> 'float':
        """float: 'ForceNormalToLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceNormalToLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def force_normal_to_right_flank(self) -> 'float':
        """float: 'ForceNormalToRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceNormalToRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def impact_power_left_flank(self) -> 'float':
        """float: 'ImpactPowerLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ImpactPowerLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def impact_power_right_flank(self) -> 'float':
        """float: 'ImpactPowerRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ImpactPowerRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def impact_power_total(self) -> 'float':
        """float: 'ImpactPowerTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ImpactPowerTotal

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_power_loss(self) -> 'float':
        """float: 'MeshPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_due_to_tilt_left_flank(self) -> 'float':
        """float: 'MisalignmentDueToTiltLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentDueToTiltLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_due_to_tilt_right_flank(self) -> 'float':
        """float: 'MisalignmentDueToTiltRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentDueToTiltRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stiffness(self) -> 'float':
        """float: 'NormalStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stiffness_left_flank(self) -> 'float':
        """float: 'NormalStiffnessLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStiffnessLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stiffness_right_flank(self) -> 'float':
        """float: 'NormalStiffnessRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStiffnessRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_line_velocity_left_flank(self) -> 'float':
        """float: 'PitchLineVelocityLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchLineVelocityLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_line_velocity_right_flank(self) -> 'float':
        """float: 'PitchLineVelocityRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchLineVelocityRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation(self) -> 'float':
        """float: 'Separation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Separation

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_normal_to_left_flank(self) -> 'float':
        """float: 'SeparationNormalToLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SeparationNormalToLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_normal_to_right_flank(self) -> 'float':
        """float: 'SeparationNormalToRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SeparationNormalToRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_transverse_to_left_flank(self) -> 'float':
        """float: 'SeparationTransverseToLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SeparationTransverseToLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_transverse_to_right_flank(self) -> 'float':
        """float: 'SeparationTransverseToRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SeparationTransverseToRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def strain_energy_left_flank(self) -> 'float':
        """float: 'StrainEnergyLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StrainEnergyLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def strain_energy_right_flank(self) -> 'float':
        """float: 'StrainEnergyRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StrainEnergyRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def strain_energy_total(self) -> 'float':
        """float: 'StrainEnergyTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StrainEnergyTotal

        if temp is None:
            return 0.0

        return temp

    @property
    def tilt_stiffness(self) -> 'float':
        """float: 'TiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_frequency(self) -> 'float':
        """float: 'ToothPassingFrequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothPassingFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_speed_gear_a(self) -> 'float':
        """float: 'ToothPassingSpeedGearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothPassingSpeedGearA

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_speed_gear_b(self) -> 'float':
        """float: 'ToothPassingSpeedGearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothPassingSpeedGearB

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_stiffness_left_flank(self) -> 'float':
        """float: 'TransverseStiffnessLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseStiffnessLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_stiffness_right_flank(self) -> 'float':
        """float: 'TransverseStiffnessRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseStiffnessRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self) -> '_2265.GearMesh':
        """GearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2265.GearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to GearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_agma_gleason_conical_gear_mesh(self) -> '_2251.AGMAGleasonConicalGearMesh':
        """AGMAGleasonConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2251.AGMAGleasonConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to AGMAGleasonConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_bevel_differential_gear_mesh(self) -> '_2253.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2253.BevelDifferentialGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to BevelDifferentialGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_bevel_gear_mesh(self) -> '_2255.BevelGearMesh':
        """BevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2255.BevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to BevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_concept_gear_mesh(self) -> '_2257.ConceptGearMesh':
        """ConceptGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2257.ConceptGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ConceptGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_conical_gear_mesh(self) -> '_2259.ConicalGearMesh':
        """ConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2259.ConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_cylindrical_gear_mesh(self) -> '_2261.CylindricalGearMesh':
        """CylindricalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2261.CylindricalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CylindricalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_face_gear_mesh(self) -> '_2263.FaceGearMesh':
        """FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2263.FaceGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to FaceGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_hypoid_gear_mesh(self) -> '_2267.HypoidGearMesh':
        """HypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2267.HypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to HypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_2270.KlingelnbergCycloPalloidConicalGearMesh':
        """KlingelnbergCycloPalloidConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2270.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_2271.KlingelnbergCycloPalloidHypoidGearMesh':
        """KlingelnbergCycloPalloidHypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2271.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_2272.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        """KlingelnbergCycloPalloidSpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2272.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_spiral_bevel_gear_mesh(self) -> '_2275.SpiralBevelGearMesh':
        """SpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2275.SpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to SpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_straight_bevel_diff_gear_mesh(self) -> '_2277.StraightBevelDiffGearMesh':
        """StraightBevelDiffGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2277.StraightBevelDiffGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to StraightBevelDiffGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_straight_bevel_gear_mesh(self) -> '_2279.StraightBevelGearMesh':
        """StraightBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2279.StraightBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to StraightBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_worm_gear_mesh(self) -> '_2281.WormGearMesh':
        """WormGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2281.WormGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to WormGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_zerol_bevel_gear_mesh(self) -> '_2283.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2283.ZerolBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ZerolBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
