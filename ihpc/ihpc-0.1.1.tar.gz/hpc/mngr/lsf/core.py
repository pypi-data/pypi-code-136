__all__ = ['LSF']


import typing as t

from .extra import command
from ... import impl

if t.TYPE_CHECKING:
    from typing_extensions import Self

    from ...base.core import Server


class LSF(impl._.Generic):
    '''IBM Platform LSF (load sharing facility)

    - Reference:
        - https://www.ibm.com/docs/en/spectrum-lsf/10.1.0
    '''

    __version__ = '10.1.0'

    def __init__(self, server: 'Server') -> None:
        self._server = server
        self._cmd = None

    @classmethod
    def from_server(cls, server: 'Server') -> 'Self':
        return cls(server)

    @property
    def cmd(self) -> command.Command:
        if self._cmd is None:
            self._cmd = command.Command.from_lsf(self)
        return self._cmd
