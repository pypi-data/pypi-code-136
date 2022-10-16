from dataclasses import dataclass
from typing import Dict, Optional, Union, List

from myccli.terraform.common import JSONDocument, InlineBlock, ETFCall, ProviderRequirement, JSONDocumentList
from myccli.terraform.resources.base import TerraformResource, basic_terraform_item, TerraformDataSource


class AWSTerraformResource(TerraformResource):
    def get_self_ref(self):
        return self.get_arg_ref('arn')

    def get_args(self) -> Dict[str, any]:
        raise NotImplementedError

    def required_providers(self) -> List[ProviderRequirement]:
        return [ProviderRequirement('aws')]


class AWSTerraformDataSource(TerraformDataSource):
    def get_self_ref(self):
        return self.get_arg_ref('arn')

    def get_args(self) -> Dict[str, any]:
        raise NotImplementedError

    def required_providers(self) -> List[ProviderRequirement]:
        return [ProviderRequirement('aws')]


class TFAWSIAMRole(AWSTerraformResource):
    def __init__(self, tf_name: str, *, assume_role_policy: Optional[dict] = None, name: Optional[str] = None):
        super().__init__('aws_iam_role', tf_name)
        self.name = name or tf_name
        self.assume_role_policy = assume_role_policy or self.create_default_assume_role_policy('lambda.amazonaws.com')

    @staticmethod
    def create_default_assume_role_policy(aws_service: str) -> dict:
        return {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'sts:AssumeRole',
                    'Principal': {
                        'Service': aws_service
                    },
                    'Effect': 'Allow',
                    'Sid': ''
                }
            ]
        }

    def get_args(self) -> Dict[str, any]:
        return {
            'name': self.name,
            'assume_role_policy': JSONDocument(self.assume_role_policy),
        }


class TFAWSIAMPolicy(AWSTerraformResource):
    def __init__(self, tf_name: str, *, policy: dict, name: Optional[str] = None):
        super().__init__('aws_iam_policy', tf_name)
        self.name = name or tf_name
        self.policy = policy

    def get_args(self) -> Dict[str, any]:
        return {
            'name': self.name,
            'policy': JSONDocument(self.policy),
        }


class TFAWSIAMRolePolicyAttachment(AWSTerraformResource):
    def __init__(self, tf_name: str, *, role: TFAWSIAMRole, policy: Optional[TFAWSIAMPolicy] = None,
                 policy_arn: Optional[str] = None):
        super().__init__('aws_iam_role_policy_attachment', tf_name)
        self.role = role

        assert bool(policy) ^ bool(policy_arn)
        self._policy = policy
        self._policy_arn = policy_arn

    def get_args(self) -> Dict[str, any]:
        return {
            'role': self.role.get_arg_ref('id'),
            'policy_arn': self._policy.get_arg_ref('arn') if self._policy is not None else self._policy_arn,
        }


class TFAWSIAMInstanceProfile(AWSTerraformResource):
    def __init__(self, tf_name: str, *, name: Optional[str] = None, role: TFAWSIAMRole):
        super().__init__('aws_iam_instance_profile', tf_name)
        self.name = name or tf_name
        self.role = role

    def get_args(self) -> Dict[str, any]:
        return {
            'name': self.name,
            'role': self.role.get_arg_ref('id'),
        }


class TFAWSVpc(AWSTerraformResource):
    def __init__(self, tf_name, *, cidr_block: str, name: Optional[str], enable_dns_support=True,
                 enable_dns_hostnames=True):
        super().__init__('aws_vpc', tf_name)
        self.cidr_block = cidr_block
        self.name = name
        self.enable_dns_support = enable_dns_support
        self.enable_dns_hostnames = enable_dns_hostnames

    def get_args(self) -> Dict[str, any]:
        args = {
            'cidr_block': self.cidr_block,
            'enable_dns_support': self.enable_dns_support,
            'enable_dns_hostnames': self.enable_dns_hostnames,
        }

        if self.name is not None:
            args['tags'] = {
                'Name': self.name,
            }

        return args


