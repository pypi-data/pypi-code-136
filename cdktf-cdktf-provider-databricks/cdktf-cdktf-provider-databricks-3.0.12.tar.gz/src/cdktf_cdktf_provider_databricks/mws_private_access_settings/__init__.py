'''
# `databricks_mws_private_access_settings`

Refer to the Terraform Registory for docs: [`databricks_mws_private_access_settings`](https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings).
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


class MwsPrivateAccessSettings(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mwsPrivateAccessSettings.MwsPrivateAccessSettings",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings databricks_mws_private_access_settings}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        private_access_settings_name: builtins.str,
        region: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        allowed_vpc_endpoint_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        private_access_level: typing.Optional[builtins.str] = None,
        private_access_settings_id: typing.Optional[builtins.str] = None,
        public_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        status: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings databricks_mws_private_access_settings} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param private_access_settings_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#private_access_settings_name MwsPrivateAccessSettings#private_access_settings_name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#region MwsPrivateAccessSettings#region}.
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#account_id MwsPrivateAccessSettings#account_id}.
        :param allowed_vpc_endpoint_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#allowed_vpc_endpoint_ids MwsPrivateAccessSettings#allowed_vpc_endpoint_ids}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#id MwsPrivateAccessSettings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param private_access_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#private_access_level MwsPrivateAccessSettings#private_access_level}.
        :param private_access_settings_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#private_access_settings_id MwsPrivateAccessSettings#private_access_settings_id}.
        :param public_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#public_access_enabled MwsPrivateAccessSettings#public_access_enabled}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#status MwsPrivateAccessSettings#status}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MwsPrivateAccessSettings.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MwsPrivateAccessSettingsConfig(
            private_access_settings_name=private_access_settings_name,
            region=region,
            account_id=account_id,
            allowed_vpc_endpoint_ids=allowed_vpc_endpoint_ids,
            id=id,
            private_access_level=private_access_level,
            private_access_settings_id=private_access_settings_id,
            public_access_enabled=public_access_enabled,
            status=status,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetAllowedVpcEndpointIds")
    def reset_allowed_vpc_endpoint_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedVpcEndpointIds", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPrivateAccessLevel")
    def reset_private_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateAccessLevel", []))

    @jsii.member(jsii_name="resetPrivateAccessSettingsId")
    def reset_private_access_settings_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateAccessSettingsId", []))

    @jsii.member(jsii_name="resetPublicAccessEnabled")
    def reset_public_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicAccessEnabled", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedVpcEndpointIdsInput")
    def allowed_vpc_endpoint_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedVpcEndpointIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="privateAccessLevelInput")
    def private_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="privateAccessSettingsIdInput")
    def private_access_settings_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateAccessSettingsIdInput"))

    @builtins.property
    @jsii.member(jsii_name="privateAccessSettingsNameInput")
    def private_access_settings_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateAccessSettingsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicAccessEnabledInput")
    def public_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsPrivateAccessSettings, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="allowedVpcEndpointIds")
    def allowed_vpc_endpoint_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedVpcEndpointIds"))

    @allowed_vpc_endpoint_ids.setter
    def allowed_vpc_endpoint_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsPrivateAccessSettings, "allowed_vpc_endpoint_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedVpcEndpointIds", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsPrivateAccessSettings, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="privateAccessLevel")
    def private_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateAccessLevel"))

    @private_access_level.setter
    def private_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsPrivateAccessSettings, "private_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="privateAccessSettingsId")
    def private_access_settings_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateAccessSettingsId"))

    @private_access_settings_id.setter
    def private_access_settings_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsPrivateAccessSettings, "private_access_settings_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateAccessSettingsId", value)

    @builtins.property
    @jsii.member(jsii_name="privateAccessSettingsName")
    def private_access_settings_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateAccessSettingsName"))

    @private_access_settings_name.setter
    def private_access_settings_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsPrivateAccessSettings, "private_access_settings_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateAccessSettingsName", value)

    @builtins.property
    @jsii.member(jsii_name="publicAccessEnabled")
    def public_access_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publicAccessEnabled"))

    @public_access_enabled.setter
    def public_access_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsPrivateAccessSettings, "public_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsPrivateAccessSettings, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsPrivateAccessSettings, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mwsPrivateAccessSettings.MwsPrivateAccessSettingsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "private_access_settings_name": "privateAccessSettingsName",
        "region": "region",
        "account_id": "accountId",
        "allowed_vpc_endpoint_ids": "allowedVpcEndpointIds",
        "id": "id",
        "private_access_level": "privateAccessLevel",
        "private_access_settings_id": "privateAccessSettingsId",
        "public_access_enabled": "publicAccessEnabled",
        "status": "status",
    },
)
class MwsPrivateAccessSettingsConfig(cdktf.TerraformMetaArguments):
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
        private_access_settings_name: builtins.str,
        region: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        allowed_vpc_endpoint_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        private_access_level: typing.Optional[builtins.str] = None,
        private_access_settings_id: typing.Optional[builtins.str] = None,
        public_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param private_access_settings_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#private_access_settings_name MwsPrivateAccessSettings#private_access_settings_name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#region MwsPrivateAccessSettings#region}.
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#account_id MwsPrivateAccessSettings#account_id}.
        :param allowed_vpc_endpoint_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#allowed_vpc_endpoint_ids MwsPrivateAccessSettings#allowed_vpc_endpoint_ids}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#id MwsPrivateAccessSettings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param private_access_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#private_access_level MwsPrivateAccessSettings#private_access_level}.
        :param private_access_settings_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#private_access_settings_id MwsPrivateAccessSettings#private_access_settings_id}.
        :param public_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#public_access_enabled MwsPrivateAccessSettings#public_access_enabled}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#status MwsPrivateAccessSettings#status}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(MwsPrivateAccessSettingsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument private_access_settings_name", value=private_access_settings_name, expected_type=type_hints["private_access_settings_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument allowed_vpc_endpoint_ids", value=allowed_vpc_endpoint_ids, expected_type=type_hints["allowed_vpc_endpoint_ids"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument private_access_level", value=private_access_level, expected_type=type_hints["private_access_level"])
            check_type(argname="argument private_access_settings_id", value=private_access_settings_id, expected_type=type_hints["private_access_settings_id"])
            check_type(argname="argument public_access_enabled", value=public_access_enabled, expected_type=type_hints["public_access_enabled"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[str, typing.Any] = {
            "private_access_settings_name": private_access_settings_name,
            "region": region,
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
        if allowed_vpc_endpoint_ids is not None:
            self._values["allowed_vpc_endpoint_ids"] = allowed_vpc_endpoint_ids
        if id is not None:
            self._values["id"] = id
        if private_access_level is not None:
            self._values["private_access_level"] = private_access_level
        if private_access_settings_id is not None:
            self._values["private_access_settings_id"] = private_access_settings_id
        if public_access_enabled is not None:
            self._values["public_access_enabled"] = public_access_enabled
        if status is not None:
            self._values["status"] = status

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
    def private_access_settings_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#private_access_settings_name MwsPrivateAccessSettings#private_access_settings_name}.'''
        result = self._values.get("private_access_settings_name")
        assert result is not None, "Required property 'private_access_settings_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#region MwsPrivateAccessSettings#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#account_id MwsPrivateAccessSettings#account_id}.'''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allowed_vpc_endpoint_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#allowed_vpc_endpoint_ids MwsPrivateAccessSettings#allowed_vpc_endpoint_ids}.'''
        result = self._values.get("allowed_vpc_endpoint_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#id MwsPrivateAccessSettings#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_access_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#private_access_level MwsPrivateAccessSettings#private_access_level}.'''
        result = self._values.get("private_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_access_settings_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#private_access_settings_id MwsPrivateAccessSettings#private_access_settings_id}.'''
        result = self._values.get("private_access_settings_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#public_access_enabled MwsPrivateAccessSettings#public_access_enabled}.'''
        result = self._values.get("public_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_private_access_settings#status MwsPrivateAccessSettings#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsPrivateAccessSettingsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "MwsPrivateAccessSettings",
    "MwsPrivateAccessSettingsConfig",
]

publication.publish()
