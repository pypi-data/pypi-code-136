"""_5412.py

PulleyMultibodyDynamicsAnalysis
"""


from typing import List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.couplings import _2541, _2538
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6866, _6782
from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import _5462
from mastapy.system_model.analyses_and_results.mbd_analyses import _5354
from mastapy._internal.python_net import python_net_import

_PULLEY_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'PulleyMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleyMultibodyDynamicsAnalysis',)


class PulleyMultibodyDynamicsAnalysis(_5354.CouplingHalfMultibodyDynamicsAnalysis):
    """PulleyMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PULLEY_MULTIBODY_DYNAMICS_ANALYSIS

    def __init__(self, instance_to_wrap: 'PulleyMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def force_on_pulley_from_belts(self) -> 'Vector3D':
        """Vector3D: 'ForceOnPulleyFromBelts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceOnPulleyFromBelts

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def pulley_torque(self) -> 'List[float]':
        """List[float]: 'PulleyTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PulleyTorque

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def component_design(self) -> '_2541.Pulley':
        """Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2541.Pulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Pulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6866.PulleyLoadCase':
        """PulleyLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        if _6866.PulleyLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_load_case to PulleyLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def peak_pulley_torque(self) -> 'List[_5462.DynamicTorqueResultAtTime]':
        """List[DynamicTorqueResultAtTime]: 'PeakPulleyTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakPulleyTorque

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
