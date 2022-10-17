from dataclasses import dataclass
from typing import List, Optional, Union
from ddd_objects.infrastructure.do import BaseDO
from pydantic import BaseModel

class ConditionDO(BaseModel):
    min_cpu_num: int = 1
    max_cpu_num: int = 1
    min_memory_size: int = 1
    max_memory_size: int = 1
    min_gpu_num: int = None
    max_gpu_num: int = None
    min_gpu_memory_size: int = None
    max_gpu_memory_size: int = None

class InstanceUserSettingDO(BaseModel):
    name: str
    password: str = '1234Abcd'
    amount: int = 1
    image_id: Optional[str] = None
    region_id: str
    internet_pay_type: Optional[str] = None
    bandwidth_in: int = 1
    bandwidth_out: int = 100
    user_data: Optional[str] = None
    disk_size: int = 20
    key_name: str = 'ansible'
    exclude_instance_types: List[str] = []
    inner_connection: bool = True

@dataclass
class InstanceTypeUserSettingDO(BaseDO):
    region_id: str
    zone_id: str
    instance_type_id: str

@dataclass
class InstanceTypeWithStatusDO(BaseDO):
    region_id: str
    zone_id: str
    instance_type_id: str
    cpu_number: int
    memory_size: float
    gpu_type: str
    gpu_number: int
    status: str
    status_category: str
    _life_time: int = 5

class InstanceInfoDO(BaseModel):
    id: str
    instance_type: str
    create_time: str
    name: str
    hostname: str
    pay_type: str
    public_ip: List[str]
    private_ip: str
    os_name: str
    price: float
    image_id: str
    region_id: str
    zone_id: str
    internet_pay_type: str
    bandwidth_in: str
    bandwidth_out: str
    security_group_id: List[str]
    expired_time: Optional[str]
    auto_release_time: Optional[str]
    status: str
    key_name: str
    _life_time: int = 5

@dataclass
class CommandSettingDO(BaseDO):
    command: Optional[str]=None
    forks: int=1
    timeout: int=3
    username: str='root'
    port: int=22
    password: Optional[str]=None
    inner_connection: bool=True
    module: str='shell'
    retries: int=3
    delay: float=0.1

@dataclass
class CommandResultDO(BaseDO):
    output: str
    instance_id: str
    instance_name: str
    ip: str
    succeed: bool
    _life_time: int=1

@dataclass
class OSSOperationInfoDO(BaseDO):
    name: str
    bucket_name: str
    local_path: str
    target_path: str
    endpoint: str
    with_tar: bool = False

@dataclass
class DNSRecordDO(BaseDO):
    domain_name: str
    subdomain: str
    value: str
    id: Optional[str]=None
    weight: Optional[int]=None
    dns_type: str='A'
    ttl: int=600
    priority: Optional[int]=None
    line: Optional[str]=None

@dataclass
class OSSObjectDO(BaseDO):
    name: str
    bucket_name: str
    endpoint: str
    version_ids: List[str]
    version_creation_times: Optional[List[int]]=None

class InstanceCreationRequestDO(BaseModel):
    instance_user_setting: InstanceUserSettingDO
    condition: ConditionDO

class InstanceCreationItemDO(BaseModel):
    id: str
    instance_creation_request: Optional[InstanceCreationRequestDO]
    status: str
    creation_time: str
    details: Optional[List[InstanceInfoDO]] = None
    entry_time: Optional[str] = None
    exit_time: Optional[str] = None
    _life_time: int=86400

class CommandContextDO(BaseModel):
    connection: str='smart'
    module_path: str='/usr/local/bin/ansible'
    forks: int= 1
    timeout: int=300 
    remote_user: str='root'
    ask_pass: bool = False 
    ssh_extra_args: Optional[str] = None
    sftp_extra_args: Optional[str] = None
    scp_extra_args: Optional[str] = None 
    ask_value_pass: bool = False
    listhosts: bool = False 
    listtasks: bool = False 
    listtags: bool = False
    syntax: bool = False
    ssh_common_args='-o StrictHostKeyChecking=no'
    become: Optional[str] = None
    become_method: Optional[str] = None
    become_user: str = 'root' 
    check: bool = False 
    diff: bool = False
    verbosity: int = 1

class CommandSettingDetailDO(BaseModel):
    command: Union[str, dict]
    module: str = 'shell'
    retries: int = 2
    timeout: int = 3
    delay: float = 0.1

class CommandHostDO(BaseModel):
    ip: str
    hostname: Optional[str] = None
    port: int = 22
    username: str = 'root'
    password: Optional[str] = None
    private_key_file: Optional[str] = None

class CommandRequestDO(BaseModel):
    commands: Union[List[str], List[CommandSettingDetailDO]]
    hosts: Union[List[str], List[CommandHostDO]]
    context: Optional[CommandContextDO] = None
    priority: int = 3
    timeout: int = 3

class CommandResponseDO(BaseModel):
    status: str
    ip: str
    message: Optional[str] = None
    exception: Optional[str] = None
    stdout: Optional[str] = None
    cmd: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    delta_time: Optional[str] = None
    stderr: Optional[str] = None
    entry_time: Optional[str] = None
    exit_time: Optional[str] = None

class CommandItemDO(BaseModel):
    id: str
    command_request: Optional[CommandRequestDO]
    creation_time: str
    status: str
    details: Optional[List[CommandResponseDO]] = None
    _life_time: int = 600
