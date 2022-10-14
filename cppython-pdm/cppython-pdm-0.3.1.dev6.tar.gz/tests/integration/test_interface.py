"""Integration tests for the interface
"""

import pytest
from pdm.core import Core
from pytest_cppython.plugin import InterfaceIntegrationTests
from pytest_mock import MockerFixture

from cppython_pdm.plugin import CPPythonPlugin


class TestCPPythonInterface(InterfaceIntegrationTests[CPPythonPlugin]):
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

    def test_entrypoint(self, mocker: MockerFixture) -> None:
        """Verify that this project's plugin hook is setup correctly

        Args:
            mocker: Mocker fixture for plugin patch
        """

        patch = mocker.patch("cppython_pdm.plugin.CPPythonPlugin")

        core = Core()
        core.load_plugins()

        assert patch.called
