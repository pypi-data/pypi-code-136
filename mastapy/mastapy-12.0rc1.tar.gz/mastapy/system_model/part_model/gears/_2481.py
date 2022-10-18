"""_2481.py

Gear
"""


from mastapy._internal import constructor
from mastapy.gears.gear_designs import _940
from mastapy.gears.gear_designs.zerol_bevel import _945
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.worm import _949, _950, _953
from mastapy.gears.gear_designs.straight_bevel import _954
from mastapy.gears.gear_designs.straight_bevel_diff import _958
from mastapy.gears.gear_designs.spiral_bevel import _962
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _966
from mastapy.gears.gear_designs.klingelnberg_hypoid import _970
from mastapy.gears.gear_designs.klingelnberg_conical import _974
from mastapy.gears.gear_designs.hypoid import _978
from mastapy.gears.gear_designs.face import _982, _987, _990
from mastapy.gears.gear_designs.cylindrical import _1005, _1034
from mastapy.gears.gear_designs.conical import _1144
from mastapy.gears.gear_designs.concept import _1166
from mastapy.gears.gear_designs.bevel import _1170
from mastapy.gears.gear_designs.agma_gleason_conical import _1183
from mastapy.system_model.part_model.gears import (
    _2483, _2465, _2467, _2471,
    _2473, _2475, _2477, _2480,
    _2486, _2488, _2490, _2492,
    _2493, _2495, _2497, _2499,
    _2503, _2505
)
from mastapy.system_model.part_model.shaft_model import _2434
from mastapy.system_model.part_model import _2416
from mastapy._internal.python_net import python_net_import

_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'Gear')


__docformat__ = 'restructuredtext en'
__all__ = ('Gear',)


