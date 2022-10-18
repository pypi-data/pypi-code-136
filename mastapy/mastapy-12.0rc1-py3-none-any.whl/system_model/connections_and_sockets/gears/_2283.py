"""_2283.py

ZerolBevelGearMesh
"""


from mastapy.gears.gear_designs.zerol_bevel import _946
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2255
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ZerolBevelGearMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearMesh',)


class ZerolBevelGearMesh(_2255.BevelGearMesh):
    """ZerolBevelGearMesh

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH

    def __init__(self, instance_to_wrap: 'ZerolBevelGearMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_mesh_design(self) -> '_946.ZerolBevelGearMeshDesign':
        """ZerolBevelGearMeshDesign: 'BevelGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def zerol_bevel_gear_mesh_design(self) -> '_946.ZerolBevelGearMeshDesign':
        """ZerolBevelGearMeshDesign: 'ZerolBevelGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
