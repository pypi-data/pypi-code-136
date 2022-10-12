"""
This is supposed to be a replacement for bazel runfiles that can be used in pypi packages
"""
from importlib.resources import files

class runfiles:

    @classmethod
    def Create(cls) -> 'Runfiles':
        return cls

    @staticmethod
    def Rlocation(path):
        return files('beit') / path
