"""_2275.py

SpiralBevelGearMesh
"""


from mastapy.gears.gear_designs.spiral_bevel import _963
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2255
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'SpiralBevelGearMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearMesh',)


class SpiralBevelGearMesh(_2255.BevelGearMesh):
    """SpiralBevelGearMesh

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH

    def __init__(self, instance_to_wrap: 'SpiralBevelGearMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_mesh_design(self) -> '_963.SpiralBevelGearMeshDesign':
        """SpiralBevelGearMeshDesign: 'BevelGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spiral_bevel_gear_mesh_design(self) -> '_963.SpiralBevelGearMeshDesign':
        """SpiralBevelGearMeshDesign: 'SpiralBevelGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
