"""_446.py

CylindricalGearDesignAndRatingSettings
"""


from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DESIGN_AND_RATING_SETTINGS = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearDesignAndRatingSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearDesignAndRatingSettings',)


class CylindricalGearDesignAndRatingSettings(_0.APIBase):
    """CylindricalGearDesignAndRatingSettings

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DESIGN_AND_RATING_SETTINGS

    def __init__(self, instance_to_wrap: 'CylindricalGearDesignAndRatingSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
