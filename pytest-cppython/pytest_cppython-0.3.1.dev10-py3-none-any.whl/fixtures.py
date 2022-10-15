"""Direct Fixtures
"""

from pathlib import Path
from typing import Any, cast

import pytest
from cppython_core.resolution import (
    resolve_cppython,
    resolve_pep621,
    resolve_project_configuration,
)
from cppython_core.schema import (
    CoreData,
    CPPythonData,
    CPPythonGlobalConfiguration,
    CPPythonLocalConfiguration,
    PEP621Configuration,
    PEP621Data,
    ProjectConfiguration,
    ProjectData,
    PyProject,
    ToolData,
)

from pytest_cppython.data import (
    cppython_global_variants,
    cppython_local_variants,
    pep621_variants,
    project_variants,
)
from pytest_cppython.mock import MockGenerator, MockProvider


class CPPythonFixtures:
    """Fixtures available to CPPython test classes"""

    @pytest.fixture(
        name="install_path",
        scope="session",
    )
    def fixture_install_path(self, tmp_path_factory: pytest.TempPathFactory) -> Path:
        """Creates temporary install location
        Args:
            tmp_path_factory: Factory for centralized temporary directories
        Returns:
            A temporary directory
        """
        path = tmp_path_factory.getbasetemp()
        path.mkdir(parents=True, exist_ok=True)
        return path

    @pytest.fixture(
        name="pep621_configuration",
        scope="session",
        params=pep621_variants,
    )
    def fixture_pep621_configuration(self, request: pytest.FixtureRequest) -> PEP621Configuration:
        """Fixture defining all testable variations of PEP621

        Args:
            request: Parameterization list

        Returns:
            PEP621 variant
        """

        return cast(PEP621Configuration, request.param)

    @pytest.fixture(name="pep621_data")
    def fixture_pep621_data(
        self, pep621_configuration: PEP621Configuration, project_configuration: ProjectConfiguration
    ) -> PEP621Data:
        """Resolved project table fixture

        Args:
            pep621_configuration: The input configuration to resolve
            project_configuration: The project configuration to help with the resolve

        Returns:
            The resolved project table
        """

        return resolve_pep621(pep621_configuration, project_configuration)

    @pytest.fixture(
        name="cppython_local_configuration",
        scope="session",
        params=cppython_local_variants,
    )
    def fixture_cppython_local_configuration(
        self, request: pytest.FixtureRequest, install_path: Path
    ) -> CPPythonLocalConfiguration:
        """Fixture defining all testable variations of CPPythonData

        Args:
            request: Parameterization list
            install_path: The temporary install directory

        Returns:
            Variation of CPPython data
        """
        cppython_local_configuration = cast(CPPythonLocalConfiguration, request.param)

        data = cppython_local_configuration.dict(by_alias=True)

        # Pin the install location to the base temporary directory
        data["install-path"] = install_path

        return CPPythonLocalConfiguration(**data)

    @pytest.fixture(
        name="cppython_global_configuration",
        scope="session",
        params=cppython_global_variants,
    )
    def fixture_cppython_global_configuration(self, request: pytest.FixtureRequest) -> CPPythonGlobalConfiguration:
        """Fixture defining all testable variations of CPPythonData

        Args:
            request: Parameterization list

        Returns:
            Variation of CPPython data
        """
        cppython_global_configuration = cast(CPPythonGlobalConfiguration, request.param)

        return cppython_global_configuration

    @pytest.fixture(
        name="cppython_data",
    )
    def fixture_cppython_data(
        self,
        cppython_local_configuration: CPPythonLocalConfiguration,
        cppython_global_configuration: CPPythonGlobalConfiguration,
        project_data: ProjectData,
    ) -> CPPythonData:
        """Fixture for constructing resolved CPPython table data

        Args:
            cppython_local_configuration: The local configuration to resolve
            cppython_global_configuration: The global configuration to resolve
            project_data: The project data to help with the resolve

        Returns:
            The resolved CPPython table
        """

        return resolve_cppython(cppython_local_configuration, cppython_global_configuration, project_data)

    @pytest.fixture(
        name="core_data",
    )
    def fixture_core_data(
        self, cppython_data: CPPythonData, project_data: ProjectData, pep621_data: PEP621Data
    ) -> CoreData:
        """Fixture for creating the wrapper CoreData type

        Args:
            cppython_data: CPPython data
            project_data: The project data
            pep621_data: Project table data

        Returns:
            Wrapper Core Type
        """

        return CoreData(cppython_data=cppython_data, project_data=project_data, pep621_data=pep621_data)

    @pytest.fixture(name="project_configuration", params=project_variants)
    def fixture_project_configuration(
        self, request: pytest.FixtureRequest, tmp_path_factory: pytest.TempPathFactory
    ) -> ProjectConfiguration:
        """Project configuration fixture

        Args:
            request: Parameterized configuration data
            tmp_path_factory: Factory for centralized temporary directories


        Returns:
            Configuration with temporary directory capabilities
        """

        tmp_path = tmp_path_factory.mktemp("workspace-")
        pyproject_path = tmp_path / "test_project"
        pyproject_path.mkdir(parents=True)
        pyproject_file = pyproject_path / "pyproject.toml"
        pyproject_file.write_text("Test Project File", encoding="utf-8")

        configuration = cast(ProjectConfiguration, request.param)

        # Pin the project location
        configuration.pyproject_file = pyproject_file

        return configuration

    @pytest.fixture(name="project_data")
    def fixture_project_data(self, project_configuration: ProjectConfiguration) -> ProjectData:
        """Fixture that creates a project space at 'workspace/test_project/pyproject.toml'
        Args:
            project_configuration: Project data
        Returns:
            A project data object that has populated a function level temporary directory
        """

        return resolve_project_configuration(project_configuration)

    @pytest.fixture(name="project")
    def fixture_project(
        self, cppython_local_configuration: CPPythonLocalConfiguration, pep621_configuration: PEP621Configuration
    ) -> PyProject:
        """Parameterized construction of PyProject data
        Args:
            cppython_local_configuration: The parameterized cppython table
            pep621_configuration: The project table
        Returns:
            All the data as one object
        """

        tool = ToolData(cppython=cppython_local_configuration)
        return PyProject(project=pep621_configuration, tool=tool)

    @pytest.fixture(name="project_with_mocks")
    def fixture_project_with_mocks(self, project: PyProject) -> dict[str, Any]:
        """Extension of the 'project' fixture with mock data attached
        Args:
            project: The input project
        Returns:
            All the data as a dictionary
        """
        mocked_pyproject = project.dict(by_alias=True)
        mocked_pyproject["tool"]["cppython"]["provider"][MockProvider.name()] = {}
        mocked_pyproject["tool"]["cppython"]["generator"][MockGenerator.name()] = {}
        return mocked_pyproject
