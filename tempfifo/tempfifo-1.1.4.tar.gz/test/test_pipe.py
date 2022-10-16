import pytest
import random
import shutil
import string
import subprocess

from tempfifo import NamedTemporaryFIFO

@pytest.fixture
def random_string():
    return ''.join(random.choices(string.ascii_letters, k=4))


def without_open(data: str):
    with NamedTemporaryFIFO() as pipe:
        with subprocess.Popen(
            (shutil.which('sh'), '-c', f'echo {data} > {pipe.name}')):
            with subprocess.Popen((shutil.which('cat'), pipe.name),
                                  stdout=subprocess.PIPE) as reader:
                result, _ = reader.communicate()
    return result.decode().rstrip()


def with_open(data: str):
    with NamedTemporaryFIFO(open_read_end=True, open_write_end=True) as pipe:
        with subprocess.Popen((shutil.which('echo'), data),
                              stdout=pipe.write_end):
            with subprocess.Popen(shutil.which('cat'), stdin=pipe.read_end,
                                  stdout=subprocess.PIPE) as reader:
                pipe.close()
                result, _ = reader.communicate()
    return result.decode().rstrip()


def test_without_open(random_string):
    assert without_open(random_string) == random_string


def test_with_open(random_string):
    assert with_open(random_string) == random_string