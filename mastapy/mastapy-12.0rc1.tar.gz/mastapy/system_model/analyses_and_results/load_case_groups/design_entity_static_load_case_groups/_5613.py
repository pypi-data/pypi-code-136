"""_5613.py

PartStaticLoadCaseGroup
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
from mastapy.system_model.analyses_and_results.static_loads import _6854
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5611
from mastapy._internal.python_net import python_net_import

_PART_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups', 'PartStaticLoadCaseGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('PartStaticLoadCaseGroup',)


class PartStaticLoadCaseGroup(_5611.DesignEntityStaticLoadCaseGroup):
    """PartStaticLoadCaseGroup

    This is a mastapy class.
    """

    TYPE = _PART_STATIC_LOAD_CASE_GROUP

    def __init__(self, instance_to_wrap: 'PartStaticLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part(self) -> '_2420.Part':
        """Part: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2420.Part.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to Part. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_assembly(self) -> '_2386.Assembly':
        """Assembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2386.Assembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to Assembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_abstract_assembly(self) -> '_2387.AbstractAssembly':
        """AbstractAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2387.AbstractAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to AbstractAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_abstract_shaft(self) -> '_2388.AbstractShaft':
        """AbstractShaft: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2388.AbstractShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to AbstractShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_abstract_shaft_or_housing(self) -> '_2389.AbstractShaftOrHousing':
        """AbstractShaftOrHousing: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2389.AbstractShaftOrHousing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to AbstractShaftOrHousing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_bearing(self) -> '_2392.Bearing':
        """Bearing: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2392.Bearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to Bearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_bolt(self) -> '_2394.Bolt':
        """Bolt: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2394.Bolt.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to Bolt. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_bolted_joint(self) -> '_2395.BoltedJoint':
        """BoltedJoint: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2395.BoltedJoint.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to BoltedJoint. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_component(self) -> '_2396.Component':
        """Component: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2396.Component.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to Component. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_connector(self) -> '_2399.Connector':
        """Connector: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2399.Connector.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to Connector. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_datum(self) -> '_2400.Datum':
        """Datum: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2400.Datum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to Datum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_external_cad_model(self) -> '_2404.ExternalCADModel':
        """ExternalCADModel: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2404.ExternalCADModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to ExternalCADModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_fe_part(self) -> '_2405.FEPart':
        """FEPart: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2405.FEPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to FEPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_flexible_pin_assembly(self) -> '_2406.FlexiblePinAssembly':
        """FlexiblePinAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2406.FlexiblePinAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to FlexiblePinAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_guide_dxf_model(self) -> '_2407.GuideDxfModel':
        """GuideDxfModel: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2407.GuideDxfModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to GuideDxfModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_mass_disc(self) -> '_2414.MassDisc':
        """MassDisc: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2414.MassDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to MassDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_measurement_component(self) -> '_2415.MeasurementComponent':
        """MeasurementComponent: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2415.MeasurementComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to MeasurementComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_mountable_component(self) -> '_2416.MountableComponent':
        """MountableComponent: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2416.MountableComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to MountableComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_oil_seal(self) -> '_2418.OilSeal':
        """OilSeal: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2418.OilSeal.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to OilSeal. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_planet_carrier(self) -> '_2421.PlanetCarrier':
        """PlanetCarrier: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2421.PlanetCarrier.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to PlanetCarrier. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_point_load(self) -> '_2423.PointLoad':
        """PointLoad: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2423.PointLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to PointLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_power_load(self) -> '_2424.PowerLoad':
        """PowerLoad: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2424.PowerLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to PowerLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_root_assembly(self) -> '_2426.RootAssembly':
        """RootAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2426.RootAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to RootAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_specialised_assembly(self) -> '_2428.SpecialisedAssembly':
        """SpecialisedAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2428.SpecialisedAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to SpecialisedAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_unbalanced_mass(self) -> '_2429.UnbalancedMass':
        """UnbalancedMass: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2429.UnbalancedMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to UnbalancedMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_virtual_component(self) -> '_2431.VirtualComponent':
        """VirtualComponent: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2431.VirtualComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to VirtualComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_shaft(self) -> '_2434.Shaft':
        """Shaft: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2434.Shaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to Shaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_agma_gleason_conical_gear(self) -> '_2464.AGMAGleasonConicalGear':
        """AGMAGleasonConicalGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2464.AGMAGleasonConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to AGMAGleasonConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_agma_gleason_conical_gear_set(self) -> '_2465.AGMAGleasonConicalGearSet':
        """AGMAGleasonConicalGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2465.AGMAGleasonConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to AGMAGleasonConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_bevel_differential_gear(self) -> '_2466.BevelDifferentialGear':
        """BevelDifferentialGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2466.BevelDifferentialGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to BevelDifferentialGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_bevel_differential_gear_set(self) -> '_2467.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2467.BevelDifferentialGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to BevelDifferentialGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_bevel_differential_planet_gear(self) -> '_2468.BevelDifferentialPlanetGear':
        """BevelDifferentialPlanetGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2468.BevelDifferentialPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to BevelDifferentialPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_bevel_differential_sun_gear(self) -> '_2469.BevelDifferentialSunGear':
        """BevelDifferentialSunGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2469.BevelDifferentialSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to BevelDifferentialSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_bevel_gear(self) -> '_2470.BevelGear':
        """BevelGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2470.BevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to BevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_bevel_gear_set(self) -> '_2471.BevelGearSet':
        """BevelGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2471.BevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to BevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_concept_gear(self) -> '_2472.ConceptGear':
        """ConceptGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2472.ConceptGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to ConceptGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_concept_gear_set(self) -> '_2473.ConceptGearSet':
        """ConceptGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2473.ConceptGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to ConceptGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_conical_gear(self) -> '_2474.ConicalGear':
        """ConicalGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2474.ConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to ConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_conical_gear_set(self) -> '_2475.ConicalGearSet':
        """ConicalGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2475.ConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to ConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_cylindrical_gear(self) -> '_2476.CylindricalGear':
        """CylindricalGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2476.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_cylindrical_gear_set(self) -> '_2477.CylindricalGearSet':
        """CylindricalGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2477.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_cylindrical_planet_gear(self) -> '_2478.CylindricalPlanetGear':
        """CylindricalPlanetGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2478.CylindricalPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to CylindricalPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_face_gear(self) -> '_2479.FaceGear':
        """FaceGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2479.FaceGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to FaceGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_face_gear_set(self) -> '_2480.FaceGearSet':
        """FaceGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2480.FaceGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to FaceGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_gear(self) -> '_2481.Gear':
        """Gear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2481.Gear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to Gear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_gear_set(self) -> '_2483.GearSet':
        """GearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2483.GearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to GearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_hypoid_gear(self) -> '_2485.HypoidGear':
        """HypoidGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2485.HypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to HypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_hypoid_gear_set(self) -> '_2486.HypoidGearSet':
        """HypoidGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2486.HypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to HypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2487.KlingelnbergCycloPalloidConicalGear':
        """KlingelnbergCycloPalloidConicalGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2487.KlingelnbergCycloPalloidConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> '_2488.KlingelnbergCycloPalloidConicalGearSet':
        """KlingelnbergCycloPalloidConicalGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2488.KlingelnbergCycloPalloidConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2489.KlingelnbergCycloPalloidHypoidGear':
        """KlingelnbergCycloPalloidHypoidGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2489.KlingelnbergCycloPalloidHypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2490.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2490.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2491.KlingelnbergCycloPalloidSpiralBevelGear':
        """KlingelnbergCycloPalloidSpiralBevelGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2491.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2492.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2492.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_planetary_gear_set(self) -> '_2493.PlanetaryGearSet':
        """PlanetaryGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2493.PlanetaryGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to PlanetaryGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_spiral_bevel_gear(self) -> '_2494.SpiralBevelGear':
        """SpiralBevelGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2494.SpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to SpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_spiral_bevel_gear_set(self) -> '_2495.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2495.SpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to SpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_straight_bevel_diff_gear(self) -> '_2496.StraightBevelDiffGear':
        """StraightBevelDiffGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2496.StraightBevelDiffGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelDiffGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_straight_bevel_diff_gear_set(self) -> '_2497.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2497.StraightBevelDiffGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelDiffGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_straight_bevel_gear(self) -> '_2498.StraightBevelGear':
        """StraightBevelGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2498.StraightBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_straight_bevel_gear_set(self) -> '_2499.StraightBevelGearSet':
        """StraightBevelGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2499.StraightBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_straight_bevel_planet_gear(self) -> '_2500.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2500.StraightBevelPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_straight_bevel_sun_gear(self) -> '_2501.StraightBevelSunGear':
        """StraightBevelSunGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2501.StraightBevelSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_worm_gear(self) -> '_2502.WormGear':
        """WormGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2502.WormGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to WormGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_worm_gear_set(self) -> '_2503.WormGearSet':
        """WormGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2503.WormGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to WormGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_zerol_bevel_gear(self) -> '_2504.ZerolBevelGear':
        """ZerolBevelGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2504.ZerolBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to ZerolBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_zerol_bevel_gear_set(self) -> '_2505.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2505.ZerolBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to ZerolBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_cycloidal_assembly(self) -> '_2519.CycloidalAssembly':
        """CycloidalAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2519.CycloidalAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to CycloidalAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_cycloidal_disc(self) -> '_2520.CycloidalDisc':
        """CycloidalDisc: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2520.CycloidalDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to CycloidalDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_ring_pins(self) -> '_2521.RingPins':
        """RingPins: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2521.RingPins.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to RingPins. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_belt_drive(self) -> '_2527.BeltDrive':
        """BeltDrive: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2527.BeltDrive.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to BeltDrive. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_clutch(self) -> '_2529.Clutch':
        """Clutch: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2529.Clutch.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to Clutch. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_clutch_half(self) -> '_2530.ClutchHalf':
        """ClutchHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2530.ClutchHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to ClutchHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_concept_coupling(self) -> '_2532.ConceptCoupling':
        """ConceptCoupling: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2532.ConceptCoupling.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to ConceptCoupling. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_concept_coupling_half(self) -> '_2533.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2533.ConceptCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to ConceptCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_coupling(self) -> '_2534.Coupling':
        """Coupling: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2534.Coupling.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to Coupling. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_coupling_half(self) -> '_2535.CouplingHalf':
        """CouplingHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2535.CouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to CouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_cvt(self) -> '_2537.CVT':
        """CVT: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2537.CVT.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to CVT. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_cvt_pulley(self) -> '_2538.CVTPulley':
        """CVTPulley: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2538.CVTPulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to CVTPulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_part_to_part_shear_coupling(self) -> '_2539.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2539.PartToPartShearCoupling.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to PartToPartShearCoupling. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_part_to_part_shear_coupling_half(self) -> '_2540.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2540.PartToPartShearCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to PartToPartShearCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_pulley(self) -> '_2541.Pulley':
        """Pulley: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2541.Pulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to Pulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_rolling_ring(self) -> '_2547.RollingRing':
        """RollingRing: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2547.RollingRing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to RollingRing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_rolling_ring_assembly(self) -> '_2548.RollingRingAssembly':
        """RollingRingAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2548.RollingRingAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to RollingRingAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_shaft_hub_connection(self) -> '_2549.ShaftHubConnection':
        """ShaftHubConnection: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2549.ShaftHubConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to ShaftHubConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_spring_damper(self) -> '_2551.SpringDamper':
        """SpringDamper: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2551.SpringDamper.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to SpringDamper. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_spring_damper_half(self) -> '_2552.SpringDamperHalf':
        """SpringDamperHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2552.SpringDamperHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to SpringDamperHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_synchroniser(self) -> '_2553.Synchroniser':
        """Synchroniser: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2553.Synchroniser.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to Synchroniser. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_synchroniser_half(self) -> '_2555.SynchroniserHalf':
        """SynchroniserHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2555.SynchroniserHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to SynchroniserHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_synchroniser_part(self) -> '_2556.SynchroniserPart':
        """SynchroniserPart: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2556.SynchroniserPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to SynchroniserPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_synchroniser_sleeve(self) -> '_2557.SynchroniserSleeve':
        """SynchroniserSleeve: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2557.SynchroniserSleeve.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to SynchroniserSleeve. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_torque_converter(self) -> '_2558.TorqueConverter':
        """TorqueConverter: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2558.TorqueConverter.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to TorqueConverter. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_torque_converter_pump(self) -> '_2559.TorqueConverterPump':
        """TorqueConverterPump: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2559.TorqueConverterPump.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to TorqueConverterPump. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_of_type_torque_converter_turbine(self) -> '_2561.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        if _2561.TorqueConverterTurbine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast part to TorqueConverterTurbine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_load_cases(self) -> 'List[_6854.PartLoadCase]':
        """List[PartLoadCase]: 'PartLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def clear_user_specified_excitation_data_for_all_load_cases(self):
        """ 'ClearUserSpecifiedExcitationDataForAllLoadCases' is the original name of this method."""

        self.wrapped.ClearUserSpecifiedExcitationDataForAllLoadCases()
