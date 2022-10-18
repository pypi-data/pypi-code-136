"""_6525.py

FaceGearCriticalSpeedAnalysis
"""


from mastapy.system_model.part_model.gears import _2479
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6810
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6530
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'FaceGearCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearCriticalSpeedAnalysis',)


class FaceGearCriticalSpeedAnalysis(_6530.GearCriticalSpeedAnalysis):
    """FaceGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_CRITICAL_SPEED_ANALYSIS

    def __init__(self, instance_to_wrap: 'FaceGearCriticalSpeedAnalysis.TYPE'):
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
