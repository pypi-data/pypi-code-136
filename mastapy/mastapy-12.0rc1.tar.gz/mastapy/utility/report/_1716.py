"""_1716.py

CustomDrawing
"""


from mastapy._internal import constructor
from mastapy.utility.report import _1717
from mastapy._internal.python_net import python_net_import

_CUSTOM_DRAWING = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomDrawing')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomDrawing',)


class CustomDrawing(_1717.CustomGraphic):
    """CustomDrawing

    This is a mastapy class.
    """

    TYPE = _CUSTOM_DRAWING

    def __init__(self, instance_to_wrap: 'CustomDrawing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def show_editor(self) -> 'bool':
        """bool: 'ShowEditor' is the original name of this property."""

        temp = self.wrapped.ShowEditor

        if temp is None:
            return False

        return temp

    @show_editor.setter
    def show_editor(self, value: 'bool'):
        self.wrapped.ShowEditor = bool(value) if value else False
