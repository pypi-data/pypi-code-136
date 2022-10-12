'''
# `snowflake_database`

Refer to the Terraform Registory for docs: [`snowflake_database`](https://www.terraform.io/docs/providers/snowflake/r/database).
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


class Database(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.database.Database",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/database snowflake_database}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        data_retention_time_in_days: typing.Optional[jsii.Number] = None,
        from_database: typing.Optional[builtins.str] = None,
        from_replica: typing.Optional[builtins.str] = None,
        from_share: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        is_transient: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        replication_configuration: typing.Optional[typing.Union["DatabaseReplicationConfiguration", typing.Dict[str, typing.Any]]] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseTag", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/database snowflake_database} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#name Database#name}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#comment Database#comment}.
        :param data_retention_time_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#data_retention_time_in_days Database#data_retention_time_in_days}.
        :param from_database: Specify a database to create a clone from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#from_database Database#from_database}
        :param from_replica: Specify a fully-qualified path to a database to create a replica from. A fully qualified path follows the format of "<organization_name>"."<account_name>"."<db_name>". An example would be: "myorg1"."account1"."db1" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#from_replica Database#from_replica}
        :param from_share: Specify a provider and a share in this map to create a database from a share. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#from_share Database#from_share}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#id Database#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_transient: Specifies a database as transient. Transient databases do not have a Fail-safe period so they do not incur additional storage costs once they leave Time Travel; however, this means they are also not protected by Fail-safe in the event of a data loss. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#is_transient Database#is_transient}
        :param replication_configuration: replication_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#replication_configuration Database#replication_configuration}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#tag Database#tag}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Database.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatabaseConfig(
            name=name,
            comment=comment,
            data_retention_time_in_days=data_retention_time_in_days,
            from_database=from_database,
            from_replica=from_replica,
            from_share=from_share,
            id=id,
            is_transient=is_transient,
            replication_configuration=replication_configuration,
            tag=tag,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putReplicationConfiguration")
    def put_replication_configuration(
        self,
        *,
        accounts: typing.Sequence[builtins.str],
        ignore_edition_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param accounts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#accounts Database#accounts}.
        :param ignore_edition_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#ignore_edition_check Database#ignore_edition_check}.
        '''
        value = DatabaseReplicationConfiguration(
            accounts=accounts, ignore_edition_check=ignore_edition_check
        )

        return typing.cast(None, jsii.invoke(self, "putReplicationConfiguration", [value]))

    @jsii.member(jsii_name="putTag")
    def put_tag(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseTag", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Database.put_tag)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTag", [value]))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetDataRetentionTimeInDays")
    def reset_data_retention_time_in_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataRetentionTimeInDays", []))

    @jsii.member(jsii_name="resetFromDatabase")
    def reset_from_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromDatabase", []))

    @jsii.member(jsii_name="resetFromReplica")
    def reset_from_replica(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromReplica", []))

    @jsii.member(jsii_name="resetFromShare")
    def reset_from_share(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromShare", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsTransient")
    def reset_is_transient(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsTransient", []))

    @jsii.member(jsii_name="resetReplicationConfiguration")
    def reset_replication_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicationConfiguration", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="replicationConfiguration")
    def replication_configuration(
        self,
    ) -> "DatabaseReplicationConfigurationOutputReference":
        return typing.cast("DatabaseReplicationConfigurationOutputReference", jsii.get(self, "replicationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> "DatabaseTagList":
        return typing.cast("DatabaseTagList", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="dataRetentionTimeInDaysInput")
    def data_retention_time_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataRetentionTimeInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="fromDatabaseInput")
    def from_database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromDatabaseInput"))

    @builtins.property
    @jsii.member(jsii_name="fromReplicaInput")
    def from_replica_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromReplicaInput"))

    @builtins.property
    @jsii.member(jsii_name="fromShareInput")
    def from_share_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "fromShareInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isTransientInput")
    def is_transient_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isTransientInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationConfigurationInput")
    def replication_configuration_input(
        self,
    ) -> typing.Optional["DatabaseReplicationConfiguration"]:
        return typing.cast(typing.Optional["DatabaseReplicationConfiguration"], jsii.get(self, "replicationConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseTag"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseTag"]]], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "comment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="dataRetentionTimeInDays")
    def data_retention_time_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dataRetentionTimeInDays"))

    @data_retention_time_in_days.setter
    def data_retention_time_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "data_retention_time_in_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataRetentionTimeInDays", value)

    @builtins.property
    @jsii.member(jsii_name="fromDatabase")
    def from_database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fromDatabase"))

    @from_database.setter
    def from_database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "from_database").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromDatabase", value)

    @builtins.property
    @jsii.member(jsii_name="fromReplica")
    def from_replica(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fromReplica"))

    @from_replica.setter
    def from_replica(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "from_replica").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromReplica", value)

    @builtins.property
    @jsii.member(jsii_name="fromShare")
    def from_share(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "fromShare"))

    @from_share.setter
    def from_share(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "from_share").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromShare", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isTransient")
    def is_transient(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isTransient"))

    @is_transient.setter
    def is_transient(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "is_transient").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isTransient", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.database.DatabaseConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "comment": "comment",
        "data_retention_time_in_days": "dataRetentionTimeInDays",
        "from_database": "fromDatabase",
        "from_replica": "fromReplica",
        "from_share": "fromShare",
        "id": "id",
        "is_transient": "isTransient",
        "replication_configuration": "replicationConfiguration",
        "tag": "tag",
    },
)
class DatabaseConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        data_retention_time_in_days: typing.Optional[jsii.Number] = None,
        from_database: typing.Optional[builtins.str] = None,
        from_replica: typing.Optional[builtins.str] = None,
        from_share: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        is_transient: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        replication_configuration: typing.Optional[typing.Union["DatabaseReplicationConfiguration", typing.Dict[str, typing.Any]]] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DatabaseTag", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#name Database#name}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#comment Database#comment}.
        :param data_retention_time_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#data_retention_time_in_days Database#data_retention_time_in_days}.
        :param from_database: Specify a database to create a clone from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#from_database Database#from_database}
        :param from_replica: Specify a fully-qualified path to a database to create a replica from. A fully qualified path follows the format of "<organization_name>"."<account_name>"."<db_name>". An example would be: "myorg1"."account1"."db1" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#from_replica Database#from_replica}
        :param from_share: Specify a provider and a share in this map to create a database from a share. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#from_share Database#from_share}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#id Database#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_transient: Specifies a database as transient. Transient databases do not have a Fail-safe period so they do not incur additional storage costs once they leave Time Travel; however, this means they are also not protected by Fail-safe in the event of a data loss. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#is_transient Database#is_transient}
        :param replication_configuration: replication_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#replication_configuration Database#replication_configuration}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#tag Database#tag}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(replication_configuration, dict):
            replication_configuration = DatabaseReplicationConfiguration(**replication_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument data_retention_time_in_days", value=data_retention_time_in_days, expected_type=type_hints["data_retention_time_in_days"])
            check_type(argname="argument from_database", value=from_database, expected_type=type_hints["from_database"])
            check_type(argname="argument from_replica", value=from_replica, expected_type=type_hints["from_replica"])
            check_type(argname="argument from_share", value=from_share, expected_type=type_hints["from_share"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_transient", value=is_transient, expected_type=type_hints["is_transient"])
            check_type(argname="argument replication_configuration", value=replication_configuration, expected_type=type_hints["replication_configuration"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
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
        if comment is not None:
            self._values["comment"] = comment
        if data_retention_time_in_days is not None:
            self._values["data_retention_time_in_days"] = data_retention_time_in_days
        if from_database is not None:
            self._values["from_database"] = from_database
        if from_replica is not None:
            self._values["from_replica"] = from_replica
        if from_share is not None:
            self._values["from_share"] = from_share
        if id is not None:
            self._values["id"] = id
        if is_transient is not None:
            self._values["is_transient"] = is_transient
        if replication_configuration is not None:
            self._values["replication_configuration"] = replication_configuration
        if tag is not None:
            self._values["tag"] = tag

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#name Database#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#comment Database#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_retention_time_in_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#data_retention_time_in_days Database#data_retention_time_in_days}.'''
        result = self._values.get("data_retention_time_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def from_database(self) -> typing.Optional[builtins.str]:
        '''Specify a database to create a clone from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#from_database Database#from_database}
        '''
        result = self._values.get("from_database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def from_replica(self) -> typing.Optional[builtins.str]:
        '''Specify a fully-qualified path to a database to create a replica from.

        A fully qualified path follows the format of "<organization_name>"."<account_name>"."<db_name>". An example would be: "myorg1"."account1"."db1"

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#from_replica Database#from_replica}
        '''
        result = self._values.get("from_replica")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def from_share(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Specify a provider and a share in this map to create a database from a share.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#from_share Database#from_share}
        '''
        result = self._values.get("from_share")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#id Database#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_transient(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies a database as transient.

        Transient databases do not have a Fail-safe period so they do not incur additional storage costs once they leave Time Travel; however, this means they are also not protected by Fail-safe in the event of a data loss.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#is_transient Database#is_transient}
        '''
        result = self._values.get("is_transient")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def replication_configuration(
        self,
    ) -> typing.Optional["DatabaseReplicationConfiguration"]:
        '''replication_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#replication_configuration Database#replication_configuration}
        '''
        result = self._values.get("replication_configuration")
        return typing.cast(typing.Optional["DatabaseReplicationConfiguration"], result)

    @builtins.property
    def tag(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseTag"]]]:
        '''tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#tag Database#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DatabaseTag"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.database.DatabaseReplicationConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "accounts": "accounts",
        "ignore_edition_check": "ignoreEditionCheck",
    },
)
class DatabaseReplicationConfiguration:
    def __init__(
        self,
        *,
        accounts: typing.Sequence[builtins.str],
        ignore_edition_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param accounts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#accounts Database#accounts}.
        :param ignore_edition_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#ignore_edition_check Database#ignore_edition_check}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseReplicationConfiguration.__init__)
            check_type(argname="argument accounts", value=accounts, expected_type=type_hints["accounts"])
            check_type(argname="argument ignore_edition_check", value=ignore_edition_check, expected_type=type_hints["ignore_edition_check"])
        self._values: typing.Dict[str, typing.Any] = {
            "accounts": accounts,
        }
        if ignore_edition_check is not None:
            self._values["ignore_edition_check"] = ignore_edition_check

    @builtins.property
    def accounts(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#accounts Database#accounts}.'''
        result = self._values.get("accounts")
        assert result is not None, "Required property 'accounts' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def ignore_edition_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#ignore_edition_check Database#ignore_edition_check}.'''
        result = self._values.get("ignore_edition_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseReplicationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseReplicationConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.database.DatabaseReplicationConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseReplicationConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIgnoreEditionCheck")
    def reset_ignore_edition_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreEditionCheck", []))

    @builtins.property
    @jsii.member(jsii_name="accountsInput")
    def accounts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "accountsInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreEditionCheckInput")
    def ignore_edition_check_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreEditionCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="accounts")
    def accounts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "accounts"))

    @accounts.setter
    def accounts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseReplicationConfigurationOutputReference, "accounts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accounts", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreEditionCheck")
    def ignore_edition_check(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreEditionCheck"))

    @ignore_edition_check.setter
    def ignore_edition_check(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseReplicationConfigurationOutputReference, "ignore_edition_check").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreEditionCheck", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatabaseReplicationConfiguration]:
        return typing.cast(typing.Optional[DatabaseReplicationConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseReplicationConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseReplicationConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.database.DatabaseTag",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "value": "value",
        "database": "database",
        "schema": "schema",
    },
)
class DatabaseTag:
    def __init__(
        self,
        *,
        name: builtins.str,
        value: builtins.str,
        database: typing.Optional[builtins.str] = None,
        schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Tag name, e.g. department. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#name Database#name}
        :param value: Tag value, e.g. marketing_info. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#value Database#value}
        :param database: Name of the database that the tag was created in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#database Database#database}
        :param schema: Name of the schema that the tag was created in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#schema Database#schema}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseTag.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }
        if database is not None:
            self._values["database"] = database
        if schema is not None:
            self._values["schema"] = schema

    @builtins.property
    def name(self) -> builtins.str:
        '''Tag name, e.g. department.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#name Database#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Tag value, e.g. marketing_info.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#value Database#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database(self) -> typing.Optional[builtins.str]:
        '''Name of the database that the tag was created in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#database Database#database}
        '''
        result = self._values.get("database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema(self) -> typing.Optional[builtins.str]:
        '''Name of the schema that the tag was created in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/database#schema Database#schema}
        '''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseTagList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.database.DatabaseTagList",
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
            type_hints = typing.get_type_hints(DatabaseTagList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DatabaseTagOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseTagList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabaseTagOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseTagList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseTagList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabaseTagList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseTag]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseTag]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DatabaseTag]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseTagList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatabaseTagOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.database.DatabaseTagOutputReference",
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
            type_hints = typing.get_type_hints(DatabaseTagOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDatabase")
    def reset_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabase", []))

    @jsii.member(jsii_name="resetSchema")
    def reset_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchema", []))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseTagOutputReference, "database").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseTagOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseTagOutputReference, "schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseTagOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseTag, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseTag, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseTag, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseTagOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Database",
    "DatabaseConfig",
    "DatabaseReplicationConfiguration",
    "DatabaseReplicationConfigurationOutputReference",
    "DatabaseTag",
    "DatabaseTagList",
    "DatabaseTagOutputReference",
]

publication.publish()
