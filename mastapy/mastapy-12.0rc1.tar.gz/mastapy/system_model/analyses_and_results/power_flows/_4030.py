"""_4030.py

FaceGearMeshPowerFlow
"""


from mastapy.gears.rating.face import _441
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2263
from mastapy.system_model.analyses_and_results.static_loads import _6811
from mastapy.system_model.analyses_and_results.power_flows import _4035
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'FaceGearMeshPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshPowerFlow',)


class FaceGearMeshPowerFlow(_4035.GearMeshPowerFlow):
    """FaceGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_POWER_FLOW

    def __init__(self, instance_to_wrap: 'FaceGearMeshPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> '_441.FaceGearMeshRating':
        """FaceGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_441.FaceGearMeshRating':
        """FaceGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2263.FaceGearMesh':
        """FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6811.FaceGearMeshLoadCase':
        """FaceGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
