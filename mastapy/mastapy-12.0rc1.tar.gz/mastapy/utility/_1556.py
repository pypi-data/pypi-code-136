"""_1556.py

MethodOutcome
"""


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_METHOD_OUTCOME = python_net_import('SMT.MastaAPI.Utility', 'MethodOutcome')


__docformat__ = 'restructuredtext en'
__all__ = ('MethodOutcome',)


class MethodOutcome(_0.APIBase):
    """MethodOutcome

    This is a mastapy class.
    """

    TYPE = _METHOD_OUTCOME

    def __init__(self, instance_to_wrap: 'MethodOutcome.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def failure_message(self) -> 'str':
        """str: 'FailureMessage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FailureMessage

        if temp is None:
            return ''

        return temp

    @property
    def successful(self) -> 'bool':
        """bool: 'Successful' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Successful

        if temp is None:
            return False

        return temp
