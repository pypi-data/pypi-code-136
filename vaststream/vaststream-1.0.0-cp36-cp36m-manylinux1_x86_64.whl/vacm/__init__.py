# coding: utf-8

from typing import Optional
from _vaststream_pybind11 import vacm

# 返回值校验
def err_checker(func):
    def wrapper(*args,**kwargs):
        ret = func(*args,**kwargs)
        if ret != vacm.vacmER_SUCCESS:
            raise Exception(f"{func.__name__} return error.")
    return wrapper

@err_checker
def initialize(config: Optional[str] = None) -> int:
    """
    Initialize the environment for VACM API. This is the first API need to call.\n
    ----------\n
    config [in]: Config file will be loaded for initialization. If NULL, default config will be used.\n
    """
    return vacm.initialize(config)

@err_checker
def uninitialize() -> int:
    """
    Release the environment for VACM API. This is the last API need to call.\n
    """
    return vacm.uninitialize()

@err_checker
def setDevice(devIdx: int) -> int:
    """
    Set the device to be used in the process. All resources will be bound to the device specified.\n
    ----------\n
    devIdx [in]: Device index to be set.\n
    """
    return vacm.setDevice(devIdx)
