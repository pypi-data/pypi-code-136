from copy import deepcopy
from typing import List, Dict
from pydigitalenergy.models import Result
from pydigitalenergy.cloudbroker import models
from pydigitalenergy.cloudbroker.endpoints import API_PATH
from pydigitalenergy.adapter import RestAdapter
from pydigitalenergy.basegroup import BaseGroup
from pydigitalenergy.exceptions import DigitalEnergyApiException


class Cloudbroker:
    def __init__(self, adapter: RestAdapter):
        self.computes = ComputeGroup(adapter)
        self.vms = VMGroup(adapter)
        self.stacks = StackGroup(adapter)
        self.nodes = NodeGroup(adapter)
        self.hosts = HostGroup(adapter)
        self.clusters = ClusterGroup(adapter)
        self.grids = GridGroup(adapter)
        self.data_centers = DataCenterGroup(adapter)
        self.storages = StorageEndpointGroup(adapter)
        self.images = IamgeGroup(adapter)
        self.disks = DiskGroup(adapter)
        self.networks = ExternalNetworkGroup(adapter)


class ComputeGroup(BaseGroup):
    """
    Compute Group
    """

    def list(self, include_deleted: bool = False, page: int = 0, size: int = 0) -> List[models.Compute]:
        """
        Get list of compute instances
        Page and size can be specified only together

        :param include_deleted: (optional)
            Whether add deleted compute instances or not
        :param page: (optional)
            Page number
        :param size: (optional)
            Amount of instances per page
        
        :return: 
            List of Compute objects
        """
        result = self._get_data(API_PATH['compute_list'], {'includedeleted': include_deleted, 'page': page, 'size': size})
        return [models.Compute(**compute) for compute in result.data]

    def get(self, compute_id: int, reason: str = '') -> models.Compute:
        """
        Get information about compute instance

        :param compute_id: 
            Compute instance identifier
        :param reason: (optional)
            Reason of action
        
        :return: 
            Compute object
        """
        result = self._get_data(API_PATH['compute_get'], {'computeId': compute_id, 'reason': reason})
        return models.Compute(**result.data)


class StackGroup(BaseGroup):
    """
    Stack Group
    """

    def list(self, enabled: bool = True, page: int = 0, size: int = 0) -> List[models.Stack]:
        """
        Get list of stack instances
        Page and size can be specified only together

        :param enabled: (optional)
            Whether to show only enabled stacks or all of them
        :param page: (optional)
            Page number
        :param size: (optional)
            Amount of instances per page
        
        :return: 
            List of Stack objects
        """
        result = self._get_data(API_PATH['stack_list'], {'enabled': enabled, 'page': page, 'size': size})
        return [models.Stack(**stack) for stack in result.data]

    def get(self, stack_id: int) -> models.Stack:
        """
        Get information about stack instance

        :param stack_id: 
            Stack instance identifier

        :return: 
            Stack object
        """
        result = self._get_data(API_PATH['stack_get'], {'stackId': stack_id})
        return models.Stack(**result.data)


class NodeGroup(BaseGroup):
    """
    Node Group
    """

    def list(self, page: int = 0, size: int = 0) -> List[models.Node]:
        """
        Get list of node instances
        Page and size can be specified only together

        :param page: (optional)
            Page number
        :param size: (optional)
            Amount of instances per page
        
        :return: 
            List of Node objects
        """
        result = self._get_data(API_PATH['node_list'], {'page': page, 'size': size})
        return [models.Node(**node) for node in result.data]

    def get(self, node_id: int) -> models.Node:
        """
        Get information about node instance

        :param node_id: 
            Node instance identifier

        :return: 
            Node object
        """
        result = self._get_data(API_PATH['node_get'], {'nid': node_id})
        return models.Node(**result.data)


class BaseClusterGroup(BaseGroup):
    """
    
    """

    def _prep_stack_for_cluster(self, data: Dict):
        self._remove_fields(data, ('apiUrl', 'apikey'))

    def _prep_node(self, data: Dict):
        self._remove_fields(data, ('gid', 'id', 'name', 'status'))

    def _find_node(self, nodes: Result, stack: Dict) -> Dict:
        if stack is not None:
            for node in nodes.data:
                node_id = int(stack['referenceId']) if stack['referenceId'].isdigit() else stack['referenceId']
                if node_id == node.get('id', None):
                    return deepcopy(node)
        return None


