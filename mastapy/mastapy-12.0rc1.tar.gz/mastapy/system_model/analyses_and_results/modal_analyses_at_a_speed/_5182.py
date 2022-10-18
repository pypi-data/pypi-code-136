"""_5182.py

ZerolBevelGearModalAnalysisAtASpeed
"""


from mastapy.system_model.part_model.gears import _2504
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6911
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5072
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'ZerolBevelGearModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearModalAnalysisAtASpeed',)


class ZerolBevelGearModalAnalysisAtASpeed(_5072.BevelGearModalAnalysisAtASpeed):
    """ZerolBevelGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MODAL_ANALYSIS_AT_A_SPEED

    def __init__(self, instance_to_wrap: 'ZerolBevelGearModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2504.ZerolBevelGear':
        """ZerolBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6911.ZerolBevelGearLoadCase':
        """ZerolBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