class Gear(_2416.MountableComponent):
    """Gear

    This is a mastapy class.
    """

    TYPE = _GEAR

    def __init__(self, instance_to_wrap: 'Gear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cloned_from(self) -> 'str':
        """str: 'ClonedFrom' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClonedFrom

        if temp is None:
            return ''

        return temp

    @property
    def is_clone_gear(self) -> 'bool':
        """bool: 'IsCloneGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsCloneGear

        if temp is None:
            return False

        return temp

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value else 0.0

    @property
    def maximum_number_of_teeth(self) -> 'int':
        """int: 'MaximumNumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.MaximumNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @maximum_number_of_teeth.setter
    def maximum_number_of_teeth(self, value: 'int'):
        self.wrapped.MaximumNumberOfTeeth = int(value) if value else 0

    @property
    def minimum_number_of_teeth(self) -> 'int':
        """int: 'MinimumNumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.MinimumNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @minimum_number_of_teeth.setter
    def minimum_number_of_teeth(self, value: 'int'):
        self.wrapped.MinimumNumberOfTeeth = int(value) if value else 0

    @property
    def active_gear_design(self) -> '_940.GearDesign':
        """GearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _940.GearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to GearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_zerol_bevel_gear_design(self) -> '_945.ZerolBevelGearDesign':
        """ZerolBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _945.ZerolBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to ZerolBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_worm_design(self) -> '_949.WormDesign':
        """WormDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _949.WormDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to WormDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_worm_gear_design(self) -> '_950.WormGearDesign':
        """WormGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _950.WormGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to WormGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_worm_wheel_design(self) -> '_953.WormWheelDesign':
        """WormWheelDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _953.WormWheelDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to WormWheelDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_straight_bevel_gear_design(self) -> '_954.StraightBevelGearDesign':
        """StraightBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _954.StraightBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to StraightBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_straight_bevel_diff_gear_design(self) -> '_958.StraightBevelDiffGearDesign':
        """StraightBevelDiffGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _958.StraightBevelDiffGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to StraightBevelDiffGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_spiral_bevel_gear_design(self) -> '_962.SpiralBevelGearDesign':
        """SpiralBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _962.SpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to SpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_966.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _966.KlingelnbergCycloPalloidSpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_970.KlingelnbergCycloPalloidHypoidGearDesign':
        """KlingelnbergCycloPalloidHypoidGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _970.KlingelnbergCycloPalloidHypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_klingelnberg_conical_gear_design(self) -> '_974.KlingelnbergConicalGearDesign':
        """KlingelnbergConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _974.KlingelnbergConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to KlingelnbergConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_hypoid_gear_design(self) -> '_978.HypoidGearDesign':
        """HypoidGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _978.HypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to HypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_face_gear_design(self) -> '_982.FaceGearDesign':
        """FaceGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _982.FaceGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to FaceGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_face_gear_pinion_design(self) -> '_987.FaceGearPinionDesign':
        """FaceGearPinionDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _987.FaceGearPinionDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to FaceGearPinionDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_face_gear_wheel_design(self) -> '_990.FaceGearWheelDesign':
        """FaceGearWheelDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _990.FaceGearWheelDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to FaceGearWheelDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_cylindrical_gear_design(self) -> '_1005.CylindricalGearDesign':
        """CylindricalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _1005.CylindricalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to CylindricalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_cylindrical_planet_gear_design(self) -> '_1034.CylindricalPlanetGearDesign':
        """CylindricalPlanetGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _1034.CylindricalPlanetGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to CylindricalPlanetGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_conical_gear_design(self) -> '_1144.ConicalGearDesign':
        """ConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _1144.ConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to ConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_concept_gear_design(self) -> '_1166.ConceptGearDesign':
        """ConceptGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _1166.ConceptGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to ConceptGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_bevel_gear_design(self) -> '_1170.BevelGearDesign':
        """BevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _1170.BevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to BevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_agma_gleason_conical_gear_design(self) -> '_1183.AGMAGleasonConicalGearDesign':
        """AGMAGleasonConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _1183.AGMAGleasonConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to AGMAGleasonConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_width(self) -> 'float':
        """float: 'FaceWidth' is the original name of this property."""

        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    def face_width(self, value: 'float'):
        self.wrapped.FaceWidth = float(value) if value else 0.0

    @property
    def gear_set(self) -> '_2483.GearSet':
        """GearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2483.GearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to GearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_agma_gleason_conical_gear_set(self) -> '_2465.AGMAGleasonConicalGearSet':
        """AGMAGleasonConicalGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2465.AGMAGleasonConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to AGMAGleasonConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_bevel_differential_gear_set(self) -> '_2467.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2467.BevelDifferentialGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to BevelDifferentialGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_bevel_gear_set(self) -> '_2471.BevelGearSet':
        """BevelGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2471.BevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to BevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_concept_gear_set(self) -> '_2473.ConceptGearSet':
        """ConceptGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2473.ConceptGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to ConceptGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_conical_gear_set(self) -> '_2475.ConicalGearSet':
        """ConicalGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2475.ConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to ConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_cylindrical_gear_set(self) -> '_2477.CylindricalGearSet':
        """CylindricalGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2477.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_face_gear_set(self) -> '_2480.FaceGearSet':
        """FaceGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2480.FaceGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to FaceGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_hypoid_gear_set(self) -> '_2486.HypoidGearSet':
        """HypoidGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2486.HypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to HypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> '_2488.KlingelnbergCycloPalloidConicalGearSet':
        """KlingelnbergCycloPalloidConicalGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2488.KlingelnbergCycloPalloidConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to KlingelnbergCycloPalloidConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2490.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2490.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2492.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2492.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_planetary_gear_set(self) -> '_2493.PlanetaryGearSet':
        """PlanetaryGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2493.PlanetaryGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to PlanetaryGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_spiral_bevel_gear_set(self) -> '_2495.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2495.SpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to SpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_straight_bevel_diff_gear_set(self) -> '_2497.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2497.StraightBevelDiffGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to StraightBevelDiffGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_straight_bevel_gear_set(self) -> '_2499.StraightBevelGearSet':
        """StraightBevelGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2499.StraightBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to StraightBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_worm_gear_set(self) -> '_2503.WormGearSet':
        """WormGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2503.WormGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to WormGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_zerol_bevel_gear_set(self) -> '_2505.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _2505.ZerolBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to ZerolBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def number_of_teeth(self) -> 'int':
        """int: 'NumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return temp

    @number_of_teeth.setter
    def number_of_teeth(self, value: 'int'):
        self.wrapped.NumberOfTeeth = int(value) if value else 0

    @property
    def shaft(self) -> '_2434.Shaft':
        """Shaft: 'Shaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shaft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def connect_to(self, other_gear: 'Gear'):
        """ 'ConnectTo' is the original name of this method.

        Args:
            other_gear (mastapy.system_model.part_model.gears.Gear)
        """

        self.wrapped.ConnectTo(other_gear.wrapped if other_gear else None)
