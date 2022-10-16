import hashlib
import inspect
import logging
import os.path
from collections import defaultdict
from typing import Optional, List

from myc.common import SERVICE_ENV_VAR
from myc.endpoint import Endpoint, FunctionEndpoint, RestFunctionEndpoint, FastAPIFunctionEndpoint
from myc.ledger import LedgerPostEntry, S3Ledger

from myccli.config import MyceliumConfiguration, LOGGER_NAME, DEFAULT_DIST_DIR, PRIVATE_NS_DOMAIN
from myccli.packager import PackagingConfig, PackagerFactory
from myccli.platform import PlatformSelector, PlatformMapping, AWSLambdaPlatform, Platform, AWSECSPlatform
from myccli.scanner import Scanner
from myccli.terraform import TerraformFile
from myccli.terraform.provider import create_default_provider_registry
from myccli.terraform.resources import TFAWSIAMRole, TFAWSIAMPolicy, TFAWSIAMRolePolicyAttachment, \
    TFAWSLambdaFunction, TFAWSLambdaFunctionURL, TFAWSCloudwatchLogGroup, TFAWSS3Bucket, TFAWSS3Object, \
    TFAWSECRRepository, TFAWSECSCluster, TFAWSECSTaskDefinition, AWSECSContainerDefinition, AWSECSPortMapping, \
    TFAWSECSService, TFAWSAutoScalingGroup, TFAWSLaunchConfiguration, TFAWSECSCapacityProvider, \
    TFAWSECSClusterCapacityProviders, TFAWSIAMInstanceProfile, AWSECSLogConfiguration, AWSECSLogConfigurationOptions, \
    TFAWSSecurityGroup, AWSSecurityGroupRule, TFAWSECRImageData, TFAWSVpc, TFAWSSubnet, TFAWSInternetGateway, \
    TFAWSRouteTable, AWSRouteTableRoute, TFAWSRouteTableAssociation, TFAWSServiceDiscoveryPrivateDnsNamespace, \
    TFAWSServiceDiscoveryService, AWSServiceRegistry
from myccli.terraform.resources.docker import TFBuildDockerImage
from myccli.terraform.resources.null import TFNull

logger = logging.getLogger(LOGGER_NAME)


