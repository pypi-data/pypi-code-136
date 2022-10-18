"""_5601.py

GenericClutchEngagementStatus
"""


from typing import Generic, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy.system_model import _2159
from mastapy._internal.python_net import python_net_import

_GENERIC_CLUTCH_ENGAGEMENT_STATUS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups', 'GenericClutchEngagementStatus')


__docformat__ = 'restructuredtext en'
__all__ = ('GenericClutchEngagementStatus',)


T = TypeVar('T', bound='_2159.DesignEntity')


class GenericClutchEngagementStatus(_0.APIBase, Generic[T]):
    """GenericClutchEngagementStatus

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _GENERIC_CLUTCH_ENGAGEMENT_STATUS

    def __init__(self, instance_to_wrap: 'GenericClutchEngagementStatus.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_engaged(self) -> 'bool':
        """bool: 'IsEngaged' is the original name of this property."""

        temp = self.wrapped.IsEngaged

        if temp is None:
            return False

        return temp

    @is_engaged.setter
    def is_engaged(self, value: 'bool'):
        self.wrapped.IsEngaged = bool(value) if value else False

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def unique_name(self) -> 'str':
        """str: 'UniqueName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UniqueName

        if temp is None:
            return ''

        return temp