class ClusterGroup(BaseClusterGroup):
    """
    Cluster Group
    """

    def list(self, page: int = 0, size: int = 0) -> List[models.Cluster]:
        """
        Get list of cluster instances
        Page and size can be specified only together

        :param page: (optional)
            Page number
        :param size: (optional)
            Amount of instances per page
        
        :return: 
            List of Cluster objects
        """
        stacks = self._get_data(API_PATH['stack_list'], {'page': page, 'size': size})
        nodes = self._get_data(API_PATH['node_list'], {'page': page, 'size': size})

        clusters = []
        for stack in stacks.data:
            node = self._find_node(nodes, stack)
            
            if node:
                self._prep_stack_for_cluster(stack)
                self._prep_node(node)
                clusters.append(models.Cluster(**{**stack, **node}))

        return clusters

    def get(self, cluster_id: int) -> models.Cluster:
        """
        Get information about cluster instance

        :param cluster_id: 
            Cluster instance identifier

        :return: 
            Cluster object
        """
        stack = self._get_data(API_PATH['stack_get'], {'stackId': cluster_id})
        self._prep_stack_for_cluster(stack.data)

        node = self._get_data(API_PATH['node_get'], {'nid': stack.data['referenceId']})
        self._prep_node(node.data)

        return models.Cluster(**{**stack.data, **node.data})


class BaseHostGroup(BaseGroup):
    """
    
    """

    def _prep_stack_for_host(self, data: Dict):
        self._remove_fields(data, ('gid', 'name', 'status', 'desc', 'eco'))
        self._rename_fields(data, {'id': 'stackId'})

    def _prep_sep(self, data: Dict):
        self._remove_fields(data, ('id', 'gid', 'guid'))
        self._rename_fields(data, {'name': 'sepName', 'type': 'sepType'})

    def _find_stack(self, stacks: Result, node: Dict) -> Dict:
        if node is not None:
            for stack in stacks.data:
                node_id = int(stack['referenceId']) if stack['referenceId'].isdigit() else stack['referenceId']
                if node_id == node.get('id', None):
                    return deepcopy(stack)
        return None

    def _find_sep(self, seps: Result, node: Dict) -> Dict:
        if node is not None:
            for sep in seps.data:
                if node.get('id', None) in sep['consumedBy']:
                    return deepcopy(sep)
        return None


class HostGroup(BaseHostGroup):
    """
    Host Group
    """

    def list(self, enabled: bool = True, page: int = 0, size: int = 0) -> List[models.Host]:
        """
        Get list of host instances
        Page and size can be specified only together

        :param enabled: (optional)
            Whether to show only enabled hosts or all of them
        :param page: (optional)
            Page number
        :param size: (optional)
            Amount of instances per page
        
        :return: 
            List of Host objects
        """
        nodes = self._get_data(API_PATH['node_list'], {'page': page, 'size': size})
        stacks = self._get_data(API_PATH['stack_list'], {'enabled': enabled, 'page': page, 'size': size})
        seps = self._get_data(API_PATH['sep_list'], {'page': page, 'size': size})

        hosts = []
        for node in nodes.data:
            stack = self._find_stack(stacks, node)
            sep = self._find_sep(seps, node)

            if stack and sep:
                self._prep_stack_for_host(stack)
                self._prep_sep(sep)
                hosts.append(models.Host(**{**node, **stack, **sep}))

        return hosts

    def get(self, host_id: int) -> models.Host:
        """
        Get information about host instance

        :param host_id: 
            Host instance identifier

        :return: 
            Host object
        """
        node = self._get_data(API_PATH['node_get'], {'nid': host_id})
        stacks = self._get_data(API_PATH['stack_list'])
        seps = self._get_data(API_PATH['sep_list'])

        stack = self._find_stack(stacks, node.data)
        sep = self._find_sep(seps, node.data)

        if stack and sep:
            self._prep_stack_for_host(stack)
            self._prep_sep(sep)
            return models.Host(**{**node.data, **stack, **sep})

        raise DigitalEnergyApiException('404: Not Found')


class BaseVMGroup(BaseGroup):
    """
    
    """

    def _find_stack_for_vm(self, stacks: Result, compute: Dict) -> Dict:
        if compute is not None:
            for stack in stacks.data:
                if stack['id'] == compute.get('stackId', None):
                    return deepcopy(stack)
            return None

    def _find_image(self, images: Result, compute: Dict) -> Dict:
        if compute is not None:
            for image in images.data:
                if image['id'] == compute.get('imageId', None):
                    return deepcopy(image)
            return {'hasImage': False}


