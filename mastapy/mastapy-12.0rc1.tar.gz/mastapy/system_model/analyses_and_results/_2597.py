"""_2597.py

SystemDeflectionAnalysis
"""


from mastapy.system_model.analyses_and_results.static_loads import (
    _6882, _6898, _6908, _6910,
    _6911, _6913, _6783, _6785,
    _6869, _6857, _6856, _6748,
    _6761, _6760, _6766, _6765,
    _6779, _6778, _6781, _6782,
    _6866, _6875, _6873, _6871,
    _6884, _6883, _6894, _6893,
    _6895, _6896, _6899, _6900,
    _6901, _6877, _6780, _6747,
    _6762, _6775, _6837, _6858,
    _6872, _6736, _6750, _6768,
    _6811, _6886, _6755, _6772,
    _6741, _6789, _6832, _6839,
    _6842, _6845, _6880, _6889,
    _6909, _6912, _6818, _6784,
    _6786, _6870, _6855, _6759,
    _6764, _6777, _6734, _6733,
    _6735, _6746, _6758, _6757,
    _6763, _6776, _6795, _6809,
    _6813, _6814, _6745, _6822,
    _6847, _6848, _6850, _6852,
    _6854, _6861, _6864, _6865,
    _6874, _6878, _6906, _6907,
    _6876, _6767, _6769, _6810,
    _6812, _6740, _6742, _6749,
    _6751, _6752, _6753, _6754,
    _6756, _6770, _6774, _6787,
    _6791, _6792, _6816, _6821,
    _6831, _6833, _6838, _6840,
    _6841, _6843, _6844, _6846,
    _6859, _6879, _6881, _6885,
    _6887, _6888, _6890, _6891,
    _6892
)
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2756, _2774, _2784, _2783,
    _2787, _2786, _2681, _2684,
    _2740, _2734, _2733, _2646,
    _2659, _2658, _2665, _2664,
    _2677, _2676, _2680, _2679,
    _2739, _2747, _2745, _2743,
    _2758, _2757, _2770, _2767,
    _2768, _2769, _2776, _2775,
    _2777, _2751, _2678, _2645,
    _2660, _2673, _2713, _2735,
    _2744, _2639, _2647, _2666,
    _2700, _2759, _2652, _2670,
    _2640, _2687, _2709, _2714,
    _2717, _2720, _2753, _2762,
    _2782, _2785, _2705, _2682,
    _2683, _2741, _2732, _2657,
    _2663, _2675, _2638, _2636,
    _2637, _2644, _2656, _2655,
    _2661, _2674, _2697, _2698,
    _2703, _2704, _2643, _2708,
    _2725, _2726, _2728, _2730,
    _2731, _2736, _2737, _2738,
    _2746, _2752, _2780, _2781,
    _2750, _2668, _2667, _2702,
    _2701, _2642, _2641, _2649,
    _2648, _2650, _2651, _2654,
    _2653, _2672, _2671, _2693,
    _2690, _2696, _2707, _2706,
    _2711, _2710, _2716, _2715,
    _2719, _2718, _2722, _2721,
    _2755, _2754, _2761, _2760,
    _2764, _2763, _2765, _2766
)
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.couplings import (
    _2304, _2300, _2294, _2296,
    _2298, _2302
)
from mastapy.system_model.part_model.gears import (
    _2503, _2504, _2505, _2472,
    _2473, _2479, _2480, _2464,
    _2465, _2466, _2467, _2468,
    _2469, _2470, _2471, _2474,
    _2475, _2476, _2477, _2478,
    _2481, _2483, _2485, _2486,
    _2487, _2488, _2489, _2490,
    _2491, _2492, _2493, _2494,
    _2495, _2496, _2497, _2498,
    _2499, _2500, _2501, _2502
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
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results import _2571

_SPRING_DAMPER_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpringDamperConnectionLoadCase')
_TORQUE_CONVERTER_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'TorqueConverterConnectionLoadCase')
_WORM_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'WormGearLoadCase')
_WORM_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'WormGearSetLoadCase')
_ZEROL_BEVEL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ZerolBevelGearLoadCase')
_ZEROL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ZerolBevelGearSetLoadCase')
_CYCLOIDAL_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CycloidalAssemblyLoadCase')
_CYCLOIDAL_DISC_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CycloidalDiscLoadCase')
_RING_PINS_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'RingPinsLoadCase')
_PART_TO_PART_SHEAR_COUPLING_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PartToPartShearCouplingLoadCase')
_PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PartToPartShearCouplingHalfLoadCase')
_BELT_DRIVE_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BeltDriveLoadCase')
_CLUTCH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ClutchLoadCase')
_CLUTCH_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ClutchHalfLoadCase')
_CONCEPT_COUPLING_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptCouplingLoadCase')
_CONCEPT_COUPLING_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptCouplingHalfLoadCase')
_COUPLING_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CouplingLoadCase')
_COUPLING_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CouplingHalfLoadCase')
_CVT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CVTLoadCase')
_CVT_PULLEY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CVTPulleyLoadCase')
_PULLEY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PulleyLoadCase')
_SHAFT_HUB_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ShaftHubConnectionLoadCase')
_ROLLING_RING_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'RollingRingLoadCase')
_ROLLING_RING_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'RollingRingAssemblyLoadCase')
_SPRING_DAMPER_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpringDamperLoadCase')
_SPRING_DAMPER_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpringDamperHalfLoadCase')
_SYNCHRONISER_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SynchroniserLoadCase')
_SYNCHRONISER_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SynchroniserHalfLoadCase')
_SYNCHRONISER_PART_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SynchroniserPartLoadCase')
_SYNCHRONISER_SLEEVE_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SynchroniserSleeveLoadCase')
_TORQUE_CONVERTER_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'TorqueConverterLoadCase')
_TORQUE_CONVERTER_PUMP_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'TorqueConverterPumpLoadCase')
_TORQUE_CONVERTER_TURBINE_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'TorqueConverterTurbineLoadCase')
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ShaftToMountableComponentConnectionLoadCase')
_CVT_BELT_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CVTBeltConnectionLoadCase')
_BELT_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BeltConnectionLoadCase')
_COAXIAL_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CoaxialConnectionLoadCase')
_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConnectionLoadCase')
_INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'InterMountableComponentConnectionLoadCase')
_PLANETARY_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PlanetaryConnectionLoadCase')
_ROLLING_RING_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'RollingRingConnectionLoadCase')
_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AbstractShaftToMountableComponentConnectionLoadCase')
_BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelDifferentialGearMeshLoadCase')
_CONCEPT_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptGearMeshLoadCase')
_FACE_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'FaceGearMeshLoadCase')
_STRAIGHT_BEVEL_DIFF_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelDiffGearMeshLoadCase')
_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelGearMeshLoadCase')
_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConicalGearMeshLoadCase')
_AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AGMAGleasonConicalGearMeshLoadCase')
_CYLINDRICAL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CylindricalGearMeshLoadCase')
_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HypoidGearMeshLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidConicalGearMeshLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidHypoidGearMeshLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase')
_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpiralBevelGearMeshLoadCase')
_STRAIGHT_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelGearMeshLoadCase')
_WORM_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'WormGearMeshLoadCase')
_ZEROL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ZerolBevelGearMeshLoadCase')
_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'GearMeshLoadCase')
_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CycloidalDiscCentralBearingConnectionLoadCase')
_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CycloidalDiscPlanetaryBearingConnectionLoadCase')
_RING_PINS_TO_DISC_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'RingPinsToDiscConnectionLoadCase')
_PART_TO_PART_SHEAR_COUPLING_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PartToPartShearCouplingConnectionLoadCase')
_CLUTCH_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ClutchConnectionLoadCase')
_CONCEPT_COUPLING_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptCouplingConnectionLoadCase')
_COUPLING_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CouplingConnectionLoadCase')
_ABSTRACT_SHAFT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AbstractShaftLoadCase')
_ABSTRACT_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AbstractAssemblyLoadCase')
_ABSTRACT_SHAFT_OR_HOUSING_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AbstractShaftOrHousingLoadCase')
_BEARING_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BearingLoadCase')
_BOLT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BoltLoadCase')
_BOLTED_JOINT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BoltedJointLoadCase')
_COMPONENT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ComponentLoadCase')
_CONNECTOR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConnectorLoadCase')
_DATUM_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'DatumLoadCase')
_EXTERNAL_CAD_MODEL_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ExternalCADModelLoadCase')
_FE_PART_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'FEPartLoadCase')
_FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'FlexiblePinAssemblyLoadCase')
_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AssemblyLoadCase')
_GUIDE_DXF_MODEL_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'GuideDxfModelLoadCase')
_MASS_DISC_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'MassDiscLoadCase')
_MEASUREMENT_COMPONENT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'MeasurementComponentLoadCase')
_MOUNTABLE_COMPONENT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'MountableComponentLoadCase')
_OIL_SEAL_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'OilSealLoadCase')
_PART_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PartLoadCase')
_PLANET_CARRIER_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PlanetCarrierLoadCase')
_POINT_LOAD_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PointLoadLoadCase')
_POWER_LOAD_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PowerLoadLoadCase')
_ROOT_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'RootAssemblyLoadCase')
_SPECIALISED_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpecialisedAssemblyLoadCase')
_UNBALANCED_MASS_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'UnbalancedMassLoadCase')
_VIRTUAL_COMPONENT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'VirtualComponentLoadCase')
_SHAFT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ShaftLoadCase')
_CONCEPT_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptGearLoadCase')
_CONCEPT_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptGearSetLoadCase')
_FACE_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'FaceGearLoadCase')
_FACE_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'FaceGearSetLoadCase')
_AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AGMAGleasonConicalGearLoadCase')
_AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AGMAGleasonConicalGearSetLoadCase')
_BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelDifferentialGearLoadCase')
_BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelDifferentialGearSetLoadCase')
_BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelDifferentialPlanetGearLoadCase')
_BEVEL_DIFFERENTIAL_SUN_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelDifferentialSunGearLoadCase')
_BEVEL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelGearLoadCase')
_BEVEL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelGearSetLoadCase')
_CONICAL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConicalGearLoadCase')
_CONICAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConicalGearSetLoadCase')
_CYLINDRICAL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CylindricalGearLoadCase')
_CYLINDRICAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CylindricalGearSetLoadCase')
_CYLINDRICAL_PLANET_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CylindricalPlanetGearLoadCase')
_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'GearLoadCase')
_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'GearSetLoadCase')
_HYPOID_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HypoidGearLoadCase')
_HYPOID_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HypoidGearSetLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidConicalGearLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidConicalGearSetLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidHypoidGearLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidHypoidGearSetLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidSpiralBevelGearLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase')
_PLANETARY_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PlanetaryGearSetLoadCase')
_SPIRAL_BEVEL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpiralBevelGearLoadCase')
_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpiralBevelGearSetLoadCase')
_STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelDiffGearLoadCase')
_STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelDiffGearSetLoadCase')
_STRAIGHT_BEVEL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelGearLoadCase')
_STRAIGHT_BEVEL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelGearSetLoadCase')
_STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelPlanetGearLoadCase')
_STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelSunGearLoadCase')
_TORQUE_CONVERTER_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'TorqueConverterConnection')
_PART_TO_PART_SHEAR_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'PartToPartShearCouplingConnection')
_CLUTCH_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'ClutchConnection')
_CONCEPT_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'ConceptCouplingConnection')
_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'CouplingConnection')
_SPRING_DAMPER_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'SpringDamperConnection')
_WORM_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'WormGearSet')
_ZEROL_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ZerolBevelGear')
_ZEROL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ZerolBevelGearSet')
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
_SYSTEM_DEFLECTION_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'SystemDeflectionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SystemDeflectionAnalysis',)