class TFAWSSubnet(AWSTerraformResource):
    def __init__(self, tf_name, *, vpc: TFAWSVpc, cidr_block: str, name: Optional[str], az: str,
                 map_public_ip_on_launch=False):
        super().__init__('aws_subnet', tf_name)
        self.vpc = vpc
        self.cidr_block = cidr_block
        self.name = name
        self.az = az
        self.map_public_ip_on_launch = map_public_ip_on_launch

    def get_args(self) -> Dict[str, any]:
        args = {
            'vpc_id': self.vpc.get_arg_ref('id'),
            'cidr_block': self.cidr_block,
            'availability_zone': self.az,
            'map_public_ip_on_launch': self.map_public_ip_on_launch
        }

        if self.name is not None:
            args['tags'] = {
                'Name': self.name,
            }

        return args


@dataclass
class AWSRouteTableRoute:
    cidr_block: str
    target_kind: str
    target_value: str


class TFAWSRouteTable(AWSTerraformResource):
    def __init__(self, tf_name, *, vpc: TFAWSVpc, routes: Optional[List[AWSRouteTableRoute]] = None):
        super().__init__('aws_route_table', tf_name)
        self.vpc = vpc
        self.routes: List[AWSRouteTableRoute] = routes or []

    def get_args(self) -> Dict[str, any]:
        args = {
            'vpc_id': self.vpc.get_arg_ref('id'),
        }

        if self.routes:
            args['route'] = [
                InlineBlock({
                    'cidr_block': route.cidr_block,
                    route.target_kind: route.target_value,
                })
                for route in self.routes
            ]

        return args


class TFAWSInternetGateway(AWSTerraformResource):
    def __init__(self, tf_name, *, vpc: TFAWSVpc):
        super().__init__('aws_internet_gateway', tf_name)
        self.vpc = vpc

    def get_args(self) -> Dict[str, any]:
        return {
            'vpc_id': self.vpc.get_arg_ref('id'),
        }


class TFAWSRouteTableAssociation(AWSTerraformResource):
    def __init__(self, tf_name, *, subnet: TFAWSSubnet, route_table: TFAWSRouteTable):
        super().__init__('aws_route_table_association', tf_name)
        self.subnet = subnet
        self.route_table = route_table

    def get_args(self) -> Dict[str, any]:
        return {
            'subnet_id': self.subnet.get_arg_ref('id'),
            'route_table_id': self.route_table.get_arg_ref('id'),
        }


class TFAWSLambdaFunction(AWSTerraformResource):
    def __init__(self, tf_name: str, *, filename: str, role: TFAWSIAMRole, handler: str, runtime: str,
                 function_name: Optional[str] = None, env: Optional[dict] = None):
        super().__init__('aws_lambda_function', tf_name)
        self.filename = filename
        self.role = role
        self.handler = handler
        self.runtime = runtime
        self.function_name = function_name or tf_name
        self.env = env

    def get_args(self) -> Dict[str, any]:
        args = {
            'filename': self.filename,
            'source_code_hash': ETFCall('filebase64sha256', [self.filename]),
            'role': self.role,
            'handler': self.handler,
            'runtime': self.runtime,
            'function_name': self.function_name,
        }

        if self.env:
            args['environment'] = InlineBlock(
                variables=self.env,
            )

        return args


class TFAWSLambdaFunctionURL(AWSTerraformResource):
    def __init__(self, tf_name: str, *, function: TFAWSLambdaFunction):
        super().__init__('aws_lambda_function_url', tf_name)
        self._function = function

    def get_args(self) -> Dict[str, any]:
        return {
            'function_name': self._function.get_arg_ref('function_name'),
            'authorization_type': 'NONE',
        }


class TFAWSCloudwatchLogGroup(AWSTerraformResource):
    def __init__(self, tf_name, *, name: str, retention_in_days: int):
        super().__init__('aws_cloudwatch_log_group', tf_name)
        self.name = name
        self.retention_in_days = retention_in_days
        self.lifecycle.prevent_destroy = False

    def get_args(self) -> Dict[str, any]:
        return {
            'name': self.name,
            'retention_in_days': self.retention_in_days,
        }


class TFAWSS3Bucket(AWSTerraformResource):
    def __init__(self, tf_name: str, *, bucket: Optional[str] = None):
        super().__init__('aws_s3_bucket', tf_name)
        self.bucket = bucket

    def get_args(self) -> Dict[str, any]:
        args = {}

        if self.bucket:
            args['bucket'] = self.bucket

        return args


