"""_1138.py

HypoidGearSetCreationOptions
"""


from mastapy.gears.gear_designs.creation_options import _1137
from mastapy.gears.gear_designs.hypoid import _980
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.CreationOptions', 'HypoidGearSetCreationOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetCreationOptions',)


class HypoidGearSetCreationOptions(_1137.GearSetCreationOptions['_980.HypoidGearSetDesign']):
    """HypoidGearSetCreationOptions

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_CREATION_OPTIONS

    def __init__(self, instance_to_wrap: 'HypoidGearSetCreationOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
