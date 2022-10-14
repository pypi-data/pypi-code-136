from remotemanager.utils import ensure_filetype
from remotemanager.storage.sendablemixin import SendableMixin


class serial(SendableMixin):

    """
    Baseclass for holding serialisation methods. Subclass this class when
    implementing new serialisation methods
    """

    def __init__(self):
        pass

    def dump(self, obj, file: str) -> None:
        """
        Dumps object `obj` to file `file`

        Args:
            obj:
                object to be dumped
            file (str):
                filepath to dump to

        Returns:
            None
        """
        raise NotImplementedError

    def load(self, file: str):
        """
        Loads previously dumped data from file `file`

        Args:
            file (str):
                filepath to load

        Returns:
            Stored object
        """
        raise NotImplementedError

    @property
    def extension(self) -> str:
        """
        Returns (str):
            intended file extension
        """
        raise NotImplementedError

    @property
    def importstring(self) -> str:
        """
        Returns (str):
            Module name to import.
            See subclasses for examples
        """
        raise NotImplementedError

    @property
    def callstring(self) -> str:
        """
        Returns (str):
            Intended string for calling this module's dump.
            See subclasses for examples
        """
        raise NotImplementedError

    def dumpstring(self, file: str) -> list:
        """
        Python code for dumping an object named `result`

        Args:
            file (str):
                filename to dump to

        Returns (list):
            Formatted list of strings for run files.
            See subclasses for examples
        """
        file = ensure_filetype(file, self.extension)
        string = [f"with open('{file}', 'w+') as o:",
                  f'\t{self.callstring}.dump(result, o)']
        return string

    def loadstring(self, file: str) -> list:
        """
        Python code for loading an object from file `file` into object named
        `loaded`

        Args:
            file (str):
                filename to load from

        Returns (list):
            Formatted list of strings for run files.
            See subclasses for examples
        """
        file = ensure_filetype(file, self.extension)
        string = [f"with open('{file}', 'r') as o:",
                  f'\tloaded = {self.callstring}.load(o)']
        return string

