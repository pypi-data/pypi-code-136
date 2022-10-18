"""_2386.py

Assembly
"""


from typing import List, TypeVar, Optional

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import (
    _2417, _2392, _2395, _2396,
    _2405, _2418, _2423, _2424,
    _2420, _2387, _2388, _2389,
    _2394, _2399, _2400, _2404,
    _2406, _2407, _2414, _2415,
    _2416, _2421, _2426, _2428,
    _2429, _2431
)
from mastapy.system_model.part_model.gears import (
    _2475, _2477, _2480, _2483,
    _2486, _2488, _2495, _2499,
    _2503, _2464, _2465, _2466,
    _2467, _2468, _2469, _2470,
    _2471, _2472, _2473, _2474,
    _2476, _2478, _2479, _2481,
    _2485, _2487, _2489, _2490,
    _2491, _2492, _2493, _2494,
    _2496, _2497, _2498, _2500,
    _2501, _2502, _2504, _2505
)
from mastapy.system_model.part_model.couplings import (
    _2549, _2527, _2529, _2530,
    _2532, _2533, _2534, _2535,
    _2537, _2538, _2539, _2540,
    _2541, _2547, _2548, _2551,
    _2552, _2553, _2555, _2556,
    _2557, _2558, _2559, _2561
)
from mastapy.system_model.part_model.shaft_model import _2434
from mastapy.system_model.part_model.cycloidal import _2519, _2520, _2521
from mastapy.bearings import _1857, _1830
from mastapy.system_model.part_model.creation_options import (
    _2522, _2523, _2524, _2525,
    _2526
)
from mastapy.gears.gear_designs.creation_options import _1136, _1139
from mastapy._internal.python_net import python_net_import
from mastapy.gears import _327
from mastapy.gears.gear_designs.bevel import _1169
from mastapy.nodal_analysis import _78

_ARRAY = python_net_import('System', 'Array')
_STRING = python_net_import('System', 'String')
_DOUBLE = python_net_import('System', 'Double')
_INT_32 = python_net_import('System', 'Int32')
_ROLLING_BEARING_TYPE = python_net_import('SMT.MastaAPI.Bearings', 'RollingBearingType')
_BELT_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.CreationOptions', 'BeltCreationOptions')
_CYCLOIDAL_ASSEMBLY_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.CreationOptions', 'CycloidalAssemblyCreationOptions')
_CYLINDRICAL_GEAR_LINEAR_TRAIN_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.CreationOptions', 'CylindricalGearLinearTrainCreationOptions')
_PLANET_CARRIER_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.CreationOptions', 'PlanetCarrierCreationOptions')
_SHAFT_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.CreationOptions', 'ShaftCreationOptions')
_CYLINDRICAL_GEAR_PAIR_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.CreationOptions', 'CylindricalGearPairCreationOptions')
_SPIRAL_BEVEL_GEAR_SET_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.CreationOptions', 'SpiralBevelGearSetCreationOptions')
_HAND = python_net_import('SMT.MastaAPI.Gears', 'Hand')
_AGMA_GLEASON_CONICAL_GEAR_GEOMETRY_METHODS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Bevel', 'AGMAGleasonConicalGearGeometryMethods')
_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Assembly')


__docformat__ = 'restructuredtext en'
__all__ = ('Assembly',)


