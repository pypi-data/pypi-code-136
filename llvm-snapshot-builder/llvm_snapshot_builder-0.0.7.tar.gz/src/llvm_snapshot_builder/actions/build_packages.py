#!/usr/bin/env python3

"""
CoprActionBuildPackages
"""

from typing import Union
from ..copr_project_ref import CoprProjectRef
from ..mixins.package_builder_mixin import CoprPackageBuilderMixin
from ..mixins.client_mixin import CoprClientMixin
from .action import CoprAction
from ..copr_project_ref import CoprProjectRef
from .make_or_edit_packages import CoprActionMakeOrEditPackages
from .make_or_edit_project import CoprActionMakeOrEditProject


class CoprActionBuildPackages(
        CoprAction,
        CoprClientMixin,
        CoprPackageBuilderMixin):
    """
    Builds a list of packages for the given chroots in the order they are given.

    NOTE: We kick-off builds for each chroot individually so that an x86_64
    build doesn't have to wait for a potentially slower s390x build.
    """

    def __init__(
            self,
            proj: Union[CoprProjectRef, str],
            package_names: list[str] = None,
            chroots: list[str] = None,
            wait_on_build_id: int = None,
            ** kwargs):
        """
        Initializes the action.

        Args:
            package_names (list): Packages to build. Defaults to default packages from CoprActionMakeOrEditPackages.
            chroots (list): Chroots to build in. Defaults to default chroots from CoprActionMakeOrEditProject.
            wait_on_build_id (int): Wait for this build to finish before starting the build.
        """
        self.__proj = CoprProjectRef(proj)
        if package_names is None:
            package_names = CoprActionMakeOrEditPackages.default_package_names
        self.__package_names = package_names
        if chroots is None:
            chroots = CoprActionMakeOrEditProject.default_chroots
        self.__chroots = chroots
        self.__wait_on_build_id = wait_on_build_id
        super().__init__(**kwargs)

    def run(self) -> bool:
        """ Runs the action. """

        for chroot in self.__chroots:
            print(f"CHROOT: {chroot}")
            previous_build_id = self.__wait_on_build_id
            for packagename in self.__package_names:
                build = self.build(
                    self.__proj,
                    packagename,
                    [chroot],
                    build_after_id=previous_build_id)
                if build != dict():
                    previous_build_id = build.id
                    print(
                        f"(build-id={previous_build_id}, state={build.state})")
                else:
                    print(
                        f"skipped build of package {packagename} in chroot {chroot}")
        return True
