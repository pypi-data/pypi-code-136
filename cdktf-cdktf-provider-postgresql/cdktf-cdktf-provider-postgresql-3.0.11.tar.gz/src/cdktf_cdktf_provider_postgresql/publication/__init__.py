'''
# `postgresql_publication`

Refer to the Terraform Registory for docs: [`postgresql_publication`](https://www.terraform.io/docs/providers/postgresql/r/publication).
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


class Publication(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-postgresql.publication.Publication",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/postgresql/r/publication postgresql_publication}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        all_tables: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        database: typing.Optional[builtins.str] = None,
        drop_cascade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        publish_param: typing.Optional[typing.Sequence[builtins.str]] = None,
        publish_via_partition_root_param: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tables: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/postgresql/r/publication postgresql_publication} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#name Publication#name}.
        :param all_tables: Sets the tables list to publish to ALL tables. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#all_tables Publication#all_tables}
        :param database: Sets the database to add the publication for. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#database Publication#database}
        :param drop_cascade: When true, will also drop all the objects that depend on the publication, and in turn all objects that depend on those objects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#drop_cascade Publication#drop_cascade}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#id Publication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param owner: Sets the owner of the publication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#owner Publication#owner}
        :param publish_param: Sets which DML operations will be published. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#publish_param Publication#publish_param}
        :param publish_via_partition_root_param: Sets whether changes in a partitioned table using the identity and schema of the partitioned table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#publish_via_partition_root_param Publication#publish_via_partition_root_param}
        :param tables: Sets the tables list to publish. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#tables Publication#tables}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Publication.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PublicationConfig(
            name=name,
            all_tables=all_tables,
            database=database,
            drop_cascade=drop_cascade,
            id=id,
            owner=owner,
            publish_param=publish_param,
            publish_via_partition_root_param=publish_via_partition_root_param,
            tables=tables,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAllTables")
    def reset_all_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllTables", []))

    @jsii.member(jsii_name="resetDatabase")
    def reset_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabase", []))

    @jsii.member(jsii_name="resetDropCascade")
    def reset_drop_cascade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDropCascade", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOwner")
    def reset_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwner", []))

    @jsii.member(jsii_name="resetPublishParam")
    def reset_publish_param(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublishParam", []))

    @jsii.member(jsii_name="resetPublishViaPartitionRootParam")
    def reset_publish_via_partition_root_param(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublishViaPartitionRootParam", []))

    @jsii.member(jsii_name="resetTables")
    def reset_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTables", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allTablesInput")
    def all_tables_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="dropCascadeInput")
    def drop_cascade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dropCascadeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="publishParamInput")
    def publish_param_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "publishParamInput"))

    @builtins.property
    @jsii.member(jsii_name="publishViaPartitionRootParamInput")
    def publish_via_partition_root_param_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publishViaPartitionRootParamInput"))

    @builtins.property
    @jsii.member(jsii_name="tablesInput")
    def tables_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tablesInput"))

    @builtins.property
    @jsii.member(jsii_name="allTables")
    def all_tables(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allTables"))

    @all_tables.setter
    def all_tables(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Publication, "all_tables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allTables", value)

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Publication, "database").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="dropCascade")
    def drop_cascade(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dropCascade"))

    @drop_cascade.setter
    def drop_cascade(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Publication, "drop_cascade").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dropCascade", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Publication, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Publication, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Publication, "owner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="publishParam")
    def publish_param(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "publishParam"))

    @publish_param.setter
    def publish_param(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Publication, "publish_param").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishParam", value)

    @builtins.property
    @jsii.member(jsii_name="publishViaPartitionRootParam")
    def publish_via_partition_root_param(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publishViaPartitionRootParam"))

    @publish_via_partition_root_param.setter
    def publish_via_partition_root_param(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Publication, "publish_via_partition_root_param").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishViaPartitionRootParam", value)

    @builtins.property
    @jsii.member(jsii_name="tables")
    def tables(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tables"))

    @tables.setter
    def tables(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Publication, "tables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tables", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-postgresql.publication.PublicationConfig",
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
        "all_tables": "allTables",
        "database": "database",
        "drop_cascade": "dropCascade",
        "id": "id",
        "owner": "owner",
        "publish_param": "publishParam",
        "publish_via_partition_root_param": "publishViaPartitionRootParam",
        "tables": "tables",
    },
)
class PublicationConfig(cdktf.TerraformMetaArguments):
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
        all_tables: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        database: typing.Optional[builtins.str] = None,
        drop_cascade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        publish_param: typing.Optional[typing.Sequence[builtins.str]] = None,
        publish_via_partition_root_param: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tables: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#name Publication#name}.
        :param all_tables: Sets the tables list to publish to ALL tables. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#all_tables Publication#all_tables}
        :param database: Sets the database to add the publication for. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#database Publication#database}
        :param drop_cascade: When true, will also drop all the objects that depend on the publication, and in turn all objects that depend on those objects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#drop_cascade Publication#drop_cascade}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#id Publication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param owner: Sets the owner of the publication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#owner Publication#owner}
        :param publish_param: Sets which DML operations will be published. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#publish_param Publication#publish_param}
        :param publish_via_partition_root_param: Sets whether changes in a partitioned table using the identity and schema of the partitioned table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#publish_via_partition_root_param Publication#publish_via_partition_root_param}
        :param tables: Sets the tables list to publish. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#tables Publication#tables}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(PublicationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument all_tables", value=all_tables, expected_type=type_hints["all_tables"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument drop_cascade", value=drop_cascade, expected_type=type_hints["drop_cascade"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument publish_param", value=publish_param, expected_type=type_hints["publish_param"])
            check_type(argname="argument publish_via_partition_root_param", value=publish_via_partition_root_param, expected_type=type_hints["publish_via_partition_root_param"])
            check_type(argname="argument tables", value=tables, expected_type=type_hints["tables"])
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
        if all_tables is not None:
            self._values["all_tables"] = all_tables
        if database is not None:
            self._values["database"] = database
        if drop_cascade is not None:
            self._values["drop_cascade"] = drop_cascade
        if id is not None:
            self._values["id"] = id
        if owner is not None:
            self._values["owner"] = owner
        if publish_param is not None:
            self._values["publish_param"] = publish_param
        if publish_via_partition_root_param is not None:
            self._values["publish_via_partition_root_param"] = publish_via_partition_root_param
        if tables is not None:
            self._values["tables"] = tables

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#name Publication#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def all_tables(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Sets the tables list to publish to ALL tables.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#all_tables Publication#all_tables}
        '''
        result = self._values.get("all_tables")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def database(self) -> typing.Optional[builtins.str]:
        '''Sets the database to add the publication for.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#database Publication#database}
        '''
        result = self._values.get("database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def drop_cascade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, will also drop all the objects that depend on the publication, and in turn all objects that depend on those objects.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#drop_cascade Publication#drop_cascade}
        '''
        result = self._values.get("drop_cascade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#id Publication#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner(self) -> typing.Optional[builtins.str]:
        '''Sets the owner of the publication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#owner Publication#owner}
        '''
        result = self._values.get("owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publish_param(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Sets which DML operations will be published.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#publish_param Publication#publish_param}
        '''
        result = self._values.get("publish_param")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def publish_via_partition_root_param(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Sets whether changes in a partitioned table using the identity and schema of the partitioned table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#publish_via_partition_root_param Publication#publish_via_partition_root_param}
        '''
        result = self._values.get("publish_via_partition_root_param")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tables(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Sets the tables list to publish.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/publication#tables Publication#tables}
        '''
        result = self._values.get("tables")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublicationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Publication",
    "PublicationConfig",
]

publication.publish()
