'''
# `databricks_mws_networks`

Refer to the Terraform Registory for docs: [`databricks_mws_networks`](https://www.terraform.io/docs/providers/databricks/r/mws_networks).
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


class MwsNetworks(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mwsNetworks.MwsNetworks",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks databricks_mws_networks}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        account_id: builtins.str,
        network_name: builtins.str,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        creation_time: typing.Optional[jsii.Number] = None,
        error_messages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MwsNetworksErrorMessages", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        network_id: typing.Optional[builtins.str] = None,
        vpc_endpoints: typing.Optional[typing.Union["MwsNetworksVpcEndpoints", typing.Dict[str, typing.Any]]] = None,
        vpc_status: typing.Optional[builtins.str] = None,
        workspace_id: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks databricks_mws_networks} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#account_id MwsNetworks#account_id}.
        :param network_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#network_name MwsNetworks#network_name}.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#security_group_ids MwsNetworks#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#subnet_ids MwsNetworks#subnet_ids}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_id MwsNetworks#vpc_id}.
        :param creation_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#creation_time MwsNetworks#creation_time}.
        :param error_messages: error_messages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#error_messages MwsNetworks#error_messages}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#id MwsNetworks#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#network_id MwsNetworks#network_id}.
        :param vpc_endpoints: vpc_endpoints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_endpoints MwsNetworks#vpc_endpoints}
        :param vpc_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_status MwsNetworks#vpc_status}.
        :param workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#workspace_id MwsNetworks#workspace_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MwsNetworks.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MwsNetworksConfig(
            account_id=account_id,
            network_name=network_name,
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
            vpc_id=vpc_id,
            creation_time=creation_time,
            error_messages=error_messages,
            id=id,
            network_id=network_id,
            vpc_endpoints=vpc_endpoints,
            vpc_status=vpc_status,
            workspace_id=workspace_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putErrorMessages")
    def put_error_messages(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MwsNetworksErrorMessages", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MwsNetworks.put_error_messages)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putErrorMessages", [value]))

    @jsii.member(jsii_name="putVpcEndpoints")
    def put_vpc_endpoints(
        self,
        *,
        dataplane_relay: typing.Sequence[builtins.str],
        rest_api: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param dataplane_relay: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#dataplane_relay MwsNetworks#dataplane_relay}.
        :param rest_api: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#rest_api MwsNetworks#rest_api}.
        '''
        value = MwsNetworksVpcEndpoints(
            dataplane_relay=dataplane_relay, rest_api=rest_api
        )

        return typing.cast(None, jsii.invoke(self, "putVpcEndpoints", [value]))

    @jsii.member(jsii_name="resetCreationTime")
    def reset_creation_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreationTime", []))

    @jsii.member(jsii_name="resetErrorMessages")
    def reset_error_messages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorMessages", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNetworkId")
    def reset_network_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkId", []))

    @jsii.member(jsii_name="resetVpcEndpoints")
    def reset_vpc_endpoints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcEndpoints", []))

    @jsii.member(jsii_name="resetVpcStatus")
    def reset_vpc_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcStatus", []))

    @jsii.member(jsii_name="resetWorkspaceId")
    def reset_workspace_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="errorMessages")
    def error_messages(self) -> "MwsNetworksErrorMessagesList":
        return typing.cast("MwsNetworksErrorMessagesList", jsii.get(self, "errorMessages"))

    @builtins.property
    @jsii.member(jsii_name="vpcEndpoints")
    def vpc_endpoints(self) -> "MwsNetworksVpcEndpointsOutputReference":
        return typing.cast("MwsNetworksVpcEndpointsOutputReference", jsii.get(self, "vpcEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="creationTimeInput")
    def creation_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "creationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="errorMessagesInput")
    def error_messages_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MwsNetworksErrorMessages"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MwsNetworksErrorMessages"]]], jsii.get(self, "errorMessagesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="networkIdInput")
    def network_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="networkNameInput")
    def network_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkNameInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointsInput")
    def vpc_endpoints_input(self) -> typing.Optional["MwsNetworksVpcEndpoints"]:
        return typing.cast(typing.Optional["MwsNetworksVpcEndpoints"], jsii.get(self, "vpcEndpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIdInput")
    def vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcStatusInput")
    def vpc_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceIdInput")
    def workspace_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "workspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworks, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "creationTime"))

    @creation_time.setter
    def creation_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworks, "creation_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creationTime", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworks, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="networkId")
    def network_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkId"))

    @network_id.setter
    def network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworks, "network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkId", value)

    @builtins.property
    @jsii.member(jsii_name="networkName")
    def network_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkName"))

    @network_name.setter
    def network_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworks, "network_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkName", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworks, "security_group_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworks, "subnet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworks, "vpc_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="vpcStatus")
    def vpc_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcStatus"))

    @vpc_status.setter
    def vpc_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworks, "vpc_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcStatus", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceId")
    def workspace_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "workspaceId"))

    @workspace_id.setter
    def workspace_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworks, "workspace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mwsNetworks.MwsNetworksConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_id": "accountId",
        "network_name": "networkName",
        "security_group_ids": "securityGroupIds",
        "subnet_ids": "subnetIds",
        "vpc_id": "vpcId",
        "creation_time": "creationTime",
        "error_messages": "errorMessages",
        "id": "id",
        "network_id": "networkId",
        "vpc_endpoints": "vpcEndpoints",
        "vpc_status": "vpcStatus",
        "workspace_id": "workspaceId",
    },
)
class MwsNetworksConfig(cdktf.TerraformMetaArguments):
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
        account_id: builtins.str,
        network_name: builtins.str,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        creation_time: typing.Optional[jsii.Number] = None,
        error_messages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MwsNetworksErrorMessages", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        network_id: typing.Optional[builtins.str] = None,
        vpc_endpoints: typing.Optional[typing.Union["MwsNetworksVpcEndpoints", typing.Dict[str, typing.Any]]] = None,
        vpc_status: typing.Optional[builtins.str] = None,
        workspace_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#account_id MwsNetworks#account_id}.
        :param network_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#network_name MwsNetworks#network_name}.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#security_group_ids MwsNetworks#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#subnet_ids MwsNetworks#subnet_ids}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_id MwsNetworks#vpc_id}.
        :param creation_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#creation_time MwsNetworks#creation_time}.
        :param error_messages: error_messages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#error_messages MwsNetworks#error_messages}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#id MwsNetworks#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#network_id MwsNetworks#network_id}.
        :param vpc_endpoints: vpc_endpoints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_endpoints MwsNetworks#vpc_endpoints}
        :param vpc_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_status MwsNetworks#vpc_status}.
        :param workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#workspace_id MwsNetworks#workspace_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(vpc_endpoints, dict):
            vpc_endpoints = MwsNetworksVpcEndpoints(**vpc_endpoints)
        if __debug__:
            type_hints = typing.get_type_hints(MwsNetworksConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument network_name", value=network_name, expected_type=type_hints["network_name"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument creation_time", value=creation_time, expected_type=type_hints["creation_time"])
            check_type(argname="argument error_messages", value=error_messages, expected_type=type_hints["error_messages"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument network_id", value=network_id, expected_type=type_hints["network_id"])
            check_type(argname="argument vpc_endpoints", value=vpc_endpoints, expected_type=type_hints["vpc_endpoints"])
            check_type(argname="argument vpc_status", value=vpc_status, expected_type=type_hints["vpc_status"])
            check_type(argname="argument workspace_id", value=workspace_id, expected_type=type_hints["workspace_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
            "network_name": network_name,
            "security_group_ids": security_group_ids,
            "subnet_ids": subnet_ids,
            "vpc_id": vpc_id,
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
        if creation_time is not None:
            self._values["creation_time"] = creation_time
        if error_messages is not None:
            self._values["error_messages"] = error_messages
        if id is not None:
            self._values["id"] = id
        if network_id is not None:
            self._values["network_id"] = network_id
        if vpc_endpoints is not None:
            self._values["vpc_endpoints"] = vpc_endpoints
        if vpc_status is not None:
            self._values["vpc_status"] = vpc_status
        if workspace_id is not None:
            self._values["workspace_id"] = workspace_id

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
    def account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#account_id MwsNetworks#account_id}.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#network_name MwsNetworks#network_name}.'''
        result = self._values.get("network_name")
        assert result is not None, "Required property 'network_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#security_group_ids MwsNetworks#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#subnet_ids MwsNetworks#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_id MwsNetworks#vpc_id}.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def creation_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#creation_time MwsNetworks#creation_time}.'''
        result = self._values.get("creation_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def error_messages(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MwsNetworksErrorMessages"]]]:
        '''error_messages block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#error_messages MwsNetworks#error_messages}
        '''
        result = self._values.get("error_messages")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MwsNetworksErrorMessages"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#id MwsNetworks#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#network_id MwsNetworks#network_id}.'''
        result = self._values.get("network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_endpoints(self) -> typing.Optional["MwsNetworksVpcEndpoints"]:
        '''vpc_endpoints block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_endpoints MwsNetworks#vpc_endpoints}
        '''
        result = self._values.get("vpc_endpoints")
        return typing.cast(typing.Optional["MwsNetworksVpcEndpoints"], result)

    @builtins.property
    def vpc_status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_status MwsNetworks#vpc_status}.'''
        result = self._values.get("vpc_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspace_id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#workspace_id MwsNetworks#workspace_id}.'''
        result = self._values.get("workspace_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsNetworksConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mwsNetworks.MwsNetworksErrorMessages",
    jsii_struct_bases=[],
    name_mapping={"error_message": "errorMessage", "error_type": "errorType"},
)
class MwsNetworksErrorMessages:
    def __init__(
        self,
        *,
        error_message: typing.Optional[builtins.str] = None,
        error_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param error_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#error_message MwsNetworks#error_message}.
        :param error_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#error_type MwsNetworks#error_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MwsNetworksErrorMessages.__init__)
            check_type(argname="argument error_message", value=error_message, expected_type=type_hints["error_message"])
            check_type(argname="argument error_type", value=error_type, expected_type=type_hints["error_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if error_message is not None:
            self._values["error_message"] = error_message
        if error_type is not None:
            self._values["error_type"] = error_type

    @builtins.property
    def error_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#error_message MwsNetworks#error_message}.'''
        result = self._values.get("error_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#error_type MwsNetworks#error_type}.'''
        result = self._values.get("error_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsNetworksErrorMessages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsNetworksErrorMessagesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mwsNetworks.MwsNetworksErrorMessagesList",
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
            type_hints = typing.get_type_hints(MwsNetworksErrorMessagesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MwsNetworksErrorMessagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MwsNetworksErrorMessagesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MwsNetworksErrorMessagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworksErrorMessagesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MwsNetworksErrorMessagesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MwsNetworksErrorMessagesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MwsNetworksErrorMessages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MwsNetworksErrorMessages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MwsNetworksErrorMessages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworksErrorMessagesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MwsNetworksErrorMessagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mwsNetworks.MwsNetworksErrorMessagesOutputReference",
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
            type_hints = typing.get_type_hints(MwsNetworksErrorMessagesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetErrorMessage")
    def reset_error_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorMessage", []))

    @jsii.member(jsii_name="resetErrorType")
    def reset_error_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorType", []))

    @builtins.property
    @jsii.member(jsii_name="errorMessageInput")
    def error_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="errorTypeInput")
    def error_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="errorMessage")
    def error_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorMessage"))

    @error_message.setter
    def error_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworksErrorMessagesOutputReference, "error_message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorMessage", value)

    @builtins.property
    @jsii.member(jsii_name="errorType")
    def error_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorType"))

    @error_type.setter
    def error_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworksErrorMessagesOutputReference, "error_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MwsNetworksErrorMessages, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MwsNetworksErrorMessages, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MwsNetworksErrorMessages, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworksErrorMessagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mwsNetworks.MwsNetworksVpcEndpoints",
    jsii_struct_bases=[],
    name_mapping={"dataplane_relay": "dataplaneRelay", "rest_api": "restApi"},
)
class MwsNetworksVpcEndpoints:
    def __init__(
        self,
        *,
        dataplane_relay: typing.Sequence[builtins.str],
        rest_api: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param dataplane_relay: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#dataplane_relay MwsNetworks#dataplane_relay}.
        :param rest_api: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#rest_api MwsNetworks#rest_api}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MwsNetworksVpcEndpoints.__init__)
            check_type(argname="argument dataplane_relay", value=dataplane_relay, expected_type=type_hints["dataplane_relay"])
            check_type(argname="argument rest_api", value=rest_api, expected_type=type_hints["rest_api"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataplane_relay": dataplane_relay,
            "rest_api": rest_api,
        }

    @builtins.property
    def dataplane_relay(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#dataplane_relay MwsNetworks#dataplane_relay}.'''
        result = self._values.get("dataplane_relay")
        assert result is not None, "Required property 'dataplane_relay' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def rest_api(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#rest_api MwsNetworks#rest_api}.'''
        result = self._values.get("rest_api")
        assert result is not None, "Required property 'rest_api' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsNetworksVpcEndpoints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsNetworksVpcEndpointsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mwsNetworks.MwsNetworksVpcEndpointsOutputReference",
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
            type_hints = typing.get_type_hints(MwsNetworksVpcEndpointsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dataplaneRelayInput")
    def dataplane_relay_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dataplaneRelayInput"))

    @builtins.property
    @jsii.member(jsii_name="restApiInput")
    def rest_api_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "restApiInput"))

    @builtins.property
    @jsii.member(jsii_name="dataplaneRelay")
    def dataplane_relay(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dataplaneRelay"))

    @dataplane_relay.setter
    def dataplane_relay(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworksVpcEndpointsOutputReference, "dataplane_relay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataplaneRelay", value)

    @builtins.property
    @jsii.member(jsii_name="restApi")
    def rest_api(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "restApi"))

    @rest_api.setter
    def rest_api(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworksVpcEndpointsOutputReference, "rest_api").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restApi", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsNetworksVpcEndpoints]:
        return typing.cast(typing.Optional[MwsNetworksVpcEndpoints], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MwsNetworksVpcEndpoints]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsNetworksVpcEndpointsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MwsNetworks",
    "MwsNetworksConfig",
    "MwsNetworksErrorMessages",
    "MwsNetworksErrorMessagesList",
    "MwsNetworksErrorMessagesOutputReference",
    "MwsNetworksVpcEndpoints",
    "MwsNetworksVpcEndpointsOutputReference",
]

publication.publish()
