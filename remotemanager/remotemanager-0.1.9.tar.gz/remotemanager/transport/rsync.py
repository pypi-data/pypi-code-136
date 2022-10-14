"""
Handles file transfer via the `rsync` protocol
"""
import logging

from remotemanager.transport.transport import Transport


class rsync(Transport):
    """
    Adds checksum arg, which if True will add --checksum flag to parameters
    """
    def __init__(self,
                 *args,
                 **kwargs):

        super().__init__(*args, **kwargs)

        # flags can be exposed, to utilise their flexibility
        flags = kwargs.pop('flags', 'auv')
        self.flags = flags

        if kwargs.get('checksum', False):
            print('adding checksum to rsync')
            self.flags += '--checksum'

        self._logger.info('created new rsync transport')

        self._cmd = 'rsync {flags} {primary}{files} {secondary}'

    @property
    def cmd(self):
        base = self._cmd.format(flags=self.flags,
                                primary='{primary}',
                                files='{files}',
                                secondary='{secondary}')
        self._logger.debug(f'returning semi-formatted cmd: "{base}"')
        return base
