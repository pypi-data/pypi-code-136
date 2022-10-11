"""
Baseclass for any file transfer
"""
import os.path

from remotemanager.connection.cmd import CMD
from remotemanager.connection.url import URL
from remotemanager.storage.sendablemixin import SendableMixin
from remotemanager.logging.utils import format_iterable
from remotemanager.utils import ensure_list, ensure_dir
from remotemanager.logging import LoggingMixin


class Transport(SendableMixin, LoggingMixin):
    """
    Baseclass for file transfer

    Args:
        url (URL):
            url to extract remote address from
    """

    def __init__(self,
                 url: URL = None,
                 *args,
                 **kwargs):

        self._remote_address = None
        self.set_remote(url)

        self._transfers = {}

    def queue_for_push(self,
                       files: list,
                       local: str = None,
                       remote: str = None):
        """
        Queue file(s) for sending (pushing)

        Args:
            files (list[str], str):
                list of files (or file) to add to push queue
            local (str):
                local/origin folder for the file(s)
            remote (str):
                remote/destination folder for the file(s)
        Returns:
            None
        """
        self._logger.info(f'adding to PUSH queue')
        self.add_transfer(files, local, remote, 'push')

    def queue_for_pull(self,
                       files: list,
                       local: str = None,
                       remote: str = None):
        """
        Queue file(s) for retrieving (pulling)

        Args:
            files (list[str], str):
                list of files (or file) to add to pull queue
            local (str):
                local/destination folder for the file(s)
            remote (str):
                remote/origin folder for the file(s)
        Returns:
            None
        """
        self._logger.info(f'adding to PULL queue')
        self.add_transfer(files, remote, local, 'pull')

    def add_transfer(self,
                     files: list,
                     origin: str,
                     target: str,
                     mode: str):
        """
        Create a transfer to be executed. The ordering of the origin/target
        files should be considered as this transport instance being a
        "tunnel" between wherever it is executed (origin), and the destination
        (target)

        Args:
            files (list[str], str):
                list of files (or file) to add to pull queue
            origin (str):
                origin folder for the file(s)
            target (str):
                target folder for the file(s)
            mode (str: "push" or "pull"):
                transfer mode. Chooses where the remote address is placed
        Returns:
            None
        """
        modes = ('push', 'pull')
        if mode.lower() not in modes:
            raise ValueError(f'mode must be one of {modes}')

        if origin is None:
            origin = '.'
        if target is None:
            target = '.'

        # ensure dir-type
        origin = os.path.join(origin, '')
        target = os.path.join(target, '')

        if mode == 'push':
            pair = f'{origin}>{self._add_address(target)}'
        else:
            pair = f'{self._add_address(origin)}>{target}'

        files = [os.path.split(f)[1] for f in ensure_list(files)]

        self._logger.info(f'adding transfer: {split_pair(pair)[0]} '
                          f'-> {split_pair(pair)[1]}')
        self._logger.info(f'for files {files}')

        if pair in self._transfers:
            self._transfers[pair] = self._transfers[pair].union(set(files))
        else:
            self._transfers[pair] = set(files)

    def _add_address(self, dir: str) -> str:
        """
        Adds the remote address to the dir `dir` if it exists

        Args:
            dir (str):
                remote dir to have address appended

        Returns:
            (str) dir
        """
        if self.address is None:
            return dir
        return f'{self.address}:{dir}'

    @staticmethod
    def _format_for_cmd(inp: list) -> str:
        """
        Formats a list into a bash expandable command with brace expansion

        Args:
            inp (list):
                list of items to compress

        Returns (str):
            formatted cmd
        """

        if isinstance(inp, str):
            raise ValueError('files is stringtype, '
                             'was a transfer forced into the queue?')
        if len(inp) > 1:
            return '{' + ','.join(inp) + '}'
        return inp[0]

    @property
    def transfers(self) -> dict:
        """
        Return the current transfer dict

        Returns (dict):
            {paths: files} transfer dict
        """
        return {k: sorted(list(v)) for k, v in self._transfers.items()}

    def print_transfers(self):
        """
        Print a formatted version of the current queued transfers

        Returns:
            None
        """
        i = 0
        for pair, files in self.transfers.items():
            i += 1
            print(f'transfer {i}:'
                  f'\norigin: {split_pair(pair)[0]}'
                  f'\ntarget: {split_pair(pair)[1]}')
            j = 0
            for file in files:
                j += 1
                print(f'\t({j}/{len(files)}) {file}')

    @property
    def address(self):
        """
        return the remote address

        Returns (str):
            the remote address
        """
        return self._remote_address

    @address.setter
    def address(self, remote_address):
        """
        set the remote address

        Returns:
            None
        """
        self._remote_address = remote_address

    def set_remote(self,
                   url: URL = None):
        """
        set the remote address with a URL object

        Returns:
            None
        """
        if url is None:
            self._remote_address = None
        elif url.is_local:
            self._remote_address = None
        else:
            self._remote_address = url.userhost

    @property
    def cmd(self):
        """
        Returns a semi formatted command for issuing transfers. It is left to
        the developer to implement this method when adding more transport
        classes

        Returns (str):
            the semi-formatted command for issuing a transfer
        """
        raise NotImplementedError

    def transfer(self,
                 dry_run: bool = False):
        """
        Perform the actual transfer

        Args:
            dry_run (bool):
                do not perform command, just return the command(s) to be
                executed

        Returns (str, None):
            the dry run string, or None
        """

        self._logger.info(f'executing a transfer')

        commands = []
        for pair, files in self.transfers.items():

            filestr = self._format_for_cmd(files)

            primary = ensure_dir(os.path.split(split_pair(pair)[0])[0])
            secondary = ensure_dir(os.path.split(split_pair(pair)[1])[0])

            base_cmd = self.cmd.format(primary=primary,
                                       secondary=secondary,
                                       files=filestr)

            commands.append(base_cmd)

        if dry_run:
            return commands

        for cmd in commands:
            CMD(cmd).exec()
            # wipe the transfer queue
            self.wipe_transfers()

    def wipe_transfers(self):
        self._logger.info('wiping transfers')
        self._transfers = {}


def split_pair(pair: str) -> list:
    """
    Convert a "dir>dir" string into list format

    Args:
        pair (tuple):
            (dir, dir) tuple to be split

    Returns (list):
        [dir, dir]

    """
    return pair.split('>')
