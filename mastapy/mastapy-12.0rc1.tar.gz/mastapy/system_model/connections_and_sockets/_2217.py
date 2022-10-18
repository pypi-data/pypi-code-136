"""_2217.py

AbstractShaftToMountableComponentConnection
"""


from mastapy.system_model.part_model import (
    _2416, _2392, _2399, _2414,
    _2415, _2418, _2421, _2423,
    _2424, _2429, _2431, _2388
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.gears import (
    _2464, _2466, _2468, _2469,
    _2470, _2472, _2474, _2476,
    _2478, _2479, _2481, _2485,
    _2487, _2489, _2491, _2494,
    _2496, _2498, _2500, _2501,
    _2502, _2504
)
from mastapy.system_model.part_model.cycloidal import _2521, _2520
from mastapy.system_model.part_model.couplings import (
    _2530, _2533, _2535, _2538,
    _2540, _2541, _2547, _2549,
    _2552, _2555, _2556, _2557,
    _2559, _2561
)
from mastapy.system_model.part_model.shaft_model import _2434
from mastapy.system_model.connections_and_sockets import _2224
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'AbstractShaftToMountableComponentConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnection',)


class AbstractShaftToMountableComponentConnection(_2224.Connection):
    """AbstractShaftToMountableComponentConnection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mountable_component(self) -> '_2416.MountableComponent':
        """MountableComponent: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2416.MountableComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to MountableComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_bearing(self) -> '_2392.Bearing':
        """Bearing: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2392.Bearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to Bearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_connector(self) -> '_2399.Connector':
        """Connector: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2399.Connector.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to Connector. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_mass_disc(self) -> '_2414.MassDisc':
        """MassDisc: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2414.MassDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to MassDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_measurement_component(self) -> '_2415.MeasurementComponent':
        """MeasurementComponent: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2415.MeasurementComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to MeasurementComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_oil_seal(self) -> '_2418.OilSeal':
        """OilSeal: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2418.OilSeal.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to OilSeal. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_planet_carrier(self) -> '_2421.PlanetCarrier':
        """PlanetCarrier: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2421.PlanetCarrier.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to PlanetCarrier. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_point_load(self) -> '_2423.PointLoad':
        """PointLoad: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2423.PointLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to PointLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_power_load(self) -> '_2424.PowerLoad':
        """PowerLoad: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2424.PowerLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to PowerLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_unbalanced_mass(self) -> '_2429.UnbalancedMass':
        """UnbalancedMass: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2429.UnbalancedMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to UnbalancedMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_virtual_component(self) -> '_2431.VirtualComponent':
        """VirtualComponent: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2431.VirtualComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to VirtualComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_agma_gleason_conical_gear(self) -> '_2464.AGMAGleasonConicalGear':
        """AGMAGleasonConicalGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2464.AGMAGleasonConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to AGMAGleasonConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_bevel_differential_gear(self) -> '_2466.BevelDifferentialGear':
        """BevelDifferentialGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2466.BevelDifferentialGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to BevelDifferentialGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_bevel_differential_planet_gear(self) -> '_2468.BevelDifferentialPlanetGear':
        """BevelDifferentialPlanetGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2468.BevelDifferentialPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to BevelDifferentialPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_bevel_differential_sun_gear(self) -> '_2469.BevelDifferentialSunGear':
        """BevelDifferentialSunGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2469.BevelDifferentialSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to BevelDifferentialSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_bevel_gear(self) -> '_2470.BevelGear':
        """BevelGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2470.BevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to BevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_concept_gear(self) -> '_2472.ConceptGear':
        """ConceptGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2472.ConceptGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to ConceptGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_conical_gear(self) -> '_2474.ConicalGear':
        """ConicalGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2474.ConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to ConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_cylindrical_gear(self) -> '_2476.CylindricalGear':
        """CylindricalGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2476.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_cylindrical_planet_gear(self) -> '_2478.CylindricalPlanetGear':
        """CylindricalPlanetGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2478.CylindricalPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to CylindricalPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_face_gear(self) -> '_2479.FaceGear':
        """FaceGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2479.FaceGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to FaceGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_gear(self) -> '_2481.Gear':
        """Gear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2481.Gear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to Gear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_hypoid_gear(self) -> '_2485.HypoidGear':
        """HypoidGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2485.HypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to HypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2487.KlingelnbergCycloPalloidConicalGear':
        """KlingelnbergCycloPalloidConicalGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2487.KlingelnbergCycloPalloidConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2489.KlingelnbergCycloPalloidHypoidGear':
        """KlingelnbergCycloPalloidHypoidGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2489.KlingelnbergCycloPalloidHypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2491.KlingelnbergCycloPalloidSpiralBevelGear':
        """KlingelnbergCycloPalloidSpiralBevelGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2491.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_spiral_bevel_gear(self) -> '_2494.SpiralBevelGear':
        """SpiralBevelGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2494.SpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to SpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_straight_bevel_diff_gear(self) -> '_2496.StraightBevelDiffGear':
        """StraightBevelDiffGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2496.StraightBevelDiffGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to StraightBevelDiffGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_straight_bevel_gear(self) -> '_2498.StraightBevelGear':
        """StraightBevelGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2498.StraightBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to StraightBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_straight_bevel_planet_gear(self) -> '_2500.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2500.StraightBevelPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to StraightBevelPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_straight_bevel_sun_gear(self) -> '_2501.StraightBevelSunGear':
        """StraightBevelSunGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2501.StraightBevelSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to StraightBevelSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_worm_gear(self) -> '_2502.WormGear':
        """WormGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2502.WormGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to WormGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_zerol_bevel_gear(self) -> '_2504.ZerolBevelGear':
        """ZerolBevelGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2504.ZerolBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to ZerolBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_ring_pins(self) -> '_2521.RingPins':
        """RingPins: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2521.RingPins.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to RingPins. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_clutch_half(self) -> '_2530.ClutchHalf':
        """ClutchHalf: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2530.ClutchHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to ClutchHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_concept_coupling_half(self) -> '_2533.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2533.ConceptCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to ConceptCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_coupling_half(self) -> '_2535.CouplingHalf':
        """CouplingHalf: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2535.CouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to CouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_cvt_pulley(self) -> '_2538.CVTPulley':
        """CVTPulley: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2538.CVTPulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to CVTPulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_part_to_part_shear_coupling_half(self) -> '_2540.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2540.PartToPartShearCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to PartToPartShearCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_pulley(self) -> '_2541.Pulley':
        """Pulley: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2541.Pulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to Pulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_rolling_ring(self) -> '_2547.RollingRing':
        """RollingRing: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2547.RollingRing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to RollingRing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_shaft_hub_connection(self) -> '_2549.ShaftHubConnection':
        """ShaftHubConnection: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2549.ShaftHubConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to ShaftHubConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_spring_damper_half(self) -> '_2552.SpringDamperHalf':
        """SpringDamperHalf: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2552.SpringDamperHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to SpringDamperHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_synchroniser_half(self) -> '_2555.SynchroniserHalf':
        """SynchroniserHalf: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2555.SynchroniserHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to SynchroniserHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_synchroniser_part(self) -> '_2556.SynchroniserPart':
        """SynchroniserPart: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2556.SynchroniserPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to SynchroniserPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_synchroniser_sleeve(self) -> '_2557.SynchroniserSleeve':
        """SynchroniserSleeve: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2557.SynchroniserSleeve.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to SynchroniserSleeve. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_torque_converter_pump(self) -> '_2559.TorqueConverterPump':
        """TorqueConverterPump: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2559.TorqueConverterPump.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to TorqueConverterPump. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mountable_component_of_type_torque_converter_turbine(self) -> '_2561.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        if _2561.TorqueConverterTurbine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to TorqueConverterTurbine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft(self) -> '_2388.AbstractShaft':
        """AbstractShaft: 'Shaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shaft

        if temp is None:
            return None

        if _2388.AbstractShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast shaft to AbstractShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_of_type_shaft(self) -> '_2434.Shaft':
        """Shaft: 'Shaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shaft

        if temp is None:
            return None

        if _2434.Shaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast shaft to Shaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_of_type_cycloidal_disc(self) -> '_2520.CycloidalDisc':
        """CycloidalDisc: 'Shaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shaft

        if temp is None:
            return None

        if _2520.CycloidalDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast shaft to CycloidalDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
