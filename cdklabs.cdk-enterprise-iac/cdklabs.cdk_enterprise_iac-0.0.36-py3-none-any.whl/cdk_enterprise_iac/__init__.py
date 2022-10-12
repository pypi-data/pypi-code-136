'''
<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: Apache-2.0
-->

# CDK Enterprise IaC

Utilities for using CDK within enterprise constraints

## Install

Typescript

```zsh
npm install @cdklabs/cdk-enterprise-iac
```

Python

```zsh
pip install cdklabs.cdk-enterprise-iac
```

## Usage

Example for `AddPermissionBoundary` in Typescript project.

```python
import * as cdk from 'aws-cdk-lib';
import { MyStack } from '../lib/my-project-stack';
import { Aspects } from 'aws-cdk-lib';
import { AddPermissionBoundary } from '@cdklabs/cdk-enterprise-iac';

const app = new cdk.App();
new MyStack(app, 'MyStack');

Aspects.of(app).add(
  new AddPermissionBoundary({
    permissionsBoundaryPolicyName: 'MyPermissionBoundaryName',
    instanceProfilePrefix: 'MY_PREFIX_', // optional, Defaults to ''
    policyPrefix: 'MY_POLICY_PREFIX_', // optional, Defaults to ''
    rolePrefix: 'MY_ROLE_PREFIX_', // optional, Defaults to ''
  })
);
```

Example for `AddPermissionBoundary` in Python project.

```python
import aws_cdk as cdk
from cdklabs.cdk_enterprise_iac import AddPermissionBoundary
from test_py.test_py_stack import TestPyStack


app = cdk.App()
TestPyStack(app, "TestPyStack")

cdk.Aspects.of(app).add(AddPermissionBoundary(
    permissions_boundary_policy_name="MyPermissionBoundaryName",
    instance_profile_prefix="MY_PREFIX_",  # optional, Defaults to ""
    policy_prefix="MY_POLICY_PREFIX_",  # optional, Defaults to ""
    role_prefix="MY_ROLE_PREFIX_"  # optional, Defaults to ""
))

app.synth()
```

Details in [API.md](API.md)
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

from ._jsii import *

import aws_cdk
import aws_cdk.aws_apigateway
import aws_cdk.aws_cloudwatch
import aws_cdk.aws_ec2
import aws_cdk.aws_ecs
import aws_cdk.aws_iam
import constructs


@jsii.implements(aws_cdk.IAspect)
class AddLambdaEnvironmentVariables(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-enterprise-iac.AddLambdaEnvironmentVariables",
):
    '''Add one or more environment variables to *all* lambda functions within a scope.

    :extends: IAspect
    '''

    def __init__(self, props: typing.Mapping[builtins.str, builtins.str]) -> None:
        '''
        :param props: : string} props - Key Value pair(s) for environment variables to add to all lambda functions.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AddLambdaEnvironmentVariables.__init__)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, node: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AddLambdaEnvironmentVariables.visit)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


