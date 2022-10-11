"""
Handles file transfer via the `rsync` protocol
"""
import logging

from remotemanager.transport.transport import Transport
from remotemanager.utils.flags import Flags


class rsync(Transport):
    def __init__(self, *args, **kwargs):

        # flags can be exposed, to utilise their flexibility
        flags = kwargs.pop('flags', 'auv')
        self.flags = Flags(flags)

        super().__init__(*args, **kwargs)

        self._logger.info('created new rsync transport')

        self._cmd = 'rsync {flags} {primary}{files} {secondary}'

    @property
    def cmd(self):
        base = self._cmd.format(flags=self.flags.flags,
                                primary='{primary}',
                                files='{files}',
                                secondary='{secondary}')
        self._logger.debug(f'returning semi-formatted cmd: "{base}"')
        return base
