'''
# `hcp_consul_cluster`

Refer to the Terraform Registory for docs: [`hcp_consul_cluster`](https://www.terraform.io/docs/providers/hcp/r/consul_cluster).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf
import constructs


class ConsulCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.consulCluster.ConsulCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster hcp_consul_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cluster_id: builtins.str,
        hvn_id: builtins.str,
        tier: builtins.str,
        auto_hvn_to_hvn_peering: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connect_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        datacenter: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        min_consul_version: typing.Optional[builtins.str] = None,
        primary_link: typing.Optional[builtins.str] = None,
        public_endpoint: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        size: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ConsulClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster hcp_consul_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_id: The ID of the HCP Consul cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#cluster_id ConsulCluster#cluster_id}
        :param hvn_id: The ID of the HVN this HCP Consul cluster is associated to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#hvn_id ConsulCluster#hvn_id}
        :param tier: The tier that the HCP Consul cluster will be provisioned as. Only ``development``, ``standard`` and ``plus`` are available at this time. See `pricing information <https://cloud.hashicorp.com/pricing/consul>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#tier ConsulCluster#tier}
        :param auto_hvn_to_hvn_peering: Enables automatic HVN to HVN peering when creating a secondary cluster in a federation. The alternative to using the auto-accept feature is to create an ```hcp_hvn_peering_connection`` <hvn_peering_connection.md>`_ resource that explicitly defines the HVN resources that are allowed to communicate with each other. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#auto_hvn_to_hvn_peering ConsulCluster#auto_hvn_to_hvn_peering}
        :param connect_enabled: Denotes the Consul connect feature should be enabled for this cluster. Default to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#connect_enabled ConsulCluster#connect_enabled}
        :param datacenter: The Consul data center name of the cluster. If not specified, it is defaulted to the value of ``cluster_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#datacenter ConsulCluster#datacenter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#id ConsulCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param min_consul_version: The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently recommended by HCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#min_consul_version ConsulCluster#min_consul_version}
        :param primary_link: The ``self_link`` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If not specified, it is a standalone cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#primary_link ConsulCluster#primary_link}
        :param public_endpoint: Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#public_endpoint ConsulCluster#public_endpoint}
        :param size: The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for development tier - ``x_small``. Valid options for other tiers - ``small``, ``medium``, ``large``. For more details - https://cloud.hashicorp.com/pricing/consul. Upgrading the size of a cluster after creation is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#size ConsulCluster#size}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#timeouts ConsulCluster#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsulCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ConsulClusterConfig(
            cluster_id=cluster_id,
            hvn_id=hvn_id,
            tier=tier,
            auto_hvn_to_hvn_peering=auto_hvn_to_hvn_peering,
            connect_enabled=connect_enabled,
            datacenter=datacenter,
            id=id,
            min_consul_version=min_consul_version,
            primary_link=primary_link,
            public_endpoint=public_endpoint,
            size=size,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#create ConsulCluster#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#default ConsulCluster#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#delete ConsulCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#update ConsulCluster#update}.
        '''
        value = ConsulClusterTimeouts(
            create=create, default=default, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutoHvnToHvnPeering")
    def reset_auto_hvn_to_hvn_peering(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoHvnToHvnPeering", []))

    @jsii.member(jsii_name="resetConnectEnabled")
    def reset_connect_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectEnabled", []))

    @jsii.member(jsii_name="resetDatacenter")
    def reset_datacenter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatacenter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMinConsulVersion")
    def reset_min_consul_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinConsulVersion", []))

    @jsii.member(jsii_name="resetPrimaryLink")
    def reset_primary_link(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryLink", []))

    @jsii.member(jsii_name="resetPublicEndpoint")
    def reset_public_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicEndpoint", []))

    @jsii.member(jsii_name="resetSize")
    def reset_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSize", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cloudProvider")
    def cloud_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudProvider"))

    @builtins.property
    @jsii.member(jsii_name="consulAutomaticUpgrades")
    def consul_automatic_upgrades(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "consulAutomaticUpgrades"))

    @builtins.property
    @jsii.member(jsii_name="consulCaFile")
    def consul_ca_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulCaFile"))

    @builtins.property
    @jsii.member(jsii_name="consulConfigFile")
    def consul_config_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulConfigFile"))

    @builtins.property
    @jsii.member(jsii_name="consulPrivateEndpointUrl")
    def consul_private_endpoint_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulPrivateEndpointUrl"))

    @builtins.property
    @jsii.member(jsii_name="consulPublicEndpointUrl")
    def consul_public_endpoint_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulPublicEndpointUrl"))

    @builtins.property
    @jsii.member(jsii_name="consulRootTokenAccessorId")
    def consul_root_token_accessor_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulRootTokenAccessorId"))

    @builtins.property
    @jsii.member(jsii_name="consulRootTokenSecretId")
    def consul_root_token_secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulRootTokenSecretId"))

    @builtins.property
    @jsii.member(jsii_name="consulSnapshotInterval")
    def consul_snapshot_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulSnapshotInterval"))

    @builtins.property
    @jsii.member(jsii_name="consulSnapshotRetention")
    def consul_snapshot_retention(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulSnapshotRetention"))

    @builtins.property
    @jsii.member(jsii_name="consulVersion")
    def consul_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulVersion"))

    @builtins.property
    @jsii.member(jsii_name="organizationId")
    def organization_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationId"))

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="scale")
    def scale(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scale"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ConsulClusterTimeoutsOutputReference":
        return typing.cast("ConsulClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="autoHvnToHvnPeeringInput")
    def auto_hvn_to_hvn_peering_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoHvnToHvnPeeringInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="connectEnabledInput")
    def connect_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "connectEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterInput")
    def datacenter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterInput"))

    @builtins.property
    @jsii.member(jsii_name="hvnIdInput")
    def hvn_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hvnIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="minConsulVersionInput")
    def min_consul_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minConsulVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryLinkInput")
    def primary_link_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="publicEndpointInput")
    def public_endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="tierInput")
    def tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tierInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ConsulClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ConsulClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoHvnToHvnPeering")
    def auto_hvn_to_hvn_peering(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoHvnToHvnPeering"))

    @auto_hvn_to_hvn_peering.setter
    def auto_hvn_to_hvn_peering(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulCluster, "auto_hvn_to_hvn_peering").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHvnToHvnPeering", value)

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulCluster, "cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="connectEnabled")
    def connect_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "connectEnabled"))

    @connect_enabled.setter
    def connect_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulCluster, "connect_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="datacenter")
    def datacenter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenter"))

    @datacenter.setter
    def datacenter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulCluster, "datacenter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenter", value)

    @builtins.property
    @jsii.member(jsii_name="hvnId")
    def hvn_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hvnId"))

    @hvn_id.setter
    def hvn_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulCluster, "hvn_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hvnId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="minConsulVersion")
    def min_consul_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minConsulVersion"))

    @min_consul_version.setter
    def min_consul_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulCluster, "min_consul_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minConsulVersion", value)

    @builtins.property
    @jsii.member(jsii_name="primaryLink")
    def primary_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryLink"))

    @primary_link.setter
    def primary_link(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulCluster, "primary_link").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryLink", value)

    @builtins.property
    @jsii.member(jsii_name="publicEndpoint")
    def public_endpoint(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publicEndpoint"))

    @public_endpoint.setter
    def public_endpoint(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulCluster, "public_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulCluster, "size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulCluster, "tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.consulCluster.ConsulClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_id": "clusterId",
        "hvn_id": "hvnId",
        "tier": "tier",
        "auto_hvn_to_hvn_peering": "autoHvnToHvnPeering",
        "connect_enabled": "connectEnabled",
        "datacenter": "datacenter",
        "id": "id",
        "min_consul_version": "minConsulVersion",
        "primary_link": "primaryLink",
        "public_endpoint": "publicEndpoint",
        "size": "size",
        "timeouts": "timeouts",
    },
)
class ConsulClusterConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        cluster_id: builtins.str,
        hvn_id: builtins.str,
        tier: builtins.str,
        auto_hvn_to_hvn_peering: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connect_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        datacenter: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        min_consul_version: typing.Optional[builtins.str] = None,
        primary_link: typing.Optional[builtins.str] = None,
        public_endpoint: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        size: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ConsulClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster_id: The ID of the HCP Consul cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#cluster_id ConsulCluster#cluster_id}
        :param hvn_id: The ID of the HVN this HCP Consul cluster is associated to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#hvn_id ConsulCluster#hvn_id}
        :param tier: The tier that the HCP Consul cluster will be provisioned as. Only ``development``, ``standard`` and ``plus`` are available at this time. See `pricing information <https://cloud.hashicorp.com/pricing/consul>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#tier ConsulCluster#tier}
        :param auto_hvn_to_hvn_peering: Enables automatic HVN to HVN peering when creating a secondary cluster in a federation. The alternative to using the auto-accept feature is to create an ```hcp_hvn_peering_connection`` <hvn_peering_connection.md>`_ resource that explicitly defines the HVN resources that are allowed to communicate with each other. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#auto_hvn_to_hvn_peering ConsulCluster#auto_hvn_to_hvn_peering}
        :param connect_enabled: Denotes the Consul connect feature should be enabled for this cluster. Default to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#connect_enabled ConsulCluster#connect_enabled}
        :param datacenter: The Consul data center name of the cluster. If not specified, it is defaulted to the value of ``cluster_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#datacenter ConsulCluster#datacenter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#id ConsulCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param min_consul_version: The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently recommended by HCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#min_consul_version ConsulCluster#min_consul_version}
        :param primary_link: The ``self_link`` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If not specified, it is a standalone cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#primary_link ConsulCluster#primary_link}
        :param public_endpoint: Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#public_endpoint ConsulCluster#public_endpoint}
        :param size: The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for development tier - ``x_small``. Valid options for other tiers - ``small``, ``medium``, ``large``. For more details - https://cloud.hashicorp.com/pricing/consul. Upgrading the size of a cluster after creation is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#size ConsulCluster#size}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#timeouts ConsulCluster#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ConsulClusterTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ConsulClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument hvn_id", value=hvn_id, expected_type=type_hints["hvn_id"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument auto_hvn_to_hvn_peering", value=auto_hvn_to_hvn_peering, expected_type=type_hints["auto_hvn_to_hvn_peering"])
            check_type(argname="argument connect_enabled", value=connect_enabled, expected_type=type_hints["connect_enabled"])
            check_type(argname="argument datacenter", value=datacenter, expected_type=type_hints["datacenter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument min_consul_version", value=min_consul_version, expected_type=type_hints["min_consul_version"])
            check_type(argname="argument primary_link", value=primary_link, expected_type=type_hints["primary_link"])
            check_type(argname="argument public_endpoint", value=public_endpoint, expected_type=type_hints["public_endpoint"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_id": cluster_id,
            "hvn_id": hvn_id,
            "tier": tier,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if auto_hvn_to_hvn_peering is not None:
            self._values["auto_hvn_to_hvn_peering"] = auto_hvn_to_hvn_peering
        if connect_enabled is not None:
            self._values["connect_enabled"] = connect_enabled
        if datacenter is not None:
            self._values["datacenter"] = datacenter
        if id is not None:
            self._values["id"] = id
        if min_consul_version is not None:
            self._values["min_consul_version"] = min_consul_version
        if primary_link is not None:
            self._values["primary_link"] = primary_link
        if public_endpoint is not None:
            self._values["public_endpoint"] = public_endpoint
        if size is not None:
            self._values["size"] = size
        if timeouts is not None:
            self._values["timeouts"] = timeouts

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def cluster_id(self) -> builtins.str:
        '''The ID of the HCP Consul cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#cluster_id ConsulCluster#cluster_id}
        '''
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hvn_id(self) -> builtins.str:
        '''The ID of the HVN this HCP Consul cluster is associated to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#hvn_id ConsulCluster#hvn_id}
        '''
        result = self._values.get("hvn_id")
        assert result is not None, "Required property 'hvn_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tier(self) -> builtins.str:
        '''The tier that the HCP Consul cluster will be provisioned as.

        Only ``development``, ``standard`` and ``plus`` are available at this time. See `pricing information <https://cloud.hashicorp.com/pricing/consul>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#tier ConsulCluster#tier}
        '''
        result = self._values.get("tier")
        assert result is not None, "Required property 'tier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_hvn_to_hvn_peering(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enables automatic HVN to HVN peering when creating a secondary cluster in a federation.

        The alternative to using the auto-accept feature is to create an ```hcp_hvn_peering_connection`` <hvn_peering_connection.md>`_ resource that explicitly defines the HVN resources that are allowed to communicate with each other.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#auto_hvn_to_hvn_peering ConsulCluster#auto_hvn_to_hvn_peering}
        '''
        result = self._values.get("auto_hvn_to_hvn_peering")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def connect_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Denotes the Consul connect feature should be enabled for this cluster.  Default to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#connect_enabled ConsulCluster#connect_enabled}
        '''
        result = self._values.get("connect_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def datacenter(self) -> typing.Optional[builtins.str]:
        '''The Consul data center name of the cluster. If not specified, it is defaulted to the value of ``cluster_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#datacenter ConsulCluster#datacenter}
        '''
        result = self._values.get("datacenter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#id ConsulCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_consul_version(self) -> typing.Optional[builtins.str]:
        '''The minimum Consul version of the cluster.

        If not specified, it is defaulted to the version that is currently recommended by HCP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#min_consul_version ConsulCluster#min_consul_version}
        '''
        result = self._values.get("min_consul_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_link(self) -> typing.Optional[builtins.str]:
        '''The ``self_link`` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster.

        If not specified, it is a standalone cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#primary_link ConsulCluster#primary_link}
        '''
        result = self._values.get("primary_link")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#public_endpoint ConsulCluster#public_endpoint}
        '''
        result = self._values.get("public_endpoint")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def size(self) -> typing.Optional[builtins.str]:
        '''The t-shirt size representation of each server VM that this Consul cluster is provisioned with.

        Valid option for development tier - ``x_small``. Valid options for other tiers - ``small``, ``medium``, ``large``. For more details - https://cloud.hashicorp.com/pricing/consul. Upgrading the size of a cluster after creation is allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#size ConsulCluster#size}
        '''
        result = self._values.get("size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ConsulClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#timeouts ConsulCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ConsulClusterTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsulClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.consulCluster.ConsulClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "default": "default",
        "delete": "delete",
        "update": "update",
    },
)
class ConsulClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#create ConsulCluster#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#default ConsulCluster#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#delete ConsulCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#update ConsulCluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsulClusterTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if default is not None:
            self._values["default"] = default
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#create ConsulCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#default ConsulCluster#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#delete ConsulCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/consul_cluster#update ConsulCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsulClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConsulClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.consulCluster.ConsulClusterTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsulClusterTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulClusterTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulClusterTimeoutsOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulClusterTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulClusterTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ConsulClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ConsulClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ConsulClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulClusterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ConsulCluster",
    "ConsulClusterConfig",
    "ConsulClusterTimeouts",
    "ConsulClusterTimeoutsOutputReference",
]

publication.publish()
