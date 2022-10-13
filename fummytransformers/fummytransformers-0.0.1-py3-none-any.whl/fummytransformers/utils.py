import time
import functools
import sys
from importlib import reload


def say_hello():
    print("hello this is frenchnlp!")


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
