"""_3328.py

AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
"""


from typing import List

from mastapy.system_model.part_model import _2386, _2426
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3198
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3329, _3331, _3334, _3341,
    _3340, _3362, _3342, _3347,
    _3352, _3364, _3366, _3370,
    _3377, _3376, _3378, _3385,
    _3392, _3395, _3396, _3397,
    _3399, _3401, _3406, _3407,
    _3408, _3410, _3412, _3417,
    _3416, _3422, _3423, _3428,
    _3431, _3434, _3438, _3442,
    _3446, _3449, _3321
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'AssemblyCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundSteadyStateSynchronousResponseOnAShaft',)


class AssemblyCompoundSteadyStateSynchronousResponseOnAShaft(_3321.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft):
    """AssemblyCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    def __init__(self, instance_to_wrap: 'AssemblyCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2386.Assembly':
        """Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2386.Assembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Assembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2386.Assembly':
        """Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2386.Assembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to Assembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3198.AssemblySteadyStateSynchronousResponseOnAShaft]':
        """List[AssemblySteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bearings(self) -> 'List[_3329.BearingCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[BearingCompoundSteadyStateSynchronousResponseOnAShaft]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def belt_drives(self) -> 'List[_3331.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BeltDrives

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_3334.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolted_joints(self) -> 'List[_3341.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltedJoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolts(self) -> 'List[_3340.BoltCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[BoltCompoundSteadyStateSynchronousResponseOnAShaft]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bolts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cv_ts(self) -> 'List[_3362.CVTCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[CVTCompoundSteadyStateSynchronousResponseOnAShaft]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CVTs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def clutches(self) -> 'List[_3342.ClutchCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[ClutchCompoundSteadyStateSynchronousResponseOnAShaft]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Clutches

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_couplings(self) -> 'List[_3347.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gear_sets(self) -> 'List[_3352.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_3364.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_discs(self) -> 'List[_3366.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_3370.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def fe_parts(self) -> 'List[_3377.FEPartCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[FEPartCompoundSteadyStateSynchronousResponseOnAShaft]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gear_sets(self) -> 'List[_3376.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_3378.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlexiblePinAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_3385.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_3392.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_3395.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def mass_discs(self) -> 'List[_3396.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[MassDiscCompoundSteadyStateSynchronousResponseOnAShaft]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def measurement_components(self) -> 'List[_3397.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeasurementComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def oil_seals(self) -> 'List[_3399.OilSealCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[OilSealCompoundSteadyStateSynchronousResponseOnAShaft]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilSeals

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_3401.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartToPartShearCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planet_carriers(self) -> 'List[_3406.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetCarriers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def point_loads(self) -> 'List[_3407.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[PointLoadCompoundSteadyStateSynchronousResponseOnAShaft]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_loads(self) -> 'List[_3408.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def ring_pins(self) -> 'List[_3410.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[RingPinsCompoundSteadyStateSynchronousResponseOnAShaft]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPins

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_3412.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingRingAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_3417.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftHubConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shafts(self) -> 'List[_3416.ShaftCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[ShaftCompoundSteadyStateSynchronousResponseOnAShaft]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shafts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_3422.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spring_dampers(self) -> 'List[_3423.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpringDampers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_3428.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_3431.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def synchronisers(self) -> 'List[_3434.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Synchronisers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def torque_converters(self) -> 'List[_3438.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueConverters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def unbalanced_masses(self) -> 'List[_3442.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UnbalancedMasses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gear_sets(self) -> 'List[_3446.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_3449.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3198.AssemblySteadyStateSynchronousResponseOnAShaft]':
        """List[AssemblySteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
