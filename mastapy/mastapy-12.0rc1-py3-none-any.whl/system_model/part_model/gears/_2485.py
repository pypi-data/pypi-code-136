"""_2485.py

HypoidGear
"""


from mastapy.gears.gear_designs.hypoid import _978
from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2464
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'HypoidGear')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGear',)


class HypoidGear(_2464.AGMAGleasonConicalGear):
    """HypoidGear

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR

    def __init__(self, instance_to_wrap: 'HypoidGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_design(self) -> '_978.HypoidGearDesign':
        """HypoidGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hypoid_gear_design(self) -> '_978.HypoidGearDesign':
        """HypoidGearDesign: 'HypoidGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