class VMGroup(BaseVMGroup, BaseHostGroup, BaseClusterGroup):
    """
    Virtual Machine Group
    """

    def list(self, include_deleted: bool = False, page: int = 0, size: int = 0) -> List[models.VM]:
        """
        Get list of virtual machine instances
        Page and size can be specified only together

        :param include_deleted: (optional)
            Whether add deleted compute instances or not
        :param page: (optional)
            Page number
        :param size: (optional)
            Amount of instances per page
        
        :return: 
            List of Virtual Machine objects
        """
        computes = self._get_data(API_PATH['compute_list'], {'includedeleted': include_deleted, 'page': page, 'size': size})
        nodes = self._get_data(API_PATH['node_list'], {'page': page, 'size': size})
        stacks = self._get_data(API_PATH['stack_list'], {'page': page, 'size': size})
        seps = self._get_data(API_PATH['sep_list'], {'page': page, 'size': size})
        images = self._get_data(API_PATH['image_list'], {'page': page, 'size': size})

        vms = []
        for compute in computes.data:

            # Host
            host_stack = self._find_stack_for_vm(stacks, compute)
            host_node = self._find_node(nodes, host_stack)
            host_sep = self._find_sep(seps, host_node)

            if host_stack and host_node and host_sep:
                self._prep_stack_for_host(host_stack)
                self._prep_sep(host_sep)
                self._add_fields_prefix(host_stack, 'host')
                self._add_fields_prefix(host_node, 'host')
                self._add_fields_prefix(host_sep, 'host')

            # Cluster
            cluster_stack = self._find_stack_for_vm(stacks, compute)
            cluster_node = self._find_node(nodes, cluster_stack)

            if cluster_stack and cluster_node:
                self._prep_stack_for_cluster(cluster_stack)
                self._prep_node(cluster_node)
                self._add_fields_prefix(cluster_stack, 'cluster')
                self._add_fields_prefix(cluster_node, 'cluster')

            # Image
            image = self._find_image(images, compute)
            self._add_fields_prefix(image, 'image')

            # Virtual machine
            if host_stack and host_node and host_sep and cluster_stack and cluster_node:
                vms.append(models.VM(**{
                    **compute,
                    **host_stack, **host_node, **host_sep,
                    **cluster_stack, **cluster_node,
                    **image
                }))

        return vms

    def get(self, vm_id: int, reason: str = '') -> models.VM:
        """
        Get information about Virtual Machine instance

        :param vm_id: 
            Virtual Machine instance identifier
        :param reason: (optional)
            Reason of action
        
        :return: 
            Virtual Machine object
        """

        compute = self._get_data(API_PATH['compute_get'], {'computeId': vm_id, 'reason': reason})
        stack = self._get_data(API_PATH['stack_get'], {'stackId': compute.data['stackId']})
        images = images = self._get_data(API_PATH['image_list'])
        nodes = self._get_data(API_PATH['node_list'])
        seps = self._get_data(API_PATH['sep_list'])

        # Host
        host_stack = deepcopy(stack.data)
        host_node = self._find_node(nodes, host_stack)
        host_sep = self._find_sep(seps, host_node)

        if host_stack and host_node and host_sep:
            self._prep_stack_for_host(host_stack)
            self._prep_sep(host_sep)
            self._add_fields_prefix(host_stack, 'host')
            self._add_fields_prefix(host_node, 'host')
            self._add_fields_prefix(host_sep, 'host')

        # Cluster
        cluster_stack = deepcopy(stack.data)
        cluster_node = self._find_node(nodes, cluster_stack)

        if cluster_stack and cluster_node:
            self._prep_stack_for_cluster(cluster_stack)
            self._prep_node(cluster_node)
            self._add_fields_prefix(cluster_stack, 'cluster')
            self._add_fields_prefix(cluster_node, 'cluster')

        # Image
        image = self._find_image(images, compute.data)
        self._add_fields_prefix(image, 'image')

        # Virtual machine
        if host_stack and host_node and host_sep and cluster_stack and cluster_node:
            return models.VM(**{
                **compute.data,
                **host_stack, **host_node, **host_sep,
                **cluster_stack, **cluster_node,
                **image
            })
        else:
            details = "Compute without Host and Cluster doesn't appear in Virtual Machine actor."
            raise DigitalEnergyApiException('404: Not Found. ' + details)


class GridGroup(BaseGroup):
    """
    Grid Group
    """

    def list(self, page: int = 0, size: int = 0) -> List[models.Grid]:
        """
        Get list of grid instances
        Page and size can be specified only together

        :param page: (optional)
            Page number
        :param size: (optional)
            Amount of instances per page
        
        :return: 
            List of Grid objects
        """
        result = self._get_data(API_PATH['grid_list'], {'page': page, 'size': size})
        return [models.Grid(**grid) for grid in result.data]

    def get(self, grid_id: int) -> models.Grid:
        """
        Get information about grid instance

        :param grid_id: 
            Grid instance identifier

        :return: 
            Grid object
        """
        result = self._get_data(API_PATH['grid_get'], {'gridId': grid_id})
        if isinstance(result.data, dict):
            return models.Grid(**result.data)
        else:
            raise DigitalEnergyApiException('404: Not Found. ' + result.data if isinstance(result.data, str) else '')


class DataCenterGroup(GridGroup):
    """
    Data Center Group 
    It is an alias for Grid Group
    """
    pass


