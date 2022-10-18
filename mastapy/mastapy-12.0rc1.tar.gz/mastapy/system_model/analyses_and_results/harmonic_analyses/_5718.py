"""_5718.py

PartHarmonicAnalysis
"""


from typing import List

from mastapy.system_model.part_model import (
    _2420, _2386, _2387, _2388,
    _2389, _2392, _2394, _2395,
    _2396, _2399, _2400, _2404,
    _2405, _2406, _2407, _2414,
    _2415, _2416, _2418, _2421,
    _2423, _2424, _2426, _2428,
    _2429, _2431
)
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.shaft_model import _2434
from mastapy.system_model.part_model.gears import (
    _2464, _2465, _2466, _2467,
    _2468, _2469, _2470, _2471,
    _2472, _2473, _2474, _2475,
    _2476, _2477, _2478, _2479,
    _2480, _2481, _2483, _2485,
    _2486, _2487, _2488, _2489,
    _2490, _2491, _2492, _2493,
    _2494, _2495, _2496, _2497,
    _2498, _2499, _2500, _2501,
    _2502, _2503, _2504, _2505
)
from mastapy.system_model.part_model.cycloidal import _2519, _2520, _2521
from mastapy.system_model.part_model.couplings import (
    _2527, _2529, _2530, _2532,
    _2533, _2534, _2535, _2537,
    _2538, _2539, _2540, _2541,
    _2547, _2548, _2549, _2551,
    _2552, _2553, _2555, _2556,
    _2557, _2558, _2559, _2561
)
from mastapy.system_model.analyses_and_results.modal_analyses import (
    _4601, _4514, _4515, _4516,
    _4519, _4520, _4521, _4522,
    _4524, _4526, _4527, _4528,
    _4529, _4531, _4532, _4533,
    _4534, _4536, _4537, _4539,
    _4541, _4542, _4544, _4545,
    _4547, _4548, _4550, _4553,
    _4554, _4556, _4557, _4558,
    _4560, _4563, _4564, _4565,
    _4566, _4569, _4571, _4572,
    _4573, _4574, _4577, _4578,
    _4579, _4581, _4582, _4585,
    _4586, _4588, _4589, _4591,
    _4592, _4593, _4594, _4598,
    _4599, _4603, _4604, _4606,
    _4607, _4608, _4609, _4610,
    _4611, _4613, _4615, _4616,
    _4617, _4618, _4621, _4623,
    _4624, _4626, _4627, _4629,
    _4630, _4632, _4633, _4634,
    _4635, _4636, _4637, _4638,
    _4639, _4641, _4642, _4643,
    _4644, _4645, _4650, _4651,
    _4653, _4654
)
from mastapy.system_model.analyses_and_results.harmonic_analyses import _2583, _2584, _5698
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6997
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5999
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2731, _2636, _2637, _2638,
    _2641, _2642, _2643, _2644,
    _2646, _2648, _2649, _2650,
    _2651, _2653, _2654, _2655,
    _2656, _2658, _2659, _2661,
    _2664, _2665, _2667, _2668,
    _2671, _2672, _2674, _2676,
    _2677, _2679, _2680, _2681,
    _2684, _2688, _2689, _2690,
    _2691, _2692, _2693, _2696,
    _2697, _2698, _2701, _2702,
    _2703, _2704, _2706, _2707,
    _2708, _2710, _2711, _2715,
    _2716, _2718, _2719, _2721,
    _2722, _2725, _2726, _2728,
    _2730, _2733, _2734, _2736,
    _2737, _2738, _2739, _2740,
    _2743, _2745, _2746, _2747,
    _2750, _2752, _2754, _2755,
    _2757, _2758, _2760, _2761,
    _2763, _2764, _2765, _2766,
    _2767, _2768, _2769, _2770,
    _2775, _2776, _2777, _2780,
    _2781, _2783, _2784, _2786,
    _2787
)
from mastapy.system_model.drawing import _2200
from mastapy.system_model.analyses_and_results.analysis_cases import _7472
from mastapy._internal.python_net import python_net_import

_PART_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'PartHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartHarmonicAnalysis',)


