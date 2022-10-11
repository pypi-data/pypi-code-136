
#!/usr/bin/env python3

"""
CoprPackageBuilderMixin
"""

import logging
from typing import Union
from copr.v3 import CoprRequestException
from ..copr_project_ref import CoprProjectRef


class CoprPackageBuilderMixin(object):
    """
    The base class for package building Actions in Copr

    Attributes:
        default_build_timeout (int): the default build timeout in seconds
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    default_build_timeout = 30 * 3600

    def build(
            self,
            proj: Union[CoprProjectRef, str],
            package_name: str,
            chroots: list[str],
            build_after_id: int = None):
        """
        Builds a package in Copr

        Args:
            proj (CoprProjectRef): the project to build in
            package_name (str): the package to build
            chroots (list[str]): the chroots to build in
            build_after_id (int): the build to build after
        """
        build = None
        proj = CoprProjectRef(proj)
        try:
            logging.info(
                f"build package {package_name} in {proj} for chroots {chroots} (build after: {build_after_id})")

            logging.info(
                "adjust chroots to have --with=snapshot_build and llvm-snapshot-builder package installed")
            for chroot in chroots:
                self.client.project_chroot_proxy.edit(
                    ownername=proj.owner,
                    projectname=proj.name,
                    chrootname=chroot,
                    with_opts="snapshot_build",
                    additional_repos=[
                        "https://download.copr.fedorainfracloud.org/results/%40fedora-llvm-team/llvm-snapshot-builder/" +
                        chroot,
                        "https://download.copr.fedorainfracloud.org/results/%40fedora-llvm-team/llvm-compat-packages/" +
                        chroot,
                    ],
                    additional_packages="llvm-snapshot-builder")
            build = self.client.package_proxy.build(
                ownername=proj.owner,
                projectname=proj.name,
                packagename=package_name,
                # See
                # https://python-copr.readthedocs.io/en/latest/client_v3/build_options.html
                buildopts={
                    "timeout": self.default_build_timeout,
                    "chroots": list(set(chroots)),
                    "after_build_id": build_after_id
                },
            )
        except CoprRequestException as ex:
            logging.exception(ex)
            raise ex
        print(f"(build-id={build.id}, state={build.state})")
        return build
