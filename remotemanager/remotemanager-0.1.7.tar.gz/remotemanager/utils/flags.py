import logging
import re

from remotemanager.storage.sendablemixin import SendableMixin


class Flags(SendableMixin):
    """
    Basic but flexible handler for terminal command flags

    Allows for inplace modification:

    >>> f = Flags('abcdd')
    >>> f -= 'd'
    >>> f.flags
    >>> '-abcd'

    Arguments:
        initial_flags (str):
            initial base flags to be used and modified if needed
        prefix (optional, str):
            the non-argument prefix for these flags (`-`, `--`, etc.)
    """

    _logger = logging.getLogger(__name__ + '.Flags')

    def __init__(self, initial_flags: str = '', prefix: str = None):

        self._logger.debug(f'creating Flags with initial flags '
                           f'{initial_flags} and prefix {prefix}')

        self._prefix = ''
        if prefix is None:
            if '-' in initial_flags:
                self.prefix = '-' * initial_flags.count('-')
            else:
                self.prefix = '-'
            self._logger.debug(f'prefix set to {self.prefix}')
        else:
            self.prefix = prefix
            initial_flags = strip_non_alphanumeric(initial_flags)

        self.flags = initial_flags

    def __repr__(self):
        return f'Flags({self.flags})'

    def __add__(self, other):
        self._flags = self._flags + other.strip('-')
        self._logger.debug(f'adding {other} to flags. '
                           f'Flags are now {self.flags}')

    def __iadd__(self, other):
        self.__add__(other)
        self._logger.debug(f'adding {other} to flags inplace. '
                           f'Flags are now {self.flags}')
        return self

    def __sub__(self, other):
        """Subtract unique flags in `other` once."""
        for char in ''.join(set(other)):
            self._flags = self._flags.replace(char, '', 1)
        self._logger.debug(f'subtracting {other} from flags. '
                           f'Flags are now {self.flags}')

    def __isub__(self, other):
        self.__sub__(other)
        self._logger.debug(f'subtracting {other} from flags inplace. '
                           f'Flags are now {self.flags}')
        return self

    @property
    def flags(self):
        """Returns the fully qualified flags as a string"""
        if len(self._flags) == 0:
            return ''
        return self.prefix + self._flags

    @flags.setter
    def flags(self, inp):
        """Set the flags to the new input

        Arguments:
            inp (str):
                new flags to use (will overwrite old ones)
        """
        self._logger.debug(f'setting flags to {inp}')
        for char in set(self.prefix):
            inp = inp.strip(char)
        self._logger.debug(f'after cleaning, flags are now: {inp}')
        self._flags = inp

    @property
    def prefix(self):
        """
        Attribute determining the - prefix used for these flags

        For example, a flag with a prefix of `-` will be added as `-flag`
        Change the prefix to `--` to be passed as `--flag`, and so on
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        self._prefix = prefix


def strip_non_alphanumeric(string):
    """
    remove any non-alphanumeric strings from input string

    Args:
        string (str):
            input string

    Returns (str):
        input string, sans any non-alphanumeric chars

    """
    pattern = re.compile('[\W_]+', re.UNICODE)

    return pattern.sub('', string)
