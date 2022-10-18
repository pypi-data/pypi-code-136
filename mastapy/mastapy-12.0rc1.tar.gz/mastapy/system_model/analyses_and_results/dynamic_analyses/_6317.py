"""_6317.py

StraightBevelPlanetGearDynamicAnalysis
"""


from mastapy.system_model.part_model.gears import _2500
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'StraightBevelPlanetGearDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelPlanetGearDynamicAnalysis',)


class StraightBevelPlanetGearDynamicAnalysis(_6311.StraightBevelDiffGearDynamicAnalysis):
    """StraightBevelPlanetGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_DYNAMIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'StraightBevelPlanetGearDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2500.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
