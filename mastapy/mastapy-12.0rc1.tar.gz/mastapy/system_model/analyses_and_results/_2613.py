"""_2613.py

CompoundDynamicAnalysis
"""


from typing import Iterable

from mastapy.system_model.connections_and_sockets.couplings import (
    _2302, _2304, _2300, _2294,
    _2296, _2298
)
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
    _6438, _6453, _6336, _6335,
    _6337, _6343, _6354, _6355,
    _6360, _6371, _6386, _6387,
    _6391, _6392, _6342, _6396,
    _6410, _6411, _6412, _6413,
    _6414, _6420, _6421, _6422,
    _6429, _6433, _6456, _6457,
    _6430, _6364, _6366, _6388,
    _6390, _6339, _6341, _6346,
    _6348, _6349, _6350, _6351,
    _6353, _6367, _6369, _6382,
    _6384, _6385, _6393, _6395,
    _6397, _6399, _6401, _6403,
    _6404, _6406, _6407, _6409,
    _6419, _6434, _6436, _6440,
    _6442, _6443, _6445, _6446,
    _6447, _6458, _6460, _6461,
    _6463, _6378, _6380, _6424,
    _6415, _6417, _6345, _6356,
    _6358, _6361, _6363, _6372,
    _6374, _6376, _6377, _6423,
    _6431, _6427, _6426, _6437,
    _6439, _6448, _6449, _6450,
    _6451, _6452, _6454, _6455,
    _6432, _6375, _6344, _6359,
    _6370, _6400, _6418, _6428,
    _6338, _6347, _6365, _6389,
    _6441, _6352, _6368, _6340,
    _6383, _6398, _6402, _6405,
    _6408, _6435, _6444, _6459,
    _6462, _6394, _6379, _6381,
    _6425, _6416, _6357, _6362,
    _6373
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
_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundDynamicAnalysis',)


