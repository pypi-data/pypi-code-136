"""Helper fixtures and plugin definitions for pytest
"""

import asyncio
from abc import ABC, abstractmethod
from importlib.metadata import entry_points
from pathlib import Path
from typing import Any, Generic

import pytest
from cppython_core.plugin_schema.generator import GeneratorData, GeneratorT
from cppython_core.plugin_schema.interface import InterfaceT
from cppython_core.plugin_schema.provider import ProviderData, ProviderT
from cppython_core.plugin_schema.vcs import VersionControlT
from cppython_core.resolution import (
    resolve_cppython_plugin,
    resolve_generator,
    resolve_provider,
)
from cppython_core.schema import (
    CorePluginData,
    CPPythonData,
    CPPythonPluginData,
    DataPluginT,
    PEP621Data,
    PluginGroupDataT,
    PluginT,
    ProjectData,
)
from packaging.utils import canonicalize_name

from pytest_cppython.fixtures import CPPythonFixtures


class PluginTests(CPPythonFixtures, ABC, Generic[PluginT]):
    """Shared testing information for all plugin test classes"""

    @abstractmethod
    @pytest.fixture(name="plugin_type", scope="session")
    def fixture_plugin_type(self) -> type[PluginT]:
        """A required testing hook that allows type generation"""

        raise NotImplementedError("Subclasses should override this fixture")


class PluginIntegrationTests(PluginTests[PluginT]):
    """Integration testing information for all plugin test classes"""


class PluginUnitTests(PluginTests[PluginT]):
    """Unit testing information for all plugin test classes"""

    def test_name(self, plugin_type: PluginT) -> None:
        """Validates the name

        Args:
            plugin_type: The input plugin type
        """

        assert plugin_type.name() == canonicalize_name(plugin_type.name())


class DataPluginTests(PluginTests[DataPluginT], Generic[PluginGroupDataT, DataPluginT]):
    """Shared testing information for all data plugin test classes"""

    @pytest.fixture(name="cppython_plugin_data")
    def fixture_cppython_plugin_data(
        self, cppython_data: CPPythonData, plugin_type: type[DataPluginT]
    ) -> CPPythonPluginData:
        """Fixture for created the plugin CPPython table

        Args:
            cppython_data: The CPPython table to help the resolve
            plugin_type: The data plugin type to resolve

        Returns:
            The plugin specific CPPython table information
        """

        return resolve_cppython_plugin(cppython_data, plugin_type)

    @pytest.fixture(
        name="core_plugin_data",
    )
    def fixture_core_plugin_data(
        self, cppython_plugin_data: CPPythonPluginData, project_data: ProjectData, pep621_data: PEP621Data
    ) -> CorePluginData:
        """Fixture for creating the wrapper CoreData type

        Args:
            cppython_plugin_data: CPPython data
            project_data: The project data
            pep621_data: Project table data

        Returns:
            Wrapper Core Type
        """

        return CorePluginData(cppython_data=cppython_plugin_data, project_data=project_data, pep621_data=pep621_data)

    @staticmethod
    @pytest.fixture(name="plugin")
    def fixture_plugin(
        plugin_type: type[DataPluginT],
        plugin_group_data: PluginGroupDataT,
        core_plugin_data: CorePluginData,
        plugin_data: dict[str, Any],
    ) -> DataPluginT:
        """Overridden plugin generator for creating a populated data plugin type

        Args:
            plugin_type: Plugin type
            plugin_group_data: The data group configuration
            core_plugin_data: The core metadata
            plugin_data: The data table

        Returns:
            A newly constructed provider
        """

        return plugin_type(plugin_group_data, core_plugin_data, plugin_data)


class DataPluginIntegrationTests(
    PluginIntegrationTests[DataPluginT],
    DataPluginTests[PluginGroupDataT, DataPluginT],
    Generic[PluginGroupDataT, DataPluginT],
):
    """Integration testing information for all data plugin test classes"""


class DataPluginUnitTests(
    PluginUnitTests[DataPluginT],
    DataPluginTests[PluginGroupDataT, DataPluginT],
    Generic[PluginGroupDataT, DataPluginT],
):
    """Unit testing information for all data plugin test classes"""

    def test_plugin_registration(self, plugin: DataPluginT) -> None:
        """Test the registration with setuptools entry_points

        Args:
            plugin: A newly constructed provider
        """
        plugin_entries = entry_points(group=f"cppython.{plugin.group()}")
        assert len(plugin_entries) > 0


class InterfaceTests(PluginTests[InterfaceT]):
    """Shared functionality between the different Interface testing categories"""

    @pytest.fixture(name="plugin")
    def fixture_plugin(self, plugin_type: type[InterfaceT]) -> InterfaceT:
        """Fixture creating the interface.
        Args:
            plugin_type: An input interface type
        Returns:
            A newly constructed interface
        """
        return plugin_type()


class InterfaceIntegrationTests(PluginIntegrationTests[InterfaceT], InterfaceTests[InterfaceT], Generic[InterfaceT]):
    """Base class for all interface integration tests that test plugin agnostic behavior"""


class InterfaceUnitTests(PluginUnitTests[InterfaceT], InterfaceTests[InterfaceT], Generic[InterfaceT]):
    """Custom implementations of the Interface class should inherit from this class for its tests.
    Base class for all interface unit tests that test plugin agnostic behavior
    """


