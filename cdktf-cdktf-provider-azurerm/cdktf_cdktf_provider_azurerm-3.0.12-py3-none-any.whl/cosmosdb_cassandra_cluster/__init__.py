'''
# `azurerm_cosmosdb_cassandra_cluster`

Refer to the Terraform Registory for docs: [`azurerm_cosmosdb_cassandra_cluster`](https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster).
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


class CosmosdbCassandraCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbCassandraCluster.CosmosdbCassandraCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster azurerm_cosmosdb_cassandra_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        default_admin_password: builtins.str,
        delegated_management_subnet_id: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        authentication_method: typing.Optional[builtins.str] = None,
        client_certificate_pems: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_gossip_certificate_pems: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_seed_node_ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        hours_between_backups: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["CosmosdbCassandraClusterIdentity", typing.Dict[str, typing.Any]]] = None,
        repair_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["CosmosdbCassandraClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster azurerm_cosmosdb_cassandra_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#default_admin_password CosmosdbCassandraCluster#default_admin_password}.
        :param delegated_management_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#delegated_management_subnet_id CosmosdbCassandraCluster#delegated_management_subnet_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#location CosmosdbCassandraCluster#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#name CosmosdbCassandraCluster#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#resource_group_name CosmosdbCassandraCluster#resource_group_name}.
        :param authentication_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#authentication_method CosmosdbCassandraCluster#authentication_method}.
        :param client_certificate_pems: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#client_certificate_pems CosmosdbCassandraCluster#client_certificate_pems}.
        :param external_gossip_certificate_pems: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#external_gossip_certificate_pems CosmosdbCassandraCluster#external_gossip_certificate_pems}.
        :param external_seed_node_ip_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#external_seed_node_ip_addresses CosmosdbCassandraCluster#external_seed_node_ip_addresses}.
        :param hours_between_backups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#hours_between_backups CosmosdbCassandraCluster#hours_between_backups}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#id CosmosdbCassandraCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#identity CosmosdbCassandraCluster#identity}
        :param repair_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#repair_enabled CosmosdbCassandraCluster#repair_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#tags CosmosdbCassandraCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#timeouts CosmosdbCassandraCluster#timeouts}
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#version CosmosdbCassandraCluster#version}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbCassandraCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CosmosdbCassandraClusterConfig(
            default_admin_password=default_admin_password,
            delegated_management_subnet_id=delegated_management_subnet_id,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            authentication_method=authentication_method,
            client_certificate_pems=client_certificate_pems,
            external_gossip_certificate_pems=external_gossip_certificate_pems,
            external_seed_node_ip_addresses=external_seed_node_ip_addresses,
            hours_between_backups=hours_between_backups,
            id=id,
            identity=identity,
            repair_enabled=repair_enabled,
            tags=tags,
            timeouts=timeouts,
            version=version,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putIdentity")
    def put_identity(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#type CosmosdbCassandraCluster#type}.
        '''
        value = CosmosdbCassandraClusterIdentity(type=type)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#create CosmosdbCassandraCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#delete CosmosdbCassandraCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#read CosmosdbCassandraCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#update CosmosdbCassandraCluster#update}.
        '''
        value = CosmosdbCassandraClusterTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAuthenticationMethod")
    def reset_authentication_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationMethod", []))

    @jsii.member(jsii_name="resetClientCertificatePems")
    def reset_client_certificate_pems(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificatePems", []))

    @jsii.member(jsii_name="resetExternalGossipCertificatePems")
    def reset_external_gossip_certificate_pems(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalGossipCertificatePems", []))

    @jsii.member(jsii_name="resetExternalSeedNodeIpAddresses")
    def reset_external_seed_node_ip_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalSeedNodeIpAddresses", []))

    @jsii.member(jsii_name="resetHoursBetweenBackups")
    def reset_hours_between_backups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHoursBetweenBackups", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetRepairEnabled")
    def reset_repair_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepairEnabled", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "CosmosdbCassandraClusterIdentityOutputReference":
        return typing.cast("CosmosdbCassandraClusterIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CosmosdbCassandraClusterTimeoutsOutputReference":
        return typing.cast("CosmosdbCassandraClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="authenticationMethodInput")
    def authentication_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificatePemsInput")
    def client_certificate_pems_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clientCertificatePemsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultAdminPasswordInput")
    def default_admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultAdminPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="delegatedManagementSubnetIdInput")
    def delegated_management_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "delegatedManagementSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="externalGossipCertificatePemsInput")
    def external_gossip_certificate_pems_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "externalGossipCertificatePemsInput"))

    @builtins.property
    @jsii.member(jsii_name="externalSeedNodeIpAddressesInput")
    def external_seed_node_ip_addresses_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "externalSeedNodeIpAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="hoursBetweenBackupsInput")
    def hours_between_backups_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hoursBetweenBackupsInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["CosmosdbCassandraClusterIdentity"]:
        return typing.cast(typing.Optional["CosmosdbCassandraClusterIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="repairEnabledInput")
    def repair_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "repairEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["CosmosdbCassandraClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["CosmosdbCassandraClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationMethod")
    def authentication_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationMethod"))

    @authentication_method.setter
    def authentication_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraCluster, "authentication_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificatePems")
    def client_certificate_pems(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "clientCertificatePems"))

    @client_certificate_pems.setter
    def client_certificate_pems(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraCluster, "client_certificate_pems").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificatePems", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAdminPassword")
    def default_admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultAdminPassword"))

    @default_admin_password.setter
    def default_admin_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraCluster, "default_admin_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAdminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="delegatedManagementSubnetId")
    def delegated_management_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delegatedManagementSubnetId"))

    @delegated_management_subnet_id.setter
    def delegated_management_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraCluster, "delegated_management_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delegatedManagementSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="externalGossipCertificatePems")
    def external_gossip_certificate_pems(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "externalGossipCertificatePems"))

    @external_gossip_certificate_pems.setter
    def external_gossip_certificate_pems(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraCluster, "external_gossip_certificate_pems").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalGossipCertificatePems", value)

    @builtins.property
    @jsii.member(jsii_name="externalSeedNodeIpAddresses")
    def external_seed_node_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "externalSeedNodeIpAddresses"))

    @external_seed_node_ip_addresses.setter
    def external_seed_node_ip_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraCluster, "external_seed_node_ip_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalSeedNodeIpAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="hoursBetweenBackups")
    def hours_between_backups(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hoursBetweenBackups"))

    @hours_between_backups.setter
    def hours_between_backups(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraCluster, "hours_between_backups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hoursBetweenBackups", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraCluster, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraCluster, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="repairEnabled")
    def repair_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "repairEnabled"))

    @repair_enabled.setter
    def repair_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraCluster, "repair_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repairEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraCluster, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraCluster, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraCluster, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbCassandraCluster.CosmosdbCassandraClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "default_admin_password": "defaultAdminPassword",
        "delegated_management_subnet_id": "delegatedManagementSubnetId",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "authentication_method": "authenticationMethod",
        "client_certificate_pems": "clientCertificatePems",
        "external_gossip_certificate_pems": "externalGossipCertificatePems",
        "external_seed_node_ip_addresses": "externalSeedNodeIpAddresses",
        "hours_between_backups": "hoursBetweenBackups",
        "id": "id",
        "identity": "identity",
        "repair_enabled": "repairEnabled",
        "tags": "tags",
        "timeouts": "timeouts",
        "version": "version",
    },
)
class CosmosdbCassandraClusterConfig(cdktf.TerraformMetaArguments):
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
        default_admin_password: builtins.str,
        delegated_management_subnet_id: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        authentication_method: typing.Optional[builtins.str] = None,
        client_certificate_pems: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_gossip_certificate_pems: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_seed_node_ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        hours_between_backups: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["CosmosdbCassandraClusterIdentity", typing.Dict[str, typing.Any]]] = None,
        repair_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["CosmosdbCassandraClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param default_admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#default_admin_password CosmosdbCassandraCluster#default_admin_password}.
        :param delegated_management_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#delegated_management_subnet_id CosmosdbCassandraCluster#delegated_management_subnet_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#location CosmosdbCassandraCluster#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#name CosmosdbCassandraCluster#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#resource_group_name CosmosdbCassandraCluster#resource_group_name}.
        :param authentication_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#authentication_method CosmosdbCassandraCluster#authentication_method}.
        :param client_certificate_pems: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#client_certificate_pems CosmosdbCassandraCluster#client_certificate_pems}.
        :param external_gossip_certificate_pems: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#external_gossip_certificate_pems CosmosdbCassandraCluster#external_gossip_certificate_pems}.
        :param external_seed_node_ip_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#external_seed_node_ip_addresses CosmosdbCassandraCluster#external_seed_node_ip_addresses}.
        :param hours_between_backups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#hours_between_backups CosmosdbCassandraCluster#hours_between_backups}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#id CosmosdbCassandraCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#identity CosmosdbCassandraCluster#identity}
        :param repair_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#repair_enabled CosmosdbCassandraCluster#repair_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#tags CosmosdbCassandraCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#timeouts CosmosdbCassandraCluster#timeouts}
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#version CosmosdbCassandraCluster#version}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(identity, dict):
            identity = CosmosdbCassandraClusterIdentity(**identity)
        if isinstance(timeouts, dict):
            timeouts = CosmosdbCassandraClusterTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbCassandraClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument default_admin_password", value=default_admin_password, expected_type=type_hints["default_admin_password"])
            check_type(argname="argument delegated_management_subnet_id", value=delegated_management_subnet_id, expected_type=type_hints["delegated_management_subnet_id"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument authentication_method", value=authentication_method, expected_type=type_hints["authentication_method"])
            check_type(argname="argument client_certificate_pems", value=client_certificate_pems, expected_type=type_hints["client_certificate_pems"])
            check_type(argname="argument external_gossip_certificate_pems", value=external_gossip_certificate_pems, expected_type=type_hints["external_gossip_certificate_pems"])
            check_type(argname="argument external_seed_node_ip_addresses", value=external_seed_node_ip_addresses, expected_type=type_hints["external_seed_node_ip_addresses"])
            check_type(argname="argument hours_between_backups", value=hours_between_backups, expected_type=type_hints["hours_between_backups"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument repair_enabled", value=repair_enabled, expected_type=type_hints["repair_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_admin_password": default_admin_password,
            "delegated_management_subnet_id": delegated_management_subnet_id,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
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
        if authentication_method is not None:
            self._values["authentication_method"] = authentication_method
        if client_certificate_pems is not None:
            self._values["client_certificate_pems"] = client_certificate_pems
        if external_gossip_certificate_pems is not None:
            self._values["external_gossip_certificate_pems"] = external_gossip_certificate_pems
        if external_seed_node_ip_addresses is not None:
            self._values["external_seed_node_ip_addresses"] = external_seed_node_ip_addresses
        if hours_between_backups is not None:
            self._values["hours_between_backups"] = hours_between_backups
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if repair_enabled is not None:
            self._values["repair_enabled"] = repair_enabled
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if version is not None:
            self._values["version"] = version

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
    def default_admin_password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#default_admin_password CosmosdbCassandraCluster#default_admin_password}.'''
        result = self._values.get("default_admin_password")
        assert result is not None, "Required property 'default_admin_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delegated_management_subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#delegated_management_subnet_id CosmosdbCassandraCluster#delegated_management_subnet_id}.'''
        result = self._values.get("delegated_management_subnet_id")
        assert result is not None, "Required property 'delegated_management_subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#location CosmosdbCassandraCluster#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#name CosmosdbCassandraCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#resource_group_name CosmosdbCassandraCluster#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authentication_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#authentication_method CosmosdbCassandraCluster#authentication_method}.'''
        result = self._values.get("authentication_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate_pems(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#client_certificate_pems CosmosdbCassandraCluster#client_certificate_pems}.'''
        result = self._values.get("client_certificate_pems")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def external_gossip_certificate_pems(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#external_gossip_certificate_pems CosmosdbCassandraCluster#external_gossip_certificate_pems}.'''
        result = self._values.get("external_gossip_certificate_pems")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def external_seed_node_ip_addresses(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#external_seed_node_ip_addresses CosmosdbCassandraCluster#external_seed_node_ip_addresses}.'''
        result = self._values.get("external_seed_node_ip_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def hours_between_backups(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#hours_between_backups CosmosdbCassandraCluster#hours_between_backups}.'''
        result = self._values.get("hours_between_backups")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#id CosmosdbCassandraCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["CosmosdbCassandraClusterIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#identity CosmosdbCassandraCluster#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["CosmosdbCassandraClusterIdentity"], result)

    @builtins.property
    def repair_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#repair_enabled CosmosdbCassandraCluster#repair_enabled}.'''
        result = self._values.get("repair_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#tags CosmosdbCassandraCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CosmosdbCassandraClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#timeouts CosmosdbCassandraCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CosmosdbCassandraClusterTimeouts"], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#version CosmosdbCassandraCluster#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbCassandraClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbCassandraCluster.CosmosdbCassandraClusterIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CosmosdbCassandraClusterIdentity:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#type CosmosdbCassandraCluster#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbCassandraClusterIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#type CosmosdbCassandraCluster#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbCassandraClusterIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbCassandraClusterIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbCassandraCluster.CosmosdbCassandraClusterIdentityOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbCassandraClusterIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraClusterIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CosmosdbCassandraClusterIdentity]:
        return typing.cast(typing.Optional[CosmosdbCassandraClusterIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CosmosdbCassandraClusterIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraClusterIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbCassandraCluster.CosmosdbCassandraClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class CosmosdbCassandraClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#create CosmosdbCassandraCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#delete CosmosdbCassandraCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#read CosmosdbCassandraCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#update CosmosdbCassandraCluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbCassandraClusterTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#create CosmosdbCassandraCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#delete CosmosdbCassandraCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#read CosmosdbCassandraCluster#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_cassandra_cluster#update CosmosdbCassandraCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbCassandraClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbCassandraClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbCassandraCluster.CosmosdbCassandraClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbCassandraClusterTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

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
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraClusterTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraClusterTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraClusterTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraClusterTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CosmosdbCassandraClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CosmosdbCassandraClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CosmosdbCassandraClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbCassandraClusterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CosmosdbCassandraCluster",
    "CosmosdbCassandraClusterConfig",
    "CosmosdbCassandraClusterIdentity",
    "CosmosdbCassandraClusterIdentityOutputReference",
    "CosmosdbCassandraClusterTimeouts",
    "CosmosdbCassandraClusterTimeoutsOutputReference",
]

publication.publish()
