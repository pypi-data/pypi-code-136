"""_942.py

GearMeshDesign
"""


from mastapy._internal import constructor
from mastapy.gears.gear_designs import _940, _941
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
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'GearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshDesign',)


class GearMeshDesign(_941.GearDesignComponent):
    """GearMeshDesign

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_DESIGN

    def __init__(self, instance_to_wrap: 'GearMeshDesign.TYPE'):
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
    def has_hunting_ratio(self) -> 'bool':
        """bool: 'HasHuntingRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasHuntingRatio

        if temp is None:
            return False

        return temp

    @property
    def highest_common_factor_of_teeth_numbers(self) -> 'int':
        """int: 'HighestCommonFactorOfTeethNumbers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HighestCommonFactorOfTeethNumbers

        if temp is None:
            return 0

        return temp

    @property
    def hunting_tooth_factor(self) -> 'float':
        """float: 'HuntingToothFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HuntingToothFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def speed_ratio_a_to_b(self) -> 'float':
        """float: 'SpeedRatioAToB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpeedRatioAToB

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ratio_a_to_b(self) -> 'float':
        """float: 'TorqueRatioAToB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueRatioAToB

        if temp is None:
            return 0.0

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
    def gear_a(self) -> '_940.GearDesign':
        """GearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _940.GearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_zerol_bevel_gear_design(self) -> '_945.ZerolBevelGearDesign':
        """ZerolBevelGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _945.ZerolBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ZerolBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_worm_design(self) -> '_949.WormDesign':
        """WormDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _949.WormDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to WormDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_worm_gear_design(self) -> '_950.WormGearDesign':
        """WormGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _950.WormGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to WormGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_worm_wheel_design(self) -> '_953.WormWheelDesign':
        """WormWheelDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _953.WormWheelDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to WormWheelDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_straight_bevel_gear_design(self) -> '_954.StraightBevelGearDesign':
        """StraightBevelGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _954.StraightBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to StraightBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_straight_bevel_diff_gear_design(self) -> '_958.StraightBevelDiffGearDesign':
        """StraightBevelDiffGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _958.StraightBevelDiffGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to StraightBevelDiffGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_spiral_bevel_gear_design(self) -> '_962.SpiralBevelGearDesign':
        """SpiralBevelGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _962.SpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to SpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_966.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _966.KlingelnbergCycloPalloidSpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_970.KlingelnbergCycloPalloidHypoidGearDesign':
        """KlingelnbergCycloPalloidHypoidGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _970.KlingelnbergCycloPalloidHypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_klingelnberg_conical_gear_design(self) -> '_974.KlingelnbergConicalGearDesign':
        """KlingelnbergConicalGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _974.KlingelnbergConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to KlingelnbergConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_hypoid_gear_design(self) -> '_978.HypoidGearDesign':
        """HypoidGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _978.HypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to HypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_face_gear_design(self) -> '_982.FaceGearDesign':
        """FaceGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _982.FaceGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to FaceGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_face_gear_pinion_design(self) -> '_987.FaceGearPinionDesign':
        """FaceGearPinionDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _987.FaceGearPinionDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to FaceGearPinionDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_face_gear_wheel_design(self) -> '_990.FaceGearWheelDesign':
        """FaceGearWheelDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _990.FaceGearWheelDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to FaceGearWheelDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_design(self) -> '_1005.CylindricalGearDesign':
        """CylindricalGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1005.CylindricalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_planet_gear_design(self) -> '_1034.CylindricalPlanetGearDesign':
        """CylindricalPlanetGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1034.CylindricalPlanetGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalPlanetGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_design(self) -> '_1144.ConicalGearDesign':
        """ConicalGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1144.ConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_concept_gear_design(self) -> '_1166.ConceptGearDesign':
        """ConceptGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1166.ConceptGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConceptGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_bevel_gear_design(self) -> '_1170.BevelGearDesign':
        """BevelGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1170.BevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to BevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_agma_gleason_conical_gear_design(self) -> '_1183.AGMAGleasonConicalGearDesign':
        """AGMAGleasonConicalGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1183.AGMAGleasonConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to AGMAGleasonConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b(self) -> '_940.GearDesign':
        """GearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _940.GearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_zerol_bevel_gear_design(self) -> '_945.ZerolBevelGearDesign':
        """ZerolBevelGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _945.ZerolBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ZerolBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_worm_design(self) -> '_949.WormDesign':
        """WormDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _949.WormDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to WormDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_worm_gear_design(self) -> '_950.WormGearDesign':
        """WormGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _950.WormGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to WormGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_worm_wheel_design(self) -> '_953.WormWheelDesign':
        """WormWheelDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _953.WormWheelDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to WormWheelDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_straight_bevel_gear_design(self) -> '_954.StraightBevelGearDesign':
        """StraightBevelGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _954.StraightBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to StraightBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_straight_bevel_diff_gear_design(self) -> '_958.StraightBevelDiffGearDesign':
        """StraightBevelDiffGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _958.StraightBevelDiffGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to StraightBevelDiffGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_spiral_bevel_gear_design(self) -> '_962.SpiralBevelGearDesign':
        """SpiralBevelGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _962.SpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to SpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_966.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _966.KlingelnbergCycloPalloidSpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_970.KlingelnbergCycloPalloidHypoidGearDesign':
        """KlingelnbergCycloPalloidHypoidGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _970.KlingelnbergCycloPalloidHypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_klingelnberg_conical_gear_design(self) -> '_974.KlingelnbergConicalGearDesign':
        """KlingelnbergConicalGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _974.KlingelnbergConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to KlingelnbergConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_hypoid_gear_design(self) -> '_978.HypoidGearDesign':
        """HypoidGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _978.HypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to HypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_face_gear_design(self) -> '_982.FaceGearDesign':
        """FaceGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _982.FaceGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to FaceGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_face_gear_pinion_design(self) -> '_987.FaceGearPinionDesign':
        """FaceGearPinionDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _987.FaceGearPinionDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to FaceGearPinionDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_face_gear_wheel_design(self) -> '_990.FaceGearWheelDesign':
        """FaceGearWheelDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _990.FaceGearWheelDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to FaceGearWheelDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_design(self) -> '_1005.CylindricalGearDesign':
        """CylindricalGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1005.CylindricalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_planet_gear_design(self) -> '_1034.CylindricalPlanetGearDesign':
        """CylindricalPlanetGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1034.CylindricalPlanetGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalPlanetGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_design(self) -> '_1144.ConicalGearDesign':
        """ConicalGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1144.ConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_concept_gear_design(self) -> '_1166.ConceptGearDesign':
        """ConceptGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1166.ConceptGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConceptGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_bevel_gear_design(self) -> '_1170.BevelGearDesign':
        """BevelGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1170.BevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to BevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_agma_gleason_conical_gear_design(self) -> '_1183.AGMAGleasonConicalGearDesign':
        """AGMAGleasonConicalGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1183.AGMAGleasonConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to AGMAGleasonConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
