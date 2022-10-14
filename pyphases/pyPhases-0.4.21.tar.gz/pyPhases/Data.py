import hashlib
import re

from pyPhases import Project
from pyPhases.util.Logger import classLogger
from pyPhases.util.Optionizable import Optionizable


class DataNotFound(Exception):
    pass


class Data(Optionizable):
    project: Project
    dataNames = {}
    version = "current"

    def flattenLongString(self, s: str):
        return hashlib.sha1(bytes(s, "utf-8")).hexdigest()[0:8]

    def hasTobeHashed(self, o):
        return isinstance(o, dict) or isinstance(o, list)

    def flatten(self, o) -> str:
        if self.hasTobeHashed(o):
            return self.flattenLongString(str(o))

        return None if o is None else re.sub("[^a-zA-Z0-9 ]", "-", str(o))

    @staticmethod
    def flattenConfigValues(o):
        return Data("").flatten(o)

    def __init__(self, name, dataTags=[]):
        self.name = name
        self.dataTags = dataTags
        Data.dataNames[name] = self

    def _getTagValue(self, tagname):
        # TODO: circle detection
        if tagname in Data.dataNames:
            tags = Data.dataNames[tagname].dataTags
            self.logDebug("Data %s depends on different dataset %s: %s" % (self.name, tagname, tags))
            return self.parseDatanames(Data.dataNames[tagname].dataTags)

        value = self.project.getConfig(tagname)
        flat = self.flatten(value)
        if self.hasTobeHashed(value):
            self.logDebug("config value %s has to be hashed: %s" % (tagname, flat))
        return flat

    def setProject(self, project):
        self.project = project

    def parseDatanames(self, tags):
        tagList = map(self._getTagValue, tags)
        return "-".join([t for t in tagList if t is not None])

    def getTagString(self):
        return self.parseDatanames(self.dataTags)

    def getDataName(self):
        return self.name + self.getTagString()

    def __str__(self):
        return self.getDataName()

    def getDataId(self):
        return self.getDataName() + "--" + self.version

    @staticmethod
    def create(val, project):
        dataObj = None
        if isinstance(val, Data):
            dataObj = val
        elif isinstance(val, str):
            dataObj = Data(val)
        else:
            raise Exception("Unsupported type as data identifier")

        dataObj.setProject(project)

        return dataObj

    @staticmethod
    def getFromName(name):
        if not name in Data.dataNames:
            raise Exception("The DataWrapper with name %s was not defined and does not exist in any phase" % (name))
        return Data.dataNames[name]
