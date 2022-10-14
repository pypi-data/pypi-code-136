#!/usr/bin/env python
from codefast.io.file import FileIO as fio
import os
from typing import Any, Dict, List, Optional, Set, Tuple, Union, Iterator
import hashlib


class osdb(object):
    """ simple key-value database implementation using expiringdict
    """

    def __init__(self, db_file: str = '/tmp/osdb'):
        '''
        Args:
            ...
        '''
        self.db_file = db_file
        self.key_path = os.path.join(self.db_file, 'keys')
        if not fio.exists(db_file):
            fio.mkdir(self.db_file)

    def abs_key(self, key: str) -> str:
        return os.path.join(self.db_file, hashlib.md5(str(key).encode()).hexdigest())

    def set(self, key: str, value: str):
        with open(self.abs_key(key), 'w') as f:
            f.write(str(value))

        with open(self.key_path, 'a') as f:
            f.write('\n' + str(key))

    def get(self, key: str) -> Union[str, None]:
        try:
            return fio.reads(self.abs_key(key))
        except:
            return None

    def exists(self, key: str) -> bool:
        return fio.exists(self.abs_key(key))

    def keys(self) -> Iterator[str]:
        try:
            with open(self.key_path, 'r') as f:
                for k in f:
                    yield k.strip()
        except:
            yield from []

    def values(self) -> Iterator[str]:
        for k in fio.walk(self.db_file):
            if k != self.key_path:
                yield fio.reads(k)

    def pop(self, key: str) -> str:
        """ pop key-value
        """
        value = self.get(key)
        fio.rm(self.abs_key(key))
        keys = [k for k in self.keys() if k != str(key)]
        fio.write('\n'.join(keys), self.key_path)
        return value

    def poplist(self, keylist: List[str]) -> str:
        """ pop key list
        """
        values = []
        for k in keylist:
            values.append(self.get(k))
            fio.rm(self.abs_key(k))
        keyset = set(keylist)
        keys = [k for k in self.keys() if k not in keyset]
        fio.write('\n'.join(keys), self.key_path)
        return values

    def rpush(self, list_name: str, value: str) -> None:
        raise NotImplementedError

    def lpush(self, list_name: str, value: str) -> None:
        raise NotImplementedError

    def blpop(self, list_name: str, timeout: int = 30) -> Tuple[str, Union[str, None]]:
        """ always return a tuple. 
        """
        raise NotImplementedError

    def __getitem__(self, key: str) -> Union[str, None]:
        return self.get(key)

    def __setitem__(self, key: str, value: str) -> None:
        self.set(key, value)

    def delete(self, key: str) -> None:
        return self.pop(key)

    def __len__(self) -> int:
        return len(self.keys())

    def __repr__(self) -> str:
        return 'PickleDB(%s)' % self.db_file
