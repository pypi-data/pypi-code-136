"""Shared definitions for testing.
"""

from pathlib import Path

from cppython_core.plugin_schema.generator import Generator
from cppython_core.plugin_schema.interface import Interface
from cppython_core.plugin_schema.provider import Provider
from cppython_core.plugin_schema.vcs import VersionControl


class MockInterface(Interface):
    """A mock interface class for behavior testing"""

    @staticmethod
    def name() -> str:
        """The name of the plugin, canonicalized

        Returns:
            Plugin name
        """
        return "mock"

    def write_pyproject(self) -> None:
        """Implementation of Interface function"""


class MockProvider(Provider):
    """A mock provider class for behavior testing"""

    downloaded: Path | None = None

    @staticmethod
    def name() -> str:
        """The name of the plugin, canonicalized

        Returns:
            The plugin name
        """
        return "mock"

    @classmethod
    def tooling_downloaded(cls, path: Path) -> bool:
        """Returns whether the provider tooling needs to be downloaded

        Args:
            path: The directory to check for downloaded tooling

        Returns:
            Whether the tooling has been downloaded or not
        """
        return cls.downloaded == path

    @classmethod
    async def download_tooling(cls, path: Path) -> None:
        cls.downloaded = path

    def install(self) -> None:
        pass

    def update(self) -> None:
        pass


class MockGenerator(Generator):
    """A mock generator class for behavior testing"""

    @staticmethod
    def name() -> str:
        """The plugin name

        Returns:
            The name
        """
        return "mock"


class MockVersionControl(VersionControl):
    """A mock generator class for behavior testing"""

    @staticmethod
    def name() -> str:
        """The plugin name

        Returns:
            The name
        """
        return "mock"

    def extract_version(self, path: Path) -> str:
        """Extracts the system's version metadata

        Args:
            path: The repository path

        Returns:
            A version
        """
        return "1.0.0"

    def is_repository(self, path: Path) -> bool:
        """Queries repository status of a path

        Args:
            path: The input path to query

        Returns:
            Whether the given path is a repository root
        """
        return False
