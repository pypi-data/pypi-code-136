import importlib
import json
import os
import urllib.parse
import zipfile
from getpass import getpass
from pathlib import Path
from typing import Optional

import requests
import xattr

from quera.utils.cache import cache

JUDGE_API = 'https://mirror.quera.org/judge_api/apikey-judge/'


def __get_current_file_id():
    response = requests.get('http://172.28.0.2:9000/api/sessions').json()
    if len(response) > 0 and 'path' in response[0] and 'fileId=' in response[0]['path']:
        _file_id = response[0]['path'].split('=', 1)[1]
        return urllib.parse.unquote(_file_id)

    return None


def get_file_id(path):
    try:
        return xattr.getxattr(path, 'user.drive.id').decode()
    except (OSError, FileNotFoundError):
        return None


def get_colab_current_file_path() -> Optional[Path]:
    try:
        drive = importlib.import_module('.drive', 'google.colab')
    except ModuleNotFoundError:
        return None

    drive_path = '/content/drive'
    drive.mount(drive_path)

    file_id = __get_current_file_id()
    if file_id is None:
        return None

    for dir_path, _, files in os.walk(f'{drive_path}/MyDrive/Quera/'):
        file_path = next(
            filter(
                lambda x: file_id == get_file_id(x),
                filter(
                    lambda x: x.endswith('.ipynb'),
                    map(
                        lambda x: os.path.join(dir_path, x),
                        files
                    )
                )
            ),
            None
        )
        if file_path:
            return Path(file_path)

    return None


def get_apikey() -> str:
    if 'apikey' not in cache:
        sibling_files = get_colab_current_file_path().parent.iterdir()
        apikey_file = next(filter(lambda f: f.is_file and f.name == '.quera_config', sibling_files), None)
        if apikey_file is not None:
            config = json.loads(apikey_file.read_text())
            set_problem_id(config['problem_id'])
            set_file_type_id(config['file_type_id'])
            cache['apikey'] = config['apikey']
        else:
            print('Enter you APIKey please:')
            cache['apikey'] = getpass('Quera APIKey: ')
    return cache['apikey']


def set_problem_id(problem_id: int):
    cache['problem_id'] = int(problem_id)


def get_problem_id() -> int:
    if 'problem_id' not in cache:
        raise Exception('run `set_problem_id(...)` function before calling this one.')
    return cache['problem_id']


def set_file_type_id(file_type_id: int):
    cache['file_type_id'] = int(file_type_id)


def get_file_type_id() -> int:
    if 'file_type_id' not in cache:
        raise Exception('run `set_file_type_id(...)` function before calling this one.')
    return cache['file_type_id']


def submit(*, submitting_file_name: str = 'result.zip', api: str = JUDGE_API):
    problem_id = get_problem_id()
    file_type_id = get_file_type_id()

    with open(submitting_file_name, 'rb') as result:
        response = requests.post(
            api,
            files={'file': result},
            data={'problem_id': problem_id, 'file_type': file_type_id},
            headers={'Judge-APIKey': get_apikey()}
        )
        if response.status_code != 201:
            print(f'Error - {response.status_code}: ', response.content.decode())
        else:
            print('Submitted to Quera Successfully')


def submit_files(file_names: list = None):
    if not file_names:
        raise Exception('No files selected to submit')

    with zipfile.ZipFile("result.zip", mode="w") as zf:
        for file_name in file_names:
            zf.write('./' + file_name, file_name, compress_type=zipfile.ZIP_DEFLATED)

    submit(submitting_file_name="result.zip")
