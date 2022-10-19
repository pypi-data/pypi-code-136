import boto3
import os
from amazon_ec2_best_instance import Ec2BestInstance

from .ami_type import AmiType
from .architecture import Architecture
from .ec2_os import Ec2Os


class Ec2:
    def __init__(self, options={}):
        self.__region = options.get('region',
                                    os.environ.get('AWS_REGION', os.environ.get('AWS_DEFAULT_REGION', 'us-east-1')))
        self.__ssm_client = boto3.client('ssm', region_name=self.__region)
        ec2_best_instance_options = {
            'region': self.__region,
            'describe_spot_price_history_concurrency': 20,
            'describe_on_demand_price_concurrency': 20,
        }

        if options is not None and options.get('clients') is not None and options['clients'].get('ec2') is not None:
            ec2_best_instance_options = {
                'clients': {
                    'ec2': options['clients']['ec2']
                }
            }

        self.__ec2_best_instance = Ec2BestInstance(ec2_best_instance_options)

    def get_image_id(self, options={}):
        ami_type = options.get('type', AmiType.ECS_OPTIMIZED.value)
        if options.get('instance_type') is not None and options.get('architecture') is None:
            instance_type = options['instance_type']
            architecture = Architecture.X86_64.value if not instance_type.startswith('a1') \
                                                        and 'g' not in instance_type[1:len(instance_type)].split('.')[
                                                            0] else Architecture.ARM64.value
        else:
            architecture = options.get('architecture', Architecture.X86_64.value)

        os = options.get('os', Ec2Os.LINUX_2.value)

        if ami_type == AmiType.ECS_OPTIMIZED.value:
            ssm_parameter_name = '/aws/service/ecs/optimized-ami/'
            if os == Ec2Os.LINUX_2.value:
                ssm_parameter_name += 'amazon-linux-2/'
            else:
                raise Exception(f'The {os} OS is not supported')
            if architecture == Architecture.X86_64.value:
                pass
            elif architecture == Architecture.ARM64.value:
                ssm_parameter_name += 'arm64/'
            else:
                raise Exception(f'The {architecture} architecture is not supported')
            ssm_parameter_name += 'recommended/image_id'
        else:
            raise Exception(f'The {ami_type} AMI type is not supported')

        response = self.__ssm_client.get_parameter(Name=ssm_parameter_name)

        image_id = response['Parameter']['Value']

        return image_id

    def get_optimal_instance_type(self, options):
        memory = options['memory']
        cpu = options['cpu']
        usage_class = options['usage_class']
        is_instance_storage_supported = options.get('is_instance_storage_supported')
        max_spot_interruption_frequency = options.get('max_spot_interruption_frequency')

        get_best_instance_types_input = {
            # Required.
            'vcpu': cpu,
            # Required.
            'memory_gb': memory,
            # Optional. Default: 'on-demand'. Values: 'spot'|'on-demand'
            'usage_class': usage_class,
            # Optional.
            'burstable': False,
            # Optional.
            'is_current_generation': True,
            # Optional. If this parameter is set to True, the method will return the instance type with the best price.
            'is_best_price': True,
        }

        if usage_class == 'spot' and max_spot_interruption_frequency is not None:
            get_best_instance_types_input['max_interruption_frequency'] = max_spot_interruption_frequency

        if is_instance_storage_supported is not None:
            get_best_instance_types_input['is_instance_storage_supported'] = is_instance_storage_supported

        response = self.__ec2_best_instance.get_best_instance_types(get_best_instance_types_input)

        return response

    def is_instance_storage_supported_for_instance_type(self, instance_type):
        return self.__ec2_best_instance.is_instance_storage_supported_for_instance_type(instance_type)

    @staticmethod
    def get_architecture(instance_type):
        return Architecture.X86_64.value if not instance_type.startswith('a1') \
                                            and 'g' not in instance_type[1:len(instance_type)].split('.')[
                                                0] else Architecture.ARM64.value
