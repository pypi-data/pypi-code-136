from typing import List, Union
import requests, json
from ddd_objects.infrastructure.ao import exception_class_dec
from ddd_objects.infrastructure.repository_impl import error_factory
from ddd_objects.domain.exception import return_codes
from .do import (
    ConditionDO,
    ConfigMapDO,
    ConfigMapUserSettingDO,
    DeploymentDO,
    IngressDO,
    InstanceInfoDO,
    InstanceTypeWithStatusDO,
    JobDO,
    JobSettingDO,
    NamespaceDO,
    NodeCreationItemDO,
    NodeCreationRequestDO,
    NodeInfoDO,
    NodeMetaDO, 
    NodeUserSettingDO,
    PersistentVolumeClaimDO,
    PersistentVolumeDO,
    PodContainerDO,
    PodDO,
    PodLogSettingDO,
    PodOSSOperationInfoDO,
    ResourceOSSSettingDO,
    SecretDO,
    SecretUserSettingDO,
    ServiceDO,
    StorageClassDO
)

class K3SController:
    def __init__(self, ip: str, port: int, token: str) -> None:
        self.url = f"http://{ip}:{port}"
        self.header = {"api-token":token}

    def _check_error(self, status_code, info):
        if status_code>299:
            if isinstance(info['detail'], str):
                return_code = return_codes['OTHER_CODE']
                error_traceback = info['detail']
            else:
                return_code = info['detail']['return_code']
                error_traceback = info['detail']['error_traceback']
            raise error_factory.make(return_code)(error_traceback)

    @exception_class_dec(max_try=1)
    def check_connection(self, timeout=3):
        response=requests.get(f'{self.url}', headers=self.header, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        if info['message']=='Hello World':
            return True
        else:
            return False

    @exception_class_dec(max_try=1)
    def create_node(self, condition: ConditionDO, node_user_setting: NodeUserSettingDO, timeout=1200):
        data = {
            "condition": condition.dict(),
            "node_user_setting": node_user_setting.dict()
        }
        data = json.dumps(data)
        response=requests.post(f'{self.url}/node', headers=self.header, data=data, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        if infos is None:
            return None
        else:
            return [NodeInfoDO(**info) for info in infos]

    @exception_class_dec(max_try=1)
    def delete_nodes(self, node_infos: List[Union[NodeInfoDO, NodeMetaDO]], timeout=60):
        data = [info.dict() for info in node_infos]
        data = json.dumps(data)
        response=requests.delete(f'{self.url}/nodes', headers=self.header, data=data, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec(max_try=1)
    def get_instance_info_by_node_meta(self, region_id: str, node_meta: NodeMetaDO, timeout=300):
        data = json.dumps(node_meta.dict())
        response=requests.get(f'{self.url}/instance/region_id/{region_id}/node_meta', 
            headers=self.header, data=data, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        instance_info, instance_type_info = info
        instance_info = InstanceInfoDO(**instance_info)
        instance_type_info = InstanceTypeWithStatusDO(**instance_type_info)
        return instance_info, instance_type_info

    @exception_class_dec(max_try=1)
    def get_existing_nodes(self, cluster_name: str, timeout=300):
        response=requests.get(f'{self.url}/nodes/cluster_name/{cluster_name}', 
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        return [NodeInfoDO(**info) for info in infos]

    @exception_class_dec(max_try=1)
    def get_existing_nodes_by_name(self, node_name:str, timeout=300):
        response=requests.get(f'{self.url}/nodes/node_name/{node_name}', 
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        return [NodeInfoDO(**info) for info in infos]

    @exception_class_dec(max_try=1)
    def get_node_metas(self, cluster_name: str, timeout=7):
        response=requests.get(f'{self.url}/node_metas/cluster_name/{cluster_name}', 
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        return [NodeMetaDO(**meta) for meta in infos]

    @exception_class_dec(max_try=1)
    def add_node_label(self, node_infos: List[NodeInfoDO], key: str, value: str, timeout=30):
        data = [info.to_json() for info in node_infos]
        data = json.dumps(data)
        response=requests.post(f'{self.url}/label/key/{key}/value/{value}', 
            headers=self.header, data=data, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        return infos

    @exception_class_dec(max_try=1)
    def get_namespaces(self, cluster_name: str, timeout=30):
        response=requests.get(f'{self.url}/namespaces/cluster_name/{cluster_name}', 
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        if infos is None:
            return None
        else:
            return [NamespaceDO(**namespace) for namespace in infos]

    @exception_class_dec(max_try=1)
    def create_namespace(self, cluster_name: str, namespace_name: str, timeout=30):
        response=requests.post(
            f'{self.url}/namespace/cluster_name/{cluster_name}/namespace_name/{namespace_name}', 
            headers=self.header, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec(max_try=1)
    def create_secrets(
        self, 
        cluster_name: str, 
        secret_user_settings: List[SecretUserSettingDO],
        timeout=300
    ):
        data = [setting.to_json() for setting in secret_user_settings]
        data = json.dumps(data)
        response=requests.post(
            f'{self.url}/secrets/cluster_name/{cluster_name}', 
            headers=self.header, data=data, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec(max_try=1)
    def get_secrets(self, cluster_name: str, namespace_name: str, timeout=30):
        response=requests.get(
            f'{self.url}/secrets/cluster_name/{cluster_name}/namespace_name/{namespace_name}', 
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        if infos is None:
            return None
        else:
            return [SecretDO(**s) for s in infos]

    @exception_class_dec(max_try=1)
    def create_config_maps(
        self, 
        cluster_name: str, 
        config_map_user_settings: List[ConfigMapUserSettingDO],
        timeout=300
    ):
        data = [setting.to_json() for setting in config_map_user_settings]
        data = json.dumps(data)
        response=requests.post(
            f'{self.url}/config_maps/cluster_name/{cluster_name}', 
            headers=self.header, data=data, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec(max_try=1)
    def get_config_maps(self, cluster_name:str, namespace_name:str, timeout=30):
        response=requests.get(
            f'{self.url}/config_maps/cluster_name/{cluster_name}/namespace_name/{namespace_name}', 
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        if infos is None:
            return None
        else:
            return [ConfigMapDO(**s) for s in infos]

    @exception_class_dec(max_try=1)
    def create_resource_from_oss(self, cluster_name:str, target_paths:List[str], timeout=60):
        resource_oss_setting = ResourceOSSSettingDO(
            cluster_name=cluster_name, target_paths=target_paths)
        data = json.dumps(resource_oss_setting.to_json())
        response=requests.post(
            f'{self.url}/resource/oss', 
            headers=self.header, data=data, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec(max_try=1)
    def delete_resource_from_oss(self, cluster_name: str, target_paths: List[str], timeout=60):
        resource_oss_setting = ResourceOSSSettingDO(
            cluster_name=cluster_name, target_paths=target_paths)
        data = json.dumps(resource_oss_setting.to_json())
        response=requests.delete(
            f'{self.url}/resource/oss', 
            headers=self.header, data=data, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec(max_try=1)
    def get_deployments(self, cluster_name:str, namespace_name:str, timeout=30):
        response=requests.get(
            f'{self.url}/deployments/cluster_name/{cluster_name}/namespace_name/{namespace_name}', 
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        if infos is None:
            return None
        else:
            return [DeploymentDO(**s) for s in infos]

    @exception_class_dec(max_try=1)
    def get_ingresses(self, cluster_name:str, namespace_name:str, timeout=30):
        response=requests.get(
            f'{self.url}/ingresses/cluster_name/{cluster_name}/namespace_name/{namespace_name}', 
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        if infos is None:
            return None
        else:
            return [IngressDO(**s) for s in infos]

    @exception_class_dec(max_try=1)
    def get_pods(self, cluster_name:str, namespace_name:str, timeout=30):
        response=requests.get(
            f'{self.url}/pods/cluster_name/{cluster_name}/namespace_name/{namespace_name}', 
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        if infos is None:
            return None
        else:
            return [PodDO(**s) for s in infos]

    @exception_class_dec(max_try=1)
    def delete_pod(self, cluster_name:str, namespace_name:str, pod_name:str, timeout=5):
        response=requests.delete(
            f'{self.url}/pod/cluster_name/{cluster_name}/namespace_name/{namespace_name}/pod_name/{pod_name}', 
            headers=self.header, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec(max_try=1)
    def upload_to_oss_from_pod(self, pod_oss_operation_info: PodOSSOperationInfoDO, timeout=1200):
        data = json.dumps(pod_oss_operation_info.to_json())
        response=requests.post(
            f'{self.url}/oss/pod', 
            headers=self.header, data=data, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec(max_try=1)
    def get_services(self, cluster_name:str, namespace_name:str, timeout=30):
        response=requests.get(
            f'{self.url}/services/cluster_name/{cluster_name}/namespace_name/{namespace_name}', 
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        if infos is None:
            return None
        else:
            return [ServiceDO(**s) for s in infos]

    @exception_class_dec(max_try=1)
    def get_pod_containers(self, cluster_name:str, namespace_name:str, timeout=30):
        response=requests.get(
            f'{self.url}/pod_containers/cluster_name/{cluster_name}/namespace_name/{namespace_name}', 
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        if infos is None:
            return None
        else:
            return [PodContainerDO(**s) for s in infos]

    @exception_class_dec(max_try=1)
    def get_jobs(self, cluster_name:str, namespace_name:str, timeout=10):
        response=requests.get(
            f'{self.url}/jobs/cluster_name/{cluster_name}/namespace_name/{namespace_name}', 
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        if infos is None:
            return None
        else:
            return [JobDO(**s) for s in infos]
        
    @exception_class_dec(max_try=1)
    def create_job(self, cluster_name:str, job_setting:JobSettingDO, timeout=10):
        data = json.dumps(job_setting.dict())
        response=requests.post(
            f'{self.url}/job/cluster_name/{cluster_name}', 
            headers=self.header, data=data, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        if info is None:
            return None
        else:
            return JobDO(**info)
    
    @exception_class_dec(max_try=1)
    def get_pod_log(
        self, 
        cluster_name:str,
        pod_log_setting: PodLogSettingDO,
        timeout:int=10
    ):
        data = json.dumps(pod_log_setting.to_json())
        response=requests.get(
            f'{self.url}/log/cluster_name/{cluster_name}', 
            headers=self.header, data=data,timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec(max_try=1)
    def delete_job(
        self,
        cluster_name:str,
        namespace_name:str,
        job_name:str,
        timeout:int=10
    ):
        response=requests.delete(
            f'{self.url}/job/cluster_name/{cluster_name}/namespace_name/{namespace_name}/job_name/{job_name}', 
            headers=self.header, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec(max_try=1)
    def create_storage_class(
        self,
        cluster_name: str,
        storage_class: StorageClassDO,
        timeout: int = 3
    ):
        data = json.dumps(storage_class.dict())
        response = requests.post(
            f'{self.url}/storage_class/cluster_name/{cluster_name}',
            headers=self.header, data=data, timeout=timeout
        )
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec(max_try=1)
    def delete_storage_class(
        self,
        cluster_name: str,
        storage_class_name: str,
        timeout: int = 3
    ):
        response = requests.delete(
            f'{self.url}/storage_class/cluster_name/{cluster_name}/storage_class_name/{storage_class_name}',
            headers=self.header, timeout=timeout
        )
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec(max_try=1)
    def create_persistent_volume(
        self,
        cluster_name: str,
        persistent_volume: PersistentVolumeDO,
        timeout: int = 3
    ):
        data = json.dumps(persistent_volume.dict())
        response = requests.post(
            f'{self.url}/persistent_volume/cluster_name/{cluster_name}',
            headers=self.header, data=data, timeout=timeout
        )
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec(max_try=1)
    def delete_persistent_volume(
        self,
        cluster_name: str,
        persistent_volume_name: str,
        timeout: int = 3
    ):
        response = requests.delete(
            f'{self.url}/persistent_volume/cluster_name/{cluster_name}/persistent_volume_name/{persistent_volume_name}',
            headers=self.header, timeout=timeout
        )
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec(max_try=1)
    def create_persistent_volume_claim(
        self,
        cluster_name: str,
        persistent_volume_claim: PersistentVolumeClaimDO,
        timeout: int = 3
    ):
        data = json.dumps(persistent_volume_claim.dict())
        response = requests.post(
            f'{self.url}/persistent_volume_claim/cluster_name/{cluster_name}',
            headers=self.header, data=data, timeout=timeout
        )
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec(max_try=1)
    def delete_persistent_volume_claim(
        self,
        cluster_name: str,
        namespace_name: str,
        persistent_volume_claim_name: str,
        timeout: int = 3
    ):
        response = requests.delete(
            f'{self.url}/persistent_volume_claim/cluster_name/{cluster_name}/namespace_name/{namespace_name}/persistent_volume_claim_name/{persistent_volume_claim_name}',
            headers=self.header, timeout=timeout
        )
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec()
    def send_node_creation_request(self, request: NodeCreationRequestDO, timeout=3):
        data = json.dumps(request.dict())
        response=requests.post(f'{self.url}/node/request', 
            headers=self.header, data=data, timeout=timeout)
        id = json.loads(response.text)
        self._check_error(response.status_code, id)
        if id is None:
            return None
        else:
            return id

    @exception_class_dec()
    def find_node_creation_item(self, id: str, timeout=3):
        response=requests.get(f'{self.url}/node/item/id/{id}', 
            headers=self.header, timeout=timeout)
        item = json.loads(response.text)
        self._check_error(response.status_code, item)
        if item is None:
            return None
        else:
            return NodeCreationItemDO(**item)

    @exception_class_dec()
    def find_unprocessed_node_creation_item(self, timeout=3):
        response=requests.get(f'{self.url}/node/item/unprocessed', 
            headers=self.header, timeout=timeout)
        item = json.loads(response.text)
        self._check_error(response.status_code, item)
        if item is None:
            return None
        else:
            return NodeCreationItemDO(**item)

    @exception_class_dec()
    def update_node_creation_item(self, item:NodeCreationItemDO, timeout=10):
        data = json.dumps(item.dict())
        response=requests.put(f'{self.url}/node/item', 
            headers=self.header, data=data, timeout=timeout)
        succeed = json.loads(response.text)
        self._check_error(response.status_code, succeed)
        return succeed

    @exception_class_dec()
    def clear_node_creation_item(self, timeout=3):
        response=requests.get(f'{self.url}/node/item/clear', 
            headers=self.header, timeout=timeout)
        n = json.loads(response.text)
        self._check_error(response.status_code, n)
        return n

    @exception_class_dec()
    def delete_node_creation_item(self, item_id:str, timeout=3):
        response=requests.delete(f'{self.url}/node/item/id/{item_id}', 
            headers=self.header, timeout=timeout)
        succeed = json.loads(response.text)
        self._check_error(response.status_code, succeed)
        return succeed

