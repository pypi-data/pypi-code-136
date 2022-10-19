__all__ = ['Command']


import re
import typing as t

from ....base.type import Table

if t.TYPE_CHECKING:
    from typing_extensions import Self

    from ..core import LSF
    from ....base.core import Server


class Command:
    '''LSF commands

    - TODO:
        - bsub: Submits a job to LSF by running the specified command and its arguments
    '''

    def __init__(self, server: 'Server') -> None:
        self._server = server

    @classmethod
    def from_server(cls, server: 'Server') -> 'Self':
        return cls(server)

    @classmethod
    def from_lsf(cls, lsf: 'LSF') -> 'Self':
        return cls.from_server(lsf._server)

    def bhosts(self, *args: str) -> Table[str]:
        '''Displays hosts and their static and dynamic resources
        '''
        return self._table(self._run('bhosts', *args).decode())

    def bjobs(self, *args: str) -> Table[str]:
        '''Displays and filters information about LSF jobs. Specify one or more job IDs (and, optionally, an array index list) to display information about specific jobs (and job arrays)
        '''
        try:
            return self._table(self._run('bjobs', *args).decode())
        except AssertionError:
            # No unfinished job found
            return []

    def bparams(self, *args: str) -> str:
        '''Displays information about configurable system parameters in lsb.params
        '''
        return self._run('bparams', *args).decode()

    def bqueues(self, *args: str) -> Table[str]:
        '''Displays information about queues
        '''
        return self._table(self._run('bqueues', *args).decode())

    def busers(self, *args: str) -> Table[str]:
        '''Displays information about users and user groups
        '''
        return self._table(self._run('busers', *args).decode())

    def lsclusters(self, *args: str) -> Table[str]:
        '''Displays configuration information about LSF clusters
        '''
        return self._table(self._run('lsclusters', *args).decode())

    def lshosts(self, *args: str) -> Table[str]:
        '''Displays hosts and their static resource information
        '''
        return self._table(self._run('lshosts', *args).decode())

    def lsid(self) -> t.Dict[str, t.Optional[str]]:
        '''Displays the current LSF version number, the cluster name, and the master host name
        '''
        patterns = {
            'version': re.compile(r'(\d+\.){2,}\d+'),
            'date': re.compile(r'(?<=, )[a-zA-Z]+ \d{1,2} \d{4}(?=\n)'),
            'cluster': re.compile(r'(?<=My cluster name is )\S+(?=\n)'),
            'master': re.compile(r'(?<=My master name is )\S+(?=\n)'),
        }
        info = {'stdout': self._run('lsid').decode()}
        for key, pattern in patterns.items():
            match = pattern.search(info['stdout'])
            info[key] = None if match is None else match.group()
        return info

    def lsload(self, *args: str) -> Table[str]:
        '''Displays load information for hosts
        '''
        return self._table(self._run('lsload', *args).decode())

    def _run(self, *args: str) -> bytes:
        stdout, stderr = self._server._run(' '.join(map(str, args)))
        assert not stderr, stderr.decode()
        return stdout

    def _table(self, text: str) -> Table[str]:
        lines = text.splitlines()
        keys = lines[0].split()
        return [
            dict(zip(keys, line.split()))
            for line in lines[1:]
        ]
