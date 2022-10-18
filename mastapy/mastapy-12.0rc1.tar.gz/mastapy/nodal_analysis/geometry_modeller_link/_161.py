"""_161.py

MeshRequest
"""


from typing import Dict

from mastapy._internal import constructor
from mastapy.nodal_analysis.geometry_modeller_link import _154, _155
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_MESH_REQUEST = python_net_import('SMT.MastaAPI.NodalAnalysis.GeometryModellerLink', 'MeshRequest')


__docformat__ = 'restructuredtext en'
__all__ = ('MeshRequest',)


class MeshRequest(_0.APIBase):
    """MeshRequest

    This is a mastapy class.
    """

    TYPE = _MESH_REQUEST

    def __init__(self, instance_to_wrap: 'MeshRequest.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cad_face_group(self) -> 'bool':
        """bool: 'CADFaceGroup' is the original name of this property."""

        temp = self.wrapped.CADFaceGroup

        if temp is None:
            return False

        return temp

    @cad_face_group.setter
    def cad_face_group(self, value: 'bool'):
        self.wrapped.CADFaceGroup = bool(value) if value else False

    @property
    def geometry_modeller_design_information(self) -> '_154.GeometryModellerDesignInformation':
        """GeometryModellerDesignInformation: 'GeometryModellerDesignInformation' is the original name of this property."""

        temp = self.wrapped.GeometryModellerDesignInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @geometry_modeller_design_information.setter
    def geometry_modeller_design_information(self, value: '_154.GeometryModellerDesignInformation'):
        value = value.wrapped if value else None
        self.wrapped.GeometryModellerDesignInformation = value

    @property
    def moniker(self) -> 'str':
        """str: 'Moniker' is the original name of this property."""

        temp = self.wrapped.Moniker

        if temp is None:
            return ''

        return temp

    @moniker.setter
    def moniker(self, value: 'str'):
        self.wrapped.Moniker = str(value) if value else ''

    def geometry_modeller_dimensions(self) -> 'Dict[str, _155.GeometryModellerDimension]':
        """ 'GeometryModellerDimensions' is the original name of this method.

        Returns:
            Dict[str, mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimension]
        """

        method_result = self.wrapped.GeometryModellerDimensions()
        return method_result
