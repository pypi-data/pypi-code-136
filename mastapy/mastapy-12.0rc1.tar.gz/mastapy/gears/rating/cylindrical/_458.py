"""_458.py

CylindricalGearSetRating
"""


from typing import List

from mastapy.materials import _245
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.gear_designs.cylindrical import _1021, _1033
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.cylindrical.optimisation import _494
from mastapy.gears.rating.cylindrical import _448, _454, _452
from mastapy.gears.rating.cylindrical.vdi import _482
from mastapy.gears.rating import _357
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetRating',)


class CylindricalGearSetRating(_357.GearSetRating):
    """CylindricalGearSetRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_RATING

    def __init__(self, instance_to_wrap: 'CylindricalGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating_method(self) -> '_245.CylindricalGearRatingMethods':
        """CylindricalGearRatingMethods: 'RatingMethod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_245.CylindricalGearRatingMethods)(value) if value is not None else None

    @property
    def rating_standard_name(self) -> 'str':
        """str: 'RatingStandardName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ''

        return temp

    @property
    def cylindrical_gear_set(self) -> '_1021.CylindricalGearSetDesign':
        """CylindricalGearSetDesign: 'CylindricalGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSet

        if temp is None:
            return None

        if _1021.CylindricalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cylindrical_gear_set to CylindricalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def optimisations(self) -> '_494.CylindricalGearSetRatingOptimisationHelper':
        """CylindricalGearSetRatingOptimisationHelper: 'Optimisations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Optimisations

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_settings(self) -> '_448.CylindricalGearDesignAndRatingSettingsItem':
        """CylindricalGearDesignAndRatingSettingsItem: 'RatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_ratings(self) -> 'List[_454.CylindricalGearRating]':
        """List[CylindricalGearRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_ratings(self) -> 'List[_454.CylindricalGearRating]':
        """List[CylindricalGearRating]: 'CylindricalGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_mesh_ratings(self) -> 'List[_452.CylindricalGearMeshRating]':
        """List[CylindricalGearMeshRating]: 'CylindricalMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def vdi_cylindrical_gear_single_flank_ratings(self) -> 'List[_482.VDI2737InternalGearSingleFlankRating]':
        """List[VDI2737InternalGearSingleFlankRating]: 'VDICylindricalGearSingleFlankRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VDICylindricalGearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
