"""_5327.py

BevelDifferentialGearMultibodyDynamicsAnalysis
"""


from mastapy.system_model.part_model.gears import _2466, _2468, _2469
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6749, _6752, _6753
from mastapy.system_model.analyses_and_results.mbd_analyses import _5332
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'BevelDifferentialGearMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearMultibodyDynamicsAnalysis',)


class BevelDifferentialGearMultibodyDynamicsAnalysis(_5332.BevelGearMultibodyDynamicsAnalysis):
    """BevelDifferentialGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2466.BevelDifferentialGear':
        """BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2466.BevelDifferentialGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6749.BevelDifferentialGearLoadCase':
        """BevelDifferentialGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        if _6749.BevelDifferentialGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_load_case to BevelDifferentialGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
