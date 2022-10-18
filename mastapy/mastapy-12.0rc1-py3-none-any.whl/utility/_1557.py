"""_1557.py

MethodOutcomeWithResult
"""


from typing import Generic, TypeVar

from mastapy._internal import constructor
from mastapy.utility import _1556
from mastapy._internal.python_net import python_net_import

_METHOD_OUTCOME_WITH_RESULT = python_net_import('SMT.MastaAPI.Utility', 'MethodOutcomeWithResult')


__docformat__ = 'restructuredtext en'
__all__ = ('MethodOutcomeWithResult',)


T = TypeVar('T')


class MethodOutcomeWithResult(_1556.MethodOutcome, Generic[T]):
    """MethodOutcomeWithResult

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _METHOD_OUTCOME_WITH_RESULT

    def __init__(self, instance_to_wrap: 'MethodOutcomeWithResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def result(self) -> 'T':
        """T: 'Result' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Result

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
