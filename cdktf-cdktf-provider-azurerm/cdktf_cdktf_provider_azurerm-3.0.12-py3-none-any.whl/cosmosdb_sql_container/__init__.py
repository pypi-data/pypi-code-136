'''
# `azurerm_cosmosdb_sql_container`

Refer to the Terraform Registory for docs: [`azurerm_cosmosdb_sql_container`](https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container).
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


class CosmosdbSqlContainer(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container azurerm_cosmosdb_sql_container}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        account_name: builtins.str,
        database_name: builtins.str,
        name: builtins.str,
        partition_key_path: builtins.str,
        resource_group_name: builtins.str,
        analytical_storage_ttl: typing.Optional[jsii.Number] = None,
        autoscale_settings: typing.Optional[typing.Union["CosmosdbSqlContainerAutoscaleSettings", typing.Dict[str, typing.Any]]] = None,
        conflict_resolution_policy: typing.Optional[typing.Union["CosmosdbSqlContainerConflictResolutionPolicy", typing.Dict[str, typing.Any]]] = None,
        default_ttl: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        indexing_policy: typing.Optional[typing.Union["CosmosdbSqlContainerIndexingPolicy", typing.Dict[str, typing.Any]]] = None,
        partition_key_version: typing.Optional[jsii.Number] = None,
        throughput: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["CosmosdbSqlContainerTimeouts", typing.Dict[str, typing.Any]]] = None,
        unique_key: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbSqlContainerUniqueKey", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container azurerm_cosmosdb_sql_container} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#account_name CosmosdbSqlContainer#account_name}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#database_name CosmosdbSqlContainer#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#name CosmosdbSqlContainer#name}.
        :param partition_key_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#partition_key_path CosmosdbSqlContainer#partition_key_path}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#resource_group_name CosmosdbSqlContainer#resource_group_name}.
        :param analytical_storage_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#analytical_storage_ttl CosmosdbSqlContainer#analytical_storage_ttl}.
        :param autoscale_settings: autoscale_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#autoscale_settings CosmosdbSqlContainer#autoscale_settings}
        :param conflict_resolution_policy: conflict_resolution_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#conflict_resolution_policy CosmosdbSqlContainer#conflict_resolution_policy}
        :param default_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#default_ttl CosmosdbSqlContainer#default_ttl}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#id CosmosdbSqlContainer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param indexing_policy: indexing_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#indexing_policy CosmosdbSqlContainer#indexing_policy}
        :param partition_key_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#partition_key_version CosmosdbSqlContainer#partition_key_version}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#throughput CosmosdbSqlContainer#throughput}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#timeouts CosmosdbSqlContainer#timeouts}
        :param unique_key: unique_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#unique_key CosmosdbSqlContainer#unique_key}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainer.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CosmosdbSqlContainerConfig(
            account_name=account_name,
            database_name=database_name,
            name=name,
            partition_key_path=partition_key_path,
            resource_group_name=resource_group_name,
            analytical_storage_ttl=analytical_storage_ttl,
            autoscale_settings=autoscale_settings,
            conflict_resolution_policy=conflict_resolution_policy,
            default_ttl=default_ttl,
            id=id,
            indexing_policy=indexing_policy,
            partition_key_version=partition_key_version,
            throughput=throughput,
            timeouts=timeouts,
            unique_key=unique_key,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAutoscaleSettings")
    def put_autoscale_settings(
        self,
        *,
        max_throughput: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#max_throughput CosmosdbSqlContainer#max_throughput}.
        '''
        value = CosmosdbSqlContainerAutoscaleSettings(max_throughput=max_throughput)

        return typing.cast(None, jsii.invoke(self, "putAutoscaleSettings", [value]))

    @jsii.member(jsii_name="putConflictResolutionPolicy")
    def put_conflict_resolution_policy(
        self,
        *,
        mode: builtins.str,
        conflict_resolution_path: typing.Optional[builtins.str] = None,
        conflict_resolution_procedure: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#mode CosmosdbSqlContainer#mode}.
        :param conflict_resolution_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#conflict_resolution_path CosmosdbSqlContainer#conflict_resolution_path}.
        :param conflict_resolution_procedure: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#conflict_resolution_procedure CosmosdbSqlContainer#conflict_resolution_procedure}.
        '''
        value = CosmosdbSqlContainerConflictResolutionPolicy(
            mode=mode,
            conflict_resolution_path=conflict_resolution_path,
            conflict_resolution_procedure=conflict_resolution_procedure,
        )

        return typing.cast(None, jsii.invoke(self, "putConflictResolutionPolicy", [value]))

    @jsii.member(jsii_name="putIndexingPolicy")
    def put_indexing_policy(
        self,
        *,
        composite_index: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbSqlContainerIndexingPolicyCompositeIndex", typing.Dict[str, typing.Any]]]]] = None,
        excluded_path: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbSqlContainerIndexingPolicyExcludedPath", typing.Dict[str, typing.Any]]]]] = None,
        included_path: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbSqlContainerIndexingPolicyIncludedPath", typing.Dict[str, typing.Any]]]]] = None,
        indexing_mode: typing.Optional[builtins.str] = None,
        spatial_index: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbSqlContainerIndexingPolicySpatialIndex", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param composite_index: composite_index block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#composite_index CosmosdbSqlContainer#composite_index}
        :param excluded_path: excluded_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#excluded_path CosmosdbSqlContainer#excluded_path}
        :param included_path: included_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#included_path CosmosdbSqlContainer#included_path}
        :param indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#indexing_mode CosmosdbSqlContainer#indexing_mode}.
        :param spatial_index: spatial_index block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#spatial_index CosmosdbSqlContainer#spatial_index}
        '''
        value = CosmosdbSqlContainerIndexingPolicy(
            composite_index=composite_index,
            excluded_path=excluded_path,
            included_path=included_path,
            indexing_mode=indexing_mode,
            spatial_index=spatial_index,
        )

        return typing.cast(None, jsii.invoke(self, "putIndexingPolicy", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#create CosmosdbSqlContainer#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#delete CosmosdbSqlContainer#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#read CosmosdbSqlContainer#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#update CosmosdbSqlContainer#update}.
        '''
        value = CosmosdbSqlContainerTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putUniqueKey")
    def put_unique_key(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbSqlContainerUniqueKey", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainer.put_unique_key)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUniqueKey", [value]))

    @jsii.member(jsii_name="resetAnalyticalStorageTtl")
    def reset_analytical_storage_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnalyticalStorageTtl", []))

    @jsii.member(jsii_name="resetAutoscaleSettings")
    def reset_autoscale_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaleSettings", []))

    @jsii.member(jsii_name="resetConflictResolutionPolicy")
    def reset_conflict_resolution_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConflictResolutionPolicy", []))

    @jsii.member(jsii_name="resetDefaultTtl")
    def reset_default_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTtl", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIndexingPolicy")
    def reset_indexing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIndexingPolicy", []))

    @jsii.member(jsii_name="resetPartitionKeyVersion")
    def reset_partition_key_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionKeyVersion", []))

    @jsii.member(jsii_name="resetThroughput")
    def reset_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThroughput", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUniqueKey")
    def reset_unique_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUniqueKey", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleSettings")
    def autoscale_settings(
        self,
    ) -> "CosmosdbSqlContainerAutoscaleSettingsOutputReference":
        return typing.cast("CosmosdbSqlContainerAutoscaleSettingsOutputReference", jsii.get(self, "autoscaleSettings"))

    @builtins.property
    @jsii.member(jsii_name="conflictResolutionPolicy")
    def conflict_resolution_policy(
        self,
    ) -> "CosmosdbSqlContainerConflictResolutionPolicyOutputReference":
        return typing.cast("CosmosdbSqlContainerConflictResolutionPolicyOutputReference", jsii.get(self, "conflictResolutionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="indexingPolicy")
    def indexing_policy(self) -> "CosmosdbSqlContainerIndexingPolicyOutputReference":
        return typing.cast("CosmosdbSqlContainerIndexingPolicyOutputReference", jsii.get(self, "indexingPolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CosmosdbSqlContainerTimeoutsOutputReference":
        return typing.cast("CosmosdbSqlContainerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="uniqueKey")
    def unique_key(self) -> "CosmosdbSqlContainerUniqueKeyList":
        return typing.cast("CosmosdbSqlContainerUniqueKeyList", jsii.get(self, "uniqueKey"))

    @builtins.property
    @jsii.member(jsii_name="accountNameInput")
    def account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="analyticalStorageTtlInput")
    def analytical_storage_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "analyticalStorageTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleSettingsInput")
    def autoscale_settings_input(
        self,
    ) -> typing.Optional["CosmosdbSqlContainerAutoscaleSettings"]:
        return typing.cast(typing.Optional["CosmosdbSqlContainerAutoscaleSettings"], jsii.get(self, "autoscaleSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="conflictResolutionPolicyInput")
    def conflict_resolution_policy_input(
        self,
    ) -> typing.Optional["CosmosdbSqlContainerConflictResolutionPolicy"]:
        return typing.cast(typing.Optional["CosmosdbSqlContainerConflictResolutionPolicy"], jsii.get(self, "conflictResolutionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTtlInput")
    def default_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="indexingPolicyInput")
    def indexing_policy_input(
        self,
    ) -> typing.Optional["CosmosdbSqlContainerIndexingPolicy"]:
        return typing.cast(typing.Optional["CosmosdbSqlContainerIndexingPolicy"], jsii.get(self, "indexingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionKeyPathInput")
    def partition_key_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionKeyPathInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionKeyVersionInput")
    def partition_key_version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partitionKeyVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="throughputInput")
    def throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throughputInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["CosmosdbSqlContainerTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["CosmosdbSqlContainerTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="uniqueKeyInput")
    def unique_key_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerUniqueKey"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerUniqueKey"]]], jsii.get(self, "uniqueKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accountName")
    def account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountName"))

    @account_name.setter
    def account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainer, "account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountName", value)

    @builtins.property
    @jsii.member(jsii_name="analyticalStorageTtl")
    def analytical_storage_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "analyticalStorageTtl"))

    @analytical_storage_ttl.setter
    def analytical_storage_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainer, "analytical_storage_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "analyticalStorageTtl", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainer, "database_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTtl")
    def default_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultTtl"))

    @default_ttl.setter
    def default_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainer, "default_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTtl", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainer, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainer, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="partitionKeyPath")
    def partition_key_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partitionKeyPath"))

    @partition_key_path.setter
    def partition_key_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainer, "partition_key_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionKeyPath", value)

    @builtins.property
    @jsii.member(jsii_name="partitionKeyVersion")
    def partition_key_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "partitionKeyVersion"))

    @partition_key_version.setter
    def partition_key_version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainer, "partition_key_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionKeyVersion", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainer, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainer, "throughput").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerAutoscaleSettings",
    jsii_struct_bases=[],
    name_mapping={"max_throughput": "maxThroughput"},
)
class CosmosdbSqlContainerAutoscaleSettings:
    def __init__(self, *, max_throughput: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param max_throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#max_throughput CosmosdbSqlContainer#max_throughput}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerAutoscaleSettings.__init__)
            check_type(argname="argument max_throughput", value=max_throughput, expected_type=type_hints["max_throughput"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_throughput is not None:
            self._values["max_throughput"] = max_throughput

    @builtins.property
    def max_throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#max_throughput CosmosdbSqlContainer#max_throughput}.'''
        result = self._values.get("max_throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbSqlContainerAutoscaleSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbSqlContainerAutoscaleSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerAutoscaleSettingsOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerAutoscaleSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxThroughput")
    def reset_max_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxThroughput", []))

    @builtins.property
    @jsii.member(jsii_name="maxThroughputInput")
    def max_throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxThroughputInput"))

    @builtins.property
    @jsii.member(jsii_name="maxThroughput")
    def max_throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxThroughput"))

    @max_throughput.setter
    def max_throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerAutoscaleSettingsOutputReference, "max_throughput").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxThroughput", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CosmosdbSqlContainerAutoscaleSettings]:
        return typing.cast(typing.Optional[CosmosdbSqlContainerAutoscaleSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CosmosdbSqlContainerAutoscaleSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerAutoscaleSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_name": "accountName",
        "database_name": "databaseName",
        "name": "name",
        "partition_key_path": "partitionKeyPath",
        "resource_group_name": "resourceGroupName",
        "analytical_storage_ttl": "analyticalStorageTtl",
        "autoscale_settings": "autoscaleSettings",
        "conflict_resolution_policy": "conflictResolutionPolicy",
        "default_ttl": "defaultTtl",
        "id": "id",
        "indexing_policy": "indexingPolicy",
        "partition_key_version": "partitionKeyVersion",
        "throughput": "throughput",
        "timeouts": "timeouts",
        "unique_key": "uniqueKey",
    },
)
class CosmosdbSqlContainerConfig(cdktf.TerraformMetaArguments):
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
        account_name: builtins.str,
        database_name: builtins.str,
        name: builtins.str,
        partition_key_path: builtins.str,
        resource_group_name: builtins.str,
        analytical_storage_ttl: typing.Optional[jsii.Number] = None,
        autoscale_settings: typing.Optional[typing.Union[CosmosdbSqlContainerAutoscaleSettings, typing.Dict[str, typing.Any]]] = None,
        conflict_resolution_policy: typing.Optional[typing.Union["CosmosdbSqlContainerConflictResolutionPolicy", typing.Dict[str, typing.Any]]] = None,
        default_ttl: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        indexing_policy: typing.Optional[typing.Union["CosmosdbSqlContainerIndexingPolicy", typing.Dict[str, typing.Any]]] = None,
        partition_key_version: typing.Optional[jsii.Number] = None,
        throughput: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["CosmosdbSqlContainerTimeouts", typing.Dict[str, typing.Any]]] = None,
        unique_key: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbSqlContainerUniqueKey", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#account_name CosmosdbSqlContainer#account_name}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#database_name CosmosdbSqlContainer#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#name CosmosdbSqlContainer#name}.
        :param partition_key_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#partition_key_path CosmosdbSqlContainer#partition_key_path}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#resource_group_name CosmosdbSqlContainer#resource_group_name}.
        :param analytical_storage_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#analytical_storage_ttl CosmosdbSqlContainer#analytical_storage_ttl}.
        :param autoscale_settings: autoscale_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#autoscale_settings CosmosdbSqlContainer#autoscale_settings}
        :param conflict_resolution_policy: conflict_resolution_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#conflict_resolution_policy CosmosdbSqlContainer#conflict_resolution_policy}
        :param default_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#default_ttl CosmosdbSqlContainer#default_ttl}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#id CosmosdbSqlContainer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param indexing_policy: indexing_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#indexing_policy CosmosdbSqlContainer#indexing_policy}
        :param partition_key_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#partition_key_version CosmosdbSqlContainer#partition_key_version}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#throughput CosmosdbSqlContainer#throughput}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#timeouts CosmosdbSqlContainer#timeouts}
        :param unique_key: unique_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#unique_key CosmosdbSqlContainer#unique_key}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(autoscale_settings, dict):
            autoscale_settings = CosmosdbSqlContainerAutoscaleSettings(**autoscale_settings)
        if isinstance(conflict_resolution_policy, dict):
            conflict_resolution_policy = CosmosdbSqlContainerConflictResolutionPolicy(**conflict_resolution_policy)
        if isinstance(indexing_policy, dict):
            indexing_policy = CosmosdbSqlContainerIndexingPolicy(**indexing_policy)
        if isinstance(timeouts, dict):
            timeouts = CosmosdbSqlContainerTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument partition_key_path", value=partition_key_path, expected_type=type_hints["partition_key_path"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument analytical_storage_ttl", value=analytical_storage_ttl, expected_type=type_hints["analytical_storage_ttl"])
            check_type(argname="argument autoscale_settings", value=autoscale_settings, expected_type=type_hints["autoscale_settings"])
            check_type(argname="argument conflict_resolution_policy", value=conflict_resolution_policy, expected_type=type_hints["conflict_resolution_policy"])
            check_type(argname="argument default_ttl", value=default_ttl, expected_type=type_hints["default_ttl"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument indexing_policy", value=indexing_policy, expected_type=type_hints["indexing_policy"])
            check_type(argname="argument partition_key_version", value=partition_key_version, expected_type=type_hints["partition_key_version"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument unique_key", value=unique_key, expected_type=type_hints["unique_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_name": account_name,
            "database_name": database_name,
            "name": name,
            "partition_key_path": partition_key_path,
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
        if analytical_storage_ttl is not None:
            self._values["analytical_storage_ttl"] = analytical_storage_ttl
        if autoscale_settings is not None:
            self._values["autoscale_settings"] = autoscale_settings
        if conflict_resolution_policy is not None:
            self._values["conflict_resolution_policy"] = conflict_resolution_policy
        if default_ttl is not None:
            self._values["default_ttl"] = default_ttl
        if id is not None:
            self._values["id"] = id
        if indexing_policy is not None:
            self._values["indexing_policy"] = indexing_policy
        if partition_key_version is not None:
            self._values["partition_key_version"] = partition_key_version
        if throughput is not None:
            self._values["throughput"] = throughput
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if unique_key is not None:
            self._values["unique_key"] = unique_key

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
    def account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#account_name CosmosdbSqlContainer#account_name}.'''
        result = self._values.get("account_name")
        assert result is not None, "Required property 'account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#database_name CosmosdbSqlContainer#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#name CosmosdbSqlContainer#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def partition_key_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#partition_key_path CosmosdbSqlContainer#partition_key_path}.'''
        result = self._values.get("partition_key_path")
        assert result is not None, "Required property 'partition_key_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#resource_group_name CosmosdbSqlContainer#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def analytical_storage_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#analytical_storage_ttl CosmosdbSqlContainer#analytical_storage_ttl}.'''
        result = self._values.get("analytical_storage_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def autoscale_settings(
        self,
    ) -> typing.Optional[CosmosdbSqlContainerAutoscaleSettings]:
        '''autoscale_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#autoscale_settings CosmosdbSqlContainer#autoscale_settings}
        '''
        result = self._values.get("autoscale_settings")
        return typing.cast(typing.Optional[CosmosdbSqlContainerAutoscaleSettings], result)

    @builtins.property
    def conflict_resolution_policy(
        self,
    ) -> typing.Optional["CosmosdbSqlContainerConflictResolutionPolicy"]:
        '''conflict_resolution_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#conflict_resolution_policy CosmosdbSqlContainer#conflict_resolution_policy}
        '''
        result = self._values.get("conflict_resolution_policy")
        return typing.cast(typing.Optional["CosmosdbSqlContainerConflictResolutionPolicy"], result)

    @builtins.property
    def default_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#default_ttl CosmosdbSqlContainer#default_ttl}.'''
        result = self._values.get("default_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#id CosmosdbSqlContainer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def indexing_policy(self) -> typing.Optional["CosmosdbSqlContainerIndexingPolicy"]:
        '''indexing_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#indexing_policy CosmosdbSqlContainer#indexing_policy}
        '''
        result = self._values.get("indexing_policy")
        return typing.cast(typing.Optional["CosmosdbSqlContainerIndexingPolicy"], result)

    @builtins.property
    def partition_key_version(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#partition_key_version CosmosdbSqlContainer#partition_key_version}.'''
        result = self._values.get("partition_key_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#throughput CosmosdbSqlContainer#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CosmosdbSqlContainerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#timeouts CosmosdbSqlContainer#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CosmosdbSqlContainerTimeouts"], result)

    @builtins.property
    def unique_key(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerUniqueKey"]]]:
        '''unique_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#unique_key CosmosdbSqlContainer#unique_key}
        '''
        result = self._values.get("unique_key")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerUniqueKey"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbSqlContainerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerConflictResolutionPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "mode": "mode",
        "conflict_resolution_path": "conflictResolutionPath",
        "conflict_resolution_procedure": "conflictResolutionProcedure",
    },
)
class CosmosdbSqlContainerConflictResolutionPolicy:
    def __init__(
        self,
        *,
        mode: builtins.str,
        conflict_resolution_path: typing.Optional[builtins.str] = None,
        conflict_resolution_procedure: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#mode CosmosdbSqlContainer#mode}.
        :param conflict_resolution_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#conflict_resolution_path CosmosdbSqlContainer#conflict_resolution_path}.
        :param conflict_resolution_procedure: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#conflict_resolution_procedure CosmosdbSqlContainer#conflict_resolution_procedure}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerConflictResolutionPolicy.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument conflict_resolution_path", value=conflict_resolution_path, expected_type=type_hints["conflict_resolution_path"])
            check_type(argname="argument conflict_resolution_procedure", value=conflict_resolution_procedure, expected_type=type_hints["conflict_resolution_procedure"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
        }
        if conflict_resolution_path is not None:
            self._values["conflict_resolution_path"] = conflict_resolution_path
        if conflict_resolution_procedure is not None:
            self._values["conflict_resolution_procedure"] = conflict_resolution_procedure

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#mode CosmosdbSqlContainer#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conflict_resolution_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#conflict_resolution_path CosmosdbSqlContainer#conflict_resolution_path}.'''
        result = self._values.get("conflict_resolution_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conflict_resolution_procedure(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#conflict_resolution_procedure CosmosdbSqlContainer#conflict_resolution_procedure}.'''
        result = self._values.get("conflict_resolution_procedure")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbSqlContainerConflictResolutionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbSqlContainerConflictResolutionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerConflictResolutionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerConflictResolutionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConflictResolutionPath")
    def reset_conflict_resolution_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConflictResolutionPath", []))

    @jsii.member(jsii_name="resetConflictResolutionProcedure")
    def reset_conflict_resolution_procedure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConflictResolutionProcedure", []))

    @builtins.property
    @jsii.member(jsii_name="conflictResolutionPathInput")
    def conflict_resolution_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conflictResolutionPathInput"))

    @builtins.property
    @jsii.member(jsii_name="conflictResolutionProcedureInput")
    def conflict_resolution_procedure_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conflictResolutionProcedureInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="conflictResolutionPath")
    def conflict_resolution_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conflictResolutionPath"))

    @conflict_resolution_path.setter
    def conflict_resolution_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerConflictResolutionPolicyOutputReference, "conflict_resolution_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conflictResolutionPath", value)

    @builtins.property
    @jsii.member(jsii_name="conflictResolutionProcedure")
    def conflict_resolution_procedure(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conflictResolutionProcedure"))

    @conflict_resolution_procedure.setter
    def conflict_resolution_procedure(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerConflictResolutionPolicyOutputReference, "conflict_resolution_procedure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conflictResolutionProcedure", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerConflictResolutionPolicyOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CosmosdbSqlContainerConflictResolutionPolicy]:
        return typing.cast(typing.Optional[CosmosdbSqlContainerConflictResolutionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CosmosdbSqlContainerConflictResolutionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerConflictResolutionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "composite_index": "compositeIndex",
        "excluded_path": "excludedPath",
        "included_path": "includedPath",
        "indexing_mode": "indexingMode",
        "spatial_index": "spatialIndex",
    },
)
class CosmosdbSqlContainerIndexingPolicy:
    def __init__(
        self,
        *,
        composite_index: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbSqlContainerIndexingPolicyCompositeIndex", typing.Dict[str, typing.Any]]]]] = None,
        excluded_path: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbSqlContainerIndexingPolicyExcludedPath", typing.Dict[str, typing.Any]]]]] = None,
        included_path: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbSqlContainerIndexingPolicyIncludedPath", typing.Dict[str, typing.Any]]]]] = None,
        indexing_mode: typing.Optional[builtins.str] = None,
        spatial_index: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbSqlContainerIndexingPolicySpatialIndex", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param composite_index: composite_index block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#composite_index CosmosdbSqlContainer#composite_index}
        :param excluded_path: excluded_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#excluded_path CosmosdbSqlContainer#excluded_path}
        :param included_path: included_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#included_path CosmosdbSqlContainer#included_path}
        :param indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#indexing_mode CosmosdbSqlContainer#indexing_mode}.
        :param spatial_index: spatial_index block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#spatial_index CosmosdbSqlContainer#spatial_index}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicy.__init__)
            check_type(argname="argument composite_index", value=composite_index, expected_type=type_hints["composite_index"])
            check_type(argname="argument excluded_path", value=excluded_path, expected_type=type_hints["excluded_path"])
            check_type(argname="argument included_path", value=included_path, expected_type=type_hints["included_path"])
            check_type(argname="argument indexing_mode", value=indexing_mode, expected_type=type_hints["indexing_mode"])
            check_type(argname="argument spatial_index", value=spatial_index, expected_type=type_hints["spatial_index"])
        self._values: typing.Dict[str, typing.Any] = {}
        if composite_index is not None:
            self._values["composite_index"] = composite_index
        if excluded_path is not None:
            self._values["excluded_path"] = excluded_path
        if included_path is not None:
            self._values["included_path"] = included_path
        if indexing_mode is not None:
            self._values["indexing_mode"] = indexing_mode
        if spatial_index is not None:
            self._values["spatial_index"] = spatial_index

    @builtins.property
    def composite_index(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerIndexingPolicyCompositeIndex"]]]:
        '''composite_index block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#composite_index CosmosdbSqlContainer#composite_index}
        '''
        result = self._values.get("composite_index")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerIndexingPolicyCompositeIndex"]]], result)

    @builtins.property
    def excluded_path(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerIndexingPolicyExcludedPath"]]]:
        '''excluded_path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#excluded_path CosmosdbSqlContainer#excluded_path}
        '''
        result = self._values.get("excluded_path")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerIndexingPolicyExcludedPath"]]], result)

    @builtins.property
    def included_path(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerIndexingPolicyIncludedPath"]]]:
        '''included_path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#included_path CosmosdbSqlContainer#included_path}
        '''
        result = self._values.get("included_path")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerIndexingPolicyIncludedPath"]]], result)

    @builtins.property
    def indexing_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#indexing_mode CosmosdbSqlContainer#indexing_mode}.'''
        result = self._values.get("indexing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spatial_index(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerIndexingPolicySpatialIndex"]]]:
        '''spatial_index block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#spatial_index CosmosdbSqlContainer#spatial_index}
        '''
        result = self._values.get("spatial_index")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerIndexingPolicySpatialIndex"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbSqlContainerIndexingPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicyCompositeIndex",
    jsii_struct_bases=[],
    name_mapping={"index": "index"},
)
class CosmosdbSqlContainerIndexingPolicyCompositeIndex:
    def __init__(
        self,
        *,
        index: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param index: index block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#index CosmosdbSqlContainer#index}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyCompositeIndex.__init__)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        self._values: typing.Dict[str, typing.Any] = {
            "index": index,
        }

    @builtins.property
    def index(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex"]]:
        '''index block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#index CosmosdbSqlContainer#index}
        '''
        result = self._values.get("index")
        assert result is not None, "Required property 'index' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbSqlContainerIndexingPolicyCompositeIndex(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex",
    jsii_struct_bases=[],
    name_mapping={"order": "order", "path": "path"},
)
class CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex:
    def __init__(self, *, order: builtins.str, path: builtins.str) -> None:
        '''
        :param order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#order CosmosdbSqlContainer#order}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#path CosmosdbSqlContainer#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex.__init__)
            check_type(argname="argument order", value=order, expected_type=type_hints["order"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "order": order,
            "path": path,
        }

    @builtins.property
    def order(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#order CosmosdbSqlContainer#order}.'''
        result = self._values.get("order")
        assert result is not None, "Required property 'order' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#path CosmosdbSqlContainer#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexList",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="orderInput")
    def order_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orderInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "order"))

    @order.setter
    def order(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexOutputReference, "order").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "order", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CosmosdbSqlContainerIndexingPolicyCompositeIndexList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicyCompositeIndexList",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyCompositeIndexList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CosmosdbSqlContainerIndexingPolicyCompositeIndexOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyCompositeIndexList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CosmosdbSqlContainerIndexingPolicyCompositeIndexOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyCompositeIndexList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyCompositeIndexList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyCompositeIndexList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyCompositeIndex]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyCompositeIndex]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyCompositeIndex]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyCompositeIndexList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CosmosdbSqlContainerIndexingPolicyCompositeIndexOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicyCompositeIndexOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyCompositeIndexOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putIndex")
    def put_index(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyCompositeIndexOutputReference.put_index)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIndex", [value]))

    @builtins.property
    @jsii.member(jsii_name="index")
    def index(self) -> CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexList:
        return typing.cast(CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexList, jsii.get(self, "index"))

    @builtins.property
    @jsii.member(jsii_name="indexInput")
    def index_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex]]], jsii.get(self, "indexInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CosmosdbSqlContainerIndexingPolicyCompositeIndex, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CosmosdbSqlContainerIndexingPolicyCompositeIndex, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CosmosdbSqlContainerIndexingPolicyCompositeIndex, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyCompositeIndexOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicyExcludedPath",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class CosmosdbSqlContainerIndexingPolicyExcludedPath:
    def __init__(self, *, path: builtins.str) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#path CosmosdbSqlContainer#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyExcludedPath.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#path CosmosdbSqlContainer#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbSqlContainerIndexingPolicyExcludedPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbSqlContainerIndexingPolicyExcludedPathList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicyExcludedPathList",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyExcludedPathList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CosmosdbSqlContainerIndexingPolicyExcludedPathOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyExcludedPathList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CosmosdbSqlContainerIndexingPolicyExcludedPathOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyExcludedPathList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyExcludedPathList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyExcludedPathList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyExcludedPath]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyExcludedPath]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyExcludedPath]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyExcludedPathList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CosmosdbSqlContainerIndexingPolicyExcludedPathOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicyExcludedPathOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyExcludedPathOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyExcludedPathOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CosmosdbSqlContainerIndexingPolicyExcludedPath, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CosmosdbSqlContainerIndexingPolicyExcludedPath, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CosmosdbSqlContainerIndexingPolicyExcludedPath, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyExcludedPathOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicyIncludedPath",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class CosmosdbSqlContainerIndexingPolicyIncludedPath:
    def __init__(self, *, path: builtins.str) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#path CosmosdbSqlContainer#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyIncludedPath.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#path CosmosdbSqlContainer#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbSqlContainerIndexingPolicyIncludedPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbSqlContainerIndexingPolicyIncludedPathList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicyIncludedPathList",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyIncludedPathList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CosmosdbSqlContainerIndexingPolicyIncludedPathOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyIncludedPathList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CosmosdbSqlContainerIndexingPolicyIncludedPathOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyIncludedPathList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyIncludedPathList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyIncludedPathList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyIncludedPath]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyIncludedPath]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyIncludedPath]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyIncludedPathList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CosmosdbSqlContainerIndexingPolicyIncludedPathOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicyIncludedPathOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyIncludedPathOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyIncludedPathOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CosmosdbSqlContainerIndexingPolicyIncludedPath, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CosmosdbSqlContainerIndexingPolicyIncludedPath, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CosmosdbSqlContainerIndexingPolicyIncludedPath, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyIncludedPathOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CosmosdbSqlContainerIndexingPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicyOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCompositeIndex")
    def put_composite_index(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CosmosdbSqlContainerIndexingPolicyCompositeIndex, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyOutputReference.put_composite_index)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCompositeIndex", [value]))

    @jsii.member(jsii_name="putExcludedPath")
    def put_excluded_path(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CosmosdbSqlContainerIndexingPolicyExcludedPath, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyOutputReference.put_excluded_path)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExcludedPath", [value]))

    @jsii.member(jsii_name="putIncludedPath")
    def put_included_path(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CosmosdbSqlContainerIndexingPolicyIncludedPath, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyOutputReference.put_included_path)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIncludedPath", [value]))

    @jsii.member(jsii_name="putSpatialIndex")
    def put_spatial_index(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbSqlContainerIndexingPolicySpatialIndex", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicyOutputReference.put_spatial_index)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSpatialIndex", [value]))

    @jsii.member(jsii_name="resetCompositeIndex")
    def reset_composite_index(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompositeIndex", []))

    @jsii.member(jsii_name="resetExcludedPath")
    def reset_excluded_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedPath", []))

    @jsii.member(jsii_name="resetIncludedPath")
    def reset_included_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludedPath", []))

    @jsii.member(jsii_name="resetIndexingMode")
    def reset_indexing_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIndexingMode", []))

    @jsii.member(jsii_name="resetSpatialIndex")
    def reset_spatial_index(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpatialIndex", []))

    @builtins.property
    @jsii.member(jsii_name="compositeIndex")
    def composite_index(self) -> CosmosdbSqlContainerIndexingPolicyCompositeIndexList:
        return typing.cast(CosmosdbSqlContainerIndexingPolicyCompositeIndexList, jsii.get(self, "compositeIndex"))

    @builtins.property
    @jsii.member(jsii_name="excludedPath")
    def excluded_path(self) -> CosmosdbSqlContainerIndexingPolicyExcludedPathList:
        return typing.cast(CosmosdbSqlContainerIndexingPolicyExcludedPathList, jsii.get(self, "excludedPath"))

    @builtins.property
    @jsii.member(jsii_name="includedPath")
    def included_path(self) -> CosmosdbSqlContainerIndexingPolicyIncludedPathList:
        return typing.cast(CosmosdbSqlContainerIndexingPolicyIncludedPathList, jsii.get(self, "includedPath"))

    @builtins.property
    @jsii.member(jsii_name="spatialIndex")
    def spatial_index(self) -> "CosmosdbSqlContainerIndexingPolicySpatialIndexList":
        return typing.cast("CosmosdbSqlContainerIndexingPolicySpatialIndexList", jsii.get(self, "spatialIndex"))

    @builtins.property
    @jsii.member(jsii_name="compositeIndexInput")
    def composite_index_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyCompositeIndex]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyCompositeIndex]]], jsii.get(self, "compositeIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedPathInput")
    def excluded_path_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyExcludedPath]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyExcludedPath]]], jsii.get(self, "excludedPathInput"))

    @builtins.property
    @jsii.member(jsii_name="includedPathInput")
    def included_path_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyIncludedPath]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicyIncludedPath]]], jsii.get(self, "includedPathInput"))

    @builtins.property
    @jsii.member(jsii_name="indexingModeInput")
    def indexing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="spatialIndexInput")
    def spatial_index_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerIndexingPolicySpatialIndex"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbSqlContainerIndexingPolicySpatialIndex"]]], jsii.get(self, "spatialIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="indexingMode")
    def indexing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "indexingMode"))

    @indexing_mode.setter
    def indexing_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyOutputReference, "indexing_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexingMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CosmosdbSqlContainerIndexingPolicy]:
        return typing.cast(typing.Optional[CosmosdbSqlContainerIndexingPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CosmosdbSqlContainerIndexingPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicySpatialIndex",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class CosmosdbSqlContainerIndexingPolicySpatialIndex:
    def __init__(self, *, path: builtins.str) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#path CosmosdbSqlContainer#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicySpatialIndex.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#path CosmosdbSqlContainer#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbSqlContainerIndexingPolicySpatialIndex(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbSqlContainerIndexingPolicySpatialIndexList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicySpatialIndexList",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicySpatialIndexList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CosmosdbSqlContainerIndexingPolicySpatialIndexOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicySpatialIndexList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CosmosdbSqlContainerIndexingPolicySpatialIndexOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicySpatialIndexList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicySpatialIndexList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicySpatialIndexList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicySpatialIndex]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicySpatialIndex]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerIndexingPolicySpatialIndex]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicySpatialIndexList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CosmosdbSqlContainerIndexingPolicySpatialIndexOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerIndexingPolicySpatialIndexOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerIndexingPolicySpatialIndexOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="types")
    def types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "types"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicySpatialIndexOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CosmosdbSqlContainerIndexingPolicySpatialIndex, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CosmosdbSqlContainerIndexingPolicySpatialIndex, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CosmosdbSqlContainerIndexingPolicySpatialIndex, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerIndexingPolicySpatialIndexOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class CosmosdbSqlContainerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#create CosmosdbSqlContainer#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#delete CosmosdbSqlContainer#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#read CosmosdbSqlContainer#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#update CosmosdbSqlContainer#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#create CosmosdbSqlContainer#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#delete CosmosdbSqlContainer#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#read CosmosdbSqlContainer#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#update CosmosdbSqlContainer#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbSqlContainerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbSqlContainerTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CosmosdbSqlContainerTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CosmosdbSqlContainerTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CosmosdbSqlContainerTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerUniqueKey",
    jsii_struct_bases=[],
    name_mapping={"paths": "paths"},
)
class CosmosdbSqlContainerUniqueKey:
    def __init__(self, *, paths: typing.Sequence[builtins.str]) -> None:
        '''
        :param paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#paths CosmosdbSqlContainer#paths}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerUniqueKey.__init__)
            check_type(argname="argument paths", value=paths, expected_type=type_hints["paths"])
        self._values: typing.Dict[str, typing.Any] = {
            "paths": paths,
        }

    @builtins.property
    def paths(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_sql_container#paths CosmosdbSqlContainer#paths}.'''
        result = self._values.get("paths")
        assert result is not None, "Required property 'paths' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbSqlContainerUniqueKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbSqlContainerUniqueKeyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerUniqueKeyList",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerUniqueKeyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CosmosdbSqlContainerUniqueKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbSqlContainerUniqueKeyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CosmosdbSqlContainerUniqueKeyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerUniqueKeyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerUniqueKeyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerUniqueKeyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerUniqueKey]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerUniqueKey]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbSqlContainerUniqueKey]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerUniqueKeyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CosmosdbSqlContainerUniqueKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbSqlContainer.CosmosdbSqlContainerUniqueKeyOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbSqlContainerUniqueKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="pathsInput")
    def paths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pathsInput"))

    @builtins.property
    @jsii.member(jsii_name="paths")
    def paths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "paths"))

    @paths.setter
    def paths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerUniqueKeyOutputReference, "paths").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paths", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CosmosdbSqlContainerUniqueKey, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CosmosdbSqlContainerUniqueKey, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CosmosdbSqlContainerUniqueKey, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbSqlContainerUniqueKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CosmosdbSqlContainer",
    "CosmosdbSqlContainerAutoscaleSettings",
    "CosmosdbSqlContainerAutoscaleSettingsOutputReference",
    "CosmosdbSqlContainerConfig",
    "CosmosdbSqlContainerConflictResolutionPolicy",
    "CosmosdbSqlContainerConflictResolutionPolicyOutputReference",
    "CosmosdbSqlContainerIndexingPolicy",
    "CosmosdbSqlContainerIndexingPolicyCompositeIndex",
    "CosmosdbSqlContainerIndexingPolicyCompositeIndexIndex",
    "CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexList",
    "CosmosdbSqlContainerIndexingPolicyCompositeIndexIndexOutputReference",
    "CosmosdbSqlContainerIndexingPolicyCompositeIndexList",
    "CosmosdbSqlContainerIndexingPolicyCompositeIndexOutputReference",
    "CosmosdbSqlContainerIndexingPolicyExcludedPath",
    "CosmosdbSqlContainerIndexingPolicyExcludedPathList",
    "CosmosdbSqlContainerIndexingPolicyExcludedPathOutputReference",
    "CosmosdbSqlContainerIndexingPolicyIncludedPath",
    "CosmosdbSqlContainerIndexingPolicyIncludedPathList",
    "CosmosdbSqlContainerIndexingPolicyIncludedPathOutputReference",
    "CosmosdbSqlContainerIndexingPolicyOutputReference",
    "CosmosdbSqlContainerIndexingPolicySpatialIndex",
    "CosmosdbSqlContainerIndexingPolicySpatialIndexList",
    "CosmosdbSqlContainerIndexingPolicySpatialIndexOutputReference",
    "CosmosdbSqlContainerTimeouts",
    "CosmosdbSqlContainerTimeoutsOutputReference",
    "CosmosdbSqlContainerUniqueKey",
    "CosmosdbSqlContainerUniqueKeyList",
    "CosmosdbSqlContainerUniqueKeyOutputReference",
]

publication.publish()
