"""_6257.py

DynamicAnalysisDrawStyle
"""


from mastapy._internal import constructor
from mastapy.system_model.drawing import _2197
from mastapy._internal.python_net import python_net_import

_DYNAMIC_ANALYSIS_DRAW_STYLE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'DynamicAnalysisDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicAnalysisDrawStyle',)


class DynamicAnalysisDrawStyle(_2197.ContourDrawStyle):
    """DynamicAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_ANALYSIS_DRAW_STYLE

    def __init__(self, instance_to_wrap: 'DynamicAnalysisDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def animate_contour(self) -> 'bool':
        """bool: 'AnimateContour' is the original name of this property."""

        temp = self.wrapped.AnimateContour

        if temp is None:
            return False

        return temp

    @animate_contour.setter
    def animate_contour(self, value: 'bool'):
        self.wrapped.AnimateContour = bool(value) if value else False
