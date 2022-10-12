'''
# `azurerm_app_service_slot_custom_hostname_binding`

Refer to the Terraform Registory for docs: [`azurerm_app_service_slot_custom_hostname_binding`](https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding).
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


class AppServiceSlotCustomHostnameBinding(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.appServiceSlotCustomHostnameBinding.AppServiceSlotCustomHostnameBinding",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding azurerm_app_service_slot_custom_hostname_binding}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        app_service_slot_id: builtins.str,
        hostname: builtins.str,
        id: typing.Optional[builtins.str] = None,
        ssl_state: typing.Optional[builtins.str] = None,
        thumbprint: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["AppServiceSlotCustomHostnameBindingTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding azurerm_app_service_slot_custom_hostname_binding} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param app_service_slot_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#app_service_slot_id AppServiceSlotCustomHostnameBinding#app_service_slot_id}.
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#hostname AppServiceSlotCustomHostnameBinding#hostname}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#id AppServiceSlotCustomHostnameBinding#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ssl_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#ssl_state AppServiceSlotCustomHostnameBinding#ssl_state}.
        :param thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#thumbprint AppServiceSlotCustomHostnameBinding#thumbprint}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#timeouts AppServiceSlotCustomHostnameBinding#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppServiceSlotCustomHostnameBinding.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppServiceSlotCustomHostnameBindingConfig(
            app_service_slot_id=app_service_slot_id,
            hostname=hostname,
            id=id,
            ssl_state=ssl_state,
            thumbprint=thumbprint,
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
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#create AppServiceSlotCustomHostnameBinding#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#delete AppServiceSlotCustomHostnameBinding#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#read AppServiceSlotCustomHostnameBinding#read}.
        '''
        value = AppServiceSlotCustomHostnameBindingTimeouts(
            create=create, delete=delete, read=read
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSslState")
    def reset_ssl_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslState", []))

    @jsii.member(jsii_name="resetThumbprint")
    def reset_thumbprint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThumbprint", []))

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
    def timeouts(self) -> "AppServiceSlotCustomHostnameBindingTimeoutsOutputReference":
        return typing.cast("AppServiceSlotCustomHostnameBindingTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="virtualIp")
    def virtual_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualIp"))

    @builtins.property
    @jsii.member(jsii_name="appServiceSlotIdInput")
    def app_service_slot_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appServiceSlotIdInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="sslStateInput")
    def ssl_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslStateInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbprintInput")
    def thumbprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["AppServiceSlotCustomHostnameBindingTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["AppServiceSlotCustomHostnameBindingTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="appServiceSlotId")
    def app_service_slot_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appServiceSlotId"))

    @app_service_slot_id.setter
    def app_service_slot_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceSlotCustomHostnameBinding, "app_service_slot_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appServiceSlotId", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceSlotCustomHostnameBinding, "hostname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceSlotCustomHostnameBinding, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="sslState")
    def ssl_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslState"))

    @ssl_state.setter
    def ssl_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceSlotCustomHostnameBinding, "ssl_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslState", value)

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @thumbprint.setter
    def thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceSlotCustomHostnameBinding, "thumbprint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thumbprint", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.appServiceSlotCustomHostnameBinding.AppServiceSlotCustomHostnameBindingConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "app_service_slot_id": "appServiceSlotId",
        "hostname": "hostname",
        "id": "id",
        "ssl_state": "sslState",
        "thumbprint": "thumbprint",
        "timeouts": "timeouts",
    },
)
class AppServiceSlotCustomHostnameBindingConfig(cdktf.TerraformMetaArguments):
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
        app_service_slot_id: builtins.str,
        hostname: builtins.str,
        id: typing.Optional[builtins.str] = None,
        ssl_state: typing.Optional[builtins.str] = None,
        thumbprint: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["AppServiceSlotCustomHostnameBindingTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param app_service_slot_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#app_service_slot_id AppServiceSlotCustomHostnameBinding#app_service_slot_id}.
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#hostname AppServiceSlotCustomHostnameBinding#hostname}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#id AppServiceSlotCustomHostnameBinding#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ssl_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#ssl_state AppServiceSlotCustomHostnameBinding#ssl_state}.
        :param thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#thumbprint AppServiceSlotCustomHostnameBinding#thumbprint}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#timeouts AppServiceSlotCustomHostnameBinding#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = AppServiceSlotCustomHostnameBindingTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(AppServiceSlotCustomHostnameBindingConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument app_service_slot_id", value=app_service_slot_id, expected_type=type_hints["app_service_slot_id"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ssl_state", value=ssl_state, expected_type=type_hints["ssl_state"])
            check_type(argname="argument thumbprint", value=thumbprint, expected_type=type_hints["thumbprint"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "app_service_slot_id": app_service_slot_id,
            "hostname": hostname,
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
        if id is not None:
            self._values["id"] = id
        if ssl_state is not None:
            self._values["ssl_state"] = ssl_state
        if thumbprint is not None:
            self._values["thumbprint"] = thumbprint
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
    def app_service_slot_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#app_service_slot_id AppServiceSlotCustomHostnameBinding#app_service_slot_id}.'''
        result = self._values.get("app_service_slot_id")
        assert result is not None, "Required property 'app_service_slot_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hostname(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#hostname AppServiceSlotCustomHostnameBinding#hostname}.'''
        result = self._values.get("hostname")
        assert result is not None, "Required property 'hostname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#id AppServiceSlotCustomHostnameBinding#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#ssl_state AppServiceSlotCustomHostnameBinding#ssl_state}.'''
        result = self._values.get("ssl_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def thumbprint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#thumbprint AppServiceSlotCustomHostnameBinding#thumbprint}.'''
        result = self._values.get("thumbprint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["AppServiceSlotCustomHostnameBindingTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#timeouts AppServiceSlotCustomHostnameBinding#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["AppServiceSlotCustomHostnameBindingTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppServiceSlotCustomHostnameBindingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.appServiceSlotCustomHostnameBinding.AppServiceSlotCustomHostnameBindingTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "read": "read"},
)
class AppServiceSlotCustomHostnameBindingTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#create AppServiceSlotCustomHostnameBinding#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#delete AppServiceSlotCustomHostnameBinding#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#read AppServiceSlotCustomHostnameBinding#read}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppServiceSlotCustomHostnameBindingTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#create AppServiceSlotCustomHostnameBinding#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#delete AppServiceSlotCustomHostnameBinding#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/app_service_slot_custom_hostname_binding#read AppServiceSlotCustomHostnameBinding#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppServiceSlotCustomHostnameBindingTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppServiceSlotCustomHostnameBindingTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.appServiceSlotCustomHostnameBinding.AppServiceSlotCustomHostnameBindingTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(AppServiceSlotCustomHostnameBindingTimeoutsOutputReference.__init__)
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
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceSlotCustomHostnameBindingTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceSlotCustomHostnameBindingTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceSlotCustomHostnameBindingTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppServiceSlotCustomHostnameBindingTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppServiceSlotCustomHostnameBindingTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppServiceSlotCustomHostnameBindingTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppServiceSlotCustomHostnameBindingTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppServiceSlotCustomHostnameBinding",
    "AppServiceSlotCustomHostnameBindingConfig",
    "AppServiceSlotCustomHostnameBindingTimeouts",
    "AppServiceSlotCustomHostnameBindingTimeoutsOutputReference",
]

publication.publish()
