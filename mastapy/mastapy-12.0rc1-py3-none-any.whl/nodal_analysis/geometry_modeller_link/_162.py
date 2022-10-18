"""_162.py

MeshRequestResult
"""


from typing import Dict

from mastapy._internal import constructor
from mastapy.geometry.two_d import _305
from mastapy.math_utility import _1474
from mastapy.nodal_analysis.geometry_modeller_link import _154, _155
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_MESH_REQUEST_RESULT = python_net_import('SMT.MastaAPI.NodalAnalysis.GeometryModellerLink', 'MeshRequestResult')


__docformat__ = 'restructuredtext en'
__all__ = ('MeshRequestResult',)


class MeshRequestResult(_0.APIBase):
    """MeshRequestResult

    This is a mastapy class.
    """

    TYPE = _MESH_REQUEST_RESULT

    def __init__(self, instance_to_wrap: 'MeshRequestResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def aborted(self) -> 'bool':
        """bool: 'Aborted' is the original name of this property."""

        temp = self.wrapped.Aborted

        if temp is None:
            return False

        return temp

    @aborted.setter
    def aborted(self, value: 'bool'):
        self.wrapped.Aborted = bool(value) if value else False

    @property
    def body_moniker(self) -> 'str':
        """str: 'BodyMoniker' is the original name of this property."""

        temp = self.wrapped.BodyMoniker

        if temp is None:
            return ''

        return temp

    @body_moniker.setter
    def body_moniker(self, value: 'str'):
        self.wrapped.BodyMoniker = str(value) if value else ''

    @property
    def cad_face_group(self) -> '_305.CADFaceGroup':
        """CADFaceGroup: 'CADFaceGroup' is the original name of this property."""

        temp = self.wrapped.CADFaceGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @cad_face_group.setter
    def cad_face_group(self, value: '_305.CADFaceGroup'):
        value = value.wrapped if value else None
        self.wrapped.CADFaceGroup = value

    @property
    def data_file_name(self) -> 'str':
        """str: 'DataFileName' is the original name of this property."""

        temp = self.wrapped.DataFileName

        if temp is None:
            return ''

        return temp

    @data_file_name.setter
    def data_file_name(self, value: 'str'):
        self.wrapped.DataFileName = str(value) if value else ''

    @property
    def error_message(self) -> 'str':
        """str: 'ErrorMessage' is the original name of this property."""

        temp = self.wrapped.ErrorMessage

        if temp is None:
            return ''

        return temp

    @error_message.setter
    def error_message(self, value: 'str'):
        self.wrapped.ErrorMessage = str(value) if value else ''

    @property
    def faceted_body(self) -> '_1474.FacetedBody':
        """FacetedBody: 'FacetedBody' is the original name of this property."""

        temp = self.wrapped.FacetedBody

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @faceted_body.setter
    def faceted_body(self, value: '_1474.FacetedBody'):
        value = value.wrapped if value else None
        self.wrapped.FacetedBody = value

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

    def set_geometry_modeller_dimensions(self, dimensions: 'Dict[str, _155.GeometryModellerDimension]'):
        """ 'SetGeometryModellerDimensions' is the original name of this method.

        Args:
            dimensions (Dict[str, mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimension])
        """

        self.wrapped.SetGeometryModellerDimensions(dimensions)
