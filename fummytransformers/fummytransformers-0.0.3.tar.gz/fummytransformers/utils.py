import time
import functools
import sys
from importlib import reload
import tensorflow as tf

def show_gpuinfo():
    print("gpu list:",tf.config.list_physical_devices('GPU'))
    print("n of GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
    sys_details = tf.sysconfig.get_build_info()
    try:
        cuda_version = sys_details["cuda_version"]
        print("cuda_version:",cuda_version)
    except:
        print("no cuda")

def say_hello():
    print("hello this is fummytransformers!")


def timer(func):
    @functools.wraps(func)
    def time_closure(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        time_elapsed = time.perf_counter() - start
        print(f"Function: {func.__name__}, Time: {time_elapsed}")
        return result
    return time_closure


def reimport_all(package):
    reload(sys.modules[package])
