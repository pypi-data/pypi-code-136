"""_1206.py

AbstractGearMeshAnalysis
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import (
    _1205, _1208, _1209, _1210,
    _1211
)
from mastapy.gears.rating import _348, _352, _355
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.zerol_bevel import _364
from mastapy.gears.rating.worm import _366, _368
from mastapy.gears.rating.straight_bevel import _390
from mastapy.gears.rating.straight_bevel_diff import _393
from mastapy.gears.rating.spiral_bevel import _397
from mastapy.gears.rating.klingelnberg_spiral_bevel import _400
from mastapy.gears.rating.klingelnberg_hypoid import _403
from mastapy.gears.rating.klingelnberg_conical import _406
from mastapy.gears.rating.hypoid import _433
from mastapy.gears.rating.face import _439, _442
from mastapy.gears.rating.cylindrical import _449, _454
from mastapy.gears.rating.conical import _531, _533
from mastapy.gears.rating.concept import _541, _544
from mastapy.gears.rating.bevel import _548
from mastapy.gears.rating.agma_gleason_conical import _559
from mastapy.gears.manufacturing.cylindrical import _605, _609, _610
from mastapy.gears.manufacturing.bevel import (
    _768, _769, _770, _771,
    _781, _782, _787
)
from mastapy.gears.ltca import _833
from mastapy.gears.ltca.cylindrical import _849
from mastapy.gears.ltca.conical import _860
from mastapy.gears.load_case import _866
from mastapy.gears.load_case.worm import _869
from mastapy.gears.load_case.face import _872
from mastapy.gears.load_case.cylindrical import _875
from mastapy.gears.load_case.conical import _878
from mastapy.gears.load_case.concept import _881
from mastapy.gears.load_case.bevel import _884
from mastapy.gears.gear_two_d_fe_analysis import _891, _892
from mastapy.gears.gear_designs.face import _986
from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
    _1092, _1093, _1094, _1096
)
from mastapy.gears.fe_model import _1187
from mastapy.gears.fe_model.cylindrical import _1191
from mastapy.gears.fe_model.conical import _1194
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_MESH_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'AbstractGearMeshAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractGearMeshAnalysis',)


class AbstractGearMeshAnalysis(_0.APIBase):
    """AbstractGearMeshAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_MESH_ANALYSIS

    def __init__(self, instance_to_wrap: 'AbstractGearMeshAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_name(self) -> 'str':
        """str: 'MeshName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshName

        if temp is None:
            return ''

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def gear_a(self) -> '_1205.AbstractGearAnalysis':
        """AbstractGearAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1205.AbstractGearAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to AbstractGearAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_abstract_gear_rating(self) -> '_348.AbstractGearRating':
        """AbstractGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _348.AbstractGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to AbstractGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_gear_duty_cycle_rating(self) -> '_352.GearDutyCycleRating':
        """GearDutyCycleRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _352.GearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_gear_rating(self) -> '_355.GearRating':
        """GearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _355.GearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_zerol_bevel_gear_rating(self) -> '_364.ZerolBevelGearRating':
        """ZerolBevelGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _364.ZerolBevelGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ZerolBevelGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_worm_gear_duty_cycle_rating(self) -> '_366.WormGearDutyCycleRating':
        """WormGearDutyCycleRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _366.WormGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to WormGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_worm_gear_rating(self) -> '_368.WormGearRating':
        """WormGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _368.WormGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to WormGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_straight_bevel_gear_rating(self) -> '_390.StraightBevelGearRating':
        """StraightBevelGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _390.StraightBevelGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to StraightBevelGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_straight_bevel_diff_gear_rating(self) -> '_393.StraightBevelDiffGearRating':
        """StraightBevelDiffGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _393.StraightBevelDiffGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to StraightBevelDiffGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_spiral_bevel_gear_rating(self) -> '_397.SpiralBevelGearRating':
        """SpiralBevelGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _397.SpiralBevelGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to SpiralBevelGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(self) -> '_400.KlingelnbergCycloPalloidSpiralBevelGearRating':
        """KlingelnbergCycloPalloidSpiralBevelGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _400.KlingelnbergCycloPalloidSpiralBevelGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidSpiralBevelGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_hypoid_gear_rating(self) -> '_403.KlingelnbergCycloPalloidHypoidGearRating':
        """KlingelnbergCycloPalloidHypoidGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _403.KlingelnbergCycloPalloidHypoidGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidHypoidGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_conical_gear_rating(self) -> '_406.KlingelnbergCycloPalloidConicalGearRating':
        """KlingelnbergCycloPalloidConicalGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _406.KlingelnbergCycloPalloidConicalGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidConicalGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_hypoid_gear_rating(self) -> '_433.HypoidGearRating':
        """HypoidGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _433.HypoidGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to HypoidGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_face_gear_duty_cycle_rating(self) -> '_439.FaceGearDutyCycleRating':
        """FaceGearDutyCycleRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _439.FaceGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to FaceGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_face_gear_rating(self) -> '_442.FaceGearRating':
        """FaceGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _442.FaceGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to FaceGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_duty_cycle_rating(self) -> '_449.CylindricalGearDutyCycleRating':
        """CylindricalGearDutyCycleRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _449.CylindricalGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_rating(self) -> '_454.CylindricalGearRating':
        """CylindricalGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _454.CylindricalGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_duty_cycle_rating(self) -> '_531.ConicalGearDutyCycleRating':
        """ConicalGearDutyCycleRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _531.ConicalGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_rating(self) -> '_533.ConicalGearRating':
        """ConicalGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _533.ConicalGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_concept_gear_duty_cycle_rating(self) -> '_541.ConceptGearDutyCycleRating':
        """ConceptGearDutyCycleRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _541.ConceptGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConceptGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_concept_gear_rating(self) -> '_544.ConceptGearRating':
        """ConceptGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _544.ConceptGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConceptGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_bevel_gear_rating(self) -> '_548.BevelGearRating':
        """BevelGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _548.BevelGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to BevelGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_agma_gleason_conical_gear_rating(self) -> '_559.AGMAGleasonConicalGearRating':
        """AGMAGleasonConicalGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _559.AGMAGleasonConicalGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to AGMAGleasonConicalGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_manufacturing_config(self) -> '_605.CylindricalGearManufacturingConfig':
        """CylindricalGearManufacturingConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _605.CylindricalGearManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_manufactured_gear_duty_cycle(self) -> '_609.CylindricalManufacturedGearDutyCycle':
        """CylindricalManufacturedGearDutyCycle: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _609.CylindricalManufacturedGearDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalManufacturedGearDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_manufactured_gear_load_case(self) -> '_610.CylindricalManufacturedGearLoadCase':
        """CylindricalManufacturedGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _610.CylindricalManufacturedGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalManufacturedGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_manufacturing_analysis(self) -> '_768.ConicalGearManufacturingAnalysis':
        """ConicalGearManufacturingAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _768.ConicalGearManufacturingAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearManufacturingAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_manufacturing_config(self) -> '_769.ConicalGearManufacturingConfig':
        """ConicalGearManufacturingConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _769.ConicalGearManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_micro_geometry_config(self) -> '_770.ConicalGearMicroGeometryConfig':
        """ConicalGearMicroGeometryConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _770.ConicalGearMicroGeometryConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearMicroGeometryConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_micro_geometry_config_base(self) -> '_771.ConicalGearMicroGeometryConfigBase':
        """ConicalGearMicroGeometryConfigBase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _771.ConicalGearMicroGeometryConfigBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearMicroGeometryConfigBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_pinion_manufacturing_config(self) -> '_781.ConicalPinionManufacturingConfig':
        """ConicalPinionManufacturingConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _781.ConicalPinionManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalPinionManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_pinion_micro_geometry_config(self) -> '_782.ConicalPinionMicroGeometryConfig':
        """ConicalPinionMicroGeometryConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _782.ConicalPinionMicroGeometryConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalPinionMicroGeometryConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_wheel_manufacturing_config(self) -> '_787.ConicalWheelManufacturingConfig':
        """ConicalWheelManufacturingConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _787.ConicalWheelManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalWheelManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_gear_load_distribution_analysis(self) -> '_833.GearLoadDistributionAnalysis':
        """GearLoadDistributionAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _833.GearLoadDistributionAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearLoadDistributionAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_load_distribution_analysis(self) -> '_849.CylindricalGearLoadDistributionAnalysis':
        """CylindricalGearLoadDistributionAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _849.CylindricalGearLoadDistributionAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearLoadDistributionAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_load_distribution_analysis(self) -> '_860.ConicalGearLoadDistributionAnalysis':
        """ConicalGearLoadDistributionAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _860.ConicalGearLoadDistributionAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearLoadDistributionAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_gear_load_case_base(self) -> '_866.GearLoadCaseBase':
        """GearLoadCaseBase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _866.GearLoadCaseBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearLoadCaseBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_worm_gear_load_case(self) -> '_869.WormGearLoadCase':
        """WormGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _869.WormGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to WormGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_face_gear_load_case(self) -> '_872.FaceGearLoadCase':
        """FaceGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _872.FaceGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to FaceGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_load_case(self) -> '_875.CylindricalGearLoadCase':
        """CylindricalGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _875.CylindricalGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_load_case(self) -> '_878.ConicalGearLoadCase':
        """ConicalGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _878.ConicalGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_concept_gear_load_case(self) -> '_881.ConceptGearLoadCase':
        """ConceptGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _881.ConceptGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConceptGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_bevel_load_case(self) -> '_884.BevelLoadCase':
        """BevelLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _884.BevelLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to BevelLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_tiff_analysis(self) -> '_891.CylindricalGearTIFFAnalysis':
        """CylindricalGearTIFFAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _891.CylindricalGearTIFFAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearTIFFAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_tiff_analysis_duty_cycle(self) -> '_892.CylindricalGearTIFFAnalysisDutyCycle':
        """CylindricalGearTIFFAnalysisDutyCycle: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _892.CylindricalGearTIFFAnalysisDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearTIFFAnalysisDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_face_gear_micro_geometry(self) -> '_986.FaceGearMicroGeometry':
        """FaceGearMicroGeometry: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _986.FaceGearMicroGeometry.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to FaceGearMicroGeometry. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_micro_geometry(self) -> '_1092.CylindricalGearMicroGeometry':
        """CylindricalGearMicroGeometry: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1092.CylindricalGearMicroGeometry.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearMicroGeometry. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_micro_geometry_base(self) -> '_1093.CylindricalGearMicroGeometryBase':
        """CylindricalGearMicroGeometryBase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1093.CylindricalGearMicroGeometryBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearMicroGeometryBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_micro_geometry_duty_cycle(self) -> '_1094.CylindricalGearMicroGeometryDutyCycle':
        """CylindricalGearMicroGeometryDutyCycle: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1094.CylindricalGearMicroGeometryDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearMicroGeometryDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_micro_geometry_per_tooth(self) -> '_1096.CylindricalGearMicroGeometryPerTooth':
        """CylindricalGearMicroGeometryPerTooth: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1096.CylindricalGearMicroGeometryPerTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearMicroGeometryPerTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_gear_fe_model(self) -> '_1187.GearFEModel':
        """GearFEModel: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1187.GearFEModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearFEModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_fe_model(self) -> '_1191.CylindricalGearFEModel':
        """CylindricalGearFEModel: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1191.CylindricalGearFEModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearFEModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_fe_model(self) -> '_1194.ConicalGearFEModel':
        """ConicalGearFEModel: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1194.ConicalGearFEModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearFEModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_gear_design_analysis(self) -> '_1208.GearDesignAnalysis':
        """GearDesignAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1208.GearDesignAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearDesignAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_gear_implementation_analysis(self) -> '_1209.GearImplementationAnalysis':
        """GearImplementationAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1209.GearImplementationAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearImplementationAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_gear_implementation_analysis_duty_cycle(self) -> '_1210.GearImplementationAnalysisDutyCycle':
        """GearImplementationAnalysisDutyCycle: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1210.GearImplementationAnalysisDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearImplementationAnalysisDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_gear_implementation_detail(self) -> '_1211.GearImplementationDetail':
        """GearImplementationDetail: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        if _1211.GearImplementationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearImplementationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b(self) -> '_1205.AbstractGearAnalysis':
        """AbstractGearAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1205.AbstractGearAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to AbstractGearAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_abstract_gear_rating(self) -> '_348.AbstractGearRating':
        """AbstractGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _348.AbstractGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to AbstractGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_gear_duty_cycle_rating(self) -> '_352.GearDutyCycleRating':
        """GearDutyCycleRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _352.GearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_gear_rating(self) -> '_355.GearRating':
        """GearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _355.GearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_zerol_bevel_gear_rating(self) -> '_364.ZerolBevelGearRating':
        """ZerolBevelGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _364.ZerolBevelGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ZerolBevelGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_worm_gear_duty_cycle_rating(self) -> '_366.WormGearDutyCycleRating':
        """WormGearDutyCycleRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _366.WormGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to WormGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_worm_gear_rating(self) -> '_368.WormGearRating':
        """WormGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _368.WormGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to WormGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_straight_bevel_gear_rating(self) -> '_390.StraightBevelGearRating':
        """StraightBevelGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _390.StraightBevelGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to StraightBevelGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_straight_bevel_diff_gear_rating(self) -> '_393.StraightBevelDiffGearRating':
        """StraightBevelDiffGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _393.StraightBevelDiffGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to StraightBevelDiffGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_spiral_bevel_gear_rating(self) -> '_397.SpiralBevelGearRating':
        """SpiralBevelGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _397.SpiralBevelGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to SpiralBevelGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(self) -> '_400.KlingelnbergCycloPalloidSpiralBevelGearRating':
        """KlingelnbergCycloPalloidSpiralBevelGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _400.KlingelnbergCycloPalloidSpiralBevelGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidSpiralBevelGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_hypoid_gear_rating(self) -> '_403.KlingelnbergCycloPalloidHypoidGearRating':
        """KlingelnbergCycloPalloidHypoidGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _403.KlingelnbergCycloPalloidHypoidGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidHypoidGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_conical_gear_rating(self) -> '_406.KlingelnbergCycloPalloidConicalGearRating':
        """KlingelnbergCycloPalloidConicalGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _406.KlingelnbergCycloPalloidConicalGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidConicalGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_hypoid_gear_rating(self) -> '_433.HypoidGearRating':
        """HypoidGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _433.HypoidGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to HypoidGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_face_gear_duty_cycle_rating(self) -> '_439.FaceGearDutyCycleRating':
        """FaceGearDutyCycleRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _439.FaceGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to FaceGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_face_gear_rating(self) -> '_442.FaceGearRating':
        """FaceGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _442.FaceGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to FaceGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_duty_cycle_rating(self) -> '_449.CylindricalGearDutyCycleRating':
        """CylindricalGearDutyCycleRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _449.CylindricalGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_rating(self) -> '_454.CylindricalGearRating':
        """CylindricalGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _454.CylindricalGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_duty_cycle_rating(self) -> '_531.ConicalGearDutyCycleRating':
        """ConicalGearDutyCycleRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _531.ConicalGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_rating(self) -> '_533.ConicalGearRating':
        """ConicalGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _533.ConicalGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_concept_gear_duty_cycle_rating(self) -> '_541.ConceptGearDutyCycleRating':
        """ConceptGearDutyCycleRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _541.ConceptGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConceptGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_concept_gear_rating(self) -> '_544.ConceptGearRating':
        """ConceptGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _544.ConceptGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConceptGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_bevel_gear_rating(self) -> '_548.BevelGearRating':
        """BevelGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _548.BevelGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to BevelGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_agma_gleason_conical_gear_rating(self) -> '_559.AGMAGleasonConicalGearRating':
        """AGMAGleasonConicalGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _559.AGMAGleasonConicalGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to AGMAGleasonConicalGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_manufacturing_config(self) -> '_605.CylindricalGearManufacturingConfig':
        """CylindricalGearManufacturingConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _605.CylindricalGearManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_manufactured_gear_duty_cycle(self) -> '_609.CylindricalManufacturedGearDutyCycle':
        """CylindricalManufacturedGearDutyCycle: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _609.CylindricalManufacturedGearDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalManufacturedGearDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_manufactured_gear_load_case(self) -> '_610.CylindricalManufacturedGearLoadCase':
        """CylindricalManufacturedGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _610.CylindricalManufacturedGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalManufacturedGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_manufacturing_analysis(self) -> '_768.ConicalGearManufacturingAnalysis':
        """ConicalGearManufacturingAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _768.ConicalGearManufacturingAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearManufacturingAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_manufacturing_config(self) -> '_769.ConicalGearManufacturingConfig':
        """ConicalGearManufacturingConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _769.ConicalGearManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_micro_geometry_config(self) -> '_770.ConicalGearMicroGeometryConfig':
        """ConicalGearMicroGeometryConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _770.ConicalGearMicroGeometryConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearMicroGeometryConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_micro_geometry_config_base(self) -> '_771.ConicalGearMicroGeometryConfigBase':
        """ConicalGearMicroGeometryConfigBase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _771.ConicalGearMicroGeometryConfigBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearMicroGeometryConfigBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_pinion_manufacturing_config(self) -> '_781.ConicalPinionManufacturingConfig':
        """ConicalPinionManufacturingConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _781.ConicalPinionManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalPinionManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_pinion_micro_geometry_config(self) -> '_782.ConicalPinionMicroGeometryConfig':
        """ConicalPinionMicroGeometryConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _782.ConicalPinionMicroGeometryConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalPinionMicroGeometryConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_wheel_manufacturing_config(self) -> '_787.ConicalWheelManufacturingConfig':
        """ConicalWheelManufacturingConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _787.ConicalWheelManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalWheelManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_gear_load_distribution_analysis(self) -> '_833.GearLoadDistributionAnalysis':
        """GearLoadDistributionAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _833.GearLoadDistributionAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearLoadDistributionAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_load_distribution_analysis(self) -> '_849.CylindricalGearLoadDistributionAnalysis':
        """CylindricalGearLoadDistributionAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _849.CylindricalGearLoadDistributionAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearLoadDistributionAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_load_distribution_analysis(self) -> '_860.ConicalGearLoadDistributionAnalysis':
        """ConicalGearLoadDistributionAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _860.ConicalGearLoadDistributionAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearLoadDistributionAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_gear_load_case_base(self) -> '_866.GearLoadCaseBase':
        """GearLoadCaseBase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _866.GearLoadCaseBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearLoadCaseBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_worm_gear_load_case(self) -> '_869.WormGearLoadCase':
        """WormGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _869.WormGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to WormGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_face_gear_load_case(self) -> '_872.FaceGearLoadCase':
        """FaceGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _872.FaceGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to FaceGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_load_case(self) -> '_875.CylindricalGearLoadCase':
        """CylindricalGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _875.CylindricalGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_load_case(self) -> '_878.ConicalGearLoadCase':
        """ConicalGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _878.ConicalGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_concept_gear_load_case(self) -> '_881.ConceptGearLoadCase':
        """ConceptGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _881.ConceptGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConceptGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_bevel_load_case(self) -> '_884.BevelLoadCase':
        """BevelLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _884.BevelLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to BevelLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_tiff_analysis(self) -> '_891.CylindricalGearTIFFAnalysis':
        """CylindricalGearTIFFAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _891.CylindricalGearTIFFAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearTIFFAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_tiff_analysis_duty_cycle(self) -> '_892.CylindricalGearTIFFAnalysisDutyCycle':
        """CylindricalGearTIFFAnalysisDutyCycle: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _892.CylindricalGearTIFFAnalysisDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearTIFFAnalysisDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_face_gear_micro_geometry(self) -> '_986.FaceGearMicroGeometry':
        """FaceGearMicroGeometry: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _986.FaceGearMicroGeometry.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to FaceGearMicroGeometry. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_micro_geometry(self) -> '_1092.CylindricalGearMicroGeometry':
        """CylindricalGearMicroGeometry: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1092.CylindricalGearMicroGeometry.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearMicroGeometry. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_micro_geometry_base(self) -> '_1093.CylindricalGearMicroGeometryBase':
        """CylindricalGearMicroGeometryBase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1093.CylindricalGearMicroGeometryBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearMicroGeometryBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_micro_geometry_duty_cycle(self) -> '_1094.CylindricalGearMicroGeometryDutyCycle':
        """CylindricalGearMicroGeometryDutyCycle: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1094.CylindricalGearMicroGeometryDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearMicroGeometryDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_micro_geometry_per_tooth(self) -> '_1096.CylindricalGearMicroGeometryPerTooth':
        """CylindricalGearMicroGeometryPerTooth: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1096.CylindricalGearMicroGeometryPerTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearMicroGeometryPerTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_gear_fe_model(self) -> '_1187.GearFEModel':
        """GearFEModel: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1187.GearFEModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearFEModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_fe_model(self) -> '_1191.CylindricalGearFEModel':
        """CylindricalGearFEModel: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1191.CylindricalGearFEModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearFEModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_fe_model(self) -> '_1194.ConicalGearFEModel':
        """ConicalGearFEModel: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1194.ConicalGearFEModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearFEModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_gear_design_analysis(self) -> '_1208.GearDesignAnalysis':
        """GearDesignAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1208.GearDesignAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearDesignAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_gear_implementation_analysis(self) -> '_1209.GearImplementationAnalysis':
        """GearImplementationAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1209.GearImplementationAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearImplementationAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_gear_implementation_analysis_duty_cycle(self) -> '_1210.GearImplementationAnalysisDutyCycle':
        """GearImplementationAnalysisDutyCycle: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1210.GearImplementationAnalysisDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearImplementationAnalysisDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_gear_implementation_detail(self) -> '_1211.GearImplementationDetail':
        """GearImplementationDetail: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        if _1211.GearImplementationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearImplementationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result
