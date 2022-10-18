"""_6480.py

BeltDriveCriticalSpeedAnalysis
"""


from mastapy.system_model.part_model.couplings import _2527, _2537
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6748, _6781
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6570
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'BeltDriveCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDriveCriticalSpeedAnalysis',)


class BeltDriveCriticalSpeedAnalysis(_6570.SpecialisedAssemblyCriticalSpeedAnalysis):
    """BeltDriveCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_CRITICAL_SPEED_ANALYSIS

    def __init__(self, instance_to_wrap: 'BeltDriveCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2527.BeltDrive':
        """BeltDrive: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2527.BeltDrive.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to BeltDrive. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6748.BeltDriveLoadCase':
        """BeltDriveLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        if _6748.BeltDriveLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_load_case to BeltDriveLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
