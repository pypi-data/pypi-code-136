"""Test Logger"""
import glob
import os
import time
from pathlib import Path

import pytest

from yirgachefe import logger


@pytest.fixture
def log_file() -> Path:
    root_path = Path(os.path.join(os.path.dirname(__file__), '.'))
    file_path: Path = root_path.joinpath('temp-log-file.log')
    return file_path


@pytest.fixture(autouse=True)
def clear_test_log_file(log_file):
    file_path: Path = log_file
    root_path = Path(os.path.join(file_path, '.'))

    file_list = glob.glob(f'{file_path}*')
    for file in file_list:
        path: Path = root_path.joinpath(file)
        if path.exists():
            path.unlink()

    yield

    file_list = glob.glob(f'{file_path}*')
    for file in file_list:
        path: Path = root_path.joinpath(file)
        if path.exists():
            path.unlink()


class TestLogger:
    def test_get_logger(self):
        logger.get_logger().warning('warning log')

    def test_autocomplete(self):
        logger.debug('debug log')

    def test_coloredlog(self):
        print()
        logger.update_logger(stream_out=True)
        logger.info('log')
        logger.critical('log')
        logger.error('log')
        logger.debug('log')
        logger.warning('log')
        logger.critical('log')

        logger.update_logger(stream_out=True, coloredlog=True)
        logger.info('color')
        logger.critical('color')
        logger.error('color')
        logger.debug('color')
        logger.warning('color')
        logger.critical('color')

    def test_log_file(self, log_file):
        print()
        logger.update_logger(log_path=str(log_file), stream_out=True)
        logger.debug('file')

        logger.update_logger(stream_out=True, coloredlog=True)
        logger.debug('color NO-FILE')

        logger.update_logger(log_path=str(log_file), stream_out=True, coloredlog=True)
        logger.debug('color file')

        with open(str(log_file), 'r') as _log_file:
            logs = _log_file.readlines()
            for log in logs:
                assert 'NO-FILE' not in log

    def test_log_rotating(self, log_file):
        print()
        logger.update_logger(log_path=str(log_file), stream_out=True, coloredlog=True,
                             log_when='s', log_interval=1, log_backup_count=5)
        for i in range(3):
            logger.debug('rotating file')
            time.sleep(1)

        file_path: Path = log_file
        root_path = Path(os.path.join(file_path, '.'))
        file_list = glob.glob(f'{file_path}*')
        for file in file_list:
            path: Path = root_path.joinpath(file)
            print(file)
            assert path.exists()

    def test_default_logger_name(self):
        from yirgachefe import _get_main_module_name
        assert logger.name == _get_main_module_name()
