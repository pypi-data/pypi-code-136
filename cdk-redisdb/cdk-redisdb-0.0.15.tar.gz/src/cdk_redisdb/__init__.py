'''
# cdk-redisdb

An AWS CDK construct which spins up an Elasticache Replication Group, or a MemoryDB Cluster. API still in flux as in fairly early development - pin against a specific version.

**SECURITY NOTE**: This construct is still in development, please carefully review the resources created before using this in production.

## Usage (TypeScript/JavaScript)

Install via npm:

```shell
$ npm i cdk-redisdb
```

Add an Elasticache Replication Group to your CDK stack:

```python
import { RedisDB } from 'cdk-redisdb'

new RedisDB(this, 'redisdb-repl-group', {
  nodes: 1,
  nodeType: 'cache.m6g.large',
  engineVersion: '6.2',
})
```

Add a MemoryDB Cluster to your CDK stack:

```python
import { MemoryDB } from 'cdk-redisdb'

new MemoryDB(this, 'memorydb-repl-group', {
  nodes: 1,
  nodeType: 'db.t4g.small',
  engineVersion: '6.2',
})
```

Specify a VPC rather than having a VPC auto-created for you:

```python
import { MemoryDB } from 'cdk-redisdb'

let vpc = new ec2.Vpc(this, 'Vpc', {
  subnetConfiguration: [
    {
      cidrMask: 24,
      name: 'public1',
      subnetType: ec2.SubnetType.PUBLIC,
    },
    {
      cidrMask: 24,
      name: 'isolated1',
      subnetType: ec2.SubnetType.ISOLATED,
    },
  ],
})

new RedisDB(this, 'redis-use-existing-vpc', {
  existingVpc: vpc,
})
```

Add 2 replicas per node, and add shards to cluster when memory exceeds 60%.

```python
import { RedisDB } from 'cdk-redisdb'

new RedisDB(this, 'redisdb-repl-group', {
  nodes: 1,
  replicas: 2, // 2 replicas per node
  nodeType: 'cache.m6g.large',
  memoryAutoscalingTarget: 60,
})
```

```python
import { RedisDB } from 'cdk-redisdb'

let vpc = new ec2.Vpc(this, 'Vpc', {
  subnetConfiguration: [
    {
      cidrMask: 24,
      name: 'public1',
      subnetType: ec2.SubnetType.PUBLIC,
    },
    {
      cidrMask: 24,
      name: 'isolated1',
      subnetType: ec2.SubnetType.PRIVATE,
    },
  ],
})

const ecSecurityGroup = new ec2.SecurityGroup(this, 'elasticache-sg', {
  vpc: vpc,
  description: 'SecurityGroup associated with the ElastiCache Redis Cluster',
  allowAllOutbound: false,
});

new RedisDB(this, 'redisdb-repl-group', {
  nodes: 1,
  nodeType: 'cache.m6g.large',
  nodesCpuAutoscalingTarget: 50,
  existingVpc: vpc,
  existingSecurityGroup: ecSecurityGroup,
})
```

Features in progress:

* MemoryDB ACLs (commented out to avoid default bad practices, read comments to understand the CloudFormation)

Features to come:

* Replication Groups with cluster mode disabled (for those using multiple databases)
* Improved API - sane choice of props
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
import aws_cdk.aws_ec2
import aws_cdk.aws_elasticache
import aws_cdk.aws_memorydb
import constructs


class MemoryDB(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-redisdb.MemoryDB",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]] = None,
        auth_token: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        existing_security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        existing_subnet_group_name: typing.Optional[builtins.str] = None,
        existing_vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        memory_autoscaling_target: typing.Optional[jsii.Number] = None,
        nodes: typing.Optional[jsii.Number] = None,
        nodes_cpu_autoscaling_target: typing.Optional[jsii.Number] = None,
        node_type: typing.Optional[builtins.str] = None,
        replicas: typing.Optional[jsii.Number] = None,
        replicas_cpu_autoscaling_target: typing.Optional[jsii.Number] = None,
        subnet_group_name: typing.Optional[builtins.str] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]] = None,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Union[aws_cdk.Environment, typing.Dict[str, typing.Any]]] = None,
        stack_name: typing.Optional[builtins.str] = None,
        synthesizer: typing.Optional[aws_cdk.IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param at_rest_encryption_enabled: 
        :param auth_token: 
        :param engine_version: 
        :param existing_security_group: 
        :param existing_subnet_group_name: 
        :param existing_vpc: 
        :param memory_autoscaling_target: 
        :param nodes: 
        :param nodes_cpu_autoscaling_target: 
        :param node_type: 
        :param replicas: 
        :param replicas_cpu_autoscaling_target: 
        :param subnet_group_name: 
        :param transit_encryption_enabled: 
        :param analytics_reporting: Include runtime versioning information in this Stack. Default: ``analyticsReporting`` setting of containing ``App``, or value of 'aws:cdk:version-reporting' context key
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param synthesizer: Synthesis method to use while deploying this stack. Default: - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag is set, ``LegacyStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MemoryDB.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = RedisDBProps(
            at_rest_encryption_enabled=at_rest_encryption_enabled,
            auth_token=auth_token,
            engine_version=engine_version,
            existing_security_group=existing_security_group,
            existing_subnet_group_name=existing_subnet_group_name,
            existing_vpc=existing_vpc,
            memory_autoscaling_target=memory_autoscaling_target,
            nodes=nodes,
            nodes_cpu_autoscaling_target=nodes_cpu_autoscaling_target,
            node_type=node_type,
            replicas=replicas,
            replicas_cpu_autoscaling_target=replicas_cpu_autoscaling_target,
            subnet_group_name=subnet_group_name,
            transit_encryption_enabled=transit_encryption_enabled,
            analytics_reporting=analytics_reporting,
            description=description,
            env=env,
            stack_name=stack_name,
            synthesizer=synthesizer,
            tags=tags,
            termination_protection=termination_protection,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> aws_cdk.aws_memorydb.CfnCluster:
        return typing.cast(aws_cdk.aws_memorydb.CfnCluster, jsii.get(self, "cluster"))


class RedisDB(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-redisdb.RedisDB",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]] = None,
        auth_token: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        existing_security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        existing_subnet_group_name: typing.Optional[builtins.str] = None,
        existing_vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        memory_autoscaling_target: typing.Optional[jsii.Number] = None,
        nodes: typing.Optional[jsii.Number] = None,
        nodes_cpu_autoscaling_target: typing.Optional[jsii.Number] = None,
        node_type: typing.Optional[builtins.str] = None,
        replicas: typing.Optional[jsii.Number] = None,
        replicas_cpu_autoscaling_target: typing.Optional[jsii.Number] = None,
        subnet_group_name: typing.Optional[builtins.str] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]] = None,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Union[aws_cdk.Environment, typing.Dict[str, typing.Any]]] = None,
        stack_name: typing.Optional[builtins.str] = None,
        synthesizer: typing.Optional[aws_cdk.IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param at_rest_encryption_enabled: 
        :param auth_token: 
        :param engine_version: 
        :param existing_security_group: 
        :param existing_subnet_group_name: 
        :param existing_vpc: 
        :param memory_autoscaling_target: 
        :param nodes: 
        :param nodes_cpu_autoscaling_target: 
        :param node_type: 
        :param replicas: 
        :param replicas_cpu_autoscaling_target: 
        :param subnet_group_name: 
        :param transit_encryption_enabled: 
        :param analytics_reporting: Include runtime versioning information in this Stack. Default: ``analyticsReporting`` setting of containing ``App``, or value of 'aws:cdk:version-reporting' context key
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param synthesizer: Synthesis method to use while deploying this stack. Default: - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag is set, ``LegacyStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RedisDB.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = RedisDBProps(
            at_rest_encryption_enabled=at_rest_encryption_enabled,
            auth_token=auth_token,
            engine_version=engine_version,
            existing_security_group=existing_security_group,
            existing_subnet_group_name=existing_subnet_group_name,
            existing_vpc=existing_vpc,
            memory_autoscaling_target=memory_autoscaling_target,
            nodes=nodes,
            nodes_cpu_autoscaling_target=nodes_cpu_autoscaling_target,
            node_type=node_type,
            replicas=replicas,
            replicas_cpu_autoscaling_target=replicas_cpu_autoscaling_target,
            subnet_group_name=subnet_group_name,
            transit_encryption_enabled=transit_encryption_enabled,
            analytics_reporting=analytics_reporting,
            description=description,
            env=env,
            stack_name=stack_name,
            synthesizer=synthesizer,
            tags=tags,
            termination_protection=termination_protection,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="replicationGroup")
    def replication_group(self) -> aws_cdk.aws_elasticache.CfnReplicationGroup:
        return typing.cast(aws_cdk.aws_elasticache.CfnReplicationGroup, jsii.get(self, "replicationGroup"))


@jsii.data_type(
    jsii_type="cdk-redisdb.RedisDBProps",
    jsii_struct_bases=[aws_cdk.StackProps],
    name_mapping={
        "analytics_reporting": "analyticsReporting",
        "description": "description",
        "env": "env",
        "stack_name": "stackName",
        "synthesizer": "synthesizer",
        "tags": "tags",
        "termination_protection": "terminationProtection",
        "at_rest_encryption_enabled": "atRestEncryptionEnabled",
        "auth_token": "authToken",
        "engine_version": "engineVersion",
        "existing_security_group": "existingSecurityGroup",
        "existing_subnet_group_name": "existingSubnetGroupName",
        "existing_vpc": "existingVpc",
        "memory_autoscaling_target": "memoryAutoscalingTarget",
        "nodes": "nodes",
        "nodes_cpu_autoscaling_target": "nodesCpuAutoscalingTarget",
        "node_type": "nodeType",
        "replicas": "replicas",
        "replicas_cpu_autoscaling_target": "replicasCpuAutoscalingTarget",
        "subnet_group_name": "subnetGroupName",
        "transit_encryption_enabled": "transitEncryptionEnabled",
    },
)
class RedisDBProps(aws_cdk.StackProps):
    def __init__(
        self,
        *,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Union[aws_cdk.Environment, typing.Dict[str, typing.Any]]] = None,
        stack_name: typing.Optional[builtins.str] = None,
        synthesizer: typing.Optional[aws_cdk.IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]] = None,
        auth_token: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        existing_security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        existing_subnet_group_name: typing.Optional[builtins.str] = None,
        existing_vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        memory_autoscaling_target: typing.Optional[jsii.Number] = None,
        nodes: typing.Optional[jsii.Number] = None,
        nodes_cpu_autoscaling_target: typing.Optional[jsii.Number] = None,
        node_type: typing.Optional[builtins.str] = None,
        replicas: typing.Optional[jsii.Number] = None,
        replicas_cpu_autoscaling_target: typing.Optional[jsii.Number] = None,
        subnet_group_name: typing.Optional[builtins.str] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]] = None,
    ) -> None:
        '''
        :param analytics_reporting: Include runtime versioning information in this Stack. Default: ``analyticsReporting`` setting of containing ``App``, or value of 'aws:cdk:version-reporting' context key
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param synthesizer: Synthesis method to use while deploying this stack. Default: - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag is set, ``LegacyStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false
        :param at_rest_encryption_enabled: 
        :param auth_token: 
        :param engine_version: 
        :param existing_security_group: 
        :param existing_subnet_group_name: 
        :param existing_vpc: 
        :param memory_autoscaling_target: 
        :param nodes: 
        :param nodes_cpu_autoscaling_target: 
        :param node_type: 
        :param replicas: 
        :param replicas_cpu_autoscaling_target: 
        :param subnet_group_name: 
        :param transit_encryption_enabled: 
        '''
        if isinstance(env, dict):
            env = aws_cdk.Environment(**env)
        if __debug__:
            type_hints = typing.get_type_hints(RedisDBProps.__init__)
            check_type(argname="argument analytics_reporting", value=analytics_reporting, expected_type=type_hints["analytics_reporting"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument stack_name", value=stack_name, expected_type=type_hints["stack_name"])
            check_type(argname="argument synthesizer", value=synthesizer, expected_type=type_hints["synthesizer"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument termination_protection", value=termination_protection, expected_type=type_hints["termination_protection"])
            check_type(argname="argument at_rest_encryption_enabled", value=at_rest_encryption_enabled, expected_type=type_hints["at_rest_encryption_enabled"])
            check_type(argname="argument auth_token", value=auth_token, expected_type=type_hints["auth_token"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument existing_security_group", value=existing_security_group, expected_type=type_hints["existing_security_group"])
            check_type(argname="argument existing_subnet_group_name", value=existing_subnet_group_name, expected_type=type_hints["existing_subnet_group_name"])
            check_type(argname="argument existing_vpc", value=existing_vpc, expected_type=type_hints["existing_vpc"])
            check_type(argname="argument memory_autoscaling_target", value=memory_autoscaling_target, expected_type=type_hints["memory_autoscaling_target"])
            check_type(argname="argument nodes", value=nodes, expected_type=type_hints["nodes"])
            check_type(argname="argument nodes_cpu_autoscaling_target", value=nodes_cpu_autoscaling_target, expected_type=type_hints["nodes_cpu_autoscaling_target"])
            check_type(argname="argument node_type", value=node_type, expected_type=type_hints["node_type"])
            check_type(argname="argument replicas", value=replicas, expected_type=type_hints["replicas"])
            check_type(argname="argument replicas_cpu_autoscaling_target", value=replicas_cpu_autoscaling_target, expected_type=type_hints["replicas_cpu_autoscaling_target"])
            check_type(argname="argument subnet_group_name", value=subnet_group_name, expected_type=type_hints["subnet_group_name"])
            check_type(argname="argument transit_encryption_enabled", value=transit_encryption_enabled, expected_type=type_hints["transit_encryption_enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if analytics_reporting is not None:
            self._values["analytics_reporting"] = analytics_reporting
        if description is not None:
            self._values["description"] = description
        if env is not None:
            self._values["env"] = env
        if stack_name is not None:
            self._values["stack_name"] = stack_name
        if synthesizer is not None:
            self._values["synthesizer"] = synthesizer
        if tags is not None:
            self._values["tags"] = tags
        if termination_protection is not None:
            self._values["termination_protection"] = termination_protection
        if at_rest_encryption_enabled is not None:
            self._values["at_rest_encryption_enabled"] = at_rest_encryption_enabled
        if auth_token is not None:
            self._values["auth_token"] = auth_token
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if existing_security_group is not None:
            self._values["existing_security_group"] = existing_security_group
        if existing_subnet_group_name is not None:
            self._values["existing_subnet_group_name"] = existing_subnet_group_name
        if existing_vpc is not None:
            self._values["existing_vpc"] = existing_vpc
        if memory_autoscaling_target is not None:
            self._values["memory_autoscaling_target"] = memory_autoscaling_target
        if nodes is not None:
            self._values["nodes"] = nodes
        if nodes_cpu_autoscaling_target is not None:
            self._values["nodes_cpu_autoscaling_target"] = nodes_cpu_autoscaling_target
        if node_type is not None:
            self._values["node_type"] = node_type
        if replicas is not None:
            self._values["replicas"] = replicas
        if replicas_cpu_autoscaling_target is not None:
            self._values["replicas_cpu_autoscaling_target"] = replicas_cpu_autoscaling_target
        if subnet_group_name is not None:
            self._values["subnet_group_name"] = subnet_group_name
        if transit_encryption_enabled is not None:
            self._values["transit_encryption_enabled"] = transit_encryption_enabled

    @builtins.property
    def analytics_reporting(self) -> typing.Optional[builtins.bool]:
        '''Include runtime versioning information in this Stack.

        :default:

        ``analyticsReporting`` setting of containing ``App``, or value of
        'aws:cdk:version-reporting' context key
        '''
        result = self._values.get("analytics_reporting")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the stack.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def env(self) -> typing.Optional[aws_cdk.Environment]:
        '''The AWS environment (account/region) where this stack will be deployed.

        Set the ``region``/``account`` fields of ``env`` to either a concrete value to
        select the indicated environment (recommended for production stacks), or to
        the values of environment variables
        ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment
        depend on the AWS credentials/configuration that the CDK CLI is executed
        under (recommended for development stacks).

        If the ``Stack`` is instantiated inside a ``Stage``, any undefined
        ``region``/``account`` fields from ``env`` will default to the same field on the
        encompassing ``Stage``, if configured there.

        If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the
        Stack will be considered "*environment-agnostic*"". Environment-agnostic
        stacks can be deployed to any environment but may not be able to take
        advantage of all features of the CDK. For example, they will not be able to
        use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not
        automatically translate Service Principals to the right format based on the
        environment's AWS partition, and other such enhancements.

        :default:

        - The environment of the containing ``Stage`` if available,
        otherwise create the stack will be environment-agnostic.

        Example::

            // Use a concrete account and region to deploy this stack to:
            // `.account` and `.region` will simply return these values.
            new Stack(app, 'Stack1', {
              env: {
                account: '123456789012',
                region: 'us-east-1'
              },
            });
            
            // Use the CLI's current credentials to determine the target environment:
            // `.account` and `.region` will reflect the account+region the CLI
            // is configured to use (based on the user CLI credentials)
            new Stack(app, 'Stack2', {
              env: {
                account: process.env.CDK_DEFAULT_ACCOUNT,
                region: process.env.CDK_DEFAULT_REGION
              },
            });
            
            // Define multiple stacks stage associated with an environment
            const myStage = new Stage(app, 'MyStage', {
              env: {
                account: '123456789012',
                region: 'us-east-1'
              }
            });
            
            // both of these stacks will use the stage's account/region:
            // `.account` and `.region` will resolve to the concrete values as above
            new MyStack(myStage, 'Stack1');
            new YourStack(myStage, 'Stack2');
            
            // Define an environment-agnostic stack:
            // `.account` and `.region` will resolve to `{ "Ref": "AWS::AccountId" }` and `{ "Ref": "AWS::Region" }` respectively.
            // which will only resolve to actual values by CloudFormation during deployment.
            new MyStack(app, 'Stack1');
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[aws_cdk.Environment], result)

    @builtins.property
    def stack_name(self) -> typing.Optional[builtins.str]:
        '''Name to deploy the stack with.

        :default: - Derived from construct path.
        '''
        result = self._values.get("stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def synthesizer(self) -> typing.Optional[aws_cdk.IStackSynthesizer]:
        '''Synthesis method to use while deploying this stack.

        :default:

        - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag
        is set, ``LegacyStackSynthesizer`` otherwise.
        '''
        result = self._values.get("synthesizer")
        return typing.cast(typing.Optional[aws_cdk.IStackSynthesizer], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Stack tags that will be applied to all the taggable resources and the stack itself.

        :default: {}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def termination_protection(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable termination protection for this stack.

        :default: false
        '''
        result = self._values.get("termination_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]]:
        result = self._values.get("at_rest_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]], result)

    @builtins.property
    def auth_token(self) -> typing.Optional[builtins.str]:
        result = self._values.get("auth_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def existing_security_group(
        self,
    ) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        result = self._values.get("existing_security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def existing_subnet_group_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("existing_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def existing_vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        result = self._values.get("existing_vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    @builtins.property
    def memory_autoscaling_target(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("memory_autoscaling_target")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def nodes(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def nodes_cpu_autoscaling_target(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("nodes_cpu_autoscaling_target")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def node_type(self) -> typing.Optional[builtins.str]:
        result = self._values.get("node_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replicas(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("replicas")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def replicas_cpu_autoscaling_target(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("replicas_cpu_autoscaling_target")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def subnet_group_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]]:
        result = self._values.get("transit_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RedisDBProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "MemoryDB",
    "RedisDB",
    "RedisDBProps",
]

publication.publish()
