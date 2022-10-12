'''
# `azurerm_signalr_service_network_acl`

Refer to the Terraform Registory for docs: [`azurerm_signalr_service_network_acl`](https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl).
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


class SignalrServiceNetworkAcl(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.signalrServiceNetworkAcl.SignalrServiceNetworkAcl",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl azurerm_signalr_service_network_acl}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        default_action: builtins.str,
        public_network: typing.Union["SignalrServiceNetworkAclPublicNetwork", typing.Dict[str, typing.Any]],
        signalr_service_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        private_endpoint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SignalrServiceNetworkAclPrivateEndpoint", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["SignalrServiceNetworkAclTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl azurerm_signalr_service_network_acl} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#default_action SignalrServiceNetworkAcl#default_action}.
        :param public_network: public_network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#public_network SignalrServiceNetworkAcl#public_network}
        :param signalr_service_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#signalr_service_id SignalrServiceNetworkAcl#signalr_service_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#id SignalrServiceNetworkAcl#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param private_endpoint: private_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#private_endpoint SignalrServiceNetworkAcl#private_endpoint}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#timeouts SignalrServiceNetworkAcl#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrServiceNetworkAcl.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SignalrServiceNetworkAclConfig(
            default_action=default_action,
            public_network=public_network,
            signalr_service_id=signalr_service_id,
            id=id,
            private_endpoint=private_endpoint,
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

    @jsii.member(jsii_name="putPrivateEndpoint")
    def put_private_endpoint(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SignalrServiceNetworkAclPrivateEndpoint", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrServiceNetworkAcl.put_private_endpoint)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPrivateEndpoint", [value]))

    @jsii.member(jsii_name="putPublicNetwork")
    def put_public_network(
        self,
        *,
        allowed_request_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        denied_request_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param allowed_request_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#allowed_request_types SignalrServiceNetworkAcl#allowed_request_types}.
        :param denied_request_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#denied_request_types SignalrServiceNetworkAcl#denied_request_types}.
        '''
        value = SignalrServiceNetworkAclPublicNetwork(
            allowed_request_types=allowed_request_types,
            denied_request_types=denied_request_types,
        )

        return typing.cast(None, jsii.invoke(self, "putPublicNetwork", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#create SignalrServiceNetworkAcl#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#delete SignalrServiceNetworkAcl#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#read SignalrServiceNetworkAcl#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#update SignalrServiceNetworkAcl#update}.
        '''
        value = SignalrServiceNetworkAclTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPrivateEndpoint")
    def reset_private_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateEndpoint", []))

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
    @jsii.member(jsii_name="privateEndpoint")
    def private_endpoint(self) -> "SignalrServiceNetworkAclPrivateEndpointList":
        return typing.cast("SignalrServiceNetworkAclPrivateEndpointList", jsii.get(self, "privateEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="publicNetwork")
    def public_network(self) -> "SignalrServiceNetworkAclPublicNetworkOutputReference":
        return typing.cast("SignalrServiceNetworkAclPublicNetworkOutputReference", jsii.get(self, "publicNetwork"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SignalrServiceNetworkAclTimeoutsOutputReference":
        return typing.cast("SignalrServiceNetworkAclTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="defaultActionInput")
    def default_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultActionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="privateEndpointInput")
    def private_endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SignalrServiceNetworkAclPrivateEndpoint"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SignalrServiceNetworkAclPrivateEndpoint"]]], jsii.get(self, "privateEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkInput")
    def public_network_input(
        self,
    ) -> typing.Optional["SignalrServiceNetworkAclPublicNetwork"]:
        return typing.cast(typing.Optional["SignalrServiceNetworkAclPublicNetwork"], jsii.get(self, "publicNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="signalrServiceIdInput")
    def signalr_service_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signalrServiceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SignalrServiceNetworkAclTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SignalrServiceNetworkAclTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultAction")
    def default_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultAction"))

    @default_action.setter
    def default_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAcl, "default_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAction", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAcl, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="signalrServiceId")
    def signalr_service_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signalrServiceId"))

    @signalr_service_id.setter
    def signalr_service_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAcl, "signalr_service_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalrServiceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.signalrServiceNetworkAcl.SignalrServiceNetworkAclConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "default_action": "defaultAction",
        "public_network": "publicNetwork",
        "signalr_service_id": "signalrServiceId",
        "id": "id",
        "private_endpoint": "privateEndpoint",
        "timeouts": "timeouts",
    },
)
class SignalrServiceNetworkAclConfig(cdktf.TerraformMetaArguments):
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
        default_action: builtins.str,
        public_network: typing.Union["SignalrServiceNetworkAclPublicNetwork", typing.Dict[str, typing.Any]],
        signalr_service_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        private_endpoint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SignalrServiceNetworkAclPrivateEndpoint", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["SignalrServiceNetworkAclTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param default_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#default_action SignalrServiceNetworkAcl#default_action}.
        :param public_network: public_network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#public_network SignalrServiceNetworkAcl#public_network}
        :param signalr_service_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#signalr_service_id SignalrServiceNetworkAcl#signalr_service_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#id SignalrServiceNetworkAcl#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param private_endpoint: private_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#private_endpoint SignalrServiceNetworkAcl#private_endpoint}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#timeouts SignalrServiceNetworkAcl#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(public_network, dict):
            public_network = SignalrServiceNetworkAclPublicNetwork(**public_network)
        if isinstance(timeouts, dict):
            timeouts = SignalrServiceNetworkAclTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SignalrServiceNetworkAclConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument default_action", value=default_action, expected_type=type_hints["default_action"])
            check_type(argname="argument public_network", value=public_network, expected_type=type_hints["public_network"])
            check_type(argname="argument signalr_service_id", value=signalr_service_id, expected_type=type_hints["signalr_service_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument private_endpoint", value=private_endpoint, expected_type=type_hints["private_endpoint"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_action": default_action,
            "public_network": public_network,
            "signalr_service_id": signalr_service_id,
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
        if private_endpoint is not None:
            self._values["private_endpoint"] = private_endpoint
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
    def default_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#default_action SignalrServiceNetworkAcl#default_action}.'''
        result = self._values.get("default_action")
        assert result is not None, "Required property 'default_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_network(self) -> "SignalrServiceNetworkAclPublicNetwork":
        '''public_network block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#public_network SignalrServiceNetworkAcl#public_network}
        '''
        result = self._values.get("public_network")
        assert result is not None, "Required property 'public_network' is missing"
        return typing.cast("SignalrServiceNetworkAclPublicNetwork", result)

    @builtins.property
    def signalr_service_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#signalr_service_id SignalrServiceNetworkAcl#signalr_service_id}.'''
        result = self._values.get("signalr_service_id")
        assert result is not None, "Required property 'signalr_service_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#id SignalrServiceNetworkAcl#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_endpoint(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SignalrServiceNetworkAclPrivateEndpoint"]]]:
        '''private_endpoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#private_endpoint SignalrServiceNetworkAcl#private_endpoint}
        '''
        result = self._values.get("private_endpoint")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SignalrServiceNetworkAclPrivateEndpoint"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SignalrServiceNetworkAclTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#timeouts SignalrServiceNetworkAcl#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SignalrServiceNetworkAclTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SignalrServiceNetworkAclConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.signalrServiceNetworkAcl.SignalrServiceNetworkAclPrivateEndpoint",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "allowed_request_types": "allowedRequestTypes",
        "denied_request_types": "deniedRequestTypes",
    },
)
class SignalrServiceNetworkAclPrivateEndpoint:
    def __init__(
        self,
        *,
        id: builtins.str,
        allowed_request_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        denied_request_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#id SignalrServiceNetworkAcl#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param allowed_request_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#allowed_request_types SignalrServiceNetworkAcl#allowed_request_types}.
        :param denied_request_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#denied_request_types SignalrServiceNetworkAcl#denied_request_types}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrServiceNetworkAclPrivateEndpoint.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument allowed_request_types", value=allowed_request_types, expected_type=type_hints["allowed_request_types"])
            check_type(argname="argument denied_request_types", value=denied_request_types, expected_type=type_hints["denied_request_types"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if allowed_request_types is not None:
            self._values["allowed_request_types"] = allowed_request_types
        if denied_request_types is not None:
            self._values["denied_request_types"] = denied_request_types

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#id SignalrServiceNetworkAcl#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_request_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#allowed_request_types SignalrServiceNetworkAcl#allowed_request_types}.'''
        result = self._values.get("allowed_request_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def denied_request_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#denied_request_types SignalrServiceNetworkAcl#denied_request_types}.'''
        result = self._values.get("denied_request_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SignalrServiceNetworkAclPrivateEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SignalrServiceNetworkAclPrivateEndpointList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.signalrServiceNetworkAcl.SignalrServiceNetworkAclPrivateEndpointList",
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
            type_hints = typing.get_type_hints(SignalrServiceNetworkAclPrivateEndpointList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SignalrServiceNetworkAclPrivateEndpointOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrServiceNetworkAclPrivateEndpointList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SignalrServiceNetworkAclPrivateEndpointOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclPrivateEndpointList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclPrivateEndpointList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclPrivateEndpointList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SignalrServiceNetworkAclPrivateEndpoint]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SignalrServiceNetworkAclPrivateEndpoint]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SignalrServiceNetworkAclPrivateEndpoint]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclPrivateEndpointList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SignalrServiceNetworkAclPrivateEndpointOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.signalrServiceNetworkAcl.SignalrServiceNetworkAclPrivateEndpointOutputReference",
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
            type_hints = typing.get_type_hints(SignalrServiceNetworkAclPrivateEndpointOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedRequestTypes")
    def reset_allowed_request_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRequestTypes", []))

    @jsii.member(jsii_name="resetDeniedRequestTypes")
    def reset_denied_request_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeniedRequestTypes", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRequestTypesInput")
    def allowed_request_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRequestTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="deniedRequestTypesInput")
    def denied_request_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "deniedRequestTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRequestTypes")
    def allowed_request_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRequestTypes"))

    @allowed_request_types.setter
    def allowed_request_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclPrivateEndpointOutputReference, "allowed_request_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRequestTypes", value)

    @builtins.property
    @jsii.member(jsii_name="deniedRequestTypes")
    def denied_request_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "deniedRequestTypes"))

    @denied_request_types.setter
    def denied_request_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclPrivateEndpointOutputReference, "denied_request_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deniedRequestTypes", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclPrivateEndpointOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SignalrServiceNetworkAclPrivateEndpoint, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SignalrServiceNetworkAclPrivateEndpoint, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SignalrServiceNetworkAclPrivateEndpoint, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclPrivateEndpointOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.signalrServiceNetworkAcl.SignalrServiceNetworkAclPublicNetwork",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_request_types": "allowedRequestTypes",
        "denied_request_types": "deniedRequestTypes",
    },
)
class SignalrServiceNetworkAclPublicNetwork:
    def __init__(
        self,
        *,
        allowed_request_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        denied_request_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param allowed_request_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#allowed_request_types SignalrServiceNetworkAcl#allowed_request_types}.
        :param denied_request_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#denied_request_types SignalrServiceNetworkAcl#denied_request_types}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrServiceNetworkAclPublicNetwork.__init__)
            check_type(argname="argument allowed_request_types", value=allowed_request_types, expected_type=type_hints["allowed_request_types"])
            check_type(argname="argument denied_request_types", value=denied_request_types, expected_type=type_hints["denied_request_types"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_request_types is not None:
            self._values["allowed_request_types"] = allowed_request_types
        if denied_request_types is not None:
            self._values["denied_request_types"] = denied_request_types

    @builtins.property
    def allowed_request_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#allowed_request_types SignalrServiceNetworkAcl#allowed_request_types}.'''
        result = self._values.get("allowed_request_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def denied_request_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#denied_request_types SignalrServiceNetworkAcl#denied_request_types}.'''
        result = self._values.get("denied_request_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SignalrServiceNetworkAclPublicNetwork(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SignalrServiceNetworkAclPublicNetworkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.signalrServiceNetworkAcl.SignalrServiceNetworkAclPublicNetworkOutputReference",
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
            type_hints = typing.get_type_hints(SignalrServiceNetworkAclPublicNetworkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedRequestTypes")
    def reset_allowed_request_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedRequestTypes", []))

    @jsii.member(jsii_name="resetDeniedRequestTypes")
    def reset_denied_request_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeniedRequestTypes", []))

    @builtins.property
    @jsii.member(jsii_name="allowedRequestTypesInput")
    def allowed_request_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedRequestTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="deniedRequestTypesInput")
    def denied_request_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "deniedRequestTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedRequestTypes")
    def allowed_request_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedRequestTypes"))

    @allowed_request_types.setter
    def allowed_request_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclPublicNetworkOutputReference, "allowed_request_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedRequestTypes", value)

    @builtins.property
    @jsii.member(jsii_name="deniedRequestTypes")
    def denied_request_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "deniedRequestTypes"))

    @denied_request_types.setter
    def denied_request_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclPublicNetworkOutputReference, "denied_request_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deniedRequestTypes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SignalrServiceNetworkAclPublicNetwork]:
        return typing.cast(typing.Optional[SignalrServiceNetworkAclPublicNetwork], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SignalrServiceNetworkAclPublicNetwork],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclPublicNetworkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.signalrServiceNetworkAcl.SignalrServiceNetworkAclTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SignalrServiceNetworkAclTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#create SignalrServiceNetworkAcl#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#delete SignalrServiceNetworkAcl#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#read SignalrServiceNetworkAcl#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#update SignalrServiceNetworkAcl#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrServiceNetworkAclTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#create SignalrServiceNetworkAcl#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#delete SignalrServiceNetworkAcl#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#read SignalrServiceNetworkAcl#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service_network_acl#update SignalrServiceNetworkAcl#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SignalrServiceNetworkAclTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SignalrServiceNetworkAclTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.signalrServiceNetworkAcl.SignalrServiceNetworkAclTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SignalrServiceNetworkAclTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SignalrServiceNetworkAclTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SignalrServiceNetworkAclTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SignalrServiceNetworkAclTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceNetworkAclTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SignalrServiceNetworkAcl",
    "SignalrServiceNetworkAclConfig",
    "SignalrServiceNetworkAclPrivateEndpoint",
    "SignalrServiceNetworkAclPrivateEndpointList",
    "SignalrServiceNetworkAclPrivateEndpointOutputReference",
    "SignalrServiceNetworkAclPublicNetwork",
    "SignalrServiceNetworkAclPublicNetworkOutputReference",
    "SignalrServiceNetworkAclTimeouts",
    "SignalrServiceNetworkAclTimeoutsOutputReference",
]

publication.publish()
