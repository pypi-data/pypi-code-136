"""_2626.py

CompoundMultibodyDynamicsAnalysis
"""


from typing import Iterable

from mastapy.system_model.connections_and_sockets.couplings import (
    _2302, _2304, _2300, _2294,
    _2296, _2298
)
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
    _5568, _5583, _5466, _5465,
    _5467, _5473, _5484, _5485,
    _5490, _5501, _5516, _5517,
    _5521, _5522, _5472, _5526,
    _5540, _5541, _5542, _5543,
    _5544, _5550, _5551, _5552,
    _5559, _5563, _5586, _5587,
    _5560, _5494, _5496, _5518,
    _5520, _5469, _5471, _5476,
    _5478, _5479, _5480, _5481,
    _5483, _5497, _5499, _5512,
    _5514, _5515, _5523, _5525,
    _5527, _5529, _5531, _5533,
    _5534, _5536, _5537, _5539,
    _5549, _5564, _5566, _5570,
    _5572, _5573, _5575, _5576,
    _5577, _5588, _5590, _5591,
    _5593, _5508, _5510, _5554,
    _5545, _5547, _5475, _5486,
    _5488, _5491, _5493, _5502,
    _5504, _5506, _5507, _5553,
    _5561, _5557, _5556, _5567,
    _5569, _5578, _5579, _5580,
    _5581, _5582, _5584, _5585,
    _5562, _5505, _5474, _5489,
    _5500, _5530, _5548, _5558,
    _5468, _5477, _5495, _5519,
    _5571, _5482, _5498, _5470,
    _5513, _5528, _5532, _5535,
    _5538, _5565, _5574, _5589,
    _5592, _5524, _5509, _5511,
    _5555, _5546, _5487, _5492,
    _5503
)
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import (
    _2388, _2387, _2389, _2392,
    _2394, _2395, _2396, _2399,
    _2400, _2404, _2405, _2406,
    _2386, _2407, _2414, _2415,
    _2416, _2418, _2420, _2421,
    _2423, _2424, _2426, _2428,
    _2429, _2431
)
from mastapy.system_model.part_model.shaft_model import _2434
from mastapy.system_model.part_model.gears import (
    _2472, _2473, _2479, _2480,
    _2464, _2465, _2466, _2467,
    _2468, _2469, _2470, _2471,
    _2474, _2475, _2476, _2477,
    _2478, _2481, _2483, _2485,
    _2486, _2487, _2488, _2489,
    _2490, _2491, _2492, _2493,
    _2494, _2495, _2496, _2497,
    _2498, _2499, _2500, _2501,
    _2502, _2503, _2504, _2505
)
from mastapy.system_model.part_model.cycloidal import _2519, _2520, _2521
from mastapy.system_model.part_model.couplings import (
    _2539, _2540, _2527, _2529,
    _2530, _2532, _2533, _2534,
    _2535, _2537, _2538, _2541,
    _2549, _2547, _2548, _2551,
    _2552, _2553, _2555, _2556,
    _2557, _2558, _2559, _2561
)
from mastapy.system_model.connections_and_sockets import (
    _2247, _2225, _2220, _2221,
    _2224, _2233, _2239, _2244,
    _2217
)
from mastapy.system_model.connections_and_sockets.gears import (
    _2253, _2257, _2263, _2277,
    _2255, _2259, _2251, _2261,
    _2267, _2270, _2271, _2272,
    _2275, _2279, _2281, _2283,
    _2265
)
from mastapy.system_model.connections_and_sockets.cycloidal import _2287, _2290, _2293
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results import _2570