class CompoundDynamicAnalysis(_2570.CompoundAnalysis):
    """CompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_DYNAMIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'CompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def results_for_spring_damper_connection(self, design_entity: '_2302.SpringDamperConnection') -> 'Iterable[_6438.SpringDamperConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpringDamperConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_torque_converter_connection(self, design_entity: '_2304.TorqueConverterConnection') -> 'Iterable[_6453.TorqueConverterConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.TorqueConverterConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_abstract_shaft(self, design_entity: '_2388.AbstractShaft') -> 'Iterable[_6336.AbstractShaftCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.AbstractShaftCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT](design_entity.wrapped if design_entity else None))

    def results_for_abstract_assembly(self, design_entity: '_2387.AbstractAssembly') -> 'Iterable[_6335.AbstractAssemblyCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.AbstractAssemblyCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY](design_entity.wrapped if design_entity else None))

    def results_for_abstract_shaft_or_housing(self, design_entity: '_2389.AbstractShaftOrHousing') -> 'Iterable[_6337.AbstractShaftOrHousingCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.AbstractShaftOrHousingCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](design_entity.wrapped if design_entity else None))

    def results_for_bearing(self, design_entity: '_2392.Bearing') -> 'Iterable[_6343.BearingCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BearingCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEARING](design_entity.wrapped if design_entity else None))

    def results_for_bolt(self, design_entity: '_2394.Bolt') -> 'Iterable[_6354.BoltCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BoltCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BOLT](design_entity.wrapped if design_entity else None))

    def results_for_bolted_joint(self, design_entity: '_2395.BoltedJoint') -> 'Iterable[_6355.BoltedJointCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BoltedJointCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT](design_entity.wrapped if design_entity else None))

    def results_for_component(self, design_entity: '_2396.Component') -> 'Iterable[_6360.ComponentCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ComponentCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COMPONENT](design_entity.wrapped if design_entity else None))

    def results_for_connector(self, design_entity: '_2399.Connector') -> 'Iterable[_6371.ConnectorCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConnectorCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONNECTOR](design_entity.wrapped if design_entity else None))

    def results_for_datum(self, design_entity: '_2400.Datum') -> 'Iterable[_6386.DatumCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.DatumCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_DATUM](design_entity.wrapped if design_entity else None))

    def results_for_external_cad_model(self, design_entity: '_2404.ExternalCADModel') -> 'Iterable[_6387.ExternalCADModelCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ExternalCADModelCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL](design_entity.wrapped if design_entity else None))

    def results_for_fe_part(self, design_entity: '_2405.FEPart') -> 'Iterable[_6391.FEPartCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FEPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.FEPartCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FE_PART](design_entity.wrapped if design_entity else None))

    def results_for_flexible_pin_assembly(self, design_entity: '_2406.FlexiblePinAssembly') -> 'Iterable[_6392.FlexiblePinAssemblyCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.FlexiblePinAssemblyCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](design_entity.wrapped if design_entity else None))

    def results_for_assembly(self, design_entity: '_2386.Assembly') -> 'Iterable[_6342.AssemblyCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.AssemblyCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ASSEMBLY](design_entity.wrapped if design_entity else None))

    def results_for_guide_dxf_model(self, design_entity: '_2407.GuideDxfModel') -> 'Iterable[_6396.GuideDxfModelCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.GuideDxfModelCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL](design_entity.wrapped if design_entity else None))

    def results_for_mass_disc(self, design_entity: '_2414.MassDisc') -> 'Iterable[_6410.MassDiscCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.MassDiscCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_MASS_DISC](design_entity.wrapped if design_entity else None))

    def results_for_measurement_component(self, design_entity: '_2415.MeasurementComponent') -> 'Iterable[_6411.MeasurementComponentCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.MeasurementComponentCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT](design_entity.wrapped if design_entity else None))

    def results_for_mountable_component(self, design_entity: '_2416.MountableComponent') -> 'Iterable[_6412.MountableComponentCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.MountableComponentCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT](design_entity.wrapped if design_entity else None))

    def results_for_oil_seal(self, design_entity: '_2418.OilSeal') -> 'Iterable[_6413.OilSealCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.OilSealCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_OIL_SEAL](design_entity.wrapped if design_entity else None))

    def results_for_part(self, design_entity: '_2420.Part') -> 'Iterable[_6414.PartCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PartCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART](design_entity.wrapped if design_entity else None))

    def results_for_planet_carrier(self, design_entity: '_2421.PlanetCarrier') -> 'Iterable[_6420.PlanetCarrierCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PlanetCarrierCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER](design_entity.wrapped if design_entity else None))

    def results_for_point_load(self, design_entity: '_2423.PointLoad') -> 'Iterable[_6421.PointLoadCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PointLoadCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_POINT_LOAD](design_entity.wrapped if design_entity else None))

    def results_for_power_load(self, design_entity: '_2424.PowerLoad') -> 'Iterable[_6422.PowerLoadCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PowerLoadCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_POWER_LOAD](design_entity.wrapped if design_entity else None))

    def results_for_root_assembly(self, design_entity: '_2426.RootAssembly') -> 'Iterable[_6429.RootAssemblyCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.RootAssemblyCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY](design_entity.wrapped if design_entity else None))

    def results_for_specialised_assembly(self, design_entity: '_2428.SpecialisedAssembly') -> 'Iterable[_6433.SpecialisedAssemblyCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpecialisedAssemblyCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY](design_entity.wrapped if design_entity else None))

    def results_for_unbalanced_mass(self, design_entity: '_2429.UnbalancedMass') -> 'Iterable[_6456.UnbalancedMassCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.UnbalancedMassCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS](design_entity.wrapped if design_entity else None))

    def results_for_virtual_component(self, design_entity: '_2431.VirtualComponent') -> 'Iterable[_6457.VirtualComponentCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.VirtualComponentCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT](design_entity.wrapped if design_entity else None))

    def results_for_shaft(self, design_entity: '_2434.Shaft') -> 'Iterable[_6430.ShaftCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ShaftCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SHAFT](design_entity.wrapped if design_entity else None))

    def results_for_concept_gear(self, design_entity: '_2472.ConceptGear') -> 'Iterable[_6364.ConceptGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConceptGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_concept_gear_set(self, design_entity: '_2473.ConceptGearSet') -> 'Iterable[_6366.ConceptGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConceptGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_face_gear(self, design_entity: '_2479.FaceGear') -> 'Iterable[_6388.FaceGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.FaceGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FACE_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_face_gear_set(self, design_entity: '_2480.FaceGearSet') -> 'Iterable[_6390.FaceGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.FaceGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2464.AGMAGleasonConicalGear') -> 'Iterable[_6339.AGMAGleasonConicalGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.AGMAGleasonConicalGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2465.AGMAGleasonConicalGearSet') -> 'Iterable[_6341.AGMAGleasonConicalGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.AGMAGleasonConicalGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_bevel_differential_gear(self, design_entity: '_2466.BevelDifferentialGear') -> 'Iterable[_6346.BevelDifferentialGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelDifferentialGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_bevel_differential_gear_set(self, design_entity: '_2467.BevelDifferentialGearSet') -> 'Iterable[_6348.BevelDifferentialGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelDifferentialGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2468.BevelDifferentialPlanetGear') -> 'Iterable[_6349.BevelDifferentialPlanetGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelDifferentialPlanetGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_PLANET_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2469.BevelDifferentialSunGear') -> 'Iterable[_6350.BevelDifferentialSunGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelDifferentialSunGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_bevel_gear(self, design_entity: '_2470.BevelGear') -> 'Iterable[_6351.BevelGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_bevel_gear_set(self, design_entity: '_2471.BevelGearSet') -> 'Iterable[_6353.BevelGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_conical_gear(self, design_entity: '_2474.ConicalGear') -> 'Iterable[_6367.ConicalGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConicalGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_conical_gear_set(self, design_entity: '_2475.ConicalGearSet') -> 'Iterable[_6369.ConicalGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConicalGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_cylindrical_gear(self, design_entity: '_2476.CylindricalGear') -> 'Iterable[_6382.CylindricalGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CylindricalGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_cylindrical_gear_set(self, design_entity: '_2477.CylindricalGearSet') -> 'Iterable[_6384.CylindricalGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CylindricalGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_cylindrical_planet_gear(self, design_entity: '_2478.CylindricalPlanetGear') -> 'Iterable[_6385.CylindricalPlanetGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CylindricalPlanetGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_gear(self, design_entity: '_2481.Gear') -> 'Iterable[_6393.GearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.GearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_gear_set(self, design_entity: '_2483.GearSet') -> 'Iterable[_6395.GearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.GearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_hypoid_gear(self, design_entity: '_2485.HypoidGear') -> 'Iterable[_6397.HypoidGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.HypoidGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_hypoid_gear_set(self, design_entity: '_2486.HypoidGearSet') -> 'Iterable[_6399.HypoidGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.HypoidGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2487.KlingelnbergCycloPalloidConicalGear') -> 'Iterable[_6401.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2488.KlingelnbergCycloPalloidConicalGearSet') -> 'Iterable[_6403.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2489.KlingelnbergCycloPalloidHypoidGear') -> 'Iterable[_6404.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2490.KlingelnbergCycloPalloidHypoidGearSet') -> 'Iterable[_6406.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2491.KlingelnbergCycloPalloidSpiralBevelGear') -> 'Iterable[_6407.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2492.KlingelnbergCycloPalloidSpiralBevelGearSet') -> 'Iterable[_6409.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_planetary_gear_set(self, design_entity: '_2493.PlanetaryGearSet') -> 'Iterable[_6419.PlanetaryGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PlanetaryGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_spiral_bevel_gear(self, design_entity: '_2494.SpiralBevelGear') -> 'Iterable[_6434.SpiralBevelGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpiralBevelGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2495.SpiralBevelGearSet') -> 'Iterable[_6436.SpiralBevelGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpiralBevelGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2496.StraightBevelDiffGear') -> 'Iterable[_6440.StraightBevelDiffGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelDiffGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2497.StraightBevelDiffGearSet') -> 'Iterable[_6442.StraightBevelDiffGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelDiffGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_gear(self, design_entity: '_2498.StraightBevelGear') -> 'Iterable[_6443.StraightBevelGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_gear_set(self, design_entity: '_2499.StraightBevelGearSet') -> 'Iterable[_6445.StraightBevelGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2500.StraightBevelPlanetGear') -> 'Iterable[_6446.StraightBevelPlanetGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelPlanetGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2501.StraightBevelSunGear') -> 'Iterable[_6447.StraightBevelSunGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelSunGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_worm_gear(self, design_entity: '_2502.WormGear') -> 'Iterable[_6458.WormGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.WormGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_WORM_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_worm_gear_set(self, design_entity: '_2503.WormGearSet') -> 'Iterable[_6460.WormGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.WormGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_zerol_bevel_gear(self, design_entity: '_2504.ZerolBevelGear') -> 'Iterable[_6461.ZerolBevelGearCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ZerolBevelGearCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR](design_entity.wrapped if design_entity else None))

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2505.ZerolBevelGearSet') -> 'Iterable[_6463.ZerolBevelGearSetCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ZerolBevelGearSetCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None))

    def results_for_cycloidal_assembly(self, design_entity: '_2519.CycloidalAssembly') -> 'Iterable[_6378.CycloidalAssemblyCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CycloidalAssemblyCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_ASSEMBLY](design_entity.wrapped if design_entity else None))

    def results_for_cycloidal_disc(self, design_entity: '_2520.CycloidalDisc') -> 'Iterable[_6380.CycloidalDiscCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CycloidalDiscCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC](design_entity.wrapped if design_entity else None))

    def results_for_ring_pins(self, design_entity: '_2521.RingPins') -> 'Iterable[_6424.RingPinsCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.RingPins)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.RingPinsCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_RING_PINS](design_entity.wrapped if design_entity else None))

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2539.PartToPartShearCoupling') -> 'Iterable[_6415.PartToPartShearCouplingCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PartToPartShearCouplingCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](design_entity.wrapped if design_entity else None))

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2540.PartToPartShearCouplingHalf') -> 'Iterable[_6417.PartToPartShearCouplingHalfCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PartToPartShearCouplingHalfCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_HALF](design_entity.wrapped if design_entity else None))

    def results_for_belt_drive(self, design_entity: '_2527.BeltDrive') -> 'Iterable[_6345.BeltDriveCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BeltDriveCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BELT_DRIVE](design_entity.wrapped if design_entity else None))

    def results_for_clutch(self, design_entity: '_2529.Clutch') -> 'Iterable[_6356.ClutchCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ClutchCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CLUTCH](design_entity.wrapped if design_entity else None))

    def results_for_clutch_half(self, design_entity: '_2530.ClutchHalf') -> 'Iterable[_6358.ClutchHalfCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ClutchHalfCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF](design_entity.wrapped if design_entity else None))

    def results_for_concept_coupling(self, design_entity: '_2532.ConceptCoupling') -> 'Iterable[_6361.ConceptCouplingCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConceptCouplingCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING](design_entity.wrapped if design_entity else None))

    def results_for_concept_coupling_half(self, design_entity: '_2533.ConceptCouplingHalf') -> 'Iterable[_6363.ConceptCouplingHalfCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConceptCouplingHalfCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF](design_entity.wrapped if design_entity else None))

    def results_for_coupling(self, design_entity: '_2534.Coupling') -> 'Iterable[_6372.CouplingCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CouplingCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COUPLING](design_entity.wrapped if design_entity else None))

    def results_for_coupling_half(self, design_entity: '_2535.CouplingHalf') -> 'Iterable[_6374.CouplingHalfCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CouplingHalfCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COUPLING_HALF](design_entity.wrapped if design_entity else None))

    def results_for_cvt(self, design_entity: '_2537.CVT') -> 'Iterable[_6376.CVTCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CVTCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CVT](design_entity.wrapped if design_entity else None))

    def results_for_cvt_pulley(self, design_entity: '_2538.CVTPulley') -> 'Iterable[_6377.CVTPulleyCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CVTPulleyCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CVT_PULLEY](design_entity.wrapped if design_entity else None))

    def results_for_pulley(self, design_entity: '_2541.Pulley') -> 'Iterable[_6423.PulleyCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PulleyCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PULLEY](design_entity.wrapped if design_entity else None))

    def results_for_shaft_hub_connection(self, design_entity: '_2549.ShaftHubConnection') -> 'Iterable[_6431.ShaftHubConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ShaftHubConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_rolling_ring(self, design_entity: '_2547.RollingRing') -> 'Iterable[_6427.RollingRingCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.RollingRingCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROLLING_RING](design_entity.wrapped if design_entity else None))

    def results_for_rolling_ring_assembly(self, design_entity: '_2548.RollingRingAssembly') -> 'Iterable[_6426.RollingRingAssemblyCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.RollingRingAssemblyCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY](design_entity.wrapped if design_entity else None))

    def results_for_spring_damper(self, design_entity: '_2551.SpringDamper') -> 'Iterable[_6437.SpringDamperCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpringDamperCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER](design_entity.wrapped if design_entity else None))

    def results_for_spring_damper_half(self, design_entity: '_2552.SpringDamperHalf') -> 'Iterable[_6439.SpringDamperHalfCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpringDamperHalfCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF](design_entity.wrapped if design_entity else None))

    def results_for_synchroniser(self, design_entity: '_2553.Synchroniser') -> 'Iterable[_6448.SynchroniserCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SynchroniserCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER](design_entity.wrapped if design_entity else None))

    def results_for_synchroniser_half(self, design_entity: '_2555.SynchroniserHalf') -> 'Iterable[_6449.SynchroniserHalfCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SynchroniserHalfCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF](design_entity.wrapped if design_entity else None))

    def results_for_synchroniser_part(self, design_entity: '_2556.SynchroniserPart') -> 'Iterable[_6450.SynchroniserPartCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SynchroniserPartCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART](design_entity.wrapped if design_entity else None))

    def results_for_synchroniser_sleeve(self, design_entity: '_2557.SynchroniserSleeve') -> 'Iterable[_6451.SynchroniserSleeveCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SynchroniserSleeveCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE](design_entity.wrapped if design_entity else None))

    def results_for_torque_converter(self, design_entity: '_2558.TorqueConverter') -> 'Iterable[_6452.TorqueConverterCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.TorqueConverterCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER](design_entity.wrapped if design_entity else None))

    def results_for_torque_converter_pump(self, design_entity: '_2559.TorqueConverterPump') -> 'Iterable[_6454.TorqueConverterPumpCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.TorqueConverterPumpCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP](design_entity.wrapped if design_entity else None))

    def results_for_torque_converter_turbine(self, design_entity: '_2561.TorqueConverterTurbine') -> 'Iterable[_6455.TorqueConverterTurbineCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.TorqueConverterTurbineCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE](design_entity.wrapped if design_entity else None))

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_2247.ShaftToMountableComponentConnection') -> 'Iterable[_6432.ShaftToMountableComponentConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ShaftToMountableComponentConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_cvt_belt_connection(self, design_entity: '_2225.CVTBeltConnection') -> 'Iterable[_6375.CVTBeltConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CVTBeltConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_belt_connection(self, design_entity: '_2220.BeltConnection') -> 'Iterable[_6344.BeltConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BeltConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_coaxial_connection(self, design_entity: '_2221.CoaxialConnection') -> 'Iterable[_6359.CoaxialConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CoaxialConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_connection(self, design_entity: '_2224.Connection') -> 'Iterable[_6370.ConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_inter_mountable_component_connection(self, design_entity: '_2233.InterMountableComponentConnection') -> 'Iterable[_6400.InterMountableComponentConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.InterMountableComponentConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_INTER_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_planetary_connection(self, design_entity: '_2239.PlanetaryConnection') -> 'Iterable[_6418.PlanetaryConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PlanetaryConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_rolling_ring_connection(self, design_entity: '_2244.RollingRingConnection') -> 'Iterable[_6428.RollingRingConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.RollingRingConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_abstract_shaft_to_mountable_component_connection(self, design_entity: '_2217.AbstractShaftToMountableComponentConnection') -> 'Iterable[_6338.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_2253.BevelDifferentialGearMesh') -> 'Iterable[_6347.BevelDifferentialGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelDifferentialGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_concept_gear_mesh(self, design_entity: '_2257.ConceptGearMesh') -> 'Iterable[_6365.ConceptGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConceptGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_face_gear_mesh(self, design_entity: '_2263.FaceGearMesh') -> 'Iterable[_6389.FaceGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.FaceGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_2277.StraightBevelDiffGearMesh') -> 'Iterable[_6441.StraightBevelDiffGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelDiffGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_bevel_gear_mesh(self, design_entity: '_2255.BevelGearMesh') -> 'Iterable[_6352.BevelGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_conical_gear_mesh(self, design_entity: '_2259.ConicalGearMesh') -> 'Iterable[_6368.ConicalGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConicalGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_2251.AGMAGleasonConicalGearMesh') -> 'Iterable[_6340.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_cylindrical_gear_mesh(self, design_entity: '_2261.CylindricalGearMesh') -> 'Iterable[_6383.CylindricalGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CylindricalGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_hypoid_gear_mesh(self, design_entity: '_2267.HypoidGearMesh') -> 'Iterable[_6398.HypoidGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.HypoidGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_2270.KlingelnbergCycloPalloidConicalGearMesh') -> 'Iterable[_6402.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_2271.KlingelnbergCycloPalloidHypoidGearMesh') -> 'Iterable[_6405.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_2272.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> 'Iterable[_6408.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_2275.SpiralBevelGearMesh') -> 'Iterable[_6435.SpiralBevelGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpiralBevelGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_2279.StraightBevelGearMesh') -> 'Iterable[_6444.StraightBevelGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_worm_gear_mesh(self, design_entity: '_2281.WormGearMesh') -> 'Iterable[_6459.WormGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.WormGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_2283.ZerolBevelGearMesh') -> 'Iterable[_6462.ZerolBevelGearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ZerolBevelGearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_gear_mesh(self, design_entity: '_2265.GearMesh') -> 'Iterable[_6394.GearMeshCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.GearMeshCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GEAR_MESH](design_entity.wrapped if design_entity else None))

    def results_for_cycloidal_disc_central_bearing_connection(self, design_entity: '_2287.CycloidalDiscCentralBearingConnection') -> 'Iterable[_6379.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_cycloidal_disc_planetary_bearing_connection(self, design_entity: '_2290.CycloidalDiscPlanetaryBearingConnection') -> 'Iterable[_6381.CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_ring_pins_to_disc_connection(self, design_entity: '_2293.RingPinsToDiscConnection') -> 'Iterable[_6425.RingPinsToDiscConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.RingPinsToDiscConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_RING_PINS_TO_DISC_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_2300.PartToPartShearCouplingConnection') -> 'Iterable[_6416.PartToPartShearCouplingConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PartToPartShearCouplingConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_clutch_connection(self, design_entity: '_2294.ClutchConnection') -> 'Iterable[_6357.ClutchConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ClutchConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_concept_coupling_connection(self, design_entity: '_2296.ConceptCouplingConnection') -> 'Iterable[_6362.ConceptCouplingConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConceptCouplingConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None))

    def results_for_coupling_connection(self, design_entity: '_2298.CouplingConnection') -> 'Iterable[_6373.CouplingConnectionCompoundDynamicAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CouplingConnectionCompoundDynamicAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None))
