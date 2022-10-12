'''
# `azurerm_sql_server`

Refer to the Terraform Registory for docs: [`azurerm_sql_server`](https://www.terraform.io/docs/providers/azurerm/r/sql_server).
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


class SqlServer(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sqlServer.SqlServer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server azurerm_sql_server}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        administrator_login: builtins.str,
        administrator_login_password: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        version: builtins.str,
        connection_policy: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["SqlServerIdentity", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        threat_detection_policy: typing.Optional[typing.Union["SqlServerThreatDetectionPolicy", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["SqlServerTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server azurerm_sql_server} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param administrator_login: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#administrator_login SqlServer#administrator_login}.
        :param administrator_login_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#administrator_login_password SqlServer#administrator_login_password}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#location SqlServer#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#name SqlServer#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#resource_group_name SqlServer#resource_group_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#version SqlServer#version}.
        :param connection_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#connection_policy SqlServer#connection_policy}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#id SqlServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#identity SqlServer#identity}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#tags SqlServer#tags}.
        :param threat_detection_policy: threat_detection_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#threat_detection_policy SqlServer#threat_detection_policy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#timeouts SqlServer#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlServer.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SqlServerConfig(
            administrator_login=administrator_login,
            administrator_login_password=administrator_login_password,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            version=version,
            connection_policy=connection_policy,
            id=id,
            identity=identity,
            tags=tags,
            threat_detection_policy=threat_detection_policy,
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

    @jsii.member(jsii_name="putIdentity")
    def put_identity(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#type SqlServer#type}.
        '''
        value = SqlServerIdentity(type=type)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putThreatDetectionPolicy")
    def put_threat_detection_policy(
        self,
        *,
        disabled_alerts: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_account_admins: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        email_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        retention_days: typing.Optional[jsii.Number] = None,
        state: typing.Optional[builtins.str] = None,
        storage_account_access_key: typing.Optional[builtins.str] = None,
        storage_endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disabled_alerts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#disabled_alerts SqlServer#disabled_alerts}.
        :param email_account_admins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#email_account_admins SqlServer#email_account_admins}.
        :param email_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#email_addresses SqlServer#email_addresses}.
        :param retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#retention_days SqlServer#retention_days}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#state SqlServer#state}.
        :param storage_account_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#storage_account_access_key SqlServer#storage_account_access_key}.
        :param storage_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#storage_endpoint SqlServer#storage_endpoint}.
        '''
        value = SqlServerThreatDetectionPolicy(
            disabled_alerts=disabled_alerts,
            email_account_admins=email_account_admins,
            email_addresses=email_addresses,
            retention_days=retention_days,
            state=state,
            storage_account_access_key=storage_account_access_key,
            storage_endpoint=storage_endpoint,
        )

        return typing.cast(None, jsii.invoke(self, "putThreatDetectionPolicy", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#create SqlServer#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#delete SqlServer#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#read SqlServer#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#update SqlServer#update}.
        '''
        value = SqlServerTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetConnectionPolicy")
    def reset_connection_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionPolicy", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetThreatDetectionPolicy")
    def reset_threat_detection_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThreatDetectionPolicy", []))

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
    @jsii.member(jsii_name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fullyQualifiedDomainName"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "SqlServerIdentityOutputReference":
        return typing.cast("SqlServerIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="threatDetectionPolicy")
    def threat_detection_policy(
        self,
    ) -> "SqlServerThreatDetectionPolicyOutputReference":
        return typing.cast("SqlServerThreatDetectionPolicyOutputReference", jsii.get(self, "threatDetectionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SqlServerTimeoutsOutputReference":
        return typing.cast("SqlServerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="administratorLoginInput")
    def administrator_login_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "administratorLoginInput"))

    @builtins.property
    @jsii.member(jsii_name="administratorLoginPasswordInput")
    def administrator_login_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "administratorLoginPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionPolicyInput")
    def connection_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["SqlServerIdentity"]:
        return typing.cast(typing.Optional["SqlServerIdentity"], jsii.get(self, "identityInput"))

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
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="threatDetectionPolicyInput")
    def threat_detection_policy_input(
        self,
    ) -> typing.Optional["SqlServerThreatDetectionPolicy"]:
        return typing.cast(typing.Optional["SqlServerThreatDetectionPolicy"], jsii.get(self, "threatDetectionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SqlServerTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SqlServerTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="administratorLogin")
    def administrator_login(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "administratorLogin"))

    @administrator_login.setter
    def administrator_login(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServer, "administrator_login").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "administratorLogin", value)

    @builtins.property
    @jsii.member(jsii_name="administratorLoginPassword")
    def administrator_login_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "administratorLoginPassword"))

    @administrator_login_password.setter
    def administrator_login_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServer, "administrator_login_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "administratorLoginPassword", value)

    @builtins.property
    @jsii.member(jsii_name="connectionPolicy")
    def connection_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionPolicy"))

    @connection_policy.setter
    def connection_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServer, "connection_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServer, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServer, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServer, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServer, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServer, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServer, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.sqlServer.SqlServerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "administrator_login": "administratorLogin",
        "administrator_login_password": "administratorLoginPassword",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "version": "version",
        "connection_policy": "connectionPolicy",
        "id": "id",
        "identity": "identity",
        "tags": "tags",
        "threat_detection_policy": "threatDetectionPolicy",
        "timeouts": "timeouts",
    },
)
class SqlServerConfig(cdktf.TerraformMetaArguments):
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
        administrator_login: builtins.str,
        administrator_login_password: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        version: builtins.str,
        connection_policy: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["SqlServerIdentity", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        threat_detection_policy: typing.Optional[typing.Union["SqlServerThreatDetectionPolicy", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["SqlServerTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param administrator_login: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#administrator_login SqlServer#administrator_login}.
        :param administrator_login_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#administrator_login_password SqlServer#administrator_login_password}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#location SqlServer#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#name SqlServer#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#resource_group_name SqlServer#resource_group_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#version SqlServer#version}.
        :param connection_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#connection_policy SqlServer#connection_policy}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#id SqlServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#identity SqlServer#identity}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#tags SqlServer#tags}.
        :param threat_detection_policy: threat_detection_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#threat_detection_policy SqlServer#threat_detection_policy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#timeouts SqlServer#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(identity, dict):
            identity = SqlServerIdentity(**identity)
        if isinstance(threat_detection_policy, dict):
            threat_detection_policy = SqlServerThreatDetectionPolicy(**threat_detection_policy)
        if isinstance(timeouts, dict):
            timeouts = SqlServerTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SqlServerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument administrator_login", value=administrator_login, expected_type=type_hints["administrator_login"])
            check_type(argname="argument administrator_login_password", value=administrator_login_password, expected_type=type_hints["administrator_login_password"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument connection_policy", value=connection_policy, expected_type=type_hints["connection_policy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument threat_detection_policy", value=threat_detection_policy, expected_type=type_hints["threat_detection_policy"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "administrator_login": administrator_login,
            "administrator_login_password": administrator_login_password,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "version": version,
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
        if connection_policy is not None:
            self._values["connection_policy"] = connection_policy
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if tags is not None:
            self._values["tags"] = tags
        if threat_detection_policy is not None:
            self._values["threat_detection_policy"] = threat_detection_policy
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
    def administrator_login(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#administrator_login SqlServer#administrator_login}.'''
        result = self._values.get("administrator_login")
        assert result is not None, "Required property 'administrator_login' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def administrator_login_password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#administrator_login_password SqlServer#administrator_login_password}.'''
        result = self._values.get("administrator_login_password")
        assert result is not None, "Required property 'administrator_login_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#location SqlServer#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#name SqlServer#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#resource_group_name SqlServer#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#version SqlServer#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#connection_policy SqlServer#connection_policy}.'''
        result = self._values.get("connection_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#id SqlServer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["SqlServerIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#identity SqlServer#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["SqlServerIdentity"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#tags SqlServer#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def threat_detection_policy(
        self,
    ) -> typing.Optional["SqlServerThreatDetectionPolicy"]:
        '''threat_detection_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#threat_detection_policy SqlServer#threat_detection_policy}
        '''
        result = self._values.get("threat_detection_policy")
        return typing.cast(typing.Optional["SqlServerThreatDetectionPolicy"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SqlServerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#timeouts SqlServer#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SqlServerTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlServerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.sqlServer.SqlServerIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class SqlServerIdentity:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#type SqlServer#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlServerIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#type SqlServer#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlServerIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlServerIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sqlServer.SqlServerIdentityOutputReference",
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
            type_hints = typing.get_type_hints(SqlServerIdentityOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SqlServerIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlServerIdentity]:
        return typing.cast(typing.Optional[SqlServerIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlServerIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServerIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.sqlServer.SqlServerThreatDetectionPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "disabled_alerts": "disabledAlerts",
        "email_account_admins": "emailAccountAdmins",
        "email_addresses": "emailAddresses",
        "retention_days": "retentionDays",
        "state": "state",
        "storage_account_access_key": "storageAccountAccessKey",
        "storage_endpoint": "storageEndpoint",
    },
)
class SqlServerThreatDetectionPolicy:
    def __init__(
        self,
        *,
        disabled_alerts: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_account_admins: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        email_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        retention_days: typing.Optional[jsii.Number] = None,
        state: typing.Optional[builtins.str] = None,
        storage_account_access_key: typing.Optional[builtins.str] = None,
        storage_endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disabled_alerts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#disabled_alerts SqlServer#disabled_alerts}.
        :param email_account_admins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#email_account_admins SqlServer#email_account_admins}.
        :param email_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#email_addresses SqlServer#email_addresses}.
        :param retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#retention_days SqlServer#retention_days}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#state SqlServer#state}.
        :param storage_account_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#storage_account_access_key SqlServer#storage_account_access_key}.
        :param storage_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#storage_endpoint SqlServer#storage_endpoint}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlServerThreatDetectionPolicy.__init__)
            check_type(argname="argument disabled_alerts", value=disabled_alerts, expected_type=type_hints["disabled_alerts"])
            check_type(argname="argument email_account_admins", value=email_account_admins, expected_type=type_hints["email_account_admins"])
            check_type(argname="argument email_addresses", value=email_addresses, expected_type=type_hints["email_addresses"])
            check_type(argname="argument retention_days", value=retention_days, expected_type=type_hints["retention_days"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument storage_account_access_key", value=storage_account_access_key, expected_type=type_hints["storage_account_access_key"])
            check_type(argname="argument storage_endpoint", value=storage_endpoint, expected_type=type_hints["storage_endpoint"])
        self._values: typing.Dict[str, typing.Any] = {}
        if disabled_alerts is not None:
            self._values["disabled_alerts"] = disabled_alerts
        if email_account_admins is not None:
            self._values["email_account_admins"] = email_account_admins
        if email_addresses is not None:
            self._values["email_addresses"] = email_addresses
        if retention_days is not None:
            self._values["retention_days"] = retention_days
        if state is not None:
            self._values["state"] = state
        if storage_account_access_key is not None:
            self._values["storage_account_access_key"] = storage_account_access_key
        if storage_endpoint is not None:
            self._values["storage_endpoint"] = storage_endpoint

    @builtins.property
    def disabled_alerts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#disabled_alerts SqlServer#disabled_alerts}.'''
        result = self._values.get("disabled_alerts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email_account_admins(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#email_account_admins SqlServer#email_account_admins}.'''
        result = self._values.get("email_account_admins")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def email_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#email_addresses SqlServer#email_addresses}.'''
        result = self._values.get("email_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def retention_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#retention_days SqlServer#retention_days}.'''
        result = self._values.get("retention_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#state SqlServer#state}.'''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_access_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#storage_account_access_key SqlServer#storage_account_access_key}.'''
        result = self._values.get("storage_account_access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#storage_endpoint SqlServer#storage_endpoint}.'''
        result = self._values.get("storage_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlServerThreatDetectionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlServerThreatDetectionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sqlServer.SqlServerThreatDetectionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(SqlServerThreatDetectionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDisabledAlerts")
    def reset_disabled_alerts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabledAlerts", []))

    @jsii.member(jsii_name="resetEmailAccountAdmins")
    def reset_email_account_admins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailAccountAdmins", []))

    @jsii.member(jsii_name="resetEmailAddresses")
    def reset_email_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailAddresses", []))

    @jsii.member(jsii_name="resetRetentionDays")
    def reset_retention_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionDays", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetStorageAccountAccessKey")
    def reset_storage_account_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountAccessKey", []))

    @jsii.member(jsii_name="resetStorageEndpoint")
    def reset_storage_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageEndpoint", []))

    @builtins.property
    @jsii.member(jsii_name="disabledAlertsInput")
    def disabled_alerts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "disabledAlertsInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAccountAdminsInput")
    def email_account_admins_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "emailAccountAdminsInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAddressesInput")
    def email_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionDaysInput")
    def retention_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountAccessKeyInput")
    def storage_account_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="storageEndpointInput")
    def storage_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledAlerts")
    def disabled_alerts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "disabledAlerts"))

    @disabled_alerts.setter
    def disabled_alerts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServerThreatDetectionPolicyOutputReference, "disabled_alerts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabledAlerts", value)

    @builtins.property
    @jsii.member(jsii_name="emailAccountAdmins")
    def email_account_admins(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "emailAccountAdmins"))

    @email_account_admins.setter
    def email_account_admins(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServerThreatDetectionPolicyOutputReference, "email_account_admins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAccountAdmins", value)

    @builtins.property
    @jsii.member(jsii_name="emailAddresses")
    def email_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emailAddresses"))

    @email_addresses.setter
    def email_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServerThreatDetectionPolicyOutputReference, "email_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="retentionDays")
    def retention_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionDays"))

    @retention_days.setter
    def retention_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServerThreatDetectionPolicyOutputReference, "retention_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionDays", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServerThreatDetectionPolicyOutputReference, "state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountAccessKey")
    def storage_account_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountAccessKey"))

    @storage_account_access_key.setter
    def storage_account_access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServerThreatDetectionPolicyOutputReference, "storage_account_access_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountAccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="storageEndpoint")
    def storage_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageEndpoint"))

    @storage_endpoint.setter
    def storage_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServerThreatDetectionPolicyOutputReference, "storage_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlServerThreatDetectionPolicy]:
        return typing.cast(typing.Optional[SqlServerThreatDetectionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlServerThreatDetectionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServerThreatDetectionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.sqlServer.SqlServerTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SqlServerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#create SqlServer#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#delete SqlServer#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#read SqlServer#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#update SqlServer#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlServerTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#create SqlServer#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#delete SqlServer#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#read SqlServer#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sql_server#update SqlServer#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlServerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlServerTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sqlServer.SqlServerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SqlServerTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SqlServerTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServerTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServerTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServerTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SqlServerTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SqlServerTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SqlServerTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlServerTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SqlServer",
    "SqlServerConfig",
    "SqlServerIdentity",
    "SqlServerIdentityOutputReference",
    "SqlServerThreatDetectionPolicy",
    "SqlServerThreatDetectionPolicyOutputReference",
    "SqlServerTimeouts",
    "SqlServerTimeoutsOutputReference",
]

publication.publish()
