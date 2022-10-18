"""_6524.py

ExternalCADModelCriticalSpeedAnalysis
"""


from mastapy.system_model.part_model import _2404
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6809
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6495
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'ExternalCADModelCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModelCriticalSpeedAnalysis',)


class ExternalCADModelCriticalSpeedAnalysis(_6495.ComponentCriticalSpeedAnalysis):
    """ExternalCADModelCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_CRITICAL_SPEED_ANALYSIS

    def __init__(self, instance_to_wrap: 'ExternalCADModelCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2404.ExternalCADModel':
        """ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6809.ExternalCADModelLoadCase':
        """ExternalCADModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
