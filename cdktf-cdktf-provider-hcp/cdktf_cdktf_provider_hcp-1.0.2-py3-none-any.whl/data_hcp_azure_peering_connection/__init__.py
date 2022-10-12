'''
# `data_hcp_azure_peering_connection`

Refer to the Terraform Registory for docs: [`data_hcp_azure_peering_connection`](https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection).
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


class DataHcpAzurePeeringConnection(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.dataHcpAzurePeeringConnection.DataHcpAzurePeeringConnection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection hcp_azure_peering_connection}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        hvn_link: builtins.str,
        peering_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataHcpAzurePeeringConnectionTimeouts", typing.Dict[str, typing.Any]]] = None,
        wait_for_active_state: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection hcp_azure_peering_connection} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param hvn_link: The ``self_link`` of the HashiCorp Virtual Network (HVN). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#hvn_link DataHcpAzurePeeringConnection#hvn_link}
        :param peering_id: The ID of the peering connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#peering_id DataHcpAzurePeeringConnection#peering_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#id DataHcpAzurePeeringConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#timeouts DataHcpAzurePeeringConnection#timeouts}
        :param wait_for_active_state: If ``true``, Terraform will wait for the peering connection to reach an ``ACTIVE`` state before continuing. Default ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#wait_for_active_state DataHcpAzurePeeringConnection#wait_for_active_state}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpAzurePeeringConnection.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataHcpAzurePeeringConnectionConfig(
            hvn_link=hvn_link,
            peering_id=peering_id,
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
    def put_timeouts(self, *, read: typing.Optional[builtins.str] = None) -> None:
        '''
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#read DataHcpAzurePeeringConnection#read}.
        '''
        value = DataHcpAzurePeeringConnectionTimeouts(read=read)

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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @builtins.property
    @jsii.member(jsii_name="azurePeeringId")
    def azure_peering_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azurePeeringId"))

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
    @jsii.member(jsii_name="peerResourceGroupName")
    def peer_resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerResourceGroupName"))

    @builtins.property
    @jsii.member(jsii_name="peerSubscriptionId")
    def peer_subscription_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerSubscriptionId"))

    @builtins.property
    @jsii.member(jsii_name="peerTenantId")
    def peer_tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerTenantId"))

    @builtins.property
    @jsii.member(jsii_name="peerVnetName")
    def peer_vnet_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerVnetName"))

    @builtins.property
    @jsii.member(jsii_name="peerVnetRegion")
    def peer_vnet_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerVnetRegion"))

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

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
    def timeouts(self) -> "DataHcpAzurePeeringConnectionTimeoutsOutputReference":
        return typing.cast("DataHcpAzurePeeringConnectionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="hvnLinkInput")
    def hvn_link_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hvnLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="peeringIdInput")
    def peering_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peeringIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataHcpAzurePeeringConnectionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataHcpAzurePeeringConnectionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForActiveStateInput")
    def wait_for_active_state_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "waitForActiveStateInput"))

    @builtins.property
    @jsii.member(jsii_name="hvnLink")
    def hvn_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hvnLink"))

    @hvn_link.setter
    def hvn_link(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpAzurePeeringConnection, "hvn_link").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hvnLink", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpAzurePeeringConnection, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="peeringId")
    def peering_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peeringId"))

    @peering_id.setter
    def peering_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpAzurePeeringConnection, "peering_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peeringId", value)

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
            type_hints = typing.get_type_hints(getattr(DataHcpAzurePeeringConnection, "wait_for_active_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForActiveState", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.dataHcpAzurePeeringConnection.DataHcpAzurePeeringConnectionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "hvn_link": "hvnLink",
        "peering_id": "peeringId",
        "id": "id",
        "timeouts": "timeouts",
        "wait_for_active_state": "waitForActiveState",
    },
)
class DataHcpAzurePeeringConnectionConfig(cdktf.TerraformMetaArguments):
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
        hvn_link: builtins.str,
        peering_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataHcpAzurePeeringConnectionTimeouts", typing.Dict[str, typing.Any]]] = None,
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
        :param hvn_link: The ``self_link`` of the HashiCorp Virtual Network (HVN). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#hvn_link DataHcpAzurePeeringConnection#hvn_link}
        :param peering_id: The ID of the peering connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#peering_id DataHcpAzurePeeringConnection#peering_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#id DataHcpAzurePeeringConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#timeouts DataHcpAzurePeeringConnection#timeouts}
        :param wait_for_active_state: If ``true``, Terraform will wait for the peering connection to reach an ``ACTIVE`` state before continuing. Default ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#wait_for_active_state DataHcpAzurePeeringConnection#wait_for_active_state}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DataHcpAzurePeeringConnectionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpAzurePeeringConnectionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument hvn_link", value=hvn_link, expected_type=type_hints["hvn_link"])
            check_type(argname="argument peering_id", value=peering_id, expected_type=type_hints["peering_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument wait_for_active_state", value=wait_for_active_state, expected_type=type_hints["wait_for_active_state"])
        self._values: typing.Dict[str, typing.Any] = {
            "hvn_link": hvn_link,
            "peering_id": peering_id,
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
    def hvn_link(self) -> builtins.str:
        '''The ``self_link`` of the HashiCorp Virtual Network (HVN).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#hvn_link DataHcpAzurePeeringConnection#hvn_link}
        '''
        result = self._values.get("hvn_link")
        assert result is not None, "Required property 'hvn_link' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def peering_id(self) -> builtins.str:
        '''The ID of the peering connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#peering_id DataHcpAzurePeeringConnection#peering_id}
        '''
        result = self._values.get("peering_id")
        assert result is not None, "Required property 'peering_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#id DataHcpAzurePeeringConnection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataHcpAzurePeeringConnectionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#timeouts DataHcpAzurePeeringConnection#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataHcpAzurePeeringConnectionTimeouts"], result)

    @builtins.property
    def wait_for_active_state(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true``, Terraform will wait for the peering connection to reach an ``ACTIVE`` state before continuing. Default ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#wait_for_active_state DataHcpAzurePeeringConnection#wait_for_active_state}
        '''
        result = self._values.get("wait_for_active_state")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataHcpAzurePeeringConnectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.dataHcpAzurePeeringConnection.DataHcpAzurePeeringConnectionTimeouts",
    jsii_struct_bases=[],
    name_mapping={"read": "read"},
)
class DataHcpAzurePeeringConnectionTimeouts:
    def __init__(self, *, read: typing.Optional[builtins.str] = None) -> None:
        '''
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#read DataHcpAzurePeeringConnection#read}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataHcpAzurePeeringConnectionTimeouts.__init__)
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
        self._values: typing.Dict[str, typing.Any] = {}
        if read is not None:
            self._values["read"] = read

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/d/azure_peering_connection#read DataHcpAzurePeeringConnection#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataHcpAzurePeeringConnectionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataHcpAzurePeeringConnectionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.dataHcpAzurePeeringConnection.DataHcpAzurePeeringConnectionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataHcpAzurePeeringConnectionTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpAzurePeeringConnectionTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataHcpAzurePeeringConnectionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataHcpAzurePeeringConnectionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataHcpAzurePeeringConnectionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataHcpAzurePeeringConnectionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataHcpAzurePeeringConnection",
    "DataHcpAzurePeeringConnectionConfig",
    "DataHcpAzurePeeringConnectionTimeouts",
    "DataHcpAzurePeeringConnectionTimeoutsOutputReference",
]

publication.publish()
