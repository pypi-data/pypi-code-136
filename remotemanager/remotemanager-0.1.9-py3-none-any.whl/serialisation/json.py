import json

from remotemanager.utils import ensure_filetype
from remotemanager.serialisation.serial import serial


class serialjson(serial):
    """
    subclass of serial, implementing json methods
    """

    def dump(self, obj, file):
        file = ensure_filetype(file, self.extension)
        with open(file, 'w+') as ofile:
            json.dump(obj, ofile)

    def load(self, file):
        file = ensure_filetype(file, self.extension)
        with open(file, 'r') as ofile:
            data = json.load(ofile)
        return data

    @property
    def extension(self):
        return ".json"

    @property
    def importstring(self):
        return "import json"

    @property
    def callstring(self):
        return "json"
