"""Implementation of the PDM Interface Plugin
"""

from typing import Any

from cppython.project import Project as CPPythonProject
from cppython_core.plugin_schema.interface import Interface
from cppython_core.schema import ProjectConfiguration
from pdm.core import Core
from pdm.project.core import Project
from pdm.signals import post_install


class CPPythonPlugin(Interface):
    """Implementation of the PDM Interface Plugin"""

    def __init__(self, _core: Core) -> None:
        post_install.connect(self.on_post_install, weak=False)

    @staticmethod
    def name() -> str:
        """Name of the plugin

        Returns:
            The name
        """
        return "pdm"

    def write_pyproject(self) -> None:
        """Write to file"""

    def on_post_install(self, project: Project, dry_run: bool, **_kwargs: Any) -> None:
        """Called after a pdm install command is called

        Args:
            project: The input PDM project
            dry_run: If true, won't perform any actions
            _kwargs: Sink for unknown arguments
        """

        pyproject_file = project.pyproject_file.absolute()

        # Attach configuration for CPPythonPlugin callbacks
        project_configuration = ProjectConfiguration(pyproject_file=pyproject_file, version=project.core.version)
        project_configuration.verbosity = project.core.ui.verbosity

        logger = self.logger()
        logger.info("CPPython: Entered 'on_post_install'")

        if (pdm_pyproject := project.pyproject) is None:
            logger.info("CPPython: Project data was not available")
            return

        cppython_project = CPPythonProject(project_configuration, self, pdm_pyproject)

        if not dry_run:
            cppython_project.install()
