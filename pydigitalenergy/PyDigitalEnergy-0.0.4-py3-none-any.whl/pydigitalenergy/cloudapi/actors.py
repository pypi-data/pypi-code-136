from typing import List
from pydigitalenergy.cloudapi import models
from pydigitalenergy.cloudapi.endpoints import API_PATH
from pydigitalenergy.adapter import RestAdapter
from pydigitalenergy.basegroup import BaseGroup


class Cloudapi:
    def __init__(self, adapter: RestAdapter):
        self.virtual_machines = MachineGroup(adapter)


class MachineGroup(BaseGroup):
    """
    Virtual Machine Group
    """

    def list(self, include_deleted: bool = False, cloudspace_id: int = 0, page: int = 0, size: int = 0) -> List[models.Machine]:
        """
        Get list of virtual machine instances
        Page and size can be specified only together

        :param include_deleted: (optional)
            Whether add deleted machine instances or not
        :param cloudspace_id: (optional)
            Cloud space identifier which contains that machine instance
        :param page: (optional)
            Page number
        :param size: (optional)
            Amount of instances per page
        
        :return: 
            List of Machine objects
        """
        result = self._get_data(API_PATH['machine_list'], {'includedeleted': include_deleted, 'cloudspaceId': cloudspace_id, 'page': page, 'size': size})
        return [models.Machine(**machine) for machine in result.data]

    def get(self, machine_id: int) -> models.Machine:
        """
        Get information about virtual machine instance

        :param machine_id: 
            Machine instance identifier
        
        :return: 
            Machine object
        """
        result = self._get_data(API_PATH['machine_get'], {'machineId': machine_id})
        return models.Machine(**result.data)

