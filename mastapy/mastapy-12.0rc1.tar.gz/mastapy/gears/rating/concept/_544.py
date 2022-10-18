"""_544.py

ConceptGearRating
"""


from mastapy.gears.rating import _353, _355
from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical import _450, _451
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.concept import _1166
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Concept', 'ConceptGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearRating',)


class ConceptGearRating(_355.GearRating):
    """ConceptGearRating

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_RATING

    def __init__(self, instance_to_wrap: 'ConceptGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def concave_flank_rating(self) -> '_353.GearFlankRating':
        """GearFlankRating: 'ConcaveFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConcaveFlankRating

        if temp is None:
            return None

        if _353.GearFlankRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast concave_flank_rating to GearFlankRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gear(self) -> '_1166.ConceptGearDesign':
        """ConceptGearDesign: 'ConceptGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def convex_flank_rating(self) -> '_353.GearFlankRating':
        """GearFlankRating: 'ConvexFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConvexFlankRating

        if temp is None:
            return None

        if _353.GearFlankRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast convex_flank_rating to GearFlankRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
