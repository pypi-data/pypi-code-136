"""_1543.py

AnalysisRunInformation
"""


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ANALYSIS_RUN_INFORMATION = python_net_import('SMT.MastaAPI.Utility', 'AnalysisRunInformation')


__docformat__ = 'restructuredtext en'
__all__ = ('AnalysisRunInformation',)


class AnalysisRunInformation(_0.APIBase):
    """AnalysisRunInformation

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_RUN_INFORMATION

    def __init__(self, instance_to_wrap: 'AnalysisRunInformation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def masta_version_used(self) -> 'str':
        """str: 'MASTAVersionUsed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MASTAVersionUsed

        if temp is None:
            return ''

        return temp

    @property
    def specifications_of_computer_used(self) -> 'str':
        """str: 'SpecificationsOfComputerUsed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecificationsOfComputerUsed

        if temp is None:
            return ''

        return temp

    @property
    def time_taken(self) -> 'str':
        """str: 'TimeTaken' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeTaken

        if temp is None:
            return ''

        return temp
