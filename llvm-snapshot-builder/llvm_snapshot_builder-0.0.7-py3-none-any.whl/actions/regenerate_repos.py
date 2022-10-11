"""
CoprActionRegenerateRepos
"""

from typing import Union
from ..mixins.build_walker_mixin import CoprBuildWalkerMixin
from ..mixins.client_mixin import CoprClientMixin
from ..copr_project_ref import CoprProjectRef
from .action import CoprAction


class CoprActionRegenerateRepos(CoprClientMixin, CoprAction):
    """
    Regenerates the repositories for the given project.
    NOTE: The regeneration of repository data is not finished when this function returns.
    """

    def __init__(self, proj: Union[CoprProjectRef, str], ** kwargs):
        """ Initializes the action. """
        self.__proj = CoprProjectRef(proj)
        super().__init__(**kwargs)

    def run(self) -> bool:
        """ Runs the action. """
        self.client.project_proxy.regenerate_repos(
            ownername=self.__proj.owner, projectname=self.__proj.name)
        return True
