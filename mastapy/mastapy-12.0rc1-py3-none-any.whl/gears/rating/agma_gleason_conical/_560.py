"""_560.py

AGMAGleasonConicalGearSetRating
"""


from mastapy.gears.rating.conical import _535
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.AGMAGleasonConical', 'AGMAGleasonConicalGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearSetRating',)


class AGMAGleasonConicalGearSetRating(_535.ConicalGearSetRating):
    """AGMAGleasonConicalGearSetRating

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_RATING

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
