import boto3
import time
import logging
import datetime


class Fsx:
    __FSX_DEPLOYING_TIMEOUT_IN_MINUTES = 5

    def __init__(self, options={}):
        if options.get('region') is not None:
            region = options['region']
            self.__clients = {
                'fsx': boto3.client('fsx', region_name=region),
                'ec2': boto3.client('ec2', region_name=region)
            }
            self.__region = region
        else:
            self.__clients = {
                'fsx': boto3.client('fsx'),
                'ec2': boto3.client('ec2')
            }
            self.__region = self.__clients['ec2'].meta.region_name

        if options.get('tags') is None:
            self.__tags = []
        else:
            self.__tags = list(map(lambda tag: {'Key': tag['Key'], 'Value': tag['Value']}, options.get('tags')))

        self.__unique_id = str(time.time()).replace('.', '')

        if options.get('logger'):
            self.__logger = options.get('logger')
        else:
            self.__logger = logging.getLogger()
            self.__logger.setLevel(logging.INFO)

    def describe_file_system(self, file_system_id):
        response = self.__clients['fsx'].describe_file_systems(FileSystemIds=[file_system_id])
        file_systems = response['FileSystems']
        if len(file_systems) == 0:
            raise Exception(f'The file system {file_system_id} not found')
        return file_systems[0]

    def create_fsx(self,
                   subnet_ids,
                   vpc_id,
                   storage_capacity=1200,
                   sg_ids=None,
                   source_security_group_id=None):
        source_security_group_id = source_security_group_id if source_security_group_id is not None else self.__create_source_security_group(vpc_id)
        sg_ids = sg_ids if sg_ids is not None else [self.__create_fsx_security_group(vpc_id, source_security_group_id)]

        file_system_id = self.__create_fsx(subnet_ids, sg_ids, storage_capacity)

        self.__wait_for_fsx_deploying(file_system_id)

        return {
            'file_system_id': file_system_id,
            'source_sg_id': source_security_group_id,
            'fsx_sg_ids': sg_ids
        }

    def __create_fsx_security_group(self, vpc_id: str, source_security_group_id: str) -> str:
        group_name = f'TemporaryFsxSecurityGroup{self.__unique_id}'
        create_security_group_response = self.__clients['ec2'].create_security_group(
            Description='A temporary Security Group for the FSX',
            GroupName=group_name,
            VpcId=vpc_id,
            TagSpecifications=[
                {
                    'ResourceType': 'security-group',
                    'Tags': [
                                {
                                    'Key': 'Name',
                                    'Value': group_name
                                },
                            ] + self.__tags
                },
            ],
        )

        group_id = create_security_group_response['GroupId']

        self.__clients['ec2'].authorize_security_group_ingress(
            GroupId=group_id,
            IpPermissions=[
                {
                    'FromPort': 988,
                    'IpProtocol': 'tcp',
                    'ToPort': 988,
                    'UserIdGroupPairs': [
                        {
                            'GroupId': source_security_group_id,
                        },
                        {
                            'GroupId': group_id,
                        }
                    ]
                },
                {
                    'FromPort': 1021,
                    'IpProtocol': 'tcp',
                    'ToPort': 1023,
                    'UserIdGroupPairs': [
                        {
                            'GroupId': source_security_group_id,
                        },
                        {
                            'GroupId': group_id,
                        }
                    ]
                }
            ]
        )

        return group_id

    def __create_source_security_group(self, vpc_id: str) -> str:
        group_name = f'TemporaryFsxSourceSecurityGroup{self.__unique_id}'
        create_security_group_response = self.__clients['ec2'].create_security_group(
            Description='A temporary Security Group for the FSX source',
            GroupName=group_name,
            VpcId=vpc_id,
            TagSpecifications=[
                {
                    'ResourceType': 'security-group',
                    'Tags': [
                                {
                                    'Key': 'Name',
                                    'Value': group_name
                                },
                            ] + self.__tags
                },
            ],
        )

        group_id = create_security_group_response['GroupId']

        return group_id

    def __wait_for_fsx_deploying(self, file_system_id: str) -> None:
        # 'AVAILABLE' | 'CREATING' | 'FAILED' | 'DELETING' | 'MISCONFIGURED' | 'UPDATING' | 'MISCONFIGURED_UNAVAILABLE'
        final_statuses = ['AVAILABLE', 'FAILED']

        status = self.__get_fsx_status(file_system_id)

        start_time = datetime.datetime.now()

        self.__logger.info(f'Waiting for the FSx {file_system_id} deploying')

        while True:
            now_time = datetime.datetime.now()
            diff = now_time - start_time
            diff_minutes = diff.total_seconds() / 60
            if diff_minutes > self.__FSX_DEPLOYING_TIMEOUT_IN_MINUTES:
                raise Exception(f'FSX {file_system_id} deploying timeout')
            if status in final_statuses:
                break
            time.sleep(10)
            status = self.__get_fsx_status(file_system_id)
            self.__logger.debug(f'Waiting for the FSx {file_system_id} deploying')

        self.__logger.info(f"The FSx {file_system_id} status: {status}")

    def __get_fsx_status(self, file_system_id: str) -> str:
        response = self.__clients['fsx'].describe_file_systems(FileSystemIds=[file_system_id])
        status = response['FileSystems'][0]['Lifecycle']
        return status

    def __create_fsx(self, subnet_ids, sg_ids, storage_capacity):
        response = self.__clients['fsx'].create_file_system(
            FileSystemType='LUSTRE',
            StorageCapacity=storage_capacity,
            StorageType='SSD',
            SubnetIds=subnet_ids,
            SecurityGroupIds=sg_ids,
            Tags=[
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            LustreConfiguration={
                'DeploymentType': 'SCRATCH_2',
                'DataCompressionType': 'NONE',
                # 'LogConfiguration': {
                #    'Level': 'WARN_ERROR',
                #    'Destination': f'arn:aws:logs:{self.region}:{self.account_id}:log-group:/aws/fsx/lustre:log-stream:fsx-${self.unique_id}'
                # }
            }
        )

        return response['FileSystem']['FileSystemId']
