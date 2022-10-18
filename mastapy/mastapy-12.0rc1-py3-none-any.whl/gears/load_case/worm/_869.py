"""_869.py

WormGearLoadCase
"""


from mastapy.gears.load_case import _866
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Worm', 'WormGearLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearLoadCase',)


class WormGearLoadCase(_866.GearLoadCaseBase):
    """WormGearLoadCase

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_LOAD_CASE

    def __init__(self, instance_to_wrap: 'WormGearLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
