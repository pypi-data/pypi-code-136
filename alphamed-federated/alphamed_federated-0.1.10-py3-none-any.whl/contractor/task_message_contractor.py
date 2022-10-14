"""公共合约."""

import base64
import os
import secrets
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional

import requests
from requests import Response

from .. import logger
from ..utils import retry
from .common import (ContractEvent, ContractEventFactory, ContractException,
                     Contractor)
from .task_contractor import TaskContractor

__all__ = [
    'ApplySendingDataEvent',
    'DenySendingDataEvent',
    'AcceptSendingDataEvent',
    'TaskMessageEventFactory',
    'TaskMessageContractor'
]


@dataclass
class ApplySendingDataEvent(ContractEvent):
    """An event of requesting sending data."""

    TYPE = 'apply_sending_data'

    session_id: str
    source: str
    target: str
    public_key: bytes

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'ApplySendingDataEvent':
        event_type = contract.get('type')
        session_id = contract.get('session_id')
        source = contract.get('source')
        target = contract.get('target')
        base64_key = contract.get('public_key')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert session_id and isinstance(session_id, str), f'invalid session_id: {session_id}'
        assert source and isinstance(source, str), f'invalid source: {source}'
        assert target and isinstance(session_id, str), f'invalid target: {target}'
        assert base64_key and isinstance(base64_key, str), f'invalid public_key: {base64_key}'
        public_key = base64.b64decode(base64_key.encode())
        return ApplySendingDataEvent(session_id=session_id,
                                     source=source,
                                     target=target,
                                     public_key=public_key)


@dataclass
class DenySendingDataEvent(ContractEvent):
    """An event of denying sending data."""

    TYPE = 'deny_sending_data'

    session_id: str

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'DenySendingDataEvent':
        event_type = contract.get('type')
        session_id = contract.get('session_id')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert session_id and isinstance(session_id, str), f'invalid session_id: {session_id}'
        return DenySendingDataEvent(session_id=session_id)


@dataclass
class AcceptSendingDataEvent(ContractEvent):
    """A event of accepting receiving data."""

    TYPE = 'accept_sending_data'

    session_id: str
    public_key: bytes
    port: bytes

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'AcceptSendingDataEvent':
        event_type = contract.get('type')
        session_id = contract.get('session_id')
        base64_key = contract.get('public_key')
        base64_port = contract.get('port')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert session_id and isinstance(session_id, str), f'invalid session_id: {session_id}'
        assert base64_key and isinstance(base64_key, str), f'invalid public_key: {base64_key}'
        assert base64_port and isinstance(base64_port, str), f'invalid port: {base64_port}'
        public_key = base64.b64decode(base64_key.encode())
        port = base64.b64decode(base64_port.encode())
        return AcceptSendingDataEvent(session_id=session_id,
                                      public_key=public_key,
                                      port=port)


@dataclass
class UploadTaskAchievementEvent(ContractEvent):
    """A event of uploading task achievement materials."""

    TYPE = 'upload_task_achieve'

    model: str
    report: str = None

    @classmethod
    def contract_to_event(cls, contract: dict) -> None:
        raise NotImplementedError()


@dataclass
class NoticeTaskCompletionEvent(ContractEvent):
    """A event of noticing task manager that current task is complete."""

    TYPE = 'notice_task_completion'

    result: bool

    @classmethod
    def contract_to_event(cls, contract: dict) -> None:
        raise NotImplementedError()


class TaskMessageEventFactory(ContractEventFactory):

    _CLASS_MAP: Dict[str, ContractEvent] = {
        ApplySendingDataEvent.TYPE: ApplySendingDataEvent,
        DenySendingDataEvent.TYPE: DenySendingDataEvent,
        AcceptSendingDataEvent.TYPE: AcceptSendingDataEvent
    }

    @classmethod
    def contract_to_event(cls, contract: dict) -> Optional[ContractEvent]:
        try:
            assert contract and isinstance(contract, dict)
            event_type = contract.get('type')
            assert event_type in cls._CLASS_MAP.keys()
            event = cls._CLASS_MAP[event_type].contract_to_event(contract)
            return event
        except AssertionError:
            logger.exception(f'invalid contract data: {contract}')
            return None


