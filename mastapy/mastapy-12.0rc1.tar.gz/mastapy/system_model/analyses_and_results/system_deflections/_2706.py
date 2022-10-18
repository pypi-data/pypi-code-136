"""_2706.py

GearSetSystemDeflection
"""


from typing import Optional

from mastapy.system_model.part_model.gears import (
    _2483, _2465, _2467, _2471,
    _2473, _2475, _2477, _2480,
    _2486, _2488, _2490, _2492,
    _2493, _2495, _2497, _2499,
    _2503, _2505
)
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating import _357
from mastapy.gears.rating.zerol_bevel import _365
from mastapy.gears.rating.worm import _370
from mastapy.gears.rating.straight_bevel import _391
from mastapy.gears.rating.straight_bevel_diff import _394
from mastapy.gears.rating.spiral_bevel import _398
from mastapy.gears.rating.klingelnberg_spiral_bevel import _401
from mastapy.gears.rating.klingelnberg_hypoid import _404
from mastapy.gears.rating.klingelnberg_conical import _407
from mastapy.gears.rating.hypoid import _434
from mastapy.gears.rating.face import _444
from mastapy.gears.rating.cylindrical import _458
from mastapy.gears.rating.conical import _535
from mastapy.gears.rating.concept import _546
from mastapy.gears.rating.bevel import _549
from mastapy.gears.rating.agma_gleason_conical import _560
from mastapy.system_model.analyses_and_results.power_flows import (
    _4037, _3982, _3989, _3994,
    _4007, _4010, _4026, _4032,
    _4041, _4045, _4048, _4051,
    _4061, _4080, _4086, _4089,
    _4105, _4108
)
from mastapy.gears.analysis import _1221, _1218
from mastapy.gears import _323
from mastapy import _7483
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results.system_deflections import _2752

_GEAR_SET_IMPLEMENTATION_DETAIL = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearSetImplementationDetail')
_GEAR_SET_MODES = python_net_import('SMT.MastaAPI.Gears', 'GearSetModes')
_TASK_PROGRESS = python_net_import('SMT.MastaAPIUtility', 'TaskProgress')
_BOOLEAN = python_net_import('System', 'Boolean')
_GEAR_SET_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'GearSetSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetSystemDeflection',)