class Compiler:
    def __init__(self, project_path: str, app_path: str, config: MyceliumConfiguration):
        self._config = config
        self._project_path = project_path
        self._app_path = app_path
        self._project_hash = hashlib.sha1((self._project_path + ':' + self._app_path).encode('utf-8')).hexdigest()[:8]

        self._scanner = Scanner(project_path, app_path)
        self._compiled_endpoints: Optional[List[Endpoint]] = None
        self._endpoint_to_package = {}
        self._platform_selection: Optional[PlatformMapping] = None

        self._packager_factory = PackagerFactory()
        self._dist_dir = DEFAULT_DIST_DIR

        # in the future add providers dynamically
        self._tf = TerraformFile(create_default_provider_registry(config))
        self._tf_vpc = None
        self._tf_public_subnets = []
        self._tf_sd_private_namespace = None
        self._tf_ecs_cluster = None
        self._tf_ecs_services = {}
        self._tf_ecr_image_data = None
        self._ecs_ecr_path = None

        self._tf_ledger_bucket = None
        self._tf_ledger_platforms_obj = None
        self._endpoint_ledger_map = {}

    def _scan(self):
        logger.debug('Analyzing application...')
        app = self._scanner.scan()

        self._compiled_endpoints = app.compile_endpoints()
        logger.debug(f'    Found {len(self._compiled_endpoints)} endpoints')

    def _select_platforms(self):
        logger.debug('Performing platform selection for endpoints...')
        selector = PlatformSelector(self._compiled_endpoints)
        self._platform_selection = selector.select()
        logger.debug('    Done')

    def _create_packages(self):
        # divide endpoints into services
        service_map = defaultdict(list)
        for endpoint in self._compiled_endpoints:
            service_map[endpoint.service].append(endpoint)

        package_path_map = defaultdict(list)

        # create a package for each service
        logger.debug('Creating packages...')
        for endpoint in self._compiled_endpoints:
            platform = self._platform_selection.get_endpoint_platform(endpoint)
            packager = self._packager_factory.create_for_platform(platform)
            package_path = packager.wrap_package(PackagingConfig(
                root_dir=self._project_path,
                out_dir=os.path.join(self._dist_dir, 'packages'),
                use_local_myc=True,
            ))

            self._endpoint_to_package[endpoint] = package_path
            package_path_map[package_path].append(endpoint)

        for package_path, endpoints in package_path_map.items():
            logger.debug(f'    Package {package_path} with endpoints:')
            for endpoint in endpoints:
                endpoint_id = self._scanner.app.endpoint_registry.get_endpoint_id(endpoint)
                logger.debug(f'       - {endpoint_id}')

    def _determine_object_module_import_path(self, obj):
        function_file_path = os.path.abspath(inspect.getfile(obj))
        rel_path = os.path.relpath(function_file_path, os.path.abspath(self._project_path))
        parts = os.path.normpath(rel_path).split('/')

        if parts:
            parts[-1] = os.path.splitext(parts[-1])[0]  # remove.py
            if parts and parts[-1] == '__init__':
                parts.pop()

        return '.'.join(parts)

    def _register_endpoint_in_ledger(self, endpoint: Endpoint, platform: Platform, extra):
        endpoint_id = self._scanner.app.endpoint_registry.get_endpoint_id(endpoint)

        if isinstance(endpoint, RestFunctionEndpoint):
            entry = LedgerPostEntry(
                platform_entry=platform.make_ledger_entry(endpoint_id),
                protocol='http',
                extra=extra,
            )
        else:
            raise NotImplementedError

        self._endpoint_ledger_map[endpoint] = entry

    def _generate_tf_for_aws_ecs_endpoint(self, endpoint: FunctionEndpoint, platform: AWSECSPlatform):
        # determine route
        if isinstance(endpoint, FastAPIFunctionEndpoint):
            route_path = endpoint.route.path
        else:
            raise NotImplementedError

        # create post entry
        qualified_service_name = f'{endpoint.service.name}.{PRIVATE_NS_DOMAIN}'
        self._register_endpoint_in_ledger(
            endpoint,
            platform,
            extra={
                'service': qualified_service_name,
                'route': route_path,
            }
        )

        if endpoint.service.name in self._tf_ecs_services:
            # ECS infrastructure for this service has already been generated
            return

        # create cluster if not already created
        cluster_name = f'mycelium-{hashlib.sha1(self._project_path.encode("utf-8")).hexdigest()[:8]}'
        if self._tf_ecs_cluster is None:
            package_path = self._endpoint_to_package[endpoint]
            context_path = os.path.abspath(package_path)

            image_name = 'mycelium'
            image_tag = 'latest'

            # create resource that builds the docker image for the endpoint
            docker_image = self._tf.add_item(TFBuildDockerImage(
                image_name + '_docker_image',
                name=image_name,
                context_path=context_path,
                tags=[image_tag],
                ))

            # create an appropriate ECR repository to hold the built docker image
            ecr_repo = self._tf.add_item(TFAWSECRRepository(
                image_name + '_ecr_repo',
                name=image_name,
                mutable=True,
                force_delete=True,
                ))

            # create null resource that will deploy to ECR
            self._ecs_ecr_path = f'{self._config.aws_account_id}.dkr.ecr.{self._config.aws_region}.amazonaws.com/{image_name}:{image_tag}'
            ecr_push = self._tf.add_item(TFNull(
                image_tag + '_push_to_ecr',
                commands=[
                    f'docker tag {image_name}:{image_tag} {self._ecs_ecr_path}',
                    f'docker push {self._ecs_ecr_path}',
                ]
            ))
            ecr_push.add_dependency(ecr_repo)
            ecr_push.add_dependency(docker_image)
            ecr_push.add_trigger('image_id', docker_image.get_arg_ref('image_id'))

            # create data source that we will use to fetch the latest docker image digest
            self._tf_ecr_image_data = self._tf.add_item(TFAWSECRImageData(
                image_name + '_ecr_image',
                repository_name=image_name,
                image_tag=image_tag
            ))
            self._tf_ecr_image_data.add_dependency(ecr_push)

            # create ec2 instance profile
            ec2_instance_role = self._tf.add_item(TFAWSIAMRole(
                cluster_name + '_ec2_instance_role',
                assume_role_policy=TFAWSIAMRole.create_default_assume_role_policy('ec2.amazonaws.com'),
            ))
            self._tf.add_item(TFAWSIAMRolePolicyAttachment(
                cluster_name + '_add_policy',
                role=ec2_instance_role,
                policy_arn='arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role'
            ))
            instance_profile = self._tf.add_item(TFAWSIAMInstanceProfile(
                cluster_name + '_instance_profile',
                role=ec2_instance_role,
            ))

            # allow ec2 role to access ledger bucket
            ledger_access_policy = self._tf.add_item(TFAWSIAMPolicy(
                cluster_name + '_ledger_policy',
                policy={
                    'Version': '2012-10-17',
                    'Statement': [
                        {
                            'Action': [
                                's3:*',
                            ],
                            'Effect': 'Allow',
                            'Resource': f'${{{self._tf_ledger_bucket.get_self_ref()}}}/*',
                        }
                    ]
                }
            ))
            self._tf.add_item(TFAWSIAMRolePolicyAttachment(
                cluster_name + '_ledger_access_policy_attachment',
                role=ec2_instance_role,
                policy=ledger_access_policy,
            ))

            # create security group for instances in autoscaling group
            sg = self._tf.add_item((TFAWSSecurityGroup(
                cluster_name + '_sg',
                description='Cluster EC2 instance security group (automatically generated)',
                ingress=[AWSSecurityGroupRule('Allow HTTP from Internet', from_port=80, to_port=80, protocol='tcp', cidr_blocks=['0.0.0.0/0'])],
                egress=[AWSSecurityGroupRule('Allow All Outbound', from_port=0, to_port=0, cidr_blocks=['0.0.0.0/0'])],
                vpc=self._tf_vpc,
            )))

            # create autoscaling group
            # FIXME: use latest AMI using data source
            launch_conf = self._tf.add_item(TFAWSLaunchConfiguration(
                cluster_name + '_asg_lc',
                image_id='ami-0319b5b60d7feac49',
                instance_type='t3.micro',
                cluster_name=cluster_name,
                iam_instance_profile=instance_profile,
                security_groups=[sg]
            ))
            launch_conf.lifecycle.create_before_destroy = True

            machine_count = self._platform_selection.count_unique(AWSECSPlatform)
            asg = self._tf.add_item(TFAWSAutoScalingGroup(
                cluster_name + '_asg',
                min_size=1,
                max_size=machine_count,
                desired_capacity=machine_count,
                launch_configuration=launch_conf,
                vpc_subnets=self._tf_public_subnets[:1],
            ))
            asg.lifecycle.create_before_destroy = True

            # create capacity provider
            capacity_provider = self._tf.add_item(TFAWSECSCapacityProvider(
                cluster_name + '_capacity_provider',
                asg=asg,
            ))

            # create cluster
            self._tf_ecs_cluster = self._tf.add_item(TFAWSECSCluster(cluster_name))

            # attach capacity provider to cluster
            self._tf.add_item(TFAWSECSClusterCapacityProviders(
                cluster_name + '_cluster_capacity_providers',
                cluster=self._tf_ecs_cluster,
                provider=capacity_provider,
                weight=100,
            ))

            # create service discovery stuff
            self._tf_sd_private_namespace = self._tf.add_item(TFAWSServiceDiscoveryPrivateDnsNamespace(
                cluster_name + '_sd_private',
                name=PRIVATE_NS_DOMAIN,
                vpc=self._tf_vpc,
            ))

        # create task execution role
        execution_role = self._tf.add_item(TFAWSIAMRole(
            f'{cluster_name}_{endpoint.service.name}_execution_role',
            assume_role_policy=TFAWSIAMRole.create_default_assume_role_policy('ecs-tasks.amazonaws.com')
        ))

        # attach AmazonECSTaskExecutionRolePolicy policy to task execution role
        self._tf.add_item(TFAWSIAMRolePolicyAttachment(
            execution_role.tf_name + '_policy',
            role=execution_role,
            policy_arn='arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy'
        ))

        # create log group
        log_group = self._tf.add_item(TFAWSCloudwatchLogGroup(
            cluster_name + f'_{endpoint.service.name}_log_group',
            name=cluster_name + f'-{endpoint.service.name}-log-group',
            retention_in_days=7,
        ))

        if isinstance(endpoint, FastAPIFunctionEndpoint):
            fastapi_path = f'{self._app_path}._services_object.{endpoint.service.name}.fastapi'
        else:
            raise NotImplementedError

        # create task definition for the service
        task_def_family = f'{cluster_name}-{endpoint.service.name}'
        http_container_name = endpoint.service.name
        task_def = self._tf.add_item(TFAWSECSTaskDefinition(
            f'{cluster_name}_{endpoint.service.name}_task_def',
            family=task_def_family,
            execution_role=execution_role,
            fargate=False,
            cpu=256,
            memory=512,
            container_definitions=[
                AWSECSContainerDefinition(
                    name=http_container_name,
                    image=self._ecs_ecr_path + f'@${{{self._tf_ecr_image_data.get_arg_ref("image_digest")}}}',
                    essential=True,
                    command=['uvicorn', fastapi_path, '--host', '0.0.0.0', '--port', '80', '--interface', 'asgi3'],
                    port_mappings=[
                        AWSECSPortMapping(container_port=80, host_port=80),
                    ],
                    log_configuration=AWSECSLogConfiguration(
                        log_driver='awslogs',
                        options=AWSECSLogConfigurationOptions(
                            group=log_group.get_arg_ref('name'),
                            region=self._config.aws_region,
                            stream_prefix='ecs',
                        )
                    ),
                    environment={
                        S3Ledger.LEDGER_BUCKET_ENV_VAR: self._tf_ledger_bucket.get_arg_ref('bucket'),
                        SERVICE_ENV_VAR: endpoint.service.name,
                    }
                )
            ],
        ))
        task_def.dependencies.append(log_group)

        # create a service for this endpoint
        sd = self._tf.add_item(TFAWSServiceDiscoveryService(
            cluster_name + '_' + endpoint.service.name + '__sd',
            name=endpoint.service.name,
            namespace=self._tf_sd_private_namespace,
            dns_type='SRV',
            dns_ttl=30,
        ))
        service = self._tf.add_item(TFAWSECSService(
            f'{cluster_name}_{endpoint.service.name}_service',
            name=endpoint.service.name,
            cluster=self._tf_ecs_cluster,
            task_definition=task_def,
            desired_count=1,
            service_registry=AWSServiceRegistry(
                service_discovery=sd,
                container_name=http_container_name,
                container_port=80,
            )
        ))

        service.add_dependency(self._tf_ledger_platforms_obj)

        self._tf_ecs_services[endpoint.service.name] = service

    def _generate_tf_for_aws_lambda_endpoint(self, endpoint: FunctionEndpoint, platform: AWSLambdaPlatform):
        # FIXME: handle name collisions
        lambda_name = platform.logical_id
        # function_name = endpoint.function.__name__
        function_name = platform.logical_id
        role_name = f'{lambda_name}_role'

        # find out import path for function
        handler = self._determine_object_module_import_path(endpoint.function) + '.' + endpoint.function.__name__

        # create role
        role = self._tf.add_item(TFAWSIAMRole(role_name))

        # create lambda function
        lfn = self._tf.add_item(TFAWSLambdaFunction(
            lambda_name,
            function_name=function_name,
            filename=os.path.relpath(self._endpoint_to_package[endpoint], self._dist_dir),
            role=role,
            runtime='python3.9',
            handler=handler,
            env={
                S3Ledger.LEDGER_BUCKET_ENV_VAR: self._tf_ledger_bucket.get_arg_ref('bucket'),
                SERVICE_ENV_VAR: endpoint.service.name,
            }
        ))

        # force lambda to be created only after the platform object is up
        lfn.add_dependency(self._tf_ledger_platforms_obj)

        # create log group
        self._tf.add_item(TFAWSCloudwatchLogGroup(
            lambda_name + '_log_group',
            name=f'/aws/lambda/${{{lfn.get_arg_ref("function_name")}}}',
            retention_in_days=7,
        ))

        # create policy that allows for logging
        log_policy = self._tf.add_item(TFAWSIAMPolicy(
            lambda_name + '_log_policy',
            policy={
                'Version': '2012-10-17',
                'Statement': [
                    {
                        'Action': [
                            'logs:CreateLogStream',
                            'logs:PutLogEvents',
                        ],
                        'Effect': 'Allow',
                        'Resource': 'arn:aws:logs:*:*:*',  # FIXME: too permissive
                    },
                    {
                        'Action': [
                            's3:*',
                        ],
                        'Effect': 'Allow',
                        'Resource': f'${{{self._tf_ledger_bucket.get_self_ref()}}}/*',
                    }
                ]
            }
        ))

        # attach log policy to lambda's role
        self._tf.add_item(TFAWSIAMRolePolicyAttachment(
            lambda_name + '_log_policy_attachment',
            role=role,
            policy=log_policy,
        ))

        # create URL endpoint
        lambda_url = self._tf.add_item(TFAWSLambdaFunctionURL(lambda_name + '_url', function=lfn))
        self._register_endpoint_in_ledger(
            endpoint,
            platform,
            extra={'url': lambda_url.get_arg_ref('function_url')}
        )

    def _generate_tf_for_endpoint(self, endpoint: Endpoint):
        platform = self._platform_selection.get_endpoint_platform(endpoint)
        if isinstance(platform, AWSLambdaPlatform):
            assert isinstance(endpoint, FunctionEndpoint)
            self._generate_tf_for_aws_lambda_endpoint(endpoint, platform)
        elif isinstance(platform, AWSECSPlatform):
            assert isinstance(endpoint, FunctionEndpoint)
            self._generate_tf_for_aws_ecs_endpoint(endpoint, platform)
        else:
            raise NotImplementedError

    def _generate_tf_for_ledger_bucket(self):
        """
        Creates the S3 bucket responsible for synchronizing between services.
        """
        self._tf_ledger_bucket = self._tf.add_item(TFAWSS3Bucket('ledger'))

    def _generate_tf_for_ledger_post(self):
        """
        Generates the S3 object that maps endpoints to their physical locations.
        The contents of this object are dynamically resolved by Terraform after
        the endpoints have been deployed to whatever platform is selected for them.
        """
        ep_registry = self._scanner.app.endpoint_registry
        content = {
            ep_registry.get_endpoint_id(endpoint): self._endpoint_ledger_map[endpoint].to_dict()
            for endpoint in self._compiled_endpoints
            if endpoint in self._endpoint_ledger_map
        }

        self._tf.add_item(
            TFAWSS3Object('ledger_post_file', bucket=self._tf_ledger_bucket, key=S3Ledger.LEDGER_POST_KEY,
                          content=content)
        )

    def _generate_tf_for_ledger_platforms(self):
        """
        Generates the S3 object that maps endpoints to their corresponding selected platform.
        """
        ep_registry = self._scanner.app.endpoint_registry

        content = {}
        for endpoint in self._compiled_endpoints:
            endpoint_id = ep_registry.get_endpoint_id(endpoint)
            content[endpoint_id] = self._platform_selection. \
                get_endpoint_platform(endpoint).make_ledger_entry(endpoint_id).to_dict()

        self._tf_ledger_platforms_obj = self._tf.add_item(
            TFAWSS3Object('ledger_platforms_file', bucket=self._tf_ledger_bucket, key=S3Ledger.LEDGER_PLATFORMS_KEY,
                          content=content)
        )

    def _generate_tf_for_vpc(self):
        # create vpc
        vpc_name = 'mycelium_' + self._project_hash
        self._tf_vpc = self._tf.add_item(TFAWSVpc(
            tf_name=vpc_name,
            cidr_block='10.0.0.0/16',
            name=f'Mycelium VPC {self._project_hash}',
        ))

        # create public subnet
        public_subnet = self._tf.add_item(TFAWSSubnet(
            tf_name=vpc_name + '_public',
            vpc=self._tf_vpc,
            cidr_block='10.0.0.0/17',
            name=f'Public Subnet {self._project_hash}',
            az=self._config.aws_region + 'a',
            map_public_ip_on_launch=True,
        ))
        self._tf_public_subnets.append(public_subnet)

        # create internet gateway
        ig = self._tf.add_item(TFAWSInternetGateway(
            vpc_name + '_ig',
            vpc=self._tf_vpc,
        ))

        # create route table for public subnet and attach internet gateway to it
        public_route_table = self._tf.add_item(TFAWSRouteTable(
            vpc_name + '_public_route_table',
            vpc=self._tf_vpc,
            routes=[
                AWSRouteTableRoute('0.0.0.0/0', 'gateway_id', ig.get_arg_ref('id'))
            ]
        ))
        self._tf.add_item(TFAWSRouteTableAssociation(
            vpc_name + '_public_route_table_assoc',
            subnet=public_subnet,
            route_table=public_route_table,
        ))

    def _generate_terraform(self):
        """
        Generates and writes out the infrastructure's terraform file(s).
        """
        logger.debug('Generating terraform code...')
        self._generate_tf_for_vpc()
        self._generate_tf_for_ledger_bucket()
        self._generate_tf_for_ledger_platforms()

        # create resources for required endpoints
        for endpoint in self._compiled_endpoints:
            self._generate_tf_for_endpoint(endpoint)

        self._generate_tf_for_ledger_post()

        # dump
        tf_path = os.path.join(self._dist_dir, 'main.tf')
        with open(tf_path, 'w') as f:
            self._tf.dump(f)

        logger.debug('    Done')

    def compile(self):
        self._scan()
        self._select_platforms()
        self._create_packages()
        self._generate_terraform()