class PartHarmonicAnalysis(_7472.PartStaticLoadAnalysisCase):
    """PartHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_HARMONIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'PartHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2420.Part':
        """Part: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2420.Part.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Part. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_assembly(self) -> '_2386.Assembly':
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
    def component_design_of_type_abstract_assembly(self) -> '_2387.AbstractAssembly':
        """AbstractAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2387.AbstractAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_abstract_shaft(self) -> '_2388.AbstractShaft':
        """AbstractShaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2388.AbstractShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_abstract_shaft_or_housing(self) -> '_2389.AbstractShaftOrHousing':
        """AbstractShaftOrHousing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2389.AbstractShaftOrHousing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractShaftOrHousing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bearing(self) -> '_2392.Bearing':
        """Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2392.Bearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Bearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bolt(self) -> '_2394.Bolt':
        """Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2394.Bolt.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Bolt. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bolted_joint(self) -> '_2395.BoltedJoint':
        """BoltedJoint: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2395.BoltedJoint.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BoltedJoint. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_component(self) -> '_2396.Component':
        """Component: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2396.Component.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Component. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_connector(self) -> '_2399.Connector':
        """Connector: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2399.Connector.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Connector. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_datum(self) -> '_2400.Datum':
        """Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2400.Datum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Datum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_external_cad_model(self) -> '_2404.ExternalCADModel':
        """ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2404.ExternalCADModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ExternalCADModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_fe_part(self) -> '_2405.FEPart':
        """FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2405.FEPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to FEPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_flexible_pin_assembly(self) -> '_2406.FlexiblePinAssembly':
        """FlexiblePinAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2406.FlexiblePinAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to FlexiblePinAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_guide_dxf_model(self) -> '_2407.GuideDxfModel':
        """GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2407.GuideDxfModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to GuideDxfModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_mass_disc(self) -> '_2414.MassDisc':
        """MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2414.MassDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to MassDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_measurement_component(self) -> '_2415.MeasurementComponent':
        """MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2415.MeasurementComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to MeasurementComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_mountable_component(self) -> '_2416.MountableComponent':
        """MountableComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2416.MountableComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to MountableComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_oil_seal(self) -> '_2418.OilSeal':
        """OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2418.OilSeal.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to OilSeal. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_planet_carrier(self) -> '_2421.PlanetCarrier':
        """PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2421.PlanetCarrier.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to PlanetCarrier. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_point_load(self) -> '_2423.PointLoad':
        """PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2423.PointLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to PointLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_power_load(self) -> '_2424.PowerLoad':
        """PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2424.PowerLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to PowerLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_root_assembly(self) -> '_2426.RootAssembly':
        """RootAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2426.RootAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to RootAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_specialised_assembly(self) -> '_2428.SpecialisedAssembly':
        """SpecialisedAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2428.SpecialisedAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpecialisedAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_unbalanced_mass(self) -> '_2429.UnbalancedMass':
        """UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2429.UnbalancedMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to UnbalancedMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_virtual_component(self) -> '_2431.VirtualComponent':
        """VirtualComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2431.VirtualComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to VirtualComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_shaft(self) -> '_2434.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2434.Shaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Shaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_agma_gleason_conical_gear(self) -> '_2464.AGMAGleasonConicalGear':
        """AGMAGleasonConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2464.AGMAGleasonConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AGMAGleasonConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_agma_gleason_conical_gear_set(self) -> '_2465.AGMAGleasonConicalGearSet':
        """AGMAGleasonConicalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2465.AGMAGleasonConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AGMAGleasonConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bevel_differential_gear(self) -> '_2466.BevelDifferentialGear':
        """BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2466.BevelDifferentialGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bevel_differential_gear_set(self) -> '_2467.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2467.BevelDifferentialGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bevel_differential_planet_gear(self) -> '_2468.BevelDifferentialPlanetGear':
        """BevelDifferentialPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2468.BevelDifferentialPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bevel_differential_sun_gear(self) -> '_2469.BevelDifferentialSunGear':
        """BevelDifferentialSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2469.BevelDifferentialSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bevel_gear(self) -> '_2470.BevelGear':
        """BevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2470.BevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bevel_gear_set(self) -> '_2471.BevelGearSet':
        """BevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2471.BevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_concept_gear(self) -> '_2472.ConceptGear':
        """ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2472.ConceptGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_concept_gear_set(self) -> '_2473.ConceptGearSet':
        """ConceptGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2473.ConceptGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_conical_gear(self) -> '_2474.ConicalGear':
        """ConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2474.ConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_conical_gear_set(self) -> '_2475.ConicalGearSet':
        """ConicalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2475.ConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cylindrical_gear(self) -> '_2476.CylindricalGear':
        """CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2476.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cylindrical_gear_set(self) -> '_2477.CylindricalGearSet':
        """CylindricalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2477.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cylindrical_planet_gear(self) -> '_2478.CylindricalPlanetGear':
        """CylindricalPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2478.CylindricalPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_face_gear(self) -> '_2479.FaceGear':
        """FaceGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2479.FaceGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to FaceGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_face_gear_set(self) -> '_2480.FaceGearSet':
        """FaceGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2480.FaceGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to FaceGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_gear(self) -> '_2481.Gear':
        """Gear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2481.Gear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Gear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_gear_set(self) -> '_2483.GearSet':
        """GearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2483.GearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to GearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_hypoid_gear(self) -> '_2485.HypoidGear':
        """HypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2485.HypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to HypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_hypoid_gear_set(self) -> '_2486.HypoidGearSet':
        """HypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2486.HypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to HypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2487.KlingelnbergCycloPalloidConicalGear':
        """KlingelnbergCycloPalloidConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2487.KlingelnbergCycloPalloidConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> '_2488.KlingelnbergCycloPalloidConicalGearSet':
        """KlingelnbergCycloPalloidConicalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2488.KlingelnbergCycloPalloidConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2489.KlingelnbergCycloPalloidHypoidGear':
        """KlingelnbergCycloPalloidHypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2489.KlingelnbergCycloPalloidHypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2490.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2490.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2491.KlingelnbergCycloPalloidSpiralBevelGear':
        """KlingelnbergCycloPalloidSpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2491.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2492.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2492.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_planetary_gear_set(self) -> '_2493.PlanetaryGearSet':
        """PlanetaryGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2493.PlanetaryGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to PlanetaryGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_spiral_bevel_gear(self) -> '_2494.SpiralBevelGear':
        """SpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2494.SpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_spiral_bevel_gear_set(self) -> '_2495.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2495.SpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_straight_bevel_diff_gear(self) -> '_2496.StraightBevelDiffGear':
        """StraightBevelDiffGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2496.StraightBevelDiffGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelDiffGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_straight_bevel_diff_gear_set(self) -> '_2497.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2497.StraightBevelDiffGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelDiffGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_straight_bevel_gear(self) -> '_2498.StraightBevelGear':
        """StraightBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2498.StraightBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_straight_bevel_gear_set(self) -> '_2499.StraightBevelGearSet':
        """StraightBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2499.StraightBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_straight_bevel_planet_gear(self) -> '_2500.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2500.StraightBevelPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_straight_bevel_sun_gear(self) -> '_2501.StraightBevelSunGear':
        """StraightBevelSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2501.StraightBevelSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_worm_gear(self) -> '_2502.WormGear':
        """WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2502.WormGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to WormGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_worm_gear_set(self) -> '_2503.WormGearSet':
        """WormGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2503.WormGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to WormGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_zerol_bevel_gear(self) -> '_2504.ZerolBevelGear':
        """ZerolBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2504.ZerolBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ZerolBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_zerol_bevel_gear_set(self) -> '_2505.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2505.ZerolBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ZerolBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cycloidal_assembly(self) -> '_2519.CycloidalAssembly':
        """CycloidalAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2519.CycloidalAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CycloidalAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cycloidal_disc(self) -> '_2520.CycloidalDisc':
        """CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2520.CycloidalDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CycloidalDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_ring_pins(self) -> '_2521.RingPins':
        """RingPins: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2521.RingPins.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to RingPins. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_belt_drive(self) -> '_2527.BeltDrive':
        """BeltDrive: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2527.BeltDrive.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BeltDrive. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_clutch(self) -> '_2529.Clutch':
        """Clutch: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2529.Clutch.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Clutch. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_clutch_half(self) -> '_2530.ClutchHalf':
        """ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2530.ClutchHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ClutchHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_concept_coupling(self) -> '_2532.ConceptCoupling':
        """ConceptCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2532.ConceptCoupling.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptCoupling. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_concept_coupling_half(self) -> '_2533.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2533.ConceptCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_coupling(self) -> '_2534.Coupling':
        """Coupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2534.Coupling.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Coupling. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_coupling_half(self) -> '_2535.CouplingHalf':
        """CouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2535.CouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cvt(self) -> '_2537.CVT':
        """CVT: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2537.CVT.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CVT. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cvt_pulley(self) -> '_2538.CVTPulley':
        """CVTPulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2538.CVTPulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CVTPulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_part_to_part_shear_coupling(self) -> '_2539.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2539.PartToPartShearCoupling.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to PartToPartShearCoupling. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_part_to_part_shear_coupling_half(self) -> '_2540.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2540.PartToPartShearCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to PartToPartShearCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_pulley(self) -> '_2541.Pulley':
        """Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2541.Pulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Pulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_rolling_ring(self) -> '_2547.RollingRing':
        """RollingRing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2547.RollingRing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to RollingRing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_rolling_ring_assembly(self) -> '_2548.RollingRingAssembly':
        """RollingRingAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2548.RollingRingAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to RollingRingAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_shaft_hub_connection(self) -> '_2549.ShaftHubConnection':
        """ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2549.ShaftHubConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ShaftHubConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_spring_damper(self) -> '_2551.SpringDamper':
        """SpringDamper: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2551.SpringDamper.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpringDamper. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_spring_damper_half(self) -> '_2552.SpringDamperHalf':
        """SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2552.SpringDamperHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpringDamperHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_synchroniser(self) -> '_2553.Synchroniser':
        """Synchroniser: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2553.Synchroniser.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Synchroniser. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_synchroniser_half(self) -> '_2555.SynchroniserHalf':
        """SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2555.SynchroniserHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_synchroniser_part(self) -> '_2556.SynchroniserPart':
        """SynchroniserPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2556.SynchroniserPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_synchroniser_sleeve(self) -> '_2557.SynchroniserSleeve':
        """SynchroniserSleeve: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2557.SynchroniserSleeve.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserSleeve. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_torque_converter(self) -> '_2558.TorqueConverter':
        """TorqueConverter: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2558.TorqueConverter.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverter. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_torque_converter_pump(self) -> '_2559.TorqueConverterPump':
        """TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2559.TorqueConverterPump.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverterPump. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_torque_converter_turbine(self) -> '_2561.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2561.TorqueConverterTurbine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverterTurbine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis(self) -> '_4601.PartModalAnalysis':
        """PartModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4601.PartModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to PartModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_abstract_assembly_modal_analysis(self) -> '_4514.AbstractAssemblyModalAnalysis':
        """AbstractAssemblyModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4514.AbstractAssemblyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to AbstractAssemblyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_abstract_shaft_modal_analysis(self) -> '_4515.AbstractShaftModalAnalysis':
        """AbstractShaftModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4515.AbstractShaftModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to AbstractShaftModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_abstract_shaft_or_housing_modal_analysis(self) -> '_4516.AbstractShaftOrHousingModalAnalysis':
        """AbstractShaftOrHousingModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4516.AbstractShaftOrHousingModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to AbstractShaftOrHousingModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_agma_gleason_conical_gear_modal_analysis(self) -> '_4519.AGMAGleasonConicalGearModalAnalysis':
        """AGMAGleasonConicalGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4519.AGMAGleasonConicalGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to AGMAGleasonConicalGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_agma_gleason_conical_gear_set_modal_analysis(self) -> '_4520.AGMAGleasonConicalGearSetModalAnalysis':
        """AGMAGleasonConicalGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4520.AGMAGleasonConicalGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to AGMAGleasonConicalGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_assembly_modal_analysis(self) -> '_4521.AssemblyModalAnalysis':
        """AssemblyModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4521.AssemblyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to AssemblyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_bearing_modal_analysis(self) -> '_4522.BearingModalAnalysis':
        """BearingModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4522.BearingModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to BearingModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_belt_drive_modal_analysis(self) -> '_4524.BeltDriveModalAnalysis':
        """BeltDriveModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4524.BeltDriveModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to BeltDriveModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_bevel_differential_gear_modal_analysis(self) -> '_4526.BevelDifferentialGearModalAnalysis':
        """BevelDifferentialGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4526.BevelDifferentialGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to BevelDifferentialGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_bevel_differential_gear_set_modal_analysis(self) -> '_4527.BevelDifferentialGearSetModalAnalysis':
        """BevelDifferentialGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4527.BevelDifferentialGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to BevelDifferentialGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_bevel_differential_planet_gear_modal_analysis(self) -> '_4528.BevelDifferentialPlanetGearModalAnalysis':
        """BevelDifferentialPlanetGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4528.BevelDifferentialPlanetGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to BevelDifferentialPlanetGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_bevel_differential_sun_gear_modal_analysis(self) -> '_4529.BevelDifferentialSunGearModalAnalysis':
        """BevelDifferentialSunGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4529.BevelDifferentialSunGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to BevelDifferentialSunGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_bevel_gear_modal_analysis(self) -> '_4531.BevelGearModalAnalysis':
        """BevelGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4531.BevelGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to BevelGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_bevel_gear_set_modal_analysis(self) -> '_4532.BevelGearSetModalAnalysis':
        """BevelGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4532.BevelGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to BevelGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_bolted_joint_modal_analysis(self) -> '_4533.BoltedJointModalAnalysis':
        """BoltedJointModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4533.BoltedJointModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to BoltedJointModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_bolt_modal_analysis(self) -> '_4534.BoltModalAnalysis':
        """BoltModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4534.BoltModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to BoltModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_clutch_half_modal_analysis(self) -> '_4536.ClutchHalfModalAnalysis':
        """ClutchHalfModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4536.ClutchHalfModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ClutchHalfModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_clutch_modal_analysis(self) -> '_4537.ClutchModalAnalysis':
        """ClutchModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4537.ClutchModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ClutchModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_component_modal_analysis(self) -> '_4539.ComponentModalAnalysis':
        """ComponentModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4539.ComponentModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ComponentModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_concept_coupling_half_modal_analysis(self) -> '_4541.ConceptCouplingHalfModalAnalysis':
        """ConceptCouplingHalfModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4541.ConceptCouplingHalfModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ConceptCouplingHalfModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_concept_coupling_modal_analysis(self) -> '_4542.ConceptCouplingModalAnalysis':
        """ConceptCouplingModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4542.ConceptCouplingModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ConceptCouplingModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_concept_gear_modal_analysis(self) -> '_4544.ConceptGearModalAnalysis':
        """ConceptGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4544.ConceptGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ConceptGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_concept_gear_set_modal_analysis(self) -> '_4545.ConceptGearSetModalAnalysis':
        """ConceptGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4545.ConceptGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ConceptGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_conical_gear_modal_analysis(self) -> '_4547.ConicalGearModalAnalysis':
        """ConicalGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4547.ConicalGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ConicalGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_conical_gear_set_modal_analysis(self) -> '_4548.ConicalGearSetModalAnalysis':
        """ConicalGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4548.ConicalGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ConicalGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_connector_modal_analysis(self) -> '_4550.ConnectorModalAnalysis':
        """ConnectorModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4550.ConnectorModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ConnectorModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_coupling_half_modal_analysis(self) -> '_4553.CouplingHalfModalAnalysis':
        """CouplingHalfModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4553.CouplingHalfModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to CouplingHalfModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_coupling_modal_analysis(self) -> '_4554.CouplingModalAnalysis':
        """CouplingModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4554.CouplingModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to CouplingModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_cvt_modal_analysis(self) -> '_4556.CVTModalAnalysis':
        """CVTModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4556.CVTModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to CVTModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_cvt_pulley_modal_analysis(self) -> '_4557.CVTPulleyModalAnalysis':
        """CVTPulleyModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4557.CVTPulleyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to CVTPulleyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_cycloidal_assembly_modal_analysis(self) -> '_4558.CycloidalAssemblyModalAnalysis':
        """CycloidalAssemblyModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4558.CycloidalAssemblyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to CycloidalAssemblyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_cycloidal_disc_modal_analysis(self) -> '_4560.CycloidalDiscModalAnalysis':
        """CycloidalDiscModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4560.CycloidalDiscModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to CycloidalDiscModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_cylindrical_gear_modal_analysis(self) -> '_4563.CylindricalGearModalAnalysis':
        """CylindricalGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4563.CylindricalGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to CylindricalGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_cylindrical_gear_set_modal_analysis(self) -> '_4564.CylindricalGearSetModalAnalysis':
        """CylindricalGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4564.CylindricalGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to CylindricalGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_cylindrical_planet_gear_modal_analysis(self) -> '_4565.CylindricalPlanetGearModalAnalysis':
        """CylindricalPlanetGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4565.CylindricalPlanetGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to CylindricalPlanetGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_datum_modal_analysis(self) -> '_4566.DatumModalAnalysis':
        """DatumModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4566.DatumModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to DatumModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_external_cad_model_modal_analysis(self) -> '_4569.ExternalCADModelModalAnalysis':
        """ExternalCADModelModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4569.ExternalCADModelModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ExternalCADModelModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_face_gear_modal_analysis(self) -> '_4571.FaceGearModalAnalysis':
        """FaceGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4571.FaceGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to FaceGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_face_gear_set_modal_analysis(self) -> '_4572.FaceGearSetModalAnalysis':
        """FaceGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4572.FaceGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to FaceGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_fe_part_modal_analysis(self) -> '_4573.FEPartModalAnalysis':
        """FEPartModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4573.FEPartModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to FEPartModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_flexible_pin_assembly_modal_analysis(self) -> '_4574.FlexiblePinAssemblyModalAnalysis':
        """FlexiblePinAssemblyModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4574.FlexiblePinAssemblyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to FlexiblePinAssemblyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_gear_modal_analysis(self) -> '_4577.GearModalAnalysis':
        """GearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4577.GearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to GearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_gear_set_modal_analysis(self) -> '_4578.GearSetModalAnalysis':
        """GearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4578.GearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to GearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_guide_dxf_model_modal_analysis(self) -> '_4579.GuideDxfModelModalAnalysis':
        """GuideDxfModelModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4579.GuideDxfModelModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to GuideDxfModelModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_hypoid_gear_modal_analysis(self) -> '_4581.HypoidGearModalAnalysis':
        """HypoidGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4581.HypoidGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to HypoidGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_hypoid_gear_set_modal_analysis(self) -> '_4582.HypoidGearSetModalAnalysis':
        """HypoidGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4582.HypoidGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to HypoidGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_conical_gear_modal_analysis(self) -> '_4585.KlingelnbergCycloPalloidConicalGearModalAnalysis':
        """KlingelnbergCycloPalloidConicalGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4585.KlingelnbergCycloPalloidConicalGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to KlingelnbergCycloPalloidConicalGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(self) -> '_4586.KlingelnbergCycloPalloidConicalGearSetModalAnalysis':
        """KlingelnbergCycloPalloidConicalGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4586.KlingelnbergCycloPalloidConicalGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to KlingelnbergCycloPalloidConicalGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(self) -> '_4588.KlingelnbergCycloPalloidHypoidGearModalAnalysis':
        """KlingelnbergCycloPalloidHypoidGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4588.KlingelnbergCycloPalloidHypoidGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to KlingelnbergCycloPalloidHypoidGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(self) -> '_4589.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis':
        """KlingelnbergCycloPalloidHypoidGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4589.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to KlingelnbergCycloPalloidHypoidGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(self) -> '_4591.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis':
        """KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4591.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(self) -> '_4592.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis':
        """KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4592.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_mass_disc_modal_analysis(self) -> '_4593.MassDiscModalAnalysis':
        """MassDiscModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4593.MassDiscModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to MassDiscModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_measurement_component_modal_analysis(self) -> '_4594.MeasurementComponentModalAnalysis':
        """MeasurementComponentModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4594.MeasurementComponentModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to MeasurementComponentModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_mountable_component_modal_analysis(self) -> '_4598.MountableComponentModalAnalysis':
        """MountableComponentModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4598.MountableComponentModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to MountableComponentModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_oil_seal_modal_analysis(self) -> '_4599.OilSealModalAnalysis':
        """OilSealModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4599.OilSealModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to OilSealModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_part_to_part_shear_coupling_half_modal_analysis(self) -> '_4603.PartToPartShearCouplingHalfModalAnalysis':
        """PartToPartShearCouplingHalfModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4603.PartToPartShearCouplingHalfModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to PartToPartShearCouplingHalfModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_part_to_part_shear_coupling_modal_analysis(self) -> '_4604.PartToPartShearCouplingModalAnalysis':
        """PartToPartShearCouplingModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4604.PartToPartShearCouplingModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to PartToPartShearCouplingModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_planetary_gear_set_modal_analysis(self) -> '_4606.PlanetaryGearSetModalAnalysis':
        """PlanetaryGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4606.PlanetaryGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to PlanetaryGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_planet_carrier_modal_analysis(self) -> '_4607.PlanetCarrierModalAnalysis':
        """PlanetCarrierModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4607.PlanetCarrierModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to PlanetCarrierModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_point_load_modal_analysis(self) -> '_4608.PointLoadModalAnalysis':
        """PointLoadModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4608.PointLoadModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to PointLoadModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_power_load_modal_analysis(self) -> '_4609.PowerLoadModalAnalysis':
        """PowerLoadModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4609.PowerLoadModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to PowerLoadModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_pulley_modal_analysis(self) -> '_4610.PulleyModalAnalysis':
        """PulleyModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4610.PulleyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to PulleyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_ring_pins_modal_analysis(self) -> '_4611.RingPinsModalAnalysis':
        """RingPinsModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4611.RingPinsModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to RingPinsModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_rolling_ring_assembly_modal_analysis(self) -> '_4613.RollingRingAssemblyModalAnalysis':
        """RollingRingAssemblyModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4613.RollingRingAssemblyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to RollingRingAssemblyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_rolling_ring_modal_analysis(self) -> '_4615.RollingRingModalAnalysis':
        """RollingRingModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4615.RollingRingModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to RollingRingModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_root_assembly_modal_analysis(self) -> '_4616.RootAssemblyModalAnalysis':
        """RootAssemblyModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4616.RootAssemblyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to RootAssemblyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_shaft_hub_connection_modal_analysis(self) -> '_4617.ShaftHubConnectionModalAnalysis':
        """ShaftHubConnectionModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4617.ShaftHubConnectionModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ShaftHubConnectionModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_shaft_modal_analysis(self) -> '_4618.ShaftModalAnalysis':
        """ShaftModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4618.ShaftModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ShaftModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_specialised_assembly_modal_analysis(self) -> '_4621.SpecialisedAssemblyModalAnalysis':
        """SpecialisedAssemblyModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4621.SpecialisedAssemblyModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to SpecialisedAssemblyModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_spiral_bevel_gear_modal_analysis(self) -> '_4623.SpiralBevelGearModalAnalysis':
        """SpiralBevelGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4623.SpiralBevelGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to SpiralBevelGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_spiral_bevel_gear_set_modal_analysis(self) -> '_4624.SpiralBevelGearSetModalAnalysis':
        """SpiralBevelGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4624.SpiralBevelGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to SpiralBevelGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_spring_damper_half_modal_analysis(self) -> '_4626.SpringDamperHalfModalAnalysis':
        """SpringDamperHalfModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4626.SpringDamperHalfModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to SpringDamperHalfModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_spring_damper_modal_analysis(self) -> '_4627.SpringDamperModalAnalysis':
        """SpringDamperModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4627.SpringDamperModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to SpringDamperModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_straight_bevel_diff_gear_modal_analysis(self) -> '_4629.StraightBevelDiffGearModalAnalysis':
        """StraightBevelDiffGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4629.StraightBevelDiffGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to StraightBevelDiffGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_straight_bevel_diff_gear_set_modal_analysis(self) -> '_4630.StraightBevelDiffGearSetModalAnalysis':
        """StraightBevelDiffGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4630.StraightBevelDiffGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to StraightBevelDiffGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_straight_bevel_gear_modal_analysis(self) -> '_4632.StraightBevelGearModalAnalysis':
        """StraightBevelGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4632.StraightBevelGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to StraightBevelGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_straight_bevel_gear_set_modal_analysis(self) -> '_4633.StraightBevelGearSetModalAnalysis':
        """StraightBevelGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4633.StraightBevelGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to StraightBevelGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_straight_bevel_planet_gear_modal_analysis(self) -> '_4634.StraightBevelPlanetGearModalAnalysis':
        """StraightBevelPlanetGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4634.StraightBevelPlanetGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to StraightBevelPlanetGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_straight_bevel_sun_gear_modal_analysis(self) -> '_4635.StraightBevelSunGearModalAnalysis':
        """StraightBevelSunGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4635.StraightBevelSunGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to StraightBevelSunGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_synchroniser_half_modal_analysis(self) -> '_4636.SynchroniserHalfModalAnalysis':
        """SynchroniserHalfModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4636.SynchroniserHalfModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to SynchroniserHalfModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_synchroniser_modal_analysis(self) -> '_4637.SynchroniserModalAnalysis':
        """SynchroniserModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4637.SynchroniserModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to SynchroniserModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_synchroniser_part_modal_analysis(self) -> '_4638.SynchroniserPartModalAnalysis':
        """SynchroniserPartModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4638.SynchroniserPartModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to SynchroniserPartModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_synchroniser_sleeve_modal_analysis(self) -> '_4639.SynchroniserSleeveModalAnalysis':
        """SynchroniserSleeveModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4639.SynchroniserSleeveModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to SynchroniserSleeveModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_torque_converter_modal_analysis(self) -> '_4641.TorqueConverterModalAnalysis':
        """TorqueConverterModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4641.TorqueConverterModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to TorqueConverterModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_torque_converter_pump_modal_analysis(self) -> '_4642.TorqueConverterPumpModalAnalysis':
        """TorqueConverterPumpModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4642.TorqueConverterPumpModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to TorqueConverterPumpModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_torque_converter_turbine_modal_analysis(self) -> '_4643.TorqueConverterTurbineModalAnalysis':
        """TorqueConverterTurbineModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4643.TorqueConverterTurbineModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to TorqueConverterTurbineModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_unbalanced_mass_modal_analysis(self) -> '_4644.UnbalancedMassModalAnalysis':
        """UnbalancedMassModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4644.UnbalancedMassModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to UnbalancedMassModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_virtual_component_modal_analysis(self) -> '_4645.VirtualComponentModalAnalysis':
        """VirtualComponentModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4645.VirtualComponentModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to VirtualComponentModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_worm_gear_modal_analysis(self) -> '_4650.WormGearModalAnalysis':
        """WormGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4650.WormGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to WormGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_worm_gear_set_modal_analysis(self) -> '_4651.WormGearSetModalAnalysis':
        """WormGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4651.WormGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to WormGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_zerol_bevel_gear_modal_analysis(self) -> '_4653.ZerolBevelGearModalAnalysis':
        """ZerolBevelGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4653.ZerolBevelGearModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ZerolBevelGearModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis_of_type_zerol_bevel_gear_set_modal_analysis(self) -> '_4654.ZerolBevelGearSetModalAnalysis':
        """ZerolBevelGearSetModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        if _4654.ZerolBevelGearSetModalAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ZerolBevelGearSetModalAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis(self) -> '_2583.HarmonicAnalysis':
        """HarmonicAnalysis: 'HarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysis

        if temp is None:
            return None

        if _2583.HarmonicAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast harmonic_analysis to HarmonicAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis_options(self) -> '_5698.HarmonicAnalysisOptions':
        """HarmonicAnalysisOptions: 'HarmonicAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysisOptions

        if temp is None:
            return None

        if _5698.HarmonicAnalysisOptions.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast harmonic_analysis_options to HarmonicAnalysisOptions. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analyses_of_single_excitations(self) -> 'List[_5999.HarmonicAnalysisOfSingleExcitation]':
        """List[HarmonicAnalysisOfSingleExcitation]: 'HarmonicAnalysesOfSingleExcitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysesOfSingleExcitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def system_deflection_results(self) -> '_2731.PartSystemDeflection':
        """PartSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2731.PartSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to PartSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_abstract_assembly_system_deflection(self) -> '_2636.AbstractAssemblySystemDeflection':
        """AbstractAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2636.AbstractAssemblySystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to AbstractAssemblySystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_abstract_shaft_or_housing_system_deflection(self) -> '_2637.AbstractShaftOrHousingSystemDeflection':
        """AbstractShaftOrHousingSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2637.AbstractShaftOrHousingSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to AbstractShaftOrHousingSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_abstract_shaft_system_deflection(self) -> '_2638.AbstractShaftSystemDeflection':
        """AbstractShaftSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2638.AbstractShaftSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to AbstractShaftSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_agma_gleason_conical_gear_set_system_deflection(self) -> '_2641.AGMAGleasonConicalGearSetSystemDeflection':
        """AGMAGleasonConicalGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2641.AGMAGleasonConicalGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to AGMAGleasonConicalGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_agma_gleason_conical_gear_system_deflection(self) -> '_2642.AGMAGleasonConicalGearSystemDeflection':
        """AGMAGleasonConicalGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2642.AGMAGleasonConicalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to AGMAGleasonConicalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_assembly_system_deflection(self) -> '_2643.AssemblySystemDeflection':
        """AssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2643.AssemblySystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to AssemblySystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_bearing_system_deflection(self) -> '_2644.BearingSystemDeflection':
        """BearingSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2644.BearingSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BearingSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_belt_drive_system_deflection(self) -> '_2646.BeltDriveSystemDeflection':
        """BeltDriveSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2646.BeltDriveSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BeltDriveSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_bevel_differential_gear_set_system_deflection(self) -> '_2648.BevelDifferentialGearSetSystemDeflection':
        """BevelDifferentialGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2648.BevelDifferentialGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BevelDifferentialGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_bevel_differential_gear_system_deflection(self) -> '_2649.BevelDifferentialGearSystemDeflection':
        """BevelDifferentialGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2649.BevelDifferentialGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BevelDifferentialGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_bevel_differential_planet_gear_system_deflection(self) -> '_2650.BevelDifferentialPlanetGearSystemDeflection':
        """BevelDifferentialPlanetGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2650.BevelDifferentialPlanetGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BevelDifferentialPlanetGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_bevel_differential_sun_gear_system_deflection(self) -> '_2651.BevelDifferentialSunGearSystemDeflection':
        """BevelDifferentialSunGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2651.BevelDifferentialSunGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BevelDifferentialSunGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_bevel_gear_set_system_deflection(self) -> '_2653.BevelGearSetSystemDeflection':
        """BevelGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2653.BevelGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BevelGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_bevel_gear_system_deflection(self) -> '_2654.BevelGearSystemDeflection':
        """BevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2654.BevelGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BevelGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_bolted_joint_system_deflection(self) -> '_2655.BoltedJointSystemDeflection':
        """BoltedJointSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2655.BoltedJointSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BoltedJointSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_bolt_system_deflection(self) -> '_2656.BoltSystemDeflection':
        """BoltSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2656.BoltSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BoltSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_clutch_half_system_deflection(self) -> '_2658.ClutchHalfSystemDeflection':
        """ClutchHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2658.ClutchHalfSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ClutchHalfSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_clutch_system_deflection(self) -> '_2659.ClutchSystemDeflection':
        """ClutchSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2659.ClutchSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ClutchSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_component_system_deflection(self) -> '_2661.ComponentSystemDeflection':
        """ComponentSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2661.ComponentSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ComponentSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_concept_coupling_half_system_deflection(self) -> '_2664.ConceptCouplingHalfSystemDeflection':
        """ConceptCouplingHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2664.ConceptCouplingHalfSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ConceptCouplingHalfSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_concept_coupling_system_deflection(self) -> '_2665.ConceptCouplingSystemDeflection':
        """ConceptCouplingSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2665.ConceptCouplingSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ConceptCouplingSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_concept_gear_set_system_deflection(self) -> '_2667.ConceptGearSetSystemDeflection':
        """ConceptGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2667.ConceptGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ConceptGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_concept_gear_system_deflection(self) -> '_2668.ConceptGearSystemDeflection':
        """ConceptGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2668.ConceptGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ConceptGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_conical_gear_set_system_deflection(self) -> '_2671.ConicalGearSetSystemDeflection':
        """ConicalGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2671.ConicalGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ConicalGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_conical_gear_system_deflection(self) -> '_2672.ConicalGearSystemDeflection':
        """ConicalGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2672.ConicalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ConicalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_connector_system_deflection(self) -> '_2674.ConnectorSystemDeflection':
        """ConnectorSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2674.ConnectorSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ConnectorSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_coupling_half_system_deflection(self) -> '_2676.CouplingHalfSystemDeflection':
        """CouplingHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2676.CouplingHalfSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CouplingHalfSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_coupling_system_deflection(self) -> '_2677.CouplingSystemDeflection':
        """CouplingSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2677.CouplingSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CouplingSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_cvt_pulley_system_deflection(self) -> '_2679.CVTPulleySystemDeflection':
        """CVTPulleySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2679.CVTPulleySystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CVTPulleySystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_cvt_system_deflection(self) -> '_2680.CVTSystemDeflection':
        """CVTSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2680.CVTSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CVTSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_cycloidal_assembly_system_deflection(self) -> '_2681.CycloidalAssemblySystemDeflection':
        """CycloidalAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2681.CycloidalAssemblySystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CycloidalAssemblySystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_cycloidal_disc_system_deflection(self) -> '_2684.CycloidalDiscSystemDeflection':
        """CycloidalDiscSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2684.CycloidalDiscSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CycloidalDiscSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_cylindrical_gear_set_system_deflection(self) -> '_2688.CylindricalGearSetSystemDeflection':
        """CylindricalGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2688.CylindricalGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_cylindrical_gear_set_system_deflection_timestep(self) -> '_2689.CylindricalGearSetSystemDeflectionTimestep':
        """CylindricalGearSetSystemDeflectionTimestep: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2689.CylindricalGearSetSystemDeflectionTimestep.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearSetSystemDeflectionTimestep. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_cylindrical_gear_set_system_deflection_with_ltca_results(self) -> '_2690.CylindricalGearSetSystemDeflectionWithLTCAResults':
        """CylindricalGearSetSystemDeflectionWithLTCAResults: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2690.CylindricalGearSetSystemDeflectionWithLTCAResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearSetSystemDeflectionWithLTCAResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_cylindrical_gear_system_deflection(self) -> '_2691.CylindricalGearSystemDeflection':
        """CylindricalGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2691.CylindricalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_cylindrical_gear_system_deflection_timestep(self) -> '_2692.CylindricalGearSystemDeflectionTimestep':
        """CylindricalGearSystemDeflectionTimestep: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2692.CylindricalGearSystemDeflectionTimestep.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearSystemDeflectionTimestep. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_cylindrical_gear_system_deflection_with_ltca_results(self) -> '_2693.CylindricalGearSystemDeflectionWithLTCAResults':
        """CylindricalGearSystemDeflectionWithLTCAResults: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2693.CylindricalGearSystemDeflectionWithLTCAResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearSystemDeflectionWithLTCAResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_cylindrical_planet_gear_system_deflection(self) -> '_2696.CylindricalPlanetGearSystemDeflection':
        """CylindricalPlanetGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2696.CylindricalPlanetGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalPlanetGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_datum_system_deflection(self) -> '_2697.DatumSystemDeflection':
        """DatumSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2697.DatumSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to DatumSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_external_cad_model_system_deflection(self) -> '_2698.ExternalCADModelSystemDeflection':
        """ExternalCADModelSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2698.ExternalCADModelSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ExternalCADModelSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_face_gear_set_system_deflection(self) -> '_2701.FaceGearSetSystemDeflection':
        """FaceGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2701.FaceGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to FaceGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_face_gear_system_deflection(self) -> '_2702.FaceGearSystemDeflection':
        """FaceGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2702.FaceGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to FaceGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_fe_part_system_deflection(self) -> '_2703.FEPartSystemDeflection':
        """FEPartSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2703.FEPartSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to FEPartSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_flexible_pin_assembly_system_deflection(self) -> '_2704.FlexiblePinAssemblySystemDeflection':
        """FlexiblePinAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2704.FlexiblePinAssemblySystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to FlexiblePinAssemblySystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_gear_set_system_deflection(self) -> '_2706.GearSetSystemDeflection':
        """GearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2706.GearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to GearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_gear_system_deflection(self) -> '_2707.GearSystemDeflection':
        """GearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2707.GearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to GearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_guide_dxf_model_system_deflection(self) -> '_2708.GuideDxfModelSystemDeflection':
        """GuideDxfModelSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2708.GuideDxfModelSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to GuideDxfModelSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_hypoid_gear_set_system_deflection(self) -> '_2710.HypoidGearSetSystemDeflection':
        """HypoidGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2710.HypoidGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to HypoidGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_hypoid_gear_system_deflection(self) -> '_2711.HypoidGearSystemDeflection':
        """HypoidGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2711.HypoidGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to HypoidGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(self) -> '_2715.KlingelnbergCycloPalloidConicalGearSetSystemDeflection':
        """KlingelnbergCycloPalloidConicalGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2715.KlingelnbergCycloPalloidConicalGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to KlingelnbergCycloPalloidConicalGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_klingelnberg_cyclo_palloid_conical_gear_system_deflection(self) -> '_2716.KlingelnbergCycloPalloidConicalGearSystemDeflection':
        """KlingelnbergCycloPalloidConicalGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2716.KlingelnbergCycloPalloidConicalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to KlingelnbergCycloPalloidConicalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(self) -> '_2718.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection':
        """KlingelnbergCycloPalloidHypoidGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2718.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to KlingelnbergCycloPalloidHypoidGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(self) -> '_2719.KlingelnbergCycloPalloidHypoidGearSystemDeflection':
        """KlingelnbergCycloPalloidHypoidGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2719.KlingelnbergCycloPalloidHypoidGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to KlingelnbergCycloPalloidHypoidGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(self) -> '_2721.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection':
        """KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2721.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(self) -> '_2722.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection':
        """KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2722.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_mass_disc_system_deflection(self) -> '_2725.MassDiscSystemDeflection':
        """MassDiscSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2725.MassDiscSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to MassDiscSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_measurement_component_system_deflection(self) -> '_2726.MeasurementComponentSystemDeflection':
        """MeasurementComponentSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2726.MeasurementComponentSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to MeasurementComponentSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_mountable_component_system_deflection(self) -> '_2728.MountableComponentSystemDeflection':
        """MountableComponentSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2728.MountableComponentSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to MountableComponentSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_oil_seal_system_deflection(self) -> '_2730.OilSealSystemDeflection':
        """OilSealSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2730.OilSealSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to OilSealSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_part_to_part_shear_coupling_half_system_deflection(self) -> '_2733.PartToPartShearCouplingHalfSystemDeflection':
        """PartToPartShearCouplingHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2733.PartToPartShearCouplingHalfSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to PartToPartShearCouplingHalfSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_part_to_part_shear_coupling_system_deflection(self) -> '_2734.PartToPartShearCouplingSystemDeflection':
        """PartToPartShearCouplingSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2734.PartToPartShearCouplingSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to PartToPartShearCouplingSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_planet_carrier_system_deflection(self) -> '_2736.PlanetCarrierSystemDeflection':
        """PlanetCarrierSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2736.PlanetCarrierSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to PlanetCarrierSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_point_load_system_deflection(self) -> '_2737.PointLoadSystemDeflection':
        """PointLoadSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2737.PointLoadSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to PointLoadSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_power_load_system_deflection(self) -> '_2738.PowerLoadSystemDeflection':
        """PowerLoadSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2738.PowerLoadSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to PowerLoadSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_pulley_system_deflection(self) -> '_2739.PulleySystemDeflection':
        """PulleySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2739.PulleySystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to PulleySystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_ring_pins_system_deflection(self) -> '_2740.RingPinsSystemDeflection':
        """RingPinsSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2740.RingPinsSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to RingPinsSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_rolling_ring_assembly_system_deflection(self) -> '_2743.RollingRingAssemblySystemDeflection':
        """RollingRingAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2743.RollingRingAssemblySystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to RollingRingAssemblySystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_rolling_ring_system_deflection(self) -> '_2745.RollingRingSystemDeflection':
        """RollingRingSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2745.RollingRingSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to RollingRingSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_root_assembly_system_deflection(self) -> '_2746.RootAssemblySystemDeflection':
        """RootAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2746.RootAssemblySystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to RootAssemblySystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_shaft_hub_connection_system_deflection(self) -> '_2747.ShaftHubConnectionSystemDeflection':
        """ShaftHubConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2747.ShaftHubConnectionSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ShaftHubConnectionSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_shaft_system_deflection(self) -> '_2750.ShaftSystemDeflection':
        """ShaftSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2750.ShaftSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ShaftSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_specialised_assembly_system_deflection(self) -> '_2752.SpecialisedAssemblySystemDeflection':
        """SpecialisedAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2752.SpecialisedAssemblySystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to SpecialisedAssemblySystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_spiral_bevel_gear_set_system_deflection(self) -> '_2754.SpiralBevelGearSetSystemDeflection':
        """SpiralBevelGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2754.SpiralBevelGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to SpiralBevelGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_spiral_bevel_gear_system_deflection(self) -> '_2755.SpiralBevelGearSystemDeflection':
        """SpiralBevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2755.SpiralBevelGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to SpiralBevelGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_spring_damper_half_system_deflection(self) -> '_2757.SpringDamperHalfSystemDeflection':
        """SpringDamperHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2757.SpringDamperHalfSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to SpringDamperHalfSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_spring_damper_system_deflection(self) -> '_2758.SpringDamperSystemDeflection':
        """SpringDamperSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2758.SpringDamperSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to SpringDamperSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_straight_bevel_diff_gear_set_system_deflection(self) -> '_2760.StraightBevelDiffGearSetSystemDeflection':
        """StraightBevelDiffGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2760.StraightBevelDiffGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to StraightBevelDiffGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_straight_bevel_diff_gear_system_deflection(self) -> '_2761.StraightBevelDiffGearSystemDeflection':
        """StraightBevelDiffGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2761.StraightBevelDiffGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to StraightBevelDiffGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_straight_bevel_gear_set_system_deflection(self) -> '_2763.StraightBevelGearSetSystemDeflection':
        """StraightBevelGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2763.StraightBevelGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to StraightBevelGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_straight_bevel_gear_system_deflection(self) -> '_2764.StraightBevelGearSystemDeflection':
        """StraightBevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2764.StraightBevelGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to StraightBevelGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_straight_bevel_planet_gear_system_deflection(self) -> '_2765.StraightBevelPlanetGearSystemDeflection':
        """StraightBevelPlanetGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2765.StraightBevelPlanetGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to StraightBevelPlanetGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_straight_bevel_sun_gear_system_deflection(self) -> '_2766.StraightBevelSunGearSystemDeflection':
        """StraightBevelSunGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2766.StraightBevelSunGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to StraightBevelSunGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_synchroniser_half_system_deflection(self) -> '_2767.SynchroniserHalfSystemDeflection':
        """SynchroniserHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2767.SynchroniserHalfSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to SynchroniserHalfSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_synchroniser_part_system_deflection(self) -> '_2768.SynchroniserPartSystemDeflection':
        """SynchroniserPartSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2768.SynchroniserPartSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to SynchroniserPartSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_synchroniser_sleeve_system_deflection(self) -> '_2769.SynchroniserSleeveSystemDeflection':
        """SynchroniserSleeveSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2769.SynchroniserSleeveSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to SynchroniserSleeveSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_synchroniser_system_deflection(self) -> '_2770.SynchroniserSystemDeflection':
        """SynchroniserSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2770.SynchroniserSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to SynchroniserSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_torque_converter_pump_system_deflection(self) -> '_2775.TorqueConverterPumpSystemDeflection':
        """TorqueConverterPumpSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2775.TorqueConverterPumpSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to TorqueConverterPumpSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_torque_converter_system_deflection(self) -> '_2776.TorqueConverterSystemDeflection':
        """TorqueConverterSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2776.TorqueConverterSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to TorqueConverterSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_torque_converter_turbine_system_deflection(self) -> '_2777.TorqueConverterTurbineSystemDeflection':
        """TorqueConverterTurbineSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2777.TorqueConverterTurbineSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to TorqueConverterTurbineSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_unbalanced_mass_system_deflection(self) -> '_2780.UnbalancedMassSystemDeflection':
        """UnbalancedMassSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2780.UnbalancedMassSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to UnbalancedMassSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_virtual_component_system_deflection(self) -> '_2781.VirtualComponentSystemDeflection':
        """VirtualComponentSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2781.VirtualComponentSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to VirtualComponentSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_worm_gear_set_system_deflection(self) -> '_2783.WormGearSetSystemDeflection':
        """WormGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2783.WormGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to WormGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_worm_gear_system_deflection(self) -> '_2784.WormGearSystemDeflection':
        """WormGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2784.WormGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to WormGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_zerol_bevel_gear_set_system_deflection(self) -> '_2786.ZerolBevelGearSetSystemDeflection':
        """ZerolBevelGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2786.ZerolBevelGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ZerolBevelGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results_of_type_zerol_bevel_gear_system_deflection(self) -> '_2787.ZerolBevelGearSystemDeflection':
        """ZerolBevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        if _2787.ZerolBevelGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ZerolBevelGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def create_viewable(self) -> '_2200.HarmonicAnalysisViewable':
        """ 'CreateViewable' is the original name of this method.

        Returns:
            mastapy.system_model.drawing.HarmonicAnalysisViewable
        """

        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None
