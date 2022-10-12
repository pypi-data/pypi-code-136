# std
from contextlib import contextmanager
import os


@contextmanager
def in_dir(dirpath: str):
    cwd = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(cwd)
