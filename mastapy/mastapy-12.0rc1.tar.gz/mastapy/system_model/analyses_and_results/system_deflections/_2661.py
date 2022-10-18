"""_2661.py

ComponentSystemDeflection
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import (
    _2396, _2388, _2389, _2392,
    _2394, _2399, _2400, _2404,
    _2405, _2407, _2414, _2415,
    _2416, _2418, _2421, _2423,
    _2424, _2429, _2431
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.shaft_model import _2434
from mastapy.system_model.part_model.gears import (
    _2464, _2466, _2468, _2469,
    _2470, _2472, _2474, _2476,
    _2478, _2479, _2481, _2485,
    _2487, _2489, _2491, _2494,
    _2496, _2498, _2500, _2501,
    _2502, _2504
)
from mastapy.system_model.part_model.cycloidal import _2520, _2521
from mastapy.system_model.part_model.couplings import (
    _2530, _2533, _2535, _2538,
    _2540, _2541, _2547, _2549,
    _2552, _2555, _2556, _2557,
    _2559, _2561
)
from mastapy.math_utility import _1481
from mastapy.materials.efficiency import (
    _296, _289, _291, _297,
    _287, _290
)
from mastapy.system_model.analyses_and_results.system_deflections.reporting import _2794
from mastapy.math_utility.measured_vectors import _1525, _1526
from mastapy.system_model.analyses_and_results.power_flows import (
    _4001, _3977, _3978, _3981,
    _3984, _3988, _3990, _3991,
    _3993, _3996, _3998, _4003,
    _4006, _4009, _4012, _4014,
    _4018, _4022, _4025, _4027,
    _4028, _4029, _4031, _4033,
    _4036, _4038, _4040, _4044,
    _4047, _4050, _4052, _4053,
    _4054, _4055, _4058, _4062,
    _4063, _4066, _4067, _4068,
    _4072, _4074, _4075, _4079,
    _4082, _4085, _4088, _4090,
    _4091, _4092, _4093, _4095,
    _4099, _4100, _4101, _4102,
    _4104, _4107
)
from mastapy.system_model.analyses_and_results.system_deflections import _2731
from mastapy._internal.python_net import python_net_import

_COMPONENT_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ComponentSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentSystemDeflection',)


class ComponentSystemDeflection(_2731.PartSystemDeflection):
    """ComponentSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COMPONENT_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'ComponentSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def energy_loss_during_load_case(self) -> 'float':
        """float: 'EnergyLossDuringLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EnergyLossDuringLoadCase

        if temp is None:
            return 0.0

        return temp

    @property
    def has_converged(self) -> 'bool':
        """bool: 'HasConverged' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasConverged

        if temp is None:
            return False

        return temp

    @property
    def percentage_of_iterations_converged(self) -> 'float':
        """float: 'PercentageOfIterationsConverged' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PercentageOfIterationsConverged

        if temp is None:
            return 0.0

        return temp

    @property
    def reason_for_non_convergence(self) -> 'str':
        """str: 'ReasonForNonConvergence' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReasonForNonConvergence

        if temp is None:
            return ''

        return temp

    @property
    def reason_mass_properties_are_unknown(self) -> 'str':
        """str: 'ReasonMassPropertiesAreUnknown' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReasonMassPropertiesAreUnknown

        if temp is None:
            return ''

        return temp

    @property
    def reason_mass_properties_are_zero(self) -> 'str':
        """str: 'ReasonMassPropertiesAreZero' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReasonMassPropertiesAreZero

        if temp is None:
            return ''

        return temp

    @property
    def relaxation(self) -> 'float':
        """float: 'Relaxation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Relaxation

        if temp is None:
            return 0.0

        return temp

    @property
    def speed(self) -> 'float':
        """float: 'Speed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self) -> '_2396.Component':
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
    def mass_properties_in_local_coordinate_system_from_node_model(self) -> '_1481.MassProperties':
        """MassProperties: 'MassPropertiesInLocalCoordinateSystemFromNodeModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassPropertiesInLocalCoordinateSystemFromNodeModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_loss(self) -> '_296.PowerLoss':
        """PowerLoss: 'PowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoss

        if temp is None:
            return None

        if _296.PowerLoss.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_loss to PowerLoss. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_loss_of_type_independent_power_loss(self) -> '_289.IndependentPowerLoss':
        """IndependentPowerLoss: 'PowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoss

        if temp is None:
            return None

        if _289.IndependentPowerLoss.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_loss to IndependentPowerLoss. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_loss_of_type_load_and_speed_combined_power_loss(self) -> '_291.LoadAndSpeedCombinedPowerLoss':
        """LoadAndSpeedCombinedPowerLoss: 'PowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoss

        if temp is None:
            return None

        if _291.LoadAndSpeedCombinedPowerLoss.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_loss to LoadAndSpeedCombinedPowerLoss. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def resistive_torque(self) -> '_297.ResistiveTorque':
        """ResistiveTorque: 'ResistiveTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResistiveTorque

        if temp is None:
            return None

        if _297.ResistiveTorque.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast resistive_torque to ResistiveTorque. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def resistive_torque_of_type_combined_resistive_torque(self) -> '_287.CombinedResistiveTorque':
        """CombinedResistiveTorque: 'ResistiveTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResistiveTorque

        if temp is None:
            return None

        if _287.CombinedResistiveTorque.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast resistive_torque to CombinedResistiveTorque. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def resistive_torque_of_type_independent_resistive_torque(self) -> '_290.IndependentResistiveTorque':
        """IndependentResistiveTorque: 'ResistiveTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResistiveTorque

        if temp is None:
            return None

        if _290.IndependentResistiveTorque.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast resistive_torque to IndependentResistiveTorque. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rigidly_connected_components(self) -> '_2794.RigidlyConnectedComponentGroupSystemDeflection':
        """RigidlyConnectedComponentGroupSystemDeflection: 'RigidlyConnectedComponents' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RigidlyConnectedComponents

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connected_components_forces_in_lcs(self) -> 'List[_1525.ForceResults]':
        """List[ForceResults]: 'ConnectedComponentsForcesInLCS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectedComponentsForcesInLCS

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connected_components_forces_in_wcs(self) -> 'List[_1525.ForceResults]':
        """List[ForceResults]: 'ConnectedComponentsForcesInWCS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectedComponentsForcesInWCS

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def node_results(self) -> 'List[_1526.NodeResults]':
        """List[NodeResults]: 'NodeResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_flow_results(self) -> '_4001.ComponentPowerFlow':
        """ComponentPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4001.ComponentPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ComponentPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_abstract_shaft_or_housing_power_flow(self) -> '_3977.AbstractShaftOrHousingPowerFlow':
        """AbstractShaftOrHousingPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _3977.AbstractShaftOrHousingPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to AbstractShaftOrHousingPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_abstract_shaft_power_flow(self) -> '_3978.AbstractShaftPowerFlow':
        """AbstractShaftPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _3978.AbstractShaftPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to AbstractShaftPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_agma_gleason_conical_gear_power_flow(self) -> '_3981.AGMAGleasonConicalGearPowerFlow':
        """AGMAGleasonConicalGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _3981.AGMAGleasonConicalGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to AGMAGleasonConicalGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_bearing_power_flow(self) -> '_3984.BearingPowerFlow':
        """BearingPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _3984.BearingPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to BearingPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_bevel_differential_gear_power_flow(self) -> '_3988.BevelDifferentialGearPowerFlow':
        """BevelDifferentialGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _3988.BevelDifferentialGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to BevelDifferentialGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_bevel_differential_planet_gear_power_flow(self) -> '_3990.BevelDifferentialPlanetGearPowerFlow':
        """BevelDifferentialPlanetGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _3990.BevelDifferentialPlanetGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to BevelDifferentialPlanetGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_bevel_differential_sun_gear_power_flow(self) -> '_3991.BevelDifferentialSunGearPowerFlow':
        """BevelDifferentialSunGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _3991.BevelDifferentialSunGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to BevelDifferentialSunGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_bevel_gear_power_flow(self) -> '_3993.BevelGearPowerFlow':
        """BevelGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _3993.BevelGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to BevelGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_bolt_power_flow(self) -> '_3996.BoltPowerFlow':
        """BoltPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _3996.BoltPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to BoltPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_clutch_half_power_flow(self) -> '_3998.ClutchHalfPowerFlow':
        """ClutchHalfPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _3998.ClutchHalfPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ClutchHalfPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_concept_coupling_half_power_flow(self) -> '_4003.ConceptCouplingHalfPowerFlow':
        """ConceptCouplingHalfPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4003.ConceptCouplingHalfPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ConceptCouplingHalfPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_concept_gear_power_flow(self) -> '_4006.ConceptGearPowerFlow':
        """ConceptGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4006.ConceptGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ConceptGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_conical_gear_power_flow(self) -> '_4009.ConicalGearPowerFlow':
        """ConicalGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4009.ConicalGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ConicalGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_connector_power_flow(self) -> '_4012.ConnectorPowerFlow':
        """ConnectorPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4012.ConnectorPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ConnectorPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_coupling_half_power_flow(self) -> '_4014.CouplingHalfPowerFlow':
        """CouplingHalfPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4014.CouplingHalfPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to CouplingHalfPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_cvt_pulley_power_flow(self) -> '_4018.CVTPulleyPowerFlow':
        """CVTPulleyPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4018.CVTPulleyPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to CVTPulleyPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_cycloidal_disc_power_flow(self) -> '_4022.CycloidalDiscPowerFlow':
        """CycloidalDiscPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4022.CycloidalDiscPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to CycloidalDiscPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_cylindrical_gear_power_flow(self) -> '_4025.CylindricalGearPowerFlow':
        """CylindricalGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4025.CylindricalGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to CylindricalGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_cylindrical_planet_gear_power_flow(self) -> '_4027.CylindricalPlanetGearPowerFlow':
        """CylindricalPlanetGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4027.CylindricalPlanetGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to CylindricalPlanetGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_datum_power_flow(self) -> '_4028.DatumPowerFlow':
        """DatumPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4028.DatumPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to DatumPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_external_cad_model_power_flow(self) -> '_4029.ExternalCADModelPowerFlow':
        """ExternalCADModelPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4029.ExternalCADModelPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ExternalCADModelPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_face_gear_power_flow(self) -> '_4031.FaceGearPowerFlow':
        """FaceGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4031.FaceGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to FaceGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_fe_part_power_flow(self) -> '_4033.FEPartPowerFlow':
        """FEPartPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4033.FEPartPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to FEPartPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_gear_power_flow(self) -> '_4036.GearPowerFlow':
        """GearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4036.GearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to GearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_guide_dxf_model_power_flow(self) -> '_4038.GuideDxfModelPowerFlow':
        """GuideDxfModelPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4038.GuideDxfModelPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to GuideDxfModelPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_hypoid_gear_power_flow(self) -> '_4040.HypoidGearPowerFlow':
        """HypoidGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4040.HypoidGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to HypoidGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_klingelnberg_cyclo_palloid_conical_gear_power_flow(self) -> '_4044.KlingelnbergCycloPalloidConicalGearPowerFlow':
        """KlingelnbergCycloPalloidConicalGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4044.KlingelnbergCycloPalloidConicalGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to KlingelnbergCycloPalloidConicalGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_klingelnberg_cyclo_palloid_hypoid_gear_power_flow(self) -> '_4047.KlingelnbergCycloPalloidHypoidGearPowerFlow':
        """KlingelnbergCycloPalloidHypoidGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4047.KlingelnbergCycloPalloidHypoidGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to KlingelnbergCycloPalloidHypoidGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(self) -> '_4050.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow':
        """KlingelnbergCycloPalloidSpiralBevelGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4050.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to KlingelnbergCycloPalloidSpiralBevelGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_mass_disc_power_flow(self) -> '_4052.MassDiscPowerFlow':
        """MassDiscPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4052.MassDiscPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to MassDiscPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_measurement_component_power_flow(self) -> '_4053.MeasurementComponentPowerFlow':
        """MeasurementComponentPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4053.MeasurementComponentPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to MeasurementComponentPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_mountable_component_power_flow(self) -> '_4054.MountableComponentPowerFlow':
        """MountableComponentPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4054.MountableComponentPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to MountableComponentPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_oil_seal_power_flow(self) -> '_4055.OilSealPowerFlow':
        """OilSealPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4055.OilSealPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to OilSealPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_part_to_part_shear_coupling_half_power_flow(self) -> '_4058.PartToPartShearCouplingHalfPowerFlow':
        """PartToPartShearCouplingHalfPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4058.PartToPartShearCouplingHalfPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to PartToPartShearCouplingHalfPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_planet_carrier_power_flow(self) -> '_4062.PlanetCarrierPowerFlow':
        """PlanetCarrierPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4062.PlanetCarrierPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to PlanetCarrierPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_point_load_power_flow(self) -> '_4063.PointLoadPowerFlow':
        """PointLoadPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4063.PointLoadPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to PointLoadPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_power_load_power_flow(self) -> '_4066.PowerLoadPowerFlow':
        """PowerLoadPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4066.PowerLoadPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to PowerLoadPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_pulley_power_flow(self) -> '_4067.PulleyPowerFlow':
        """PulleyPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4067.PulleyPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to PulleyPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_ring_pins_power_flow(self) -> '_4068.RingPinsPowerFlow':
        """RingPinsPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4068.RingPinsPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to RingPinsPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_rolling_ring_power_flow(self) -> '_4072.RollingRingPowerFlow':
        """RollingRingPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4072.RollingRingPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to RollingRingPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_shaft_hub_connection_power_flow(self) -> '_4074.ShaftHubConnectionPowerFlow':
        """ShaftHubConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4074.ShaftHubConnectionPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ShaftHubConnectionPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_shaft_power_flow(self) -> '_4075.ShaftPowerFlow':
        """ShaftPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4075.ShaftPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ShaftPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_spiral_bevel_gear_power_flow(self) -> '_4079.SpiralBevelGearPowerFlow':
        """SpiralBevelGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4079.SpiralBevelGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to SpiralBevelGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_spring_damper_half_power_flow(self) -> '_4082.SpringDamperHalfPowerFlow':
        """SpringDamperHalfPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4082.SpringDamperHalfPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to SpringDamperHalfPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_straight_bevel_diff_gear_power_flow(self) -> '_4085.StraightBevelDiffGearPowerFlow':
        """StraightBevelDiffGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4085.StraightBevelDiffGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to StraightBevelDiffGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_straight_bevel_gear_power_flow(self) -> '_4088.StraightBevelGearPowerFlow':
        """StraightBevelGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4088.StraightBevelGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to StraightBevelGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_straight_bevel_planet_gear_power_flow(self) -> '_4090.StraightBevelPlanetGearPowerFlow':
        """StraightBevelPlanetGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4090.StraightBevelPlanetGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to StraightBevelPlanetGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_straight_bevel_sun_gear_power_flow(self) -> '_4091.StraightBevelSunGearPowerFlow':
        """StraightBevelSunGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4091.StraightBevelSunGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to StraightBevelSunGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_synchroniser_half_power_flow(self) -> '_4092.SynchroniserHalfPowerFlow':
        """SynchroniserHalfPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4092.SynchroniserHalfPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to SynchroniserHalfPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_synchroniser_part_power_flow(self) -> '_4093.SynchroniserPartPowerFlow':
        """SynchroniserPartPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4093.SynchroniserPartPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to SynchroniserPartPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_synchroniser_sleeve_power_flow(self) -> '_4095.SynchroniserSleevePowerFlow':
        """SynchroniserSleevePowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4095.SynchroniserSleevePowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to SynchroniserSleevePowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_torque_converter_pump_power_flow(self) -> '_4099.TorqueConverterPumpPowerFlow':
        """TorqueConverterPumpPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4099.TorqueConverterPumpPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to TorqueConverterPumpPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_torque_converter_turbine_power_flow(self) -> '_4100.TorqueConverterTurbinePowerFlow':
        """TorqueConverterTurbinePowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4100.TorqueConverterTurbinePowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to TorqueConverterTurbinePowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_unbalanced_mass_power_flow(self) -> '_4101.UnbalancedMassPowerFlow':
        """UnbalancedMassPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4101.UnbalancedMassPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to UnbalancedMassPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_virtual_component_power_flow(self) -> '_4102.VirtualComponentPowerFlow':
        """VirtualComponentPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4102.VirtualComponentPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to VirtualComponentPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_worm_gear_power_flow(self) -> '_4104.WormGearPowerFlow':
        """WormGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4104.WormGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to WormGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_zerol_bevel_gear_power_flow(self) -> '_4107.ZerolBevelGearPowerFlow':
        """ZerolBevelGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4107.ZerolBevelGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ZerolBevelGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
