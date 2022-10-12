'''
# `data_hcp_aws_transit_gateway_attachment`

Refer to the Terraform Registory for docs: [`data_hcp_aws_transit_gateway_attachment`](https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment).
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


class DataHcpAwsTransitGatewayAttachment(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.dataHcpAwsTransitGatewayAttachment.DataHcpAwsTransitGatewayAttachment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment hcp_aws_transit_gateway_attachment}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        hvn_id: builtins.str,
        transit_gateway_attachment_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataHcpAwsTransitGatewayAttachmentTimeouts", typing.Dict[str, typing.Any]]] = None,
        wait_for_active_state: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment hcp_aws_transit_gateway_attachment} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param hvn_id: The ID of the HashiCorp Virtual Network (HVN). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#hvn_id DataHcpAwsTransitGatewayAttachment#hvn_id}
        :param transit_gateway_attachment_id: The user-settable name of the transit gateway attachment in HCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#transit_gateway_attachment_id DataHcpAwsTransitGatewayAttachment#transit_gateway_attachment_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#id DataHcpAwsTransitGatewayAttachment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#timeouts DataHcpAwsTransitGatewayAttachment#timeouts}
        :param wait_for_active_state: If ``true``, Terraform will wait for the transit gateway attachment to reach an ``ACTIVE`` state before continuing. Default ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#wait_for_active_state DataHcpAwsTransitGatewayAttachment#wait_for_active_state}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpAwsTransitGatewayAttachment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataHcpAwsTransitGatewayAttachmentConfig(
            hvn_id=hvn_id,
            transit_gateway_attachment_id=transit_gateway_attachment_id,
            id=id,
            timeouts=timeouts,
            wait_for_active_state=wait_for_active_state,
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
    def put_timeouts(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#default DataHcpAwsTransitGatewayAttachment#default}.
        '''
        value = DataHcpAwsTransitGatewayAttachmentTimeouts(default=default)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWaitForActiveState")
    def reset_wait_for_active_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForActiveState", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="expiresAt")
    def expires_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiresAt"))

    @builtins.property
    @jsii.member(jsii_name="organizationId")
    def organization_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationId"))

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @builtins.property
    @jsii.member(jsii_name="providerTransitGatewayAttachmentId")
    def provider_transit_gateway_attachment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "providerTransitGatewayAttachmentId"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DataHcpAwsTransitGatewayAttachmentTimeoutsOutputReference":
        return typing.cast("DataHcpAwsTransitGatewayAttachmentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="transitGatewayId")
    def transit_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayId"))

    @builtins.property
    @jsii.member(jsii_name="hvnIdInput")
    def hvn_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hvnIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataHcpAwsTransitGatewayAttachmentTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataHcpAwsTransitGatewayAttachmentTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="transitGatewayAttachmentIdInput")
    def transit_gateway_attachment_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transitGatewayAttachmentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForActiveStateInput")
    def wait_for_active_state_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "waitForActiveStateInput"))

    @builtins.property
    @jsii.member(jsii_name="hvnId")
    def hvn_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hvnId"))

    @hvn_id.setter
    def hvn_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpAwsTransitGatewayAttachment, "hvn_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hvnId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpAwsTransitGatewayAttachment, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayAttachmentId"))

    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpAwsTransitGatewayAttachment, "transit_gateway_attachment_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitGatewayAttachmentId", value)

    @builtins.property
    @jsii.member(jsii_name="waitForActiveState")
    def wait_for_active_state(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "waitForActiveState"))

    @wait_for_active_state.setter
    def wait_for_active_state(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpAwsTransitGatewayAttachment, "wait_for_active_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForActiveState", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.dataHcpAwsTransitGatewayAttachment.DataHcpAwsTransitGatewayAttachmentConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "hvn_id": "hvnId",
        "transit_gateway_attachment_id": "transitGatewayAttachmentId",
        "id": "id",
        "timeouts": "timeouts",
        "wait_for_active_state": "waitForActiveState",
    },
)
class DataHcpAwsTransitGatewayAttachmentConfig(cdktf.TerraformMetaArguments):
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
        hvn_id: builtins.str,
        transit_gateway_attachment_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataHcpAwsTransitGatewayAttachmentTimeouts", typing.Dict[str, typing.Any]]] = None,
        wait_for_active_state: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param hvn_id: The ID of the HashiCorp Virtual Network (HVN). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#hvn_id DataHcpAwsTransitGatewayAttachment#hvn_id}
        :param transit_gateway_attachment_id: The user-settable name of the transit gateway attachment in HCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#transit_gateway_attachment_id DataHcpAwsTransitGatewayAttachment#transit_gateway_attachment_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#id DataHcpAwsTransitGatewayAttachment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#timeouts DataHcpAwsTransitGatewayAttachment#timeouts}
        :param wait_for_active_state: If ``true``, Terraform will wait for the transit gateway attachment to reach an ``ACTIVE`` state before continuing. Default ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#wait_for_active_state DataHcpAwsTransitGatewayAttachment#wait_for_active_state}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DataHcpAwsTransitGatewayAttachmentTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpAwsTransitGatewayAttachmentConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument hvn_id", value=hvn_id, expected_type=type_hints["hvn_id"])
            check_type(argname="argument transit_gateway_attachment_id", value=transit_gateway_attachment_id, expected_type=type_hints["transit_gateway_attachment_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument wait_for_active_state", value=wait_for_active_state, expected_type=type_hints["wait_for_active_state"])
        self._values: typing.Dict[str, typing.Any] = {
            "hvn_id": hvn_id,
            "transit_gateway_attachment_id": transit_gateway_attachment_id,
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
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if wait_for_active_state is not None:
            self._values["wait_for_active_state"] = wait_for_active_state

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
    def hvn_id(self) -> builtins.str:
        '''The ID of the HashiCorp Virtual Network (HVN).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#hvn_id DataHcpAwsTransitGatewayAttachment#hvn_id}
        '''
        result = self._values.get("hvn_id")
        assert result is not None, "Required property 'hvn_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_attachment_id(self) -> builtins.str:
        '''The user-settable name of the transit gateway attachment in HCP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#transit_gateway_attachment_id DataHcpAwsTransitGatewayAttachment#transit_gateway_attachment_id}
        '''
        result = self._values.get("transit_gateway_attachment_id")
        assert result is not None, "Required property 'transit_gateway_attachment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#id DataHcpAwsTransitGatewayAttachment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataHcpAwsTransitGatewayAttachmentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#timeouts DataHcpAwsTransitGatewayAttachment#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataHcpAwsTransitGatewayAttachmentTimeouts"], result)

    @builtins.property
    def wait_for_active_state(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true``, Terraform will wait for the transit gateway attachment to reach an ``ACTIVE`` state before continuing. Default ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#wait_for_active_state DataHcpAwsTransitGatewayAttachment#wait_for_active_state}
        '''
        result = self._values.get("wait_for_active_state")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataHcpAwsTransitGatewayAttachmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.dataHcpAwsTransitGatewayAttachment.DataHcpAwsTransitGatewayAttachmentTimeouts",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class DataHcpAwsTransitGatewayAttachmentTimeouts:
    def __init__(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#default DataHcpAwsTransitGatewayAttachment#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpAwsTransitGatewayAttachmentTimeouts.__init__)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/aws_transit_gateway_attachment#default DataHcpAwsTransitGatewayAttachment#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataHcpAwsTransitGatewayAttachmentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataHcpAwsTransitGatewayAttachmentTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.dataHcpAwsTransitGatewayAttachment.DataHcpAwsTransitGatewayAttachmentTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataHcpAwsTransitGatewayAttachmentTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpAwsTransitGatewayAttachmentTimeoutsOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataHcpAwsTransitGatewayAttachmentTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataHcpAwsTransitGatewayAttachmentTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataHcpAwsTransitGatewayAttachmentTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpAwsTransitGatewayAttachmentTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataHcpAwsTransitGatewayAttachment",
    "DataHcpAwsTransitGatewayAttachmentConfig",
    "DataHcpAwsTransitGatewayAttachmentTimeouts",
    "DataHcpAwsTransitGatewayAttachmentTimeoutsOutputReference",
]

publication.publish()
