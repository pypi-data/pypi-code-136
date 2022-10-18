"""_2463.py

ActiveGearSetDesignSelectionGroup
"""


from mastapy._internal import constructor
from mastapy.system_model.part_model.configurations import _2568
from mastapy.system_model.part_model.gears import _2462, _2483
from mastapy.gears.gear_designs import _943
from mastapy._internal.python_net import python_net_import

_ACTIVE_GEAR_SET_DESIGN_SELECTION_GROUP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ActiveGearSetDesignSelectionGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveGearSetDesignSelectionGroup',)


class ActiveGearSetDesignSelectionGroup(_2568.PartDetailConfiguration['_2462.ActiveGearSetDesignSelection', '_2483.GearSet', '_943.GearSetDesign']):
    """ActiveGearSetDesignSelectionGroup

    This is a mastapy class.
    """

    TYPE = _ACTIVE_GEAR_SET_DESIGN_SELECTION_GROUP

    def __init__(self, instance_to_wrap: 'ActiveGearSetDesignSelectionGroup.TYPE'):
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
    def minimum_cylindrical_axial_contact_ratio(self) -> 'float':
        """float: 'MinimumCylindricalAxialContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumCylindricalAxialContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_cylindrical_transverse_contact_ratio(self) -> 'float':
        """float: 'MinimumCylindricalTransverseContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumCylindricalTransverseContactRatio

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
    def simple_mass_of_cylindrical_gears(self) -> 'float':
        """float: 'SimpleMassOfCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleMassOfCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def total_face_width_of_cylindrical_gears(self) -> 'float':
        """float: 'TotalFaceWidthOfCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalFaceWidthOfCylindricalGears

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
