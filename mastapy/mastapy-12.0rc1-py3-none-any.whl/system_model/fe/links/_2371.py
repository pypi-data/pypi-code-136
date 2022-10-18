"""_2371.py

FELinkWithSelection
"""


from mastapy.system_model.fe.links import (
    _2369, _2370, _2372, _2373,
    _2374, _2375, _2376, _2377,
    _2378, _2379, _2380, _2381,
    _2382, _2383
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_FE_LINK_WITH_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'FELinkWithSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('FELinkWithSelection',)


class FELinkWithSelection(_0.APIBase):
    """FELinkWithSelection

    This is a mastapy class.
    """

    TYPE = _FE_LINK_WITH_SELECTION

    def __init__(self, instance_to_wrap: 'FELinkWithSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def link(self) -> '_2369.FELink':
        """FELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link

        if temp is None:
            return None

        if _2369.FELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to FELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_electric_machine_stator_fe_link(self) -> '_2370.ElectricMachineStatorFELink':
        """ElectricMachineStatorFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link

        if temp is None:
            return None

        if _2370.ElectricMachineStatorFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to ElectricMachineStatorFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_gear_mesh_fe_link(self) -> '_2372.GearMeshFELink':
        """GearMeshFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link

        if temp is None:
            return None

        if _2372.GearMeshFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to GearMeshFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_gear_with_duplicated_meshes_fe_link(self) -> '_2373.GearWithDuplicatedMeshesFELink':
        """GearWithDuplicatedMeshesFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link

        if temp is None:
            return None

        if _2373.GearWithDuplicatedMeshesFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to GearWithDuplicatedMeshesFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_multi_angle_connection_fe_link(self) -> '_2374.MultiAngleConnectionFELink':
        """MultiAngleConnectionFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link

        if temp is None:
            return None

        if _2374.MultiAngleConnectionFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to MultiAngleConnectionFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_multi_node_connector_fe_link(self) -> '_2375.MultiNodeConnectorFELink':
        """MultiNodeConnectorFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link

        if temp is None:
            return None

        if _2375.MultiNodeConnectorFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to MultiNodeConnectorFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_multi_node_fe_link(self) -> '_2376.MultiNodeFELink':
        """MultiNodeFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link

        if temp is None:
            return None

        if _2376.MultiNodeFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to MultiNodeFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_planetary_connector_multi_node_fe_link(self) -> '_2377.PlanetaryConnectorMultiNodeFELink':
        """PlanetaryConnectorMultiNodeFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link

        if temp is None:
            return None

        if _2377.PlanetaryConnectorMultiNodeFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to PlanetaryConnectorMultiNodeFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_planet_based_fe_link(self) -> '_2378.PlanetBasedFELink':
        """PlanetBasedFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link

        if temp is None:
            return None

        if _2378.PlanetBasedFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to PlanetBasedFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_planet_carrier_fe_link(self) -> '_2379.PlanetCarrierFELink':
        """PlanetCarrierFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link

        if temp is None:
            return None

        if _2379.PlanetCarrierFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to PlanetCarrierFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_point_load_fe_link(self) -> '_2380.PointLoadFELink':
        """PointLoadFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link

        if temp is None:
            return None

        if _2380.PointLoadFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to PointLoadFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_rolling_ring_connection_fe_link(self) -> '_2381.RollingRingConnectionFELink':
        """RollingRingConnectionFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link

        if temp is None:
            return None

        if _2381.RollingRingConnectionFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to RollingRingConnectionFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_shaft_hub_connection_fe_link(self) -> '_2382.ShaftHubConnectionFELink':
        """ShaftHubConnectionFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link

        if temp is None:
            return None

        if _2382.ShaftHubConnectionFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to ShaftHubConnectionFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_single_node_fe_link(self) -> '_2383.SingleNodeFELink':
        """SingleNodeFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link

        if temp is None:
            return None

        if _2383.SingleNodeFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to SingleNodeFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def add_selected_nodes(self):
        """ 'AddSelectedNodes' is the original name of this method."""

        self.wrapped.AddSelectedNodes()

    def delete_all_nodes(self):
        """ 'DeleteAllNodes' is the original name of this method."""

        self.wrapped.DeleteAllNodes()

    def select_component(self):
        """ 'SelectComponent' is the original name of this method."""

        self.wrapped.SelectComponent()