class GearSetSystemDeflection(_2752.SpecialisedAssemblySystemDeflection):
    """GearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'GearSetSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2483.GearSet':
        """GearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2483.GearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to GearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_agma_gleason_conical_gear_set(self) -> '_2465.AGMAGleasonConicalGearSet':
        """AGMAGleasonConicalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2465.AGMAGleasonConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to AGMAGleasonConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_bevel_differential_gear_set(self) -> '_2467.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2467.BevelDifferentialGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to BevelDifferentialGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_bevel_gear_set(self) -> '_2471.BevelGearSet':
        """BevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2471.BevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to BevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_concept_gear_set(self) -> '_2473.ConceptGearSet':
        """ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2473.ConceptGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to ConceptGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_conical_gear_set(self) -> '_2475.ConicalGearSet':
        """ConicalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2475.ConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to ConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_cylindrical_gear_set(self) -> '_2477.CylindricalGearSet':
        """CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2477.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_face_gear_set(self) -> '_2480.FaceGearSet':
        """FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2480.FaceGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to FaceGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_hypoid_gear_set(self) -> '_2486.HypoidGearSet':
        """HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2486.HypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to HypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> '_2488.KlingelnbergCycloPalloidConicalGearSet':
        """KlingelnbergCycloPalloidConicalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2488.KlingelnbergCycloPalloidConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to KlingelnbergCycloPalloidConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2490.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2490.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2492.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2492.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_planetary_gear_set(self) -> '_2493.PlanetaryGearSet':
        """PlanetaryGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2493.PlanetaryGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to PlanetaryGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_spiral_bevel_gear_set(self) -> '_2495.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2495.SpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to SpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_straight_bevel_diff_gear_set(self) -> '_2497.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2497.StraightBevelDiffGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to StraightBevelDiffGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_straight_bevel_gear_set(self) -> '_2499.StraightBevelGearSet':
        """StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2499.StraightBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to StraightBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_worm_gear_set(self) -> '_2503.WormGearSet':
        """WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2503.WormGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to WormGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design_of_type_zerol_bevel_gear_set(self) -> '_2505.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2505.ZerolBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to ZerolBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_357.GearSetRating':
        """GearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _357.GearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to GearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_zerol_bevel_gear_set_rating(self) -> '_365.ZerolBevelGearSetRating':
        """ZerolBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _365.ZerolBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to ZerolBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_worm_gear_set_rating(self) -> '_370.WormGearSetRating':
        """WormGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _370.WormGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to WormGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_straight_bevel_gear_set_rating(self) -> '_391.StraightBevelGearSetRating':
        """StraightBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _391.StraightBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to StraightBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_straight_bevel_diff_gear_set_rating(self) -> '_394.StraightBevelDiffGearSetRating':
        """StraightBevelDiffGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _394.StraightBevelDiffGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to StraightBevelDiffGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_spiral_bevel_gear_set_rating(self) -> '_398.SpiralBevelGearSetRating':
        """SpiralBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _398.SpiralBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to SpiralBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(self) -> '_401.KlingelnbergCycloPalloidSpiralBevelGearSetRating':
        """KlingelnbergCycloPalloidSpiralBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _401.KlingelnbergCycloPalloidSpiralBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to KlingelnbergCycloPalloidSpiralBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_rating(self) -> '_404.KlingelnbergCycloPalloidHypoidGearSetRating':
        """KlingelnbergCycloPalloidHypoidGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _404.KlingelnbergCycloPalloidHypoidGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to KlingelnbergCycloPalloidHypoidGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_klingelnberg_cyclo_palloid_conical_gear_set_rating(self) -> '_407.KlingelnbergCycloPalloidConicalGearSetRating':
        """KlingelnbergCycloPalloidConicalGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _407.KlingelnbergCycloPalloidConicalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to KlingelnbergCycloPalloidConicalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_hypoid_gear_set_rating(self) -> '_434.HypoidGearSetRating':
        """HypoidGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _434.HypoidGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to HypoidGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_face_gear_set_rating(self) -> '_444.FaceGearSetRating':
        """FaceGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _444.FaceGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to FaceGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_cylindrical_gear_set_rating(self) -> '_458.CylindricalGearSetRating':
        """CylindricalGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _458.CylindricalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to CylindricalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_conical_gear_set_rating(self) -> '_535.ConicalGearSetRating':
        """ConicalGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _535.ConicalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to ConicalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_concept_gear_set_rating(self) -> '_546.ConceptGearSetRating':
        """ConceptGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _546.ConceptGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to ConceptGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_bevel_gear_set_rating(self) -> '_549.BevelGearSetRating':
        """BevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _549.BevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to BevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_agma_gleason_conical_gear_set_rating(self) -> '_560.AGMAGleasonConicalGearSetRating':
        """AGMAGleasonConicalGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        if _560.AGMAGleasonConicalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to AGMAGleasonConicalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4037.GearSetPowerFlow':
        """GearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4037.GearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to GearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_agma_gleason_conical_gear_set_power_flow(self) -> '_3982.AGMAGleasonConicalGearSetPowerFlow':
        """AGMAGleasonConicalGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _3982.AGMAGleasonConicalGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to AGMAGleasonConicalGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_bevel_differential_gear_set_power_flow(self) -> '_3989.BevelDifferentialGearSetPowerFlow':
        """BevelDifferentialGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _3989.BevelDifferentialGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to BevelDifferentialGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_bevel_gear_set_power_flow(self) -> '_3994.BevelGearSetPowerFlow':
        """BevelGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _3994.BevelGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to BevelGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_concept_gear_set_power_flow(self) -> '_4007.ConceptGearSetPowerFlow':
        """ConceptGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4007.ConceptGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ConceptGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_conical_gear_set_power_flow(self) -> '_4010.ConicalGearSetPowerFlow':
        """ConicalGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4010.ConicalGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ConicalGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_cylindrical_gear_set_power_flow(self) -> '_4026.CylindricalGearSetPowerFlow':
        """CylindricalGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4026.CylindricalGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to CylindricalGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_face_gear_set_power_flow(self) -> '_4032.FaceGearSetPowerFlow':
        """FaceGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4032.FaceGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to FaceGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_hypoid_gear_set_power_flow(self) -> '_4041.HypoidGearSetPowerFlow':
        """HypoidGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4041.HypoidGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to HypoidGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_klingelnberg_cyclo_palloid_conical_gear_set_power_flow(self) -> '_4045.KlingelnbergCycloPalloidConicalGearSetPowerFlow':
        """KlingelnbergCycloPalloidConicalGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4045.KlingelnbergCycloPalloidConicalGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to KlingelnbergCycloPalloidConicalGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(self) -> '_4048.KlingelnbergCycloPalloidHypoidGearSetPowerFlow':
        """KlingelnbergCycloPalloidHypoidGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4048.KlingelnbergCycloPalloidHypoidGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to KlingelnbergCycloPalloidHypoidGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(self) -> '_4051.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow':
        """KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4051.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_planetary_gear_set_power_flow(self) -> '_4061.PlanetaryGearSetPowerFlow':
        """PlanetaryGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4061.PlanetaryGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to PlanetaryGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_spiral_bevel_gear_set_power_flow(self) -> '_4080.SpiralBevelGearSetPowerFlow':
        """SpiralBevelGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4080.SpiralBevelGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to SpiralBevelGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_straight_bevel_diff_gear_set_power_flow(self) -> '_4086.StraightBevelDiffGearSetPowerFlow':
        """StraightBevelDiffGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4086.StraightBevelDiffGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to StraightBevelDiffGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_straight_bevel_gear_set_power_flow(self) -> '_4089.StraightBevelGearSetPowerFlow':
        """StraightBevelGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4089.StraightBevelGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to StraightBevelGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_worm_gear_set_power_flow(self) -> '_4105.WormGearSetPowerFlow':
        """WormGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4105.WormGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to WormGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_zerol_bevel_gear_set_power_flow(self) -> '_4108.ZerolBevelGearSetPowerFlow':
        """ZerolBevelGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        if _4108.ZerolBevelGearSetPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ZerolBevelGearSetPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def analysis_for(self, gear_set_imp_detail: '_1221.GearSetImplementationDetail', gear_set_mode: '_323.GearSetModes') -> '_1218.GearSetImplementationAnalysis':
        """ 'AnalysisFor' is the original name of this method.

        Args:
            gear_set_imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)

        Returns:
            mastapy.gears.analysis.GearSetImplementationAnalysis
        """

        gear_set_mode = conversion.mp_to_pn_enum(gear_set_mode)
        method_result = self.wrapped.AnalysisFor(gear_set_imp_detail.wrapped if gear_set_imp_detail else None, gear_set_mode)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def implementation_detail_results_failed_for(self, gear_set_imp_detail: '_1221.GearSetImplementationDetail', gear_set_mode: '_323.GearSetModes') -> 'bool':
        """ 'ImplementationDetailResultsFailedFor' is the original name of this method.

        Args:
            gear_set_imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)

        Returns:
            bool
        """

        gear_set_mode = conversion.mp_to_pn_enum(gear_set_mode)
        method_result = self.wrapped.ImplementationDetailResultsFailedFor(gear_set_imp_detail.wrapped if gear_set_imp_detail else None, gear_set_mode)
        return method_result

    def perform_implementation_detail_analysis_with_progress(self, imp_detail: '_1221.GearSetImplementationDetail', gear_set_mode: '_323.GearSetModes', progress: '_7483.TaskProgress', run_all_planetary_meshes: Optional['bool'] = True):
        """ 'PerformImplementationDetailAnalysis' is the original name of this method.

        Args:
            imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)
            progress (mastapy.TaskProgress)
            run_all_planetary_meshes (bool, optional)
        """

        gear_set_mode = conversion.mp_to_pn_enum(gear_set_mode)
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformImplementationDetailAnalysis.Overloads[_GEAR_SET_IMPLEMENTATION_DETAIL, _GEAR_SET_MODES, _TASK_PROGRESS, _BOOLEAN](imp_detail.wrapped if imp_detail else None, gear_set_mode, progress.wrapped if progress else None, run_all_planetary_meshes if run_all_planetary_meshes else False)

    def perform_implementation_detail_analysis(self, imp_detail: '_1221.GearSetImplementationDetail', gear_set_mode: '_323.GearSetModes', run_all_planetary_meshes: Optional['bool'] = True):
        """ 'PerformImplementationDetailAnalysis' is the original name of this method.

        Args:
            imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)
            run_all_planetary_meshes (bool, optional)
        """

        gear_set_mode = conversion.mp_to_pn_enum(gear_set_mode)
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformImplementationDetailAnalysis.Overloads[_GEAR_SET_IMPLEMENTATION_DETAIL, _GEAR_SET_MODES, _BOOLEAN](imp_detail.wrapped if imp_detail else None, gear_set_mode, run_all_planetary_meshes if run_all_planetary_meshes else False)
