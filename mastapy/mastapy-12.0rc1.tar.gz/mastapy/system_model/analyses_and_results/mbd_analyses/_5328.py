"""_5328.py

BevelDifferentialGearSetMultibodyDynamicsAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2467
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6751
from mastapy.system_model.analyses_and_results.mbd_analyses import _5327, _5326, _5333
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'BevelDifferentialGearSetMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetMultibodyDynamicsAnalysis',)


class BevelDifferentialGearSetMultibodyDynamicsAnalysis(_5333.BevelGearSetMultibodyDynamicsAnalysis):
    """BevelDifferentialGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2467.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6751.BevelDifferentialGearSetLoadCase':
        """BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears(self) -> 'List[_5327.BevelDifferentialGearMultibodyDynamicsAnalysis]':
        """List[BevelDifferentialGearMultibodyDynamicsAnalysis]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gears_multibody_dynamics_analysis(self) -> 'List[_5327.BevelDifferentialGearMultibodyDynamicsAnalysis]':
        """List[BevelDifferentialGearMultibodyDynamicsAnalysis]: 'BevelDifferentialGearsMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_multibody_dynamics_analysis(self) -> 'List[_5326.BevelDifferentialGearMeshMultibodyDynamicsAnalysis]':
        """List[BevelDifferentialGearMeshMultibodyDynamicsAnalysis]: 'BevelDifferentialMeshesMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
