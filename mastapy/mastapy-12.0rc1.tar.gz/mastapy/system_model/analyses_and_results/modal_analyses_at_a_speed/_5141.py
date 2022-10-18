"""_5141.py

PointLoadModalAnalysisAtASpeed
"""


from mastapy.system_model.part_model import _2423
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6864
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5177
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'PointLoadModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadModalAnalysisAtASpeed',)


class PointLoadModalAnalysisAtASpeed(_5177.VirtualComponentModalAnalysisAtASpeed):
    """PointLoadModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_MODAL_ANALYSIS_AT_A_SPEED

    def __init__(self, instance_to_wrap: 'PointLoadModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2423.PointLoad':
        """PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6864.PointLoadLoadCase':
        """PointLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