class ProviderTests(DataPluginTests[ProviderData, ProviderT], Generic[ProviderT]):
    """Shared functionality between the different Provider testing categories"""

    @pytest.fixture(name="plugin_configuration_type", scope="session")
    def fixture_plugin_configuration_type(self) -> type[ProviderData]:
        """A required testing hook that allows plugin configuration data generation

        Returns:
            The configuration type
        """

        return ProviderData

    @pytest.fixture(name="plugin_group_data")
    def fixture_plugin_group_data(self, project_data: ProjectData) -> ProviderData:
        """Generates plugin configuration data generation from environment configuration

        Args:
            project_data: The workspace configuration

        Returns:
            The plugin configuration
        """

        return resolve_provider(project_data)


class ProviderIntegrationTests(
    DataPluginIntegrationTests[ProviderData, ProviderT],
    ProviderTests[ProviderT],
    Generic[ProviderT],
):
    """Base class for all provider integration tests that test plugin agnostic behavior"""

    @pytest.fixture(autouse=True, scope="session")
    def _fixture_install_dependency(self, plugin_type: type[ProviderT], install_path: Path) -> None:
        """Forces the download to only happen once per test session"""

        path = install_path / plugin_type.name()
        path.mkdir(parents=True, exist_ok=True)

        asyncio.run(plugin_type.download_tooling(path))

    def test_is_downloaded(self, plugin: ProviderT) -> None:
        """Verify the plugin is downloaded from fixture

        Args:
            plugin: A newly constructed provider
        """

        assert plugin.tooling_downloaded(plugin.core_data.cppython_data.install_path)

    def test_not_downloaded(self, plugin_type: type[ProviderT], tmp_path: Path) -> None:
        """Verify the provider can identify an empty tool

        Args:
            plugin_type: An input provider type
            tmp_path: A temporary path for the lifetime of the function
        """

        assert not plugin_type.tooling_downloaded(tmp_path)

    def test_install(self, plugin: ProviderT) -> None:
        """Ensure that the vanilla install command functions

        Args:
            plugin: A newly constructed provider
        """
        plugin.install()

    def test_update(self, plugin: ProviderT) -> None:
        """Ensure that the vanilla update command functions

        Args:
            plugin: A newly constructed provider
        """
        plugin.update()


class ProviderUnitTests(
    DataPluginUnitTests[ProviderData, ProviderT],
    ProviderTests[ProviderT],
    Generic[ProviderT],
):
    """Custom implementations of the Provider class should inherit from this class for its tests.
    Base class for all provider unit tests that test plugin agnostic behavior
    """


class GeneratorTests(DataPluginTests[GeneratorData, GeneratorT], Generic[GeneratorT]):
    """Shared functionality between the different Generator testing categories"""

    @pytest.fixture(name="plugin_configuration_type", scope="session")
    def fixture_plugin_configuration_type(self) -> type[GeneratorData]:
        """A required testing hook that allows plugin configuration data generation

        Returns:
            The configuration type
        """

        return GeneratorData

    @pytest.fixture(name="plugin_group_data")
    def fixture_plugin_group_data(self, project_data: ProjectData) -> GeneratorData:
        """Generates plugin configuration data generation from environment configuration

        Args:
            project_data: The workspace configuration

        Returns:
            The plugin configuration
        """

        return resolve_generator(project_data)


class GeneratorIntegrationTests(
    DataPluginIntegrationTests[GeneratorData, GeneratorT],
    GeneratorTests[GeneratorT],
    Generic[GeneratorT],
):
    """Base class for all vcs integration tests that test plugin agnostic behavior"""


class GeneratorUnitTests(
    DataPluginUnitTests[GeneratorData, GeneratorT],
    GeneratorTests[GeneratorT],
    Generic[GeneratorT],
):
    """Custom implementations of the Generator class should inherit from this class for its tests.
    Base class for all Generator unit tests that test plugin agnostic behavior"""


class VersionControlTests(
    PluginTests[VersionControlT],
    Generic[VersionControlT],
):
    """Shared functionality between the different VersionControl testing categories"""

    @pytest.fixture(name="plugin")
    def fixture_plugin(self, plugin_type: type[VersionControlT]) -> VersionControlT:
        """Fixture creating the plugin.
        Args:
            plugin_type: An input plugin type
        Returns:
            A newly constructed plugin
        """
        return plugin_type()


class VersionControlIntegrationTests(
    PluginIntegrationTests[VersionControlT],
    VersionControlTests[VersionControlT],
    Generic[VersionControlT],
):
    """Base class for all generator integration tests that test plugin agnostic behavior"""


class VersionControlUnitTests(
    PluginUnitTests[VersionControlT],
    VersionControlTests[VersionControlT],
    Generic[VersionControlT],
):
    """Custom implementations of the Generator class should inherit from this class for its tests.
    Base class for all Generator unit tests that test plugin agnostic behavior
    """

    def test_not_repository(self, plugin: VersionControlT, tmp_path: Path) -> None:
        """Tests that the temporary directory path will not be registered as a repository

        Args:
            plugin: The VCS constructed type
            tmp_path: Temporary directory
        """

        assert not plugin.is_repository(tmp_path)
