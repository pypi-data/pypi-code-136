"""Implementations related to BASS system."""

import os
from io import IOBase
from typing import overload

from requests import Response, session

from . import logger


class BassException(Exception):
    ...


class BassProxy:

    _URL = 'http://playground-backend:9060/alpha-med/fed-bass'

    def __init__(self):
        self._sess = session()
        self._token = None
        self._headers = {
            'accept': 'application/json',
            'content-type': 'application/json'
        }

        self._login()

    def _verify_response(self, resp: Response) -> dict:
        assert (
            resp and isinstance(resp, Response)
        ), f'invalid response object: {resp=}'
        assert (
            resp.status_code >= 200 and resp.status_code < 300
        ), f'request failed: {resp.status_code=}'
        resp_json = resp.json()
        assert (
            resp_json and isinstance(resp_json, dict)
        ), f'invalid response content: {resp.text=}'
        _Response = resp_json.get('Response')
        assert (
            _Response and isinstance(_Response, dict)
        ), f'invalid response data: {resp_json=}'
        _Data = _Response.get('Data')
        assert (
            _Data and isinstance(_Data, dict)
        ), f'invalid response data: {_Response=}'
        return _Data

    def _login(self) -> str:
        """Login to BASS system."""
        params = {
            'cmb': 'Login'
        }
        data = {
            'UserName': 'admin',
            'Password': 'dc483e80a7a0bd9ef71d8cf973673924',
            'Captcha': 'aes2'
        }
        resp = self._sess.post(url=self._URL, params=params, json=data, headers=self._headers)
        resp_data = self._verify_response(resp=resp)
        token = resp_data.get('Token')
        assert token and isinstance(token, str), f'invalid token: {resp_data=}'
        self._token = token
        self._sess.cookies.update(resp.cookies)
        self._headers['token'] = self._token
        self._headers['cookie'] = ';'.join(f'{name}={value}'
                                           for name, value in self._sess.cookies.items())

    @overload
    def upload_file(self, upload_name: str, fp: str) -> str: ...

    @overload
    def upload_file(self, upload_name: str, fp: IOBase) -> str: ...

    def upload_file(self, upload_name: str, fp) -> str:
        """Upload a file to BASS system."""
        assert self._token, 'must login at first'
        assert upload_name and isinstance(upload_name, str), f'invalid name: {upload_name}'
        assert fp, 'nothing to upload'
        assert isinstance(fp, (str, IOBase)), f'invalid file type: {type(fp)}'
        if isinstance(fp, str):
            assert (
                isinstance(fp, str)
                and os.path.exists(fp)
                and os.path.isfile(fp)
            ), f'{fp} does not exist or is not a file'

        params = {
            'cmb': 'UploadFile'
        }
        headers = self._headers.copy()
        headers.pop('content-type')
        if isinstance(fp, str):
            files = {'File': (upload_name, open(fp, 'rb'))}
        else:
            fp.seek(0)
            files = {'File': (upload_name, fp)}
        resp = self._sess.post(self._URL, params=params, headers=headers, files=files)
        resp_data = self._verify_response(resp=resp)
        file_key = resp_data.get('FileKey')
        assert file_key and isinstance(file_key, str), f'invalid file key: {file_key=}'
        return file_key

    def launch_task(self, task_id: str, pickle_file_key: str) -> bool:
        assert task_id and isinstance(task_id, str), f'invalid task ID: {task_id}'
        assert (
            pickle_file_key and isinstance(pickle_file_key, str)
        ), f'invalid key of pickle file: {pickle_file_key}'

        params = {
            'cmb': 'StartCalculationTaskRunning'
        }
        data = {
            'TaskId': task_id,
            'ProgramObject': pickle_file_key
        }
        resp = self._sess.post(self._URL, params=params, json=data, headers=self._headers)
        resp_data = self._verify_response(resp=resp)
        if resp_data.get('Status') == 'OK':
            return True
        else:
            logger.error(f'failed to launch task: {resp_data}')
            return False

    def notify_dataset_state(self, task_id: str, verified: bool):
        """Notify varification result of local dataset to the task manager."""
        assert task_id and isinstance(task_id, str), f'invalid task ID: {task_id}'
        assert isinstance(verified, bool), f'invalid verification state: {verified}'

        params = {
            'cmb': 'VerifyTaskDataSetCallback'
        }
        data = {
            'TaskId': task_id,
            'VerifyResult': verified
        }
        resp = self._sess.post(self._URL, params=params, json=data, headers=self._headers)
        self._verify_response(resp=resp)