class SystemDeflectionAnalysis(_2571.SingleAnalysis):
    """SystemDeflectionAnalysis

    This is a mastapy class.
    """

    TYPE = _SYSTEM_DEFLECTION_ANALYSIS

    def __init__(self, instance_to_wrap: 'SystemDeflectionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def results_for_spring_damper_connection_load_case(self, design_entity_analysis: '_6882.SpringDamperConnectionLoadCase') -> '_2756.SpringDamperConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_torque_converter_connection(self, design_entity: '_2304.TorqueConverterConnection') -> '_2774.TorqueConverterConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_torque_converter_connection_load_case(self, design_entity_analysis: '_6898.TorqueConverterConnectionLoadCase') -> '_2774.TorqueConverterConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_worm_gear_load_case(self, design_entity_analysis: '_6908.WormGearLoadCase') -> '_2784.WormGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_worm_gear_set(self, design_entity: '_2503.WormGearSet') -> '_2783.WormGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_worm_gear_set_load_case(self, design_entity_analysis: '_6910.WormGearSetLoadCase') -> '_2783.WormGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_zerol_bevel_gear(self, design_entity: '_2504.ZerolBevelGear') -> '_2787.ZerolBevelGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_zerol_bevel_gear_load_case(self, design_entity_analysis: '_6911.ZerolBevelGearLoadCase') -> '_2787.ZerolBevelGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2505.ZerolBevelGearSet') -> '_2786.ZerolBevelGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_zerol_bevel_gear_set_load_case(self, design_entity_analysis: '_6913.ZerolBevelGearSetLoadCase') -> '_2786.ZerolBevelGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cycloidal_assembly(self, design_entity: '_2519.CycloidalAssembly') -> '_2681.CycloidalAssemblySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CycloidalAssemblySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_ASSEMBLY](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cycloidal_assembly_load_case(self, design_entity_analysis: '_6783.CycloidalAssemblyLoadCase') -> '_2681.CycloidalAssemblySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CycloidalAssemblySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_ASSEMBLY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cycloidal_disc(self, design_entity: '_2520.CycloidalDisc') -> '_2684.CycloidalDiscSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalDisc)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cycloidal_disc_load_case(self, design_entity_analysis: '_6785.CycloidalDiscLoadCase') -> '_2684.CycloidalDiscSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_ring_pins(self, design_entity: '_2521.RingPins') -> '_2740.RingPinsSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.RingPins)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RingPinsSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_RING_PINS](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_ring_pins_load_case(self, design_entity_analysis: '_6869.RingPinsLoadCase') -> '_2740.RingPinsSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RingPinsSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_RING_PINS_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2539.PartToPartShearCoupling') -> '_2734.PartToPartShearCouplingSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_part_to_part_shear_coupling_load_case(self, design_entity_analysis: '_6857.PartToPartShearCouplingLoadCase') -> '_2734.PartToPartShearCouplingSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2540.PartToPartShearCouplingHalf') -> '_2733.PartToPartShearCouplingHalfSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingHalfSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_HALF](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_part_to_part_shear_coupling_half_load_case(self, design_entity_analysis: '_6856.PartToPartShearCouplingHalfLoadCase') -> '_2733.PartToPartShearCouplingHalfSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingHalfSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_belt_drive(self, design_entity: '_2527.BeltDrive') -> '_2646.BeltDriveSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BeltDriveSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BELT_DRIVE](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_belt_drive_load_case(self, design_entity_analysis: '_6748.BeltDriveLoadCase') -> '_2646.BeltDriveSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BeltDriveSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BELT_DRIVE_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_clutch(self, design_entity: '_2529.Clutch') -> '_2659.ClutchSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_clutch_load_case(self, design_entity_analysis: '_6761.ClutchLoadCase') -> '_2659.ClutchSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_clutch_half(self, design_entity: '_2530.ClutchHalf') -> '_2658.ClutchHalfSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchHalfSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_clutch_half_load_case(self, design_entity_analysis: '_6760.ClutchHalfLoadCase') -> '_2658.ClutchHalfSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchHalfSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_concept_coupling(self, design_entity: '_2532.ConceptCoupling') -> '_2665.ConceptCouplingSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_concept_coupling_load_case(self, design_entity_analysis: '_6766.ConceptCouplingLoadCase') -> '_2665.ConceptCouplingSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_concept_coupling_half(self, design_entity: '_2533.ConceptCouplingHalf') -> '_2664.ConceptCouplingHalfSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingHalfSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_concept_coupling_half_load_case(self, design_entity_analysis: '_6765.ConceptCouplingHalfLoadCase') -> '_2664.ConceptCouplingHalfSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingHalfSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_coupling(self, design_entity: '_2534.Coupling') -> '_2677.CouplingSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_coupling_load_case(self, design_entity_analysis: '_6779.CouplingLoadCase') -> '_2677.CouplingSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_coupling_half(self, design_entity: '_2535.CouplingHalf') -> '_2676.CouplingHalfSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_HALF](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_coupling_half_load_case(self, design_entity_analysis: '_6778.CouplingHalfLoadCase') -> '_2676.CouplingHalfSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_HALF_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cvt(self, design_entity: '_2537.CVT') -> '_2680.CVTSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CVT](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cvt_load_case(self, design_entity_analysis: '_6781.CVTLoadCase') -> '_2680.CVTSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CVT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cvt_pulley(self, design_entity: '_2538.CVTPulley') -> '_2679.CVTPulleySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTPulleySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CVT_PULLEY](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cvt_pulley_load_case(self, design_entity_analysis: '_6782.CVTPulleyLoadCase') -> '_2679.CVTPulleySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTPulleySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CVT_PULLEY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_pulley(self, design_entity: '_2541.Pulley') -> '_2739.PulleySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PulleySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PULLEY](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_pulley_load_case(self, design_entity_analysis: '_6866.PulleyLoadCase') -> '_2739.PulleySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PulleySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PULLEY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_shaft_hub_connection(self, design_entity: '_2549.ShaftHubConnection') -> '_2747.ShaftHubConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftHubConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_shaft_hub_connection_load_case(self, design_entity_analysis: '_6875.ShaftHubConnectionLoadCase') -> '_2747.ShaftHubConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftHubConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_rolling_ring(self, design_entity: '_2547.RollingRing') -> '_2745.RollingRingSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_rolling_ring_load_case(self, design_entity_analysis: '_6873.RollingRingLoadCase') -> '_2745.RollingRingSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_rolling_ring_assembly(self, design_entity: '_2548.RollingRingAssembly') -> '_2743.RollingRingAssemblySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingAssemblySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_rolling_ring_assembly_load_case(self, design_entity_analysis: '_6871.RollingRingAssemblyLoadCase') -> '_2743.RollingRingAssemblySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingAssemblySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_spring_damper(self, design_entity: '_2551.SpringDamper') -> '_2758.SpringDamperSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_spring_damper_load_case(self, design_entity_analysis: '_6884.SpringDamperLoadCase') -> '_2758.SpringDamperSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_spring_damper_half(self, design_entity: '_2552.SpringDamperHalf') -> '_2757.SpringDamperHalfSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperHalfSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_spring_damper_half_load_case(self, design_entity_analysis: '_6883.SpringDamperHalfLoadCase') -> '_2757.SpringDamperHalfSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperHalfSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_synchroniser(self, design_entity: '_2553.Synchroniser') -> '_2770.SynchroniserSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_synchroniser_load_case(self, design_entity_analysis: '_6894.SynchroniserLoadCase') -> '_2770.SynchroniserSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_synchroniser_half(self, design_entity: '_2555.SynchroniserHalf') -> '_2767.SynchroniserHalfSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserHalfSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_synchroniser_half_load_case(self, design_entity_analysis: '_6893.SynchroniserHalfLoadCase') -> '_2767.SynchroniserHalfSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserHalfSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_synchroniser_part(self, design_entity: '_2556.SynchroniserPart') -> '_2768.SynchroniserPartSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserPartSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_synchroniser_part_load_case(self, design_entity_analysis: '_6895.SynchroniserPartLoadCase') -> '_2768.SynchroniserPartSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserPartSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_synchroniser_sleeve(self, design_entity: '_2557.SynchroniserSleeve') -> '_2769.SynchroniserSleeveSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSleeveSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_synchroniser_sleeve_load_case(self, design_entity_analysis: '_6896.SynchroniserSleeveLoadCase') -> '_2769.SynchroniserSleeveSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSleeveSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_torque_converter(self, design_entity: '_2558.TorqueConverter') -> '_2776.TorqueConverterSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_torque_converter_load_case(self, design_entity_analysis: '_6899.TorqueConverterLoadCase') -> '_2776.TorqueConverterSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_torque_converter_pump(self, design_entity: '_2559.TorqueConverterPump') -> '_2775.TorqueConverterPumpSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterPumpSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_torque_converter_pump_load_case(self, design_entity_analysis: '_6900.TorqueConverterPumpLoadCase') -> '_2775.TorqueConverterPumpSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterPumpSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_torque_converter_turbine(self, design_entity: '_2561.TorqueConverterTurbine') -> '_2777.TorqueConverterTurbineSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterTurbineSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_torque_converter_turbine_load_case(self, design_entity_analysis: '_6901.TorqueConverterTurbineLoadCase') -> '_2777.TorqueConverterTurbineSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterTurbineSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_2247.ShaftToMountableComponentConnection') -> '_2751.ShaftToMountableComponentConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftToMountableComponentConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_6877.ShaftToMountableComponentConnectionLoadCase') -> '_2751.ShaftToMountableComponentConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftToMountableComponentConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cvt_belt_connection(self, design_entity: '_2225.CVTBeltConnection') -> '_2678.CVTBeltConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTBeltConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cvt_belt_connection_load_case(self, design_entity_analysis: '_6780.CVTBeltConnectionLoadCase') -> '_2678.CVTBeltConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTBeltConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_belt_connection(self, design_entity: '_2220.BeltConnection') -> '_2645.BeltConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BeltConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_belt_connection_load_case(self, design_entity_analysis: '_6747.BeltConnectionLoadCase') -> '_2645.BeltConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BeltConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_coaxial_connection(self, design_entity: '_2221.CoaxialConnection') -> '_2660.CoaxialConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_coaxial_connection_load_case(self, design_entity_analysis: '_6762.CoaxialConnectionLoadCase') -> '_2660.CoaxialConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_connection(self, design_entity: '_2224.Connection') -> '_2673.ConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_connection_load_case(self, design_entity_analysis: '_6775.ConnectionLoadCase') -> '_2673.ConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_inter_mountable_component_connection(self, design_entity: '_2233.InterMountableComponentConnection') -> '_2713.InterMountableComponentConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.InterMountableComponentConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_INTER_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_inter_mountable_component_connection_load_case(self, design_entity_analysis: '_6837.InterMountableComponentConnectionLoadCase') -> '_2713.InterMountableComponentConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.InterMountableComponentConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_planetary_connection(self, design_entity: '_2239.PlanetaryConnection') -> '_2735.PlanetaryConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PlanetaryConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_planetary_connection_load_case(self, design_entity_analysis: '_6858.PlanetaryConnectionLoadCase') -> '_2735.PlanetaryConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PlanetaryConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_rolling_ring_connection(self, design_entity: '_2244.RollingRingConnection') -> '_2744.RollingRingConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_rolling_ring_connection_load_case(self, design_entity_analysis: '_6872.RollingRingConnectionLoadCase') -> '_2744.RollingRingConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_abstract_shaft_to_mountable_component_connection(self, design_entity: '_2217.AbstractShaftToMountableComponentConnection') -> '_2639.AbstractShaftToMountableComponentConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftToMountableComponentConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_abstract_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_6736.AbstractShaftToMountableComponentConnectionLoadCase') -> '_2639.AbstractShaftToMountableComponentConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftToMountableComponentConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_2253.BevelDifferentialGearMesh') -> '_2647.BevelDifferentialGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_differential_gear_mesh_load_case(self, design_entity_analysis: '_6750.BevelDifferentialGearMeshLoadCase') -> '_2647.BevelDifferentialGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_concept_gear_mesh(self, design_entity: '_2257.ConceptGearMesh') -> '_2666.ConceptGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_concept_gear_mesh_load_case(self, design_entity_analysis: '_6768.ConceptGearMeshLoadCase') -> '_2666.ConceptGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_face_gear_mesh(self, design_entity: '_2263.FaceGearMesh') -> '_2700.FaceGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_face_gear_mesh_load_case(self, design_entity_analysis: '_6811.FaceGearMeshLoadCase') -> '_2700.FaceGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_2277.StraightBevelDiffGearMesh') -> '_2759.StraightBevelDiffGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_diff_gear_mesh_load_case(self, design_entity_analysis: '_6886.StraightBevelDiffGearMeshLoadCase') -> '_2759.StraightBevelDiffGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_gear_mesh(self, design_entity: '_2255.BevelGearMesh') -> '_2652.BevelGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6755.BevelGearMeshLoadCase') -> '_2652.BevelGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_conical_gear_mesh(self, design_entity: '_2259.ConicalGearMesh') -> '_2670.ConicalGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_conical_gear_mesh_load_case(self, design_entity_analysis: '_6772.ConicalGearMeshLoadCase') -> '_2670.ConicalGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_2251.AGMAGleasonConicalGearMesh') -> '_2640.AGMAGleasonConicalGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_agma_gleason_conical_gear_mesh_load_case(self, design_entity_analysis: '_6741.AGMAGleasonConicalGearMeshLoadCase') -> '_2640.AGMAGleasonConicalGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cylindrical_gear_mesh(self, design_entity: '_2261.CylindricalGearMesh') -> '_2687.CylindricalGearMeshSystemDeflectionWithLTCAResults':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearMeshSystemDeflectionWithLTCAResults
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cylindrical_gear_mesh_load_case(self, design_entity_analysis: '_6789.CylindricalGearMeshLoadCase') -> '_2687.CylindricalGearMeshSystemDeflectionWithLTCAResults':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearMeshSystemDeflectionWithLTCAResults
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_hypoid_gear_mesh(self, design_entity: '_2267.HypoidGearMesh') -> '_2709.HypoidGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6832.HypoidGearMeshLoadCase') -> '_2709.HypoidGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_2270.KlingelnbergCycloPalloidConicalGearMesh') -> '_2714.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self, design_entity_analysis: '_6839.KlingelnbergCycloPalloidConicalGearMeshLoadCase') -> '_2714.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_2271.KlingelnbergCycloPalloidHypoidGearMesh') -> '_2717.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6842.KlingelnbergCycloPalloidHypoidGearMeshLoadCase') -> '_2717.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_2272.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_2720.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6845.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase') -> '_2720.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_2275.SpiralBevelGearMesh') -> '_2753.SpiralBevelGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6880.SpiralBevelGearMeshLoadCase') -> '_2753.SpiralBevelGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_2279.StraightBevelGearMesh') -> '_2762.StraightBevelGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6889.StraightBevelGearMeshLoadCase') -> '_2762.StraightBevelGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_worm_gear_mesh(self, design_entity: '_2281.WormGearMesh') -> '_2782.WormGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_worm_gear_mesh_load_case(self, design_entity_analysis: '_6909.WormGearMeshLoadCase') -> '_2782.WormGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_2283.ZerolBevelGearMesh') -> '_2785.ZerolBevelGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_zerol_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6912.ZerolBevelGearMeshLoadCase') -> '_2785.ZerolBevelGearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_gear_mesh(self, design_entity: '_2265.GearMesh') -> '_2705.GearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_MESH](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_gear_mesh_load_case(self, design_entity_analysis: '_6818.GearMeshLoadCase') -> '_2705.GearMeshSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearMeshSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cycloidal_disc_central_bearing_connection(self, design_entity: '_2287.CycloidalDiscCentralBearingConnection') -> '_2682.CycloidalDiscCentralBearingConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscCentralBearingConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cycloidal_disc_central_bearing_connection_load_case(self, design_entity_analysis: '_6784.CycloidalDiscCentralBearingConnectionLoadCase') -> '_2682.CycloidalDiscCentralBearingConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscCentralBearingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscCentralBearingConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cycloidal_disc_planetary_bearing_connection(self, design_entity: '_2290.CycloidalDiscPlanetaryBearingConnection') -> '_2683.CycloidalDiscPlanetaryBearingConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscPlanetaryBearingConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cycloidal_disc_planetary_bearing_connection_load_case(self, design_entity_analysis: '_6786.CycloidalDiscPlanetaryBearingConnectionLoadCase') -> '_2683.CycloidalDiscPlanetaryBearingConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscPlanetaryBearingConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_ring_pins_to_disc_connection(self, design_entity: '_2293.RingPinsToDiscConnection') -> '_2741.RingPinsToDiscConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RingPinsToDiscConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_RING_PINS_TO_DISC_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_ring_pins_to_disc_connection_load_case(self, design_entity_analysis: '_6870.RingPinsToDiscConnectionLoadCase') -> '_2741.RingPinsToDiscConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RingPinsToDiscConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_RING_PINS_TO_DISC_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_2300.PartToPartShearCouplingConnection') -> '_2732.PartToPartShearCouplingConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_part_to_part_shear_coupling_connection_load_case(self, design_entity_analysis: '_6855.PartToPartShearCouplingConnectionLoadCase') -> '_2732.PartToPartShearCouplingConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_clutch_connection(self, design_entity: '_2294.ClutchConnection') -> '_2657.ClutchConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_clutch_connection_load_case(self, design_entity_analysis: '_6759.ClutchConnectionLoadCase') -> '_2657.ClutchConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_concept_coupling_connection(self, design_entity: '_2296.ConceptCouplingConnection') -> '_2663.ConceptCouplingConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_concept_coupling_connection_load_case(self, design_entity_analysis: '_6764.ConceptCouplingConnectionLoadCase') -> '_2663.ConceptCouplingConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_coupling_connection(self, design_entity: '_2298.CouplingConnection') -> '_2675.CouplingConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_coupling_connection_load_case(self, design_entity_analysis: '_6777.CouplingConnectionLoadCase') -> '_2675.CouplingConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_spring_damper_connection(self, design_entity: '_2302.SpringDamperConnection') -> '_2756.SpringDamperConnectionSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperConnectionSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_abstract_shaft(self, design_entity: '_2388.AbstractShaft') -> '_2638.AbstractShaftSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaft)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_abstract_shaft_load_case(self, design_entity_analysis: '_6734.AbstractShaftLoadCase') -> '_2638.AbstractShaftSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_abstract_assembly(self, design_entity: '_2387.AbstractAssembly') -> '_2636.AbstractAssemblySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_abstract_assembly_load_case(self, design_entity_analysis: '_6733.AbstractAssemblyLoadCase') -> '_2636.AbstractAssemblySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_abstract_shaft_or_housing(self, design_entity: '_2389.AbstractShaftOrHousing') -> '_2637.AbstractShaftOrHousingSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftOrHousingSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_abstract_shaft_or_housing_load_case(self, design_entity_analysis: '_6735.AbstractShaftOrHousingLoadCase') -> '_2637.AbstractShaftOrHousingSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftOrHousingSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bearing(self, design_entity: '_2392.Bearing') -> '_2644.BearingSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BearingSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEARING](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bearing_load_case(self, design_entity_analysis: '_6746.BearingLoadCase') -> '_2644.BearingSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BearingSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEARING_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bolt(self, design_entity: '_2394.Bolt') -> '_2656.BoltSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BoltSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BOLT](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bolt_load_case(self, design_entity_analysis: '_6758.BoltLoadCase') -> '_2656.BoltSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BoltSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BOLT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bolted_joint(self, design_entity: '_2395.BoltedJoint') -> '_2655.BoltedJointSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BoltedJointSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bolted_joint_load_case(self, design_entity_analysis: '_6757.BoltedJointLoadCase') -> '_2655.BoltedJointSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BoltedJointSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_component(self, design_entity: '_2396.Component') -> '_2661.ComponentSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_COMPONENT](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_component_load_case(self, design_entity_analysis: '_6763.ComponentLoadCase') -> '_2661.ComponentSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_COMPONENT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_connector(self, design_entity: '_2399.Connector') -> '_2674.ConnectorSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTOR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_connector_load_case(self, design_entity_analysis: '_6776.ConnectorLoadCase') -> '_2674.ConnectorSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTOR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_datum(self, design_entity: '_2400.Datum') -> '_2697.DatumSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.DatumSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_DATUM](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_datum_load_case(self, design_entity_analysis: '_6795.DatumLoadCase') -> '_2697.DatumSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.DatumSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_DATUM_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_external_cad_model(self, design_entity: '_2404.ExternalCADModel') -> '_2698.ExternalCADModelSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ExternalCADModelSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_external_cad_model_load_case(self, design_entity_analysis: '_6809.ExternalCADModelLoadCase') -> '_2698.ExternalCADModelSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ExternalCADModelSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_fe_part(self, design_entity: '_2405.FEPart') -> '_2703.FEPartSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FEPart)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FEPartSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_FE_PART](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_fe_part_load_case(self, design_entity_analysis: '_6813.FEPartLoadCase') -> '_2703.FEPartSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FEPartSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_FE_PART_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_flexible_pin_assembly(self, design_entity: '_2406.FlexiblePinAssembly') -> '_2704.FlexiblePinAssemblySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FlexiblePinAssemblySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_flexible_pin_assembly_load_case(self, design_entity_analysis: '_6814.FlexiblePinAssemblyLoadCase') -> '_2704.FlexiblePinAssemblySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FlexiblePinAssemblySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_assembly(self, design_entity: '_2386.Assembly') -> '_2643.AssemblySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AssemblySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ASSEMBLY](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_assembly_load_case(self, design_entity_analysis: '_6745.AssemblyLoadCase') -> '_2643.AssemblySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AssemblySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ASSEMBLY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_guide_dxf_model(self, design_entity: '_2407.GuideDxfModel') -> '_2708.GuideDxfModelSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GuideDxfModelSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_guide_dxf_model_load_case(self, design_entity_analysis: '_6822.GuideDxfModelLoadCase') -> '_2708.GuideDxfModelSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GuideDxfModelSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_mass_disc(self, design_entity: '_2414.MassDisc') -> '_2725.MassDiscSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MassDiscSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_MASS_DISC](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_mass_disc_load_case(self, design_entity_analysis: '_6847.MassDiscLoadCase') -> '_2725.MassDiscSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MassDiscSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_MASS_DISC_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_measurement_component(self, design_entity: '_2415.MeasurementComponent') -> '_2726.MeasurementComponentSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MeasurementComponentSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_measurement_component_load_case(self, design_entity_analysis: '_6848.MeasurementComponentLoadCase') -> '_2726.MeasurementComponentSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MeasurementComponentSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_mountable_component(self, design_entity: '_2416.MountableComponent') -> '_2728.MountableComponentSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_mountable_component_load_case(self, design_entity_analysis: '_6850.MountableComponentLoadCase') -> '_2728.MountableComponentSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_oil_seal(self, design_entity: '_2418.OilSeal') -> '_2730.OilSealSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.OilSealSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_OIL_SEAL](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_oil_seal_load_case(self, design_entity_analysis: '_6852.OilSealLoadCase') -> '_2730.OilSealSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.OilSealSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_OIL_SEAL_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_part(self, design_entity: '_2420.Part') -> '_2731.PartSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PART](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_part_load_case(self, design_entity_analysis: '_6854.PartLoadCase') -> '_2731.PartSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PART_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_planet_carrier(self, design_entity: '_2421.PlanetCarrier') -> '_2736.PlanetCarrierSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PlanetCarrierSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_planet_carrier_load_case(self, design_entity_analysis: '_6861.PlanetCarrierLoadCase') -> '_2736.PlanetCarrierSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PlanetCarrierSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_point_load(self, design_entity: '_2423.PointLoad') -> '_2737.PointLoadSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PointLoadSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_POINT_LOAD](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_point_load_load_case(self, design_entity_analysis: '_6864.PointLoadLoadCase') -> '_2737.PointLoadSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PointLoadSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_POINT_LOAD_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_power_load(self, design_entity: '_2424.PowerLoad') -> '_2738.PowerLoadSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PowerLoadSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_POWER_LOAD](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_power_load_load_case(self, design_entity_analysis: '_6865.PowerLoadLoadCase') -> '_2738.PowerLoadSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PowerLoadSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_POWER_LOAD_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_root_assembly(self, design_entity: '_2426.RootAssembly') -> '_2746.RootAssemblySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RootAssemblySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_root_assembly_load_case(self, design_entity_analysis: '_6874.RootAssemblyLoadCase') -> '_2746.RootAssemblySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RootAssemblySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_specialised_assembly(self, design_entity: '_2428.SpecialisedAssembly') -> '_2752.SpecialisedAssemblySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_specialised_assembly_load_case(self, design_entity_analysis: '_6878.SpecialisedAssemblyLoadCase') -> '_2752.SpecialisedAssemblySystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_unbalanced_mass(self, design_entity: '_2429.UnbalancedMass') -> '_2780.UnbalancedMassSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.UnbalancedMassSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_unbalanced_mass_load_case(self, design_entity_analysis: '_6906.UnbalancedMassLoadCase') -> '_2780.UnbalancedMassSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.UnbalancedMassSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_virtual_component(self, design_entity: '_2431.VirtualComponent') -> '_2781.VirtualComponentSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_virtual_component_load_case(self, design_entity_analysis: '_6907.VirtualComponentLoadCase') -> '_2781.VirtualComponentSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_shaft(self, design_entity: '_2434.Shaft') -> '_2750.ShaftSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_shaft_load_case(self, design_entity_analysis: '_6876.ShaftLoadCase') -> '_2750.ShaftSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_concept_gear(self, design_entity: '_2472.ConceptGear') -> '_2668.ConceptGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_concept_gear_load_case(self, design_entity_analysis: '_6767.ConceptGearLoadCase') -> '_2668.ConceptGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_concept_gear_set(self, design_entity: '_2473.ConceptGearSet') -> '_2667.ConceptGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_concept_gear_set_load_case(self, design_entity_analysis: '_6769.ConceptGearSetLoadCase') -> '_2667.ConceptGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_face_gear(self, design_entity: '_2479.FaceGear') -> '_2702.FaceGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_face_gear_load_case(self, design_entity_analysis: '_6810.FaceGearLoadCase') -> '_2702.FaceGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_face_gear_set(self, design_entity: '_2480.FaceGearSet') -> '_2701.FaceGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_face_gear_set_load_case(self, design_entity_analysis: '_6812.FaceGearSetLoadCase') -> '_2701.FaceGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2464.AGMAGleasonConicalGear') -> '_2642.AGMAGleasonConicalGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_agma_gleason_conical_gear_load_case(self, design_entity_analysis: '_6740.AGMAGleasonConicalGearLoadCase') -> '_2642.AGMAGleasonConicalGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2465.AGMAGleasonConicalGearSet') -> '_2641.AGMAGleasonConicalGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_agma_gleason_conical_gear_set_load_case(self, design_entity_analysis: '_6742.AGMAGleasonConicalGearSetLoadCase') -> '_2641.AGMAGleasonConicalGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_differential_gear(self, design_entity: '_2466.BevelDifferentialGear') -> '_2649.BevelDifferentialGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_differential_gear_load_case(self, design_entity_analysis: '_6749.BevelDifferentialGearLoadCase') -> '_2649.BevelDifferentialGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_differential_gear_set(self, design_entity: '_2467.BevelDifferentialGearSet') -> '_2648.BevelDifferentialGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_differential_gear_set_load_case(self, design_entity_analysis: '_6751.BevelDifferentialGearSetLoadCase') -> '_2648.BevelDifferentialGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2468.BevelDifferentialPlanetGear') -> '_2650.BevelDifferentialPlanetGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialPlanetGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_PLANET_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_differential_planet_gear_load_case(self, design_entity_analysis: '_6752.BevelDifferentialPlanetGearLoadCase') -> '_2650.BevelDifferentialPlanetGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialPlanetGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2469.BevelDifferentialSunGear') -> '_2651.BevelDifferentialSunGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialSunGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_differential_sun_gear_load_case(self, design_entity_analysis: '_6753.BevelDifferentialSunGearLoadCase') -> '_2651.BevelDifferentialSunGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialSunGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_gear(self, design_entity: '_2470.BevelGear') -> '_2654.BevelGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_gear_load_case(self, design_entity_analysis: '_6754.BevelGearLoadCase') -> '_2654.BevelGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_gear_set(self, design_entity: '_2471.BevelGearSet') -> '_2653.BevelGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_bevel_gear_set_load_case(self, design_entity_analysis: '_6756.BevelGearSetLoadCase') -> '_2653.BevelGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_conical_gear(self, design_entity: '_2474.ConicalGear') -> '_2672.ConicalGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_conical_gear_load_case(self, design_entity_analysis: '_6770.ConicalGearLoadCase') -> '_2672.ConicalGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_conical_gear_set(self, design_entity: '_2475.ConicalGearSet') -> '_2671.ConicalGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_conical_gear_set_load_case(self, design_entity_analysis: '_6774.ConicalGearSetLoadCase') -> '_2671.ConicalGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cylindrical_gear(self, design_entity: '_2476.CylindricalGear') -> '_2693.CylindricalGearSystemDeflectionWithLTCAResults':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflectionWithLTCAResults
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cylindrical_gear_load_case(self, design_entity_analysis: '_6787.CylindricalGearLoadCase') -> '_2693.CylindricalGearSystemDeflectionWithLTCAResults':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflectionWithLTCAResults
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cylindrical_gear_set(self, design_entity: '_2477.CylindricalGearSet') -> '_2690.CylindricalGearSetSystemDeflectionWithLTCAResults':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflectionWithLTCAResults
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cylindrical_gear_set_load_case(self, design_entity_analysis: '_6791.CylindricalGearSetLoadCase') -> '_2690.CylindricalGearSetSystemDeflectionWithLTCAResults':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflectionWithLTCAResults
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cylindrical_planet_gear(self, design_entity: '_2478.CylindricalPlanetGear') -> '_2696.CylindricalPlanetGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalPlanetGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_cylindrical_planet_gear_load_case(self, design_entity_analysis: '_6792.CylindricalPlanetGearLoadCase') -> '_2696.CylindricalPlanetGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalPlanetGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_gear(self, design_entity: '_2481.Gear') -> '_2707.GearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_gear_load_case(self, design_entity_analysis: '_6816.GearLoadCase') -> '_2707.GearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_gear_set(self, design_entity: '_2483.GearSet') -> '_2706.GearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_gear_set_load_case(self, design_entity_analysis: '_6821.GearSetLoadCase') -> '_2706.GearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_hypoid_gear(self, design_entity: '_2485.HypoidGear') -> '_2711.HypoidGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_hypoid_gear_load_case(self, design_entity_analysis: '_6831.HypoidGearLoadCase') -> '_2711.HypoidGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_hypoid_gear_set(self, design_entity: '_2486.HypoidGearSet') -> '_2710.HypoidGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_hypoid_gear_set_load_case(self, design_entity_analysis: '_6833.HypoidGearSetLoadCase') -> '_2710.HypoidGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2487.KlingelnbergCycloPalloidConicalGear') -> '_2716.KlingelnbergCycloPalloidConicalGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(self, design_entity_analysis: '_6838.KlingelnbergCycloPalloidConicalGearLoadCase') -> '_2716.KlingelnbergCycloPalloidConicalGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2488.KlingelnbergCycloPalloidConicalGearSet') -> '_2715.KlingelnbergCycloPalloidConicalGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self, design_entity_analysis: '_6840.KlingelnbergCycloPalloidConicalGearSetLoadCase') -> '_2715.KlingelnbergCycloPalloidConicalGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2489.KlingelnbergCycloPalloidHypoidGear') -> '_2719.KlingelnbergCycloPalloidHypoidGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(self, design_entity_analysis: '_6841.KlingelnbergCycloPalloidHypoidGearLoadCase') -> '_2719.KlingelnbergCycloPalloidHypoidGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2490.KlingelnbergCycloPalloidHypoidGearSet') -> '_2718.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self, design_entity_analysis: '_6843.KlingelnbergCycloPalloidHypoidGearSetLoadCase') -> '_2718.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2491.KlingelnbergCycloPalloidSpiralBevelGear') -> '_2722.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6844.KlingelnbergCycloPalloidSpiralBevelGearLoadCase') -> '_2722.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2492.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_2721.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6846.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase') -> '_2721.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_planetary_gear_set(self, design_entity: '_2493.PlanetaryGearSet') -> '_2690.CylindricalGearSetSystemDeflectionWithLTCAResults':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflectionWithLTCAResults
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_planetary_gear_set_load_case(self, design_entity_analysis: '_6859.PlanetaryGearSetLoadCase') -> '_2690.CylindricalGearSetSystemDeflectionWithLTCAResults':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflectionWithLTCAResults
        """

        method_result = self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_spiral_bevel_gear(self, design_entity: '_2494.SpiralBevelGear') -> '_2755.SpiralBevelGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6879.SpiralBevelGearLoadCase') -> '_2755.SpiralBevelGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2495.SpiralBevelGearSet') -> '_2754.SpiralBevelGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6881.SpiralBevelGearSetLoadCase') -> '_2754.SpiralBevelGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2496.StraightBevelDiffGear') -> '_2761.StraightBevelDiffGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_diff_gear_load_case(self, design_entity_analysis: '_6885.StraightBevelDiffGearLoadCase') -> '_2761.StraightBevelDiffGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2497.StraightBevelDiffGearSet') -> '_2760.StraightBevelDiffGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_diff_gear_set_load_case(self, design_entity_analysis: '_6887.StraightBevelDiffGearSetLoadCase') -> '_2760.StraightBevelDiffGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_gear(self, design_entity: '_2498.StraightBevelGear') -> '_2764.StraightBevelGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_gear_load_case(self, design_entity_analysis: '_6888.StraightBevelGearLoadCase') -> '_2764.StraightBevelGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_gear_set(self, design_entity: '_2499.StraightBevelGearSet') -> '_2763.StraightBevelGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_gear_set_load_case(self, design_entity_analysis: '_6890.StraightBevelGearSetLoadCase') -> '_2763.StraightBevelGearSetSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSetSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2500.StraightBevelPlanetGear') -> '_2765.StraightBevelPlanetGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelPlanetGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_planet_gear_load_case(self, design_entity_analysis: '_6891.StraightBevelPlanetGearLoadCase') -> '_2765.StraightBevelPlanetGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelPlanetGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2501.StraightBevelSunGear') -> '_2766.StraightBevelSunGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelSunGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_straight_bevel_sun_gear_load_case(self, design_entity_analysis: '_6892.StraightBevelSunGearLoadCase') -> '_2766.StraightBevelSunGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelSunGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_worm_gear(self, design_entity: '_2502.WormGear') -> '_2784.WormGearSystemDeflection':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearSystemDeflection
        """

        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None
