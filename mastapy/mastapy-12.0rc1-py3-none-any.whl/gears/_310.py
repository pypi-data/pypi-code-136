"""_310.py

BevelHypoidGearDesignSettings
"""


from mastapy import _0
from mastapy._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_DESIGN_SETTINGS = python_net_import('SMT.MastaAPI.Gears', 'BevelHypoidGearDesignSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelHypoidGearDesignSettings',)


class BevelHypoidGearDesignSettings(_0.APIBase):
    """BevelHypoidGearDesignSettings

    This is a mastapy class.
    """

    TYPE = _BEVEL_HYPOID_GEAR_DESIGN_SETTINGS

    def __init__(self, instance_to_wrap: 'BevelHypoidGearDesignSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
