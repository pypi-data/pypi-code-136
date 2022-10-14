import dill

from remotemanager.utils import ensure_filetype
from remotemanager.serialisation.serial import serial


class serialdill(serial):
    """
    subclass of serial, implementing dill methods
    """

    def dump(self, obj, file):
        file = ensure_filetype(file, self.extension)
        with open(file, 'wb+') as ofile:
            dill.dump(obj, ofile)

    def load(self, file):
        file = ensure_filetype(file, self.extension)
        with open(file, 'rb') as ofile:
            data = dill.load(ofile)
        return data

    @property
    def extension(self):
        return ".dill"

    @property
    def importstring(self):
        return "import dill"

    @property
    def callstring(self):
        return "dill"

    def dumpstring(self, file):
        file = ensure_filetype(file, self.extension)
        string = [f"with open('{file}', 'wb+') as o:",
                  f'\t{self.callstring}.dump(result, o)']
        return string
