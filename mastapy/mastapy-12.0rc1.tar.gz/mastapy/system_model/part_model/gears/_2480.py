"""_2480.py

FaceGearSet
"""


from typing import List

from mastapy.gears.gear_designs.face import _988
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2479, _2483
from mastapy.system_model.connections_and_sockets.gears import _2263
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'FaceGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSet',)


class FaceGearSet(_2483.GearSet):
    """FaceGearSet

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET

    def __init__(self, instance_to_wrap: 'FaceGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_set_design(self) -> '_988.FaceGearSetDesign':
        """FaceGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_gear_set_design(self) -> '_988.FaceGearSetDesign':
        """FaceGearSetDesign: 'FaceGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_gears(self) -> 'List[_2479.FaceGear]':
        """List[FaceGear]: 'FaceGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes(self) -> 'List[_2263.FaceGearMesh]':
        """List[FaceGearMesh]: 'FaceMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
