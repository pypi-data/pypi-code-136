from remotemanager.serialisation.yaml import serialyaml
from remotemanager.serialisation.json import serialjson

__all__ = ['serialyaml', 'serialjson']

try:
    from remotemanager.serialisation.dill import serialdill
    __all__.append('serialdill')
except ImportError:
    pass
