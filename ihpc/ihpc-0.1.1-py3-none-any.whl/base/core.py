__all__ = ['Server']


import functools as f
import pathlib as p
import typing as t

import paramiko

from .type import AnyPosixPath, Path, StdOE
from .. import impl

if t.TYPE_CHECKING:
    from typing_extensions import Self


class Server(
    impl._.Generic,
    impl.server.ClassMethod,
    impl.server.Magic,
):
    '''Python wrapper for paramiko library

    - Reference:
        - https://github.com/paramiko/paramiko
    '''

    __version__ = '0.1.1'

    def __init__(self, host: str, port: int, username: str, password: str) -> None:
        self._host, self._port, self._user = host, port, username
        self._trans = paramiko.Transport((host, port))
        self._trans.connect(username=username, password=password)
        self._ssh = self._sftp = None

    @property
    def ssh(self) -> paramiko.SSHClient:
        if self._ssh is None:
            self._ssh = paramiko.SSHClient()
            self._ssh.load_system_host_keys()
            self._ssh._transport = self._trans
        return self._ssh

    @property
    def sftp(self) -> paramiko.SFTPClient:
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._trans)
        return self._sftp

    @f.cached_property
    def home(self) -> 'RemotePath':
        stdout, _ = self.run('echo $HOME')
        return RemotePath(stdout.strip().decode(), self)

    @f.cached_property
    def root(self) -> 'RemotePath':
        return RemotePath('/', self)

    def close(self) -> None:
        if self._ssh is not None:
            self._ssh.close()
        if self._sftp is not None:
            self._sftp.close()
        self._ssh = self._sftp = None

    def is_alive(self) -> bool:
        return self._trans.is_alive()

    def run(self, command: str, cwd: t.Optional[str] = None) -> StdOE:
        if cwd is not None:
            command = f'cd {p.Path(cwd).as_posix()} && {command}'
        return self._run(command)

    def _run(self, command: str) -> StdOE:
        _, stdout, stderr = self.ssh.exec_command(command)
        return stdout.read(), stderr.read()


class RemotePath(
    impl._.Generic,
    impl.remote_path.Magic,
    impl.remote_path.PosixPath,
    impl.remote_path.SwitchDirectory,
):
    '''Manage servers by path

    - Reference:
        - https://docs.python.org/3/library/pathlib.html
    '''

    def __init__(self, path: Path, server: Server) -> None:
        self._path = p.Path(path)
        self._server = server

    def run(self, command: str) -> StdOE:
        return self._server.run(command, cwd=self.as_posix())

    def walk(self) -> t.Iterator['Self']:
        for path in self.iterdir():
            if path.is_dir():
                yield from path.walk()
            else:
                yield path

    def switch(self, path: Path, upload: bool = True) -> AnyPosixPath:
        # Good Luck & Have Fun
        if upload:
            return self.upload(path)
        else:
            return self.download(path)

    def download(self, path: Path) -> p.Path:
        '''Download

        - Analysis:
            | self | path | action                   | ? |
            | ==== | ==== | ======================== | = |
            |  404 |  404 | error                    | x |
            |  404 |  dir | error                    | x |
            |  404 | file | error                    | x |
            | ---- | ---- | ------------------------ | - |
            |  dir |  404 | self/* -> path/*         | x |
            |  dir |  dir | self/* -> path/*         | x |
            |  dir | file | error                    | x |
            | ---- | ---- | ------------------------ | - |
            | file |  404 | self   -> path/self.name | x |
            | file |  dir | self   -> path/self.name | x |
            | file | file | self   -> path           | x |
        '''
        path = p.Path(path)
        if self.is_dir():
            return self.switch_dir(path, upload=False, via='rglob')
        elif self.is_file():
            return self.switch_file(path, upload=False)
        else:
            raise

    def upload(self, path: Path) -> 'Self':
        '''Upload

        - Analysis:
            | self | path | action                   | ? |
            | ==== | ==== | ======================== | = |
            |  404 |  404 | error                    | x |
            |  dir |  404 | error                    | x |
            | file |  404 | error                    | x |
            | ---- | ---- | ------------------------ | - |
            |  404 |  dir | path/* -> self/*         | x |
            |  dir |  dir | path/* -> self/*         | x |
            | file |  dir | error                    | x |
            | ---- | ---- | ------------------------ | - |
            |  404 | file | path   -> self/path.name | x |
            |  dir | file | path   -> self/path.name | x |
            | file | file | path   -> self           | x |
        '''
        path = p.Path(path)
        if path.is_dir():
            return self.switch_dir(path, upload=True, via='rglob')
        elif path.is_file():
            return self.switch_file(path, upload=True)
        else:
            raise

    def switch_dir(self, path: Path, upload: bool = True, via: str = 'rglob') -> AnyPosixPath:
        path = p.Path(path)
        if upload:
            src, dst = path, self
        else:
            src, dst = self, path
        # assert src.exists() and src.is_dir()
        if not dst.exists():
            dst.mkdir(parents=True, exist_ok=True)
            dest = dst
        elif dst.is_dir():
            dest = dst
        else:
            raise
        getattr(self, f'_switch_dir_via_{via}')(dst=dest, src=src, upload=upload)
        return dest

    def switch_file(self, path: Path, upload: bool = True) -> AnyPosixPath:
        path = p.Path(path)
        if upload:
            src, dst = path, self
            switch = self._server.sftp.put
        else:
            src, dst = self, path
            switch = self._server.sftp.get
        # assert src.exists() and src.is_file()
        if not dst.exists():
            dst.mkdir(parents=True, exist_ok=True)
            dest = dst / src.name
        elif dst.is_dir():
            dest = dst / src.name
        elif dst.is_file():
            dest = dst
        else:
            raise
        switch(src.as_posix(), dest.as_posix())
        return dest
