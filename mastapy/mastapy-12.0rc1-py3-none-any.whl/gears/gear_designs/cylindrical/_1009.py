"""_1009.py

CylindricalGearDesignConstraintSettings
"""


from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DESIGN_CONSTRAINT_SETTINGS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearDesignConstraintSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearDesignConstraintSettings',)


class CylindricalGearDesignConstraintSettings(_0.APIBase):
    """CylindricalGearDesignConstraintSettings

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DESIGN_CONSTRAINT_SETTINGS

    def __init__(self, instance_to_wrap: 'CylindricalGearDesignConstraintSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
