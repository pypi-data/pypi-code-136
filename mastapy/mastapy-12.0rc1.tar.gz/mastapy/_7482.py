"""_7482.py

SimpleTaskProgress
"""


from mastapy._internal import constructor
from mastapy import _7476
from mastapy._internal.python_net import python_net_import

_SIMPLE_TASK_PROGRESS = python_net_import('SMT.MastaAPIUtility', 'SimpleTaskProgress')


__docformat__ = 'restructuredtext en'
__all__ = ('SimpleTaskProgress',)


class SimpleTaskProgress(_7476.ConsoleProgress):
    """SimpleTaskProgress

    This is a mastapy class.
    """

    TYPE = _SIMPLE_TASK_PROGRESS

    def __init__(self, instance_to_wrap: 'SimpleTaskProgress.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def complete(self):
        """ 'Complete' is the original name of this method."""

        self.wrapped.Complete()
