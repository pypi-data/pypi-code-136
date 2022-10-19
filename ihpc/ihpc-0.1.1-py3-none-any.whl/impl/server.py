__all__ = ['ClassMethod', 'Magic']


import json
import pathlib as p
import typing as t

import paramiko

from ..base.type import Path

if t.TYPE_CHECKING:
    from typing_extensions import Self

    from ..base.core import RemotePath


class ClassMethod:
    '''Impl class methods for Server
    '''

    @classmethod
    def from_first_valid_file(cls, *paths: Path, verbose: bool = True) -> 'Self':
        for path in map(p.Path, paths):
            try:
                return cls.from_file(path)
            except Exception as e:
                if verbose:
                    print(path, e)
        raise FileNotFoundError

    @classmethod
    def from_file(cls, path: Path) -> 'Self':
        path = p.Path(path)
        return getattr(cls, f'from_{path.suffix[1:]}')(path)

    @classmethod
    def from_json(cls, path: Path) -> 'Self':
        path = p.Path(path)
        return cls(**json.loads(path.read_text()))


class Magic:
    '''Impl magic methods for Server

    - Reference:
        - https://docs.python.org/3/reference/datamodel.html
    '''

    _host: str
    _port: int
    _user: str
    _trans: paramiko.Transport
    _ssh: t.Optional[paramiko.SSHClient]
    _sftp: t.Optional[paramiko.SFTPClient]

    def __enter__(self) -> 'Self':
        return self

    def __exit__(self, type, value, traceback) -> None:
        self.close()

    def __repr__(self) -> str:
        return f'<{self._user}@{self._host}({self._port})>'

    def __truediv__(self, path: Path) -> 'RemotePath':
        # Not recommended at this time, try property root and home
        from ..base.core import RemotePath

        return RemotePath(path, self)
