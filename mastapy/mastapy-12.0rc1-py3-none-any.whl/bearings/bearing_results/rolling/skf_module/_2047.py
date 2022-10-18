"""_2047.py

MinimumLoad
"""


from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2052
from mastapy._internal.python_net import python_net_import

_MINIMUM_LOAD = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'MinimumLoad')


__docformat__ = 'restructuredtext en'
__all__ = ('MinimumLoad',)


class MinimumLoad(_2052.SKFCalculationResult):
    """MinimumLoad

    This is a mastapy class.
    """

    TYPE = _MINIMUM_LOAD

    def __init__(self, instance_to_wrap: 'MinimumLoad.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def requirement_met(self) -> 'bool':
        """bool: 'RequirementMet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RequirementMet

        if temp is None:
            return False

        return temp