class StorageEndpointGroup(BaseGroup):
    """
    Storage Endpoint Group
    """

    def list(self, page: int = 0, size: int = 0) -> List[models.StorageEndpoint]:
        """
        Get list of Storage Endpoint instances
        Page and size can be specified only together

        :param page: (optional)
            Page number
        :param size: (optional)
            Amount of instances per page
        
        :return: 
            List of StorageEndpoint objects
        """
        result = self._get_data(API_PATH['sep_list'], {'page': page, 'size': size})
        return [models.StorageEndpoint(**sep) for sep in result.data]

    def get(self, sep_id: int) -> models.StorageEndpoint:
        """
        Get information about Storage Endpoint instance

        :param sep_id: 
            Storage Endpoint instance identifier

        :return: 
            StorageEndpoint object
        """
        result = self._get_data(API_PATH['sep_get'], {'sep_id': sep_id})
        return models.StorageEndpoint(**result.data)

    def get_config(self, sep_id: int) -> models.StorageConfig:
        """
        Get config of Storage Endpoint instance

        :param sep_id: 
            Storage Endpoint instance identifier

        :return: 
            StorageConfig object
        """
        result = self._get_data(API_PATH['sep_get_config'], {'sep_id': sep_id})
        return models.StorageConfig(**result.data)

    def get_pool(self, sep_id: int, pool_name: str) -> models.StoragePool:
        """
        Get pool of Storage Endpoint instance

        :param sep_id: 
            Storage Endpoint instance identifier
        :param pool_name: 
            Name of certain Storage Endpoint pool

        :return: 
            StoragePool object
        """
        result = self._get_data(API_PATH['sep_get_pool'], {'sep_id': sep_id, 'pool_name': pool_name})
        return models.StoragePool(**result.data)


class IamgeGroup(BaseGroup):
    """
    Image Group
    """

    def list(self, sep_id: int = None, shared_with: int = None, page: int = 0, size: int = 0) -> List[models.Image]:
        """
        Get list of Image instances
        Page and size can be specified only together

        :param sep_id: (optional)
            Filter images based on Storage Endpoint instance identifier
        :param shared_with: (optional)
            Filter images based on Account identifier availability
        :param page: (optional)
            Page number
        :param size: (optional)
            Amount of instances per page
        
        :return: 
            List of Image objects
        """
        result = self._get_data(API_PATH['image_list'], {'sepId': sep_id, 'sharedWith': shared_with, 'page': page, 'size': size})
        return [models.Image(**image) for image in result.data]

    def get(self, image_id: int) -> models.Image:
        """
        Get information about Image instance

        :param image_id: 
            Image instance identifier

        :return: 
            Image object
        """
        result = self._get_data(API_PATH['image_get'], {'imageId': image_id})
        return models.Image(**result.data)


class DiskGroup(BaseGroup):
    """
    Disk Group
    """

    def list(self, account_id: int = None, disk_type: str = None, page: int = 0, size: int = 0) -> List[models.Disk]:
        """
        Get list of Disk instances
        Page and size can be specified only together

        :param account_id: (optional)
            Filter disks based on their belonging to the Account
        :param disk_type: (optional)
            Filter disks based on their type mark
        :param page: (optional)
            Page number
        :param size: (optional)
            Amount of instances per page
        
        :return: 
            List of Disk objects
        """
        result = self._get_data(API_PATH['disks_list'], {'accountId': account_id, 'type': disk_type, 'page': page, 'size': size})
        return [models.Disk(**disk) for disk in result.data]

    def get(self, disk_id: int) -> models.Disk:
        """
        Get information about Disk instance

        :param disk_id: 
            Disk instance identifier

        :return: 
            Disk object
        """
        result = self._get_data(API_PATH['disks_get'], {'diskId': disk_id})
        return models.Disk(**result.data)


class ExternalNetworkGroup(BaseGroup):
    """
    External Network Group
    """

    def list(self, account_id: int = None, page: int = 0, size: int = 0) -> List[models.ExternalNetwork]:
        """
        Get list of External Network instances
        Page and size can be specified only together

        :param account_id: (optional)
            Filter external networks based on their belonging to the Account
        :param page: (optional)
            Page number
        :param size: (optional)
            Amount of instances per page
        
        :return: 
            List of ExternalNetwork objects
        """
        result = self._get_data(API_PATH['extnet_list'], {'accountId': account_id, 'page': page, 'size': size})
        return [models.ExternalNetwork(**sep) for sep in result.data]

    def get(self, net_id: int) -> models.ExternalNetwork:
        """
        Get information about External Network instance

        :param net_id: 
            External Network instance identifier

        :return: 
            ExternalNetwork object
        """
        result = self._get_data(API_PATH['extnet_get'], {'net_id': net_id})
        return models.ExternalNetwork(**result.data)
