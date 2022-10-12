'''
# `azurerm_hdinsight_spark_cluster`

Refer to the Terraform Registory for docs: [`azurerm_hdinsight_spark_cluster`](https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster).
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


class HdinsightSparkCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster azurerm_hdinsight_spark_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cluster_version: builtins.str,
        component_version: typing.Union["HdinsightSparkClusterComponentVersion", typing.Dict[str, typing.Any]],
        gateway: typing.Union["HdinsightSparkClusterGateway", typing.Dict[str, typing.Any]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        roles: typing.Union["HdinsightSparkClusterRoles", typing.Dict[str, typing.Any]],
        tier: builtins.str,
        disk_encryption: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HdinsightSparkClusterDiskEncryption", typing.Dict[str, typing.Any]]]]] = None,
        encryption_in_transit_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        extension: typing.Optional[typing.Union["HdinsightSparkClusterExtension", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        metastores: typing.Optional[typing.Union["HdinsightSparkClusterMetastores", typing.Dict[str, typing.Any]]] = None,
        monitor: typing.Optional[typing.Union["HdinsightSparkClusterMonitor", typing.Dict[str, typing.Any]]] = None,
        network: typing.Optional[typing.Union["HdinsightSparkClusterNetwork", typing.Dict[str, typing.Any]]] = None,
        security_profile: typing.Optional[typing.Union["HdinsightSparkClusterSecurityProfile", typing.Dict[str, typing.Any]]] = None,
        storage_account: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HdinsightSparkClusterStorageAccount", typing.Dict[str, typing.Any]]]]] = None,
        storage_account_gen2: typing.Optional[typing.Union["HdinsightSparkClusterStorageAccountGen2", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["HdinsightSparkClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        tls_min_version: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster azurerm_hdinsight_spark_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#cluster_version HdinsightSparkCluster#cluster_version}.
        :param component_version: component_version block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#component_version HdinsightSparkCluster#component_version}
        :param gateway: gateway block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#gateway HdinsightSparkCluster#gateway}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#location HdinsightSparkCluster#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#name HdinsightSparkCluster#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#resource_group_name HdinsightSparkCluster#resource_group_name}.
        :param roles: roles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#roles HdinsightSparkCluster#roles}
        :param tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#tier HdinsightSparkCluster#tier}.
        :param disk_encryption: disk_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#disk_encryption HdinsightSparkCluster#disk_encryption}
        :param encryption_in_transit_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#encryption_in_transit_enabled HdinsightSparkCluster#encryption_in_transit_enabled}.
        :param extension: extension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#extension HdinsightSparkCluster#extension}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#id HdinsightSparkCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metastores: metastores block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#metastores HdinsightSparkCluster#metastores}
        :param monitor: monitor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#monitor HdinsightSparkCluster#monitor}
        :param network: network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#network HdinsightSparkCluster#network}
        :param security_profile: security_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#security_profile HdinsightSparkCluster#security_profile}
        :param storage_account: storage_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#storage_account HdinsightSparkCluster#storage_account}
        :param storage_account_gen2: storage_account_gen2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#storage_account_gen2 HdinsightSparkCluster#storage_account_gen2}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#tags HdinsightSparkCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#timeouts HdinsightSparkCluster#timeouts}
        :param tls_min_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#tls_min_version HdinsightSparkCluster#tls_min_version}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = HdinsightSparkClusterConfig(
            cluster_version=cluster_version,
            component_version=component_version,
            gateway=gateway,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            roles=roles,
            tier=tier,
            disk_encryption=disk_encryption,
            encryption_in_transit_enabled=encryption_in_transit_enabled,
            extension=extension,
            id=id,
            metastores=metastores,
            monitor=monitor,
            network=network,
            security_profile=security_profile,
            storage_account=storage_account,
            storage_account_gen2=storage_account_gen2,
            tags=tags,
            timeouts=timeouts,
            tls_min_version=tls_min_version,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putComponentVersion")
    def put_component_version(self, *, spark: builtins.str) -> None:
        '''
        :param spark: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#spark HdinsightSparkCluster#spark}.
        '''
        value = HdinsightSparkClusterComponentVersion(spark=spark)

        return typing.cast(None, jsii.invoke(self, "putComponentVersion", [value]))

    @jsii.member(jsii_name="putDiskEncryption")
    def put_disk_encryption(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HdinsightSparkClusterDiskEncryption", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkCluster.put_disk_encryption)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDiskEncryption", [value]))

    @jsii.member(jsii_name="putExtension")
    def put_extension(
        self,
        *,
        log_analytics_workspace_id: builtins.str,
        primary_key: builtins.str,
    ) -> None:
        '''
        :param log_analytics_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#log_analytics_workspace_id HdinsightSparkCluster#log_analytics_workspace_id}.
        :param primary_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#primary_key HdinsightSparkCluster#primary_key}.
        '''
        value = HdinsightSparkClusterExtension(
            log_analytics_workspace_id=log_analytics_workspace_id,
            primary_key=primary_key,
        )

        return typing.cast(None, jsii.invoke(self, "putExtension", [value]))

    @jsii.member(jsii_name="putGateway")
    def put_gateway(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.
        '''
        value = HdinsightSparkClusterGateway(password=password, username=username)

        return typing.cast(None, jsii.invoke(self, "putGateway", [value]))

    @jsii.member(jsii_name="putMetastores")
    def put_metastores(
        self,
        *,
        ambari: typing.Optional[typing.Union["HdinsightSparkClusterMetastoresAmbari", typing.Dict[str, typing.Any]]] = None,
        hive: typing.Optional[typing.Union["HdinsightSparkClusterMetastoresHive", typing.Dict[str, typing.Any]]] = None,
        oozie: typing.Optional[typing.Union["HdinsightSparkClusterMetastoresOozie", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ambari: ambari block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#ambari HdinsightSparkCluster#ambari}
        :param hive: hive block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#hive HdinsightSparkCluster#hive}
        :param oozie: oozie block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#oozie HdinsightSparkCluster#oozie}
        '''
        value = HdinsightSparkClusterMetastores(ambari=ambari, hive=hive, oozie=oozie)

        return typing.cast(None, jsii.invoke(self, "putMetastores", [value]))

    @jsii.member(jsii_name="putMonitor")
    def put_monitor(
        self,
        *,
        log_analytics_workspace_id: builtins.str,
        primary_key: builtins.str,
    ) -> None:
        '''
        :param log_analytics_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#log_analytics_workspace_id HdinsightSparkCluster#log_analytics_workspace_id}.
        :param primary_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#primary_key HdinsightSparkCluster#primary_key}.
        '''
        value = HdinsightSparkClusterMonitor(
            log_analytics_workspace_id=log_analytics_workspace_id,
            primary_key=primary_key,
        )

        return typing.cast(None, jsii.invoke(self, "putMonitor", [value]))

    @jsii.member(jsii_name="putNetwork")
    def put_network(
        self,
        *,
        connection_direction: typing.Optional[builtins.str] = None,
        private_link_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection_direction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#connection_direction HdinsightSparkCluster#connection_direction}.
        :param private_link_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#private_link_enabled HdinsightSparkCluster#private_link_enabled}.
        '''
        value = HdinsightSparkClusterNetwork(
            connection_direction=connection_direction,
            private_link_enabled=private_link_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putNetwork", [value]))

    @jsii.member(jsii_name="putRoles")
    def put_roles(
        self,
        *,
        head_node: typing.Union["HdinsightSparkClusterRolesHeadNode", typing.Dict[str, typing.Any]],
        worker_node: typing.Union["HdinsightSparkClusterRolesWorkerNode", typing.Dict[str, typing.Any]],
        zookeeper_node: typing.Union["HdinsightSparkClusterRolesZookeeperNode", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param head_node: head_node block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#head_node HdinsightSparkCluster#head_node}
        :param worker_node: worker_node block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#worker_node HdinsightSparkCluster#worker_node}
        :param zookeeper_node: zookeeper_node block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#zookeeper_node HdinsightSparkCluster#zookeeper_node}
        '''
        value = HdinsightSparkClusterRoles(
            head_node=head_node, worker_node=worker_node, zookeeper_node=zookeeper_node
        )

        return typing.cast(None, jsii.invoke(self, "putRoles", [value]))

    @jsii.member(jsii_name="putSecurityProfile")
    def put_security_profile(
        self,
        *,
        aadds_resource_id: builtins.str,
        domain_name: builtins.str,
        domain_username: builtins.str,
        domain_user_password: builtins.str,
        ldaps_urls: typing.Sequence[builtins.str],
        msi_resource_id: builtins.str,
        cluster_users_group_dns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param aadds_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#aadds_resource_id HdinsightSparkCluster#aadds_resource_id}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#domain_name HdinsightSparkCluster#domain_name}.
        :param domain_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#domain_username HdinsightSparkCluster#domain_username}.
        :param domain_user_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#domain_user_password HdinsightSparkCluster#domain_user_password}.
        :param ldaps_urls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#ldaps_urls HdinsightSparkCluster#ldaps_urls}.
        :param msi_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#msi_resource_id HdinsightSparkCluster#msi_resource_id}.
        :param cluster_users_group_dns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#cluster_users_group_dns HdinsightSparkCluster#cluster_users_group_dns}.
        '''
        value = HdinsightSparkClusterSecurityProfile(
            aadds_resource_id=aadds_resource_id,
            domain_name=domain_name,
            domain_username=domain_username,
            domain_user_password=domain_user_password,
            ldaps_urls=ldaps_urls,
            msi_resource_id=msi_resource_id,
            cluster_users_group_dns=cluster_users_group_dns,
        )

        return typing.cast(None, jsii.invoke(self, "putSecurityProfile", [value]))

    @jsii.member(jsii_name="putStorageAccount")
    def put_storage_account(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HdinsightSparkClusterStorageAccount", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkCluster.put_storage_account)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStorageAccount", [value]))

    @jsii.member(jsii_name="putStorageAccountGen2")
    def put_storage_account_gen2(
        self,
        *,
        filesystem_id: builtins.str,
        is_default: typing.Union[builtins.bool, cdktf.IResolvable],
        managed_identity_resource_id: builtins.str,
        storage_resource_id: builtins.str,
    ) -> None:
        '''
        :param filesystem_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#filesystem_id HdinsightSparkCluster#filesystem_id}.
        :param is_default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#is_default HdinsightSparkCluster#is_default}.
        :param managed_identity_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#managed_identity_resource_id HdinsightSparkCluster#managed_identity_resource_id}.
        :param storage_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#storage_resource_id HdinsightSparkCluster#storage_resource_id}.
        '''
        value = HdinsightSparkClusterStorageAccountGen2(
            filesystem_id=filesystem_id,
            is_default=is_default,
            managed_identity_resource_id=managed_identity_resource_id,
            storage_resource_id=storage_resource_id,
        )

        return typing.cast(None, jsii.invoke(self, "putStorageAccountGen2", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#create HdinsightSparkCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#delete HdinsightSparkCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#read HdinsightSparkCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#update HdinsightSparkCluster#update}.
        '''
        value = HdinsightSparkClusterTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDiskEncryption")
    def reset_disk_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryption", []))

    @jsii.member(jsii_name="resetEncryptionInTransitEnabled")
    def reset_encryption_in_transit_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionInTransitEnabled", []))

    @jsii.member(jsii_name="resetExtension")
    def reset_extension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtension", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMetastores")
    def reset_metastores(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetastores", []))

    @jsii.member(jsii_name="resetMonitor")
    def reset_monitor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitor", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetSecurityProfile")
    def reset_security_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityProfile", []))

    @jsii.member(jsii_name="resetStorageAccount")
    def reset_storage_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccount", []))

    @jsii.member(jsii_name="resetStorageAccountGen2")
    def reset_storage_account_gen2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountGen2", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTlsMinVersion")
    def reset_tls_min_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsMinVersion", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="componentVersion")
    def component_version(
        self,
    ) -> "HdinsightSparkClusterComponentVersionOutputReference":
        return typing.cast("HdinsightSparkClusterComponentVersionOutputReference", jsii.get(self, "componentVersion"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryption")
    def disk_encryption(self) -> "HdinsightSparkClusterDiskEncryptionList":
        return typing.cast("HdinsightSparkClusterDiskEncryptionList", jsii.get(self, "diskEncryption"))

    @builtins.property
    @jsii.member(jsii_name="extension")
    def extension(self) -> "HdinsightSparkClusterExtensionOutputReference":
        return typing.cast("HdinsightSparkClusterExtensionOutputReference", jsii.get(self, "extension"))

    @builtins.property
    @jsii.member(jsii_name="gateway")
    def gateway(self) -> "HdinsightSparkClusterGatewayOutputReference":
        return typing.cast("HdinsightSparkClusterGatewayOutputReference", jsii.get(self, "gateway"))

    @builtins.property
    @jsii.member(jsii_name="httpsEndpoint")
    def https_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpsEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="metastores")
    def metastores(self) -> "HdinsightSparkClusterMetastoresOutputReference":
        return typing.cast("HdinsightSparkClusterMetastoresOutputReference", jsii.get(self, "metastores"))

    @builtins.property
    @jsii.member(jsii_name="monitor")
    def monitor(self) -> "HdinsightSparkClusterMonitorOutputReference":
        return typing.cast("HdinsightSparkClusterMonitorOutputReference", jsii.get(self, "monitor"))

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> "HdinsightSparkClusterNetworkOutputReference":
        return typing.cast("HdinsightSparkClusterNetworkOutputReference", jsii.get(self, "network"))

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(self) -> "HdinsightSparkClusterRolesOutputReference":
        return typing.cast("HdinsightSparkClusterRolesOutputReference", jsii.get(self, "roles"))

    @builtins.property
    @jsii.member(jsii_name="securityProfile")
    def security_profile(self) -> "HdinsightSparkClusterSecurityProfileOutputReference":
        return typing.cast("HdinsightSparkClusterSecurityProfileOutputReference", jsii.get(self, "securityProfile"))

    @builtins.property
    @jsii.member(jsii_name="sshEndpoint")
    def ssh_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="storageAccount")
    def storage_account(self) -> "HdinsightSparkClusterStorageAccountList":
        return typing.cast("HdinsightSparkClusterStorageAccountList", jsii.get(self, "storageAccount"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountGen2")
    def storage_account_gen2(
        self,
    ) -> "HdinsightSparkClusterStorageAccountGen2OutputReference":
        return typing.cast("HdinsightSparkClusterStorageAccountGen2OutputReference", jsii.get(self, "storageAccountGen2"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "HdinsightSparkClusterTimeoutsOutputReference":
        return typing.cast("HdinsightSparkClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="clusterVersionInput")
    def cluster_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="componentVersionInput")
    def component_version_input(
        self,
    ) -> typing.Optional["HdinsightSparkClusterComponentVersion"]:
        return typing.cast(typing.Optional["HdinsightSparkClusterComponentVersion"], jsii.get(self, "componentVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionInput")
    def disk_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HdinsightSparkClusterDiskEncryption"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HdinsightSparkClusterDiskEncryption"]]], jsii.get(self, "diskEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInTransitEnabledInput")
    def encryption_in_transit_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "encryptionInTransitEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="extensionInput")
    def extension_input(self) -> typing.Optional["HdinsightSparkClusterExtension"]:
        return typing.cast(typing.Optional["HdinsightSparkClusterExtension"], jsii.get(self, "extensionInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayInput")
    def gateway_input(self) -> typing.Optional["HdinsightSparkClusterGateway"]:
        return typing.cast(typing.Optional["HdinsightSparkClusterGateway"], jsii.get(self, "gatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="metastoresInput")
    def metastores_input(self) -> typing.Optional["HdinsightSparkClusterMetastores"]:
        return typing.cast(typing.Optional["HdinsightSparkClusterMetastores"], jsii.get(self, "metastoresInput"))

    @builtins.property
    @jsii.member(jsii_name="monitorInput")
    def monitor_input(self) -> typing.Optional["HdinsightSparkClusterMonitor"]:
        return typing.cast(typing.Optional["HdinsightSparkClusterMonitor"], jsii.get(self, "monitorInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional["HdinsightSparkClusterNetwork"]:
        return typing.cast(typing.Optional["HdinsightSparkClusterNetwork"], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rolesInput")
    def roles_input(self) -> typing.Optional["HdinsightSparkClusterRoles"]:
        return typing.cast(typing.Optional["HdinsightSparkClusterRoles"], jsii.get(self, "rolesInput"))

    @builtins.property
    @jsii.member(jsii_name="securityProfileInput")
    def security_profile_input(
        self,
    ) -> typing.Optional["HdinsightSparkClusterSecurityProfile"]:
        return typing.cast(typing.Optional["HdinsightSparkClusterSecurityProfile"], jsii.get(self, "securityProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountGen2Input")
    def storage_account_gen2_input(
        self,
    ) -> typing.Optional["HdinsightSparkClusterStorageAccountGen2"]:
        return typing.cast(typing.Optional["HdinsightSparkClusterStorageAccountGen2"], jsii.get(self, "storageAccountGen2Input"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountInput")
    def storage_account_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HdinsightSparkClusterStorageAccount"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HdinsightSparkClusterStorageAccount"]]], jsii.get(self, "storageAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="tierInput")
    def tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tierInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["HdinsightSparkClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["HdinsightSparkClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsMinVersionInput")
    def tls_min_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsMinVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterVersion")
    def cluster_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterVersion"))

    @cluster_version.setter
    def cluster_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkCluster, "cluster_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterVersion", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionInTransitEnabled")
    def encryption_in_transit_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "encryptionInTransitEnabled"))

    @encryption_in_transit_enabled.setter
    def encryption_in_transit_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkCluster, "encryption_in_transit_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionInTransitEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkCluster, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkCluster, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkCluster, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkCluster, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkCluster, "tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)

    @builtins.property
    @jsii.member(jsii_name="tlsMinVersion")
    def tls_min_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsMinVersion"))

    @tls_min_version.setter
    def tls_min_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkCluster, "tls_min_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsMinVersion", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterComponentVersion",
    jsii_struct_bases=[],
    name_mapping={"spark": "spark"},
)
class HdinsightSparkClusterComponentVersion:
    def __init__(self, *, spark: builtins.str) -> None:
        '''
        :param spark: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#spark HdinsightSparkCluster#spark}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterComponentVersion.__init__)
            check_type(argname="argument spark", value=spark, expected_type=type_hints["spark"])
        self._values: typing.Dict[str, typing.Any] = {
            "spark": spark,
        }

    @builtins.property
    def spark(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#spark HdinsightSparkCluster#spark}.'''
        result = self._values.get("spark")
        assert result is not None, "Required property 'spark' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterComponentVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterComponentVersionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterComponentVersionOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterComponentVersionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="sparkInput")
    def spark_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sparkInput"))

    @builtins.property
    @jsii.member(jsii_name="spark")
    def spark(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spark"))

    @spark.setter
    def spark(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterComponentVersionOutputReference, "spark").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spark", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HdinsightSparkClusterComponentVersion]:
        return typing.cast(typing.Optional[HdinsightSparkClusterComponentVersion], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterComponentVersion],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterComponentVersionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_version": "clusterVersion",
        "component_version": "componentVersion",
        "gateway": "gateway",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "roles": "roles",
        "tier": "tier",
        "disk_encryption": "diskEncryption",
        "encryption_in_transit_enabled": "encryptionInTransitEnabled",
        "extension": "extension",
        "id": "id",
        "metastores": "metastores",
        "monitor": "monitor",
        "network": "network",
        "security_profile": "securityProfile",
        "storage_account": "storageAccount",
        "storage_account_gen2": "storageAccountGen2",
        "tags": "tags",
        "timeouts": "timeouts",
        "tls_min_version": "tlsMinVersion",
    },
)
class HdinsightSparkClusterConfig(cdktf.TerraformMetaArguments):
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
        cluster_version: builtins.str,
        component_version: typing.Union[HdinsightSparkClusterComponentVersion, typing.Dict[str, typing.Any]],
        gateway: typing.Union["HdinsightSparkClusterGateway", typing.Dict[str, typing.Any]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        roles: typing.Union["HdinsightSparkClusterRoles", typing.Dict[str, typing.Any]],
        tier: builtins.str,
        disk_encryption: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HdinsightSparkClusterDiskEncryption", typing.Dict[str, typing.Any]]]]] = None,
        encryption_in_transit_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        extension: typing.Optional[typing.Union["HdinsightSparkClusterExtension", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        metastores: typing.Optional[typing.Union["HdinsightSparkClusterMetastores", typing.Dict[str, typing.Any]]] = None,
        monitor: typing.Optional[typing.Union["HdinsightSparkClusterMonitor", typing.Dict[str, typing.Any]]] = None,
        network: typing.Optional[typing.Union["HdinsightSparkClusterNetwork", typing.Dict[str, typing.Any]]] = None,
        security_profile: typing.Optional[typing.Union["HdinsightSparkClusterSecurityProfile", typing.Dict[str, typing.Any]]] = None,
        storage_account: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HdinsightSparkClusterStorageAccount", typing.Dict[str, typing.Any]]]]] = None,
        storage_account_gen2: typing.Optional[typing.Union["HdinsightSparkClusterStorageAccountGen2", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["HdinsightSparkClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        tls_min_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#cluster_version HdinsightSparkCluster#cluster_version}.
        :param component_version: component_version block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#component_version HdinsightSparkCluster#component_version}
        :param gateway: gateway block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#gateway HdinsightSparkCluster#gateway}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#location HdinsightSparkCluster#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#name HdinsightSparkCluster#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#resource_group_name HdinsightSparkCluster#resource_group_name}.
        :param roles: roles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#roles HdinsightSparkCluster#roles}
        :param tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#tier HdinsightSparkCluster#tier}.
        :param disk_encryption: disk_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#disk_encryption HdinsightSparkCluster#disk_encryption}
        :param encryption_in_transit_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#encryption_in_transit_enabled HdinsightSparkCluster#encryption_in_transit_enabled}.
        :param extension: extension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#extension HdinsightSparkCluster#extension}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#id HdinsightSparkCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metastores: metastores block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#metastores HdinsightSparkCluster#metastores}
        :param monitor: monitor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#monitor HdinsightSparkCluster#monitor}
        :param network: network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#network HdinsightSparkCluster#network}
        :param security_profile: security_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#security_profile HdinsightSparkCluster#security_profile}
        :param storage_account: storage_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#storage_account HdinsightSparkCluster#storage_account}
        :param storage_account_gen2: storage_account_gen2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#storage_account_gen2 HdinsightSparkCluster#storage_account_gen2}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#tags HdinsightSparkCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#timeouts HdinsightSparkCluster#timeouts}
        :param tls_min_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#tls_min_version HdinsightSparkCluster#tls_min_version}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(component_version, dict):
            component_version = HdinsightSparkClusterComponentVersion(**component_version)
        if isinstance(gateway, dict):
            gateway = HdinsightSparkClusterGateway(**gateway)
        if isinstance(roles, dict):
            roles = HdinsightSparkClusterRoles(**roles)
        if isinstance(extension, dict):
            extension = HdinsightSparkClusterExtension(**extension)
        if isinstance(metastores, dict):
            metastores = HdinsightSparkClusterMetastores(**metastores)
        if isinstance(monitor, dict):
            monitor = HdinsightSparkClusterMonitor(**monitor)
        if isinstance(network, dict):
            network = HdinsightSparkClusterNetwork(**network)
        if isinstance(security_profile, dict):
            security_profile = HdinsightSparkClusterSecurityProfile(**security_profile)
        if isinstance(storage_account_gen2, dict):
            storage_account_gen2 = HdinsightSparkClusterStorageAccountGen2(**storage_account_gen2)
        if isinstance(timeouts, dict):
            timeouts = HdinsightSparkClusterTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster_version", value=cluster_version, expected_type=type_hints["cluster_version"])
            check_type(argname="argument component_version", value=component_version, expected_type=type_hints["component_version"])
            check_type(argname="argument gateway", value=gateway, expected_type=type_hints["gateway"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument disk_encryption", value=disk_encryption, expected_type=type_hints["disk_encryption"])
            check_type(argname="argument encryption_in_transit_enabled", value=encryption_in_transit_enabled, expected_type=type_hints["encryption_in_transit_enabled"])
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument metastores", value=metastores, expected_type=type_hints["metastores"])
            check_type(argname="argument monitor", value=monitor, expected_type=type_hints["monitor"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument security_profile", value=security_profile, expected_type=type_hints["security_profile"])
            check_type(argname="argument storage_account", value=storage_account, expected_type=type_hints["storage_account"])
            check_type(argname="argument storage_account_gen2", value=storage_account_gen2, expected_type=type_hints["storage_account_gen2"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument tls_min_version", value=tls_min_version, expected_type=type_hints["tls_min_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_version": cluster_version,
            "component_version": component_version,
            "gateway": gateway,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "roles": roles,
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
        if disk_encryption is not None:
            self._values["disk_encryption"] = disk_encryption
        if encryption_in_transit_enabled is not None:
            self._values["encryption_in_transit_enabled"] = encryption_in_transit_enabled
        if extension is not None:
            self._values["extension"] = extension
        if id is not None:
            self._values["id"] = id
        if metastores is not None:
            self._values["metastores"] = metastores
        if monitor is not None:
            self._values["monitor"] = monitor
        if network is not None:
            self._values["network"] = network
        if security_profile is not None:
            self._values["security_profile"] = security_profile
        if storage_account is not None:
            self._values["storage_account"] = storage_account
        if storage_account_gen2 is not None:
            self._values["storage_account_gen2"] = storage_account_gen2
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if tls_min_version is not None:
            self._values["tls_min_version"] = tls_min_version

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
    def cluster_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#cluster_version HdinsightSparkCluster#cluster_version}.'''
        result = self._values.get("cluster_version")
        assert result is not None, "Required property 'cluster_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def component_version(self) -> HdinsightSparkClusterComponentVersion:
        '''component_version block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#component_version HdinsightSparkCluster#component_version}
        '''
        result = self._values.get("component_version")
        assert result is not None, "Required property 'component_version' is missing"
        return typing.cast(HdinsightSparkClusterComponentVersion, result)

    @builtins.property
    def gateway(self) -> "HdinsightSparkClusterGateway":
        '''gateway block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#gateway HdinsightSparkCluster#gateway}
        '''
        result = self._values.get("gateway")
        assert result is not None, "Required property 'gateway' is missing"
        return typing.cast("HdinsightSparkClusterGateway", result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#location HdinsightSparkCluster#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#name HdinsightSparkCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#resource_group_name HdinsightSparkCluster#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def roles(self) -> "HdinsightSparkClusterRoles":
        '''roles block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#roles HdinsightSparkCluster#roles}
        '''
        result = self._values.get("roles")
        assert result is not None, "Required property 'roles' is missing"
        return typing.cast("HdinsightSparkClusterRoles", result)

    @builtins.property
    def tier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#tier HdinsightSparkCluster#tier}.'''
        result = self._values.get("tier")
        assert result is not None, "Required property 'tier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk_encryption(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HdinsightSparkClusterDiskEncryption"]]]:
        '''disk_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#disk_encryption HdinsightSparkCluster#disk_encryption}
        '''
        result = self._values.get("disk_encryption")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HdinsightSparkClusterDiskEncryption"]]], result)

    @builtins.property
    def encryption_in_transit_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#encryption_in_transit_enabled HdinsightSparkCluster#encryption_in_transit_enabled}.'''
        result = self._values.get("encryption_in_transit_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def extension(self) -> typing.Optional["HdinsightSparkClusterExtension"]:
        '''extension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#extension HdinsightSparkCluster#extension}
        '''
        result = self._values.get("extension")
        return typing.cast(typing.Optional["HdinsightSparkClusterExtension"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#id HdinsightSparkCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metastores(self) -> typing.Optional["HdinsightSparkClusterMetastores"]:
        '''metastores block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#metastores HdinsightSparkCluster#metastores}
        '''
        result = self._values.get("metastores")
        return typing.cast(typing.Optional["HdinsightSparkClusterMetastores"], result)

    @builtins.property
    def monitor(self) -> typing.Optional["HdinsightSparkClusterMonitor"]:
        '''monitor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#monitor HdinsightSparkCluster#monitor}
        '''
        result = self._values.get("monitor")
        return typing.cast(typing.Optional["HdinsightSparkClusterMonitor"], result)

    @builtins.property
    def network(self) -> typing.Optional["HdinsightSparkClusterNetwork"]:
        '''network block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#network HdinsightSparkCluster#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional["HdinsightSparkClusterNetwork"], result)

    @builtins.property
    def security_profile(
        self,
    ) -> typing.Optional["HdinsightSparkClusterSecurityProfile"]:
        '''security_profile block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#security_profile HdinsightSparkCluster#security_profile}
        '''
        result = self._values.get("security_profile")
        return typing.cast(typing.Optional["HdinsightSparkClusterSecurityProfile"], result)

    @builtins.property
    def storage_account(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HdinsightSparkClusterStorageAccount"]]]:
        '''storage_account block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#storage_account HdinsightSparkCluster#storage_account}
        '''
        result = self._values.get("storage_account")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HdinsightSparkClusterStorageAccount"]]], result)

    @builtins.property
    def storage_account_gen2(
        self,
    ) -> typing.Optional["HdinsightSparkClusterStorageAccountGen2"]:
        '''storage_account_gen2 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#storage_account_gen2 HdinsightSparkCluster#storage_account_gen2}
        '''
        result = self._values.get("storage_account_gen2")
        return typing.cast(typing.Optional["HdinsightSparkClusterStorageAccountGen2"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#tags HdinsightSparkCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["HdinsightSparkClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#timeouts HdinsightSparkCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["HdinsightSparkClusterTimeouts"], result)

    @builtins.property
    def tls_min_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#tls_min_version HdinsightSparkCluster#tls_min_version}.'''
        result = self._values.get("tls_min_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterDiskEncryption",
    jsii_struct_bases=[],
    name_mapping={
        "encryption_algorithm": "encryptionAlgorithm",
        "encryption_at_host_enabled": "encryptionAtHostEnabled",
        "key_vault_key_id": "keyVaultKeyId",
        "key_vault_managed_identity_id": "keyVaultManagedIdentityId",
    },
)
class HdinsightSparkClusterDiskEncryption:
    def __init__(
        self,
        *,
        encryption_algorithm: typing.Optional[builtins.str] = None,
        encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key_vault_key_id: typing.Optional[builtins.str] = None,
        key_vault_managed_identity_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param encryption_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#encryption_algorithm HdinsightSparkCluster#encryption_algorithm}.
        :param encryption_at_host_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#encryption_at_host_enabled HdinsightSparkCluster#encryption_at_host_enabled}.
        :param key_vault_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#key_vault_key_id HdinsightSparkCluster#key_vault_key_id}.
        :param key_vault_managed_identity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#key_vault_managed_identity_id HdinsightSparkCluster#key_vault_managed_identity_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterDiskEncryption.__init__)
            check_type(argname="argument encryption_algorithm", value=encryption_algorithm, expected_type=type_hints["encryption_algorithm"])
            check_type(argname="argument encryption_at_host_enabled", value=encryption_at_host_enabled, expected_type=type_hints["encryption_at_host_enabled"])
            check_type(argname="argument key_vault_key_id", value=key_vault_key_id, expected_type=type_hints["key_vault_key_id"])
            check_type(argname="argument key_vault_managed_identity_id", value=key_vault_managed_identity_id, expected_type=type_hints["key_vault_managed_identity_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if encryption_algorithm is not None:
            self._values["encryption_algorithm"] = encryption_algorithm
        if encryption_at_host_enabled is not None:
            self._values["encryption_at_host_enabled"] = encryption_at_host_enabled
        if key_vault_key_id is not None:
            self._values["key_vault_key_id"] = key_vault_key_id
        if key_vault_managed_identity_id is not None:
            self._values["key_vault_managed_identity_id"] = key_vault_managed_identity_id

    @builtins.property
    def encryption_algorithm(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#encryption_algorithm HdinsightSparkCluster#encryption_algorithm}.'''
        result = self._values.get("encryption_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_at_host_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#encryption_at_host_enabled HdinsightSparkCluster#encryption_at_host_enabled}.'''
        result = self._values.get("encryption_at_host_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key_vault_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#key_vault_key_id HdinsightSparkCluster#key_vault_key_id}.'''
        result = self._values.get("key_vault_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_managed_identity_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#key_vault_managed_identity_id HdinsightSparkCluster#key_vault_managed_identity_id}.'''
        result = self._values.get("key_vault_managed_identity_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterDiskEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterDiskEncryptionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterDiskEncryptionList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterDiskEncryptionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HdinsightSparkClusterDiskEncryptionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterDiskEncryptionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HdinsightSparkClusterDiskEncryptionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterDiskEncryptionList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterDiskEncryptionList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterDiskEncryptionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HdinsightSparkClusterDiskEncryption]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HdinsightSparkClusterDiskEncryption]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HdinsightSparkClusterDiskEncryption]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterDiskEncryptionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HdinsightSparkClusterDiskEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterDiskEncryptionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterDiskEncryptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEncryptionAlgorithm")
    def reset_encryption_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionAlgorithm", []))

    @jsii.member(jsii_name="resetEncryptionAtHostEnabled")
    def reset_encryption_at_host_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionAtHostEnabled", []))

    @jsii.member(jsii_name="resetKeyVaultKeyId")
    def reset_key_vault_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultKeyId", []))

    @jsii.member(jsii_name="resetKeyVaultManagedIdentityId")
    def reset_key_vault_managed_identity_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultManagedIdentityId", []))

    @builtins.property
    @jsii.member(jsii_name="encryptionAlgorithmInput")
    def encryption_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionAtHostEnabledInput")
    def encryption_at_host_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "encryptionAtHostEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultKeyIdInput")
    def key_vault_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultManagedIdentityIdInput")
    def key_vault_managed_identity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultManagedIdentityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionAlgorithm")
    def encryption_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionAlgorithm"))

    @encryption_algorithm.setter
    def encryption_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterDiskEncryptionOutputReference, "encryption_algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionAtHostEnabled")
    def encryption_at_host_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "encryptionAtHostEnabled"))

    @encryption_at_host_enabled.setter
    def encryption_at_host_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterDiskEncryptionOutputReference, "encryption_at_host_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionAtHostEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultKeyId")
    def key_vault_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultKeyId"))

    @key_vault_key_id.setter
    def key_vault_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterDiskEncryptionOutputReference, "key_vault_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultManagedIdentityId")
    def key_vault_managed_identity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultManagedIdentityId"))

    @key_vault_managed_identity_id.setter
    def key_vault_managed_identity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterDiskEncryptionOutputReference, "key_vault_managed_identity_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultManagedIdentityId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HdinsightSparkClusterDiskEncryption, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HdinsightSparkClusterDiskEncryption, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HdinsightSparkClusterDiskEncryption, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterDiskEncryptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterExtension",
    jsii_struct_bases=[],
    name_mapping={
        "log_analytics_workspace_id": "logAnalyticsWorkspaceId",
        "primary_key": "primaryKey",
    },
)
class HdinsightSparkClusterExtension:
    def __init__(
        self,
        *,
        log_analytics_workspace_id: builtins.str,
        primary_key: builtins.str,
    ) -> None:
        '''
        :param log_analytics_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#log_analytics_workspace_id HdinsightSparkCluster#log_analytics_workspace_id}.
        :param primary_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#primary_key HdinsightSparkCluster#primary_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterExtension.__init__)
            check_type(argname="argument log_analytics_workspace_id", value=log_analytics_workspace_id, expected_type=type_hints["log_analytics_workspace_id"])
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "log_analytics_workspace_id": log_analytics_workspace_id,
            "primary_key": primary_key,
        }

    @builtins.property
    def log_analytics_workspace_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#log_analytics_workspace_id HdinsightSparkCluster#log_analytics_workspace_id}.'''
        result = self._values.get("log_analytics_workspace_id")
        assert result is not None, "Required property 'log_analytics_workspace_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def primary_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#primary_key HdinsightSparkCluster#primary_key}.'''
        result = self._values.get("primary_key")
        assert result is not None, "Required property 'primary_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterExtension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterExtensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterExtensionOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterExtensionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsWorkspaceIdInput")
    def log_analytics_workspace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logAnalyticsWorkspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryKeyInput")
    def primary_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logAnalyticsWorkspaceId"))

    @log_analytics_workspace_id.setter
    def log_analytics_workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterExtensionOutputReference, "log_analytics_workspace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logAnalyticsWorkspaceId", value)

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryKey"))

    @primary_key.setter
    def primary_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterExtensionOutputReference, "primary_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HdinsightSparkClusterExtension]:
        return typing.cast(typing.Optional[HdinsightSparkClusterExtension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterExtension],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterExtensionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterGateway",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class HdinsightSparkClusterGateway:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterGateway.__init__)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterGatewayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterGatewayOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterGatewayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterGatewayOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterGatewayOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HdinsightSparkClusterGateway]:
        return typing.cast(typing.Optional[HdinsightSparkClusterGateway], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterGateway],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterGatewayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterMetastores",
    jsii_struct_bases=[],
    name_mapping={"ambari": "ambari", "hive": "hive", "oozie": "oozie"},
)
class HdinsightSparkClusterMetastores:
    def __init__(
        self,
        *,
        ambari: typing.Optional[typing.Union["HdinsightSparkClusterMetastoresAmbari", typing.Dict[str, typing.Any]]] = None,
        hive: typing.Optional[typing.Union["HdinsightSparkClusterMetastoresHive", typing.Dict[str, typing.Any]]] = None,
        oozie: typing.Optional[typing.Union["HdinsightSparkClusterMetastoresOozie", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ambari: ambari block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#ambari HdinsightSparkCluster#ambari}
        :param hive: hive block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#hive HdinsightSparkCluster#hive}
        :param oozie: oozie block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#oozie HdinsightSparkCluster#oozie}
        '''
        if isinstance(ambari, dict):
            ambari = HdinsightSparkClusterMetastoresAmbari(**ambari)
        if isinstance(hive, dict):
            hive = HdinsightSparkClusterMetastoresHive(**hive)
        if isinstance(oozie, dict):
            oozie = HdinsightSparkClusterMetastoresOozie(**oozie)
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterMetastores.__init__)
            check_type(argname="argument ambari", value=ambari, expected_type=type_hints["ambari"])
            check_type(argname="argument hive", value=hive, expected_type=type_hints["hive"])
            check_type(argname="argument oozie", value=oozie, expected_type=type_hints["oozie"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ambari is not None:
            self._values["ambari"] = ambari
        if hive is not None:
            self._values["hive"] = hive
        if oozie is not None:
            self._values["oozie"] = oozie

    @builtins.property
    def ambari(self) -> typing.Optional["HdinsightSparkClusterMetastoresAmbari"]:
        '''ambari block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#ambari HdinsightSparkCluster#ambari}
        '''
        result = self._values.get("ambari")
        return typing.cast(typing.Optional["HdinsightSparkClusterMetastoresAmbari"], result)

    @builtins.property
    def hive(self) -> typing.Optional["HdinsightSparkClusterMetastoresHive"]:
        '''hive block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#hive HdinsightSparkCluster#hive}
        '''
        result = self._values.get("hive")
        return typing.cast(typing.Optional["HdinsightSparkClusterMetastoresHive"], result)

    @builtins.property
    def oozie(self) -> typing.Optional["HdinsightSparkClusterMetastoresOozie"]:
        '''oozie block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#oozie HdinsightSparkCluster#oozie}
        '''
        result = self._values.get("oozie")
        return typing.cast(typing.Optional["HdinsightSparkClusterMetastoresOozie"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterMetastores(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterMetastoresAmbari",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "password": "password",
        "server": "server",
        "username": "username",
    },
)
class HdinsightSparkClusterMetastoresAmbari:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        password: builtins.str,
        server: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#database_name HdinsightSparkCluster#database_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.
        :param server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#server HdinsightSparkCluster#server}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterMetastoresAmbari.__init__)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "database_name": database_name,
            "password": password,
            "server": server,
            "username": username,
        }

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#database_name HdinsightSparkCluster#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#server HdinsightSparkCluster#server}.'''
        result = self._values.get("server")
        assert result is not None, "Required property 'server' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterMetastoresAmbari(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterMetastoresAmbariOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterMetastoresAmbariOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterMetastoresAmbariOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="serverInput")
    def server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresAmbariOutputReference, "database_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresAmbariOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "server"))

    @server.setter
    def server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresAmbariOutputReference, "server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "server", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresAmbariOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HdinsightSparkClusterMetastoresAmbari]:
        return typing.cast(typing.Optional[HdinsightSparkClusterMetastoresAmbari], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterMetastoresAmbari],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresAmbariOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterMetastoresHive",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "password": "password",
        "server": "server",
        "username": "username",
    },
)
class HdinsightSparkClusterMetastoresHive:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        password: builtins.str,
        server: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#database_name HdinsightSparkCluster#database_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.
        :param server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#server HdinsightSparkCluster#server}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterMetastoresHive.__init__)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "database_name": database_name,
            "password": password,
            "server": server,
            "username": username,
        }

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#database_name HdinsightSparkCluster#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#server HdinsightSparkCluster#server}.'''
        result = self._values.get("server")
        assert result is not None, "Required property 'server' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterMetastoresHive(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterMetastoresHiveOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterMetastoresHiveOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterMetastoresHiveOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="serverInput")
    def server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresHiveOutputReference, "database_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresHiveOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "server"))

    @server.setter
    def server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresHiveOutputReference, "server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "server", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresHiveOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HdinsightSparkClusterMetastoresHive]:
        return typing.cast(typing.Optional[HdinsightSparkClusterMetastoresHive], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterMetastoresHive],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresHiveOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterMetastoresOozie",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "password": "password",
        "server": "server",
        "username": "username",
    },
)
class HdinsightSparkClusterMetastoresOozie:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        password: builtins.str,
        server: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#database_name HdinsightSparkCluster#database_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.
        :param server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#server HdinsightSparkCluster#server}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterMetastoresOozie.__init__)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "database_name": database_name,
            "password": password,
            "server": server,
            "username": username,
        }

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#database_name HdinsightSparkCluster#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#server HdinsightSparkCluster#server}.'''
        result = self._values.get("server")
        assert result is not None, "Required property 'server' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterMetastoresOozie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterMetastoresOozieOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterMetastoresOozieOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterMetastoresOozieOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="serverInput")
    def server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresOozieOutputReference, "database_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresOozieOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "server"))

    @server.setter
    def server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresOozieOutputReference, "server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "server", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresOozieOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HdinsightSparkClusterMetastoresOozie]:
        return typing.cast(typing.Optional[HdinsightSparkClusterMetastoresOozie], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterMetastoresOozie],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresOozieOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HdinsightSparkClusterMetastoresOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterMetastoresOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterMetastoresOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAmbari")
    def put_ambari(
        self,
        *,
        database_name: builtins.str,
        password: builtins.str,
        server: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#database_name HdinsightSparkCluster#database_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.
        :param server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#server HdinsightSparkCluster#server}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.
        '''
        value = HdinsightSparkClusterMetastoresAmbari(
            database_name=database_name,
            password=password,
            server=server,
            username=username,
        )

        return typing.cast(None, jsii.invoke(self, "putAmbari", [value]))

    @jsii.member(jsii_name="putHive")
    def put_hive(
        self,
        *,
        database_name: builtins.str,
        password: builtins.str,
        server: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#database_name HdinsightSparkCluster#database_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.
        :param server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#server HdinsightSparkCluster#server}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.
        '''
        value = HdinsightSparkClusterMetastoresHive(
            database_name=database_name,
            password=password,
            server=server,
            username=username,
        )

        return typing.cast(None, jsii.invoke(self, "putHive", [value]))

    @jsii.member(jsii_name="putOozie")
    def put_oozie(
        self,
        *,
        database_name: builtins.str,
        password: builtins.str,
        server: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#database_name HdinsightSparkCluster#database_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.
        :param server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#server HdinsightSparkCluster#server}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.
        '''
        value = HdinsightSparkClusterMetastoresOozie(
            database_name=database_name,
            password=password,
            server=server,
            username=username,
        )

        return typing.cast(None, jsii.invoke(self, "putOozie", [value]))

    @jsii.member(jsii_name="resetAmbari")
    def reset_ambari(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmbari", []))

    @jsii.member(jsii_name="resetHive")
    def reset_hive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHive", []))

    @jsii.member(jsii_name="resetOozie")
    def reset_oozie(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOozie", []))

    @builtins.property
    @jsii.member(jsii_name="ambari")
    def ambari(self) -> HdinsightSparkClusterMetastoresAmbariOutputReference:
        return typing.cast(HdinsightSparkClusterMetastoresAmbariOutputReference, jsii.get(self, "ambari"))

    @builtins.property
    @jsii.member(jsii_name="hive")
    def hive(self) -> HdinsightSparkClusterMetastoresHiveOutputReference:
        return typing.cast(HdinsightSparkClusterMetastoresHiveOutputReference, jsii.get(self, "hive"))

    @builtins.property
    @jsii.member(jsii_name="oozie")
    def oozie(self) -> HdinsightSparkClusterMetastoresOozieOutputReference:
        return typing.cast(HdinsightSparkClusterMetastoresOozieOutputReference, jsii.get(self, "oozie"))

    @builtins.property
    @jsii.member(jsii_name="ambariInput")
    def ambari_input(self) -> typing.Optional[HdinsightSparkClusterMetastoresAmbari]:
        return typing.cast(typing.Optional[HdinsightSparkClusterMetastoresAmbari], jsii.get(self, "ambariInput"))

    @builtins.property
    @jsii.member(jsii_name="hiveInput")
    def hive_input(self) -> typing.Optional[HdinsightSparkClusterMetastoresHive]:
        return typing.cast(typing.Optional[HdinsightSparkClusterMetastoresHive], jsii.get(self, "hiveInput"))

    @builtins.property
    @jsii.member(jsii_name="oozieInput")
    def oozie_input(self) -> typing.Optional[HdinsightSparkClusterMetastoresOozie]:
        return typing.cast(typing.Optional[HdinsightSparkClusterMetastoresOozie], jsii.get(self, "oozieInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HdinsightSparkClusterMetastores]:
        return typing.cast(typing.Optional[HdinsightSparkClusterMetastores], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterMetastores],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMetastoresOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterMonitor",
    jsii_struct_bases=[],
    name_mapping={
        "log_analytics_workspace_id": "logAnalyticsWorkspaceId",
        "primary_key": "primaryKey",
    },
)
class HdinsightSparkClusterMonitor:
    def __init__(
        self,
        *,
        log_analytics_workspace_id: builtins.str,
        primary_key: builtins.str,
    ) -> None:
        '''
        :param log_analytics_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#log_analytics_workspace_id HdinsightSparkCluster#log_analytics_workspace_id}.
        :param primary_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#primary_key HdinsightSparkCluster#primary_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterMonitor.__init__)
            check_type(argname="argument log_analytics_workspace_id", value=log_analytics_workspace_id, expected_type=type_hints["log_analytics_workspace_id"])
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "log_analytics_workspace_id": log_analytics_workspace_id,
            "primary_key": primary_key,
        }

    @builtins.property
    def log_analytics_workspace_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#log_analytics_workspace_id HdinsightSparkCluster#log_analytics_workspace_id}.'''
        result = self._values.get("log_analytics_workspace_id")
        assert result is not None, "Required property 'log_analytics_workspace_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def primary_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#primary_key HdinsightSparkCluster#primary_key}.'''
        result = self._values.get("primary_key")
        assert result is not None, "Required property 'primary_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterMonitor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterMonitorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterMonitorOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterMonitorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsWorkspaceIdInput")
    def log_analytics_workspace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logAnalyticsWorkspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryKeyInput")
    def primary_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logAnalyticsWorkspaceId"))

    @log_analytics_workspace_id.setter
    def log_analytics_workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMonitorOutputReference, "log_analytics_workspace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logAnalyticsWorkspaceId", value)

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryKey"))

    @primary_key.setter
    def primary_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMonitorOutputReference, "primary_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HdinsightSparkClusterMonitor]:
        return typing.cast(typing.Optional[HdinsightSparkClusterMonitor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterMonitor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterMonitorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterNetwork",
    jsii_struct_bases=[],
    name_mapping={
        "connection_direction": "connectionDirection",
        "private_link_enabled": "privateLinkEnabled",
    },
)
class HdinsightSparkClusterNetwork:
    def __init__(
        self,
        *,
        connection_direction: typing.Optional[builtins.str] = None,
        private_link_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection_direction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#connection_direction HdinsightSparkCluster#connection_direction}.
        :param private_link_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#private_link_enabled HdinsightSparkCluster#private_link_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterNetwork.__init__)
            check_type(argname="argument connection_direction", value=connection_direction, expected_type=type_hints["connection_direction"])
            check_type(argname="argument private_link_enabled", value=private_link_enabled, expected_type=type_hints["private_link_enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_direction is not None:
            self._values["connection_direction"] = connection_direction
        if private_link_enabled is not None:
            self._values["private_link_enabled"] = private_link_enabled

    @builtins.property
    def connection_direction(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#connection_direction HdinsightSparkCluster#connection_direction}.'''
        result = self._values.get("connection_direction")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_link_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#private_link_enabled HdinsightSparkCluster#private_link_enabled}.'''
        result = self._values.get("private_link_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterNetwork(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterNetworkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterNetworkOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterNetworkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectionDirection")
    def reset_connection_direction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionDirection", []))

    @jsii.member(jsii_name="resetPrivateLinkEnabled")
    def reset_private_link_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateLinkEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="connectionDirectionInput")
    def connection_direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionDirectionInput"))

    @builtins.property
    @jsii.member(jsii_name="privateLinkEnabledInput")
    def private_link_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "privateLinkEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionDirection")
    def connection_direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionDirection"))

    @connection_direction.setter
    def connection_direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterNetworkOutputReference, "connection_direction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionDirection", value)

    @builtins.property
    @jsii.member(jsii_name="privateLinkEnabled")
    def private_link_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "privateLinkEnabled"))

    @private_link_enabled.setter
    def private_link_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterNetworkOutputReference, "private_link_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateLinkEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HdinsightSparkClusterNetwork]:
        return typing.cast(typing.Optional[HdinsightSparkClusterNetwork], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterNetwork],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterNetworkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRoles",
    jsii_struct_bases=[],
    name_mapping={
        "head_node": "headNode",
        "worker_node": "workerNode",
        "zookeeper_node": "zookeeperNode",
    },
)
class HdinsightSparkClusterRoles:
    def __init__(
        self,
        *,
        head_node: typing.Union["HdinsightSparkClusterRolesHeadNode", typing.Dict[str, typing.Any]],
        worker_node: typing.Union["HdinsightSparkClusterRolesWorkerNode", typing.Dict[str, typing.Any]],
        zookeeper_node: typing.Union["HdinsightSparkClusterRolesZookeeperNode", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param head_node: head_node block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#head_node HdinsightSparkCluster#head_node}
        :param worker_node: worker_node block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#worker_node HdinsightSparkCluster#worker_node}
        :param zookeeper_node: zookeeper_node block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#zookeeper_node HdinsightSparkCluster#zookeeper_node}
        '''
        if isinstance(head_node, dict):
            head_node = HdinsightSparkClusterRolesHeadNode(**head_node)
        if isinstance(worker_node, dict):
            worker_node = HdinsightSparkClusterRolesWorkerNode(**worker_node)
        if isinstance(zookeeper_node, dict):
            zookeeper_node = HdinsightSparkClusterRolesZookeeperNode(**zookeeper_node)
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterRoles.__init__)
            check_type(argname="argument head_node", value=head_node, expected_type=type_hints["head_node"])
            check_type(argname="argument worker_node", value=worker_node, expected_type=type_hints["worker_node"])
            check_type(argname="argument zookeeper_node", value=zookeeper_node, expected_type=type_hints["zookeeper_node"])
        self._values: typing.Dict[str, typing.Any] = {
            "head_node": head_node,
            "worker_node": worker_node,
            "zookeeper_node": zookeeper_node,
        }

    @builtins.property
    def head_node(self) -> "HdinsightSparkClusterRolesHeadNode":
        '''head_node block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#head_node HdinsightSparkCluster#head_node}
        '''
        result = self._values.get("head_node")
        assert result is not None, "Required property 'head_node' is missing"
        return typing.cast("HdinsightSparkClusterRolesHeadNode", result)

    @builtins.property
    def worker_node(self) -> "HdinsightSparkClusterRolesWorkerNode":
        '''worker_node block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#worker_node HdinsightSparkCluster#worker_node}
        '''
        result = self._values.get("worker_node")
        assert result is not None, "Required property 'worker_node' is missing"
        return typing.cast("HdinsightSparkClusterRolesWorkerNode", result)

    @builtins.property
    def zookeeper_node(self) -> "HdinsightSparkClusterRolesZookeeperNode":
        '''zookeeper_node block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#zookeeper_node HdinsightSparkCluster#zookeeper_node}
        '''
        result = self._values.get("zookeeper_node")
        assert result is not None, "Required property 'zookeeper_node' is missing"
        return typing.cast("HdinsightSparkClusterRolesZookeeperNode", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterRoles(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesHeadNode",
    jsii_struct_bases=[],
    name_mapping={
        "username": "username",
        "vm_size": "vmSize",
        "password": "password",
        "ssh_keys": "sshKeys",
        "subnet_id": "subnetId",
        "virtual_network_id": "virtualNetworkId",
    },
)
class HdinsightSparkClusterRolesHeadNode:
    def __init__(
        self,
        *,
        username: builtins.str,
        vm_size: builtins.str,
        password: typing.Optional[builtins.str] = None,
        ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        virtual_network_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.
        :param vm_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#vm_size HdinsightSparkCluster#vm_size}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.
        :param ssh_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#ssh_keys HdinsightSparkCluster#ssh_keys}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#subnet_id HdinsightSparkCluster#subnet_id}.
        :param virtual_network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#virtual_network_id HdinsightSparkCluster#virtual_network_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesHeadNode.__init__)
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument vm_size", value=vm_size, expected_type=type_hints["vm_size"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument ssh_keys", value=ssh_keys, expected_type=type_hints["ssh_keys"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument virtual_network_id", value=virtual_network_id, expected_type=type_hints["virtual_network_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "username": username,
            "vm_size": vm_size,
        }
        if password is not None:
            self._values["password"] = password
        if ssh_keys is not None:
            self._values["ssh_keys"] = ssh_keys
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if virtual_network_id is not None:
            self._values["virtual_network_id"] = virtual_network_id

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vm_size(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#vm_size HdinsightSparkCluster#vm_size}.'''
        result = self._values.get("vm_size")
        assert result is not None, "Required property 'vm_size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssh_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#ssh_keys HdinsightSparkCluster#ssh_keys}.'''
        result = self._values.get("ssh_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#subnet_id HdinsightSparkCluster#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_network_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#virtual_network_id HdinsightSparkCluster#virtual_network_id}.'''
        result = self._values.get("virtual_network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterRolesHeadNode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterRolesHeadNodeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesHeadNodeOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesHeadNodeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetSshKeys")
    def reset_ssh_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshKeys", []))

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @jsii.member(jsii_name="resetVirtualNetworkId")
    def reset_virtual_network_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkId", []))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="sshKeysInput")
    def ssh_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkIdInput")
    def virtual_network_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vmSizeInput")
    def vm_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesHeadNodeOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="sshKeys")
    def ssh_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sshKeys"))

    @ssh_keys.setter
    def ssh_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesHeadNodeOutputReference, "ssh_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshKeys", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesHeadNodeOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesHeadNodeOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkId")
    def virtual_network_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkId"))

    @virtual_network_id.setter
    def virtual_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesHeadNodeOutputReference, "virtual_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="vmSize")
    def vm_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmSize"))

    @vm_size.setter
    def vm_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesHeadNodeOutputReference, "vm_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmSize", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HdinsightSparkClusterRolesHeadNode]:
        return typing.cast(typing.Optional[HdinsightSparkClusterRolesHeadNode], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterRolesHeadNode],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesHeadNodeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HdinsightSparkClusterRolesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHeadNode")
    def put_head_node(
        self,
        *,
        username: builtins.str,
        vm_size: builtins.str,
        password: typing.Optional[builtins.str] = None,
        ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        virtual_network_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.
        :param vm_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#vm_size HdinsightSparkCluster#vm_size}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.
        :param ssh_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#ssh_keys HdinsightSparkCluster#ssh_keys}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#subnet_id HdinsightSparkCluster#subnet_id}.
        :param virtual_network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#virtual_network_id HdinsightSparkCluster#virtual_network_id}.
        '''
        value = HdinsightSparkClusterRolesHeadNode(
            username=username,
            vm_size=vm_size,
            password=password,
            ssh_keys=ssh_keys,
            subnet_id=subnet_id,
            virtual_network_id=virtual_network_id,
        )

        return typing.cast(None, jsii.invoke(self, "putHeadNode", [value]))

    @jsii.member(jsii_name="putWorkerNode")
    def put_worker_node(
        self,
        *,
        target_instance_count: jsii.Number,
        username: builtins.str,
        vm_size: builtins.str,
        autoscale: typing.Optional[typing.Union["HdinsightSparkClusterRolesWorkerNodeAutoscale", typing.Dict[str, typing.Any]]] = None,
        password: typing.Optional[builtins.str] = None,
        ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        virtual_network_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target_instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#target_instance_count HdinsightSparkCluster#target_instance_count}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.
        :param vm_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#vm_size HdinsightSparkCluster#vm_size}.
        :param autoscale: autoscale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#autoscale HdinsightSparkCluster#autoscale}
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.
        :param ssh_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#ssh_keys HdinsightSparkCluster#ssh_keys}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#subnet_id HdinsightSparkCluster#subnet_id}.
        :param virtual_network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#virtual_network_id HdinsightSparkCluster#virtual_network_id}.
        '''
        value = HdinsightSparkClusterRolesWorkerNode(
            target_instance_count=target_instance_count,
            username=username,
            vm_size=vm_size,
            autoscale=autoscale,
            password=password,
            ssh_keys=ssh_keys,
            subnet_id=subnet_id,
            virtual_network_id=virtual_network_id,
        )

        return typing.cast(None, jsii.invoke(self, "putWorkerNode", [value]))

    @jsii.member(jsii_name="putZookeeperNode")
    def put_zookeeper_node(
        self,
        *,
        username: builtins.str,
        vm_size: builtins.str,
        password: typing.Optional[builtins.str] = None,
        ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        virtual_network_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.
        :param vm_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#vm_size HdinsightSparkCluster#vm_size}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.
        :param ssh_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#ssh_keys HdinsightSparkCluster#ssh_keys}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#subnet_id HdinsightSparkCluster#subnet_id}.
        :param virtual_network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#virtual_network_id HdinsightSparkCluster#virtual_network_id}.
        '''
        value = HdinsightSparkClusterRolesZookeeperNode(
            username=username,
            vm_size=vm_size,
            password=password,
            ssh_keys=ssh_keys,
            subnet_id=subnet_id,
            virtual_network_id=virtual_network_id,
        )

        return typing.cast(None, jsii.invoke(self, "putZookeeperNode", [value]))

    @builtins.property
    @jsii.member(jsii_name="headNode")
    def head_node(self) -> HdinsightSparkClusterRolesHeadNodeOutputReference:
        return typing.cast(HdinsightSparkClusterRolesHeadNodeOutputReference, jsii.get(self, "headNode"))

    @builtins.property
    @jsii.member(jsii_name="workerNode")
    def worker_node(self) -> "HdinsightSparkClusterRolesWorkerNodeOutputReference":
        return typing.cast("HdinsightSparkClusterRolesWorkerNodeOutputReference", jsii.get(self, "workerNode"))

    @builtins.property
    @jsii.member(jsii_name="zookeeperNode")
    def zookeeper_node(
        self,
    ) -> "HdinsightSparkClusterRolesZookeeperNodeOutputReference":
        return typing.cast("HdinsightSparkClusterRolesZookeeperNodeOutputReference", jsii.get(self, "zookeeperNode"))

    @builtins.property
    @jsii.member(jsii_name="headNodeInput")
    def head_node_input(self) -> typing.Optional[HdinsightSparkClusterRolesHeadNode]:
        return typing.cast(typing.Optional[HdinsightSparkClusterRolesHeadNode], jsii.get(self, "headNodeInput"))

    @builtins.property
    @jsii.member(jsii_name="workerNodeInput")
    def worker_node_input(
        self,
    ) -> typing.Optional["HdinsightSparkClusterRolesWorkerNode"]:
        return typing.cast(typing.Optional["HdinsightSparkClusterRolesWorkerNode"], jsii.get(self, "workerNodeInput"))

    @builtins.property
    @jsii.member(jsii_name="zookeeperNodeInput")
    def zookeeper_node_input(
        self,
    ) -> typing.Optional["HdinsightSparkClusterRolesZookeeperNode"]:
        return typing.cast(typing.Optional["HdinsightSparkClusterRolesZookeeperNode"], jsii.get(self, "zookeeperNodeInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HdinsightSparkClusterRoles]:
        return typing.cast(typing.Optional[HdinsightSparkClusterRoles], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterRoles],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesWorkerNode",
    jsii_struct_bases=[],
    name_mapping={
        "target_instance_count": "targetInstanceCount",
        "username": "username",
        "vm_size": "vmSize",
        "autoscale": "autoscale",
        "password": "password",
        "ssh_keys": "sshKeys",
        "subnet_id": "subnetId",
        "virtual_network_id": "virtualNetworkId",
    },
)
class HdinsightSparkClusterRolesWorkerNode:
    def __init__(
        self,
        *,
        target_instance_count: jsii.Number,
        username: builtins.str,
        vm_size: builtins.str,
        autoscale: typing.Optional[typing.Union["HdinsightSparkClusterRolesWorkerNodeAutoscale", typing.Dict[str, typing.Any]]] = None,
        password: typing.Optional[builtins.str] = None,
        ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        virtual_network_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target_instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#target_instance_count HdinsightSparkCluster#target_instance_count}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.
        :param vm_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#vm_size HdinsightSparkCluster#vm_size}.
        :param autoscale: autoscale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#autoscale HdinsightSparkCluster#autoscale}
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.
        :param ssh_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#ssh_keys HdinsightSparkCluster#ssh_keys}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#subnet_id HdinsightSparkCluster#subnet_id}.
        :param virtual_network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#virtual_network_id HdinsightSparkCluster#virtual_network_id}.
        '''
        if isinstance(autoscale, dict):
            autoscale = HdinsightSparkClusterRolesWorkerNodeAutoscale(**autoscale)
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesWorkerNode.__init__)
            check_type(argname="argument target_instance_count", value=target_instance_count, expected_type=type_hints["target_instance_count"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument vm_size", value=vm_size, expected_type=type_hints["vm_size"])
            check_type(argname="argument autoscale", value=autoscale, expected_type=type_hints["autoscale"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument ssh_keys", value=ssh_keys, expected_type=type_hints["ssh_keys"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument virtual_network_id", value=virtual_network_id, expected_type=type_hints["virtual_network_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "target_instance_count": target_instance_count,
            "username": username,
            "vm_size": vm_size,
        }
        if autoscale is not None:
            self._values["autoscale"] = autoscale
        if password is not None:
            self._values["password"] = password
        if ssh_keys is not None:
            self._values["ssh_keys"] = ssh_keys
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if virtual_network_id is not None:
            self._values["virtual_network_id"] = virtual_network_id

    @builtins.property
    def target_instance_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#target_instance_count HdinsightSparkCluster#target_instance_count}.'''
        result = self._values.get("target_instance_count")
        assert result is not None, "Required property 'target_instance_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vm_size(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#vm_size HdinsightSparkCluster#vm_size}.'''
        result = self._values.get("vm_size")
        assert result is not None, "Required property 'vm_size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def autoscale(
        self,
    ) -> typing.Optional["HdinsightSparkClusterRolesWorkerNodeAutoscale"]:
        '''autoscale block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#autoscale HdinsightSparkCluster#autoscale}
        '''
        result = self._values.get("autoscale")
        return typing.cast(typing.Optional["HdinsightSparkClusterRolesWorkerNodeAutoscale"], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssh_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#ssh_keys HdinsightSparkCluster#ssh_keys}.'''
        result = self._values.get("ssh_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#subnet_id HdinsightSparkCluster#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_network_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#virtual_network_id HdinsightSparkCluster#virtual_network_id}.'''
        result = self._values.get("virtual_network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterRolesWorkerNode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesWorkerNodeAutoscale",
    jsii_struct_bases=[],
    name_mapping={"capacity": "capacity", "recurrence": "recurrence"},
)
class HdinsightSparkClusterRolesWorkerNodeAutoscale:
    def __init__(
        self,
        *,
        capacity: typing.Optional[typing.Union["HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity", typing.Dict[str, typing.Any]]] = None,
        recurrence: typing.Optional[typing.Union["HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param capacity: capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#capacity HdinsightSparkCluster#capacity}
        :param recurrence: recurrence block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#recurrence HdinsightSparkCluster#recurrence}
        '''
        if isinstance(capacity, dict):
            capacity = HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity(**capacity)
        if isinstance(recurrence, dict):
            recurrence = HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence(**recurrence)
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesWorkerNodeAutoscale.__init__)
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument recurrence", value=recurrence, expected_type=type_hints["recurrence"])
        self._values: typing.Dict[str, typing.Any] = {}
        if capacity is not None:
            self._values["capacity"] = capacity
        if recurrence is not None:
            self._values["recurrence"] = recurrence

    @builtins.property
    def capacity(
        self,
    ) -> typing.Optional["HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity"]:
        '''capacity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#capacity HdinsightSparkCluster#capacity}
        '''
        result = self._values.get("capacity")
        return typing.cast(typing.Optional["HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity"], result)

    @builtins.property
    def recurrence(
        self,
    ) -> typing.Optional["HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence"]:
        '''recurrence block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#recurrence HdinsightSparkCluster#recurrence}
        '''
        result = self._values.get("recurrence")
        return typing.cast(typing.Optional["HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterRolesWorkerNodeAutoscale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity",
    jsii_struct_bases=[],
    name_mapping={
        "max_instance_count": "maxInstanceCount",
        "min_instance_count": "minInstanceCount",
    },
)
class HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity:
    def __init__(
        self,
        *,
        max_instance_count: jsii.Number,
        min_instance_count: jsii.Number,
    ) -> None:
        '''
        :param max_instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#max_instance_count HdinsightSparkCluster#max_instance_count}.
        :param min_instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#min_instance_count HdinsightSparkCluster#min_instance_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity.__init__)
            check_type(argname="argument max_instance_count", value=max_instance_count, expected_type=type_hints["max_instance_count"])
            check_type(argname="argument min_instance_count", value=min_instance_count, expected_type=type_hints["min_instance_count"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_instance_count": max_instance_count,
            "min_instance_count": min_instance_count,
        }

    @builtins.property
    def max_instance_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#max_instance_count HdinsightSparkCluster#max_instance_count}.'''
        result = self._values.get("max_instance_count")
        assert result is not None, "Required property 'max_instance_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_instance_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#min_instance_count HdinsightSparkCluster#min_instance_count}.'''
        result = self._values.get("min_instance_count")
        assert result is not None, "Required property 'min_instance_count' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacityOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxInstanceCountInput")
    def max_instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInstanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="minInstanceCountInput")
    def min_instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInstanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="maxInstanceCount")
    def max_instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxInstanceCount"))

    @max_instance_count.setter
    def max_instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacityOutputReference, "max_instance_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxInstanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="minInstanceCount")
    def min_instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minInstanceCount"))

    @min_instance_count.setter
    def min_instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacityOutputReference, "min_instance_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minInstanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity]:
        return typing.cast(typing.Optional[HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HdinsightSparkClusterRolesWorkerNodeAutoscaleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesWorkerNodeAutoscaleOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesWorkerNodeAutoscaleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCapacity")
    def put_capacity(
        self,
        *,
        max_instance_count: jsii.Number,
        min_instance_count: jsii.Number,
    ) -> None:
        '''
        :param max_instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#max_instance_count HdinsightSparkCluster#max_instance_count}.
        :param min_instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#min_instance_count HdinsightSparkCluster#min_instance_count}.
        '''
        value = HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity(
            max_instance_count=max_instance_count,
            min_instance_count=min_instance_count,
        )

        return typing.cast(None, jsii.invoke(self, "putCapacity", [value]))

    @jsii.member(jsii_name="putRecurrence")
    def put_recurrence(
        self,
        *,
        schedule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule", typing.Dict[str, typing.Any]]]],
        timezone: builtins.str,
    ) -> None:
        '''
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#schedule HdinsightSparkCluster#schedule}
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#timezone HdinsightSparkCluster#timezone}.
        '''
        value = HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence(
            schedule=schedule, timezone=timezone
        )

        return typing.cast(None, jsii.invoke(self, "putRecurrence", [value]))

    @jsii.member(jsii_name="resetCapacity")
    def reset_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacity", []))

    @jsii.member(jsii_name="resetRecurrence")
    def reset_recurrence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecurrence", []))

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(
        self,
    ) -> HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacityOutputReference:
        return typing.cast(HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacityOutputReference, jsii.get(self, "capacity"))

    @builtins.property
    @jsii.member(jsii_name="recurrence")
    def recurrence(
        self,
    ) -> "HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceOutputReference":
        return typing.cast("HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceOutputReference", jsii.get(self, "recurrence"))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(
        self,
    ) -> typing.Optional[HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity]:
        return typing.cast(typing.Optional[HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="recurrenceInput")
    def recurrence_input(
        self,
    ) -> typing.Optional["HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence"]:
        return typing.cast(typing.Optional["HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence"], jsii.get(self, "recurrenceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HdinsightSparkClusterRolesWorkerNodeAutoscale]:
        return typing.cast(typing.Optional[HdinsightSparkClusterRolesWorkerNodeAutoscale], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterRolesWorkerNodeAutoscale],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeAutoscaleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence",
    jsii_struct_bases=[],
    name_mapping={"schedule": "schedule", "timezone": "timezone"},
)
class HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence:
    def __init__(
        self,
        *,
        schedule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule", typing.Dict[str, typing.Any]]]],
        timezone: builtins.str,
    ) -> None:
        '''
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#schedule HdinsightSparkCluster#schedule}
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#timezone HdinsightSparkCluster#timezone}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence.__init__)
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
        self._values: typing.Dict[str, typing.Any] = {
            "schedule": schedule,
            "timezone": timezone,
        }

    @builtins.property
    def schedule(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule"]]:
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#schedule HdinsightSparkCluster#schedule}
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule"]], result)

    @builtins.property
    def timezone(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#timezone HdinsightSparkCluster#timezone}.'''
        result = self._values.get("timezone")
        assert result is not None, "Required property 'timezone' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceOutputReference.put_schedule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> "HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleList":
        return typing.cast("HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleList", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule"]]], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceOutputReference, "timezone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence]:
        return typing.cast(typing.Optional[HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "days": "days",
        "target_instance_count": "targetInstanceCount",
        "time": "time",
    },
)
class HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule:
    def __init__(
        self,
        *,
        days: typing.Sequence[builtins.str],
        target_instance_count: jsii.Number,
        time: builtins.str,
    ) -> None:
        '''
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#days HdinsightSparkCluster#days}.
        :param target_instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#target_instance_count HdinsightSparkCluster#target_instance_count}.
        :param time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#time HdinsightSparkCluster#time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule.__init__)
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
            check_type(argname="argument target_instance_count", value=target_instance_count, expected_type=type_hints["target_instance_count"])
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
        self._values: typing.Dict[str, typing.Any] = {
            "days": days,
            "target_instance_count": target_instance_count,
            "time": time,
        }

    @builtins.property
    def days(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#days HdinsightSparkCluster#days}.'''
        result = self._values.get("days")
        assert result is not None, "Required property 'days' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def target_instance_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#target_instance_count HdinsightSparkCluster#target_instance_count}.'''
        result = self._values.get("target_instance_count")
        assert result is not None, "Required property 'target_instance_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#time HdinsightSparkCluster#time}.'''
        result = self._values.get("time")
        assert result is not None, "Required property 'time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="daysInput")
    def days_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "daysInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInstanceCountInput")
    def target_instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetInstanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="days")
    def days(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "days"))

    @days.setter
    def days(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleOutputReference, "days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "days", value)

    @builtins.property
    @jsii.member(jsii_name="targetInstanceCount")
    def target_instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetInstanceCount"))

    @target_instance_count.setter
    def target_instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleOutputReference, "target_instance_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetInstanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "time"))

    @time.setter
    def time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleOutputReference, "time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HdinsightSparkClusterRolesWorkerNodeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesWorkerNodeOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesWorkerNodeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutoscale")
    def put_autoscale(
        self,
        *,
        capacity: typing.Optional[typing.Union[HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity, typing.Dict[str, typing.Any]]] = None,
        recurrence: typing.Optional[typing.Union[HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param capacity: capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#capacity HdinsightSparkCluster#capacity}
        :param recurrence: recurrence block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#recurrence HdinsightSparkCluster#recurrence}
        '''
        value = HdinsightSparkClusterRolesWorkerNodeAutoscale(
            capacity=capacity, recurrence=recurrence
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscale", [value]))

    @jsii.member(jsii_name="resetAutoscale")
    def reset_autoscale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscale", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetSshKeys")
    def reset_ssh_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshKeys", []))

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @jsii.member(jsii_name="resetVirtualNetworkId")
    def reset_virtual_network_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkId", []))

    @builtins.property
    @jsii.member(jsii_name="autoscale")
    def autoscale(self) -> HdinsightSparkClusterRolesWorkerNodeAutoscaleOutputReference:
        return typing.cast(HdinsightSparkClusterRolesWorkerNodeAutoscaleOutputReference, jsii.get(self, "autoscale"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleInput")
    def autoscale_input(
        self,
    ) -> typing.Optional[HdinsightSparkClusterRolesWorkerNodeAutoscale]:
        return typing.cast(typing.Optional[HdinsightSparkClusterRolesWorkerNodeAutoscale], jsii.get(self, "autoscaleInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="sshKeysInput")
    def ssh_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInstanceCountInput")
    def target_instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetInstanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkIdInput")
    def virtual_network_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vmSizeInput")
    def vm_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="sshKeys")
    def ssh_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sshKeys"))

    @ssh_keys.setter
    def ssh_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeOutputReference, "ssh_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshKeys", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="targetInstanceCount")
    def target_instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetInstanceCount"))

    @target_instance_count.setter
    def target_instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeOutputReference, "target_instance_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetInstanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkId")
    def virtual_network_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkId"))

    @virtual_network_id.setter
    def virtual_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeOutputReference, "virtual_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="vmSize")
    def vm_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmSize"))

    @vm_size.setter
    def vm_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeOutputReference, "vm_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmSize", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HdinsightSparkClusterRolesWorkerNode]:
        return typing.cast(typing.Optional[HdinsightSparkClusterRolesWorkerNode], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterRolesWorkerNode],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesWorkerNodeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesZookeeperNode",
    jsii_struct_bases=[],
    name_mapping={
        "username": "username",
        "vm_size": "vmSize",
        "password": "password",
        "ssh_keys": "sshKeys",
        "subnet_id": "subnetId",
        "virtual_network_id": "virtualNetworkId",
    },
)
class HdinsightSparkClusterRolesZookeeperNode:
    def __init__(
        self,
        *,
        username: builtins.str,
        vm_size: builtins.str,
        password: typing.Optional[builtins.str] = None,
        ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        virtual_network_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.
        :param vm_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#vm_size HdinsightSparkCluster#vm_size}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.
        :param ssh_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#ssh_keys HdinsightSparkCluster#ssh_keys}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#subnet_id HdinsightSparkCluster#subnet_id}.
        :param virtual_network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#virtual_network_id HdinsightSparkCluster#virtual_network_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesZookeeperNode.__init__)
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument vm_size", value=vm_size, expected_type=type_hints["vm_size"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument ssh_keys", value=ssh_keys, expected_type=type_hints["ssh_keys"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument virtual_network_id", value=virtual_network_id, expected_type=type_hints["virtual_network_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "username": username,
            "vm_size": vm_size,
        }
        if password is not None:
            self._values["password"] = password
        if ssh_keys is not None:
            self._values["ssh_keys"] = ssh_keys
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if virtual_network_id is not None:
            self._values["virtual_network_id"] = virtual_network_id

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#username HdinsightSparkCluster#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vm_size(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#vm_size HdinsightSparkCluster#vm_size}.'''
        result = self._values.get("vm_size")
        assert result is not None, "Required property 'vm_size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#password HdinsightSparkCluster#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssh_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#ssh_keys HdinsightSparkCluster#ssh_keys}.'''
        result = self._values.get("ssh_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#subnet_id HdinsightSparkCluster#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_network_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#virtual_network_id HdinsightSparkCluster#virtual_network_id}.'''
        result = self._values.get("virtual_network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterRolesZookeeperNode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterRolesZookeeperNodeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterRolesZookeeperNodeOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterRolesZookeeperNodeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetSshKeys")
    def reset_ssh_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshKeys", []))

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @jsii.member(jsii_name="resetVirtualNetworkId")
    def reset_virtual_network_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkId", []))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="sshKeysInput")
    def ssh_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkIdInput")
    def virtual_network_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vmSizeInput")
    def vm_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesZookeeperNodeOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="sshKeys")
    def ssh_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sshKeys"))

    @ssh_keys.setter
    def ssh_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesZookeeperNodeOutputReference, "ssh_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshKeys", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesZookeeperNodeOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesZookeeperNodeOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkId")
    def virtual_network_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkId"))

    @virtual_network_id.setter
    def virtual_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesZookeeperNodeOutputReference, "virtual_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="vmSize")
    def vm_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmSize"))

    @vm_size.setter
    def vm_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesZookeeperNodeOutputReference, "vm_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmSize", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HdinsightSparkClusterRolesZookeeperNode]:
        return typing.cast(typing.Optional[HdinsightSparkClusterRolesZookeeperNode], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterRolesZookeeperNode],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterRolesZookeeperNodeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterSecurityProfile",
    jsii_struct_bases=[],
    name_mapping={
        "aadds_resource_id": "aaddsResourceId",
        "domain_name": "domainName",
        "domain_username": "domainUsername",
        "domain_user_password": "domainUserPassword",
        "ldaps_urls": "ldapsUrls",
        "msi_resource_id": "msiResourceId",
        "cluster_users_group_dns": "clusterUsersGroupDns",
    },
)
class HdinsightSparkClusterSecurityProfile:
    def __init__(
        self,
        *,
        aadds_resource_id: builtins.str,
        domain_name: builtins.str,
        domain_username: builtins.str,
        domain_user_password: builtins.str,
        ldaps_urls: typing.Sequence[builtins.str],
        msi_resource_id: builtins.str,
        cluster_users_group_dns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param aadds_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#aadds_resource_id HdinsightSparkCluster#aadds_resource_id}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#domain_name HdinsightSparkCluster#domain_name}.
        :param domain_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#domain_username HdinsightSparkCluster#domain_username}.
        :param domain_user_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#domain_user_password HdinsightSparkCluster#domain_user_password}.
        :param ldaps_urls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#ldaps_urls HdinsightSparkCluster#ldaps_urls}.
        :param msi_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#msi_resource_id HdinsightSparkCluster#msi_resource_id}.
        :param cluster_users_group_dns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#cluster_users_group_dns HdinsightSparkCluster#cluster_users_group_dns}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterSecurityProfile.__init__)
            check_type(argname="argument aadds_resource_id", value=aadds_resource_id, expected_type=type_hints["aadds_resource_id"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument domain_username", value=domain_username, expected_type=type_hints["domain_username"])
            check_type(argname="argument domain_user_password", value=domain_user_password, expected_type=type_hints["domain_user_password"])
            check_type(argname="argument ldaps_urls", value=ldaps_urls, expected_type=type_hints["ldaps_urls"])
            check_type(argname="argument msi_resource_id", value=msi_resource_id, expected_type=type_hints["msi_resource_id"])
            check_type(argname="argument cluster_users_group_dns", value=cluster_users_group_dns, expected_type=type_hints["cluster_users_group_dns"])
        self._values: typing.Dict[str, typing.Any] = {
            "aadds_resource_id": aadds_resource_id,
            "domain_name": domain_name,
            "domain_username": domain_username,
            "domain_user_password": domain_user_password,
            "ldaps_urls": ldaps_urls,
            "msi_resource_id": msi_resource_id,
        }
        if cluster_users_group_dns is not None:
            self._values["cluster_users_group_dns"] = cluster_users_group_dns

    @builtins.property
    def aadds_resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#aadds_resource_id HdinsightSparkCluster#aadds_resource_id}.'''
        result = self._values.get("aadds_resource_id")
        assert result is not None, "Required property 'aadds_resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#domain_name HdinsightSparkCluster#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#domain_username HdinsightSparkCluster#domain_username}.'''
        result = self._values.get("domain_username")
        assert result is not None, "Required property 'domain_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_user_password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#domain_user_password HdinsightSparkCluster#domain_user_password}.'''
        result = self._values.get("domain_user_password")
        assert result is not None, "Required property 'domain_user_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ldaps_urls(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#ldaps_urls HdinsightSparkCluster#ldaps_urls}.'''
        result = self._values.get("ldaps_urls")
        assert result is not None, "Required property 'ldaps_urls' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def msi_resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#msi_resource_id HdinsightSparkCluster#msi_resource_id}.'''
        result = self._values.get("msi_resource_id")
        assert result is not None, "Required property 'msi_resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_users_group_dns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#cluster_users_group_dns HdinsightSparkCluster#cluster_users_group_dns}.'''
        result = self._values.get("cluster_users_group_dns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterSecurityProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterSecurityProfileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterSecurityProfileOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterSecurityProfileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClusterUsersGroupDns")
    def reset_cluster_users_group_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterUsersGroupDns", []))

    @builtins.property
    @jsii.member(jsii_name="aaddsResourceIdInput")
    def aadds_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aaddsResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterUsersGroupDnsInput")
    def cluster_users_group_dns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clusterUsersGroupDnsInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="domainUsernameInput")
    def domain_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="domainUserPasswordInput")
    def domain_user_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainUserPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="ldapsUrlsInput")
    def ldaps_urls_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ldapsUrlsInput"))

    @builtins.property
    @jsii.member(jsii_name="msiResourceIdInput")
    def msi_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "msiResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="aaddsResourceId")
    def aadds_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aaddsResourceId"))

    @aadds_resource_id.setter
    def aadds_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterSecurityProfileOutputReference, "aadds_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aaddsResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="clusterUsersGroupDns")
    def cluster_users_group_dns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "clusterUsersGroupDns"))

    @cluster_users_group_dns.setter
    def cluster_users_group_dns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterSecurityProfileOutputReference, "cluster_users_group_dns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterUsersGroupDns", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterSecurityProfileOutputReference, "domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="domainUsername")
    def domain_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainUsername"))

    @domain_username.setter
    def domain_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterSecurityProfileOutputReference, "domain_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainUsername", value)

    @builtins.property
    @jsii.member(jsii_name="domainUserPassword")
    def domain_user_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainUserPassword"))

    @domain_user_password.setter
    def domain_user_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterSecurityProfileOutputReference, "domain_user_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainUserPassword", value)

    @builtins.property
    @jsii.member(jsii_name="ldapsUrls")
    def ldaps_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ldapsUrls"))

    @ldaps_urls.setter
    def ldaps_urls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterSecurityProfileOutputReference, "ldaps_urls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ldapsUrls", value)

    @builtins.property
    @jsii.member(jsii_name="msiResourceId")
    def msi_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "msiResourceId"))

    @msi_resource_id.setter
    def msi_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterSecurityProfileOutputReference, "msi_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "msiResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HdinsightSparkClusterSecurityProfile]:
        return typing.cast(typing.Optional[HdinsightSparkClusterSecurityProfile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterSecurityProfile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterSecurityProfileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterStorageAccount",
    jsii_struct_bases=[],
    name_mapping={
        "is_default": "isDefault",
        "storage_account_key": "storageAccountKey",
        "storage_container_id": "storageContainerId",
        "storage_resource_id": "storageResourceId",
    },
)
class HdinsightSparkClusterStorageAccount:
    def __init__(
        self,
        *,
        is_default: typing.Union[builtins.bool, cdktf.IResolvable],
        storage_account_key: builtins.str,
        storage_container_id: builtins.str,
        storage_resource_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param is_default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#is_default HdinsightSparkCluster#is_default}.
        :param storage_account_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#storage_account_key HdinsightSparkCluster#storage_account_key}.
        :param storage_container_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#storage_container_id HdinsightSparkCluster#storage_container_id}.
        :param storage_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#storage_resource_id HdinsightSparkCluster#storage_resource_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterStorageAccount.__init__)
            check_type(argname="argument is_default", value=is_default, expected_type=type_hints["is_default"])
            check_type(argname="argument storage_account_key", value=storage_account_key, expected_type=type_hints["storage_account_key"])
            check_type(argname="argument storage_container_id", value=storage_container_id, expected_type=type_hints["storage_container_id"])
            check_type(argname="argument storage_resource_id", value=storage_resource_id, expected_type=type_hints["storage_resource_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "is_default": is_default,
            "storage_account_key": storage_account_key,
            "storage_container_id": storage_container_id,
        }
        if storage_resource_id is not None:
            self._values["storage_resource_id"] = storage_resource_id

    @builtins.property
    def is_default(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#is_default HdinsightSparkCluster#is_default}.'''
        result = self._values.get("is_default")
        assert result is not None, "Required property 'is_default' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def storage_account_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#storage_account_key HdinsightSparkCluster#storage_account_key}.'''
        result = self._values.get("storage_account_key")
        assert result is not None, "Required property 'storage_account_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_container_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#storage_container_id HdinsightSparkCluster#storage_container_id}.'''
        result = self._values.get("storage_container_id")
        assert result is not None, "Required property 'storage_container_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_resource_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#storage_resource_id HdinsightSparkCluster#storage_resource_id}.'''
        result = self._values.get("storage_resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterStorageAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterStorageAccountGen2",
    jsii_struct_bases=[],
    name_mapping={
        "filesystem_id": "filesystemId",
        "is_default": "isDefault",
        "managed_identity_resource_id": "managedIdentityResourceId",
        "storage_resource_id": "storageResourceId",
    },
)
class HdinsightSparkClusterStorageAccountGen2:
    def __init__(
        self,
        *,
        filesystem_id: builtins.str,
        is_default: typing.Union[builtins.bool, cdktf.IResolvable],
        managed_identity_resource_id: builtins.str,
        storage_resource_id: builtins.str,
    ) -> None:
        '''
        :param filesystem_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#filesystem_id HdinsightSparkCluster#filesystem_id}.
        :param is_default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#is_default HdinsightSparkCluster#is_default}.
        :param managed_identity_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#managed_identity_resource_id HdinsightSparkCluster#managed_identity_resource_id}.
        :param storage_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#storage_resource_id HdinsightSparkCluster#storage_resource_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterStorageAccountGen2.__init__)
            check_type(argname="argument filesystem_id", value=filesystem_id, expected_type=type_hints["filesystem_id"])
            check_type(argname="argument is_default", value=is_default, expected_type=type_hints["is_default"])
            check_type(argname="argument managed_identity_resource_id", value=managed_identity_resource_id, expected_type=type_hints["managed_identity_resource_id"])
            check_type(argname="argument storage_resource_id", value=storage_resource_id, expected_type=type_hints["storage_resource_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "filesystem_id": filesystem_id,
            "is_default": is_default,
            "managed_identity_resource_id": managed_identity_resource_id,
            "storage_resource_id": storage_resource_id,
        }

    @builtins.property
    def filesystem_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#filesystem_id HdinsightSparkCluster#filesystem_id}.'''
        result = self._values.get("filesystem_id")
        assert result is not None, "Required property 'filesystem_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def is_default(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#is_default HdinsightSparkCluster#is_default}.'''
        result = self._values.get("is_default")
        assert result is not None, "Required property 'is_default' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def managed_identity_resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#managed_identity_resource_id HdinsightSparkCluster#managed_identity_resource_id}.'''
        result = self._values.get("managed_identity_resource_id")
        assert result is not None, "Required property 'managed_identity_resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#storage_resource_id HdinsightSparkCluster#storage_resource_id}.'''
        result = self._values.get("storage_resource_id")
        assert result is not None, "Required property 'storage_resource_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterStorageAccountGen2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterStorageAccountGen2OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterStorageAccountGen2OutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterStorageAccountGen2OutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="filesystemIdInput")
    def filesystem_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filesystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="isDefaultInput")
    def is_default_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isDefaultInput"))

    @builtins.property
    @jsii.member(jsii_name="managedIdentityResourceIdInput")
    def managed_identity_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedIdentityResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="storageResourceIdInput")
    def storage_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="filesystemId")
    def filesystem_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filesystemId"))

    @filesystem_id.setter
    def filesystem_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterStorageAccountGen2OutputReference, "filesystem_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filesystemId", value)

    @builtins.property
    @jsii.member(jsii_name="isDefault")
    def is_default(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isDefault"))

    @is_default.setter
    def is_default(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterStorageAccountGen2OutputReference, "is_default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isDefault", value)

    @builtins.property
    @jsii.member(jsii_name="managedIdentityResourceId")
    def managed_identity_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedIdentityResourceId"))

    @managed_identity_resource_id.setter
    def managed_identity_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterStorageAccountGen2OutputReference, "managed_identity_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedIdentityResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="storageResourceId")
    def storage_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageResourceId"))

    @storage_resource_id.setter
    def storage_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterStorageAccountGen2OutputReference, "storage_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HdinsightSparkClusterStorageAccountGen2]:
        return typing.cast(typing.Optional[HdinsightSparkClusterStorageAccountGen2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HdinsightSparkClusterStorageAccountGen2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterStorageAccountGen2OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HdinsightSparkClusterStorageAccountList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterStorageAccountList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterStorageAccountList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HdinsightSparkClusterStorageAccountOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterStorageAccountList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HdinsightSparkClusterStorageAccountOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterStorageAccountList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterStorageAccountList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterStorageAccountList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HdinsightSparkClusterStorageAccount]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HdinsightSparkClusterStorageAccount]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HdinsightSparkClusterStorageAccount]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterStorageAccountList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HdinsightSparkClusterStorageAccountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterStorageAccountOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterStorageAccountOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetStorageResourceId")
    def reset_storage_resource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageResourceId", []))

    @builtins.property
    @jsii.member(jsii_name="isDefaultInput")
    def is_default_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isDefaultInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountKeyInput")
    def storage_account_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="storageContainerIdInput")
    def storage_container_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageContainerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="storageResourceIdInput")
    def storage_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="isDefault")
    def is_default(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isDefault"))

    @is_default.setter
    def is_default(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterStorageAccountOutputReference, "is_default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isDefault", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountKey")
    def storage_account_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountKey"))

    @storage_account_key.setter
    def storage_account_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterStorageAccountOutputReference, "storage_account_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountKey", value)

    @builtins.property
    @jsii.member(jsii_name="storageContainerId")
    def storage_container_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageContainerId"))

    @storage_container_id.setter
    def storage_container_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterStorageAccountOutputReference, "storage_container_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageContainerId", value)

    @builtins.property
    @jsii.member(jsii_name="storageResourceId")
    def storage_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageResourceId"))

    @storage_resource_id.setter
    def storage_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterStorageAccountOutputReference, "storage_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HdinsightSparkClusterStorageAccount, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HdinsightSparkClusterStorageAccount, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HdinsightSparkClusterStorageAccount, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterStorageAccountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class HdinsightSparkClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#create HdinsightSparkCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#delete HdinsightSparkCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#read HdinsightSparkCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#update HdinsightSparkCluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HdinsightSparkClusterTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#create HdinsightSparkCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#delete HdinsightSparkCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#read HdinsightSparkCluster#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/hdinsight_spark_cluster#update HdinsightSparkCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HdinsightSparkClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HdinsightSparkClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.hdinsightSparkCluster.HdinsightSparkClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(HdinsightSparkClusterTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HdinsightSparkClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HdinsightSparkClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HdinsightSparkClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HdinsightSparkClusterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "HdinsightSparkCluster",
    "HdinsightSparkClusterComponentVersion",
    "HdinsightSparkClusterComponentVersionOutputReference",
    "HdinsightSparkClusterConfig",
    "HdinsightSparkClusterDiskEncryption",
    "HdinsightSparkClusterDiskEncryptionList",
    "HdinsightSparkClusterDiskEncryptionOutputReference",
    "HdinsightSparkClusterExtension",
    "HdinsightSparkClusterExtensionOutputReference",
    "HdinsightSparkClusterGateway",
    "HdinsightSparkClusterGatewayOutputReference",
    "HdinsightSparkClusterMetastores",
    "HdinsightSparkClusterMetastoresAmbari",
    "HdinsightSparkClusterMetastoresAmbariOutputReference",
    "HdinsightSparkClusterMetastoresHive",
    "HdinsightSparkClusterMetastoresHiveOutputReference",
    "HdinsightSparkClusterMetastoresOozie",
    "HdinsightSparkClusterMetastoresOozieOutputReference",
    "HdinsightSparkClusterMetastoresOutputReference",
    "HdinsightSparkClusterMonitor",
    "HdinsightSparkClusterMonitorOutputReference",
    "HdinsightSparkClusterNetwork",
    "HdinsightSparkClusterNetworkOutputReference",
    "HdinsightSparkClusterRoles",
    "HdinsightSparkClusterRolesHeadNode",
    "HdinsightSparkClusterRolesHeadNodeOutputReference",
    "HdinsightSparkClusterRolesOutputReference",
    "HdinsightSparkClusterRolesWorkerNode",
    "HdinsightSparkClusterRolesWorkerNodeAutoscale",
    "HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacity",
    "HdinsightSparkClusterRolesWorkerNodeAutoscaleCapacityOutputReference",
    "HdinsightSparkClusterRolesWorkerNodeAutoscaleOutputReference",
    "HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrence",
    "HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceOutputReference",
    "HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceSchedule",
    "HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleList",
    "HdinsightSparkClusterRolesWorkerNodeAutoscaleRecurrenceScheduleOutputReference",
    "HdinsightSparkClusterRolesWorkerNodeOutputReference",
    "HdinsightSparkClusterRolesZookeeperNode",
    "HdinsightSparkClusterRolesZookeeperNodeOutputReference",
    "HdinsightSparkClusterSecurityProfile",
    "HdinsightSparkClusterSecurityProfileOutputReference",
    "HdinsightSparkClusterStorageAccount",
    "HdinsightSparkClusterStorageAccountGen2",
    "HdinsightSparkClusterStorageAccountGen2OutputReference",
    "HdinsightSparkClusterStorageAccountList",
    "HdinsightSparkClusterStorageAccountOutputReference",
    "HdinsightSparkClusterTimeouts",
    "HdinsightSparkClusterTimeoutsOutputReference",
]

publication.publish()
