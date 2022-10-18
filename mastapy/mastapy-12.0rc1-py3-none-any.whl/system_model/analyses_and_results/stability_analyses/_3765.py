"""_3765.py

FaceGearStabilityAnalysis
"""


from mastapy.system_model.part_model.gears import _2479
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6810
from mastapy.system_model.analyses_and_results.stability_analyses import _3770
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'FaceGearStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearStabilityAnalysis',)


class FaceGearStabilityAnalysis(_3770.GearStabilityAnalysis):
    """FaceGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_STABILITY_ANALYSIS

    def __init__(self, instance_to_wrap: 'FaceGearStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2479.FaceGear':
        """FaceGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6810.FaceGearLoadCase':
        """FaceGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
