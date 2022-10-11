"""
CoprActionMakeOrEditProject
"""

import logging
from typing import Union
from ..mixins.client_mixin import CoprClientMixin
from ..copr_project_ref import CoprProjectRef
from .action import CoprAction


class CoprActionMakeOrEditProject(CoprAction, CoprClientMixin):
    """
    Make or edits a project

    Attributes:

        default_chroots (list): The default chroots to use for the project when creating
        runtime_dependencies (list): List of external repositories (== dependencies, specified as baseurls) that will be automatically enabled together with this project repository.
    """

    default_chroots = ["fedora-rawhide-x86_64"]
    runtime_dependencies = "https://download.copr.fedorainfracloud.org/results/%40fedora-llvm-team/llvm-compat-packages/fedora-$releasever-$basearch"

    def __init__(self,
                 proj: Union[CoprProjectRef, str],
                 description: str = "",
                 instructions: str = "",
                 chroots: list[str] = None,
                 delete_after_days: int = 0, **kwargs):
        """
        Initialize the make or edit project action.

        Args:
            proj (CoprProjectRef): The owner/project reference to create/edit
            description (str): A descriptive text of the project to create or edit
            instructions (str): A text for the instructions of how to enable this project
            delete_after_days (int): How many days the project shall be kept (0 equals indefinite)
            chroots (list[str]): What change roots shall be used for the project. Defaults to default_chroots (only upon creation).
        """
        self.__proj = CoprProjectRef(proj)
        self.__description = description
        self.__instructions = instructions
        self.__delete_after_days = delete_after_days
        if chroots is None or len(chroots) == 0:
            chroots = self.default_chroots
        self.__chroots = chroots
        super().__init__(**kwargs)

    def run(self) -> bool:
        """ Runs the action. """
        existingprojects = self.client.project_proxy.get_list(
            self.__proj.owner)
        existingproject_names = [p.name for p in existingprojects]

        delete_after_days = None if self.__delete_after_days == 0 else self.__delete_after_days
        if self.__proj.name in existingproject_names:
            logging.info(f"found project {self.__proj}, updating...")

            chroots = [] if self.__chroots is None else self.__chroots

            # First get existing chroots and only add new ones
            project = self.client.project_proxy.get(
                ownername=self.__proj.owner, projectname=self.__proj.name)
            existing_chroots = project.chroot_repos.keys()
            new_chroots = set(existing_chroots)

            diff_chroots = set(chroots).difference(new_chroots)
            if diff_chroots != set():
                logging.info(
                    f"add these chroots to the project: {diff_chroots}")
            new_chroots.update(chroots)

            self.client.project_proxy.edit(
                ownername=self.__proj.owner,
                projectname=self.__proj.name,
                description=self.__description,
                instructions=self.__instructions,
                enable_net=True,
                multilib=True,
                chroots=list(new_chroots),
                devel_mode=True,
                appstream=False,
                runtime_dependencies=self.runtime_dependencies,
                delete_after_days=delete_after_days)
            return True

        logging.info(f"create project {self.__proj}")
        # NOTE: devel_mode=True means that one has to manually create the
        # repo.

        self.client.project_proxy.add(
            ownername=self.__proj.owner,
            projectname=self.__proj.name,
            chroots=self.__chroots,
            description=self.__description,
            instructions=self.__instructions,
            enable_net=True,
            multilib=True,
            devel_mode=True,
            appstream=False,
            runtime_dependencies=self.runtime_dependencies,
            delete_after_days=delete_after_days)
        return True