class TaskMessageContractor(Contractor):
    """公共合约."""

    _URL = 'http://federated-service:9080/fed-service/api/v1/message'

    _TASK_INSIDE = 'TaskInside'
    _UPLOAD_TASK_ACHIEVE = 'TaskResultUpload'
    _TASK_FINISH = 'TaskFinish'

    _TITLE_ALL = (_TASK_INSIDE, _UPLOAD_TASK_ACHIEVE, _TASK_FINISH)

    def __init__(self, task_id: str) -> None:
        super().__init__()
        self.task_id = task_id
        self._event_factory = TaskMessageEventFactory
        self._task_contractor = TaskContractor(task_id=task_id)

    def _validate_response(self, resp: Response) -> dict:
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

    @retry(exceptions=ContractException)
    def _new_contract(self,
                      targets: List[str],
                      event: ContractEvent,
                      message_title: str = _TASK_INSIDE) -> str:
        assert targets, 'must specify the target consumers of the contract'
        assert (
            isinstance(targets, list)
            and all(_target and isinstance(_target, str) for _target in targets)
        ), f'the target consumers must be an ID list: {targets}'
        assert event, 'cannot send empty contract'
        assert (
            isinstance(event, ContractEvent)
        ), f'"event" should be a contract event object: {event}'
        assert (
            message_title and message_title in self._TITLE_ALL
        ), f'invalid message_title: {message_title}'

        event.validate()

        url = f'{self._URL}/push'
        post_data = {
            'task_id': self.task_id,
            'node_id_list': targets,
            'message_title': message_title,
            'message_content': event.event_to_contract()
        }
        logger.debug(f'contract content: {post_data}')
        resp = requests.post(url=url, json=post_data, headers=self._HEADERS)
        resp_data = self._validate_response(resp=resp)
        _detail = resp_data.get('message_detail')
        assert (
            _detail and isinstance(_detail, dict)
        ), f'faild to push a new contract: {resp_data}'
        TxId: str = _detail.get('TxId')
        assert TxId and isinstance(TxId, str), f'invalid TxId: {TxId}'
        logger.info(f'successfully pushed a new contract: {TxId=}')
        return TxId

    def _pop_contract(self) -> Optional[dict]:
        """Popup a contract for consuming if exists."""
        post_data = {
            'task_id': self.task_id,
        }
        post_url = f'{self._URL}/pop'
        resp = requests.post(url=post_url, json=post_data, headers=self._HEADERS)
        resp_data = self._validate_response(resp=resp)
        if not resp_data:
            return None
        _content = resp_data.get('message_content')
        assert _content and isinstance(_content, dict), f'invalid contract content: {_content}'
        logger.debug(f'popped up a contract: {_content}')
        return _content

    def apply_sending_data(self, source: str, target: str, public_key: bytes) -> str:
        """发送数据传输请求合约."""
        session_id = secrets.token_hex(16)
        event = ApplySendingDataEvent(session_id=session_id,
                                      source=source,
                                      target=target,
                                      public_key=public_key)
        self._new_contract(targets=[target], event=event)
        return session_id

    def deny_sending_data(self, target: str, session_id: str) -> None:
        """拒绝数据传输请求合约."""
        event = DenySendingDataEvent(session_id=session_id)
        self._new_contract(targets=[target], event=event)

    def accept_sending_data(self,
                            target: str,
                            session_id: str,
                            public_key: bytes,
                            cipher_port: bytes) -> None:
        """接受数据传输请求合约.

        :args
            :session_id
                the session id of this data sending
            :public_key
                the public key of the data receiver
            :cipher_port
                the port number used for connecting, encrypted by the sender's public key
        """
        event = AcceptSendingDataEvent(session_id=session_id,
                                       public_key=public_key,
                                       port=cipher_port)
        self._new_contract(targets=[target], event=event)

    def contract_events(self, timeout: int = 0) -> ContractEvent:
        """Return contract events iteratively.

        :args
            :timeout
                The seconds to timeout. Will never timeout if is set less or equal to 0.
        """
        if not isinstance(timeout, int) or timeout < 0:
            timeout = 0  # disable timeout
        if timeout > 0:
            start = datetime.utcnow().timestamp()
        while timeout <= 0 or datetime.utcnow().timestamp() - start < timeout:
            _contract = self._pop_contract()
            if _contract:
                event = self._event_factory.contract_to_event(contract=_contract)
                if event:
                    yield event
                else:
                    logger.warn(f'failed to parse a contract to an event: {_contract}')
            else:
                time.sleep(0.1)
            continue

    @retry()
    def query_address(self, target: str) -> Optional[str]:
        """Query address of the target. TODO refactory contractors."""
        return self._task_contractor.query_address(target=target)

    def upload_task_achivement(self,
                               aggregator: str,
                               model_file: str,
                               report_file: str = ''):
        """Upload achivement materials after a task is complete.

        :args
            :aggregator
                The ID of the aggregator.
            :model_file
                Local path of the model file.
            :report_file
                Local path of the report file.
        """
        assert aggregator and isinstance(aggregator, str), f'unknown aggregator: {aggregator}'
        assert (
            model_file and isinstance(model_file, str)
            and os.path.exists(model_file)
            and os.path.isfile(model_file)
        ), f'the model_file does not exist or can not be accessed: {model_file}'
        if report_file:
            assert (
                isinstance(report_file, str)
                and os.path.exists(report_file)
                and os.path.isfile(report_file)
            ), f'the report_file does not exist or can not be accessed: {report_file}'

        event = UploadTaskAchievementEvent(report=report_file, model=model_file)
        TxId = self._new_contract(targets=[aggregator],
                                  event=event,
                                  message_title=self._UPLOAD_TASK_ACHIEVE)
        if not TxId:
            raise ContractException('failed to notify task completion')

    def notify_task_completion(self, result: bool):
        """Notify task manager a task is complete.

        :args
            :result
                True if successful otherwize False.
        """
        event = NoticeTaskCompletionEvent(result=result)
        TxId = self._new_contract(targets=self.EVERYONE,
                                  event=event,
                                  message_title=self._TASK_FINISH)
        if not TxId:
            raise ContractException('failed to notify task completion')