class TFAWSS3Object(AWSTerraformResource):
    def __init__(self, tf_name: str, *, bucket: TFAWSS3Bucket, key: str, source: Optional[str] = None,
                 content: Optional[Union[dict, bytes]] = None):
        super().__init__('aws_s3_object', tf_name)
        self.bucket = bucket
        self.key = key
        self.source = source
        self.content = content

    def get_args(self) -> Dict[str, any]:
        args = {
            'key': self.key,
        }

        if self.bucket:
            args['bucket'] = self.bucket.get_arg_ref('id')
        if self.source:
            args['source'] = self.source
            args['etag'] = ETFCall('filemd5', [self.source])
        if self.content:
            if isinstance(self.content, dict):
                args['content'] = JSONDocument(self.content)
            else:
                args['content'] = self.content.decode('utf-8')

        return args


class TFAWSECRRepository(AWSTerraformResource):
    def __init__(self, tf_name, *, name: str, mutable: bool, force_delete=False):
        super().__init__('aws_ecr_repository', tf_name)
        self.name = name
        self.mutable = mutable
        self.force_delete = force_delete

    def get_args(self) -> Dict[str, any]:
        return {
            'name': self.name,
            'image_tag_mutability': 'MUTABLE' if self.mutable else 'IMMUTABLE',
            'force_delete': self.force_delete
        }


@dataclass
class AWSSecurityGroupRule:
    description: str
    from_port: int
    to_port: int
    cidr_blocks: List[str]
    protocol: Optional[str] = None

    def to_dict(self):
        return {
            'description': self.description,
            'from_port': self.from_port,
            'to_port': self.to_port,
            'protocol': self.protocol or '-1',
            'cidr_blocks': self.cidr_blocks,
        }


class TFAWSSecurityGroup(AWSTerraformResource):
    def __init__(
            self,
            tf_name,
            *,
            name: Optional[str] = None,
            description: str,
            vpc: Optional[TFAWSVpc] = None,
            ingress: Optional[List[AWSSecurityGroupRule]] = None,
            egress: Optional[List[AWSSecurityGroupRule]] = None,
    ):
        super().__init__('aws_security_group', tf_name)
        self.name = name or tf_name
        self.description = description
        self.vpc = vpc
        self.ingress = ingress or []
        self.egress = egress or []

    def get_args(self) -> Dict[str, any]:
        args = {
            'name': self.name,
            'description': self.description,
        }

        if self.vpc is not None:
            args['vpc_id'] = self.vpc.get_arg_ref('id')
        if self.ingress:
            args['ingress'] = [InlineBlock(rule.to_dict()) for rule in self.ingress]
        if self.egress:
            args['egress'] = [InlineBlock(rule.to_dict()) for rule in self.egress]

        return args


@basic_terraform_item
class TFAWSLaunchConfiguration(AWSTerraformResource):
    __kind__ = 'aws_launch_configuration'
    image_id: str
    instance_type: str
    cluster_name: str
    iam_instance_profile: TFAWSIAMInstanceProfile
    security_groups: List[TFAWSSecurityGroup]
    associate_public_ip_address: bool = True

    def override_args(self):
        return {
            'iam_instance_profile': self.iam_instance_profile.get_arg_ref('name'),
            'user_data': rf"#!/bin/bash\necho ECS_CLUSTER='{self.cluster_name}' >> /etc/ecs/ecs.config",
            'cluster_name': None,
            'security_groups': [sg.get_arg_ref('id') for sg in self.security_groups]
        }


class TFAWSAutoScalingGroup(AWSTerraformResource):
    def __init__(self,
                 tf_name,
                 *,
                 min_size: int,
                 max_size: int,
                 launch_configuration: TFAWSLaunchConfiguration,
                 desired_capacity: Optional[int] = None,
                 availability_zones: Optional[List[str]] = None,
                 vpc_subnets: Optional[List[TFAWSSubnet]] = None,
                 ):
        super().__init__('aws_autoscaling_group', tf_name)
        self.min_size = min_size
        self.max_size = max_size
        self.desired_capacity = desired_capacity
        self.launch_configuration = launch_configuration

        self.availability_zones = availability_zones
        self.vpc_subnets = vpc_subnets
        assert not (bool(self.availability_zones) and bool(self.vpc_subnets))

    def get_args(self) -> Dict[str, any]:
        args = {
            'min_size': self.min_size,
            'max_size': self.max_size,
            'launch_configuration': self.launch_configuration.get_arg_ref('name'),
        }

        if self.desired_capacity is not None:
            args['desired_capacity'] = self.desired_capacity
        if self.availability_zones is not None:
            args['availability_zones'] = self.availability_zones
        if self.vpc_subnets is not None:
            args['vpc_zone_identifier'] = [subnet.get_arg_ref('id') for subnet in self.vpc_subnets]

        return args


