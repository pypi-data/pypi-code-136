'''
# `cloudflare_access_group`

Refer to the Terraform Registory for docs: [`cloudflare_access_group`](https://www.terraform.io/docs/providers/cloudflare/r/access_group).
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


class AccessGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group cloudflare_access_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        include: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupInclude", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        exclude: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupExclude", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        require: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupRequire", typing.Dict[str, typing.Any]]]]] = None,
        zone_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group cloudflare_access_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param include: include block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#include AccessGroup#include}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#name AccessGroup#name}.
        :param account_id: The account identifier to target for the resource. Conflicts with ``zone_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#account_id AccessGroup#account_id}
        :param exclude: exclude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#exclude AccessGroup#exclude}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#id AccessGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param require: require block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#require AccessGroup#require}
        :param zone_id: The zone identifier to target for the resource. Conflicts with ``account_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#zone_id AccessGroup#zone_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AccessGroupConfig(
            include=include,
            name=name,
            account_id=account_id,
            exclude=exclude,
            id=id,
            require=require,
            zone_id=zone_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putExclude")
    def put_exclude(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupExclude", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroup.put_exclude)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExclude", [value]))

    @jsii.member(jsii_name="putInclude")
    def put_include(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupInclude", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroup.put_include)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInclude", [value]))

    @jsii.member(jsii_name="putRequire")
    def put_require(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupRequire", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroup.put_require)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequire", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetExclude")
    def reset_exclude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclude", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRequire")
    def reset_require(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequire", []))

    @jsii.member(jsii_name="resetZoneId")
    def reset_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="exclude")
    def exclude(self) -> "AccessGroupExcludeList":
        return typing.cast("AccessGroupExcludeList", jsii.get(self, "exclude"))

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(self) -> "AccessGroupIncludeList":
        return typing.cast("AccessGroupIncludeList", jsii.get(self, "include"))

    @builtins.property
    @jsii.member(jsii_name="require")
    def require(self) -> "AccessGroupRequireList":
        return typing.cast("AccessGroupRequireList", jsii.get(self, "require"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeInput")
    def exclude_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExclude"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExclude"]]], jsii.get(self, "excludeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInput")
    def include_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupInclude"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupInclude"]]], jsii.get(self, "includeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="requireInput")
    def require_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequire"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequire"]]], jsii.get(self, "requireInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroup, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroup, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "include": "include",
        "name": "name",
        "account_id": "accountId",
        "exclude": "exclude",
        "id": "id",
        "require": "require",
        "zone_id": "zoneId",
    },
)
class AccessGroupConfig(cdktf.TerraformMetaArguments):
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
        include: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupInclude", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        exclude: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupExclude", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        require: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupRequire", typing.Dict[str, typing.Any]]]]] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param include: include block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#include AccessGroup#include}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#name AccessGroup#name}.
        :param account_id: The account identifier to target for the resource. Conflicts with ``zone_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#account_id AccessGroup#account_id}
        :param exclude: exclude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#exclude AccessGroup#exclude}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#id AccessGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param require: require block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#require AccessGroup#require}
        :param zone_id: The zone identifier to target for the resource. Conflicts with ``account_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#zone_id AccessGroup#zone_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument require", value=require, expected_type=type_hints["require"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "include": include,
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if exclude is not None:
            self._values["exclude"] = exclude
        if id is not None:
            self._values["id"] = id
        if require is not None:
            self._values["require"] = require
        if zone_id is not None:
            self._values["zone_id"] = zone_id

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
    def include(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["AccessGroupInclude"]]:
        '''include block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#include AccessGroup#include}
        '''
        result = self._values.get("include")
        assert result is not None, "Required property 'include' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["AccessGroupInclude"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#name AccessGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''The account identifier to target for the resource. Conflicts with ``zone_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#account_id AccessGroup#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclude(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExclude"]]]:
        '''exclude block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#exclude AccessGroup#exclude}
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExclude"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#id AccessGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def require(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequire"]]]:
        '''require block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#require AccessGroup#require}
        '''
        result = self._values.get("require")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequire"]]], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''The zone identifier to target for the resource. Conflicts with ``account_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#zone_id AccessGroup#zone_id}
        '''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExclude",
    jsii_struct_bases=[],
    name_mapping={
        "any_valid_service_token": "anyValidServiceToken",
        "auth_method": "authMethod",
        "azure": "azure",
        "certificate": "certificate",
        "common_name": "commonName",
        "device_posture": "devicePosture",
        "email": "email",
        "email_domain": "emailDomain",
        "everyone": "everyone",
        "external_evaluation": "externalEvaluation",
        "geo": "geo",
        "github": "github",
        "group": "group",
        "gsuite": "gsuite",
        "ip": "ip",
        "login_method": "loginMethod",
        "okta": "okta",
        "saml": "saml",
        "service_token": "serviceToken",
    },
)
class AccessGroupExclude:
    def __init__(
        self,
        *,
        any_valid_service_token: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auth_method: typing.Optional[builtins.str] = None,
        azure: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupExcludeAzure", typing.Dict[str, typing.Any]]]]] = None,
        certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        common_name: typing.Optional[builtins.str] = None,
        device_posture: typing.Optional[typing.Sequence[builtins.str]] = None,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_domain: typing.Optional[typing.Sequence[builtins.str]] = None,
        everyone: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        external_evaluation: typing.Optional[typing.Union["AccessGroupExcludeExternalEvaluation", typing.Dict[str, typing.Any]]] = None,
        geo: typing.Optional[typing.Sequence[builtins.str]] = None,
        github: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupExcludeGithub", typing.Dict[str, typing.Any]]]]] = None,
        group: typing.Optional[typing.Sequence[builtins.str]] = None,
        gsuite: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupExcludeGsuite", typing.Dict[str, typing.Any]]]]] = None,
        ip: typing.Optional[typing.Sequence[builtins.str]] = None,
        login_method: typing.Optional[typing.Sequence[builtins.str]] = None,
        okta: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupExcludeOkta", typing.Dict[str, typing.Any]]]]] = None,
        saml: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupExcludeSaml", typing.Dict[str, typing.Any]]]]] = None,
        service_token: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param any_valid_service_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#any_valid_service_token AccessGroup#any_valid_service_token}.
        :param auth_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#auth_method AccessGroup#auth_method}.
        :param azure: azure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#azure AccessGroup#azure}
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#certificate AccessGroup#certificate}.
        :param common_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#common_name AccessGroup#common_name}.
        :param device_posture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#device_posture AccessGroup#device_posture}.
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email AccessGroup#email}.
        :param email_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email_domain AccessGroup#email_domain}.
        :param everyone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#everyone AccessGroup#everyone}.
        :param external_evaluation: external_evaluation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#external_evaluation AccessGroup#external_evaluation}
        :param geo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#geo AccessGroup#geo}.
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#github AccessGroup#github}
        :param group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#group AccessGroup#group}.
        :param gsuite: gsuite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#gsuite AccessGroup#gsuite}
        :param ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#ip AccessGroup#ip}.
        :param login_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#login_method AccessGroup#login_method}.
        :param okta: okta block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#okta AccessGroup#okta}
        :param saml: saml block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#saml AccessGroup#saml}
        :param service_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#service_token AccessGroup#service_token}.
        '''
        if isinstance(external_evaluation, dict):
            external_evaluation = AccessGroupExcludeExternalEvaluation(**external_evaluation)
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExclude.__init__)
            check_type(argname="argument any_valid_service_token", value=any_valid_service_token, expected_type=type_hints["any_valid_service_token"])
            check_type(argname="argument auth_method", value=auth_method, expected_type=type_hints["auth_method"])
            check_type(argname="argument azure", value=azure, expected_type=type_hints["azure"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
            check_type(argname="argument device_posture", value=device_posture, expected_type=type_hints["device_posture"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument email_domain", value=email_domain, expected_type=type_hints["email_domain"])
            check_type(argname="argument everyone", value=everyone, expected_type=type_hints["everyone"])
            check_type(argname="argument external_evaluation", value=external_evaluation, expected_type=type_hints["external_evaluation"])
            check_type(argname="argument geo", value=geo, expected_type=type_hints["geo"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument gsuite", value=gsuite, expected_type=type_hints["gsuite"])
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
            check_type(argname="argument login_method", value=login_method, expected_type=type_hints["login_method"])
            check_type(argname="argument okta", value=okta, expected_type=type_hints["okta"])
            check_type(argname="argument saml", value=saml, expected_type=type_hints["saml"])
            check_type(argname="argument service_token", value=service_token, expected_type=type_hints["service_token"])
        self._values: typing.Dict[str, typing.Any] = {}
        if any_valid_service_token is not None:
            self._values["any_valid_service_token"] = any_valid_service_token
        if auth_method is not None:
            self._values["auth_method"] = auth_method
        if azure is not None:
            self._values["azure"] = azure
        if certificate is not None:
            self._values["certificate"] = certificate
        if common_name is not None:
            self._values["common_name"] = common_name
        if device_posture is not None:
            self._values["device_posture"] = device_posture
        if email is not None:
            self._values["email"] = email
        if email_domain is not None:
            self._values["email_domain"] = email_domain
        if everyone is not None:
            self._values["everyone"] = everyone
        if external_evaluation is not None:
            self._values["external_evaluation"] = external_evaluation
        if geo is not None:
            self._values["geo"] = geo
        if github is not None:
            self._values["github"] = github
        if group is not None:
            self._values["group"] = group
        if gsuite is not None:
            self._values["gsuite"] = gsuite
        if ip is not None:
            self._values["ip"] = ip
        if login_method is not None:
            self._values["login_method"] = login_method
        if okta is not None:
            self._values["okta"] = okta
        if saml is not None:
            self._values["saml"] = saml
        if service_token is not None:
            self._values["service_token"] = service_token

    @builtins.property
    def any_valid_service_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#any_valid_service_token AccessGroup#any_valid_service_token}.'''
        result = self._values.get("any_valid_service_token")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auth_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#auth_method AccessGroup#auth_method}.'''
        result = self._values.get("auth_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExcludeAzure"]]]:
        '''azure block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#azure AccessGroup#azure}
        '''
        result = self._values.get("azure")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExcludeAzure"]]], result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#certificate AccessGroup#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def common_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#common_name AccessGroup#common_name}.'''
        result = self._values.get("common_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_posture(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#device_posture AccessGroup#device_posture}.'''
        result = self._values.get("device_posture")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email AccessGroup#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email_domain(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email_domain AccessGroup#email_domain}.'''
        result = self._values.get("email_domain")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def everyone(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#everyone AccessGroup#everyone}.'''
        result = self._values.get("everyone")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def external_evaluation(
        self,
    ) -> typing.Optional["AccessGroupExcludeExternalEvaluation"]:
        '''external_evaluation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#external_evaluation AccessGroup#external_evaluation}
        '''
        result = self._values.get("external_evaluation")
        return typing.cast(typing.Optional["AccessGroupExcludeExternalEvaluation"], result)

    @builtins.property
    def geo(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#geo AccessGroup#geo}.'''
        result = self._values.get("geo")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def github(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExcludeGithub"]]]:
        '''github block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#github AccessGroup#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExcludeGithub"]]], result)

    @builtins.property
    def group(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#group AccessGroup#group}.'''
        result = self._values.get("group")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def gsuite(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExcludeGsuite"]]]:
        '''gsuite block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#gsuite AccessGroup#gsuite}
        '''
        result = self._values.get("gsuite")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExcludeGsuite"]]], result)

    @builtins.property
    def ip(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#ip AccessGroup#ip}.'''
        result = self._values.get("ip")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def login_method(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#login_method AccessGroup#login_method}.'''
        result = self._values.get("login_method")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def okta(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExcludeOkta"]]]:
        '''okta block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#okta AccessGroup#okta}
        '''
        result = self._values.get("okta")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExcludeOkta"]]], result)

    @builtins.property
    def saml(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExcludeSaml"]]]:
        '''saml block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#saml AccessGroup#saml}
        '''
        result = self._values.get("saml")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExcludeSaml"]]], result)

    @builtins.property
    def service_token(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#service_token AccessGroup#service_token}.'''
        result = self._values.get("service_token")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupExclude(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeAzure",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "identity_provider_id": "identityProviderId"},
)
class AccessGroupExcludeAzure:
    def __init__(
        self,
        *,
        id: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#id AccessGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeAzure.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def id(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#id AccessGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupExcludeAzure(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupExcludeAzureList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeAzureList",
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
            type_hints = typing.get_type_hints(AccessGroupExcludeAzureList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupExcludeAzureOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeAzureList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupExcludeAzureOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeAzureList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeAzureList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeAzureList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeAzure]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeAzure]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeAzure]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeAzureList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupExcludeAzureOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeAzureOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupExcludeAzureOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "id"))

    @id.setter
    def id(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeAzureOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeAzureOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupExcludeAzure, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupExcludeAzure, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupExcludeAzure, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeAzureOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeExternalEvaluation",
    jsii_struct_bases=[],
    name_mapping={"evaluate_url": "evaluateUrl", "keys_url": "keysUrl"},
)
class AccessGroupExcludeExternalEvaluation:
    def __init__(
        self,
        *,
        evaluate_url: typing.Optional[builtins.str] = None,
        keys_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param evaluate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#evaluate_url AccessGroup#evaluate_url}.
        :param keys_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#keys_url AccessGroup#keys_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeExternalEvaluation.__init__)
            check_type(argname="argument evaluate_url", value=evaluate_url, expected_type=type_hints["evaluate_url"])
            check_type(argname="argument keys_url", value=keys_url, expected_type=type_hints["keys_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if evaluate_url is not None:
            self._values["evaluate_url"] = evaluate_url
        if keys_url is not None:
            self._values["keys_url"] = keys_url

    @builtins.property
    def evaluate_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#evaluate_url AccessGroup#evaluate_url}.'''
        result = self._values.get("evaluate_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keys_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#keys_url AccessGroup#keys_url}.'''
        result = self._values.get("keys_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupExcludeExternalEvaluation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupExcludeExternalEvaluationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeExternalEvaluationOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupExcludeExternalEvaluationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEvaluateUrl")
    def reset_evaluate_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateUrl", []))

    @jsii.member(jsii_name="resetKeysUrl")
    def reset_keys_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeysUrl", []))

    @builtins.property
    @jsii.member(jsii_name="evaluateUrlInput")
    def evaluate_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluateUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="keysUrlInput")
    def keys_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keysUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateUrl")
    def evaluate_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evaluateUrl"))

    @evaluate_url.setter
    def evaluate_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeExternalEvaluationOutputReference, "evaluate_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateUrl", value)

    @builtins.property
    @jsii.member(jsii_name="keysUrl")
    def keys_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keysUrl"))

    @keys_url.setter
    def keys_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeExternalEvaluationOutputReference, "keys_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keysUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AccessGroupExcludeExternalEvaluation]:
        return typing.cast(typing.Optional[AccessGroupExcludeExternalEvaluation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AccessGroupExcludeExternalEvaluation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeExternalEvaluationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeGithub",
    jsii_struct_bases=[],
    name_mapping={
        "identity_provider_id": "identityProviderId",
        "name": "name",
        "teams": "teams",
    },
)
class AccessGroupExcludeGithub:
    def __init__(
        self,
        *,
        identity_provider_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        teams: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#name AccessGroup#name}.
        :param teams: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#teams AccessGroup#teams}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeGithub.__init__)
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument teams", value=teams, expected_type=type_hints["teams"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id
        if name is not None:
            self._values["name"] = name
        if teams is not None:
            self._values["teams"] = teams

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#name AccessGroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def teams(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#teams AccessGroup#teams}.'''
        result = self._values.get("teams")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupExcludeGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupExcludeGithubList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeGithubList",
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
            type_hints = typing.get_type_hints(AccessGroupExcludeGithubList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupExcludeGithubOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeGithubList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupExcludeGithubOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeGithubList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeGithubList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeGithubList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeGithub]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeGithub]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeGithub]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeGithubList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupExcludeGithubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeGithubOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupExcludeGithubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTeams")
    def reset_teams(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeams", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="teamsInput")
    def teams_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "teamsInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeGithubOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeGithubOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="teams")
    def teams(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "teams"))

    @teams.setter
    def teams(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeGithubOutputReference, "teams").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teams", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupExcludeGithub, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupExcludeGithub, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupExcludeGithub, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeGithubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeGsuite",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "identity_provider_id": "identityProviderId"},
)
class AccessGroupExcludeGsuite:
    def __init__(
        self,
        *,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email AccessGroup#email}.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeGsuite.__init__)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def email(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email AccessGroup#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupExcludeGsuite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupExcludeGsuiteList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeGsuiteList",
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
            type_hints = typing.get_type_hints(AccessGroupExcludeGsuiteList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupExcludeGsuiteOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeGsuiteList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupExcludeGsuiteOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeGsuiteList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeGsuiteList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeGsuiteList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeGsuite]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeGsuite]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeGsuite]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeGsuiteList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupExcludeGsuiteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeGsuiteOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupExcludeGsuiteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeGsuiteOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeGsuiteOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupExcludeGsuite, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupExcludeGsuite, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupExcludeGsuite, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeGsuiteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupExcludeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeList",
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
            type_hints = typing.get_type_hints(AccessGroupExcludeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupExcludeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupExcludeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExclude]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExclude]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExclude]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeOkta",
    jsii_struct_bases=[],
    name_mapping={"identity_provider_id": "identityProviderId", "name": "name"},
)
class AccessGroupExcludeOkta:
    def __init__(
        self,
        *,
        identity_provider_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#name AccessGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeOkta.__init__)
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#name AccessGroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupExcludeOkta(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupExcludeOktaList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeOktaList",
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
            type_hints = typing.get_type_hints(AccessGroupExcludeOktaList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupExcludeOktaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeOktaList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupExcludeOktaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOktaList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOktaList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOktaList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeOkta]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeOkta]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeOkta]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOktaList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupExcludeOktaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeOktaOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupExcludeOktaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOktaOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOktaOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupExcludeOkta, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupExcludeOkta, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupExcludeOkta, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOktaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupExcludeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupExcludeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAzure")
    def put_azure(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessGroupExcludeAzure, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeOutputReference.put_azure)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAzure", [value]))

    @jsii.member(jsii_name="putExternalEvaluation")
    def put_external_evaluation(
        self,
        *,
        evaluate_url: typing.Optional[builtins.str] = None,
        keys_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param evaluate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#evaluate_url AccessGroup#evaluate_url}.
        :param keys_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#keys_url AccessGroup#keys_url}.
        '''
        value = AccessGroupExcludeExternalEvaluation(
            evaluate_url=evaluate_url, keys_url=keys_url
        )

        return typing.cast(None, jsii.invoke(self, "putExternalEvaluation", [value]))

    @jsii.member(jsii_name="putGithub")
    def put_github(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessGroupExcludeGithub, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeOutputReference.put_github)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGithub", [value]))

    @jsii.member(jsii_name="putGsuite")
    def put_gsuite(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessGroupExcludeGsuite, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeOutputReference.put_gsuite)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGsuite", [value]))

    @jsii.member(jsii_name="putOkta")
    def put_okta(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessGroupExcludeOkta, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeOutputReference.put_okta)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOkta", [value]))

    @jsii.member(jsii_name="putSaml")
    def put_saml(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupExcludeSaml", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeOutputReference.put_saml)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSaml", [value]))

    @jsii.member(jsii_name="resetAnyValidServiceToken")
    def reset_any_valid_service_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnyValidServiceToken", []))

    @jsii.member(jsii_name="resetAuthMethod")
    def reset_auth_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthMethod", []))

    @jsii.member(jsii_name="resetAzure")
    def reset_azure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzure", []))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCommonName")
    def reset_common_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonName", []))

    @jsii.member(jsii_name="resetDevicePosture")
    def reset_device_posture(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevicePosture", []))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetEmailDomain")
    def reset_email_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailDomain", []))

    @jsii.member(jsii_name="resetEveryone")
    def reset_everyone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEveryone", []))

    @jsii.member(jsii_name="resetExternalEvaluation")
    def reset_external_evaluation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalEvaluation", []))

    @jsii.member(jsii_name="resetGeo")
    def reset_geo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeo", []))

    @jsii.member(jsii_name="resetGithub")
    def reset_github(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithub", []))

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetGsuite")
    def reset_gsuite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGsuite", []))

    @jsii.member(jsii_name="resetIp")
    def reset_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIp", []))

    @jsii.member(jsii_name="resetLoginMethod")
    def reset_login_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginMethod", []))

    @jsii.member(jsii_name="resetOkta")
    def reset_okta(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOkta", []))

    @jsii.member(jsii_name="resetSaml")
    def reset_saml(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml", []))

    @jsii.member(jsii_name="resetServiceToken")
    def reset_service_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceToken", []))

    @builtins.property
    @jsii.member(jsii_name="azure")
    def azure(self) -> AccessGroupExcludeAzureList:
        return typing.cast(AccessGroupExcludeAzureList, jsii.get(self, "azure"))

    @builtins.property
    @jsii.member(jsii_name="externalEvaluation")
    def external_evaluation(
        self,
    ) -> AccessGroupExcludeExternalEvaluationOutputReference:
        return typing.cast(AccessGroupExcludeExternalEvaluationOutputReference, jsii.get(self, "externalEvaluation"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> AccessGroupExcludeGithubList:
        return typing.cast(AccessGroupExcludeGithubList, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="gsuite")
    def gsuite(self) -> AccessGroupExcludeGsuiteList:
        return typing.cast(AccessGroupExcludeGsuiteList, jsii.get(self, "gsuite"))

    @builtins.property
    @jsii.member(jsii_name="okta")
    def okta(self) -> AccessGroupExcludeOktaList:
        return typing.cast(AccessGroupExcludeOktaList, jsii.get(self, "okta"))

    @builtins.property
    @jsii.member(jsii_name="saml")
    def saml(self) -> "AccessGroupExcludeSamlList":
        return typing.cast("AccessGroupExcludeSamlList", jsii.get(self, "saml"))

    @builtins.property
    @jsii.member(jsii_name="anyValidServiceTokenInput")
    def any_valid_service_token_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "anyValidServiceTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="authMethodInput")
    def auth_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="azureInput")
    def azure_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeAzure]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeAzure]]], jsii.get(self, "azureInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="commonNameInput")
    def common_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="devicePostureInput")
    def device_posture_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "devicePostureInput"))

    @builtins.property
    @jsii.member(jsii_name="emailDomainInput")
    def email_domain_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="everyoneInput")
    def everyone_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "everyoneInput"))

    @builtins.property
    @jsii.member(jsii_name="externalEvaluationInput")
    def external_evaluation_input(
        self,
    ) -> typing.Optional[AccessGroupExcludeExternalEvaluation]:
        return typing.cast(typing.Optional[AccessGroupExcludeExternalEvaluation], jsii.get(self, "externalEvaluationInput"))

    @builtins.property
    @jsii.member(jsii_name="geoInput")
    def geo_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "geoInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeGithub]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeGithub]]], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="gsuiteInput")
    def gsuite_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeGsuite]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeGsuite]]], jsii.get(self, "gsuiteInput"))

    @builtins.property
    @jsii.member(jsii_name="ipInput")
    def ip_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipInput"))

    @builtins.property
    @jsii.member(jsii_name="loginMethodInput")
    def login_method_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loginMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="oktaInput")
    def okta_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeOkta]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeOkta]]], jsii.get(self, "oktaInput"))

    @builtins.property
    @jsii.member(jsii_name="samlInput")
    def saml_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExcludeSaml"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupExcludeSaml"]]], jsii.get(self, "samlInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceTokenInput")
    def service_token_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serviceTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="anyValidServiceToken")
    def any_valid_service_token(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "anyValidServiceToken"))

    @any_valid_service_token.setter
    def any_valid_service_token(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOutputReference, "any_valid_service_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anyValidServiceToken", value)

    @builtins.property
    @jsii.member(jsii_name="authMethod")
    def auth_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authMethod"))

    @auth_method.setter
    def auth_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOutputReference, "auth_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMethod", value)

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @common_name.setter
    def common_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOutputReference, "common_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonName", value)

    @builtins.property
    @jsii.member(jsii_name="devicePosture")
    def device_posture(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "devicePosture"))

    @device_posture.setter
    def device_posture(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOutputReference, "device_posture").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "devicePosture", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="emailDomain")
    def email_domain(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emailDomain"))

    @email_domain.setter
    def email_domain(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOutputReference, "email_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailDomain", value)

    @builtins.property
    @jsii.member(jsii_name="everyone")
    def everyone(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "everyone"))

    @everyone.setter
    def everyone(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOutputReference, "everyone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "everyone", value)

    @builtins.property
    @jsii.member(jsii_name="geo")
    def geo(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "geo"))

    @geo.setter
    def geo(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOutputReference, "geo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geo", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "group"))

    @group.setter
    def group(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOutputReference, "group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ip"))

    @ip.setter
    def ip(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOutputReference, "ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ip", value)

    @builtins.property
    @jsii.member(jsii_name="loginMethod")
    def login_method(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loginMethod"))

    @login_method.setter
    def login_method(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOutputReference, "login_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginMethod", value)

    @builtins.property
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serviceToken"))

    @service_token.setter
    def service_token(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOutputReference, "service_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupExclude, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupExclude, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupExclude, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeSaml",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_name": "attributeName",
        "attribute_value": "attributeValue",
        "identity_provider_id": "identityProviderId",
    },
)
class AccessGroupExcludeSaml:
    def __init__(
        self,
        *,
        attribute_name: typing.Optional[builtins.str] = None,
        attribute_value: typing.Optional[builtins.str] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param attribute_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#attribute_name AccessGroup#attribute_name}.
        :param attribute_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#attribute_value AccessGroup#attribute_value}.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeSaml.__init__)
            check_type(argname="argument attribute_name", value=attribute_name, expected_type=type_hints["attribute_name"])
            check_type(argname="argument attribute_value", value=attribute_value, expected_type=type_hints["attribute_value"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if attribute_name is not None:
            self._values["attribute_name"] = attribute_name
        if attribute_value is not None:
            self._values["attribute_value"] = attribute_value
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def attribute_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#attribute_name AccessGroup#attribute_name}.'''
        result = self._values.get("attribute_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attribute_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#attribute_value AccessGroup#attribute_value}.'''
        result = self._values.get("attribute_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupExcludeSaml(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupExcludeSamlList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeSamlList",
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
            type_hints = typing.get_type_hints(AccessGroupExcludeSamlList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupExcludeSamlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupExcludeSamlList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupExcludeSamlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeSamlList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeSamlList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeSamlList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeSaml]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeSaml]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupExcludeSaml]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeSamlList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupExcludeSamlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupExcludeSamlOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupExcludeSamlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAttributeName")
    def reset_attribute_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeName", []))

    @jsii.member(jsii_name="resetAttributeValue")
    def reset_attribute_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeValue", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="attributeNameInput")
    def attribute_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeValueInput")
    def attribute_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeValueInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeName")
    def attribute_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeName"))

    @attribute_name.setter
    def attribute_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeSamlOutputReference, "attribute_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeName", value)

    @builtins.property
    @jsii.member(jsii_name="attributeValue")
    def attribute_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeValue"))

    @attribute_value.setter
    def attribute_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeSamlOutputReference, "attribute_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeValue", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeSamlOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupExcludeSaml, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupExcludeSaml, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupExcludeSaml, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupExcludeSamlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupInclude",
    jsii_struct_bases=[],
    name_mapping={
        "any_valid_service_token": "anyValidServiceToken",
        "auth_method": "authMethod",
        "azure": "azure",
        "certificate": "certificate",
        "common_name": "commonName",
        "device_posture": "devicePosture",
        "email": "email",
        "email_domain": "emailDomain",
        "everyone": "everyone",
        "external_evaluation": "externalEvaluation",
        "geo": "geo",
        "github": "github",
        "group": "group",
        "gsuite": "gsuite",
        "ip": "ip",
        "login_method": "loginMethod",
        "okta": "okta",
        "saml": "saml",
        "service_token": "serviceToken",
    },
)
class AccessGroupInclude:
    def __init__(
        self,
        *,
        any_valid_service_token: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auth_method: typing.Optional[builtins.str] = None,
        azure: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupIncludeAzure", typing.Dict[str, typing.Any]]]]] = None,
        certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        common_name: typing.Optional[builtins.str] = None,
        device_posture: typing.Optional[typing.Sequence[builtins.str]] = None,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_domain: typing.Optional[typing.Sequence[builtins.str]] = None,
        everyone: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        external_evaluation: typing.Optional[typing.Union["AccessGroupIncludeExternalEvaluation", typing.Dict[str, typing.Any]]] = None,
        geo: typing.Optional[typing.Sequence[builtins.str]] = None,
        github: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupIncludeGithub", typing.Dict[str, typing.Any]]]]] = None,
        group: typing.Optional[typing.Sequence[builtins.str]] = None,
        gsuite: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupIncludeGsuite", typing.Dict[str, typing.Any]]]]] = None,
        ip: typing.Optional[typing.Sequence[builtins.str]] = None,
        login_method: typing.Optional[typing.Sequence[builtins.str]] = None,
        okta: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupIncludeOkta", typing.Dict[str, typing.Any]]]]] = None,
        saml: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupIncludeSaml", typing.Dict[str, typing.Any]]]]] = None,
        service_token: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param any_valid_service_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#any_valid_service_token AccessGroup#any_valid_service_token}.
        :param auth_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#auth_method AccessGroup#auth_method}.
        :param azure: azure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#azure AccessGroup#azure}
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#certificate AccessGroup#certificate}.
        :param common_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#common_name AccessGroup#common_name}.
        :param device_posture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#device_posture AccessGroup#device_posture}.
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email AccessGroup#email}.
        :param email_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email_domain AccessGroup#email_domain}.
        :param everyone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#everyone AccessGroup#everyone}.
        :param external_evaluation: external_evaluation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#external_evaluation AccessGroup#external_evaluation}
        :param geo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#geo AccessGroup#geo}.
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#github AccessGroup#github}
        :param group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#group AccessGroup#group}.
        :param gsuite: gsuite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#gsuite AccessGroup#gsuite}
        :param ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#ip AccessGroup#ip}.
        :param login_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#login_method AccessGroup#login_method}.
        :param okta: okta block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#okta AccessGroup#okta}
        :param saml: saml block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#saml AccessGroup#saml}
        :param service_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#service_token AccessGroup#service_token}.
        '''
        if isinstance(external_evaluation, dict):
            external_evaluation = AccessGroupIncludeExternalEvaluation(**external_evaluation)
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupInclude.__init__)
            check_type(argname="argument any_valid_service_token", value=any_valid_service_token, expected_type=type_hints["any_valid_service_token"])
            check_type(argname="argument auth_method", value=auth_method, expected_type=type_hints["auth_method"])
            check_type(argname="argument azure", value=azure, expected_type=type_hints["azure"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
            check_type(argname="argument device_posture", value=device_posture, expected_type=type_hints["device_posture"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument email_domain", value=email_domain, expected_type=type_hints["email_domain"])
            check_type(argname="argument everyone", value=everyone, expected_type=type_hints["everyone"])
            check_type(argname="argument external_evaluation", value=external_evaluation, expected_type=type_hints["external_evaluation"])
            check_type(argname="argument geo", value=geo, expected_type=type_hints["geo"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument gsuite", value=gsuite, expected_type=type_hints["gsuite"])
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
            check_type(argname="argument login_method", value=login_method, expected_type=type_hints["login_method"])
            check_type(argname="argument okta", value=okta, expected_type=type_hints["okta"])
            check_type(argname="argument saml", value=saml, expected_type=type_hints["saml"])
            check_type(argname="argument service_token", value=service_token, expected_type=type_hints["service_token"])
        self._values: typing.Dict[str, typing.Any] = {}
        if any_valid_service_token is not None:
            self._values["any_valid_service_token"] = any_valid_service_token
        if auth_method is not None:
            self._values["auth_method"] = auth_method
        if azure is not None:
            self._values["azure"] = azure
        if certificate is not None:
            self._values["certificate"] = certificate
        if common_name is not None:
            self._values["common_name"] = common_name
        if device_posture is not None:
            self._values["device_posture"] = device_posture
        if email is not None:
            self._values["email"] = email
        if email_domain is not None:
            self._values["email_domain"] = email_domain
        if everyone is not None:
            self._values["everyone"] = everyone
        if external_evaluation is not None:
            self._values["external_evaluation"] = external_evaluation
        if geo is not None:
            self._values["geo"] = geo
        if github is not None:
            self._values["github"] = github
        if group is not None:
            self._values["group"] = group
        if gsuite is not None:
            self._values["gsuite"] = gsuite
        if ip is not None:
            self._values["ip"] = ip
        if login_method is not None:
            self._values["login_method"] = login_method
        if okta is not None:
            self._values["okta"] = okta
        if saml is not None:
            self._values["saml"] = saml
        if service_token is not None:
            self._values["service_token"] = service_token

    @builtins.property
    def any_valid_service_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#any_valid_service_token AccessGroup#any_valid_service_token}.'''
        result = self._values.get("any_valid_service_token")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auth_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#auth_method AccessGroup#auth_method}.'''
        result = self._values.get("auth_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupIncludeAzure"]]]:
        '''azure block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#azure AccessGroup#azure}
        '''
        result = self._values.get("azure")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupIncludeAzure"]]], result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#certificate AccessGroup#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def common_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#common_name AccessGroup#common_name}.'''
        result = self._values.get("common_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_posture(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#device_posture AccessGroup#device_posture}.'''
        result = self._values.get("device_posture")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email AccessGroup#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email_domain(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email_domain AccessGroup#email_domain}.'''
        result = self._values.get("email_domain")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def everyone(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#everyone AccessGroup#everyone}.'''
        result = self._values.get("everyone")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def external_evaluation(
        self,
    ) -> typing.Optional["AccessGroupIncludeExternalEvaluation"]:
        '''external_evaluation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#external_evaluation AccessGroup#external_evaluation}
        '''
        result = self._values.get("external_evaluation")
        return typing.cast(typing.Optional["AccessGroupIncludeExternalEvaluation"], result)

    @builtins.property
    def geo(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#geo AccessGroup#geo}.'''
        result = self._values.get("geo")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def github(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupIncludeGithub"]]]:
        '''github block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#github AccessGroup#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupIncludeGithub"]]], result)

    @builtins.property
    def group(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#group AccessGroup#group}.'''
        result = self._values.get("group")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def gsuite(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupIncludeGsuite"]]]:
        '''gsuite block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#gsuite AccessGroup#gsuite}
        '''
        result = self._values.get("gsuite")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupIncludeGsuite"]]], result)

    @builtins.property
    def ip(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#ip AccessGroup#ip}.'''
        result = self._values.get("ip")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def login_method(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#login_method AccessGroup#login_method}.'''
        result = self._values.get("login_method")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def okta(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupIncludeOkta"]]]:
        '''okta block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#okta AccessGroup#okta}
        '''
        result = self._values.get("okta")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupIncludeOkta"]]], result)

    @builtins.property
    def saml(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupIncludeSaml"]]]:
        '''saml block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#saml AccessGroup#saml}
        '''
        result = self._values.get("saml")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupIncludeSaml"]]], result)

    @builtins.property
    def service_token(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#service_token AccessGroup#service_token}.'''
        result = self._values.get("service_token")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupInclude(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeAzure",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "identity_provider_id": "identityProviderId"},
)
class AccessGroupIncludeAzure:
    def __init__(
        self,
        *,
        id: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#id AccessGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeAzure.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def id(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#id AccessGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupIncludeAzure(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupIncludeAzureList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeAzureList",
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
            type_hints = typing.get_type_hints(AccessGroupIncludeAzureList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupIncludeAzureOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeAzureList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupIncludeAzureOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeAzureList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeAzureList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeAzureList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeAzure]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeAzure]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeAzure]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeAzureList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupIncludeAzureOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeAzureOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupIncludeAzureOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "id"))

    @id.setter
    def id(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeAzureOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeAzureOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupIncludeAzure, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupIncludeAzure, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupIncludeAzure, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeAzureOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeExternalEvaluation",
    jsii_struct_bases=[],
    name_mapping={"evaluate_url": "evaluateUrl", "keys_url": "keysUrl"},
)
class AccessGroupIncludeExternalEvaluation:
    def __init__(
        self,
        *,
        evaluate_url: typing.Optional[builtins.str] = None,
        keys_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param evaluate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#evaluate_url AccessGroup#evaluate_url}.
        :param keys_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#keys_url AccessGroup#keys_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeExternalEvaluation.__init__)
            check_type(argname="argument evaluate_url", value=evaluate_url, expected_type=type_hints["evaluate_url"])
            check_type(argname="argument keys_url", value=keys_url, expected_type=type_hints["keys_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if evaluate_url is not None:
            self._values["evaluate_url"] = evaluate_url
        if keys_url is not None:
            self._values["keys_url"] = keys_url

    @builtins.property
    def evaluate_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#evaluate_url AccessGroup#evaluate_url}.'''
        result = self._values.get("evaluate_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keys_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#keys_url AccessGroup#keys_url}.'''
        result = self._values.get("keys_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupIncludeExternalEvaluation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupIncludeExternalEvaluationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeExternalEvaluationOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupIncludeExternalEvaluationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEvaluateUrl")
    def reset_evaluate_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateUrl", []))

    @jsii.member(jsii_name="resetKeysUrl")
    def reset_keys_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeysUrl", []))

    @builtins.property
    @jsii.member(jsii_name="evaluateUrlInput")
    def evaluate_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluateUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="keysUrlInput")
    def keys_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keysUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateUrl")
    def evaluate_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evaluateUrl"))

    @evaluate_url.setter
    def evaluate_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeExternalEvaluationOutputReference, "evaluate_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateUrl", value)

    @builtins.property
    @jsii.member(jsii_name="keysUrl")
    def keys_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keysUrl"))

    @keys_url.setter
    def keys_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeExternalEvaluationOutputReference, "keys_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keysUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AccessGroupIncludeExternalEvaluation]:
        return typing.cast(typing.Optional[AccessGroupIncludeExternalEvaluation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AccessGroupIncludeExternalEvaluation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeExternalEvaluationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeGithub",
    jsii_struct_bases=[],
    name_mapping={
        "identity_provider_id": "identityProviderId",
        "name": "name",
        "teams": "teams",
    },
)
class AccessGroupIncludeGithub:
    def __init__(
        self,
        *,
        identity_provider_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        teams: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#name AccessGroup#name}.
        :param teams: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#teams AccessGroup#teams}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeGithub.__init__)
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument teams", value=teams, expected_type=type_hints["teams"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id
        if name is not None:
            self._values["name"] = name
        if teams is not None:
            self._values["teams"] = teams

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#name AccessGroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def teams(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#teams AccessGroup#teams}.'''
        result = self._values.get("teams")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupIncludeGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupIncludeGithubList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeGithubList",
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
            type_hints = typing.get_type_hints(AccessGroupIncludeGithubList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupIncludeGithubOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeGithubList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupIncludeGithubOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeGithubList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeGithubList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeGithubList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeGithub]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeGithub]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeGithub]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeGithubList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupIncludeGithubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeGithubOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupIncludeGithubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTeams")
    def reset_teams(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeams", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="teamsInput")
    def teams_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "teamsInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeGithubOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeGithubOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="teams")
    def teams(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "teams"))

    @teams.setter
    def teams(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeGithubOutputReference, "teams").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teams", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupIncludeGithub, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupIncludeGithub, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupIncludeGithub, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeGithubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeGsuite",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "identity_provider_id": "identityProviderId"},
)
class AccessGroupIncludeGsuite:
    def __init__(
        self,
        *,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email AccessGroup#email}.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeGsuite.__init__)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def email(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email AccessGroup#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupIncludeGsuite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupIncludeGsuiteList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeGsuiteList",
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
            type_hints = typing.get_type_hints(AccessGroupIncludeGsuiteList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupIncludeGsuiteOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeGsuiteList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupIncludeGsuiteOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeGsuiteList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeGsuiteList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeGsuiteList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeGsuite]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeGsuite]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeGsuite]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeGsuiteList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupIncludeGsuiteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeGsuiteOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupIncludeGsuiteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeGsuiteOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeGsuiteOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupIncludeGsuite, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupIncludeGsuite, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupIncludeGsuite, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeGsuiteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupIncludeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeList",
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
            type_hints = typing.get_type_hints(AccessGroupIncludeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupIncludeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupIncludeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupInclude]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupInclude]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupInclude]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeOkta",
    jsii_struct_bases=[],
    name_mapping={"identity_provider_id": "identityProviderId", "name": "name"},
)
class AccessGroupIncludeOkta:
    def __init__(
        self,
        *,
        identity_provider_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#name AccessGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeOkta.__init__)
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#name AccessGroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupIncludeOkta(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupIncludeOktaList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeOktaList",
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
            type_hints = typing.get_type_hints(AccessGroupIncludeOktaList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupIncludeOktaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeOktaList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupIncludeOktaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOktaList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOktaList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOktaList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeOkta]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeOkta]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeOkta]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOktaList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupIncludeOktaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeOktaOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupIncludeOktaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOktaOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOktaOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupIncludeOkta, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupIncludeOkta, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupIncludeOkta, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOktaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupIncludeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupIncludeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAzure")
    def put_azure(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessGroupIncludeAzure, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeOutputReference.put_azure)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAzure", [value]))

    @jsii.member(jsii_name="putExternalEvaluation")
    def put_external_evaluation(
        self,
        *,
        evaluate_url: typing.Optional[builtins.str] = None,
        keys_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param evaluate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#evaluate_url AccessGroup#evaluate_url}.
        :param keys_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#keys_url AccessGroup#keys_url}.
        '''
        value = AccessGroupIncludeExternalEvaluation(
            evaluate_url=evaluate_url, keys_url=keys_url
        )

        return typing.cast(None, jsii.invoke(self, "putExternalEvaluation", [value]))

    @jsii.member(jsii_name="putGithub")
    def put_github(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessGroupIncludeGithub, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeOutputReference.put_github)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGithub", [value]))

    @jsii.member(jsii_name="putGsuite")
    def put_gsuite(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessGroupIncludeGsuite, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeOutputReference.put_gsuite)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGsuite", [value]))

    @jsii.member(jsii_name="putOkta")
    def put_okta(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessGroupIncludeOkta, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeOutputReference.put_okta)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOkta", [value]))

    @jsii.member(jsii_name="putSaml")
    def put_saml(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupIncludeSaml", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeOutputReference.put_saml)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSaml", [value]))

    @jsii.member(jsii_name="resetAnyValidServiceToken")
    def reset_any_valid_service_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnyValidServiceToken", []))

    @jsii.member(jsii_name="resetAuthMethod")
    def reset_auth_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthMethod", []))

    @jsii.member(jsii_name="resetAzure")
    def reset_azure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzure", []))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCommonName")
    def reset_common_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonName", []))

    @jsii.member(jsii_name="resetDevicePosture")
    def reset_device_posture(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevicePosture", []))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetEmailDomain")
    def reset_email_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailDomain", []))

    @jsii.member(jsii_name="resetEveryone")
    def reset_everyone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEveryone", []))

    @jsii.member(jsii_name="resetExternalEvaluation")
    def reset_external_evaluation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalEvaluation", []))

    @jsii.member(jsii_name="resetGeo")
    def reset_geo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeo", []))

    @jsii.member(jsii_name="resetGithub")
    def reset_github(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithub", []))

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetGsuite")
    def reset_gsuite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGsuite", []))

    @jsii.member(jsii_name="resetIp")
    def reset_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIp", []))

    @jsii.member(jsii_name="resetLoginMethod")
    def reset_login_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginMethod", []))

    @jsii.member(jsii_name="resetOkta")
    def reset_okta(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOkta", []))

    @jsii.member(jsii_name="resetSaml")
    def reset_saml(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml", []))

    @jsii.member(jsii_name="resetServiceToken")
    def reset_service_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceToken", []))

    @builtins.property
    @jsii.member(jsii_name="azure")
    def azure(self) -> AccessGroupIncludeAzureList:
        return typing.cast(AccessGroupIncludeAzureList, jsii.get(self, "azure"))

    @builtins.property
    @jsii.member(jsii_name="externalEvaluation")
    def external_evaluation(
        self,
    ) -> AccessGroupIncludeExternalEvaluationOutputReference:
        return typing.cast(AccessGroupIncludeExternalEvaluationOutputReference, jsii.get(self, "externalEvaluation"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> AccessGroupIncludeGithubList:
        return typing.cast(AccessGroupIncludeGithubList, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="gsuite")
    def gsuite(self) -> AccessGroupIncludeGsuiteList:
        return typing.cast(AccessGroupIncludeGsuiteList, jsii.get(self, "gsuite"))

    @builtins.property
    @jsii.member(jsii_name="okta")
    def okta(self) -> AccessGroupIncludeOktaList:
        return typing.cast(AccessGroupIncludeOktaList, jsii.get(self, "okta"))

    @builtins.property
    @jsii.member(jsii_name="saml")
    def saml(self) -> "AccessGroupIncludeSamlList":
        return typing.cast("AccessGroupIncludeSamlList", jsii.get(self, "saml"))

    @builtins.property
    @jsii.member(jsii_name="anyValidServiceTokenInput")
    def any_valid_service_token_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "anyValidServiceTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="authMethodInput")
    def auth_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="azureInput")
    def azure_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeAzure]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeAzure]]], jsii.get(self, "azureInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="commonNameInput")
    def common_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="devicePostureInput")
    def device_posture_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "devicePostureInput"))

    @builtins.property
    @jsii.member(jsii_name="emailDomainInput")
    def email_domain_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="everyoneInput")
    def everyone_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "everyoneInput"))

    @builtins.property
    @jsii.member(jsii_name="externalEvaluationInput")
    def external_evaluation_input(
        self,
    ) -> typing.Optional[AccessGroupIncludeExternalEvaluation]:
        return typing.cast(typing.Optional[AccessGroupIncludeExternalEvaluation], jsii.get(self, "externalEvaluationInput"))

    @builtins.property
    @jsii.member(jsii_name="geoInput")
    def geo_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "geoInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeGithub]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeGithub]]], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="gsuiteInput")
    def gsuite_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeGsuite]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeGsuite]]], jsii.get(self, "gsuiteInput"))

    @builtins.property
    @jsii.member(jsii_name="ipInput")
    def ip_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipInput"))

    @builtins.property
    @jsii.member(jsii_name="loginMethodInput")
    def login_method_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loginMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="oktaInput")
    def okta_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeOkta]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeOkta]]], jsii.get(self, "oktaInput"))

    @builtins.property
    @jsii.member(jsii_name="samlInput")
    def saml_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupIncludeSaml"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupIncludeSaml"]]], jsii.get(self, "samlInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceTokenInput")
    def service_token_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serviceTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="anyValidServiceToken")
    def any_valid_service_token(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "anyValidServiceToken"))

    @any_valid_service_token.setter
    def any_valid_service_token(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOutputReference, "any_valid_service_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anyValidServiceToken", value)

    @builtins.property
    @jsii.member(jsii_name="authMethod")
    def auth_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authMethod"))

    @auth_method.setter
    def auth_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOutputReference, "auth_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMethod", value)

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @common_name.setter
    def common_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOutputReference, "common_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonName", value)

    @builtins.property
    @jsii.member(jsii_name="devicePosture")
    def device_posture(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "devicePosture"))

    @device_posture.setter
    def device_posture(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOutputReference, "device_posture").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "devicePosture", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="emailDomain")
    def email_domain(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emailDomain"))

    @email_domain.setter
    def email_domain(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOutputReference, "email_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailDomain", value)

    @builtins.property
    @jsii.member(jsii_name="everyone")
    def everyone(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "everyone"))

    @everyone.setter
    def everyone(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOutputReference, "everyone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "everyone", value)

    @builtins.property
    @jsii.member(jsii_name="geo")
    def geo(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "geo"))

    @geo.setter
    def geo(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOutputReference, "geo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geo", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "group"))

    @group.setter
    def group(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOutputReference, "group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ip"))

    @ip.setter
    def ip(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOutputReference, "ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ip", value)

    @builtins.property
    @jsii.member(jsii_name="loginMethod")
    def login_method(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loginMethod"))

    @login_method.setter
    def login_method(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOutputReference, "login_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginMethod", value)

    @builtins.property
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serviceToken"))

    @service_token.setter
    def service_token(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOutputReference, "service_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupInclude, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupInclude, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupInclude, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeSaml",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_name": "attributeName",
        "attribute_value": "attributeValue",
        "identity_provider_id": "identityProviderId",
    },
)
class AccessGroupIncludeSaml:
    def __init__(
        self,
        *,
        attribute_name: typing.Optional[builtins.str] = None,
        attribute_value: typing.Optional[builtins.str] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param attribute_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#attribute_name AccessGroup#attribute_name}.
        :param attribute_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#attribute_value AccessGroup#attribute_value}.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeSaml.__init__)
            check_type(argname="argument attribute_name", value=attribute_name, expected_type=type_hints["attribute_name"])
            check_type(argname="argument attribute_value", value=attribute_value, expected_type=type_hints["attribute_value"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if attribute_name is not None:
            self._values["attribute_name"] = attribute_name
        if attribute_value is not None:
            self._values["attribute_value"] = attribute_value
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def attribute_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#attribute_name AccessGroup#attribute_name}.'''
        result = self._values.get("attribute_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attribute_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#attribute_value AccessGroup#attribute_value}.'''
        result = self._values.get("attribute_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupIncludeSaml(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupIncludeSamlList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeSamlList",
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
            type_hints = typing.get_type_hints(AccessGroupIncludeSamlList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupIncludeSamlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupIncludeSamlList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupIncludeSamlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeSamlList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeSamlList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeSamlList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeSaml]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeSaml]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupIncludeSaml]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeSamlList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupIncludeSamlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupIncludeSamlOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupIncludeSamlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAttributeName")
    def reset_attribute_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeName", []))

    @jsii.member(jsii_name="resetAttributeValue")
    def reset_attribute_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeValue", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="attributeNameInput")
    def attribute_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeValueInput")
    def attribute_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeValueInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeName")
    def attribute_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeName"))

    @attribute_name.setter
    def attribute_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeSamlOutputReference, "attribute_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeName", value)

    @builtins.property
    @jsii.member(jsii_name="attributeValue")
    def attribute_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeValue"))

    @attribute_value.setter
    def attribute_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeSamlOutputReference, "attribute_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeValue", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeSamlOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupIncludeSaml, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupIncludeSaml, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupIncludeSaml, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupIncludeSamlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequire",
    jsii_struct_bases=[],
    name_mapping={
        "any_valid_service_token": "anyValidServiceToken",
        "auth_method": "authMethod",
        "azure": "azure",
        "certificate": "certificate",
        "common_name": "commonName",
        "device_posture": "devicePosture",
        "email": "email",
        "email_domain": "emailDomain",
        "everyone": "everyone",
        "external_evaluation": "externalEvaluation",
        "geo": "geo",
        "github": "github",
        "group": "group",
        "gsuite": "gsuite",
        "ip": "ip",
        "login_method": "loginMethod",
        "okta": "okta",
        "saml": "saml",
        "service_token": "serviceToken",
    },
)
class AccessGroupRequire:
    def __init__(
        self,
        *,
        any_valid_service_token: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auth_method: typing.Optional[builtins.str] = None,
        azure: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupRequireAzure", typing.Dict[str, typing.Any]]]]] = None,
        certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        common_name: typing.Optional[builtins.str] = None,
        device_posture: typing.Optional[typing.Sequence[builtins.str]] = None,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_domain: typing.Optional[typing.Sequence[builtins.str]] = None,
        everyone: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        external_evaluation: typing.Optional[typing.Union["AccessGroupRequireExternalEvaluation", typing.Dict[str, typing.Any]]] = None,
        geo: typing.Optional[typing.Sequence[builtins.str]] = None,
        github: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupRequireGithub", typing.Dict[str, typing.Any]]]]] = None,
        group: typing.Optional[typing.Sequence[builtins.str]] = None,
        gsuite: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupRequireGsuite", typing.Dict[str, typing.Any]]]]] = None,
        ip: typing.Optional[typing.Sequence[builtins.str]] = None,
        login_method: typing.Optional[typing.Sequence[builtins.str]] = None,
        okta: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupRequireOkta", typing.Dict[str, typing.Any]]]]] = None,
        saml: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupRequireSaml", typing.Dict[str, typing.Any]]]]] = None,
        service_token: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param any_valid_service_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#any_valid_service_token AccessGroup#any_valid_service_token}.
        :param auth_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#auth_method AccessGroup#auth_method}.
        :param azure: azure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#azure AccessGroup#azure}
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#certificate AccessGroup#certificate}.
        :param common_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#common_name AccessGroup#common_name}.
        :param device_posture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#device_posture AccessGroup#device_posture}.
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email AccessGroup#email}.
        :param email_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email_domain AccessGroup#email_domain}.
        :param everyone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#everyone AccessGroup#everyone}.
        :param external_evaluation: external_evaluation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#external_evaluation AccessGroup#external_evaluation}
        :param geo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#geo AccessGroup#geo}.
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#github AccessGroup#github}
        :param group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#group AccessGroup#group}.
        :param gsuite: gsuite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#gsuite AccessGroup#gsuite}
        :param ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#ip AccessGroup#ip}.
        :param login_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#login_method AccessGroup#login_method}.
        :param okta: okta block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#okta AccessGroup#okta}
        :param saml: saml block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#saml AccessGroup#saml}
        :param service_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#service_token AccessGroup#service_token}.
        '''
        if isinstance(external_evaluation, dict):
            external_evaluation = AccessGroupRequireExternalEvaluation(**external_evaluation)
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequire.__init__)
            check_type(argname="argument any_valid_service_token", value=any_valid_service_token, expected_type=type_hints["any_valid_service_token"])
            check_type(argname="argument auth_method", value=auth_method, expected_type=type_hints["auth_method"])
            check_type(argname="argument azure", value=azure, expected_type=type_hints["azure"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
            check_type(argname="argument device_posture", value=device_posture, expected_type=type_hints["device_posture"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument email_domain", value=email_domain, expected_type=type_hints["email_domain"])
            check_type(argname="argument everyone", value=everyone, expected_type=type_hints["everyone"])
            check_type(argname="argument external_evaluation", value=external_evaluation, expected_type=type_hints["external_evaluation"])
            check_type(argname="argument geo", value=geo, expected_type=type_hints["geo"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument gsuite", value=gsuite, expected_type=type_hints["gsuite"])
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
            check_type(argname="argument login_method", value=login_method, expected_type=type_hints["login_method"])
            check_type(argname="argument okta", value=okta, expected_type=type_hints["okta"])
            check_type(argname="argument saml", value=saml, expected_type=type_hints["saml"])
            check_type(argname="argument service_token", value=service_token, expected_type=type_hints["service_token"])
        self._values: typing.Dict[str, typing.Any] = {}
        if any_valid_service_token is not None:
            self._values["any_valid_service_token"] = any_valid_service_token
        if auth_method is not None:
            self._values["auth_method"] = auth_method
        if azure is not None:
            self._values["azure"] = azure
        if certificate is not None:
            self._values["certificate"] = certificate
        if common_name is not None:
            self._values["common_name"] = common_name
        if device_posture is not None:
            self._values["device_posture"] = device_posture
        if email is not None:
            self._values["email"] = email
        if email_domain is not None:
            self._values["email_domain"] = email_domain
        if everyone is not None:
            self._values["everyone"] = everyone
        if external_evaluation is not None:
            self._values["external_evaluation"] = external_evaluation
        if geo is not None:
            self._values["geo"] = geo
        if github is not None:
            self._values["github"] = github
        if group is not None:
            self._values["group"] = group
        if gsuite is not None:
            self._values["gsuite"] = gsuite
        if ip is not None:
            self._values["ip"] = ip
        if login_method is not None:
            self._values["login_method"] = login_method
        if okta is not None:
            self._values["okta"] = okta
        if saml is not None:
            self._values["saml"] = saml
        if service_token is not None:
            self._values["service_token"] = service_token

    @builtins.property
    def any_valid_service_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#any_valid_service_token AccessGroup#any_valid_service_token}.'''
        result = self._values.get("any_valid_service_token")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auth_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#auth_method AccessGroup#auth_method}.'''
        result = self._values.get("auth_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequireAzure"]]]:
        '''azure block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#azure AccessGroup#azure}
        '''
        result = self._values.get("azure")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequireAzure"]]], result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#certificate AccessGroup#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def common_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#common_name AccessGroup#common_name}.'''
        result = self._values.get("common_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_posture(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#device_posture AccessGroup#device_posture}.'''
        result = self._values.get("device_posture")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email AccessGroup#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email_domain(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email_domain AccessGroup#email_domain}.'''
        result = self._values.get("email_domain")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def everyone(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#everyone AccessGroup#everyone}.'''
        result = self._values.get("everyone")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def external_evaluation(
        self,
    ) -> typing.Optional["AccessGroupRequireExternalEvaluation"]:
        '''external_evaluation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#external_evaluation AccessGroup#external_evaluation}
        '''
        result = self._values.get("external_evaluation")
        return typing.cast(typing.Optional["AccessGroupRequireExternalEvaluation"], result)

    @builtins.property
    def geo(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#geo AccessGroup#geo}.'''
        result = self._values.get("geo")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def github(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequireGithub"]]]:
        '''github block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#github AccessGroup#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequireGithub"]]], result)

    @builtins.property
    def group(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#group AccessGroup#group}.'''
        result = self._values.get("group")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def gsuite(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequireGsuite"]]]:
        '''gsuite block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#gsuite AccessGroup#gsuite}
        '''
        result = self._values.get("gsuite")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequireGsuite"]]], result)

    @builtins.property
    def ip(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#ip AccessGroup#ip}.'''
        result = self._values.get("ip")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def login_method(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#login_method AccessGroup#login_method}.'''
        result = self._values.get("login_method")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def okta(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequireOkta"]]]:
        '''okta block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#okta AccessGroup#okta}
        '''
        result = self._values.get("okta")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequireOkta"]]], result)

    @builtins.property
    def saml(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequireSaml"]]]:
        '''saml block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#saml AccessGroup#saml}
        '''
        result = self._values.get("saml")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequireSaml"]]], result)

    @builtins.property
    def service_token(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#service_token AccessGroup#service_token}.'''
        result = self._values.get("service_token")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupRequire(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireAzure",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "identity_provider_id": "identityProviderId"},
)
class AccessGroupRequireAzure:
    def __init__(
        self,
        *,
        id: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#id AccessGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireAzure.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def id(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#id AccessGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupRequireAzure(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupRequireAzureList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireAzureList",
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
            type_hints = typing.get_type_hints(AccessGroupRequireAzureList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupRequireAzureOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireAzureList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupRequireAzureOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireAzureList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireAzureList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireAzureList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireAzure]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireAzure]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireAzure]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireAzureList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupRequireAzureOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireAzureOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupRequireAzureOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "id"))

    @id.setter
    def id(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireAzureOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireAzureOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupRequireAzure, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupRequireAzure, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupRequireAzure, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireAzureOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireExternalEvaluation",
    jsii_struct_bases=[],
    name_mapping={"evaluate_url": "evaluateUrl", "keys_url": "keysUrl"},
)
class AccessGroupRequireExternalEvaluation:
    def __init__(
        self,
        *,
        evaluate_url: typing.Optional[builtins.str] = None,
        keys_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param evaluate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#evaluate_url AccessGroup#evaluate_url}.
        :param keys_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#keys_url AccessGroup#keys_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireExternalEvaluation.__init__)
            check_type(argname="argument evaluate_url", value=evaluate_url, expected_type=type_hints["evaluate_url"])
            check_type(argname="argument keys_url", value=keys_url, expected_type=type_hints["keys_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if evaluate_url is not None:
            self._values["evaluate_url"] = evaluate_url
        if keys_url is not None:
            self._values["keys_url"] = keys_url

    @builtins.property
    def evaluate_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#evaluate_url AccessGroup#evaluate_url}.'''
        result = self._values.get("evaluate_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keys_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#keys_url AccessGroup#keys_url}.'''
        result = self._values.get("keys_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupRequireExternalEvaluation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupRequireExternalEvaluationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireExternalEvaluationOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupRequireExternalEvaluationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEvaluateUrl")
    def reset_evaluate_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateUrl", []))

    @jsii.member(jsii_name="resetKeysUrl")
    def reset_keys_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeysUrl", []))

    @builtins.property
    @jsii.member(jsii_name="evaluateUrlInput")
    def evaluate_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluateUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="keysUrlInput")
    def keys_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keysUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateUrl")
    def evaluate_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evaluateUrl"))

    @evaluate_url.setter
    def evaluate_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireExternalEvaluationOutputReference, "evaluate_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateUrl", value)

    @builtins.property
    @jsii.member(jsii_name="keysUrl")
    def keys_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keysUrl"))

    @keys_url.setter
    def keys_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireExternalEvaluationOutputReference, "keys_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keysUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AccessGroupRequireExternalEvaluation]:
        return typing.cast(typing.Optional[AccessGroupRequireExternalEvaluation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AccessGroupRequireExternalEvaluation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireExternalEvaluationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireGithub",
    jsii_struct_bases=[],
    name_mapping={
        "identity_provider_id": "identityProviderId",
        "name": "name",
        "teams": "teams",
    },
)
class AccessGroupRequireGithub:
    def __init__(
        self,
        *,
        identity_provider_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        teams: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#name AccessGroup#name}.
        :param teams: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#teams AccessGroup#teams}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireGithub.__init__)
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument teams", value=teams, expected_type=type_hints["teams"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id
        if name is not None:
            self._values["name"] = name
        if teams is not None:
            self._values["teams"] = teams

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#name AccessGroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def teams(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#teams AccessGroup#teams}.'''
        result = self._values.get("teams")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupRequireGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupRequireGithubList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireGithubList",
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
            type_hints = typing.get_type_hints(AccessGroupRequireGithubList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupRequireGithubOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireGithubList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupRequireGithubOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireGithubList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireGithubList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireGithubList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireGithub]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireGithub]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireGithub]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireGithubList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupRequireGithubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireGithubOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupRequireGithubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTeams")
    def reset_teams(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeams", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="teamsInput")
    def teams_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "teamsInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireGithubOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireGithubOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="teams")
    def teams(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "teams"))

    @teams.setter
    def teams(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireGithubOutputReference, "teams").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teams", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupRequireGithub, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupRequireGithub, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupRequireGithub, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireGithubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireGsuite",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "identity_provider_id": "identityProviderId"},
)
class AccessGroupRequireGsuite:
    def __init__(
        self,
        *,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email AccessGroup#email}.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireGsuite.__init__)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def email(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#email AccessGroup#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupRequireGsuite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupRequireGsuiteList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireGsuiteList",
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
            type_hints = typing.get_type_hints(AccessGroupRequireGsuiteList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupRequireGsuiteOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireGsuiteList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupRequireGsuiteOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireGsuiteList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireGsuiteList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireGsuiteList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireGsuite]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireGsuite]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireGsuite]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireGsuiteList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupRequireGsuiteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireGsuiteOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupRequireGsuiteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireGsuiteOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireGsuiteOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupRequireGsuite, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupRequireGsuite, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupRequireGsuite, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireGsuiteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupRequireList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireList",
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
            type_hints = typing.get_type_hints(AccessGroupRequireList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupRequireOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupRequireOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequire]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequire]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequire]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireOkta",
    jsii_struct_bases=[],
    name_mapping={"identity_provider_id": "identityProviderId", "name": "name"},
)
class AccessGroupRequireOkta:
    def __init__(
        self,
        *,
        identity_provider_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#name AccessGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireOkta.__init__)
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#name AccessGroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupRequireOkta(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupRequireOktaList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireOktaList",
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
            type_hints = typing.get_type_hints(AccessGroupRequireOktaList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupRequireOktaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireOktaList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupRequireOktaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOktaList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOktaList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOktaList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireOkta]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireOkta]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireOkta]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOktaList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupRequireOktaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireOktaOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupRequireOktaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOktaOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOktaOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupRequireOkta, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupRequireOkta, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupRequireOkta, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOktaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupRequireOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupRequireOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAzure")
    def put_azure(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessGroupRequireAzure, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireOutputReference.put_azure)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAzure", [value]))

    @jsii.member(jsii_name="putExternalEvaluation")
    def put_external_evaluation(
        self,
        *,
        evaluate_url: typing.Optional[builtins.str] = None,
        keys_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param evaluate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#evaluate_url AccessGroup#evaluate_url}.
        :param keys_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#keys_url AccessGroup#keys_url}.
        '''
        value = AccessGroupRequireExternalEvaluation(
            evaluate_url=evaluate_url, keys_url=keys_url
        )

        return typing.cast(None, jsii.invoke(self, "putExternalEvaluation", [value]))

    @jsii.member(jsii_name="putGithub")
    def put_github(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessGroupRequireGithub, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireOutputReference.put_github)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGithub", [value]))

    @jsii.member(jsii_name="putGsuite")
    def put_gsuite(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessGroupRequireGsuite, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireOutputReference.put_gsuite)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGsuite", [value]))

    @jsii.member(jsii_name="putOkta")
    def put_okta(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AccessGroupRequireOkta, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireOutputReference.put_okta)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOkta", [value]))

    @jsii.member(jsii_name="putSaml")
    def put_saml(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AccessGroupRequireSaml", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireOutputReference.put_saml)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSaml", [value]))

    @jsii.member(jsii_name="resetAnyValidServiceToken")
    def reset_any_valid_service_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnyValidServiceToken", []))

    @jsii.member(jsii_name="resetAuthMethod")
    def reset_auth_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthMethod", []))

    @jsii.member(jsii_name="resetAzure")
    def reset_azure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzure", []))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCommonName")
    def reset_common_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonName", []))

    @jsii.member(jsii_name="resetDevicePosture")
    def reset_device_posture(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevicePosture", []))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetEmailDomain")
    def reset_email_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailDomain", []))

    @jsii.member(jsii_name="resetEveryone")
    def reset_everyone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEveryone", []))

    @jsii.member(jsii_name="resetExternalEvaluation")
    def reset_external_evaluation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalEvaluation", []))

    @jsii.member(jsii_name="resetGeo")
    def reset_geo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeo", []))

    @jsii.member(jsii_name="resetGithub")
    def reset_github(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithub", []))

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetGsuite")
    def reset_gsuite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGsuite", []))

    @jsii.member(jsii_name="resetIp")
    def reset_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIp", []))

    @jsii.member(jsii_name="resetLoginMethod")
    def reset_login_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginMethod", []))

    @jsii.member(jsii_name="resetOkta")
    def reset_okta(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOkta", []))

    @jsii.member(jsii_name="resetSaml")
    def reset_saml(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml", []))

    @jsii.member(jsii_name="resetServiceToken")
    def reset_service_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceToken", []))

    @builtins.property
    @jsii.member(jsii_name="azure")
    def azure(self) -> AccessGroupRequireAzureList:
        return typing.cast(AccessGroupRequireAzureList, jsii.get(self, "azure"))

    @builtins.property
    @jsii.member(jsii_name="externalEvaluation")
    def external_evaluation(
        self,
    ) -> AccessGroupRequireExternalEvaluationOutputReference:
        return typing.cast(AccessGroupRequireExternalEvaluationOutputReference, jsii.get(self, "externalEvaluation"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> AccessGroupRequireGithubList:
        return typing.cast(AccessGroupRequireGithubList, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="gsuite")
    def gsuite(self) -> AccessGroupRequireGsuiteList:
        return typing.cast(AccessGroupRequireGsuiteList, jsii.get(self, "gsuite"))

    @builtins.property
    @jsii.member(jsii_name="okta")
    def okta(self) -> AccessGroupRequireOktaList:
        return typing.cast(AccessGroupRequireOktaList, jsii.get(self, "okta"))

    @builtins.property
    @jsii.member(jsii_name="saml")
    def saml(self) -> "AccessGroupRequireSamlList":
        return typing.cast("AccessGroupRequireSamlList", jsii.get(self, "saml"))

    @builtins.property
    @jsii.member(jsii_name="anyValidServiceTokenInput")
    def any_valid_service_token_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "anyValidServiceTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="authMethodInput")
    def auth_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="azureInput")
    def azure_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireAzure]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireAzure]]], jsii.get(self, "azureInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="commonNameInput")
    def common_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="devicePostureInput")
    def device_posture_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "devicePostureInput"))

    @builtins.property
    @jsii.member(jsii_name="emailDomainInput")
    def email_domain_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="everyoneInput")
    def everyone_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "everyoneInput"))

    @builtins.property
    @jsii.member(jsii_name="externalEvaluationInput")
    def external_evaluation_input(
        self,
    ) -> typing.Optional[AccessGroupRequireExternalEvaluation]:
        return typing.cast(typing.Optional[AccessGroupRequireExternalEvaluation], jsii.get(self, "externalEvaluationInput"))

    @builtins.property
    @jsii.member(jsii_name="geoInput")
    def geo_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "geoInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireGithub]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireGithub]]], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="gsuiteInput")
    def gsuite_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireGsuite]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireGsuite]]], jsii.get(self, "gsuiteInput"))

    @builtins.property
    @jsii.member(jsii_name="ipInput")
    def ip_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipInput"))

    @builtins.property
    @jsii.member(jsii_name="loginMethodInput")
    def login_method_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loginMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="oktaInput")
    def okta_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireOkta]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireOkta]]], jsii.get(self, "oktaInput"))

    @builtins.property
    @jsii.member(jsii_name="samlInput")
    def saml_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequireSaml"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AccessGroupRequireSaml"]]], jsii.get(self, "samlInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceTokenInput")
    def service_token_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serviceTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="anyValidServiceToken")
    def any_valid_service_token(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "anyValidServiceToken"))

    @any_valid_service_token.setter
    def any_valid_service_token(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOutputReference, "any_valid_service_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anyValidServiceToken", value)

    @builtins.property
    @jsii.member(jsii_name="authMethod")
    def auth_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authMethod"))

    @auth_method.setter
    def auth_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOutputReference, "auth_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMethod", value)

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @common_name.setter
    def common_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOutputReference, "common_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonName", value)

    @builtins.property
    @jsii.member(jsii_name="devicePosture")
    def device_posture(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "devicePosture"))

    @device_posture.setter
    def device_posture(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOutputReference, "device_posture").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "devicePosture", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="emailDomain")
    def email_domain(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emailDomain"))

    @email_domain.setter
    def email_domain(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOutputReference, "email_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailDomain", value)

    @builtins.property
    @jsii.member(jsii_name="everyone")
    def everyone(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "everyone"))

    @everyone.setter
    def everyone(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOutputReference, "everyone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "everyone", value)

    @builtins.property
    @jsii.member(jsii_name="geo")
    def geo(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "geo"))

    @geo.setter
    def geo(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOutputReference, "geo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geo", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "group"))

    @group.setter
    def group(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOutputReference, "group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ip"))

    @ip.setter
    def ip(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOutputReference, "ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ip", value)

    @builtins.property
    @jsii.member(jsii_name="loginMethod")
    def login_method(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loginMethod"))

    @login_method.setter
    def login_method(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOutputReference, "login_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginMethod", value)

    @builtins.property
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serviceToken"))

    @service_token.setter
    def service_token(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOutputReference, "service_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupRequire, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupRequire, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupRequire, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireSaml",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_name": "attributeName",
        "attribute_value": "attributeValue",
        "identity_provider_id": "identityProviderId",
    },
)
class AccessGroupRequireSaml:
    def __init__(
        self,
        *,
        attribute_name: typing.Optional[builtins.str] = None,
        attribute_value: typing.Optional[builtins.str] = None,
        identity_provider_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param attribute_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#attribute_name AccessGroup#attribute_name}.
        :param attribute_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#attribute_value AccessGroup#attribute_value}.
        :param identity_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireSaml.__init__)
            check_type(argname="argument attribute_name", value=attribute_name, expected_type=type_hints["attribute_name"])
            check_type(argname="argument attribute_value", value=attribute_value, expected_type=type_hints["attribute_value"])
            check_type(argname="argument identity_provider_id", value=identity_provider_id, expected_type=type_hints["identity_provider_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if attribute_name is not None:
            self._values["attribute_name"] = attribute_name
        if attribute_value is not None:
            self._values["attribute_value"] = attribute_value
        if identity_provider_id is not None:
            self._values["identity_provider_id"] = identity_provider_id

    @builtins.property
    def attribute_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#attribute_name AccessGroup#attribute_name}.'''
        result = self._values.get("attribute_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attribute_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#attribute_value AccessGroup#attribute_value}.'''
        result = self._values.get("attribute_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_provider_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/access_group#identity_provider_id AccessGroup#identity_provider_id}.'''
        result = self._values.get("identity_provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGroupRequireSaml(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AccessGroupRequireSamlList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireSamlList",
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
            type_hints = typing.get_type_hints(AccessGroupRequireSamlList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AccessGroupRequireSamlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AccessGroupRequireSamlList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AccessGroupRequireSamlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireSamlList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireSamlList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireSamlList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireSaml]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireSaml]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AccessGroupRequireSaml]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireSamlList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AccessGroupRequireSamlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.accessGroup.AccessGroupRequireSamlOutputReference",
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
            type_hints = typing.get_type_hints(AccessGroupRequireSamlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAttributeName")
    def reset_attribute_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeName", []))

    @jsii.member(jsii_name="resetAttributeValue")
    def reset_attribute_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeValue", []))

    @jsii.member(jsii_name="resetIdentityProviderId")
    def reset_identity_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderId", []))

    @builtins.property
    @jsii.member(jsii_name="attributeNameInput")
    def attribute_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeValueInput")
    def attribute_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeValueInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderIdInput")
    def identity_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeName")
    def attribute_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeName"))

    @attribute_name.setter
    def attribute_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireSamlOutputReference, "attribute_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeName", value)

    @builtins.property
    @jsii.member(jsii_name="attributeValue")
    def attribute_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeValue"))

    @attribute_value.setter
    def attribute_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireSamlOutputReference, "attribute_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeValue", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderId")
    def identity_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderId"))

    @identity_provider_id.setter
    def identity_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireSamlOutputReference, "identity_provider_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AccessGroupRequireSaml, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AccessGroupRequireSaml, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AccessGroupRequireSaml, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AccessGroupRequireSamlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AccessGroup",
    "AccessGroupConfig",
    "AccessGroupExclude",
    "AccessGroupExcludeAzure",
    "AccessGroupExcludeAzureList",
    "AccessGroupExcludeAzureOutputReference",
    "AccessGroupExcludeExternalEvaluation",
    "AccessGroupExcludeExternalEvaluationOutputReference",
    "AccessGroupExcludeGithub",
    "AccessGroupExcludeGithubList",
    "AccessGroupExcludeGithubOutputReference",
    "AccessGroupExcludeGsuite",
    "AccessGroupExcludeGsuiteList",
    "AccessGroupExcludeGsuiteOutputReference",
    "AccessGroupExcludeList",
    "AccessGroupExcludeOkta",
    "AccessGroupExcludeOktaList",
    "AccessGroupExcludeOktaOutputReference",
    "AccessGroupExcludeOutputReference",
    "AccessGroupExcludeSaml",
    "AccessGroupExcludeSamlList",
    "AccessGroupExcludeSamlOutputReference",
    "AccessGroupInclude",
    "AccessGroupIncludeAzure",
    "AccessGroupIncludeAzureList",
    "AccessGroupIncludeAzureOutputReference",
    "AccessGroupIncludeExternalEvaluation",
    "AccessGroupIncludeExternalEvaluationOutputReference",
    "AccessGroupIncludeGithub",
    "AccessGroupIncludeGithubList",
    "AccessGroupIncludeGithubOutputReference",
    "AccessGroupIncludeGsuite",
    "AccessGroupIncludeGsuiteList",
    "AccessGroupIncludeGsuiteOutputReference",
    "AccessGroupIncludeList",
    "AccessGroupIncludeOkta",
    "AccessGroupIncludeOktaList",
    "AccessGroupIncludeOktaOutputReference",
    "AccessGroupIncludeOutputReference",
    "AccessGroupIncludeSaml",
    "AccessGroupIncludeSamlList",
    "AccessGroupIncludeSamlOutputReference",
    "AccessGroupRequire",
    "AccessGroupRequireAzure",
    "AccessGroupRequireAzureList",
    "AccessGroupRequireAzureOutputReference",
    "AccessGroupRequireExternalEvaluation",
    "AccessGroupRequireExternalEvaluationOutputReference",
    "AccessGroupRequireGithub",
    "AccessGroupRequireGithubList",
    "AccessGroupRequireGithubOutputReference",
    "AccessGroupRequireGsuite",
    "AccessGroupRequireGsuiteList",
    "AccessGroupRequireGsuiteOutputReference",
    "AccessGroupRequireList",
    "AccessGroupRequireOkta",
    "AccessGroupRequireOktaList",
    "AccessGroupRequireOktaOutputReference",
    "AccessGroupRequireOutputReference",
    "AccessGroupRequireSaml",
    "AccessGroupRequireSamlList",
    "AccessGroupRequireSamlOutputReference",
]

publication.publish()
