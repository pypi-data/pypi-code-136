"""
CoprActionDeleteProject
"""

from copr.v3 import CoprNoResultException
from ..mixins.client_mixin import CoprClientMixin
from .cancel_builds import CoprActionCancelBuilds
from ..copr_project_ref import CoprProjectRef
from .action import CoprAction


class CoprActionDeleteProject(CoprAction, CoprClientMixin):
    """
    Attempts to delete the project if it exists and cancels builds before.
    """

    def __init__(self, proj: CoprProjectRef, ** kwargs):
        """ Initializes the action. """
        self.__proj = proj
        super().__init__(**kwargs)

    def run(self) -> bool:
        """ Runs the action. """
        print(f"Deleting project {self.__proj}")
        CoprActionCancelBuilds(proj=self.__proj, client=self.client).run()
        try:
            self.client.project_proxy.delete(
                self.__proj.owner, self.__proj.name)
        except CoprNoResultException as ex:
            print(f"ERROR: {ex}")
            return False
        return True
