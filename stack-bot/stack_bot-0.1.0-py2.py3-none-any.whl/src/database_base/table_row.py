import random
from dataclasses import dataclass
from typing import Any, Dict, List


def random_id():
    return random.randint(0, 2**31-1)


@dataclass
class TableRow(object):
    
    @classmethod
    def get_columns(cls) -> Dict[str, type]:
        return cls.__annotations__  

    @classmethod
    def primary_key(cls) -> str:
        for k in cls.get_columns():
            return k
        return ""

    def values(self) -> List[Any]:
        return list(map(lambda k: self[k], self.get_columns().keys()))

    @classmethod
    def create_model(cls, **kwargs):
        fields = {}
        for (c, t) in cls.get_columns().items():
            if c in kwargs:
                fields[c] = t(kwargs[c])
            else:
                if cls.primary_key() == c:
                    fields[c] = random_id()
                else:
                    fields[c] = None

        return cls(**fields)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)
    
    def __repr__(self):
        return self.__str__()

