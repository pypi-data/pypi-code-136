"""_3723.py

BevelDifferentialPlanetGearStabilityAnalysis
"""


from mastapy.system_model.part_model.gears import _2468
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3722
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'BevelDifferentialPlanetGearStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialPlanetGearStabilityAnalysis',)


class BevelDifferentialPlanetGearStabilityAnalysis(_3722.BevelDifferentialGearStabilityAnalysis):
    """BevelDifferentialPlanetGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_STABILITY_ANALYSIS

    def __init__(self, instance_to_wrap: 'BevelDifferentialPlanetGearStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2468.BevelDifferentialPlanetGear':
        """BevelDifferentialPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
