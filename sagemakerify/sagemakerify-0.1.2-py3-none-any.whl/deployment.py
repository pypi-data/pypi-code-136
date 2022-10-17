import inspect
from sagemakerify import utils

class _Endpoint():
    def __init__(self, Cls, **kwargs):
        print("Init de _Endpoint")
        print(utils.get_imports(Cls))
        

    def __call__(self, *args, **kwargs):
        print("call de _Endpoint")

def endpoint(**kwargs):    
    def wrapper(Cls):
        return _Endpoint(Cls, **kwargs)

    return wrapper

