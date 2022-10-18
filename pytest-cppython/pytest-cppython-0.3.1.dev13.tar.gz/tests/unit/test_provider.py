"""Test the functions related to the internal provider implementation and the 'Provider' interface itself
"""

from typing import Any

import pytest

from pytest_cppython.mock import MockProvider
from pytest_cppython.plugin import ProviderUnitTests


class TestMockProvider(ProviderUnitTests[MockProvider]):
    """The tests for our Mock provider"""

    @pytest.fixture(name="plugin_data", scope="session")
    def fixture_provider_data(self) -> dict[str, Any]:
        """Returns mock data

        Returns:
            An overridden data instance
        """

        return {}

    @pytest.fixture(name="plugin_type", scope="session")
    def fixture_plugin_type(self) -> type[MockProvider]:
        """A required testing hook that allows type generation

        Returns:
            An overridden provider type
        """
        return MockProvider

    def test_plugin_registration(self, plugin: MockProvider) -> None:
        """Override the base class 'ProviderIntegrationTests' preventing a registration check for the Mock

        Args:
            plugin: Required to override base function
        """
