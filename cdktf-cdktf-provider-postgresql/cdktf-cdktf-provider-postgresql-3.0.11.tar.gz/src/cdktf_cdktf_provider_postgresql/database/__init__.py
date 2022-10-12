'''
# `postgresql_database`

Refer to the Terraform Registory for docs: [`postgresql_database`](https://www.terraform.io/docs/providers/postgresql/r/database).
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
    jsii_type="@cdktf/provider-postgresql.database.Database",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/postgresql/r/database postgresql_database}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        allow_connections: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection_limit: typing.Optional[jsii.Number] = None,
        encoding: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        is_template: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        lc_collate: typing.Optional[builtins.str] = None,
        lc_ctype: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        tablespace_name: typing.Optional[builtins.str] = None,
        template: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/postgresql/r/database postgresql_database} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The PostgreSQL database name to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#name Database#name}
        :param allow_connections: If false then no one can connect to this database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#allow_connections Database#allow_connections}
        :param connection_limit: How many concurrent connections can be made to this database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#connection_limit Database#connection_limit}
        :param encoding: Character set encoding to use in the new database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#encoding Database#encoding}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#id Database#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_template: If true, then this database can be cloned by any user with CREATEDB privileges. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#is_template Database#is_template}
        :param lc_collate: Collation order (LC_COLLATE) to use in the new database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#lc_collate Database#lc_collate}
        :param lc_ctype: Character classification (LC_CTYPE) to use in the new database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#lc_ctype Database#lc_ctype}
        :param owner: The ROLE which owns the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#owner Database#owner}
        :param tablespace_name: The name of the tablespace that will be associated with the new database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#tablespace_name Database#tablespace_name}
        :param template: The name of the template from which to create the new database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#template Database#template}
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
            allow_connections=allow_connections,
            connection_limit=connection_limit,
            encoding=encoding,
            id=id,
            is_template=is_template,
            lc_collate=lc_collate,
            lc_ctype=lc_ctype,
            owner=owner,
            tablespace_name=tablespace_name,
            template=template,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAllowConnections")
    def reset_allow_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowConnections", []))

    @jsii.member(jsii_name="resetConnectionLimit")
    def reset_connection_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionLimit", []))

    @jsii.member(jsii_name="resetEncoding")
    def reset_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncoding", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsTemplate")
    def reset_is_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsTemplate", []))

    @jsii.member(jsii_name="resetLcCollate")
    def reset_lc_collate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLcCollate", []))

    @jsii.member(jsii_name="resetLcCtype")
    def reset_lc_ctype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLcCtype", []))

    @jsii.member(jsii_name="resetOwner")
    def reset_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwner", []))

    @jsii.member(jsii_name="resetTablespaceName")
    def reset_tablespace_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTablespaceName", []))

    @jsii.member(jsii_name="resetTemplate")
    def reset_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplate", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allowConnectionsInput")
    def allow_connections_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionLimitInput")
    def connection_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectionLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="encodingInput")
    def encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encodingInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isTemplateInput")
    def is_template_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="lcCollateInput")
    def lc_collate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lcCollateInput"))

    @builtins.property
    @jsii.member(jsii_name="lcCtypeInput")
    def lc_ctype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lcCtypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="tablespaceNameInput")
    def tablespace_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tablespaceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="templateInput")
    def template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateInput"))

    @builtins.property
    @jsii.member(jsii_name="allowConnections")
    def allow_connections(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowConnections"))

    @allow_connections.setter
    def allow_connections(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "allow_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowConnections", value)

    @builtins.property
    @jsii.member(jsii_name="connectionLimit")
    def connection_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "connectionLimit"))

    @connection_limit.setter
    def connection_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "connection_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionLimit", value)

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @encoding.setter
    def encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "encoding").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encoding", value)

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
    @jsii.member(jsii_name="isTemplate")
    def is_template(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isTemplate"))

    @is_template.setter
    def is_template(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "is_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="lcCollate")
    def lc_collate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lcCollate"))

    @lc_collate.setter
    def lc_collate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "lc_collate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lcCollate", value)

    @builtins.property
    @jsii.member(jsii_name="lcCtype")
    def lc_ctype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lcCtype"))

    @lc_ctype.setter
    def lc_ctype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "lc_ctype").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lcCtype", value)

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

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "owner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="tablespaceName")
    def tablespace_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tablespaceName"))

    @tablespace_name.setter
    def tablespace_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "tablespace_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tablespaceName", value)

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "template"))

    @template.setter
    def template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Database, "template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "template", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-postgresql.database.DatabaseConfig",
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
        "allow_connections": "allowConnections",
        "connection_limit": "connectionLimit",
        "encoding": "encoding",
        "id": "id",
        "is_template": "isTemplate",
        "lc_collate": "lcCollate",
        "lc_ctype": "lcCtype",
        "owner": "owner",
        "tablespace_name": "tablespaceName",
        "template": "template",
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
        allow_connections: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection_limit: typing.Optional[jsii.Number] = None,
        encoding: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        is_template: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        lc_collate: typing.Optional[builtins.str] = None,
        lc_ctype: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        tablespace_name: typing.Optional[builtins.str] = None,
        template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The PostgreSQL database name to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#name Database#name}
        :param allow_connections: If false then no one can connect to this database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#allow_connections Database#allow_connections}
        :param connection_limit: How many concurrent connections can be made to this database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#connection_limit Database#connection_limit}
        :param encoding: Character set encoding to use in the new database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#encoding Database#encoding}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#id Database#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_template: If true, then this database can be cloned by any user with CREATEDB privileges. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#is_template Database#is_template}
        :param lc_collate: Collation order (LC_COLLATE) to use in the new database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#lc_collate Database#lc_collate}
        :param lc_ctype: Character classification (LC_CTYPE) to use in the new database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#lc_ctype Database#lc_ctype}
        :param owner: The ROLE which owns the database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#owner Database#owner}
        :param tablespace_name: The name of the tablespace that will be associated with the new database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#tablespace_name Database#tablespace_name}
        :param template: The name of the template from which to create the new database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#template Database#template}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
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
            check_type(argname="argument allow_connections", value=allow_connections, expected_type=type_hints["allow_connections"])
            check_type(argname="argument connection_limit", value=connection_limit, expected_type=type_hints["connection_limit"])
            check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_template", value=is_template, expected_type=type_hints["is_template"])
            check_type(argname="argument lc_collate", value=lc_collate, expected_type=type_hints["lc_collate"])
            check_type(argname="argument lc_ctype", value=lc_ctype, expected_type=type_hints["lc_ctype"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument tablespace_name", value=tablespace_name, expected_type=type_hints["tablespace_name"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
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
        if allow_connections is not None:
            self._values["allow_connections"] = allow_connections
        if connection_limit is not None:
            self._values["connection_limit"] = connection_limit
        if encoding is not None:
            self._values["encoding"] = encoding
        if id is not None:
            self._values["id"] = id
        if is_template is not None:
            self._values["is_template"] = is_template
        if lc_collate is not None:
            self._values["lc_collate"] = lc_collate
        if lc_ctype is not None:
            self._values["lc_ctype"] = lc_ctype
        if owner is not None:
            self._values["owner"] = owner
        if tablespace_name is not None:
            self._values["tablespace_name"] = tablespace_name
        if template is not None:
            self._values["template"] = template

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
        '''The PostgreSQL database name to connect to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#name Database#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_connections(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If false then no one can connect to this database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#allow_connections Database#allow_connections}
        '''
        result = self._values.get("allow_connections")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def connection_limit(self) -> typing.Optional[jsii.Number]:
        '''How many concurrent connections can be made to this database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#connection_limit Database#connection_limit}
        '''
        result = self._values.get("connection_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def encoding(self) -> typing.Optional[builtins.str]:
        '''Character set encoding to use in the new database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#encoding Database#encoding}
        '''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#id Database#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_template(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, then this database can be cloned by any user with CREATEDB privileges.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#is_template Database#is_template}
        '''
        result = self._values.get("is_template")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def lc_collate(self) -> typing.Optional[builtins.str]:
        '''Collation order (LC_COLLATE) to use in the new database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#lc_collate Database#lc_collate}
        '''
        result = self._values.get("lc_collate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lc_ctype(self) -> typing.Optional[builtins.str]:
        '''Character classification (LC_CTYPE) to use in the new database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#lc_ctype Database#lc_ctype}
        '''
        result = self._values.get("lc_ctype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner(self) -> typing.Optional[builtins.str]:
        '''The ROLE which owns the database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#owner Database#owner}
        '''
        result = self._values.get("owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tablespace_name(self) -> typing.Optional[builtins.str]:
        '''The name of the tablespace that will be associated with the new database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#tablespace_name Database#tablespace_name}
        '''
        result = self._values.get("tablespace_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template(self) -> typing.Optional[builtins.str]:
        '''The name of the template from which to create the new database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/postgresql/r/database#template Database#template}
        '''
        result = self._values.get("template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Database",
    "DatabaseConfig",
]

publication.publish()
