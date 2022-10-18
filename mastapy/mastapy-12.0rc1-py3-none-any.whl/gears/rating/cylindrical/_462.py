"""_462.py

CylindricalPlasticGearRatingSettings
"""


from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalPlasticGearRatingSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlasticGearRatingSettings',)


class CylindricalPlasticGearRatingSettings(_0.APIBase):
    """CylindricalPlasticGearRatingSettings

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS

    def __init__(self, instance_to_wrap: 'CylindricalPlasticGearRatingSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
