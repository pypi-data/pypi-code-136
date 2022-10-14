import yaml

from remotemanager.utils import ensure_filetype
from remotemanager.serialisation.serial import serial


class serialyaml(serial):
    """
    subclass of serial, implementing yaml methods
    """

    def dump(self, obj, file):
        file = ensure_filetype(file, self.extension)
        with open(file, 'w+') as ofile:
            yaml.dump(obj, ofile)

    def load(self, file):
        file = ensure_filetype(file, self.extension)
        with open(file, 'r') as ofile:
            data = yaml.safe_load(ofile)
        return data

    @property
    def extension(self):
        return ".yaml"

    @property
    def importstring(self):
        return "import yaml"

    @property
    def callstring(self):
        return "yaml"

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
        string = ["if isinstance(result, tuple):",
                  "\tresult = list(result)",
                  f"with open('{file}', 'w+') as o:",
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
                  f'\tloaded = {self.callstring}.safe_load(o)']
        return string
