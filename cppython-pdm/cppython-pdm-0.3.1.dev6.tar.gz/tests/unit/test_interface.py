"""Unit tests for the interface
"""

from pathlib import Path

import pytest
from cppython_core.exceptions import PluginError
from cppython_core.schema import PyProject
from pdm.core import Core
from pytest_cppython.plugin import InterfaceUnitTests
from pytest_mock.plugin import MockerFixture

from cppython_pdm.plugin import CPPythonPlugin


class TestCPPythonInterface(InterfaceUnitTests[CPPythonPlugin]):
    """The tests for the PDM interface"""

    @pytest.fixture(name="plugin_type")
    def fixture_plugin_type(self) -> type[CPPythonPlugin]:
        """A required testing hook that allows type generation

        Returns:
            The plugin type
        """

        return CPPythonPlugin

    @pytest.fixture(name="interface")
    def fixture_interface(self, plugin_type: type[CPPythonPlugin]) -> CPPythonPlugin:
        """A hook allowing implementations to override the fixture

        Args:
            plugin_type: An input interface type

        Returns:
            A newly constructed interface
        """
        return plugin_type(Core())

    def test_install(self, project: PyProject, interface: CPPythonPlugin, mocker: MockerFixture) -> None:
        """Tests the post install path

        Args:
            project: Mock project
            interface: The constructed plugin
            mocker: Mocker fixture for project mocking
        """

        pdm_project = mocker.MagicMock()
        pdm_project.core.ui.verbosity = 0
        pdm_project.core.version = "1.0.0"
        pdm_project.pyproject_file = Path("pyproject.toml")
        pdm_project.pyproject = project.dict(by_alias=True)

        with pytest.raises(PluginError):
            interface.on_post_install(project=pdm_project, candidates={}, dry_run=False)
