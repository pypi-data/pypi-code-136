import re
from os.path import split
from typing import List


class BaseSqlNode:
    """Node representing SQL object and a method to initalise dependencies."""

    dependency_regex_pattern = None

    def __init__(self, file_path: str) -> None:
        _, self.name = split(file_path)
        self.file_path = file_path
        self.dependencies = self.detect_dependencies()

    def detect_dependencies(self) -> List:
        """returns a list of sql objects that the node is dependent on.

        Raises:
            TypeError: raised if regex pattern not set.

        Returns:
            List: dependencies.
        """
        with open(self.file_path) as f:
            data = "".join(f.read().splitlines())

        if self.dependency_regex_pattern is None:
            raise TypeError("Dependency regex pattern not defined")
        pattern = re.compile(self.dependency_regex_pattern)

        return re.findall(pattern, data)


class ViewNode(BaseSqlNode):
    """Represents database view and materliazed view objects."""

    dependency_regex_pattern = "(?<=join )vw_\w+|mvw_\w+|(?<=from )vw_\w+|mvw_\w+"
