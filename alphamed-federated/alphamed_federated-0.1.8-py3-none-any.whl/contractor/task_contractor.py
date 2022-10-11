"""Tools for task related contracts."""

from typing import List, Optional

import requests

from .. import logger
from .common import ContractException, Contractor

__all__ = ['TaskContractor']


class TaskContractor(Contractor):
    """A contractor to handle task related ones."""

    _URL = 'http://federated-service:9080/fed-service/api/v1'

    def __init__(self, task_id: str) -> None:
        super().__init__()
        self.task_id = task_id

    def _validate_response(self, resp: requests.Response) -> dict:
        if resp.status_code < 200 or resp.status_code >= 300:
            raise ContractException(f'failed to submit a contract: {resp}')
        resp_json: dict = resp.json()
        if not resp_json or not isinstance(resp_json, dict):
            raise ContractException(f'invalid response:\nresp: {resp}\njson: {resp_json}')
        if resp_json.get('code') != 0:
            raise ContractException(f'failed to handle a contract: {resp_json}')
        data = resp_json.get('data')
        if data is None or not isinstance(data, dict):
            raise ContractException(f'contract data error: {resp_json}')
        task_id = data.get('task_id')
        assert task_id is None or task_id == self.task_id, f'task_id dismatch: {task_id}'
        return data

    def query_address(self, target: str) -> Optional[str]:
        """Query address of the target."""
        assert target and isinstance(target, str), f'invalid target node: {target}'
        post_data = {
            'task_id': self.task_id,
            'node_id': target
        }
        post_url = f'{self._URL}/fed/network/node/detail'
        resp = requests.post(url=post_url, json=post_data, headers=self._HEADERS)
        resp_data = self._validate_response(resp=resp)
        ip = resp_data.get('node_ip')
        if not ip or not isinstance(ip, str):
            logger.warn(f'failed to obtain target address: {resp_data}')
            return None
        else:
            return ip

    def query_nodes(self) -> List[str]:
        """Query all nodes in this task."""
        post_data = {'task_id': self.task_id}
        post_url = f'{self._URL}/task/nodelist'
        resp = requests.post(url=post_url, json=post_data, headers=self._HEADERS)
        resp_data = self._validate_response(resp=resp)
        records: list[dict] = resp_data.get('records')
        assert (
            records and isinstance(records, list)
        ), f'failed to query node IDs of task: {self.task_id}'
        for _node in records:
            assert _node and _node.get('node_id'), f'broken node data: {records}'
        return [_node['node_id'] for _node in records]
