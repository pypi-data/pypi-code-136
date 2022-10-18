"""_2643.py

AssemblySystemDeflection
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis import _50
from mastapy.system_model.part_model import _2386, _2426
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6745, _6874
from mastapy.system_model.analyses_and_results.power_flows import _3983, _4073
from mastapy.gears.analysis import _1217
from mastapy.shafts import _40
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2644, _2646, _2648, _2655,
    _2656, _2680, _2659, _2661,
    _2665, _2667, _2673, _2681,
    _2684, _2688, _2703, _2701,
    _2704, _2710, _2718, _2721,
    _2725, _2726, _2728, _2730,
    _2734, _2736, _2737, _2738,
    _2740, _2743, _2747, _2750,
    _2637, _2754, _2758, _2760,
    _2763, _2770, _2776, _2780,
    _2705, _2783, _2786, _2636
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'AssemblySystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblySystemDeflection',)


class AssemblySystemDeflection(_2636.AbstractAssemblySystemDeflection):
    """AssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE = _ASSEMBLY_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'AssemblySystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def overall_bearing_reliability(self) -> 'float':
        """float: 'OverallBearingReliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverallBearingReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def overall_gear_reliability(self) -> 'float':
        """float: 'OverallGearReliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverallGearReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def overall_oil_seal_reliability(self) -> 'float':
        """float: 'OverallOilSealReliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverallOilSealReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def overall_shaft_reliability(self) -> 'float':
        """float: 'OverallShaftReliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverallShaftReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def overall_system_reliability(self) -> 'float':
        """float: 'OverallSystemReliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverallSystemReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def analysis_settings(self) -> '_50.AnalysisSettingsItem':
        """AnalysisSettingsItem: 'AnalysisSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisSettings

        if temp is None:
            return None

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
    def assembly_load_case(self) -> '_6745.AssemblyLoadCase':
        """AssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        if _6745.AssemblyLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_load_case to AssemblyLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_3983.AssemblyPowerFlow':
        """AssemblyPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _3983.AssemblyPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to AssemblyPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_for_all_gear_sets(self) -> '_1217.GearSetGroupDutyCycle':
        """GearSetGroupDutyCycle: 'RatingForAllGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingForAllGearSets

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
    def bearings(self) -> 'List[_2644.BearingSystemDeflection]':
        """List[BearingSystemDeflection]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def belt_drives(self) -> 'List[_2646.BeltDriveSystemDeflection]':
        """List[BeltDriveSystemDeflection]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BeltDrives

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_2648.BevelDifferentialGearSetSystemDeflection]':
        """List[BevelDifferentialGearSetSystemDeflection]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolted_joints(self) -> 'List[_2655.BoltedJointSystemDeflection]':
        """List[BoltedJointSystemDeflection]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltedJoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolts(self) -> 'List[_2656.BoltSystemDeflection]':
        """List[BoltSystemDeflection]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bolts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cv_ts(self) -> 'List[_2680.CVTSystemDeflection]':
        """List[CVTSystemDeflection]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CVTs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def clutches(self) -> 'List[_2659.ClutchSystemDeflection]':
        """List[ClutchSystemDeflection]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Clutches

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_details(self) -> 'List[_2661.ComponentSystemDeflection]':
        """List[ComponentSystemDeflection]: 'ComponentDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_couplings(self) -> 'List[_2665.ConceptCouplingSystemDeflection]':
        """List[ConceptCouplingSystemDeflection]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gear_sets(self) -> 'List[_2667.ConceptGearSetSystemDeflection]':
        """List[ConceptGearSetSystemDeflection]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_details(self) -> 'List[_2673.ConnectionSystemDeflection]':
        """List[ConnectionSystemDeflection]: 'ConnectionDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_2681.CycloidalAssemblySystemDeflection]':
        """List[CycloidalAssemblySystemDeflection]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_discs(self) -> 'List[_2684.CycloidalDiscSystemDeflection]':
        """List[CycloidalDiscSystemDeflection]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_2688.CylindricalGearSetSystemDeflection]':
        """List[CylindricalGearSetSystemDeflection]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def fe_parts(self) -> 'List[_2703.FEPartSystemDeflection]':
        """List[FEPartSystemDeflection]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gear_sets(self) -> 'List[_2701.FaceGearSetSystemDeflection]':
        """List[FaceGearSetSystemDeflection]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_2704.FlexiblePinAssemblySystemDeflection]':
        """List[FlexiblePinAssemblySystemDeflection]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlexiblePinAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_2710.HypoidGearSetSystemDeflection]':
        """List[HypoidGearSetSystemDeflection]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_2718.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection]':
        """List[KlingelnbergCycloPalloidHypoidGearSetSystemDeflection]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_2721.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def mass_discs(self) -> 'List[_2725.MassDiscSystemDeflection]':
        """List[MassDiscSystemDeflection]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def measurement_components(self) -> 'List[_2726.MeasurementComponentSystemDeflection]':
        """List[MeasurementComponentSystemDeflection]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeasurementComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def mountable_component_details(self) -> 'List[_2728.MountableComponentSystemDeflection]':
        """List[MountableComponentSystemDeflection]: 'MountableComponentDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponentDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def oil_seals(self) -> 'List[_2730.OilSealSystemDeflection]':
        """List[OilSealSystemDeflection]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilSeals

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_2734.PartToPartShearCouplingSystemDeflection]':
        """List[PartToPartShearCouplingSystemDeflection]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartToPartShearCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planet_carriers(self) -> 'List[_2736.PlanetCarrierSystemDeflection]':
        """List[PlanetCarrierSystemDeflection]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetCarriers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def point_loads(self) -> 'List[_2737.PointLoadSystemDeflection]':
        """List[PointLoadSystemDeflection]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_loads(self) -> 'List[_2738.PowerLoadSystemDeflection]':
        """List[PowerLoadSystemDeflection]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def ring_pins(self) -> 'List[_2740.RingPinsSystemDeflection]':
        """List[RingPinsSystemDeflection]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPins

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def rolling_bearings(self) -> 'List[_2644.BearingSystemDeflection]':
        """List[BearingSystemDeflection]: 'RollingBearings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingBearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_2743.RollingRingAssemblySystemDeflection]':
        """List[RollingRingAssemblySystemDeflection]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingRingAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_2747.ShaftHubConnectionSystemDeflection]':
        """List[ShaftHubConnectionSystemDeflection]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftHubConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shafts(self) -> 'List[_2750.ShaftSystemDeflection]':
        """List[ShaftSystemDeflection]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shafts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shafts_and_housings(self) -> 'List[_2637.AbstractShaftOrHousingSystemDeflection]':
        """List[AbstractShaftOrHousingSystemDeflection]: 'ShaftsAndHousings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftsAndHousings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def sorted_converged_component_details(self) -> 'List[_2661.ComponentSystemDeflection]':
        """List[ComponentSystemDeflection]: 'SortedConvergedComponentDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SortedConvergedComponentDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def sorted_converged_connection_details(self) -> 'List[_2673.ConnectionSystemDeflection]':
        """List[ConnectionSystemDeflection]: 'SortedConvergedConnectionDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SortedConvergedConnectionDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def sorted_unconverged_component_details(self) -> 'List[_2661.ComponentSystemDeflection]':
        """List[ComponentSystemDeflection]: 'SortedUnconvergedComponentDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SortedUnconvergedComponentDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def sorted_unconverged_connection_details(self) -> 'List[_2673.ConnectionSystemDeflection]':
        """List[ConnectionSystemDeflection]: 'SortedUnconvergedConnectionDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SortedUnconvergedConnectionDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_2754.SpiralBevelGearSetSystemDeflection]':
        """List[SpiralBevelGearSetSystemDeflection]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spring_dampers(self) -> 'List[_2758.SpringDamperSystemDeflection]':
        """List[SpringDamperSystemDeflection]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpringDampers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_2760.StraightBevelDiffGearSetSystemDeflection]':
        """List[StraightBevelDiffGearSetSystemDeflection]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_2763.StraightBevelGearSetSystemDeflection]':
        """List[StraightBevelGearSetSystemDeflection]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def supercharger_rotor_sets(self) -> 'List[_2688.CylindricalGearSetSystemDeflection]':
        """List[CylindricalGearSetSystemDeflection]: 'SuperchargerRotorSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SuperchargerRotorSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def synchronisers(self) -> 'List[_2770.SynchroniserSystemDeflection]':
        """List[SynchroniserSystemDeflection]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Synchronisers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def torque_converters(self) -> 'List[_2776.TorqueConverterSystemDeflection]':
        """List[TorqueConverterSystemDeflection]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueConverters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def unbalanced_masses(self) -> 'List[_2780.UnbalancedMassSystemDeflection]':
        """List[UnbalancedMassSystemDeflection]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UnbalancedMasses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def unconverged_bearings_sorted_by_load(self) -> 'List[_2644.BearingSystemDeflection]':
        """List[BearingSystemDeflection]: 'UnconvergedBearingsSortedByLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UnconvergedBearingsSortedByLoad

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def unconverged_gear_meshes_sorted_by_power(self) -> 'List[_2705.GearMeshSystemDeflection]':
        """List[GearMeshSystemDeflection]: 'UnconvergedGearMeshesSortedByPower' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UnconvergedGearMeshesSortedByPower

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gear_sets(self) -> 'List[_2783.WormGearSetSystemDeflection]':
        """List[WormGearSetSystemDeflection]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_2786.ZerolBevelGearSetSystemDeflection]':
        """List[ZerolBevelGearSetSystemDeflection]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