_SPRING_DAMPER_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'SpringDamperConnection')
_TORQUE_CONVERTER_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'TorqueConverterConnection')
_PART_TO_PART_SHEAR_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'PartToPartShearCouplingConnection')
_CLUTCH_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'ClutchConnection')
_CONCEPT_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'ConceptCouplingConnection')
_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'CouplingConnection')
_ABSTRACT_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractShaft')
_ABSTRACT_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractAssembly')
_ABSTRACT_SHAFT_OR_HOUSING = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractShaftOrHousing')
_BEARING = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bearing')
_BOLT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bolt')
_BOLTED_JOINT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'BoltedJoint')
_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Component')
_CONNECTOR = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Connector')
_DATUM = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Datum')
_EXTERNAL_CAD_MODEL = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'ExternalCADModel')
_FE_PART = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'FEPart')
_FLEXIBLE_PIN_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'FlexiblePinAssembly')
_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Assembly')
_GUIDE_DXF_MODEL = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'GuideDxfModel')
_MASS_DISC = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MassDisc')
_MEASUREMENT_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MeasurementComponent')
_MOUNTABLE_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MountableComponent')
_OIL_SEAL = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'OilSeal')
_PART = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Part')
_PLANET_CARRIER = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PlanetCarrier')
_POINT_LOAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PointLoad')
_POWER_LOAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PowerLoad')
_ROOT_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'RootAssembly')
_SPECIALISED_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'SpecialisedAssembly')
_UNBALANCED_MASS = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'UnbalancedMass')
_VIRTUAL_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'VirtualComponent')
_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ShaftModel', 'Shaft')
_CONCEPT_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConceptGear')
_CONCEPT_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConceptGearSet')
_FACE_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'FaceGear')
_FACE_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'FaceGearSet')
_AGMA_GLEASON_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'AGMAGleasonConicalGear')
_AGMA_GLEASON_CONICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'AGMAGleasonConicalGearSet')
_BEVEL_DIFFERENTIAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialGear')
_BEVEL_DIFFERENTIAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialGearSet')
_BEVEL_DIFFERENTIAL_PLANET_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialPlanetGear')
_BEVEL_DIFFERENTIAL_SUN_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialSunGear')
_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelGear')
_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelGearSet')
_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGear')
_CONICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGearSet')
_CYLINDRICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalGear')
_CYLINDRICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalGearSet')
_CYLINDRICAL_PLANET_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalPlanetGear')
_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'Gear')
_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'GearSet')
_HYPOID_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'HypoidGear')
_HYPOID_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'HypoidGearSet')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidConicalGear')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidConicalGearSet')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidHypoidGear')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidHypoidGearSet')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidSpiralBevelGear')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidSpiralBevelGearSet')
_PLANETARY_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'PlanetaryGearSet')
_SPIRAL_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'SpiralBevelGear')
_SPIRAL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'SpiralBevelGearSet')
_STRAIGHT_BEVEL_DIFF_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelDiffGear')
_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelDiffGearSet')
_STRAIGHT_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelGear')
_STRAIGHT_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelGearSet')
_STRAIGHT_BEVEL_PLANET_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelPlanetGear')
_STRAIGHT_BEVEL_SUN_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelSunGear')
_WORM_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'WormGear')
_WORM_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'WormGearSet')
_ZEROL_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ZerolBevelGear')
_ZEROL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ZerolBevelGearSet')
_CYCLOIDAL_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Cycloidal', 'CycloidalAssembly')
_CYCLOIDAL_DISC = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Cycloidal', 'CycloidalDisc')
_RING_PINS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Cycloidal', 'RingPins')
_PART_TO_PART_SHEAR_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'PartToPartShearCoupling')
_PART_TO_PART_SHEAR_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'PartToPartShearCouplingHalf')
_BELT_DRIVE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'BeltDrive')
_CLUTCH = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Clutch')
_CLUTCH_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ClutchHalf')
_CONCEPT_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ConceptCoupling')
_CONCEPT_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ConceptCouplingHalf')
_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Coupling')
_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CouplingHalf')
_CVT = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CVT')
_CVT_PULLEY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CVTPulley')
_PULLEY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Pulley')
_SHAFT_HUB_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ShaftHubConnection')
_ROLLING_RING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'RollingRing')
_ROLLING_RING_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'RollingRingAssembly')
_SPRING_DAMPER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SpringDamper')
_SPRING_DAMPER_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SpringDamperHalf')
_SYNCHRONISER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Synchroniser')
_SYNCHRONISER_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserHalf')
_SYNCHRONISER_PART = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserPart')
_SYNCHRONISER_SLEEVE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserSleeve')
_TORQUE_CONVERTER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverter')
_TORQUE_CONVERTER_PUMP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverterPump')
_TORQUE_CONVERTER_TURBINE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverterTurbine')
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'ShaftToMountableComponentConnection')
_CVT_BELT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'CVTBeltConnection')
_BELT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'BeltConnection')
_COAXIAL_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'CoaxialConnection')
_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'Connection')
_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'InterMountableComponentConnection')
_PLANETARY_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'PlanetaryConnection')
_ROLLING_RING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'RollingRingConnection')
_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'AbstractShaftToMountableComponentConnection')
_BEVEL_DIFFERENTIAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'BevelDifferentialGearMesh')
_CONCEPT_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ConceptGearMesh')
_FACE_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'FaceGearMesh')
_STRAIGHT_BEVEL_DIFF_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'StraightBevelDiffGearMesh')
_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'BevelGearMesh')
_CONICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ConicalGearMesh')
_AGMA_GLEASON_CONICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'AGMAGleasonConicalGearMesh')
_CYLINDRICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'CylindricalGearMesh')
_HYPOID_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'HypoidGearMesh')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergCycloPalloidConicalGearMesh')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergCycloPalloidHypoidGearMesh')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergCycloPalloidSpiralBevelGearMesh')
_SPIRAL_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'SpiralBevelGearMesh')
_STRAIGHT_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'StraightBevelGearMesh')
_WORM_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'WormGearMesh')
_ZEROL_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ZerolBevelGearMesh')
_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'GearMesh')
_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal', 'CycloidalDiscCentralBearingConnection')
_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal', 'CycloidalDiscPlanetaryBearingConnection')
_RING_PINS_TO_DISC_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal', 'RingPinsToDiscConnection')
_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundMultibodyDynamicsAnalysis',)


class CompoundMultibodyDynamicsAnalysis(_2570.CompoundAnalysis):
    """CompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    def __init__(self, instance_to_wrap: 'CompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def results_for_spring_damper_connection(self, design_entity: '_2302.SpringDamperConnection') -> 'Iterable[_5568.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_torque_converter_connection(self, design_entity: '_2304.TorqueConverterConnection') -> 'Iterable[_5583.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_abstract_shaft(self, design_entity: '_2388.AbstractShaft') -> 'Iterable[_5466.AbstractShaftCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AbstractShaftCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT](design_entity.wrapped if design_entity else None))

    def results_for_abstract_assembly(self, design_entity: '_2387.AbstractAssembly') -> 'Iterable[_5465.AbstractAssemblyCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AbstractAssemblyCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY](design_entity.wrapped if design_entity else None))

    def results_for_abstract_shaft_or_housing(self, design_entity: '_2389.AbstractShaftOrHousing') -> 'Iterable[_5467.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](design_entity.wrapped if design_entity else None))

    def results_for_bearing(self, design_entity: '_2392.Bearing') -> 'Iterable[_5473.BearingCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BearingCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEARING](design_entity.wrapped if design_entity else None))

    def results_for_bolt(self, design_entity: '_2394.Bolt') -> 'Iterable[_5484.BoltCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BoltCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BOLT](design_entity.wrapped if design_entity else None))

    def results_for_bolted_joint(self, design_entity: '_2395.BoltedJoint') -> 'Iterable[_5485.BoltedJointCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BoltedJointCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT](design_entity.wrapped if design_entity else None))

    def results_for_component(self, design_entity: '_2396.Component') -> 'Iterable[_5490.ComponentCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ComponentCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COMPONENT](design_entity.wrapped if design_entity else None))

    def results_for_connector(self, design_entity: '_2399.Connector') -> 'Iterable[_5501.ConnectorCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConnectorCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONNECTOR](design_entity.wrapped if design_entity else None))

    def results_for_datum(self, design_entity: '_2400.Datum') -> 'Iterable[_5516.DatumCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.DatumCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_DATUM](design_entity.wrapped if design_entity else None))

    def results_for_external_cad_model(self, design_entity: '_2404.ExternalCADModel') -> 'Iterable[_5517.ExternalCADModelCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ExternalCADModelCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL](design_entity.wrapped if design_entity else None))

    def results_for_fe_part(self, design_entity: '_2405.FEPart') -> 'Iterable[_5521.FEPartCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FEPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FEPartCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FE_PART](design_entity.wrapped if design_entity else None))

    def results_for_flexible_pin_assembly(self, design_entity: '_2406.FlexiblePinAssembly') -> 'Iterable[_5522.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](design_entity.wrapped if design_entity else None))

    def results_for_assembly(self, design_entity: '_2386.Assembly') -> 'Iterable[_5472.AssemblyCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AssemblyCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ASSEMBLY](design_entity.wrapped if design_entity else None))

    def results_for_guide_dxf_model(self, design_entity: '_2407.GuideDxfModel') -> 'Iterable[_5526.GuideDxfModelCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.GuideDxfModelCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL](design_entity.wrapped if design_entity else None))

    def results_for_mass_disc(self, design_entity: '_2414.MassDisc') -> 'Iterable[_5540.MassDiscCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.MassDiscCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_MASS_DISC](design_entity.wrapped if design_entity else None))

    def results_for_measurement_component(self, design_entity: '_2415.MeasurementComponent') -> 'Iterable[_5541.MeasurementComponentCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.MeasurementComponentCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT](design_entity.wrapped if design_entity else None))

    def results_for_mountable_component(self, design_entity: '_2416.MountableComponent') -> 'Iterable[_5542.MountableComponentCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.MountableComponentCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT](design_entity.wrapped if design_entity else None))

    def results_for_oil_seal(self, design_entity: '_2418.OilSeal') -> 'Iterable[_5543.OilSealCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.OilSealCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_OIL_SEAL](design_entity.wrapped if design_entity else None))

    def results_for_part(self, design_entity: '_2420.Part') -> 'Iterable[_5544.PartCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PartCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART](design_entity.wrapped if design_entity else None))

    def results_for_planet_carrier(self, design_entity: '_2421.PlanetCarrier') -> 'Iterable[_5550.PlanetCarrierCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PlanetCarrierCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER](design_entity.wrapped if design_entity else None))

    def results_for_point_load(self, design_entity: '_2423.PointLoad') -> 'Iterable[_5551.PointLoadCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PointLoadCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_POINT_LOAD](design_entity.wrapped if design_entity else None))

    def results_for_power_load(self, design_entity: '_2424.PowerLoad') -> 'Iterable[_5552.PowerLoadCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PowerLoadCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_POWER_LOAD](design_entity.wrapped if design_entity else None))

    def results_for_root_assembly(self, design_entity: '_2426.RootAssembly') -> 'Iterable[_5559.RootAssemblyCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RootAssemblyCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY](design_entity.wrapped if design_entity else None))

    def results_for_specialised_assembly(self, design_entity: '_2428.SpecialisedAssembly') -> 'Iterable[_5563.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY](design_entity.wrapped if design_entity else None))

    def results_for_unbalanced_mass(self, design_entity: '_2429.UnbalancedMass') -> 'Iterable[_5586.UnbalancedMassCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.UnbalancedMassCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS](design_entity.wrapped if design_entity else None))

    def results_for_virtual_component(self, design_entity: '_2431.VirtualComponent') -> 'Iterable[_5587.VirtualComponentCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.VirtualComponentCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT](design_entity.wrapped if design_entity else None))

    def results_for_shaft(self, design_entity: '_2434.Shaft') -> 'Iterable[_5560.ShaftCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ShaftCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SHAFT](design_entity.wrapped if design_entity else None))

    def results_for_concept_gear(self, design_entity: '_2472.ConceptGear') -> 'Iterable[_5494.ConceptGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_concept_gear_set(self, design_entity: '_2473.ConceptGearSet') -> 'Iterable[_5496.ConceptGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_face_gear(self, design_entity: '_2479.FaceGear') -> 'Iterable[_5518.FaceGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FaceGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FACE_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_face_gear_set(self, design_entity: '_2480.FaceGearSet') -> 'Iterable[_5520.FaceGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FaceGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2464.AGMAGleasonConicalGear') -> 'Iterable[_5469.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2465.AGMAGleasonConicalGearSet') -> 'Iterable[_5471.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_bevel_differential_gear(self, design_entity: '_2466.BevelDifferentialGear') -> 'Iterable[_5476.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_bevel_differential_gear_set(self, design_entity: '_2467.BevelDifferentialGearSet') -> 'Iterable[_5478.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2468.BevelDifferentialPlanetGear') -> 'Iterable[_5479.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_PLANET_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2469.BevelDifferentialSunGear') -> 'Iterable[_5480.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_bevel_gear(self, design_entity: '_2470.BevelGear') -> 'Iterable[_5481.BevelGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_bevel_gear_set(self, design_entity: '_2471.BevelGearSet') -> 'Iterable[_5483.BevelGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_conical_gear(self, design_entity: '_2474.ConicalGear') -> 'Iterable[_5497.ConicalGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConicalGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_conical_gear_set(self, design_entity: '_2475.ConicalGearSet') -> 'Iterable[_5499.ConicalGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConicalGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_cylindrical_gear(self, design_entity: '_2476.CylindricalGear') -> 'Iterable[_5512.CylindricalGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CylindricalGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_cylindrical_gear_set(self, design_entity: '_2477.CylindricalGearSet') -> 'Iterable[_5514.CylindricalGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CylindricalGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_cylindrical_planet_gear(self, design_entity: '_2478.CylindricalPlanetGear') -> 'Iterable[_5515.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_gear(self, design_entity: '_2481.Gear') -> 'Iterable[_5523.GearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.GearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_gear_set(self, design_entity: '_2483.GearSet') -> 'Iterable[_5525.GearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.GearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_hypoid_gear(self, design_entity: '_2485.HypoidGear') -> 'Iterable[_5527.HypoidGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.HypoidGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_hypoid_gear_set(self, design_entity: '_2486.HypoidGearSet') -> 'Iterable[_5529.HypoidGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.HypoidGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2487.KlingelnbergCycloPalloidConicalGear') -> 'Iterable[_5531.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2488.KlingelnbergCycloPalloidConicalGearSet') -> 'Iterable[_5533.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2489.KlingelnbergCycloPalloidHypoidGear') -> 'Iterable[_5534.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2490.KlingelnbergCycloPalloidHypoidGearSet') -> 'Iterable[_5536.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2491.KlingelnbergCycloPalloidSpiralBevelGear') -> 'Iterable[_5537.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2492.KlingelnbergCycloPalloidSpiralBevelGearSet') -> 'Iterable[_5539.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_planetary_gear_set(self, design_entity: '_2493.PlanetaryGearSet') -> 'Iterable[_5549.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_spiral_bevel_gear(self, design_entity: '_2494.SpiralBevelGear') -> 'Iterable[_5564.SpiralBevelGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpiralBevelGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2495.SpiralBevelGearSet') -> 'Iterable[_5566.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2496.StraightBevelDiffGear') -> 'Iterable[_5570.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2497.StraightBevelDiffGearSet') -> 'Iterable[_5572.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_gear(self, design_entity: '_2498.StraightBevelGear') -> 'Iterable[_5573.StraightBevelGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_gear_set(self, design_entity: '_2499.StraightBevelGearSet') -> 'Iterable[_5575.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2500.StraightBevelPlanetGear') -> 'Iterable[_5576.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2501.StraightBevelSunGear') -> 'Iterable[_5577.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_worm_gear(self, design_entity: '_2502.WormGear') -> 'Iterable[_5588.WormGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.WormGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_WORM_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_worm_gear_set(self, design_entity: '_2503.WormGearSet') -> 'Iterable[_5590.WormGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.WormGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_zerol_bevel_gear(self, design_entity: '_2504.ZerolBevelGear') -> 'Iterable[_5591.ZerolBevelGearCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ZerolBevelGearCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2505.ZerolBevelGearSet') -> 'Iterable[_5593.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_cycloidal_assembly(self, design_entity: '_2519.CycloidalAssembly') -> 'Iterable[_5508.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_ASSEMBLY](design_entity.wrapped if design_entity else None))

    def results_for_cycloidal_disc(self, design_entity: '_2520.CycloidalDisc') -> 'Iterable[_5510.CycloidalDiscCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CycloidalDiscCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC](design_entity.wrapped if design_entity else None))

    def results_for_ring_pins(self, design_entity: '_2521.RingPins') -> 'Iterable[_5554.RingPinsCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.RingPins)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RingPinsCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_RING_PINS](design_entity.wrapped if design_entity else None))

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2539.PartToPartShearCoupling') -> 'Iterable[_5545.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](design_entity.wrapped if design_entity else None))

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2540.PartToPartShearCouplingHalf') -> 'Iterable[_5547.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_HALF](design_entity.wrapped if design_entity else None))

    def results_for_belt_drive(self, design_entity: '_2527.BeltDrive') -> 'Iterable[_5475.BeltDriveCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BeltDriveCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BELT_DRIVE](design_entity.wrapped if design_entity else None))

    def results_for_clutch(self, design_entity: '_2529.Clutch') -> 'Iterable[_5486.ClutchCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ClutchCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CLUTCH](design_entity.wrapped if design_entity else None))

    def results_for_clutch_half(self, design_entity: '_2530.ClutchHalf') -> 'Iterable[_5488.ClutchHalfCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ClutchHalfCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF](design_entity.wrapped if design_entity else None))

    def results_for_concept_coupling(self, design_entity: '_2532.ConceptCoupling') -> 'Iterable[_5491.ConceptCouplingCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptCouplingCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING](design_entity.wrapped if design_entity else None))

    def results_for_concept_coupling_half(self, design_entity: '_2533.ConceptCouplingHalf') -> 'Iterable[_5493.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF](design_entity.wrapped if design_entity else None))

    def results_for_coupling(self, design_entity: '_2534.Coupling') -> 'Iterable[_5502.CouplingCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CouplingCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COUPLING](design_entity.wrapped if design_entity else None))

    def results_for_coupling_half(self, design_entity: '_2535.CouplingHalf') -> 'Iterable[_5504.CouplingHalfCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CouplingHalfCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COUPLING_HALF](design_entity.wrapped if design_entity else None))

    def results_for_cvt(self, design_entity: '_2537.CVT') -> 'Iterable[_5506.CVTCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CVTCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CVT](design_entity.wrapped if design_entity else None))

    def results_for_cvt_pulley(self, design_entity: '_2538.CVTPulley') -> 'Iterable[_5507.CVTPulleyCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CVTPulleyCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CVT_PULLEY](design_entity.wrapped if design_entity else None))

    def results_for_pulley(self, design_entity: '_2541.Pulley') -> 'Iterable[_5553.PulleyCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PulleyCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PULLEY](design_entity.wrapped if design_entity else None))

    def results_for_shaft_hub_connection(self, design_entity: '_2549.ShaftHubConnection') -> 'Iterable[_5561.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_rolling_ring(self, design_entity: '_2547.RollingRing') -> 'Iterable[_5557.RollingRingCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RollingRingCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROLLING_RING](design_entity.wrapped if design_entity else None))

    def results_for_rolling_ring_assembly(self, design_entity: '_2548.RollingRingAssembly') -> 'Iterable[_5556.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY](design_entity.wrapped if design_entity else None))

    def results_for_spring_damper(self, design_entity: '_2551.SpringDamper') -> 'Iterable[_5567.SpringDamperCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpringDamperCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER](design_entity.wrapped if design_entity else None))

    def results_for_spring_damper_half(self, design_entity: '_2552.SpringDamperHalf') -> 'Iterable[_5569.SpringDamperHalfCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpringDamperHalfCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF](design_entity.wrapped if design_entity else None))

    def results_for_synchroniser(self, design_entity: '_2553.Synchroniser') -> 'Iterable[_5578.SynchroniserCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SynchroniserCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER](design_entity.wrapped if design_entity else None))

    def results_for_synchroniser_half(self, design_entity: '_2555.SynchroniserHalf') -> 'Iterable[_5579.SynchroniserHalfCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SynchroniserHalfCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF](design_entity.wrapped if design_entity else None))

    def results_for_synchroniser_part(self, design_entity: '_2556.SynchroniserPart') -> 'Iterable[_5580.SynchroniserPartCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SynchroniserPartCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART](design_entity.wrapped if design_entity else None))

    def results_for_synchroniser_sleeve(self, design_entity: '_2557.SynchroniserSleeve') -> 'Iterable[_5581.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE](design_entity.wrapped if design_entity else None))

    def results_for_torque_converter(self, design_entity: '_2558.TorqueConverter') -> 'Iterable[_5582.TorqueConverterCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.TorqueConverterCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER](design_entity.wrapped if design_entity else None))

    def results_for_torque_converter_pump(self, design_entity: '_2559.TorqueConverterPump') -> 'Iterable[_5584.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP](design_entity.wrapped if design_entity else None))

    def results_for_torque_converter_turbine(self, design_entity: '_2561.TorqueConverterTurbine') -> 'Iterable[_5585.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE](design_entity.wrapped if design_entity else None))

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_2247.ShaftToMountableComponentConnection') -> 'Iterable[_5562.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_cvt_belt_connection(self, design_entity: '_2225.CVTBeltConnection') -> 'Iterable[_5505.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_belt_connection(self, design_entity: '_2220.BeltConnection') -> 'Iterable[_5474.BeltConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BeltConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_coaxial_connection(self, design_entity: '_2221.CoaxialConnection') -> 'Iterable[_5489.CoaxialConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CoaxialConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_connection(self, design_entity: '_2224.Connection') -> 'Iterable[_5500.ConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_inter_mountable_component_connection(self, design_entity: '_2233.InterMountableComponentConnection') -> 'Iterable[_5530.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_INTER_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_planetary_connection(self, design_entity: '_2239.PlanetaryConnection') -> 'Iterable[_5548.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_rolling_ring_connection(self, design_entity: '_2244.RollingRingConnection') -> 'Iterable[_5558.RollingRingConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RollingRingConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_abstract_shaft_to_mountable_component_connection(self, design_entity: '_2217.AbstractShaftToMountableComponentConnection') -> 'Iterable[_5468.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_2253.BevelDifferentialGearMesh') -> 'Iterable[_5477.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_concept_gear_mesh(self, design_entity: '_2257.ConceptGearMesh') -> 'Iterable[_5495.ConceptGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_face_gear_mesh(self, design_entity: '_2263.FaceGearMesh') -> 'Iterable[_5519.FaceGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FaceGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_2277.StraightBevelDiffGearMesh') -> 'Iterable[_5571.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_bevel_gear_mesh(self, design_entity: '_2255.BevelGearMesh') -> 'Iterable[_5482.BevelGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_conical_gear_mesh(self, design_entity: '_2259.ConicalGearMesh') -> 'Iterable[_5498.ConicalGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConicalGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_2251.AGMAGleasonConicalGearMesh') -> 'Iterable[_5470.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_cylindrical_gear_mesh(self, design_entity: '_2261.CylindricalGearMesh') -> 'Iterable[_5513.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_hypoid_gear_mesh(self, design_entity: '_2267.HypoidGearMesh') -> 'Iterable[_5528.HypoidGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.HypoidGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_2270.KlingelnbergCycloPalloidConicalGearMesh') -> 'Iterable[_5532.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_2271.KlingelnbergCycloPalloidHypoidGearMesh') -> 'Iterable[_5535.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_2272.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> 'Iterable[_5538.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_2275.SpiralBevelGearMesh') -> 'Iterable[_5565.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_2279.StraightBevelGearMesh') -> 'Iterable[_5574.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_worm_gear_mesh(self, design_entity: '_2281.WormGearMesh') -> 'Iterable[_5589.WormGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.WormGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_2283.ZerolBevelGearMesh') -> 'Iterable[_5592.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_gear_mesh(self, design_entity: '_2265.GearMesh') -> 'Iterable[_5524.GearMeshCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.GearMeshCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_cycloidal_disc_central_bearing_connection(self, design_entity: '_2287.CycloidalDiscCentralBearingConnection') -> 'Iterable[_5509.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_cycloidal_disc_planetary_bearing_connection(self, design_entity: '_2290.CycloidalDiscPlanetaryBearingConnection') -> 'Iterable[_5511.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_ring_pins_to_disc_connection(self, design_entity: '_2293.RingPinsToDiscConnection') -> 'Iterable[_5555.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_RING_PINS_TO_DISC_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_2300.PartToPartShearCouplingConnection') -> 'Iterable[_5546.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_clutch_connection(self, design_entity: '_2294.ClutchConnection') -> 'Iterable[_5487.ClutchConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ClutchConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_concept_coupling_connection(self, design_entity: '_2296.ConceptCouplingConnection') -> 'Iterable[_5492.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_coupling_connection(self, design_entity: '_2298.CouplingConnection') -> 'Iterable[_5503.CouplingConnectionCompoundMultibodyDynamicsAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CouplingConnectionCompoundMultibodyDynamicsAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None))
