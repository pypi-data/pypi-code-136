'''
# `azurerm_spring_cloud_app_cosmosdb_association`

Refer to the Terraform Registory for docs: [`azurerm_spring_cloud_app_cosmosdb_association`](https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association).
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


class SpringCloudAppCosmosdbAssociation(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudAppCosmosdbAssociation.SpringCloudAppCosmosdbAssociation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association azurerm_spring_cloud_app_cosmosdb_association}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_type: builtins.str,
        cosmosdb_access_key: builtins.str,
        cosmosdb_account_id: builtins.str,
        name: builtins.str,
        spring_cloud_app_id: builtins.str,
        cosmosdb_cassandra_keyspace_name: typing.Optional[builtins.str] = None,
        cosmosdb_gremlin_database_name: typing.Optional[builtins.str] = None,
        cosmosdb_gremlin_graph_name: typing.Optional[builtins.str] = None,
        cosmosdb_mongo_database_name: typing.Optional[builtins.str] = None,
        cosmosdb_sql_database_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SpringCloudAppCosmosdbAssociationTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association azurerm_spring_cloud_app_cosmosdb_association} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#api_type SpringCloudAppCosmosdbAssociation#api_type}.
        :param cosmosdb_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_access_key SpringCloudAppCosmosdbAssociation#cosmosdb_access_key}.
        :param cosmosdb_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_account_id SpringCloudAppCosmosdbAssociation#cosmosdb_account_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#name SpringCloudAppCosmosdbAssociation#name}.
        :param spring_cloud_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#spring_cloud_app_id SpringCloudAppCosmosdbAssociation#spring_cloud_app_id}.
        :param cosmosdb_cassandra_keyspace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_cassandra_keyspace_name SpringCloudAppCosmosdbAssociation#cosmosdb_cassandra_keyspace_name}.
        :param cosmosdb_gremlin_database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_gremlin_database_name SpringCloudAppCosmosdbAssociation#cosmosdb_gremlin_database_name}.
        :param cosmosdb_gremlin_graph_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_gremlin_graph_name SpringCloudAppCosmosdbAssociation#cosmosdb_gremlin_graph_name}.
        :param cosmosdb_mongo_database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_mongo_database_name SpringCloudAppCosmosdbAssociation#cosmosdb_mongo_database_name}.
        :param cosmosdb_sql_database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_sql_database_name SpringCloudAppCosmosdbAssociation#cosmosdb_sql_database_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#id SpringCloudAppCosmosdbAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#timeouts SpringCloudAppCosmosdbAssociation#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudAppCosmosdbAssociation.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SpringCloudAppCosmosdbAssociationConfig(
            api_type=api_type,
            cosmosdb_access_key=cosmosdb_access_key,
            cosmosdb_account_id=cosmosdb_account_id,
            name=name,
            spring_cloud_app_id=spring_cloud_app_id,
            cosmosdb_cassandra_keyspace_name=cosmosdb_cassandra_keyspace_name,
            cosmosdb_gremlin_database_name=cosmosdb_gremlin_database_name,
            cosmosdb_gremlin_graph_name=cosmosdb_gremlin_graph_name,
            cosmosdb_mongo_database_name=cosmosdb_mongo_database_name,
            cosmosdb_sql_database_name=cosmosdb_sql_database_name,
            id=id,
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
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#create SpringCloudAppCosmosdbAssociation#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#delete SpringCloudAppCosmosdbAssociation#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#read SpringCloudAppCosmosdbAssociation#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#update SpringCloudAppCosmosdbAssociation#update}.
        '''
        value = SpringCloudAppCosmosdbAssociationTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCosmosdbCassandraKeyspaceName")
    def reset_cosmosdb_cassandra_keyspace_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCosmosdbCassandraKeyspaceName", []))

    @jsii.member(jsii_name="resetCosmosdbGremlinDatabaseName")
    def reset_cosmosdb_gremlin_database_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCosmosdbGremlinDatabaseName", []))

    @jsii.member(jsii_name="resetCosmosdbGremlinGraphName")
    def reset_cosmosdb_gremlin_graph_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCosmosdbGremlinGraphName", []))

    @jsii.member(jsii_name="resetCosmosdbMongoDatabaseName")
    def reset_cosmosdb_mongo_database_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCosmosdbMongoDatabaseName", []))

    @jsii.member(jsii_name="resetCosmosdbSqlDatabaseName")
    def reset_cosmosdb_sql_database_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCosmosdbSqlDatabaseName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SpringCloudAppCosmosdbAssociationTimeoutsOutputReference":
        return typing.cast("SpringCloudAppCosmosdbAssociationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="apiTypeInput")
    def api_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="cosmosdbAccessKeyInput")
    def cosmosdb_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cosmosdbAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="cosmosdbAccountIdInput")
    def cosmosdb_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cosmosdbAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cosmosdbCassandraKeyspaceNameInput")
    def cosmosdb_cassandra_keyspace_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cosmosdbCassandraKeyspaceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cosmosdbGremlinDatabaseNameInput")
    def cosmosdb_gremlin_database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cosmosdbGremlinDatabaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cosmosdbGremlinGraphNameInput")
    def cosmosdb_gremlin_graph_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cosmosdbGremlinGraphNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cosmosdbMongoDatabaseNameInput")
    def cosmosdb_mongo_database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cosmosdbMongoDatabaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cosmosdbSqlDatabaseNameInput")
    def cosmosdb_sql_database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cosmosdbSqlDatabaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="springCloudAppIdInput")
    def spring_cloud_app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "springCloudAppIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SpringCloudAppCosmosdbAssociationTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SpringCloudAppCosmosdbAssociationTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="apiType")
    def api_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiType"))

    @api_type.setter
    def api_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociation, "api_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiType", value)

    @builtins.property
    @jsii.member(jsii_name="cosmosdbAccessKey")
    def cosmosdb_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cosmosdbAccessKey"))

    @cosmosdb_access_key.setter
    def cosmosdb_access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociation, "cosmosdb_access_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cosmosdbAccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="cosmosdbAccountId")
    def cosmosdb_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cosmosdbAccountId"))

    @cosmosdb_account_id.setter
    def cosmosdb_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociation, "cosmosdb_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cosmosdbAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="cosmosdbCassandraKeyspaceName")
    def cosmosdb_cassandra_keyspace_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cosmosdbCassandraKeyspaceName"))

    @cosmosdb_cassandra_keyspace_name.setter
    def cosmosdb_cassandra_keyspace_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociation, "cosmosdb_cassandra_keyspace_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cosmosdbCassandraKeyspaceName", value)

    @builtins.property
    @jsii.member(jsii_name="cosmosdbGremlinDatabaseName")
    def cosmosdb_gremlin_database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cosmosdbGremlinDatabaseName"))

    @cosmosdb_gremlin_database_name.setter
    def cosmosdb_gremlin_database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociation, "cosmosdb_gremlin_database_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cosmosdbGremlinDatabaseName", value)

    @builtins.property
    @jsii.member(jsii_name="cosmosdbGremlinGraphName")
    def cosmosdb_gremlin_graph_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cosmosdbGremlinGraphName"))

    @cosmosdb_gremlin_graph_name.setter
    def cosmosdb_gremlin_graph_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociation, "cosmosdb_gremlin_graph_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cosmosdbGremlinGraphName", value)

    @builtins.property
    @jsii.member(jsii_name="cosmosdbMongoDatabaseName")
    def cosmosdb_mongo_database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cosmosdbMongoDatabaseName"))

    @cosmosdb_mongo_database_name.setter
    def cosmosdb_mongo_database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociation, "cosmosdb_mongo_database_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cosmosdbMongoDatabaseName", value)

    @builtins.property
    @jsii.member(jsii_name="cosmosdbSqlDatabaseName")
    def cosmosdb_sql_database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cosmosdbSqlDatabaseName"))

    @cosmosdb_sql_database_name.setter
    def cosmosdb_sql_database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociation, "cosmosdb_sql_database_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cosmosdbSqlDatabaseName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociation, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociation, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="springCloudAppId")
    def spring_cloud_app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "springCloudAppId"))

    @spring_cloud_app_id.setter
    def spring_cloud_app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociation, "spring_cloud_app_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "springCloudAppId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudAppCosmosdbAssociation.SpringCloudAppCosmosdbAssociationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_type": "apiType",
        "cosmosdb_access_key": "cosmosdbAccessKey",
        "cosmosdb_account_id": "cosmosdbAccountId",
        "name": "name",
        "spring_cloud_app_id": "springCloudAppId",
        "cosmosdb_cassandra_keyspace_name": "cosmosdbCassandraKeyspaceName",
        "cosmosdb_gremlin_database_name": "cosmosdbGremlinDatabaseName",
        "cosmosdb_gremlin_graph_name": "cosmosdbGremlinGraphName",
        "cosmosdb_mongo_database_name": "cosmosdbMongoDatabaseName",
        "cosmosdb_sql_database_name": "cosmosdbSqlDatabaseName",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class SpringCloudAppCosmosdbAssociationConfig(cdktf.TerraformMetaArguments):
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
        api_type: builtins.str,
        cosmosdb_access_key: builtins.str,
        cosmosdb_account_id: builtins.str,
        name: builtins.str,
        spring_cloud_app_id: builtins.str,
        cosmosdb_cassandra_keyspace_name: typing.Optional[builtins.str] = None,
        cosmosdb_gremlin_database_name: typing.Optional[builtins.str] = None,
        cosmosdb_gremlin_graph_name: typing.Optional[builtins.str] = None,
        cosmosdb_mongo_database_name: typing.Optional[builtins.str] = None,
        cosmosdb_sql_database_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SpringCloudAppCosmosdbAssociationTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#api_type SpringCloudAppCosmosdbAssociation#api_type}.
        :param cosmosdb_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_access_key SpringCloudAppCosmosdbAssociation#cosmosdb_access_key}.
        :param cosmosdb_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_account_id SpringCloudAppCosmosdbAssociation#cosmosdb_account_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#name SpringCloudAppCosmosdbAssociation#name}.
        :param spring_cloud_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#spring_cloud_app_id SpringCloudAppCosmosdbAssociation#spring_cloud_app_id}.
        :param cosmosdb_cassandra_keyspace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_cassandra_keyspace_name SpringCloudAppCosmosdbAssociation#cosmosdb_cassandra_keyspace_name}.
        :param cosmosdb_gremlin_database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_gremlin_database_name SpringCloudAppCosmosdbAssociation#cosmosdb_gremlin_database_name}.
        :param cosmosdb_gremlin_graph_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_gremlin_graph_name SpringCloudAppCosmosdbAssociation#cosmosdb_gremlin_graph_name}.
        :param cosmosdb_mongo_database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_mongo_database_name SpringCloudAppCosmosdbAssociation#cosmosdb_mongo_database_name}.
        :param cosmosdb_sql_database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_sql_database_name SpringCloudAppCosmosdbAssociation#cosmosdb_sql_database_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#id SpringCloudAppCosmosdbAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#timeouts SpringCloudAppCosmosdbAssociation#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = SpringCloudAppCosmosdbAssociationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudAppCosmosdbAssociationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_type", value=api_type, expected_type=type_hints["api_type"])
            check_type(argname="argument cosmosdb_access_key", value=cosmosdb_access_key, expected_type=type_hints["cosmosdb_access_key"])
            check_type(argname="argument cosmosdb_account_id", value=cosmosdb_account_id, expected_type=type_hints["cosmosdb_account_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument spring_cloud_app_id", value=spring_cloud_app_id, expected_type=type_hints["spring_cloud_app_id"])
            check_type(argname="argument cosmosdb_cassandra_keyspace_name", value=cosmosdb_cassandra_keyspace_name, expected_type=type_hints["cosmosdb_cassandra_keyspace_name"])
            check_type(argname="argument cosmosdb_gremlin_database_name", value=cosmosdb_gremlin_database_name, expected_type=type_hints["cosmosdb_gremlin_database_name"])
            check_type(argname="argument cosmosdb_gremlin_graph_name", value=cosmosdb_gremlin_graph_name, expected_type=type_hints["cosmosdb_gremlin_graph_name"])
            check_type(argname="argument cosmosdb_mongo_database_name", value=cosmosdb_mongo_database_name, expected_type=type_hints["cosmosdb_mongo_database_name"])
            check_type(argname="argument cosmosdb_sql_database_name", value=cosmosdb_sql_database_name, expected_type=type_hints["cosmosdb_sql_database_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_type": api_type,
            "cosmosdb_access_key": cosmosdb_access_key,
            "cosmosdb_account_id": cosmosdb_account_id,
            "name": name,
            "spring_cloud_app_id": spring_cloud_app_id,
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
        if cosmosdb_cassandra_keyspace_name is not None:
            self._values["cosmosdb_cassandra_keyspace_name"] = cosmosdb_cassandra_keyspace_name
        if cosmosdb_gremlin_database_name is not None:
            self._values["cosmosdb_gremlin_database_name"] = cosmosdb_gremlin_database_name
        if cosmosdb_gremlin_graph_name is not None:
            self._values["cosmosdb_gremlin_graph_name"] = cosmosdb_gremlin_graph_name
        if cosmosdb_mongo_database_name is not None:
            self._values["cosmosdb_mongo_database_name"] = cosmosdb_mongo_database_name
        if cosmosdb_sql_database_name is not None:
            self._values["cosmosdb_sql_database_name"] = cosmosdb_sql_database_name
        if id is not None:
            self._values["id"] = id
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
    def api_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#api_type SpringCloudAppCosmosdbAssociation#api_type}.'''
        result = self._values.get("api_type")
        assert result is not None, "Required property 'api_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cosmosdb_access_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_access_key SpringCloudAppCosmosdbAssociation#cosmosdb_access_key}.'''
        result = self._values.get("cosmosdb_access_key")
        assert result is not None, "Required property 'cosmosdb_access_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cosmosdb_account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_account_id SpringCloudAppCosmosdbAssociation#cosmosdb_account_id}.'''
        result = self._values.get("cosmosdb_account_id")
        assert result is not None, "Required property 'cosmosdb_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#name SpringCloudAppCosmosdbAssociation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spring_cloud_app_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#spring_cloud_app_id SpringCloudAppCosmosdbAssociation#spring_cloud_app_id}.'''
        result = self._values.get("spring_cloud_app_id")
        assert result is not None, "Required property 'spring_cloud_app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cosmosdb_cassandra_keyspace_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_cassandra_keyspace_name SpringCloudAppCosmosdbAssociation#cosmosdb_cassandra_keyspace_name}.'''
        result = self._values.get("cosmosdb_cassandra_keyspace_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cosmosdb_gremlin_database_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_gremlin_database_name SpringCloudAppCosmosdbAssociation#cosmosdb_gremlin_database_name}.'''
        result = self._values.get("cosmosdb_gremlin_database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cosmosdb_gremlin_graph_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_gremlin_graph_name SpringCloudAppCosmosdbAssociation#cosmosdb_gremlin_graph_name}.'''
        result = self._values.get("cosmosdb_gremlin_graph_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cosmosdb_mongo_database_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_mongo_database_name SpringCloudAppCosmosdbAssociation#cosmosdb_mongo_database_name}.'''
        result = self._values.get("cosmosdb_mongo_database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cosmosdb_sql_database_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#cosmosdb_sql_database_name SpringCloudAppCosmosdbAssociation#cosmosdb_sql_database_name}.'''
        result = self._values.get("cosmosdb_sql_database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#id SpringCloudAppCosmosdbAssociation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SpringCloudAppCosmosdbAssociationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#timeouts SpringCloudAppCosmosdbAssociation#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SpringCloudAppCosmosdbAssociationTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudAppCosmosdbAssociationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudAppCosmosdbAssociation.SpringCloudAppCosmosdbAssociationTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SpringCloudAppCosmosdbAssociationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#create SpringCloudAppCosmosdbAssociation#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#delete SpringCloudAppCosmosdbAssociation#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#read SpringCloudAppCosmosdbAssociation#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#update SpringCloudAppCosmosdbAssociation#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudAppCosmosdbAssociationTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#create SpringCloudAppCosmosdbAssociation#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#delete SpringCloudAppCosmosdbAssociation#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#read SpringCloudAppCosmosdbAssociation#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app_cosmosdb_association#update SpringCloudAppCosmosdbAssociation#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudAppCosmosdbAssociationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudAppCosmosdbAssociationTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudAppCosmosdbAssociation.SpringCloudAppCosmosdbAssociationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudAppCosmosdbAssociationTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociationTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociationTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociationTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociationTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SpringCloudAppCosmosdbAssociationTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SpringCloudAppCosmosdbAssociationTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SpringCloudAppCosmosdbAssociationTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCosmosdbAssociationTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SpringCloudAppCosmosdbAssociation",
    "SpringCloudAppCosmosdbAssociationConfig",
    "SpringCloudAppCosmosdbAssociationTimeouts",
    "SpringCloudAppCosmosdbAssociationTimeoutsOutputReference",
]

publication.publish()
