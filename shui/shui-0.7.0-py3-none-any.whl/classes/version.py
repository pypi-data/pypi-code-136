"""Class to contain information about a Spark/Hadoop version"""
import re
from packaging.version import parse as version_parse


class Version:
    """Class to contain information about a Spark/Hadoop version"""

    regex = re.compile("spark-([0-9.]*)-bin-hadoop([0-9.]*).tgz$")

    def __init__(self, filename, url):
        self.filename = filename
        self.url = url

    @property
    def spark(self) -> str:
        """Spark version"""
        match = self.regex.match(self.filename)
        if not match:
            return ""
        return match.group(1)

    @property
    def hadoop(self) -> str:
        """Hadoop version"""
        match = self.regex.match(self.filename)
        if not match:
            return ""
        return match.group(2)

    def __str__(self) -> str:
        return f"<comment>Spark</comment> (<info>{self.spark}</info>) <comment>Hadoop</comment> (<info>{self.hadoop}</info>)"

    def __repr__(self) -> str:
        return f"<Version {self.filename} {self.url}>"

    def __lt__(self, other: "Version") -> bool:
        if version_parse(self.spark) != version_parse(other.spark):
            return version_parse(self.spark) < version_parse(other.spark)
        return version_parse(self.hadoop) < version_parse(other.hadoop)
