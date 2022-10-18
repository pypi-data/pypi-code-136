"""_886.py

BevelSetLoadCase
"""


from mastapy.gears.load_case.conical import _879
from mastapy._internal.python_net import python_net_import

_BEVEL_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Bevel', 'BevelSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelSetLoadCase',)


class BevelSetLoadCase(_879.ConicalGearSetLoadCase):
    """BevelSetLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_SET_LOAD_CASE

    def __init__(self, instance_to_wrap: 'BevelSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
