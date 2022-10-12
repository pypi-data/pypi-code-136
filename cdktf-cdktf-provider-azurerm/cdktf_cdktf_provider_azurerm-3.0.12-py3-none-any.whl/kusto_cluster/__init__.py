'''
# `azurerm_kusto_cluster`

Refer to the Terraform Registory for docs: [`azurerm_kusto_cluster`](https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster).
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


class KustoCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kustoCluster.KustoCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster azurerm_kusto_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku: typing.Union["KustoClusterSku", typing.Dict[str, typing.Any]],
        allowed_fqdns: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        auto_stop_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disk_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        double_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        engine: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["KustoClusterIdentity", typing.Dict[str, typing.Any]]] = None,
        language_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
        optimized_auto_scale: typing.Optional[typing.Union["KustoClusterOptimizedAutoScale", typing.Dict[str, typing.Any]]] = None,
        outbound_network_access_restricted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        public_ip_type: typing.Optional[builtins.str] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        purge_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        streaming_ingestion_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KustoClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        trusted_external_tenants: typing.Optional[typing.Sequence[builtins.str]] = None,
        virtual_network_configuration: typing.Optional[typing.Union["KustoClusterVirtualNetworkConfiguration", typing.Dict[str, typing.Any]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster azurerm_kusto_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#location KustoCluster#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#name KustoCluster#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#resource_group_name KustoCluster#resource_group_name}.
        :param sku: sku block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#sku KustoCluster#sku}
        :param allowed_fqdns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#allowed_fqdns KustoCluster#allowed_fqdns}.
        :param allowed_ip_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#allowed_ip_ranges KustoCluster#allowed_ip_ranges}.
        :param auto_stop_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#auto_stop_enabled KustoCluster#auto_stop_enabled}.
        :param disk_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#disk_encryption_enabled KustoCluster#disk_encryption_enabled}.
        :param double_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#double_encryption_enabled KustoCluster#double_encryption_enabled}.
        :param engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#engine KustoCluster#engine}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#id KustoCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#identity KustoCluster#identity}
        :param language_extensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#language_extensions KustoCluster#language_extensions}.
        :param optimized_auto_scale: optimized_auto_scale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#optimized_auto_scale KustoCluster#optimized_auto_scale}
        :param outbound_network_access_restricted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#outbound_network_access_restricted KustoCluster#outbound_network_access_restricted}.
        :param public_ip_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#public_ip_type KustoCluster#public_ip_type}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#public_network_access_enabled KustoCluster#public_network_access_enabled}.
        :param purge_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#purge_enabled KustoCluster#purge_enabled}.
        :param streaming_ingestion_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#streaming_ingestion_enabled KustoCluster#streaming_ingestion_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#tags KustoCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#timeouts KustoCluster#timeouts}
        :param trusted_external_tenants: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#trusted_external_tenants KustoCluster#trusted_external_tenants}.
        :param virtual_network_configuration: virtual_network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#virtual_network_configuration KustoCluster#virtual_network_configuration}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#zones KustoCluster#zones}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KustoCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KustoClusterConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sku=sku,
            allowed_fqdns=allowed_fqdns,
            allowed_ip_ranges=allowed_ip_ranges,
            auto_stop_enabled=auto_stop_enabled,
            disk_encryption_enabled=disk_encryption_enabled,
            double_encryption_enabled=double_encryption_enabled,
            engine=engine,
            id=id,
            identity=identity,
            language_extensions=language_extensions,
            optimized_auto_scale=optimized_auto_scale,
            outbound_network_access_restricted=outbound_network_access_restricted,
            public_ip_type=public_ip_type,
            public_network_access_enabled=public_network_access_enabled,
            purge_enabled=purge_enabled,
            streaming_ingestion_enabled=streaming_ingestion_enabled,
            tags=tags,
            timeouts=timeouts,
            trusted_external_tenants=trusted_external_tenants,
            virtual_network_configuration=virtual_network_configuration,
            zones=zones,
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
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#type KustoCluster#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#identity_ids KustoCluster#identity_ids}.
        '''
        value = KustoClusterIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putOptimizedAutoScale")
    def put_optimized_auto_scale(
        self,
        *,
        maximum_instances: jsii.Number,
        minimum_instances: jsii.Number,
    ) -> None:
        '''
        :param maximum_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#maximum_instances KustoCluster#maximum_instances}.
        :param minimum_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#minimum_instances KustoCluster#minimum_instances}.
        '''
        value = KustoClusterOptimizedAutoScale(
            maximum_instances=maximum_instances, minimum_instances=minimum_instances
        )

        return typing.cast(None, jsii.invoke(self, "putOptimizedAutoScale", [value]))

    @jsii.member(jsii_name="putSku")
    def put_sku(
        self,
        *,
        name: builtins.str,
        capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#name KustoCluster#name}.
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#capacity KustoCluster#capacity}.
        '''
        value = KustoClusterSku(name=name, capacity=capacity)

        return typing.cast(None, jsii.invoke(self, "putSku", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#create KustoCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#delete KustoCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#read KustoCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#update KustoCluster#update}.
        '''
        value = KustoClusterTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVirtualNetworkConfiguration")
    def put_virtual_network_configuration(
        self,
        *,
        data_management_public_ip_id: builtins.str,
        engine_public_ip_id: builtins.str,
        subnet_id: builtins.str,
    ) -> None:
        '''
        :param data_management_public_ip_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#data_management_public_ip_id KustoCluster#data_management_public_ip_id}.
        :param engine_public_ip_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#engine_public_ip_id KustoCluster#engine_public_ip_id}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#subnet_id KustoCluster#subnet_id}.
        '''
        value = KustoClusterVirtualNetworkConfiguration(
            data_management_public_ip_id=data_management_public_ip_id,
            engine_public_ip_id=engine_public_ip_id,
            subnet_id=subnet_id,
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualNetworkConfiguration", [value]))

    @jsii.member(jsii_name="resetAllowedFqdns")
    def reset_allowed_fqdns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedFqdns", []))

    @jsii.member(jsii_name="resetAllowedIpRanges")
    def reset_allowed_ip_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedIpRanges", []))

    @jsii.member(jsii_name="resetAutoStopEnabled")
    def reset_auto_stop_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoStopEnabled", []))

    @jsii.member(jsii_name="resetDiskEncryptionEnabled")
    def reset_disk_encryption_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionEnabled", []))

    @jsii.member(jsii_name="resetDoubleEncryptionEnabled")
    def reset_double_encryption_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDoubleEncryptionEnabled", []))

    @jsii.member(jsii_name="resetEngine")
    def reset_engine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngine", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetLanguageExtensions")
    def reset_language_extensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLanguageExtensions", []))

    @jsii.member(jsii_name="resetOptimizedAutoScale")
    def reset_optimized_auto_scale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptimizedAutoScale", []))

    @jsii.member(jsii_name="resetOutboundNetworkAccessRestricted")
    def reset_outbound_network_access_restricted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutboundNetworkAccessRestricted", []))

    @jsii.member(jsii_name="resetPublicIpType")
    def reset_public_ip_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicIpType", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

    @jsii.member(jsii_name="resetPurgeEnabled")
    def reset_purge_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPurgeEnabled", []))

    @jsii.member(jsii_name="resetStreamingIngestionEnabled")
    def reset_streaming_ingestion_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreamingIngestionEnabled", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTrustedExternalTenants")
    def reset_trusted_external_tenants(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedExternalTenants", []))

    @jsii.member(jsii_name="resetVirtualNetworkConfiguration")
    def reset_virtual_network_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkConfiguration", []))

    @jsii.member(jsii_name="resetZones")
    def reset_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZones", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="dataIngestionUri")
    def data_ingestion_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataIngestionUri"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "KustoClusterIdentityOutputReference":
        return typing.cast("KustoClusterIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="optimizedAutoScale")
    def optimized_auto_scale(self) -> "KustoClusterOptimizedAutoScaleOutputReference":
        return typing.cast("KustoClusterOptimizedAutoScaleOutputReference", jsii.get(self, "optimizedAutoScale"))

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> "KustoClusterSkuOutputReference":
        return typing.cast("KustoClusterSkuOutputReference", jsii.get(self, "sku"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "KustoClusterTimeoutsOutputReference":
        return typing.cast("KustoClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkConfiguration")
    def virtual_network_configuration(
        self,
    ) -> "KustoClusterVirtualNetworkConfigurationOutputReference":
        return typing.cast("KustoClusterVirtualNetworkConfigurationOutputReference", jsii.get(self, "virtualNetworkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="allowedFqdnsInput")
    def allowed_fqdns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedFqdnsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedIpRangesInput")
    def allowed_ip_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedIpRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="autoStopEnabledInput")
    def auto_stop_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoStopEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionEnabledInput")
    def disk_encryption_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "diskEncryptionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="doubleEncryptionEnabledInput")
    def double_encryption_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "doubleEncryptionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="engineInput")
    def engine_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["KustoClusterIdentity"]:
        return typing.cast(typing.Optional["KustoClusterIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="languageExtensionsInput")
    def language_extensions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "languageExtensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optimizedAutoScaleInput")
    def optimized_auto_scale_input(
        self,
    ) -> typing.Optional["KustoClusterOptimizedAutoScale"]:
        return typing.cast(typing.Optional["KustoClusterOptimizedAutoScale"], jsii.get(self, "optimizedAutoScaleInput"))

    @builtins.property
    @jsii.member(jsii_name="outboundNetworkAccessRestrictedInput")
    def outbound_network_access_restricted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "outboundNetworkAccessRestrictedInput"))

    @builtins.property
    @jsii.member(jsii_name="publicIpTypeInput")
    def public_ip_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicIpTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabledInput")
    def public_network_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicNetworkAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="purgeEnabledInput")
    def purge_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "purgeEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional["KustoClusterSku"]:
        return typing.cast(typing.Optional["KustoClusterSku"], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="streamingIngestionEnabledInput")
    def streaming_ingestion_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "streamingIngestionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["KustoClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["KustoClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedExternalTenantsInput")
    def trusted_external_tenants_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "trustedExternalTenantsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkConfigurationInput")
    def virtual_network_configuration_input(
        self,
    ) -> typing.Optional["KustoClusterVirtualNetworkConfiguration"]:
        return typing.cast(typing.Optional["KustoClusterVirtualNetworkConfiguration"], jsii.get(self, "virtualNetworkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="zonesInput")
    def zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "zonesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedFqdns")
    def allowed_fqdns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedFqdns"))

    @allowed_fqdns.setter
    def allowed_fqdns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "allowed_fqdns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedFqdns", value)

    @builtins.property
    @jsii.member(jsii_name="allowedIpRanges")
    def allowed_ip_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedIpRanges"))

    @allowed_ip_ranges.setter
    def allowed_ip_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "allowed_ip_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedIpRanges", value)

    @builtins.property
    @jsii.member(jsii_name="autoStopEnabled")
    def auto_stop_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoStopEnabled"))

    @auto_stop_enabled.setter
    def auto_stop_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "auto_stop_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoStopEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionEnabled")
    def disk_encryption_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "diskEncryptionEnabled"))

    @disk_encryption_enabled.setter
    def disk_encryption_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "disk_encryption_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="doubleEncryptionEnabled")
    def double_encryption_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "doubleEncryptionEnabled"))

    @double_encryption_enabled.setter
    def double_encryption_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "double_encryption_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "doubleEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="engine")
    def engine(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "engine").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engine", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="languageExtensions")
    def language_extensions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "languageExtensions"))

    @language_extensions.setter
    def language_extensions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "language_extensions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageExtensions", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="outboundNetworkAccessRestricted")
    def outbound_network_access_restricted(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "outboundNetworkAccessRestricted"))

    @outbound_network_access_restricted.setter
    def outbound_network_access_restricted(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "outbound_network_access_restricted").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outboundNetworkAccessRestricted", value)

    @builtins.property
    @jsii.member(jsii_name="publicIpType")
    def public_ip_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpType"))

    @public_ip_type.setter
    def public_ip_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "public_ip_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicIpType", value)

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabled")
    def public_network_access_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publicNetworkAccessEnabled"))

    @public_network_access_enabled.setter
    def public_network_access_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="purgeEnabled")
    def purge_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "purgeEnabled"))

    @purge_enabled.setter
    def purge_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "purge_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "purgeEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="streamingIngestionEnabled")
    def streaming_ingestion_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "streamingIngestionEnabled"))

    @streaming_ingestion_enabled.setter
    def streaming_ingestion_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "streaming_ingestion_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamingIngestionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="trustedExternalTenants")
    def trusted_external_tenants(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "trustedExternalTenants"))

    @trusted_external_tenants.setter
    def trusted_external_tenants(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "trusted_external_tenants").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedExternalTenants", value)

    @builtins.property
    @jsii.member(jsii_name="zones")
    def zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "zones"))

    @zones.setter
    def zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoCluster, "zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zones", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kustoCluster.KustoClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "sku": "sku",
        "allowed_fqdns": "allowedFqdns",
        "allowed_ip_ranges": "allowedIpRanges",
        "auto_stop_enabled": "autoStopEnabled",
        "disk_encryption_enabled": "diskEncryptionEnabled",
        "double_encryption_enabled": "doubleEncryptionEnabled",
        "engine": "engine",
        "id": "id",
        "identity": "identity",
        "language_extensions": "languageExtensions",
        "optimized_auto_scale": "optimizedAutoScale",
        "outbound_network_access_restricted": "outboundNetworkAccessRestricted",
        "public_ip_type": "publicIpType",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "purge_enabled": "purgeEnabled",
        "streaming_ingestion_enabled": "streamingIngestionEnabled",
        "tags": "tags",
        "timeouts": "timeouts",
        "trusted_external_tenants": "trustedExternalTenants",
        "virtual_network_configuration": "virtualNetworkConfiguration",
        "zones": "zones",
    },
)
class KustoClusterConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku: typing.Union["KustoClusterSku", typing.Dict[str, typing.Any]],
        allowed_fqdns: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        auto_stop_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disk_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        double_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        engine: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["KustoClusterIdentity", typing.Dict[str, typing.Any]]] = None,
        language_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
        optimized_auto_scale: typing.Optional[typing.Union["KustoClusterOptimizedAutoScale", typing.Dict[str, typing.Any]]] = None,
        outbound_network_access_restricted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        public_ip_type: typing.Optional[builtins.str] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        purge_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        streaming_ingestion_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KustoClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        trusted_external_tenants: typing.Optional[typing.Sequence[builtins.str]] = None,
        virtual_network_configuration: typing.Optional[typing.Union["KustoClusterVirtualNetworkConfiguration", typing.Dict[str, typing.Any]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#location KustoCluster#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#name KustoCluster#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#resource_group_name KustoCluster#resource_group_name}.
        :param sku: sku block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#sku KustoCluster#sku}
        :param allowed_fqdns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#allowed_fqdns KustoCluster#allowed_fqdns}.
        :param allowed_ip_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#allowed_ip_ranges KustoCluster#allowed_ip_ranges}.
        :param auto_stop_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#auto_stop_enabled KustoCluster#auto_stop_enabled}.
        :param disk_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#disk_encryption_enabled KustoCluster#disk_encryption_enabled}.
        :param double_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#double_encryption_enabled KustoCluster#double_encryption_enabled}.
        :param engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#engine KustoCluster#engine}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#id KustoCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#identity KustoCluster#identity}
        :param language_extensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#language_extensions KustoCluster#language_extensions}.
        :param optimized_auto_scale: optimized_auto_scale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#optimized_auto_scale KustoCluster#optimized_auto_scale}
        :param outbound_network_access_restricted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#outbound_network_access_restricted KustoCluster#outbound_network_access_restricted}.
        :param public_ip_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#public_ip_type KustoCluster#public_ip_type}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#public_network_access_enabled KustoCluster#public_network_access_enabled}.
        :param purge_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#purge_enabled KustoCluster#purge_enabled}.
        :param streaming_ingestion_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#streaming_ingestion_enabled KustoCluster#streaming_ingestion_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#tags KustoCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#timeouts KustoCluster#timeouts}
        :param trusted_external_tenants: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#trusted_external_tenants KustoCluster#trusted_external_tenants}.
        :param virtual_network_configuration: virtual_network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#virtual_network_configuration KustoCluster#virtual_network_configuration}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#zones KustoCluster#zones}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(sku, dict):
            sku = KustoClusterSku(**sku)
        if isinstance(identity, dict):
            identity = KustoClusterIdentity(**identity)
        if isinstance(optimized_auto_scale, dict):
            optimized_auto_scale = KustoClusterOptimizedAutoScale(**optimized_auto_scale)
        if isinstance(timeouts, dict):
            timeouts = KustoClusterTimeouts(**timeouts)
        if isinstance(virtual_network_configuration, dict):
            virtual_network_configuration = KustoClusterVirtualNetworkConfiguration(**virtual_network_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(KustoClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument allowed_fqdns", value=allowed_fqdns, expected_type=type_hints["allowed_fqdns"])
            check_type(argname="argument allowed_ip_ranges", value=allowed_ip_ranges, expected_type=type_hints["allowed_ip_ranges"])
            check_type(argname="argument auto_stop_enabled", value=auto_stop_enabled, expected_type=type_hints["auto_stop_enabled"])
            check_type(argname="argument disk_encryption_enabled", value=disk_encryption_enabled, expected_type=type_hints["disk_encryption_enabled"])
            check_type(argname="argument double_encryption_enabled", value=double_encryption_enabled, expected_type=type_hints["double_encryption_enabled"])
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument language_extensions", value=language_extensions, expected_type=type_hints["language_extensions"])
            check_type(argname="argument optimized_auto_scale", value=optimized_auto_scale, expected_type=type_hints["optimized_auto_scale"])
            check_type(argname="argument outbound_network_access_restricted", value=outbound_network_access_restricted, expected_type=type_hints["outbound_network_access_restricted"])
            check_type(argname="argument public_ip_type", value=public_ip_type, expected_type=type_hints["public_ip_type"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument purge_enabled", value=purge_enabled, expected_type=type_hints["purge_enabled"])
            check_type(argname="argument streaming_ingestion_enabled", value=streaming_ingestion_enabled, expected_type=type_hints["streaming_ingestion_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument trusted_external_tenants", value=trusted_external_tenants, expected_type=type_hints["trusted_external_tenants"])
            check_type(argname="argument virtual_network_configuration", value=virtual_network_configuration, expected_type=type_hints["virtual_network_configuration"])
            check_type(argname="argument zones", value=zones, expected_type=type_hints["zones"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku": sku,
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
        if allowed_fqdns is not None:
            self._values["allowed_fqdns"] = allowed_fqdns
        if allowed_ip_ranges is not None:
            self._values["allowed_ip_ranges"] = allowed_ip_ranges
        if auto_stop_enabled is not None:
            self._values["auto_stop_enabled"] = auto_stop_enabled
        if disk_encryption_enabled is not None:
            self._values["disk_encryption_enabled"] = disk_encryption_enabled
        if double_encryption_enabled is not None:
            self._values["double_encryption_enabled"] = double_encryption_enabled
        if engine is not None:
            self._values["engine"] = engine
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if language_extensions is not None:
            self._values["language_extensions"] = language_extensions
        if optimized_auto_scale is not None:
            self._values["optimized_auto_scale"] = optimized_auto_scale
        if outbound_network_access_restricted is not None:
            self._values["outbound_network_access_restricted"] = outbound_network_access_restricted
        if public_ip_type is not None:
            self._values["public_ip_type"] = public_ip_type
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
        if purge_enabled is not None:
            self._values["purge_enabled"] = purge_enabled
        if streaming_ingestion_enabled is not None:
            self._values["streaming_ingestion_enabled"] = streaming_ingestion_enabled
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if trusted_external_tenants is not None:
            self._values["trusted_external_tenants"] = trusted_external_tenants
        if virtual_network_configuration is not None:
            self._values["virtual_network_configuration"] = virtual_network_configuration
        if zones is not None:
            self._values["zones"] = zones

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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#location KustoCluster#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#name KustoCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#resource_group_name KustoCluster#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> "KustoClusterSku":
        '''sku block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#sku KustoCluster#sku}
        '''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast("KustoClusterSku", result)

    @builtins.property
    def allowed_fqdns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#allowed_fqdns KustoCluster#allowed_fqdns}.'''
        result = self._values.get("allowed_fqdns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_ip_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#allowed_ip_ranges KustoCluster#allowed_ip_ranges}.'''
        result = self._values.get("allowed_ip_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def auto_stop_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#auto_stop_enabled KustoCluster#auto_stop_enabled}.'''
        result = self._values.get("auto_stop_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def disk_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#disk_encryption_enabled KustoCluster#disk_encryption_enabled}.'''
        result = self._values.get("disk_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def double_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#double_encryption_enabled KustoCluster#double_encryption_enabled}.'''
        result = self._values.get("double_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def engine(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#engine KustoCluster#engine}.'''
        result = self._values.get("engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#id KustoCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["KustoClusterIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#identity KustoCluster#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["KustoClusterIdentity"], result)

    @builtins.property
    def language_extensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#language_extensions KustoCluster#language_extensions}.'''
        result = self._values.get("language_extensions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def optimized_auto_scale(self) -> typing.Optional["KustoClusterOptimizedAutoScale"]:
        '''optimized_auto_scale block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#optimized_auto_scale KustoCluster#optimized_auto_scale}
        '''
        result = self._values.get("optimized_auto_scale")
        return typing.cast(typing.Optional["KustoClusterOptimizedAutoScale"], result)

    @builtins.property
    def outbound_network_access_restricted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#outbound_network_access_restricted KustoCluster#outbound_network_access_restricted}.'''
        result = self._values.get("outbound_network_access_restricted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def public_ip_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#public_ip_type KustoCluster#public_ip_type}.'''
        result = self._values.get("public_ip_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#public_network_access_enabled KustoCluster#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def purge_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#purge_enabled KustoCluster#purge_enabled}.'''
        result = self._values.get("purge_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def streaming_ingestion_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#streaming_ingestion_enabled KustoCluster#streaming_ingestion_enabled}.'''
        result = self._values.get("streaming_ingestion_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#tags KustoCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["KustoClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#timeouts KustoCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["KustoClusterTimeouts"], result)

    @builtins.property
    def trusted_external_tenants(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#trusted_external_tenants KustoCluster#trusted_external_tenants}.'''
        result = self._values.get("trusted_external_tenants")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def virtual_network_configuration(
        self,
    ) -> typing.Optional["KustoClusterVirtualNetworkConfiguration"]:
        '''virtual_network_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#virtual_network_configuration KustoCluster#virtual_network_configuration}
        '''
        result = self._values.get("virtual_network_configuration")
        return typing.cast(typing.Optional["KustoClusterVirtualNetworkConfiguration"], result)

    @builtins.property
    def zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#zones KustoCluster#zones}.'''
        result = self._values.get("zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustoClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kustoCluster.KustoClusterIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class KustoClusterIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#type KustoCluster#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#identity_ids KustoCluster#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KustoClusterIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#type KustoCluster#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#identity_ids KustoCluster#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustoClusterIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KustoClusterIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kustoCluster.KustoClusterIdentityOutputReference",
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
            type_hints = typing.get_type_hints(KustoClusterIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdentityIds")
    def reset_identity_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityIds", []))

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="identityIdsInput")
    def identity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIds")
    def identity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityIds"))

    @identity_ids.setter
    def identity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KustoClusterIdentity]:
        return typing.cast(typing.Optional[KustoClusterIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[KustoClusterIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kustoCluster.KustoClusterOptimizedAutoScale",
    jsii_struct_bases=[],
    name_mapping={
        "maximum_instances": "maximumInstances",
        "minimum_instances": "minimumInstances",
    },
)
class KustoClusterOptimizedAutoScale:
    def __init__(
        self,
        *,
        maximum_instances: jsii.Number,
        minimum_instances: jsii.Number,
    ) -> None:
        '''
        :param maximum_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#maximum_instances KustoCluster#maximum_instances}.
        :param minimum_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#minimum_instances KustoCluster#minimum_instances}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KustoClusterOptimizedAutoScale.__init__)
            check_type(argname="argument maximum_instances", value=maximum_instances, expected_type=type_hints["maximum_instances"])
            check_type(argname="argument minimum_instances", value=minimum_instances, expected_type=type_hints["minimum_instances"])
        self._values: typing.Dict[str, typing.Any] = {
            "maximum_instances": maximum_instances,
            "minimum_instances": minimum_instances,
        }

    @builtins.property
    def maximum_instances(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#maximum_instances KustoCluster#maximum_instances}.'''
        result = self._values.get("maximum_instances")
        assert result is not None, "Required property 'maximum_instances' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def minimum_instances(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#minimum_instances KustoCluster#minimum_instances}.'''
        result = self._values.get("minimum_instances")
        assert result is not None, "Required property 'minimum_instances' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustoClusterOptimizedAutoScale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KustoClusterOptimizedAutoScaleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kustoCluster.KustoClusterOptimizedAutoScaleOutputReference",
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
            type_hints = typing.get_type_hints(KustoClusterOptimizedAutoScaleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maximumInstancesInput")
    def maximum_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumInstancesInput")
    def minimum_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumInstances")
    def maximum_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumInstances"))

    @maximum_instances.setter
    def maximum_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterOptimizedAutoScaleOutputReference, "maximum_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumInstances", value)

    @builtins.property
    @jsii.member(jsii_name="minimumInstances")
    def minimum_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumInstances"))

    @minimum_instances.setter
    def minimum_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterOptimizedAutoScaleOutputReference, "minimum_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumInstances", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KustoClusterOptimizedAutoScale]:
        return typing.cast(typing.Optional[KustoClusterOptimizedAutoScale], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KustoClusterOptimizedAutoScale],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterOptimizedAutoScaleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kustoCluster.KustoClusterSku",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "capacity": "capacity"},
)
class KustoClusterSku:
    def __init__(
        self,
        *,
        name: builtins.str,
        capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#name KustoCluster#name}.
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#capacity KustoCluster#capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KustoClusterSku.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if capacity is not None:
            self._values["capacity"] = capacity

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#name KustoCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#capacity KustoCluster#capacity}.'''
        result = self._values.get("capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustoClusterSku(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KustoClusterSkuOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kustoCluster.KustoClusterSkuOutputReference",
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
            type_hints = typing.get_type_hints(KustoClusterSkuOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCapacity")
    def reset_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterSkuOutputReference, "capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterSkuOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KustoClusterSku]:
        return typing.cast(typing.Optional[KustoClusterSku], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[KustoClusterSku]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterSkuOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kustoCluster.KustoClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class KustoClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#create KustoCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#delete KustoCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#read KustoCluster#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#update KustoCluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KustoClusterTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#create KustoCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#delete KustoCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#read KustoCluster#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#update KustoCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustoClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KustoClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kustoCluster.KustoClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(KustoClusterTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(KustoClusterTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KustoClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KustoClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KustoClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.kustoCluster.KustoClusterVirtualNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "data_management_public_ip_id": "dataManagementPublicIpId",
        "engine_public_ip_id": "enginePublicIpId",
        "subnet_id": "subnetId",
    },
)
class KustoClusterVirtualNetworkConfiguration:
    def __init__(
        self,
        *,
        data_management_public_ip_id: builtins.str,
        engine_public_ip_id: builtins.str,
        subnet_id: builtins.str,
    ) -> None:
        '''
        :param data_management_public_ip_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#data_management_public_ip_id KustoCluster#data_management_public_ip_id}.
        :param engine_public_ip_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#engine_public_ip_id KustoCluster#engine_public_ip_id}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#subnet_id KustoCluster#subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KustoClusterVirtualNetworkConfiguration.__init__)
            check_type(argname="argument data_management_public_ip_id", value=data_management_public_ip_id, expected_type=type_hints["data_management_public_ip_id"])
            check_type(argname="argument engine_public_ip_id", value=engine_public_ip_id, expected_type=type_hints["engine_public_ip_id"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_management_public_ip_id": data_management_public_ip_id,
            "engine_public_ip_id": engine_public_ip_id,
            "subnet_id": subnet_id,
        }

    @builtins.property
    def data_management_public_ip_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#data_management_public_ip_id KustoCluster#data_management_public_ip_id}.'''
        result = self._values.get("data_management_public_ip_id")
        assert result is not None, "Required property 'data_management_public_ip_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_public_ip_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#engine_public_ip_id KustoCluster#engine_public_ip_id}.'''
        result = self._values.get("engine_public_ip_id")
        assert result is not None, "Required property 'engine_public_ip_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/kusto_cluster#subnet_id KustoCluster#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KustoClusterVirtualNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KustoClusterVirtualNetworkConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.kustoCluster.KustoClusterVirtualNetworkConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(KustoClusterVirtualNetworkConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dataManagementPublicIpIdInput")
    def data_management_public_ip_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataManagementPublicIpIdInput"))

    @builtins.property
    @jsii.member(jsii_name="enginePublicIpIdInput")
    def engine_public_ip_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enginePublicIpIdInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dataManagementPublicIpId")
    def data_management_public_ip_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataManagementPublicIpId"))

    @data_management_public_ip_id.setter
    def data_management_public_ip_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterVirtualNetworkConfigurationOutputReference, "data_management_public_ip_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataManagementPublicIpId", value)

    @builtins.property
    @jsii.member(jsii_name="enginePublicIpId")
    def engine_public_ip_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enginePublicIpId"))

    @engine_public_ip_id.setter
    def engine_public_ip_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterVirtualNetworkConfigurationOutputReference, "engine_public_ip_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enginePublicIpId", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterVirtualNetworkConfigurationOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KustoClusterVirtualNetworkConfiguration]:
        return typing.cast(typing.Optional[KustoClusterVirtualNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KustoClusterVirtualNetworkConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KustoClusterVirtualNetworkConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KustoCluster",
    "KustoClusterConfig",
    "KustoClusterIdentity",
    "KustoClusterIdentityOutputReference",
    "KustoClusterOptimizedAutoScale",
    "KustoClusterOptimizedAutoScaleOutputReference",
    "KustoClusterSku",
    "KustoClusterSkuOutputReference",
    "KustoClusterTimeouts",
    "KustoClusterTimeoutsOutputReference",
    "KustoClusterVirtualNetworkConfiguration",
    "KustoClusterVirtualNetworkConfigurationOutputReference",
]

publication.publish()
