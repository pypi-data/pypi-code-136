'''
# `google_vpc_access_connector`

Refer to the Terraform Registory for docs: [`google_vpc_access_connector`](https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector).
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


class GoogleVpcAccessConnector(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleVpcAccessConnector.GoogleVpcAccessConnector",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector google_vpc_access_connector}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        ip_cidr_range: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        max_instances: typing.Optional[jsii.Number] = None,
        max_throughput: typing.Optional[jsii.Number] = None,
        min_instances: typing.Optional[jsii.Number] = None,
        min_throughput: typing.Optional[jsii.Number] = None,
        network: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        subnet: typing.Optional[typing.Union["GoogleVpcAccessConnectorSubnet", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleVpcAccessConnectorTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector google_vpc_access_connector} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the resource (Max 25 characters). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#name GoogleVpcAccessConnector#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#id GoogleVpcAccessConnector#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_cidr_range: The range of internal addresses that follows RFC 4632 notation. Example: '10.132.0.0/28'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#ip_cidr_range GoogleVpcAccessConnector#ip_cidr_range}
        :param machine_type: Machine type of VM Instance underlying connector. Default is e2-micro. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#machine_type GoogleVpcAccessConnector#machine_type}
        :param max_instances: Maximum value of instances in autoscaling group underlying the connector. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#max_instances GoogleVpcAccessConnector#max_instances}
        :param max_throughput: Maximum throughput of the connector in Mbps, must be greater than 'min_throughput'. Default is 300. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#max_throughput GoogleVpcAccessConnector#max_throughput}
        :param min_instances: Minimum value of instances in autoscaling group underlying the connector. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#min_instances GoogleVpcAccessConnector#min_instances}
        :param min_throughput: Minimum throughput of the connector in Mbps. Default and min is 200. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#min_throughput GoogleVpcAccessConnector#min_throughput}
        :param network: Name or self_link of the VPC network. Required if 'ip_cidr_range' is set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#network GoogleVpcAccessConnector#network}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#project GoogleVpcAccessConnector#project}.
        :param region: Region where the VPC Access connector resides. If it is not provided, the provider region is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#region GoogleVpcAccessConnector#region}
        :param subnet: subnet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#subnet GoogleVpcAccessConnector#subnet}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#timeouts GoogleVpcAccessConnector#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleVpcAccessConnector.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleVpcAccessConnectorConfig(
            name=name,
            id=id,
            ip_cidr_range=ip_cidr_range,
            machine_type=machine_type,
            max_instances=max_instances,
            max_throughput=max_throughput,
            min_instances=min_instances,
            min_throughput=min_throughput,
            network=network,
            project=project,
            region=region,
            subnet=subnet,
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

    @jsii.member(jsii_name="putSubnet")
    def put_subnet(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Subnet name (relative, not fully qualified). E.g. if the full subnet selfLink is https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetName} the correct input for this field would be {subnetName}" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#name GoogleVpcAccessConnector#name}
        :param project_id: Project in which the subnet exists. If not set, this project is assumed to be the project for which the connector create request was issued. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#project_id GoogleVpcAccessConnector#project_id}
        '''
        value = GoogleVpcAccessConnectorSubnet(name=name, project_id=project_id)

        return typing.cast(None, jsii.invoke(self, "putSubnet", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#create GoogleVpcAccessConnector#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#delete GoogleVpcAccessConnector#delete}.
        '''
        value = GoogleVpcAccessConnectorTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpCidrRange")
    def reset_ip_cidr_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpCidrRange", []))

    @jsii.member(jsii_name="resetMachineType")
    def reset_machine_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineType", []))

    @jsii.member(jsii_name="resetMaxInstances")
    def reset_max_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxInstances", []))

    @jsii.member(jsii_name="resetMaxThroughput")
    def reset_max_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxThroughput", []))

    @jsii.member(jsii_name="resetMinInstances")
    def reset_min_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinInstances", []))

    @jsii.member(jsii_name="resetMinThroughput")
    def reset_min_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinThroughput", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetSubnet")
    def reset_subnet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnet", []))

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
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="subnet")
    def subnet(self) -> "GoogleVpcAccessConnectorSubnetOutputReference":
        return typing.cast("GoogleVpcAccessConnectorSubnetOutputReference", jsii.get(self, "subnet"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleVpcAccessConnectorTimeoutsOutputReference":
        return typing.cast("GoogleVpcAccessConnectorTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipCidrRangeInput")
    def ip_cidr_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipCidrRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxInstancesInput")
    def max_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="maxThroughputInput")
    def max_throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxThroughputInput"))

    @builtins.property
    @jsii.member(jsii_name="minInstancesInput")
    def min_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="minThroughputInput")
    def min_throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minThroughputInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetInput")
    def subnet_input(self) -> typing.Optional["GoogleVpcAccessConnectorSubnet"]:
        return typing.cast(typing.Optional["GoogleVpcAccessConnectorSubnet"], jsii.get(self, "subnetInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleVpcAccessConnectorTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleVpcAccessConnectorTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnector, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipCidrRange")
    def ip_cidr_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipCidrRange"))

    @ip_cidr_range.setter
    def ip_cidr_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnector, "ip_cidr_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipCidrRange", value)

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnector, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="maxInstances")
    def max_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxInstances"))

    @max_instances.setter
    def max_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnector, "max_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxInstances", value)

    @builtins.property
    @jsii.member(jsii_name="maxThroughput")
    def max_throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxThroughput"))

    @max_throughput.setter
    def max_throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnector, "max_throughput").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxThroughput", value)

    @builtins.property
    @jsii.member(jsii_name="minInstances")
    def min_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minInstances"))

    @min_instances.setter
    def min_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnector, "min_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minInstances", value)

    @builtins.property
    @jsii.member(jsii_name="minThroughput")
    def min_throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minThroughput"))

    @min_throughput.setter
    def min_throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnector, "min_throughput").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minThroughput", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnector, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnector, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnector, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnector, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleVpcAccessConnector.GoogleVpcAccessConnectorConfig",
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
        "id": "id",
        "ip_cidr_range": "ipCidrRange",
        "machine_type": "machineType",
        "max_instances": "maxInstances",
        "max_throughput": "maxThroughput",
        "min_instances": "minInstances",
        "min_throughput": "minThroughput",
        "network": "network",
        "project": "project",
        "region": "region",
        "subnet": "subnet",
        "timeouts": "timeouts",
    },
)
class GoogleVpcAccessConnectorConfig(cdktf.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
        ip_cidr_range: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        max_instances: typing.Optional[jsii.Number] = None,
        max_throughput: typing.Optional[jsii.Number] = None,
        min_instances: typing.Optional[jsii.Number] = None,
        min_throughput: typing.Optional[jsii.Number] = None,
        network: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        subnet: typing.Optional[typing.Union["GoogleVpcAccessConnectorSubnet", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleVpcAccessConnectorTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the resource (Max 25 characters). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#name GoogleVpcAccessConnector#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#id GoogleVpcAccessConnector#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_cidr_range: The range of internal addresses that follows RFC 4632 notation. Example: '10.132.0.0/28'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#ip_cidr_range GoogleVpcAccessConnector#ip_cidr_range}
        :param machine_type: Machine type of VM Instance underlying connector. Default is e2-micro. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#machine_type GoogleVpcAccessConnector#machine_type}
        :param max_instances: Maximum value of instances in autoscaling group underlying the connector. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#max_instances GoogleVpcAccessConnector#max_instances}
        :param max_throughput: Maximum throughput of the connector in Mbps, must be greater than 'min_throughput'. Default is 300. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#max_throughput GoogleVpcAccessConnector#max_throughput}
        :param min_instances: Minimum value of instances in autoscaling group underlying the connector. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#min_instances GoogleVpcAccessConnector#min_instances}
        :param min_throughput: Minimum throughput of the connector in Mbps. Default and min is 200. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#min_throughput GoogleVpcAccessConnector#min_throughput}
        :param network: Name or self_link of the VPC network. Required if 'ip_cidr_range' is set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#network GoogleVpcAccessConnector#network}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#project GoogleVpcAccessConnector#project}.
        :param region: Region where the VPC Access connector resides. If it is not provided, the provider region is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#region GoogleVpcAccessConnector#region}
        :param subnet: subnet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#subnet GoogleVpcAccessConnector#subnet}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#timeouts GoogleVpcAccessConnector#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(subnet, dict):
            subnet = GoogleVpcAccessConnectorSubnet(**subnet)
        if isinstance(timeouts, dict):
            timeouts = GoogleVpcAccessConnectorTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleVpcAccessConnectorConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_cidr_range", value=ip_cidr_range, expected_type=type_hints["ip_cidr_range"])
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            check_type(argname="argument max_instances", value=max_instances, expected_type=type_hints["max_instances"])
            check_type(argname="argument max_throughput", value=max_throughput, expected_type=type_hints["max_throughput"])
            check_type(argname="argument min_instances", value=min_instances, expected_type=type_hints["min_instances"])
            check_type(argname="argument min_throughput", value=min_throughput, expected_type=type_hints["min_throughput"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument subnet", value=subnet, expected_type=type_hints["subnet"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
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
        if id is not None:
            self._values["id"] = id
        if ip_cidr_range is not None:
            self._values["ip_cidr_range"] = ip_cidr_range
        if machine_type is not None:
            self._values["machine_type"] = machine_type
        if max_instances is not None:
            self._values["max_instances"] = max_instances
        if max_throughput is not None:
            self._values["max_throughput"] = max_throughput
        if min_instances is not None:
            self._values["min_instances"] = min_instances
        if min_throughput is not None:
            self._values["min_throughput"] = min_throughput
        if network is not None:
            self._values["network"] = network
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
        if subnet is not None:
            self._values["subnet"] = subnet
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
    def name(self) -> builtins.str:
        '''The name of the resource (Max 25 characters).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#name GoogleVpcAccessConnector#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#id GoogleVpcAccessConnector#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_cidr_range(self) -> typing.Optional[builtins.str]:
        '''The range of internal addresses that follows RFC 4632 notation. Example: '10.132.0.0/28'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#ip_cidr_range GoogleVpcAccessConnector#ip_cidr_range}
        '''
        result = self._values.get("ip_cidr_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def machine_type(self) -> typing.Optional[builtins.str]:
        '''Machine type of VM Instance underlying connector. Default is e2-micro.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#machine_type GoogleVpcAccessConnector#machine_type}
        '''
        result = self._values.get("machine_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_instances(self) -> typing.Optional[jsii.Number]:
        '''Maximum value of instances in autoscaling group underlying the connector.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#max_instances GoogleVpcAccessConnector#max_instances}
        '''
        result = self._values.get("max_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_throughput(self) -> typing.Optional[jsii.Number]:
        '''Maximum throughput of the connector in Mbps, must be greater than 'min_throughput'. Default is 300.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#max_throughput GoogleVpcAccessConnector#max_throughput}
        '''
        result = self._values.get("max_throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_instances(self) -> typing.Optional[jsii.Number]:
        '''Minimum value of instances in autoscaling group underlying the connector.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#min_instances GoogleVpcAccessConnector#min_instances}
        '''
        result = self._values.get("min_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_throughput(self) -> typing.Optional[jsii.Number]:
        '''Minimum throughput of the connector in Mbps. Default and min is 200.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#min_throughput GoogleVpcAccessConnector#min_throughput}
        '''
        result = self._values.get("min_throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''Name or self_link of the VPC network. Required if 'ip_cidr_range' is set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#network GoogleVpcAccessConnector#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#project GoogleVpcAccessConnector#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region where the VPC Access connector resides. If it is not provided, the provider region is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#region GoogleVpcAccessConnector#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet(self) -> typing.Optional["GoogleVpcAccessConnectorSubnet"]:
        '''subnet block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#subnet GoogleVpcAccessConnector#subnet}
        '''
        result = self._values.get("subnet")
        return typing.cast(typing.Optional["GoogleVpcAccessConnectorSubnet"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleVpcAccessConnectorTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#timeouts GoogleVpcAccessConnector#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleVpcAccessConnectorTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleVpcAccessConnectorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleVpcAccessConnector.GoogleVpcAccessConnectorSubnet",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "project_id": "projectId"},
)
class GoogleVpcAccessConnectorSubnet:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Subnet name (relative, not fully qualified). E.g. if the full subnet selfLink is https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetName} the correct input for this field would be {subnetName}" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#name GoogleVpcAccessConnector#name}
        :param project_id: Project in which the subnet exists. If not set, this project is assumed to be the project for which the connector create request was issued. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#project_id GoogleVpcAccessConnector#project_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleVpcAccessConnectorSubnet.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if project_id is not None:
            self._values["project_id"] = project_id

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Subnet name (relative, not fully qualified).

        E.g. if the full subnet selfLink is
        https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetName} the correct input for this field would be {subnetName}"

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#name GoogleVpcAccessConnector#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Project in which the subnet exists.

        If not set, this project is assumed to be the project for which the connector create request was issued.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#project_id GoogleVpcAccessConnector#project_id}
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleVpcAccessConnectorSubnet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleVpcAccessConnectorSubnetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleVpcAccessConnector.GoogleVpcAccessConnectorSubnetOutputReference",
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
            type_hints = typing.get_type_hints(GoogleVpcAccessConnectorSubnetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetProjectId")
    def reset_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectId", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnectorSubnetOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnectorSubnetOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleVpcAccessConnectorSubnet]:
        return typing.cast(typing.Optional[GoogleVpcAccessConnectorSubnet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleVpcAccessConnectorSubnet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnectorSubnetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleVpcAccessConnector.GoogleVpcAccessConnectorTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GoogleVpcAccessConnectorTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#create GoogleVpcAccessConnector#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#delete GoogleVpcAccessConnector#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleVpcAccessConnectorTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#create GoogleVpcAccessConnector#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vpc_access_connector#delete GoogleVpcAccessConnector#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleVpcAccessConnectorTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleVpcAccessConnectorTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleVpcAccessConnector.GoogleVpcAccessConnectorTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleVpcAccessConnectorTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnectorTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnectorTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleVpcAccessConnectorTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleVpcAccessConnectorTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleVpcAccessConnectorTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVpcAccessConnectorTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleVpcAccessConnector",
    "GoogleVpcAccessConnectorConfig",
    "GoogleVpcAccessConnectorSubnet",
    "GoogleVpcAccessConnectorSubnetOutputReference",
    "GoogleVpcAccessConnectorTimeouts",
    "GoogleVpcAccessConnectorTimeoutsOutputReference",
]

publication.publish()