@jsii.implements(aws_cdk.IAspect)
class AddPermissionBoundary(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-enterprise-iac.AddPermissionBoundary",
):
    '''A patch for Adding Permissions Boundaries to all IAM roles.

    Additional options for adding prefixes to IAM role, policy and instance profile names

    Can account for non commercial partitions (e.g. aws-gov, aws-cn)
    '''

    def __init__(
        self,
        *,
        permissions_boundary_policy_name: builtins.str,
        instance_profile_prefix: typing.Optional[builtins.str] = None,
        policy_prefix: typing.Optional[builtins.str] = None,
        role_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param permissions_boundary_policy_name: Name of Permissions Boundary Policy to add to all IAM roles.
        :param instance_profile_prefix: A prefix to prepend to the name of the IAM InstanceProfiles (Default: '').
        :param policy_prefix: A prefix to prepend to the name of the IAM Policies and ManagedPolicies (Default: '').
        :param role_prefix: A prefix to prepend to the name of IAM Roles (Default: '').
        '''
        props = AddPermissionBoundaryProps(
            permissions_boundary_policy_name=permissions_boundary_policy_name,
            instance_profile_prefix=instance_profile_prefix,
            policy_prefix=policy_prefix,
            role_prefix=role_prefix,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="checkAndOverride")
    def check_and_override(
        self,
        node: aws_cdk.CfnResource,
        prefix: builtins.str,
        length: jsii.Number,
        cfn_prop: builtins.str,
        cdk_prop: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param node: -
        :param prefix: -
        :param length: -
        :param cfn_prop: -
        :param cdk_prop: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AddPermissionBoundary.check_and_override)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument length", value=length, expected_type=type_hints["length"])
            check_type(argname="argument cfn_prop", value=cfn_prop, expected_type=type_hints["cfn_prop"])
            check_type(argname="argument cdk_prop", value=cdk_prop, expected_type=type_hints["cdk_prop"])
        return typing.cast(None, jsii.invoke(self, "checkAndOverride", [node, prefix, length, cfn_prop, cdk_prop]))

    @jsii.member(jsii_name="visit")
    def visit(self, node: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AddPermissionBoundary.visit)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


@jsii.data_type(
    jsii_type="@cdklabs/cdk-enterprise-iac.AddPermissionBoundaryProps",
    jsii_struct_bases=[],
    name_mapping={
        "permissions_boundary_policy_name": "permissionsBoundaryPolicyName",
        "instance_profile_prefix": "instanceProfilePrefix",
        "policy_prefix": "policyPrefix",
        "role_prefix": "rolePrefix",
    },
)
class AddPermissionBoundaryProps:
    def __init__(
        self,
        *,
        permissions_boundary_policy_name: builtins.str,
        instance_profile_prefix: typing.Optional[builtins.str] = None,
        policy_prefix: typing.Optional[builtins.str] = None,
        role_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties to pass to the AddPermissionBoundary.

        :param permissions_boundary_policy_name: Name of Permissions Boundary Policy to add to all IAM roles.
        :param instance_profile_prefix: A prefix to prepend to the name of the IAM InstanceProfiles (Default: '').
        :param policy_prefix: A prefix to prepend to the name of the IAM Policies and ManagedPolicies (Default: '').
        :param role_prefix: A prefix to prepend to the name of IAM Roles (Default: '').

        :interface: AddPermissionBoundaryProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AddPermissionBoundaryProps.__init__)
            check_type(argname="argument permissions_boundary_policy_name", value=permissions_boundary_policy_name, expected_type=type_hints["permissions_boundary_policy_name"])
            check_type(argname="argument instance_profile_prefix", value=instance_profile_prefix, expected_type=type_hints["instance_profile_prefix"])
            check_type(argname="argument policy_prefix", value=policy_prefix, expected_type=type_hints["policy_prefix"])
            check_type(argname="argument role_prefix", value=role_prefix, expected_type=type_hints["role_prefix"])
        self._values: typing.Dict[str, typing.Any] = {
            "permissions_boundary_policy_name": permissions_boundary_policy_name,
        }
        if instance_profile_prefix is not None:
            self._values["instance_profile_prefix"] = instance_profile_prefix
        if policy_prefix is not None:
            self._values["policy_prefix"] = policy_prefix
        if role_prefix is not None:
            self._values["role_prefix"] = role_prefix

    @builtins.property
    def permissions_boundary_policy_name(self) -> builtins.str:
        '''Name of Permissions Boundary Policy to add to all IAM roles.'''
        result = self._values.get("permissions_boundary_policy_name")
        assert result is not None, "Required property 'permissions_boundary_policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_profile_prefix(self) -> typing.Optional[builtins.str]:
        '''A prefix to prepend to the name of the IAM InstanceProfiles (Default: '').'''
        result = self._values.get("instance_profile_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_prefix(self) -> typing.Optional[builtins.str]:
        '''A prefix to prepend to the name of the IAM Policies and ManagedPolicies (Default: '').'''
        result = self._values.get("policy_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_prefix(self) -> typing.Optional[builtins.str]:
        '''A prefix to prepend to the name of IAM Roles (Default: '').'''
        result = self._values.get("role_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddPermissionBoundaryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsIsoServiceAutoscaler(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-enterprise-iac.EcsIsoServiceAutoscaler",
):
    '''Creates a EcsIsoServiceAutoscaler construct.

    This construct allows you to scale an ECS service in an ISO
    region where classic ECS Autoscaling may not be available.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        ecs_cluster: aws_cdk.aws_ecs.Cluster,
        ecs_service: aws_cdk.aws_ecs.IService,
        role: aws_cdk.aws_iam.IRole,
        scale_alarm: aws_cdk.aws_cloudwatch.Alarm,
        maximum_task_count: typing.Optional[jsii.Number] = None,
        minimum_task_count: typing.Optional[jsii.Number] = None,
        scale_in_cooldown: typing.Optional[aws_cdk.Duration] = None,
        scale_in_increment: typing.Optional[jsii.Number] = None,
        scale_out_cooldown: typing.Optional[aws_cdk.Duration] = None,
        scale_out_increment: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ecs_cluster: The cluster the service you wish to scale resides in.
        :param ecs_service: The ECS service you wish to scale.
        :param role: The IAM role that allows the created lambda to adjust the desired count on the ECS Service . TODO: Make optional and add function for auto generation
        :param scale_alarm: The Cloudwatch Alarm that will cause scaling actions to be invoked, whether it's in or not in alarm will determine scale up and down actions.
        :param maximum_task_count: The maximum number of tasks that the service will scale out to. Note: This does not provide any protection from scaling out above the maximum allowed in your account, set this variable and manage account quotas appropriately. Default: 10
        :param minimum_task_count: The minimum number of tasks the service will have. Default: 1
        :param scale_in_cooldown: How long will the application wait before performing another scale in action. Default: 60 seconds
        :param scale_in_increment: The number of tasks that will scale in on scale in alarm status. Default: 1
        :param scale_out_cooldown: How long will a the application wait before performing another scale out action. Default: 60 seconds
        :param scale_out_increment: The number of tasks that will scale out on scale out alarm status. Default: 1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsIsoServiceAutoscaler.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EcsIsoServiceAutoscalerProps(
            ecs_cluster=ecs_cluster,
            ecs_service=ecs_service,
            role=role,
            scale_alarm=scale_alarm,
            maximum_task_count=maximum_task_count,
            minimum_task_count=minimum_task_count,
            scale_in_cooldown=scale_in_cooldown,
            scale_in_increment=scale_in_increment,
            scale_out_cooldown=scale_out_cooldown,
            scale_out_increment=scale_out_increment,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cdklabs/cdk-enterprise-iac.EcsIsoServiceAutoscalerProps",
    jsii_struct_bases=[],
    name_mapping={
        "ecs_cluster": "ecsCluster",
        "ecs_service": "ecsService",
        "role": "role",
        "scale_alarm": "scaleAlarm",
        "maximum_task_count": "maximumTaskCount",
        "minimum_task_count": "minimumTaskCount",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_in_increment": "scaleInIncrement",
        "scale_out_cooldown": "scaleOutCooldown",
        "scale_out_increment": "scaleOutIncrement",
    },
)
class EcsIsoServiceAutoscalerProps:
    def __init__(
        self,
        *,
        ecs_cluster: aws_cdk.aws_ecs.Cluster,
        ecs_service: aws_cdk.aws_ecs.IService,
        role: aws_cdk.aws_iam.IRole,
        scale_alarm: aws_cdk.aws_cloudwatch.Alarm,
        maximum_task_count: typing.Optional[jsii.Number] = None,
        minimum_task_count: typing.Optional[jsii.Number] = None,
        scale_in_cooldown: typing.Optional[aws_cdk.Duration] = None,
        scale_in_increment: typing.Optional[jsii.Number] = None,
        scale_out_cooldown: typing.Optional[aws_cdk.Duration] = None,
        scale_out_increment: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param ecs_cluster: The cluster the service you wish to scale resides in.
        :param ecs_service: The ECS service you wish to scale.
        :param role: The IAM role that allows the created lambda to adjust the desired count on the ECS Service . TODO: Make optional and add function for auto generation
        :param scale_alarm: The Cloudwatch Alarm that will cause scaling actions to be invoked, whether it's in or not in alarm will determine scale up and down actions.
        :param maximum_task_count: The maximum number of tasks that the service will scale out to. Note: This does not provide any protection from scaling out above the maximum allowed in your account, set this variable and manage account quotas appropriately. Default: 10
        :param minimum_task_count: The minimum number of tasks the service will have. Default: 1
        :param scale_in_cooldown: How long will the application wait before performing another scale in action. Default: 60 seconds
        :param scale_in_increment: The number of tasks that will scale in on scale in alarm status. Default: 1
        :param scale_out_cooldown: How long will a the application wait before performing another scale out action. Default: 60 seconds
        :param scale_out_increment: The number of tasks that will scale out on scale out alarm status. Default: 1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsIsoServiceAutoscalerProps.__init__)
            check_type(argname="argument ecs_cluster", value=ecs_cluster, expected_type=type_hints["ecs_cluster"])
            check_type(argname="argument ecs_service", value=ecs_service, expected_type=type_hints["ecs_service"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument scale_alarm", value=scale_alarm, expected_type=type_hints["scale_alarm"])
            check_type(argname="argument maximum_task_count", value=maximum_task_count, expected_type=type_hints["maximum_task_count"])
            check_type(argname="argument minimum_task_count", value=minimum_task_count, expected_type=type_hints["minimum_task_count"])
            check_type(argname="argument scale_in_cooldown", value=scale_in_cooldown, expected_type=type_hints["scale_in_cooldown"])
            check_type(argname="argument scale_in_increment", value=scale_in_increment, expected_type=type_hints["scale_in_increment"])
            check_type(argname="argument scale_out_cooldown", value=scale_out_cooldown, expected_type=type_hints["scale_out_cooldown"])
            check_type(argname="argument scale_out_increment", value=scale_out_increment, expected_type=type_hints["scale_out_increment"])
        self._values: typing.Dict[str, typing.Any] = {
            "ecs_cluster": ecs_cluster,
            "ecs_service": ecs_service,
            "role": role,
            "scale_alarm": scale_alarm,
        }
        if maximum_task_count is not None:
            self._values["maximum_task_count"] = maximum_task_count
        if minimum_task_count is not None:
            self._values["minimum_task_count"] = minimum_task_count
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_in_increment is not None:
            self._values["scale_in_increment"] = scale_in_increment
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown
        if scale_out_increment is not None:
            self._values["scale_out_increment"] = scale_out_increment

    @builtins.property
    def ecs_cluster(self) -> aws_cdk.aws_ecs.Cluster:
        '''The cluster the service you wish to scale resides in.'''
        result = self._values.get("ecs_cluster")
        assert result is not None, "Required property 'ecs_cluster' is missing"
        return typing.cast(aws_cdk.aws_ecs.Cluster, result)

    @builtins.property
    def ecs_service(self) -> aws_cdk.aws_ecs.IService:
        '''The ECS service you wish to scale.'''
        result = self._values.get("ecs_service")
        assert result is not None, "Required property 'ecs_service' is missing"
        return typing.cast(aws_cdk.aws_ecs.IService, result)

    @builtins.property
    def role(self) -> aws_cdk.aws_iam.IRole:
        '''The IAM role that allows the created lambda to adjust the desired count on the ECS Service .

        TODO: Make optional and add function for auto generation
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(aws_cdk.aws_iam.IRole, result)

    @builtins.property
    def scale_alarm(self) -> aws_cdk.aws_cloudwatch.Alarm:
        '''The Cloudwatch Alarm that will cause scaling actions to be invoked, whether it's in or not in alarm will determine scale up and down actions.'''
        result = self._values.get("scale_alarm")
        assert result is not None, "Required property 'scale_alarm' is missing"
        return typing.cast(aws_cdk.aws_cloudwatch.Alarm, result)

    @builtins.property
    def maximum_task_count(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of tasks that the service will scale out to.

        Note: This does not provide any protection from scaling out above the maximum allowed in your account, set this variable and manage account quotas appropriately.

        :default: 10
        '''
        result = self._values.get("maximum_task_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum_task_count(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of tasks the service will have.

        :default: 1
        '''
        result = self._values.get("minimum_task_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scale_in_cooldown(self) -> typing.Optional[aws_cdk.Duration]:
        '''How long will the application wait before performing another scale in action.

        :default: 60 seconds
        '''
        result = self._values.get("scale_in_cooldown")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def scale_in_increment(self) -> typing.Optional[jsii.Number]:
        '''The number of tasks that will scale in on scale in alarm status.

        :default: 1
        '''
        result = self._values.get("scale_in_increment")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scale_out_cooldown(self) -> typing.Optional[aws_cdk.Duration]:
        '''How long will a the application wait before performing another scale out action.

        :default: 60 seconds
        '''
        result = self._values.get("scale_out_cooldown")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def scale_out_increment(self) -> typing.Optional[jsii.Number]:
        '''The number of tasks that will scale out on scale out alarm status.

        :default: 1
        '''
        result = self._values.get("scale_out_increment")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsIsoServiceAutoscalerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PopulateWithConfig(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-enterprise-iac.PopulateWithConfig",
):
    '''Populate a provided VPC with subnets based on a provided configuration.

    Example::

        const mySubnetConfig: SubnetConfig[] = [
           {
             groupName: 'app',
             cidrRange: '172.31.0.0/27',
             availabilityZone: 'a',
             subnetType: subnetType.PUBLIC,
           },
           {
             groupName: 'app',
             cidrRange: '172.31.0.32/27',
             availabilityZone: 'b',
             subnetType: subnetType.PUBLIC,
           },
           {
             groupName: 'db',
             cidrRange: '172.31.0.64/27',
             availabilityZone: 'a',
             subnetType: subnetType.PRIVATE_WITH_EGRESS,
           },
           {
             groupName: 'db',
             cidrRange: '172.31.0.96/27',
             availabilityZone: 'b',
             subnetType: subnetType.PRIVATE_WITH_EGRESS,
           },
           {
             groupName: 'iso',
             cidrRange: '172.31.0.128/26',
             availabilityZone: 'a',
             subnetType: subnetType.PRIVATE_ISOLATED,
           },
           {
             groupName: 'iso',
             cidrRange: '172.31.0.196/26',
             availabilityZone: 'b',
             subnetType: subnetType.PRIVATE_ISOLATED,
           },
         ];
        new PopulateWithConfig(this, "vpcPopulater", {
          vpcId: 'vpc-abcdefg1234567',
          privateRouteTableId: 'rt-abcdefg123456',
          localRouteTableId: 'rt-123456abcdefg',
          subnetConfig: mySubnetConfig,
        })
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        local_route_table_id: builtins.str,
        private_route_table_id: builtins.str,
        subnet_config: typing.Sequence[typing.Union["SubnetConfig", typing.Dict[str, typing.Any]]],
        vpc_id: builtins.str,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param local_route_table_id: Local route table ID, with routes only to local VPC.
        :param private_route_table_id: Route table ID for a provided route table with routes to enterprise network. Both subnetType.PUBLIC and subnetType.PRIVATE_WITH_EGRESS will use this property
        :param subnet_config: List of Subnet configs to provision to provision.
        :param vpc_id: ID of the VPC provided that needs to be populated.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PopulateWithConfig.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PopulateWithConfigProps(
            local_route_table_id=local_route_table_id,
            private_route_table_id=private_route_table_id,
            subnet_config=subnet_config,
            vpc_id=vpc_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cdklabs/cdk-enterprise-iac.PopulateWithConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "local_route_table_id": "localRouteTableId",
        "private_route_table_id": "privateRouteTableId",
        "subnet_config": "subnetConfig",
        "vpc_id": "vpcId",
    },
)
class PopulateWithConfigProps:
    def __init__(
        self,
        *,
        local_route_table_id: builtins.str,
        private_route_table_id: builtins.str,
        subnet_config: typing.Sequence[typing.Union["SubnetConfig", typing.Dict[str, typing.Any]]],
        vpc_id: builtins.str,
    ) -> None:
        '''
        :param local_route_table_id: Local route table ID, with routes only to local VPC.
        :param private_route_table_id: Route table ID for a provided route table with routes to enterprise network. Both subnetType.PUBLIC and subnetType.PRIVATE_WITH_EGRESS will use this property
        :param subnet_config: List of Subnet configs to provision to provision.
        :param vpc_id: ID of the VPC provided that needs to be populated.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PopulateWithConfigProps.__init__)
            check_type(argname="argument local_route_table_id", value=local_route_table_id, expected_type=type_hints["local_route_table_id"])
            check_type(argname="argument private_route_table_id", value=private_route_table_id, expected_type=type_hints["private_route_table_id"])
            check_type(argname="argument subnet_config", value=subnet_config, expected_type=type_hints["subnet_config"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "local_route_table_id": local_route_table_id,
            "private_route_table_id": private_route_table_id,
            "subnet_config": subnet_config,
            "vpc_id": vpc_id,
        }

    @builtins.property
    def local_route_table_id(self) -> builtins.str:
        '''Local route table ID, with routes only to local VPC.'''
        result = self._values.get("local_route_table_id")
        assert result is not None, "Required property 'local_route_table_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_route_table_id(self) -> builtins.str:
        '''Route table ID for a provided route table with routes to enterprise network.

        Both subnetType.PUBLIC and subnetType.PRIVATE_WITH_EGRESS will use this property
        '''
        result = self._values.get("private_route_table_id")
        assert result is not None, "Required property 'private_route_table_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_config(self) -> typing.List["SubnetConfig"]:
        '''List of Subnet configs to provision to provision.'''
        result = self._values.get("subnet_config")
        assert result is not None, "Required property 'subnet_config' is missing"
        return typing.cast(typing.List["SubnetConfig"], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''ID of the VPC provided that needs to be populated.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PopulateWithConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.IAspect)
class RemovePublicAccessBlockConfiguration(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-enterprise-iac.RemovePublicAccessBlockConfiguration",
):
    '''Looks for S3 Buckets, and removes the ``PublicAccessBlockConfiguration`` property.

    For use in regions where Cloudformation doesn't support this property
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="visit")
    def visit(self, node: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RemovePublicAccessBlockConfiguration.visit)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


@jsii.implements(aws_cdk.IAspect)
class RemoveTags(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-enterprise-iac.RemoveTags",
):
    '''Patch for removing tags from a specific Cloudformation Resource.

    In some regions, the 'Tags' property isn't supported in Cloudformation. This patch makes it easy to remove

    Example::

        // Remove tags on a resource
        Aspects.of(stack).add(new RemoveTags({
          cloudformationResource: 'AWS::ECS::Cluster',
        }));
        // Remove tags without the standard 'Tags' name
        Aspects.of(stack).add(new RemoveTags({
          cloudformationResource: 'AWS::Backup::BackupPlan',
           tagPropertyName: 'BackupPlanTags',
        }));
    '''

    def __init__(
        self,
        *,
        cloudformation_resource: builtins.str,
        tag_property_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloudformation_resource: Name of Cloudformation resource Type (e.g. 'AWS::Lambda::Function').
        :param tag_property_name: Name of the tag property to remove from the resource. Default: Tags
        '''
        props = RemoveTagsProps(
            cloudformation_resource=cloudformation_resource,
            tag_property_name=tag_property_name,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, node: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RemoveTags.visit)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


@jsii.data_type(
    jsii_type="@cdklabs/cdk-enterprise-iac.RemoveTagsProps",
    jsii_struct_bases=[],
    name_mapping={
        "cloudformation_resource": "cloudformationResource",
        "tag_property_name": "tagPropertyName",
    },
)
class RemoveTagsProps:
    def __init__(
        self,
        *,
        cloudformation_resource: builtins.str,
        tag_property_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloudformation_resource: Name of Cloudformation resource Type (e.g. 'AWS::Lambda::Function').
        :param tag_property_name: Name of the tag property to remove from the resource. Default: Tags
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RemoveTagsProps.__init__)
            check_type(argname="argument cloudformation_resource", value=cloudformation_resource, expected_type=type_hints["cloudformation_resource"])
            check_type(argname="argument tag_property_name", value=tag_property_name, expected_type=type_hints["tag_property_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "cloudformation_resource": cloudformation_resource,
        }
        if tag_property_name is not None:
            self._values["tag_property_name"] = tag_property_name

    @builtins.property
    def cloudformation_resource(self) -> builtins.str:
        '''Name of Cloudformation resource Type (e.g. 'AWS::Lambda::Function').'''
        result = self._values.get("cloudformation_resource")
        assert result is not None, "Required property 'cloudformation_resource' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tag_property_name(self) -> typing.Optional[builtins.str]:
        '''Name of the tag property to remove from the resource.

        :default: Tags
        '''
        result = self._values.get("tag_property_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RemoveTagsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.IAspect)
class SetApiGatewayEndpointConfiguration(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-enterprise-iac.SetApiGatewayEndpointConfiguration",
):
    '''Override RestApis to use a set endpoint configuration.

    Some regions don't support EDGE endpoints, and some enterprises require
    specific endpoint types for RestApis
    '''

    def __init__(
        self,
        *,
        endpoint_type: typing.Optional[aws_cdk.aws_apigateway.EndpointType] = None,
    ) -> None:
        '''
        :param endpoint_type: API Gateway endpoint type to override to. Defaults to EndpointType.REGIONAL Default: EndpointType.REGIONAL
        '''
        props = SetApiGatewayEndpointConfigurationProps(endpoint_type=endpoint_type)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, node: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SetApiGatewayEndpointConfiguration.visit)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


@jsii.data_type(
    jsii_type="@cdklabs/cdk-enterprise-iac.SetApiGatewayEndpointConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={"endpoint_type": "endpointType"},
)
class SetApiGatewayEndpointConfigurationProps:
    def __init__(
        self,
        *,
        endpoint_type: typing.Optional[aws_cdk.aws_apigateway.EndpointType] = None,
    ) -> None:
        '''
        :param endpoint_type: API Gateway endpoint type to override to. Defaults to EndpointType.REGIONAL Default: EndpointType.REGIONAL
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SetApiGatewayEndpointConfigurationProps.__init__)
            check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if endpoint_type is not None:
            self._values["endpoint_type"] = endpoint_type

    @builtins.property
    def endpoint_type(self) -> typing.Optional[aws_cdk.aws_apigateway.EndpointType]:
        '''API Gateway endpoint type to override to.

        Defaults to EndpointType.REGIONAL

        :default: EndpointType.REGIONAL
        '''
        result = self._values.get("endpoint_type")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.EndpointType], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SetApiGatewayEndpointConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SplitVpcEvenly(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-enterprise-iac.SplitVpcEvenly",
):
    '''Splits a VPC evenly between a provided number of AZs (3 if not defined), and attaches a provided route table to each, and labels.

    Example::

        // with more specific properties
        new SplitVpcEvenly(this, 'evenSplitVpc', {
          vpcId: 'vpc-abcdefg123456',
          vpcCidr: '172.16.0.0/16',
          routeTableId: 'rt-abcdefgh123456',
          cidrBits: '10',
          numberOfAzs: 4,
          subnetType: subnetType.PRIVATE_ISOLATED,
        });
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        route_table_id: builtins.str,
        vpc_cidr: builtins.str,
        vpc_id: builtins.str,
        cidr_bits: typing.Optional[builtins.str] = None,
        number_of_azs: typing.Optional[jsii.Number] = None,
        subnet_type: typing.Optional[aws_cdk.aws_ec2.SubnetType] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param route_table_id: Route Table ID that will be attached to each subnet created.
        :param vpc_cidr: CIDR range of the VPC you're populating.
        :param vpc_id: ID of the existing VPC you're trying to populate.
        :param cidr_bits: ``cidrBits`` argument for the ```Fn::Cidr`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-cidr.html>`_ Cloudformation intrinsic function. Default: '6'
        :param number_of_azs: Number of AZs to evenly split into. Default: 3
        :param subnet_type: Default: subnetType.PRIVATE
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SplitVpcEvenly.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SplitVpcEvenlyProps(
            route_table_id=route_table_id,
            vpc_cidr=vpc_cidr,
            vpc_id=vpc_id,
            cidr_bits=cidr_bits,
            number_of_azs=number_of_azs,
            subnet_type=subnet_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cdklabs/cdk-enterprise-iac.SplitVpcEvenlyProps",
    jsii_struct_bases=[],
    name_mapping={
        "route_table_id": "routeTableId",
        "vpc_cidr": "vpcCidr",
        "vpc_id": "vpcId",
        "cidr_bits": "cidrBits",
        "number_of_azs": "numberOfAzs",
        "subnet_type": "subnetType",
    },
)
class SplitVpcEvenlyProps:
    def __init__(
        self,
        *,
        route_table_id: builtins.str,
        vpc_cidr: builtins.str,
        vpc_id: builtins.str,
        cidr_bits: typing.Optional[builtins.str] = None,
        number_of_azs: typing.Optional[jsii.Number] = None,
        subnet_type: typing.Optional[aws_cdk.aws_ec2.SubnetType] = None,
    ) -> None:
        '''
        :param route_table_id: Route Table ID that will be attached to each subnet created.
        :param vpc_cidr: CIDR range of the VPC you're populating.
        :param vpc_id: ID of the existing VPC you're trying to populate.
        :param cidr_bits: ``cidrBits`` argument for the ```Fn::Cidr`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-cidr.html>`_ Cloudformation intrinsic function. Default: '6'
        :param number_of_azs: Number of AZs to evenly split into. Default: 3
        :param subnet_type: Default: subnetType.PRIVATE
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SplitVpcEvenlyProps.__init__)
            check_type(argname="argument route_table_id", value=route_table_id, expected_type=type_hints["route_table_id"])
            check_type(argname="argument vpc_cidr", value=vpc_cidr, expected_type=type_hints["vpc_cidr"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument cidr_bits", value=cidr_bits, expected_type=type_hints["cidr_bits"])
            check_type(argname="argument number_of_azs", value=number_of_azs, expected_type=type_hints["number_of_azs"])
            check_type(argname="argument subnet_type", value=subnet_type, expected_type=type_hints["subnet_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "route_table_id": route_table_id,
            "vpc_cidr": vpc_cidr,
            "vpc_id": vpc_id,
        }
        if cidr_bits is not None:
            self._values["cidr_bits"] = cidr_bits
        if number_of_azs is not None:
            self._values["number_of_azs"] = number_of_azs
        if subnet_type is not None:
            self._values["subnet_type"] = subnet_type

    @builtins.property
    def route_table_id(self) -> builtins.str:
        '''Route Table ID that will be attached to each subnet created.'''
        result = self._values.get("route_table_id")
        assert result is not None, "Required property 'route_table_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_cidr(self) -> builtins.str:
        '''CIDR range of the VPC you're populating.'''
        result = self._values.get("vpc_cidr")
        assert result is not None, "Required property 'vpc_cidr' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''ID of the existing VPC you're trying to populate.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cidr_bits(self) -> typing.Optional[builtins.str]:
        '''``cidrBits`` argument for the ```Fn::Cidr`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-cidr.html>`_ Cloudformation intrinsic function.

        :default: '6'
        '''
        result = self._values.get("cidr_bits")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number_of_azs(self) -> typing.Optional[jsii.Number]:
        '''Number of AZs to evenly split into.

        :default: 3
        '''
        result = self._values.get("number_of_azs")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def subnet_type(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetType]:
        '''
        :default: subnetType.PRIVATE
        '''
        result = self._values.get("subnet_type")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetType], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SplitVpcEvenlyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-enterprise-iac.SubnetConfig",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zone": "availabilityZone",
        "cidr_range": "cidrRange",
        "group_name": "groupName",
        "subnet_type": "subnetType",
    },
)
class SubnetConfig:
    def __init__(
        self,
        *,
        availability_zone: builtins.str,
        cidr_range: builtins.str,
        group_name: builtins.str,
        subnet_type: aws_cdk.aws_ec2.SubnetType,
    ) -> None:
        '''
        :param availability_zone: Which availability zone the subnet should be in.
        :param cidr_range: Cidr range of the subnet to create.
        :param group_name: Logical group name of a subnet.
        :param subnet_type: What `SubnetType <https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.SubnetType.html>`_ to use. This will govern the ``aws-cdk:subnet-type`` tag on the subnet SubnetType | ``aws-cdk:subnet-type`` tag value --- | --- ``PRIVATE_ISOLATED`` | 'Isolated' ``PRIVATE_WITH_EGRESS`` | 'Private' ``PUBLIC`` | 'Public'
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SubnetConfig.__init__)
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument cidr_range", value=cidr_range, expected_type=type_hints["cidr_range"])
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument subnet_type", value=subnet_type, expected_type=type_hints["subnet_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "availability_zone": availability_zone,
            "cidr_range": cidr_range,
            "group_name": group_name,
            "subnet_type": subnet_type,
        }

    @builtins.property
    def availability_zone(self) -> builtins.str:
        '''Which availability zone the subnet should be in.'''
        result = self._values.get("availability_zone")
        assert result is not None, "Required property 'availability_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cidr_range(self) -> builtins.str:
        '''Cidr range of the subnet to create.'''
        result = self._values.get("cidr_range")
        assert result is not None, "Required property 'cidr_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_name(self) -> builtins.str:
        '''Logical group name of a subnet.

        Example::

            db
        '''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_type(self) -> aws_cdk.aws_ec2.SubnetType:
        '''What `SubnetType <https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.SubnetType.html>`_ to use.

        This will govern the ``aws-cdk:subnet-type`` tag on the subnet

        SubnetType | ``aws-cdk:subnet-type`` tag value
        --- | ---
        ``PRIVATE_ISOLATED`` | 'Isolated'
        ``PRIVATE_WITH_EGRESS`` | 'Private'
        ``PUBLIC`` | 'Public'
        '''
        result = self._values.get("subnet_type")
        assert result is not None, "Required property 'subnet_type' is missing"
        return typing.cast(aws_cdk.aws_ec2.SubnetType, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubnetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AddLambdaEnvironmentVariables",
    "AddPermissionBoundary",
    "AddPermissionBoundaryProps",
    "EcsIsoServiceAutoscaler",
    "EcsIsoServiceAutoscalerProps",
    "PopulateWithConfig",
    "PopulateWithConfigProps",
    "RemovePublicAccessBlockConfiguration",
    "RemoveTags",
    "RemoveTagsProps",
    "SetApiGatewayEndpointConfiguration",
    "SetApiGatewayEndpointConfigurationProps",
    "SplitVpcEvenly",
    "SplitVpcEvenlyProps",
    "SubnetConfig",
]

publication.publish()