class TFAWSECSCapacityProvider(AWSTerraformResource):
    def __init__(self, tf_name, *, name: Optional[str] = None, asg: TFAWSAutoScalingGroup):
        super().__init__('aws_ecs_capacity_provider', tf_name)
        self.name = name or tf_name
        self.asg = asg

    def get_args(self) -> Dict[str, any]:
        return {
            'name': self.name,
            'auto_scaling_group_provider': InlineBlock(
                auto_scaling_group_arn=self.asg.get_self_ref(),
            )
        }


class TFAWSECSCluster(AWSTerraformResource):
    def __init__(self, tf_name, *, name: Optional[str] = None):
        super().__init__('aws_ecs_cluster', tf_name)
        self.name = name or tf_name

    def get_args(self) -> Dict[str, any]:
        return {
            'name': self.name,
        }


class TFAWSECSClusterCapacityProviders(AWSTerraformResource):
    def __init__(self, tf_name, *, cluster: TFAWSECSCluster, provider: TFAWSECSCapacityProvider,
                 weight: int = 0, base: int = 0):
        super().__init__('aws_ecs_cluster_capacity_providers', tf_name)
        self.cluster = cluster
        self.provider = provider
        self.weight = weight
        self.base = base

    def get_args(self) -> Dict[str, any]:
        return {
            'cluster_name': self.cluster.get_arg_ref('name'),
            'capacity_providers': [self.provider.get_arg_ref('name')],
            'default_capacity_provider_strategy': InlineBlock(
                capacity_provider=self.provider.get_arg_ref('name'),
                weight=self.weight,
                base=self.base,
            )
        }


@dataclass
class AWSECSPortMapping:
    container_port: int
    host_port: int


@dataclass
class AWSECSLogConfigurationOptions:
    group: str
    region: str
    stream_prefix: str

    def to_dict(self):
        return {
            'awslogs-group': self.group,
            'awslogs-region': self.region,
            'awslogs-stream-prefix': self.stream_prefix,
        }


@dataclass
class AWSECSLogConfiguration:
    log_driver: str
    options: AWSECSLogConfigurationOptions

    def to_dict(self):
        return {
            'logDriver': self.log_driver,
            'options': self.options.to_dict()
        }


@dataclass
class AWSECSContainerDefinition:
    name: str
    image: str
    cpu: Optional[int] = None
    memory: Optional[int] = None
    command: Optional[List[str]] = None
    essential: bool = True
    environment: Optional[Dict[str, str]] = None
    port_mappings: List[AWSECSPortMapping] = None
    log_configuration: Optional[AWSECSLogConfiguration] = None

    def to_dict(self) -> Dict[str, any]:
        args = {
            'name': self.name,
            'image': self.image,
            'essential': self.essential,
            'portMappings': [{
                'containerPort': port_map.container_port,
                'hostPort': port_map.host_port,
            } for port_map in self.port_mappings]
        }

        if self.cpu is not None:
            args['cpu'] = self.cpu
        if self.memory is not None:
            args['memory'] = self.memory
        if self.command is not None:
            args['command'] = self.command
        if self.log_configuration is not None:
            args['logConfiguration'] = self.log_configuration.to_dict()
        if self.environment is not None:
            args['environment'] = [
                {'name': key, 'value': value}
                for key, value in self.environment.items()
            ]

        return args


