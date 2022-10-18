"""_1235.py

CADElectricMachineDetail
"""


from mastapy.nodal_analysis.geometry_modeller_link import _156
from mastapy._internal import constructor
from mastapy.electric_machines import _1237, _1238, _1249
from mastapy._internal.python_net import python_net_import

_CAD_ELECTRIC_MACHINE_DETAIL = python_net_import('SMT.MastaAPI.ElectricMachines', 'CADElectricMachineDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('CADElectricMachineDetail',)


class CADElectricMachineDetail(_1249.ElectricMachineDetail):
    """CADElectricMachineDetail

    This is a mastapy class.
    """

    TYPE = _CAD_ELECTRIC_MACHINE_DETAIL

    def __init__(self, instance_to_wrap: 'CADElectricMachineDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def geometry_modeller_dimensions(self) -> '_156.GeometryModellerDimensions':
        """GeometryModellerDimensions: 'GeometryModellerDimensions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometryModellerDimensions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor(self) -> '_1237.CADRotor':
        """CADRotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rotor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator(self) -> '_1238.CADStator':
        """CADStator: 'Stator' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Stator

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def embed_geometry_modeller_file(self):
        """ 'EmbedGeometryModellerFile' is the original name of this method."""

        self.wrapped.EmbedGeometryModellerFile()

    def open_stored_geometry_modeller_file(self):
        """ 'OpenStoredGeometryModellerFile' is the original name of this method."""

        self.wrapped.OpenStoredGeometryModellerFile()

    def reread_geometry_from_geometry_modeller(self):
        """ 'RereadGeometryFromGeometryModeller' is the original name of this method."""

        self.wrapped.RereadGeometryFromGeometryModeller()

    def update_embedded_geometry_modeller_file(self):
        """ 'UpdateEmbeddedGeometryModellerFile' is the original name of this method."""

        self.wrapped.UpdateEmbeddedGeometryModellerFile()
