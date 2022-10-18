"""_904.py

GearSetOptimiserCandidate
"""


from mastapy.gears.rating import _349, _356, _357
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.zerol_bevel import _365
from mastapy.gears.rating.worm import _369, _370
from mastapy.gears.rating.straight_bevel import _391
from mastapy.gears.rating.straight_bevel_diff import _394
from mastapy.gears.rating.spiral_bevel import _398
from mastapy.gears.rating.klingelnberg_spiral_bevel import _401
from mastapy.gears.rating.klingelnberg_hypoid import _404
from mastapy.gears.rating.klingelnberg_conical import _407
from mastapy.gears.rating.hypoid import _434
from mastapy.gears.rating.face import _443, _444
from mastapy.gears.rating.cylindrical import _457, _458
from mastapy.gears.rating.conical import _534, _535
from mastapy.gears.rating.concept import _545, _546
from mastapy.gears.rating.bevel import _549
from mastapy.gears.rating.agma_gleason_conical import _560
from mastapy.gears.gear_set_pareto_optimiser import _900
from mastapy._internal.python_net import python_net_import

_GEAR_SET_OPTIMISER_CANDIDATE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'GearSetOptimiserCandidate')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetOptimiserCandidate',)


class GearSetOptimiserCandidate(_900.DesignSpaceSearchCandidateBase['_349.AbstractGearSetRating', 'GearSetOptimiserCandidate']):
    """GearSetOptimiserCandidate

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_OPTIMISER_CANDIDATE

    def __init__(self, instance_to_wrap: 'GearSetOptimiserCandidate.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def candidate(self) -> '_349.AbstractGearSetRating':
        """AbstractGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _349.AbstractGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to AbstractGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_gear_set_duty_cycle_rating(self) -> '_356.GearSetDutyCycleRating':
        """GearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _356.GearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to GearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_gear_set_rating(self) -> '_357.GearSetRating':
        """GearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _357.GearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to GearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_zerol_bevel_gear_set_rating(self) -> '_365.ZerolBevelGearSetRating':
        """ZerolBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _365.ZerolBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to ZerolBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_worm_gear_set_duty_cycle_rating(self) -> '_369.WormGearSetDutyCycleRating':
        """WormGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _369.WormGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to WormGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_worm_gear_set_rating(self) -> '_370.WormGearSetRating':
        """WormGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _370.WormGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to WormGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_straight_bevel_gear_set_rating(self) -> '_391.StraightBevelGearSetRating':
        """StraightBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _391.StraightBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to StraightBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_straight_bevel_diff_gear_set_rating(self) -> '_394.StraightBevelDiffGearSetRating':
        """StraightBevelDiffGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _394.StraightBevelDiffGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to StraightBevelDiffGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_spiral_bevel_gear_set_rating(self) -> '_398.SpiralBevelGearSetRating':
        """SpiralBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _398.SpiralBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to SpiralBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(self) -> '_401.KlingelnbergCycloPalloidSpiralBevelGearSetRating':
        """KlingelnbergCycloPalloidSpiralBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _401.KlingelnbergCycloPalloidSpiralBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to KlingelnbergCycloPalloidSpiralBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_rating(self) -> '_404.KlingelnbergCycloPalloidHypoidGearSetRating':
        """KlingelnbergCycloPalloidHypoidGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _404.KlingelnbergCycloPalloidHypoidGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to KlingelnbergCycloPalloidHypoidGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_klingelnberg_cyclo_palloid_conical_gear_set_rating(self) -> '_407.KlingelnbergCycloPalloidConicalGearSetRating':
        """KlingelnbergCycloPalloidConicalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _407.KlingelnbergCycloPalloidConicalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to KlingelnbergCycloPalloidConicalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_hypoid_gear_set_rating(self) -> '_434.HypoidGearSetRating':
        """HypoidGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _434.HypoidGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to HypoidGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_face_gear_set_duty_cycle_rating(self) -> '_443.FaceGearSetDutyCycleRating':
        """FaceGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _443.FaceGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to FaceGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_face_gear_set_rating(self) -> '_444.FaceGearSetRating':
        """FaceGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _444.FaceGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to FaceGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_cylindrical_gear_set_duty_cycle_rating(self) -> '_457.CylindricalGearSetDutyCycleRating':
        """CylindricalGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _457.CylindricalGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to CylindricalGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_cylindrical_gear_set_rating(self) -> '_458.CylindricalGearSetRating':
        """CylindricalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _458.CylindricalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to CylindricalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_conical_gear_set_duty_cycle_rating(self) -> '_534.ConicalGearSetDutyCycleRating':
        """ConicalGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _534.ConicalGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConicalGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_conical_gear_set_rating(self) -> '_535.ConicalGearSetRating':
        """ConicalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _535.ConicalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConicalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_concept_gear_set_duty_cycle_rating(self) -> '_545.ConceptGearSetDutyCycleRating':
        """ConceptGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _545.ConceptGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConceptGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_concept_gear_set_rating(self) -> '_546.ConceptGearSetRating':
        """ConceptGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _546.ConceptGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConceptGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_bevel_gear_set_rating(self) -> '_549.BevelGearSetRating':
        """BevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _549.BevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to BevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_agma_gleason_conical_gear_set_rating(self) -> '_560.AGMAGleasonConicalGearSetRating':
        """AGMAGleasonConicalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        if _560.AGMAGleasonConicalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to AGMAGleasonConicalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def add_design(self):
        """ 'AddDesign' is the original name of this method."""

        self.wrapped.AddDesign()