class TFAWSECSTaskDefinition(AWSTerraformResource):
    def __init__(self, tf_name, *,
                 family: Optional[str],
                 container_definitions: List[AWSECSContainerDefinition],
                 execution_role: TFAWSIAMRole,
                 fargate: bool = False,
                 cpu: Optional[int] = None,
                 memory: Optional[int] = None,
                 ):
        super().__init__('aws_ecs_task_definition', tf_name)
        self.family = family or tf_name
        self.container_definitions = container_definitions
        self.execution_role = execution_role
        self.fargate = fargate
        self.cpu = cpu
        self.memory = memory

        if self.fargate:
            assert self.cpu is not None and self.memory is not None, \
                'CPU and memory requirements must be defined at task-level with FARGATE'

    def get_args(self) -> Dict[str, any]:
        args = {
            'family': self.family,
            'container_definitions': JSONDocumentList([x.to_dict() for x in self.container_definitions]),
            'execution_role_arn': self.execution_role.get_self_ref(),
        }

        if self.fargate:
            args['requires_compatibilities'] = ['FARGATE']
            args['network_mode'] = 'awsvpc'

        if self.cpu is not None:
            args['cpu'] = self.cpu
        if self.memory is not None:
            args['memory'] = self.memory

        return args


class TFAWSServiceDiscoveryNamespace(AWSTerraformResource):
    pass


class TFAWSServiceDiscoveryPrivateDnsNamespace(TFAWSServiceDiscoveryNamespace):
    def __init__(
            self,
            tf_name,
            *,
            name: str,
            description: Optional[str] = None,
            vpc: TFAWSVpc,
    ):
        super().__init__('aws_service_discovery_private_dns_namespace', tf_name)
        self.name = name
        self.vpc = vpc
        self.description = description

    def get_args(self) -> Dict[str, any]:
        args = {
            'name': self.name,
            'vpc': self.vpc.get_arg_ref('id'),
        }

        if self.description is not None:
            args['description'] = self.description

        return args


class TFAWSServiceDiscoveryService(TFAWSServiceDiscoveryNamespace):
    def __init__(
            self,
            tf_name,
            *,
            name: str,
            namespace: TFAWSServiceDiscoveryNamespace,
            dns_ttl: int,
            dns_type: str,
    ):
        super().__init__('aws_service_discovery_service', tf_name)
        self.name = name
        self.namespace = namespace
        self.dns_ttl = dns_ttl
        self.dns_type = dns_type

    def get_args(self) -> Dict[str, any]:
        return {
            'name': self.name,
            'dns_config': InlineBlock({
                'namespace_id': self.namespace.get_arg_ref('id'),
                'dns_records': InlineBlock(
                    ttl=self.dns_ttl,
                    type=self.dns_type,
                ),
            })
        }


@dataclass
class AWSServiceRegistry:
    service_discovery: TFAWSServiceDiscoveryService
    port: Optional[int] = None
    container_port: Optional[int] = None
    container_name: Optional[str] = None


class TFAWSECSService(AWSTerraformResource):
    def __init__(
            self,
            tf_name,
            *,
            name: str,
            cluster: TFAWSECSCluster,
            task_definition: TFAWSECSTaskDefinition,
            desired_count: int,
            service_registry: Optional[AWSServiceRegistry] = None,
    ):
        super().__init__('aws_ecs_service', tf_name)
        self.name = name or tf_name
        self.cluster = cluster
        self.task_definition = task_definition
        self.desired_count = desired_count
        self.service_registry = service_registry

    def get_args(self) -> Dict[str, any]:
        args = {
            'name': self.name,
            'cluster': self.cluster.get_arg_ref('id'),
            'task_definition': self.task_definition.get_self_ref(),
            'desired_count': self.desired_count,
        }

        if self.service_registry is not None:
            sr = self.service_registry
            sr_dict = {
                'registry_arn': sr.service_discovery.get_arg_ref('arn'),
            }
            if sr.port is not None:
                sr_dict['port'] = sr.port
            if sr.port is not None:
                sr_dict['port'] = sr.port
            if sr.container_port is not None:
                sr_dict['container_port'] = sr.container_port
            if sr.container_name is not None:
                sr_dict['container_name'] = sr.container_name

            args['service_registries'] = InlineBlock(sr_dict)

        return args


class TFAWSECRImageData(AWSTerraformDataSource):
    def __init__(self, tf_name: str, *, repository_name: str, image_tag: str):
        super().__init__('aws_ecr_image', tf_name)
        self.repository_name = repository_name
        self.image_tag = image_tag

    def get_args(self) -> Dict[str, any]:
        return {
            'repository_name': self.repository_name,
            'image_tag': self.image_tag,
        }
