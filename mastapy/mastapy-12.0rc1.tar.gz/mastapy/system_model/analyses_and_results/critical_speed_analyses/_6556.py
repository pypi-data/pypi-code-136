"""_6556.py

PlanetaryGearSetCriticalSpeedAnalysis
"""


from mastapy.system_model.part_model.gears import _2493
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6521
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'PlanetaryGearSetCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryGearSetCriticalSpeedAnalysis',)


class PlanetaryGearSetCriticalSpeedAnalysis(_6521.CylindricalGearSetCriticalSpeedAnalysis):
    """PlanetaryGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_CRITICAL_SPEED_ANALYSIS

    def __init__(self, instance_to_wrap: 'PlanetaryGearSetCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2493.PlanetaryGearSet':
        """PlanetaryGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