class Assembly(_2387.AbstractAssembly):
    """Assembly

    This is a mastapy class.
    """

    TYPE = _ASSEMBLY

    def __init__(self, instance_to_wrap: 'Assembly.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'AxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width_of_widest_cylindrical_gear(self) -> 'float':
        """float: 'FaceWidthOfWidestCylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceWidthOfWidestCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def largest_number_of_teeth(self) -> 'int':
        """int: 'LargestNumberOfTeeth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LargestNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @property
    def mass_of_bearings(self) -> 'float':
        """float: 'MassOfBearings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassOfBearings

        if temp is None:
            return 0.0

        return temp

    @property
    def mass_of_fe_part_housings(self) -> 'float':
        """float: 'MassOfFEPartHousings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassOfFEPartHousings

        if temp is None:
            return 0.0

        return temp

    @property
    def mass_of_fe_part_shafts(self) -> 'float':
        """float: 'MassOfFEPartShafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassOfFEPartShafts

        if temp is None:
            return 0.0

        return temp

    @property
    def mass_of_gears(self) -> 'float':
        """float: 'MassOfGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassOfGears

        if temp is None:
            return 0.0

        return temp

    @property
    def mass_of_other_parts(self) -> 'float':
        """float: 'MassOfOtherParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassOfOtherParts

        if temp is None:
            return 0.0

        return temp

    @property
    def mass_of_shafts(self) -> 'float':
        """float: 'MassOfShafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassOfShafts

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_tip_thickness(self) -> 'float':
        """float: 'MinimumTipThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumTipThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def smallest_number_of_teeth(self) -> 'int':
        """int: 'SmallestNumberOfTeeth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @property
    def transverse_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'TransverseContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_and_axial_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'TransverseAndAxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseAndAxialContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def oil_level_specification(self) -> '_2417.OilLevelSpecification':
        """OilLevelSpecification: 'OilLevelSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilLevelSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearings(self) -> 'List[_2392.Bearing]':
        """List[Bearing]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolted_joints(self) -> 'List[_2395.BoltedJoint]':
        """List[BoltedJoint]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltedJoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_details(self) -> 'List[_2396.Component]':
        """List[Component]: 'ComponentDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def components_with_unknown_scalar_mass(self) -> 'List[_2396.Component]':
        """List[Component]: 'ComponentsWithUnknownScalarMass' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentsWithUnknownScalarMass

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def conical_gear_sets(self) -> 'List[_2475.ConicalGearSet]':
        """List[ConicalGearSet]: 'ConicalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_2477.CylindricalGearSet]':
        """List[CylindricalGearSet]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def fe_parts(self) -> 'List[_2405.FEPart]':
        """List[FEPart]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gear_sets(self) -> 'List[_2480.FaceGearSet]':
        """List[FaceGearSet]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_sets(self) -> 'List[_2483.GearSet]':
        """List[GearSet]: 'GearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_2486.HypoidGearSet]':
        """List[HypoidGearSet]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_gear_sets(self) -> 'List[_2488.KlingelnbergCycloPalloidConicalGearSet]':
        """List[KlingelnbergCycloPalloidConicalGearSet]: 'KlingelnbergCycloPalloidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def oil_seals(self) -> 'List[_2418.OilSeal]':
        """List[OilSeal]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilSeals

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def point_loads(self) -> 'List[_2423.PointLoad]':
        """List[PointLoad]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_loads(self) -> 'List[_2424.PowerLoad]':
        """List[PowerLoad]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_2549.ShaftHubConnection]':
        """List[ShaftHubConnection]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftHubConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shafts(self) -> 'List[_2434.Shaft]':
        """List[Shaft]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shafts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_2495.SpiralBevelGearSet]':
        """List[SpiralBevelGearSet]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_2499.StraightBevelGearSet]':
        """List[StraightBevelGearSet]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gear_sets(self) -> 'List[_2503.WormGearSet]':
        """List[WormGearSet]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def get_part_named(self, name: 'str') -> '_2420.Part':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Part
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2420.Part.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_assembly(self, name: 'str') -> 'Assembly':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Assembly
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[Assembly.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_abstract_assembly(self, name: 'str') -> '_2387.AbstractAssembly':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.AbstractAssembly
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2387.AbstractAssembly.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_abstract_shaft(self, name: 'str') -> '_2388.AbstractShaft':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.AbstractShaft
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2388.AbstractShaft.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_abstract_shaft_or_housing(self, name: 'str') -> '_2389.AbstractShaftOrHousing':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.AbstractShaftOrHousing
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2389.AbstractShaftOrHousing.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_bearing(self, name: 'str') -> '_2392.Bearing':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Bearing
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2392.Bearing.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_bolt(self, name: 'str') -> '_2394.Bolt':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Bolt
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2394.Bolt.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_bolted_joint(self, name: 'str') -> '_2395.BoltedJoint':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.BoltedJoint
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2395.BoltedJoint.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_component(self, name: 'str') -> '_2396.Component':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Component
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2396.Component.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_connector(self, name: 'str') -> '_2399.Connector':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Connector
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2399.Connector.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_datum(self, name: 'str') -> '_2400.Datum':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Datum
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2400.Datum.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_external_cad_model(self, name: 'str') -> '_2404.ExternalCADModel':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.ExternalCADModel
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2404.ExternalCADModel.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_fe_part(self, name: 'str') -> '_2405.FEPart':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.FEPart
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2405.FEPart.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_flexible_pin_assembly(self, name: 'str') -> '_2406.FlexiblePinAssembly':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.FlexiblePinAssembly
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2406.FlexiblePinAssembly.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_guide_dxf_model(self, name: 'str') -> '_2407.GuideDxfModel':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.GuideDxfModel
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2407.GuideDxfModel.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_mass_disc(self, name: 'str') -> '_2414.MassDisc':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.MassDisc
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2414.MassDisc.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_measurement_component(self, name: 'str') -> '_2415.MeasurementComponent':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.MeasurementComponent
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2415.MeasurementComponent.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_mountable_component(self, name: 'str') -> '_2416.MountableComponent':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.MountableComponent
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2416.MountableComponent.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_oil_seal(self, name: 'str') -> '_2418.OilSeal':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.OilSeal
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2418.OilSeal.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_planet_carrier(self, name: 'str') -> '_2421.PlanetCarrier':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.PlanetCarrier
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2421.PlanetCarrier.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_point_load(self, name: 'str') -> '_2423.PointLoad':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.PointLoad
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2423.PointLoad.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_power_load(self, name: 'str') -> '_2424.PowerLoad':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.PowerLoad
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2424.PowerLoad.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_root_assembly(self, name: 'str') -> '_2426.RootAssembly':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.RootAssembly
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2426.RootAssembly.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_specialised_assembly(self, name: 'str') -> '_2428.SpecialisedAssembly':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.SpecialisedAssembly
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2428.SpecialisedAssembly.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_unbalanced_mass(self, name: 'str') -> '_2429.UnbalancedMass':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.UnbalancedMass
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2429.UnbalancedMass.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_virtual_component(self, name: 'str') -> '_2431.VirtualComponent':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.VirtualComponent
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2431.VirtualComponent.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_shaft(self, name: 'str') -> '_2434.Shaft':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.shaft_model.Shaft
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2434.Shaft.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_agma_gleason_conical_gear(self, name: 'str') -> '_2464.AGMAGleasonConicalGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.AGMAGleasonConicalGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2464.AGMAGleasonConicalGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_agma_gleason_conical_gear_set(self, name: 'str') -> '_2465.AGMAGleasonConicalGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2465.AGMAGleasonConicalGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_differential_gear(self, name: 'str') -> '_2466.BevelDifferentialGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.BevelDifferentialGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2466.BevelDifferentialGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_differential_gear_set(self, name: 'str') -> '_2467.BevelDifferentialGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.BevelDifferentialGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2467.BevelDifferentialGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_differential_planet_gear(self, name: 'str') -> '_2468.BevelDifferentialPlanetGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2468.BevelDifferentialPlanetGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_differential_sun_gear(self, name: 'str') -> '_2469.BevelDifferentialSunGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.BevelDifferentialSunGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2469.BevelDifferentialSunGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_gear(self, name: 'str') -> '_2470.BevelGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.BevelGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2470.BevelGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_gear_set(self, name: 'str') -> '_2471.BevelGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.BevelGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2471.BevelGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_concept_gear(self, name: 'str') -> '_2472.ConceptGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.ConceptGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2472.ConceptGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_concept_gear_set(self, name: 'str') -> '_2473.ConceptGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.ConceptGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2473.ConceptGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_conical_gear(self, name: 'str') -> '_2474.ConicalGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.ConicalGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2474.ConicalGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_conical_gear_set(self, name: 'str') -> '_2475.ConicalGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.ConicalGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2475.ConicalGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_cylindrical_gear(self, name: 'str') -> '_2476.CylindricalGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2476.CylindricalGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_cylindrical_gear_set(self, name: 'str') -> '_2477.CylindricalGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2477.CylindricalGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_cylindrical_planet_gear(self, name: 'str') -> '_2478.CylindricalPlanetGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.CylindricalPlanetGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2478.CylindricalPlanetGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_face_gear(self, name: 'str') -> '_2479.FaceGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.FaceGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2479.FaceGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_face_gear_set(self, name: 'str') -> '_2480.FaceGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.FaceGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2480.FaceGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_gear(self, name: 'str') -> '_2481.Gear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.Gear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2481.Gear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_gear_set(self, name: 'str') -> '_2483.GearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.GearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2483.GearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_hypoid_gear(self, name: 'str') -> '_2485.HypoidGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.HypoidGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2485.HypoidGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_hypoid_gear_set(self, name: 'str') -> '_2486.HypoidGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.HypoidGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2486.HypoidGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_conical_gear(self, name: 'str') -> '_2487.KlingelnbergCycloPalloidConicalGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2487.KlingelnbergCycloPalloidConicalGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self, name: 'str') -> '_2488.KlingelnbergCycloPalloidConicalGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2488.KlingelnbergCycloPalloidConicalGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self, name: 'str') -> '_2489.KlingelnbergCycloPalloidHypoidGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2489.KlingelnbergCycloPalloidHypoidGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self, name: 'str') -> '_2490.KlingelnbergCycloPalloidHypoidGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2490.KlingelnbergCycloPalloidHypoidGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, name: 'str') -> '_2491.KlingelnbergCycloPalloidSpiralBevelGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2491.KlingelnbergCycloPalloidSpiralBevelGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, name: 'str') -> '_2492.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2492.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_planetary_gear_set(self, name: 'str') -> '_2493.PlanetaryGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.PlanetaryGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2493.PlanetaryGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_spiral_bevel_gear(self, name: 'str') -> '_2494.SpiralBevelGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.SpiralBevelGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2494.SpiralBevelGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_spiral_bevel_gear_set(self, name: 'str') -> '_2495.SpiralBevelGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.SpiralBevelGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2495.SpiralBevelGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_diff_gear(self, name: 'str') -> '_2496.StraightBevelDiffGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelDiffGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2496.StraightBevelDiffGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_diff_gear_set(self, name: 'str') -> '_2497.StraightBevelDiffGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelDiffGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2497.StraightBevelDiffGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_gear(self, name: 'str') -> '_2498.StraightBevelGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2498.StraightBevelGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_gear_set(self, name: 'str') -> '_2499.StraightBevelGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2499.StraightBevelGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_planet_gear(self, name: 'str') -> '_2500.StraightBevelPlanetGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelPlanetGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2500.StraightBevelPlanetGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_sun_gear(self, name: 'str') -> '_2501.StraightBevelSunGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelSunGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2501.StraightBevelSunGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_worm_gear(self, name: 'str') -> '_2502.WormGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.WormGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2502.WormGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_worm_gear_set(self, name: 'str') -> '_2503.WormGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.WormGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2503.WormGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_zerol_bevel_gear(self, name: 'str') -> '_2504.ZerolBevelGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.ZerolBevelGear
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2504.ZerolBevelGear.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_zerol_bevel_gear_set(self, name: 'str') -> '_2505.ZerolBevelGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.gears.ZerolBevelGearSet
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2505.ZerolBevelGearSet.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_cycloidal_assembly(self, name: 'str') -> '_2519.CycloidalAssembly':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.cycloidal.CycloidalAssembly
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2519.CycloidalAssembly.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_cycloidal_disc(self, name: 'str') -> '_2520.CycloidalDisc':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.cycloidal.CycloidalDisc
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2520.CycloidalDisc.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_ring_pins(self, name: 'str') -> '_2521.RingPins':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.cycloidal.RingPins
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2521.RingPins.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_belt_drive(self, name: 'str') -> '_2527.BeltDrive':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.BeltDrive
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2527.BeltDrive.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_clutch(self, name: 'str') -> '_2529.Clutch':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.Clutch
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2529.Clutch.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_clutch_half(self, name: 'str') -> '_2530.ClutchHalf':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.ClutchHalf
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2530.ClutchHalf.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_concept_coupling(self, name: 'str') -> '_2532.ConceptCoupling':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.ConceptCoupling
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2532.ConceptCoupling.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_concept_coupling_half(self, name: 'str') -> '_2533.ConceptCouplingHalf':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.ConceptCouplingHalf
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2533.ConceptCouplingHalf.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_coupling(self, name: 'str') -> '_2534.Coupling':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.Coupling
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2534.Coupling.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_coupling_half(self, name: 'str') -> '_2535.CouplingHalf':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.CouplingHalf
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2535.CouplingHalf.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_cvt(self, name: 'str') -> '_2537.CVT':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.CVT
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2537.CVT.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_cvt_pulley(self, name: 'str') -> '_2538.CVTPulley':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.CVTPulley
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2538.CVTPulley.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_part_to_part_shear_coupling(self, name: 'str') -> '_2539.PartToPartShearCoupling':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.PartToPartShearCoupling
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2539.PartToPartShearCoupling.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_part_to_part_shear_coupling_half(self, name: 'str') -> '_2540.PartToPartShearCouplingHalf':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2540.PartToPartShearCouplingHalf.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_pulley(self, name: 'str') -> '_2541.Pulley':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.Pulley
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2541.Pulley.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_rolling_ring(self, name: 'str') -> '_2547.RollingRing':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.RollingRing
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2547.RollingRing.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_rolling_ring_assembly(self, name: 'str') -> '_2548.RollingRingAssembly':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.RollingRingAssembly
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2548.RollingRingAssembly.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_shaft_hub_connection(self, name: 'str') -> '_2549.ShaftHubConnection':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.ShaftHubConnection
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2549.ShaftHubConnection.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_spring_damper(self, name: 'str') -> '_2551.SpringDamper':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.SpringDamper
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2551.SpringDamper.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_spring_damper_half(self, name: 'str') -> '_2552.SpringDamperHalf':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.SpringDamperHalf
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2552.SpringDamperHalf.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_synchroniser(self, name: 'str') -> '_2553.Synchroniser':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.Synchroniser
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2553.Synchroniser.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_synchroniser_half(self, name: 'str') -> '_2555.SynchroniserHalf':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.SynchroniserHalf
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2555.SynchroniserHalf.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_synchroniser_part(self, name: 'str') -> '_2556.SynchroniserPart':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.SynchroniserPart
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2556.SynchroniserPart.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_synchroniser_sleeve(self, name: 'str') -> '_2557.SynchroniserSleeve':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.SynchroniserSleeve
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2557.SynchroniserSleeve.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_torque_converter(self, name: 'str') -> '_2558.TorqueConverter':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.TorqueConverter
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2558.TorqueConverter.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_torque_converter_pump(self, name: 'str') -> '_2559.TorqueConverterPump':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.TorqueConverterPump
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2559.TorqueConverterPump.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_part_named_of_type_torque_converter_turbine(self, name: 'str') -> '_2561.TorqueConverterTurbine':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.TorqueConverterTurbine
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2561.TorqueConverterTurbine.TYPE](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_part(self, part_type: 'Assembly.PartType', name: 'str') -> '_2420.Part':
        """ 'AddPart' is the original name of this method.

        Args:
            part_type (mastapy.system_model.part_model.Assembly.PartType)
            name (str)

        Returns:
            mastapy.system_model.part_model.Part
        """

        part_type = conversion.mp_to_pn_enum(part_type)
        name = str(name)
        method_result = self.wrapped.AddPart(part_type, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def all_parts(self) -> 'List[_2420.Part]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Part]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2420.Part.TYPE]())

    def all_parts_of_type_assembly(self) -> 'List[Assembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Assembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[Assembly.TYPE]())

    def all_parts_of_type_abstract_assembly(self) -> 'List[_2387.AbstractAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2387.AbstractAssembly.TYPE]())

    def all_parts_of_type_abstract_shaft(self) -> 'List[_2388.AbstractShaft]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractShaft]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2388.AbstractShaft.TYPE]())

    def all_parts_of_type_abstract_shaft_or_housing(self) -> 'List[_2389.AbstractShaftOrHousing]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractShaftOrHousing]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2389.AbstractShaftOrHousing.TYPE]())

    def all_parts_of_type_bearing(self) -> 'List[_2392.Bearing]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Bearing]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2392.Bearing.TYPE]())

    def all_parts_of_type_bolt(self) -> 'List[_2394.Bolt]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Bolt]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2394.Bolt.TYPE]())

    def all_parts_of_type_bolted_joint(self) -> 'List[_2395.BoltedJoint]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.BoltedJoint]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2395.BoltedJoint.TYPE]())

    def all_parts_of_type_component(self) -> 'List[_2396.Component]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Component]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2396.Component.TYPE]())

    def all_parts_of_type_connector(self) -> 'List[_2399.Connector]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Connector]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2399.Connector.TYPE]())

    def all_parts_of_type_datum(self) -> 'List[_2400.Datum]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Datum]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2400.Datum.TYPE]())

    def all_parts_of_type_external_cad_model(self) -> 'List[_2404.ExternalCADModel]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.ExternalCADModel]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2404.ExternalCADModel.TYPE]())

    def all_parts_of_type_fe_part(self) -> 'List[_2405.FEPart]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.FEPart]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2405.FEPart.TYPE]())

    def all_parts_of_type_flexible_pin_assembly(self) -> 'List[_2406.FlexiblePinAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.FlexiblePinAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2406.FlexiblePinAssembly.TYPE]())

    def all_parts_of_type_guide_dxf_model(self) -> 'List[_2407.GuideDxfModel]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.GuideDxfModel]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2407.GuideDxfModel.TYPE]())

    def all_parts_of_type_mass_disc(self) -> 'List[_2414.MassDisc]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MassDisc]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2414.MassDisc.TYPE]())

    def all_parts_of_type_measurement_component(self) -> 'List[_2415.MeasurementComponent]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MeasurementComponent]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2415.MeasurementComponent.TYPE]())

    def all_parts_of_type_mountable_component(self) -> 'List[_2416.MountableComponent]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MountableComponent]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2416.MountableComponent.TYPE]())

    def all_parts_of_type_oil_seal(self) -> 'List[_2418.OilSeal]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.OilSeal]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2418.OilSeal.TYPE]())

    def all_parts_of_type_planet_carrier(self) -> 'List[_2421.PlanetCarrier]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PlanetCarrier]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2421.PlanetCarrier.TYPE]())

    def all_parts_of_type_point_load(self) -> 'List[_2423.PointLoad]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PointLoad]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2423.PointLoad.TYPE]())

    def all_parts_of_type_power_load(self) -> 'List[_2424.PowerLoad]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PowerLoad]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2424.PowerLoad.TYPE]())

    def all_parts_of_type_root_assembly(self) -> 'List[_2426.RootAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.RootAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2426.RootAssembly.TYPE]())

    def all_parts_of_type_specialised_assembly(self) -> 'List[_2428.SpecialisedAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.SpecialisedAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2428.SpecialisedAssembly.TYPE]())

    def all_parts_of_type_unbalanced_mass(self) -> 'List[_2429.UnbalancedMass]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.UnbalancedMass]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2429.UnbalancedMass.TYPE]())

    def all_parts_of_type_virtual_component(self) -> 'List[_2431.VirtualComponent]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.VirtualComponent]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2431.VirtualComponent.TYPE]())

    def all_parts_of_type_shaft(self) -> 'List[_2434.Shaft]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.shaft_model.Shaft]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2434.Shaft.TYPE]())

    def all_parts_of_type_agma_gleason_conical_gear(self) -> 'List[_2464.AGMAGleasonConicalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2464.AGMAGleasonConicalGear.TYPE]())

    def all_parts_of_type_agma_gleason_conical_gear_set(self) -> 'List[_2465.AGMAGleasonConicalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2465.AGMAGleasonConicalGearSet.TYPE]())

    def all_parts_of_type_bevel_differential_gear(self) -> 'List[_2466.BevelDifferentialGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2466.BevelDifferentialGear.TYPE]())

    def all_parts_of_type_bevel_differential_gear_set(self) -> 'List[_2467.BevelDifferentialGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2467.BevelDifferentialGearSet.TYPE]())

    def all_parts_of_type_bevel_differential_planet_gear(self) -> 'List[_2468.BevelDifferentialPlanetGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2468.BevelDifferentialPlanetGear.TYPE]())

    def all_parts_of_type_bevel_differential_sun_gear(self) -> 'List[_2469.BevelDifferentialSunGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialSunGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2469.BevelDifferentialSunGear.TYPE]())

    def all_parts_of_type_bevel_gear(self) -> 'List[_2470.BevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2470.BevelGear.TYPE]())

    def all_parts_of_type_bevel_gear_set(self) -> 'List[_2471.BevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2471.BevelGearSet.TYPE]())

    def all_parts_of_type_concept_gear(self) -> 'List[_2472.ConceptGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConceptGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2472.ConceptGear.TYPE]())

    def all_parts_of_type_concept_gear_set(self) -> 'List[_2473.ConceptGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConceptGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2473.ConceptGearSet.TYPE]())

    def all_parts_of_type_conical_gear(self) -> 'List[_2474.ConicalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConicalGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2474.ConicalGear.TYPE]())

    def all_parts_of_type_conical_gear_set(self) -> 'List[_2475.ConicalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConicalGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2475.ConicalGearSet.TYPE]())

    def all_parts_of_type_cylindrical_gear(self) -> 'List[_2476.CylindricalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2476.CylindricalGear.TYPE]())

    def all_parts_of_type_cylindrical_gear_set(self) -> 'List[_2477.CylindricalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2477.CylindricalGearSet.TYPE]())

    def all_parts_of_type_cylindrical_planet_gear(self) -> 'List[_2478.CylindricalPlanetGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalPlanetGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2478.CylindricalPlanetGear.TYPE]())

    def all_parts_of_type_face_gear(self) -> 'List[_2479.FaceGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.FaceGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2479.FaceGear.TYPE]())

    def all_parts_of_type_face_gear_set(self) -> 'List[_2480.FaceGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.FaceGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2480.FaceGearSet.TYPE]())

    def all_parts_of_type_gear(self) -> 'List[_2481.Gear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.Gear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2481.Gear.TYPE]())

    def all_parts_of_type_gear_set(self) -> 'List[_2483.GearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.GearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2483.GearSet.TYPE]())

    def all_parts_of_type_hypoid_gear(self) -> 'List[_2485.HypoidGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.HypoidGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2485.HypoidGear.TYPE]())

    def all_parts_of_type_hypoid_gear_set(self) -> 'List[_2486.HypoidGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.HypoidGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2486.HypoidGearSet.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> 'List[_2487.KlingelnbergCycloPalloidConicalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2487.KlingelnbergCycloPalloidConicalGear.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> 'List[_2488.KlingelnbergCycloPalloidConicalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2488.KlingelnbergCycloPalloidConicalGearSet.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> 'List[_2489.KlingelnbergCycloPalloidHypoidGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2489.KlingelnbergCycloPalloidHypoidGear.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> 'List[_2490.KlingelnbergCycloPalloidHypoidGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2490.KlingelnbergCycloPalloidHypoidGearSet.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> 'List[_2491.KlingelnbergCycloPalloidSpiralBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2491.KlingelnbergCycloPalloidSpiralBevelGear.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> 'List[_2492.KlingelnbergCycloPalloidSpiralBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2492.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE]())

    def all_parts_of_type_planetary_gear_set(self) -> 'List[_2493.PlanetaryGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.PlanetaryGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2493.PlanetaryGearSet.TYPE]())

    def all_parts_of_type_spiral_bevel_gear(self) -> 'List[_2494.SpiralBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.SpiralBevelGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2494.SpiralBevelGear.TYPE]())

    def all_parts_of_type_spiral_bevel_gear_set(self) -> 'List[_2495.SpiralBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.SpiralBevelGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2495.SpiralBevelGearSet.TYPE]())

    def all_parts_of_type_straight_bevel_diff_gear(self) -> 'List[_2496.StraightBevelDiffGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelDiffGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2496.StraightBevelDiffGear.TYPE]())

    def all_parts_of_type_straight_bevel_diff_gear_set(self) -> 'List[_2497.StraightBevelDiffGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelDiffGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2497.StraightBevelDiffGearSet.TYPE]())

    def all_parts_of_type_straight_bevel_gear(self) -> 'List[_2498.StraightBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2498.StraightBevelGear.TYPE]())

    def all_parts_of_type_straight_bevel_gear_set(self) -> 'List[_2499.StraightBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2499.StraightBevelGearSet.TYPE]())

    def all_parts_of_type_straight_bevel_planet_gear(self) -> 'List[_2500.StraightBevelPlanetGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelPlanetGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2500.StraightBevelPlanetGear.TYPE]())

    def all_parts_of_type_straight_bevel_sun_gear(self) -> 'List[_2501.StraightBevelSunGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelSunGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2501.StraightBevelSunGear.TYPE]())

    def all_parts_of_type_worm_gear(self) -> 'List[_2502.WormGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.WormGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2502.WormGear.TYPE]())

    def all_parts_of_type_worm_gear_set(self) -> 'List[_2503.WormGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.WormGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2503.WormGearSet.TYPE]())

    def all_parts_of_type_zerol_bevel_gear(self) -> 'List[_2504.ZerolBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ZerolBevelGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2504.ZerolBevelGear.TYPE]())

    def all_parts_of_type_zerol_bevel_gear_set(self) -> 'List[_2505.ZerolBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ZerolBevelGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2505.ZerolBevelGearSet.TYPE]())

    def all_parts_of_type_cycloidal_assembly(self) -> 'List[_2519.CycloidalAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.CycloidalAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2519.CycloidalAssembly.TYPE]())

    def all_parts_of_type_cycloidal_disc(self) -> 'List[_2520.CycloidalDisc]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.CycloidalDisc]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2520.CycloidalDisc.TYPE]())

    def all_parts_of_type_ring_pins(self) -> 'List[_2521.RingPins]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.RingPins]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2521.RingPins.TYPE]())

    def all_parts_of_type_belt_drive(self) -> 'List[_2527.BeltDrive]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.BeltDrive]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2527.BeltDrive.TYPE]())

    def all_parts_of_type_clutch(self) -> 'List[_2529.Clutch]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Clutch]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2529.Clutch.TYPE]())

    def all_parts_of_type_clutch_half(self) -> 'List[_2530.ClutchHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ClutchHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2530.ClutchHalf.TYPE]())

    def all_parts_of_type_concept_coupling(self) -> 'List[_2532.ConceptCoupling]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ConceptCoupling]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2532.ConceptCoupling.TYPE]())

    def all_parts_of_type_concept_coupling_half(self) -> 'List[_2533.ConceptCouplingHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ConceptCouplingHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2533.ConceptCouplingHalf.TYPE]())

    def all_parts_of_type_coupling(self) -> 'List[_2534.Coupling]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Coupling]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2534.Coupling.TYPE]())

    def all_parts_of_type_coupling_half(self) -> 'List[_2535.CouplingHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CouplingHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2535.CouplingHalf.TYPE]())

    def all_parts_of_type_cvt(self) -> 'List[_2537.CVT]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CVT]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2537.CVT.TYPE]())

    def all_parts_of_type_cvt_pulley(self) -> 'List[_2538.CVTPulley]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CVTPulley]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2538.CVTPulley.TYPE]())

    def all_parts_of_type_part_to_part_shear_coupling(self) -> 'List[_2539.PartToPartShearCoupling]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.PartToPartShearCoupling]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2539.PartToPartShearCoupling.TYPE]())

    def all_parts_of_type_part_to_part_shear_coupling_half(self) -> 'List[_2540.PartToPartShearCouplingHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2540.PartToPartShearCouplingHalf.TYPE]())

    def all_parts_of_type_pulley(self) -> 'List[_2541.Pulley]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Pulley]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2541.Pulley.TYPE]())

    def all_parts_of_type_rolling_ring(self) -> 'List[_2547.RollingRing]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.RollingRing]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2547.RollingRing.TYPE]())

    def all_parts_of_type_rolling_ring_assembly(self) -> 'List[_2548.RollingRingAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.RollingRingAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2548.RollingRingAssembly.TYPE]())

    def all_parts_of_type_shaft_hub_connection(self) -> 'List[_2549.ShaftHubConnection]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ShaftHubConnection]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2549.ShaftHubConnection.TYPE]())

    def all_parts_of_type_spring_damper(self) -> 'List[_2551.SpringDamper]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SpringDamper]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2551.SpringDamper.TYPE]())

    def all_parts_of_type_spring_damper_half(self) -> 'List[_2552.SpringDamperHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SpringDamperHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2552.SpringDamperHalf.TYPE]())

    def all_parts_of_type_synchroniser(self) -> 'List[_2553.Synchroniser]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Synchroniser]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2553.Synchroniser.TYPE]())

    def all_parts_of_type_synchroniser_half(self) -> 'List[_2555.SynchroniserHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2555.SynchroniserHalf.TYPE]())

    def all_parts_of_type_synchroniser_part(self) -> 'List[_2556.SynchroniserPart]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserPart]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2556.SynchroniserPart.TYPE]())

    def all_parts_of_type_synchroniser_sleeve(self) -> 'List[_2557.SynchroniserSleeve]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserSleeve]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2557.SynchroniserSleeve.TYPE]())

    def all_parts_of_type_torque_converter(self) -> 'List[_2558.TorqueConverter]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverter]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2558.TorqueConverter.TYPE]())

    def all_parts_of_type_torque_converter_pump(self) -> 'List[_2559.TorqueConverterPump]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverterPump]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2559.TorqueConverterPump.TYPE]())

    def all_parts_of_type_torque_converter_turbine(self) -> 'List[_2561.TorqueConverterTurbine]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverterTurbine]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2561.TorqueConverterTurbine.TYPE]())

    def add_assembly(self, name: Optional['str'] = 'Assembly') -> 'Assembly':
        """ 'AddAssembly' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.Assembly
        """

        name = str(name)
        method_result = self.wrapped.AddAssembly(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_axial_clearance_bearing(self, name: 'str', contact_diameter: 'float') -> '_2392.Bearing':
        """ 'AddAxialClearanceBearing' is the original name of this method.

        Args:
            name (str)
            contact_diameter (float)

        Returns:
            mastapy.system_model.part_model.Bearing
        """

        name = str(name)
        contact_diameter = float(contact_diameter)
        method_result = self.wrapped.AddAxialClearanceBearing(name if name else '', contact_diameter if contact_diameter else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_bearing_with_name_and_rolling_bearing_type(self, name: 'str', type_: '_1857.RollingBearingType') -> '_2392.Bearing':
        """ 'AddBearing' is the original name of this method.

        Args:
            name (str)
            type_ (mastapy.bearings.RollingBearingType)

        Returns:
            mastapy.system_model.part_model.Bearing
        """

        name = str(name)
        type_ = conversion.mp_to_pn_enum(type_)
        method_result = self.wrapped.AddBearing.Overloads[_STRING, _ROLLING_BEARING_TYPE](name if name else '', type_)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_bearing_with_name_rolling_bearing_type_and_designation(self, name: 'str', type_: '_1857.RollingBearingType', designation: 'str') -> '_2392.Bearing':
        """ 'AddBearing' is the original name of this method.

        Args:
            name (str)
            type_ (mastapy.bearings.RollingBearingType)
            designation (str)

        Returns:
            mastapy.system_model.part_model.Bearing
        """

        name = str(name)
        type_ = conversion.mp_to_pn_enum(type_)
        designation = str(designation)
        method_result = self.wrapped.AddBearing.Overloads[_STRING, _ROLLING_BEARING_TYPE, _STRING](name if name else '', type_, designation if designation else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_bearing(self, name: 'str') -> '_2392.Bearing':
        """ 'AddBearing' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Bearing
        """

        name = str(name)
        method_result = self.wrapped.AddBearing.Overloads[_STRING](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_belt_drive_with_options(self, belt_creation_options: Optional['_2522.BeltCreationOptions'] = None) -> '_2527.BeltDrive':
        """ 'AddBeltDrive' is the original name of this method.

        Args:
            belt_creation_options (mastapy.system_model.part_model.creation_options.BeltCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.couplings.BeltDrive
        """

        method_result = self.wrapped.AddBeltDrive.Overloads[_BELT_CREATION_OPTIONS](belt_creation_options.wrapped if belt_creation_options else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_belt_drive(self, centre_distance: Optional['float'] = 0.1, pulley_a_diameter: Optional['float'] = 0.08, pulley_b_diameter: Optional['float'] = 0.08, name: Optional['str'] = 'Belt Drive') -> '_2527.BeltDrive':
        """ 'AddBeltDrive' is the original name of this method.

        Args:
            centre_distance (float, optional)
            pulley_a_diameter (float, optional)
            pulley_b_diameter (float, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.BeltDrive
        """

        centre_distance = float(centre_distance)
        pulley_a_diameter = float(pulley_a_diameter)
        pulley_b_diameter = float(pulley_b_diameter)
        name = str(name)
        method_result = self.wrapped.AddBeltDrive.Overloads[_DOUBLE, _DOUBLE, _DOUBLE, _STRING](centre_distance if centre_distance else 0.0, pulley_a_diameter if pulley_a_diameter else 0.0, pulley_b_diameter if pulley_b_diameter else 0.0, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_bolted_joint(self, name: Optional['str'] = 'Bolted Joint') -> '_2395.BoltedJoint':
        """ 'AddBoltedJoint' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.BoltedJoint
        """

        name = str(name)
        method_result = self.wrapped.AddBoltedJoint(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cvt(self, name: Optional['str'] = 'CVT') -> '_2537.CVT':
        """ 'AddCVT' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.CVT
        """

        name = str(name)
        method_result = self.wrapped.AddCVT(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_clutch(self, name: Optional['str'] = 'Clutch') -> '_2529.Clutch':
        """ 'AddClutch' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.Clutch
        """

        name = str(name)
        method_result = self.wrapped.AddClutch(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_concept_coupling(self, name: Optional['str'] = 'Concept Coupling') -> '_2532.ConceptCoupling':
        """ 'AddConceptCoupling' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.ConceptCoupling
        """

        name = str(name)
        method_result = self.wrapped.AddConceptCoupling(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cycloidal_assembly_with_options(self, cycloidal_assembly_creation_options: Optional['_2523.CycloidalAssemblyCreationOptions'] = None) -> '_2519.CycloidalAssembly':
        """ 'AddCycloidalAssembly' is the original name of this method.

        Args:
            cycloidal_assembly_creation_options (mastapy.system_model.part_model.creation_options.CycloidalAssemblyCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.cycloidal.CycloidalAssembly
        """

        method_result = self.wrapped.AddCycloidalAssembly.Overloads[_CYCLOIDAL_ASSEMBLY_CREATION_OPTIONS](cycloidal_assembly_creation_options.wrapped if cycloidal_assembly_creation_options else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cycloidal_assembly(self, number_of_discs: Optional['int'] = 1, number_of_pins: Optional['int'] = 10, name: Optional['str'] = 'Cycloidal Assembly') -> '_2519.CycloidalAssembly':
        """ 'AddCycloidalAssembly' is the original name of this method.

        Args:
            number_of_discs (int, optional)
            number_of_pins (int, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.cycloidal.CycloidalAssembly
        """

        number_of_discs = int(number_of_discs)
        number_of_pins = int(number_of_pins)
        name = str(name)
        method_result = self.wrapped.AddCycloidalAssembly.Overloads[_INT_32, _INT_32, _STRING](number_of_discs if number_of_discs else 0, number_of_pins if number_of_pins else 0, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cylindrical_gear_pair_with_options(self, cylindrical_gear_pair_creation_options: Optional['_1136.CylindricalGearPairCreationOptions'] = None) -> '_2477.CylindricalGearSet':
        """ 'AddCylindricalGearPair' is the original name of this method.

        Args:
            cylindrical_gear_pair_creation_options (mastapy.gears.gear_designs.creation_options.CylindricalGearPairCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        """

        method_result = self.wrapped.AddCylindricalGearPair.Overloads[_CYLINDRICAL_GEAR_PAIR_CREATION_OPTIONS](cylindrical_gear_pair_creation_options.wrapped if cylindrical_gear_pair_creation_options else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cylindrical_gear_pair(self, centre_distance: 'float') -> '_2477.CylindricalGearSet':
        """ 'AddCylindricalGearPair' is the original name of this method.

        Args:
            centre_distance (float)

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        """

        centre_distance = float(centre_distance)
        method_result = self.wrapped.AddCylindricalGearPair.Overloads[_DOUBLE](centre_distance if centre_distance else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cylindrical_gear_set_with_options(self, cylindrical_gear_linear_train_creation_options: Optional['_2524.CylindricalGearLinearTrainCreationOptions'] = None) -> '_2477.CylindricalGearSet':
        """ 'AddCylindricalGearSet' is the original name of this method.

        Args:
            cylindrical_gear_linear_train_creation_options (mastapy.system_model.part_model.creation_options.CylindricalGearLinearTrainCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        """

        method_result = self.wrapped.AddCylindricalGearSet.Overloads[_CYLINDRICAL_GEAR_LINEAR_TRAIN_CREATION_OPTIONS](cylindrical_gear_linear_train_creation_options.wrapped if cylindrical_gear_linear_train_creation_options else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cylindrical_gear_set(self, name: 'str', centre_distances: 'List[float]') -> '_2477.CylindricalGearSet':
        """ 'AddCylindricalGearSet' is the original name of this method.

        Args:
            name (str)
            centre_distances (List[float])

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        """

        name = str(name)
        centre_distances = conversion.mp_to_pn_array_float(centre_distances)
        method_result = self.wrapped.AddCylindricalGearSet.Overloads[_STRING, _ARRAY[_DOUBLE]](name if name else '', centre_distances)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cylindrical_gear_set_extended(self, name: 'str', normal_pressure_angle: 'float', helix_angle: 'float', normal_module: 'float', pinion_hand: '_327.Hand', centre_distances: 'List[float]') -> '_2477.CylindricalGearSet':
        """ 'AddCylindricalGearSet' is the original name of this method.

        Args:
            name (str)
            normal_pressure_angle (float)
            helix_angle (float)
            normal_module (float)
            pinion_hand (mastapy.gears.Hand)
            centre_distances (List[float])

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        """

        name = str(name)
        normal_pressure_angle = float(normal_pressure_angle)
        helix_angle = float(helix_angle)
        normal_module = float(normal_module)
        pinion_hand = conversion.mp_to_pn_enum(pinion_hand)
        centre_distances = conversion.mp_to_pn_array_float(centre_distances)
        method_result = self.wrapped.AddCylindricalGearSet.Overloads[_STRING, _DOUBLE, _DOUBLE, _DOUBLE, _HAND, _ARRAY[_DOUBLE]](name if name else '', normal_pressure_angle if normal_pressure_angle else 0.0, helix_angle if helix_angle else 0.0, normal_module if normal_module else 0.0, pinion_hand, centre_distances)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_datum(self, name: Optional['str'] = 'Datum') -> '_2400.Datum':
        """ 'AddDatum' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.Datum
        """

        name = str(name)
        method_result = self.wrapped.AddDatum(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_fe_part(self, name: Optional['str'] = 'FE Part') -> '_2405.FEPart':
        """ 'AddFEPart' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.FEPart
        """

        name = str(name)
        method_result = self.wrapped.AddFEPart(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_face_gear_set(self, name: Optional['str'] = 'Face Gear Set') -> '_2480.FaceGearSet':
        """ 'AddFaceGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.FaceGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddFaceGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_hypoid_gear_set(self, name: Optional['str'] = 'Hypoid Gear Set') -> '_2486.HypoidGearSet':
        """ 'AddHypoidGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.HypoidGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddHypoidGearSet.Overloads[_STRING](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_hypoid_gear_set_detailed(self, name: Optional['str'] = 'Hypoid Gear Set', pinion_number_of_teeth: Optional['int'] = 7, wheel_number_of_teeth: Optional['int'] = 41, outer_transverse_module: Optional['float'] = 0.0109756, wheel_face_width: Optional['float'] = 0.072, offset: Optional['float'] = 0.045, average_pressure_angle: Optional['float'] = 0.3926991, design_method: Optional['_1169.AGMAGleasonConicalGearGeometryMethods'] = _1169.AGMAGleasonConicalGearGeometryMethods.GLEASON) -> '_2486.HypoidGearSet':
        """ 'AddHypoidGearSet' is the original name of this method.

        Args:
            name (str, optional)
            pinion_number_of_teeth (int, optional)
            wheel_number_of_teeth (int, optional)
            outer_transverse_module (float, optional)
            wheel_face_width (float, optional)
            offset (float, optional)
            average_pressure_angle (float, optional)
            design_method (mastapy.gears.gear_designs.bevel.AGMAGleasonConicalGearGeometryMethods, optional)

        Returns:
            mastapy.system_model.part_model.gears.HypoidGearSet
        """

        name = str(name)
        pinion_number_of_teeth = int(pinion_number_of_teeth)
        wheel_number_of_teeth = int(wheel_number_of_teeth)
        outer_transverse_module = float(outer_transverse_module)
        wheel_face_width = float(wheel_face_width)
        offset = float(offset)
        average_pressure_angle = float(average_pressure_angle)
        design_method = conversion.mp_to_pn_enum(design_method)
        method_result = self.wrapped.AddHypoidGearSet.Overloads[_STRING, _INT_32, _INT_32, _DOUBLE, _DOUBLE, _DOUBLE, _DOUBLE, _AGMA_GLEASON_CONICAL_GEAR_GEOMETRY_METHODS](name if name else '', pinion_number_of_teeth if pinion_number_of_teeth else 0, wheel_number_of_teeth if wheel_number_of_teeth else 0, outer_transverse_module if outer_transverse_module else 0.0, wheel_face_width if wheel_face_width else 0.0, offset if offset else 0.0, average_pressure_angle if average_pressure_angle else 0.0, design_method)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_klingelnberg_cyclo_palloid_hypoid_gear_set(self, name: Optional['str'] = 'Klingelnberg Cyclo Palloid Hypoid Gear Set') -> '_2490.KlingelnbergCycloPalloidHypoidGearSet':
        """ 'AddKlingelnbergCycloPalloidHypoidGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddKlingelnbergCycloPalloidHypoidGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, name: Optional['str'] = 'Klingelnberg Cyclo Palloid Spiral Bevel Gear Set') -> '_2492.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """ 'AddKlingelnbergCycloPalloidSpiralBevelGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddKlingelnbergCycloPalloidSpiralBevelGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_linear_bearing(self, name: 'str', width: 'float') -> '_2392.Bearing':
        """ 'AddLinearBearing' is the original name of this method.

        Args:
            name (str)
            width (float)

        Returns:
            mastapy.system_model.part_model.Bearing
        """

        name = str(name)
        width = float(width)
        method_result = self.wrapped.AddLinearBearing(name if name else '', width if width else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_mass_disc(self, name: Optional['str'] = 'Mass Disc') -> '_2414.MassDisc':
        """ 'AddMassDisc' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.MassDisc
        """

        name = str(name)
        method_result = self.wrapped.AddMassDisc(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_measurement_component(self, name: Optional['str'] = 'Measurement Component') -> '_2415.MeasurementComponent':
        """ 'AddMeasurementComponent' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.MeasurementComponent
        """

        name = str(name)
        method_result = self.wrapped.AddMeasurementComponent(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_oil_seal(self, name: Optional['str'] = 'Oil Seal') -> '_2418.OilSeal':
        """ 'AddOilSeal' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.OilSeal
        """

        name = str(name)
        method_result = self.wrapped.AddOilSeal(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_planet_carrier_with_options(self, planet_carrier_creation_options: Optional['_2525.PlanetCarrierCreationOptions'] = None) -> '_2421.PlanetCarrier':
        """ 'AddPlanetCarrier' is the original name of this method.

        Args:
            planet_carrier_creation_options (mastapy.system_model.part_model.creation_options.PlanetCarrierCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.PlanetCarrier
        """

        method_result = self.wrapped.AddPlanetCarrier.Overloads[_PLANET_CARRIER_CREATION_OPTIONS](planet_carrier_creation_options.wrapped if planet_carrier_creation_options else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_planet_carrier(self, number_of_planets: Optional['int'] = 3, diameter: Optional['float'] = 0.05) -> '_2421.PlanetCarrier':
        """ 'AddPlanetCarrier' is the original name of this method.

        Args:
            number_of_planets (int, optional)
            diameter (float, optional)

        Returns:
            mastapy.system_model.part_model.PlanetCarrier
        """

        number_of_planets = int(number_of_planets)
        diameter = float(diameter)
        method_result = self.wrapped.AddPlanetCarrier.Overloads[_INT_32, _DOUBLE](number_of_planets if number_of_planets else 0, diameter if diameter else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_planetary_gear_set(self, name: Optional['str'] = 'Planetary Gear Set') -> '_2493.PlanetaryGearSet':
        """ 'AddPlanetaryGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.PlanetaryGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddPlanetaryGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_point_load(self, name: Optional['str'] = 'Point Load') -> '_2423.PointLoad':
        """ 'AddPointLoad' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.PointLoad
        """

        name = str(name)
        method_result = self.wrapped.AddPointLoad(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_power_load(self, name: Optional['str'] = 'Power Load') -> '_2424.PowerLoad':
        """ 'AddPowerLoad' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.PowerLoad
        """

        name = str(name)
        method_result = self.wrapped.AddPowerLoad(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_rolling_bearing_from_catalogue(self, catalogue: '_1830.BearingCatalog', designation: 'str', name: 'str') -> '_2392.Bearing':
        """ 'AddRollingBearingFromCatalogue' is the original name of this method.

        Args:
            catalogue (mastapy.bearings.BearingCatalog)
            designation (str)
            name (str)

        Returns:
            mastapy.system_model.part_model.Bearing
        """

        catalogue = conversion.mp_to_pn_enum(catalogue)
        designation = str(designation)
        name = str(name)
        method_result = self.wrapped.AddRollingBearingFromCatalogue(catalogue, designation if designation else '', name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_rolling_ring(self, name: Optional['str'] = 'Rolling Ring') -> '_2547.RollingRing':
        """ 'AddRollingRing' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.RollingRing
        """

        name = str(name)
        method_result = self.wrapped.AddRollingRing(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_shaft_with_options(self, shaft_creation_options: '_2526.ShaftCreationOptions') -> '_2434.Shaft':
        """ 'AddShaft' is the original name of this method.

        Args:
            shaft_creation_options (mastapy.system_model.part_model.creation_options.ShaftCreationOptions)

        Returns:
            mastapy.system_model.part_model.shaft_model.Shaft
        """

        method_result = self.wrapped.AddShaft.Overloads[_SHAFT_CREATION_OPTIONS](shaft_creation_options.wrapped if shaft_creation_options else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_shaft(self, length: Optional['float'] = 0.1, outer_diameter: Optional['float'] = 0.025, bore: Optional['float'] = 0.0, name: Optional['str'] = 'Shaft') -> '_2434.Shaft':
        """ 'AddShaft' is the original name of this method.

        Args:
            length (float, optional)
            outer_diameter (float, optional)
            bore (float, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.shaft_model.Shaft
        """

        length = float(length)
        outer_diameter = float(outer_diameter)
        bore = float(bore)
        name = str(name)
        method_result = self.wrapped.AddShaft.Overloads[_DOUBLE, _DOUBLE, _DOUBLE, _STRING](length if length else 0.0, outer_diameter if outer_diameter else 0.0, bore if bore else 0.0, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_spiral_bevel_differential_gear_set(self, name: Optional['str'] = 'Spiral Bevel Differential Gear Set') -> '_2467.BevelDifferentialGearSet':
        """ 'AddSpiralBevelDifferentialGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.BevelDifferentialGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddSpiralBevelDifferentialGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_spiral_bevel_gear_set(self, name: Optional['str'] = 'Spiral Bevel Gear Set') -> '_2495.SpiralBevelGearSet':
        """ 'AddSpiralBevelGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.SpiralBevelGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddSpiralBevelGearSet.Overloads[_STRING](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_spiral_bevel_gear_set_with_options(self, spiral_bevel_gear_set_creation_options: Optional['_1139.SpiralBevelGearSetCreationOptions'] = None) -> '_2495.SpiralBevelGearSet':
        """ 'AddSpiralBevelGearSet' is the original name of this method.

        Args:
            spiral_bevel_gear_set_creation_options (mastapy.gears.gear_designs.creation_options.SpiralBevelGearSetCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.gears.SpiralBevelGearSet
        """

        method_result = self.wrapped.AddSpiralBevelGearSet.Overloads[_SPIRAL_BEVEL_GEAR_SET_CREATION_OPTIONS](spiral_bevel_gear_set_creation_options.wrapped if spiral_bevel_gear_set_creation_options else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_spiral_bevel_gear_set_detailed(self, name: Optional['str'] = 'Spiral Bevel Gear Set', outer_transverse_module: Optional['float'] = 0.00635, pressure_angle: Optional['float'] = 0.02, mean_spiral_angle: Optional['float'] = 0.523599, wheel_number_of_teeth: Optional['int'] = 43, pinion_number_of_teeth: Optional['int'] = 14, wheel_face_width: Optional['float'] = 0.02, pinion_face_width: Optional['float'] = 0.02, pinion_face_width_offset: Optional['float'] = 0.0, shaft_angle: Optional['float'] = 1.5708) -> '_2495.SpiralBevelGearSet':
        """ 'AddSpiralBevelGearSet' is the original name of this method.

        Args:
            name (str, optional)
            outer_transverse_module (float, optional)
            pressure_angle (float, optional)
            mean_spiral_angle (float, optional)
            wheel_number_of_teeth (int, optional)
            pinion_number_of_teeth (int, optional)
            wheel_face_width (float, optional)
            pinion_face_width (float, optional)
            pinion_face_width_offset (float, optional)
            shaft_angle (float, optional)

        Returns:
            mastapy.system_model.part_model.gears.SpiralBevelGearSet
        """

        name = str(name)
        outer_transverse_module = float(outer_transverse_module)
        pressure_angle = float(pressure_angle)
        mean_spiral_angle = float(mean_spiral_angle)
        wheel_number_of_teeth = int(wheel_number_of_teeth)
        pinion_number_of_teeth = int(pinion_number_of_teeth)
        wheel_face_width = float(wheel_face_width)
        pinion_face_width = float(pinion_face_width)
        pinion_face_width_offset = float(pinion_face_width_offset)
        shaft_angle = float(shaft_angle)
        method_result = self.wrapped.AddSpiralBevelGearSet.Overloads[_STRING, _DOUBLE, _DOUBLE, _DOUBLE, _INT_32, _INT_32, _DOUBLE, _DOUBLE, _DOUBLE, _DOUBLE](name if name else '', outer_transverse_module if outer_transverse_module else 0.0, pressure_angle if pressure_angle else 0.0, mean_spiral_angle if mean_spiral_angle else 0.0, wheel_number_of_teeth if wheel_number_of_teeth else 0, pinion_number_of_teeth if pinion_number_of_teeth else 0, wheel_face_width if wheel_face_width else 0.0, pinion_face_width if pinion_face_width else 0.0, pinion_face_width_offset if pinion_face_width_offset else 0.0, shaft_angle if shaft_angle else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_spring_damper(self, name: Optional['str'] = 'Spring Damper') -> '_2551.SpringDamper':
        """ 'AddSpringDamper' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.SpringDamper
        """

        name = str(name)
        method_result = self.wrapped.AddSpringDamper(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_straight_bevel_differential_gear_set(self, name: Optional['str'] = 'Straight Bevel Differential Gear Set') -> '_2497.StraightBevelDiffGearSet':
        """ 'AddStraightBevelDifferentialGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelDiffGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddStraightBevelDifferentialGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_straight_bevel_gear_set(self, name: Optional['str'] = 'Straight Bevel Gear Set') -> '_2499.StraightBevelGearSet':
        """ 'AddStraightBevelGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddStraightBevelGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_synchroniser(self, name: Optional['str'] = 'Synchroniser') -> '_2553.Synchroniser':
        """ 'AddSynchroniser' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.Synchroniser
        """

        name = str(name)
        method_result = self.wrapped.AddSynchroniser(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_torque_converter(self, name: Optional['str'] = 'Torque Converter') -> '_2558.TorqueConverter':
        """ 'AddTorqueConverter' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.TorqueConverter
        """

        name = str(name)
        method_result = self.wrapped.AddTorqueConverter(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_unbalanced_mass(self, name: Optional['str'] = 'Unbalanced Mass') -> '_2429.UnbalancedMass':
        """ 'AddUnbalancedMass' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.UnbalancedMass
        """

        name = str(name)
        method_result = self.wrapped.AddUnbalancedMass(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_worm_gear_set(self, name: Optional['str'] = 'Worm Gear Set') -> '_2503.WormGearSet':
        """ 'AddWormGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.WormGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddWormGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_zerol_bevel_differential_gear_set(self, name: Optional['str'] = 'Zerol Bevel Differential Gear Set') -> '_2467.BevelDifferentialGearSet':
        """ 'AddZerolBevelDifferentialGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.BevelDifferentialGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddZerolBevelDifferentialGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_zerol_bevel_gear_set(self, name: Optional['str'] = 'Zerol Bevel Gear Set') -> '_2505.ZerolBevelGearSet':
        """ 'AddZerolBevelGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.ZerolBevelGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddZerolBevelGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_shaft_hub_connection(self, name: 'str') -> '_2549.ShaftHubConnection':
        """ 'AddShaftHubConnection' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.ShaftHubConnection
        """

        name = str(name)
        method_result = self.wrapped.AddShaftHubConnection(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def import_fe_mesh_from_file(self, file_name: 'str', stiffness_matrix: '_78.NodalMatrix') -> '_2405.FEPart':
        """ 'ImportFEMeshFromFile' is the original name of this method.

        Args:
            file_name (str)
            stiffness_matrix (mastapy.nodal_analysis.NodalMatrix)

        Returns:
            mastapy.system_model.part_model.FEPart
        """

        file_name = str(file_name)
        method_result = self.wrapped.ImportFEMeshFromFile(file_name if file_name else '', stiffness_matrix.wrapped if stiffness_matrix else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None
