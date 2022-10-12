'''
# `azurerm_container_registry_token_password`

Refer to the Terraform Registory for docs: [`azurerm_container_registry_token_password`](https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password).
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


class ContainerRegistryTokenPassword(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTokenPassword.ContainerRegistryTokenPassword",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password azurerm_container_registry_token_password}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        container_registry_token_id: builtins.str,
        password1: typing.Union["ContainerRegistryTokenPasswordPassword1", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        password2: typing.Optional[typing.Union["ContainerRegistryTokenPasswordPassword2", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["ContainerRegistryTokenPasswordTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password azurerm_container_registry_token_password} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param container_registry_token_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#container_registry_token_id ContainerRegistryTokenPassword#container_registry_token_id}.
        :param password1: password1 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#password1 ContainerRegistryTokenPassword#password1}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#id ContainerRegistryTokenPassword#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password2: password2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#password2 ContainerRegistryTokenPassword#password2}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#timeouts ContainerRegistryTokenPassword#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTokenPassword.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ContainerRegistryTokenPasswordConfig(
            container_registry_token_id=container_registry_token_id,
            password1=password1,
            id=id,
            password2=password2,
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

    @jsii.member(jsii_name="putPassword1")
    def put_password1(self, *, expiry: typing.Optional[builtins.str] = None) -> None:
        '''
        :param expiry: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#expiry ContainerRegistryTokenPassword#expiry}.
        '''
        value = ContainerRegistryTokenPasswordPassword1(expiry=expiry)

        return typing.cast(None, jsii.invoke(self, "putPassword1", [value]))

    @jsii.member(jsii_name="putPassword2")
    def put_password2(self, *, expiry: typing.Optional[builtins.str] = None) -> None:
        '''
        :param expiry: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#expiry ContainerRegistryTokenPassword#expiry}.
        '''
        value = ContainerRegistryTokenPasswordPassword2(expiry=expiry)

        return typing.cast(None, jsii.invoke(self, "putPassword2", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#create ContainerRegistryTokenPassword#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#delete ContainerRegistryTokenPassword#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#read ContainerRegistryTokenPassword#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#update ContainerRegistryTokenPassword#update}.
        '''
        value = ContainerRegistryTokenPasswordTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPassword2")
    def reset_password2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword2", []))

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
    @jsii.member(jsii_name="password1")
    def password1(self) -> "ContainerRegistryTokenPasswordPassword1OutputReference":
        return typing.cast("ContainerRegistryTokenPasswordPassword1OutputReference", jsii.get(self, "password1"))

    @builtins.property
    @jsii.member(jsii_name="password2")
    def password2(self) -> "ContainerRegistryTokenPasswordPassword2OutputReference":
        return typing.cast("ContainerRegistryTokenPasswordPassword2OutputReference", jsii.get(self, "password2"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ContainerRegistryTokenPasswordTimeoutsOutputReference":
        return typing.cast("ContainerRegistryTokenPasswordTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="containerRegistryTokenIdInput")
    def container_registry_token_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerRegistryTokenIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="password1Input")
    def password1_input(
        self,
    ) -> typing.Optional["ContainerRegistryTokenPasswordPassword1"]:
        return typing.cast(typing.Optional["ContainerRegistryTokenPasswordPassword1"], jsii.get(self, "password1Input"))

    @builtins.property
    @jsii.member(jsii_name="password2Input")
    def password2_input(
        self,
    ) -> typing.Optional["ContainerRegistryTokenPasswordPassword2"]:
        return typing.cast(typing.Optional["ContainerRegistryTokenPasswordPassword2"], jsii.get(self, "password2Input"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ContainerRegistryTokenPasswordTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ContainerRegistryTokenPasswordTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="containerRegistryTokenId")
    def container_registry_token_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerRegistryTokenId"))

    @container_registry_token_id.setter
    def container_registry_token_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTokenPassword, "container_registry_token_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryTokenId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTokenPassword, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTokenPassword.ContainerRegistryTokenPasswordConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "container_registry_token_id": "containerRegistryTokenId",
        "password1": "password1",
        "id": "id",
        "password2": "password2",
        "timeouts": "timeouts",
    },
)
class ContainerRegistryTokenPasswordConfig(cdktf.TerraformMetaArguments):
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
        container_registry_token_id: builtins.str,
        password1: typing.Union["ContainerRegistryTokenPasswordPassword1", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        password2: typing.Optional[typing.Union["ContainerRegistryTokenPasswordPassword2", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["ContainerRegistryTokenPasswordTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param container_registry_token_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#container_registry_token_id ContainerRegistryTokenPassword#container_registry_token_id}.
        :param password1: password1 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#password1 ContainerRegistryTokenPassword#password1}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#id ContainerRegistryTokenPassword#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password2: password2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#password2 ContainerRegistryTokenPassword#password2}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#timeouts ContainerRegistryTokenPassword#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(password1, dict):
            password1 = ContainerRegistryTokenPasswordPassword1(**password1)
        if isinstance(password2, dict):
            password2 = ContainerRegistryTokenPasswordPassword2(**password2)
        if isinstance(timeouts, dict):
            timeouts = ContainerRegistryTokenPasswordTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTokenPasswordConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument container_registry_token_id", value=container_registry_token_id, expected_type=type_hints["container_registry_token_id"])
            check_type(argname="argument password1", value=password1, expected_type=type_hints["password1"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument password2", value=password2, expected_type=type_hints["password2"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "container_registry_token_id": container_registry_token_id,
            "password1": password1,
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
        if password2 is not None:
            self._values["password2"] = password2
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
    def container_registry_token_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#container_registry_token_id ContainerRegistryTokenPassword#container_registry_token_id}.'''
        result = self._values.get("container_registry_token_id")
        assert result is not None, "Required property 'container_registry_token_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password1(self) -> "ContainerRegistryTokenPasswordPassword1":
        '''password1 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#password1 ContainerRegistryTokenPassword#password1}
        '''
        result = self._values.get("password1")
        assert result is not None, "Required property 'password1' is missing"
        return typing.cast("ContainerRegistryTokenPasswordPassword1", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#id ContainerRegistryTokenPassword#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password2(self) -> typing.Optional["ContainerRegistryTokenPasswordPassword2"]:
        '''password2 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#password2 ContainerRegistryTokenPassword#password2}
        '''
        result = self._values.get("password2")
        return typing.cast(typing.Optional["ContainerRegistryTokenPasswordPassword2"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ContainerRegistryTokenPasswordTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#timeouts ContainerRegistryTokenPassword#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ContainerRegistryTokenPasswordTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTokenPasswordConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTokenPassword.ContainerRegistryTokenPasswordPassword1",
    jsii_struct_bases=[],
    name_mapping={"expiry": "expiry"},
)
class ContainerRegistryTokenPasswordPassword1:
    def __init__(self, *, expiry: typing.Optional[builtins.str] = None) -> None:
        '''
        :param expiry: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#expiry ContainerRegistryTokenPassword#expiry}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTokenPasswordPassword1.__init__)
            check_type(argname="argument expiry", value=expiry, expected_type=type_hints["expiry"])
        self._values: typing.Dict[str, typing.Any] = {}
        if expiry is not None:
            self._values["expiry"] = expiry

    @builtins.property
    def expiry(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#expiry ContainerRegistryTokenPassword#expiry}.'''
        result = self._values.get("expiry")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTokenPasswordPassword1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerRegistryTokenPasswordPassword1OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTokenPassword.ContainerRegistryTokenPasswordPassword1OutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTokenPasswordPassword1OutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExpiry")
    def reset_expiry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiry", []))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="expiryInput")
    def expiry_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expiryInput"))

    @builtins.property
    @jsii.member(jsii_name="expiry")
    def expiry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiry"))

    @expiry.setter
    def expiry(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTokenPasswordPassword1OutputReference, "expiry").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiry", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerRegistryTokenPasswordPassword1]:
        return typing.cast(typing.Optional[ContainerRegistryTokenPasswordPassword1], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerRegistryTokenPasswordPassword1],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTokenPasswordPassword1OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTokenPassword.ContainerRegistryTokenPasswordPassword2",
    jsii_struct_bases=[],
    name_mapping={"expiry": "expiry"},
)
class ContainerRegistryTokenPasswordPassword2:
    def __init__(self, *, expiry: typing.Optional[builtins.str] = None) -> None:
        '''
        :param expiry: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#expiry ContainerRegistryTokenPassword#expiry}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTokenPasswordPassword2.__init__)
            check_type(argname="argument expiry", value=expiry, expected_type=type_hints["expiry"])
        self._values: typing.Dict[str, typing.Any] = {}
        if expiry is not None:
            self._values["expiry"] = expiry

    @builtins.property
    def expiry(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#expiry ContainerRegistryTokenPassword#expiry}.'''
        result = self._values.get("expiry")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTokenPasswordPassword2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerRegistryTokenPasswordPassword2OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTokenPassword.ContainerRegistryTokenPasswordPassword2OutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTokenPasswordPassword2OutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExpiry")
    def reset_expiry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiry", []))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="expiryInput")
    def expiry_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expiryInput"))

    @builtins.property
    @jsii.member(jsii_name="expiry")
    def expiry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiry"))

    @expiry.setter
    def expiry(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTokenPasswordPassword2OutputReference, "expiry").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiry", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ContainerRegistryTokenPasswordPassword2]:
        return typing.cast(typing.Optional[ContainerRegistryTokenPasswordPassword2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerRegistryTokenPasswordPassword2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTokenPasswordPassword2OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerRegistryTokenPassword.ContainerRegistryTokenPasswordTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ContainerRegistryTokenPasswordTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#create ContainerRegistryTokenPassword#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#delete ContainerRegistryTokenPassword#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#read ContainerRegistryTokenPassword#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#update ContainerRegistryTokenPassword#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerRegistryTokenPasswordTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#create ContainerRegistryTokenPassword#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#delete ContainerRegistryTokenPassword#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#read ContainerRegistryTokenPassword#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_registry_token_password#update ContainerRegistryTokenPassword#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRegistryTokenPasswordTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerRegistryTokenPasswordTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerRegistryTokenPassword.ContainerRegistryTokenPasswordTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerRegistryTokenPasswordTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTokenPasswordTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTokenPasswordTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTokenPasswordTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTokenPasswordTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerRegistryTokenPasswordTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerRegistryTokenPasswordTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerRegistryTokenPasswordTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerRegistryTokenPasswordTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ContainerRegistryTokenPassword",
    "ContainerRegistryTokenPasswordConfig",
    "ContainerRegistryTokenPasswordPassword1",
    "ContainerRegistryTokenPasswordPassword1OutputReference",
    "ContainerRegistryTokenPasswordPassword2",
    "ContainerRegistryTokenPasswordPassword2OutputReference",
    "ContainerRegistryTokenPasswordTimeouts",
    "ContainerRegistryTokenPasswordTimeoutsOutputReference",
]

publication.publish()
