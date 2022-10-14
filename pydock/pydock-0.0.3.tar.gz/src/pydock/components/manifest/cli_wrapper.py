from typing import Optional

from ..buildx.imagetools.models import Manifest
from ...client_config import DockerCLICaller
from ...exceptions import DockerException
from ...utils import run


class ManifestCLI(DockerCLICaller):

    def annotate(self,
                 tag: str,
                 image: str,
                 arch: Optional[str] = None,
                 os: Optional[str] = None,
                 os_features: Optional[str] = None,
                 os_version: Optional[str] = None,
                 variant: Optional[str] = None,
                 ) -> None:
        """
        Add additional information to a local image manifest

        :param tag:         Manifest name
        :param image:      List of images to add to the manifest
        :param arch:            Set architecture
        :param os:              Set operating system
        :param os_features:     Set operating system feature
        :param os_version:      Set operating system version
        :param variant:         Set architecture variant
        """
        full_cmd = self.docker_cmd + ["manifest", "annotate"]
        full_cmd.add_simple_arg("--arch", arch)
        full_cmd.add_simple_arg("--os", os)
        full_cmd.add_simple_arg("--os-features", os_features)
        full_cmd.add_simple_arg("--os-version", os_version)
        full_cmd.add_simple_arg("--variant", variant)
        full_cmd.append(tag)
        full_cmd.extend(image)
        # execute command
        run(full_cmd)

    def create(self,
               tag: str,
               images: str,
               amend: bool = False,
               insecure: bool = False,
               ) -> None:
        """
        Creates the manifest of a Docker image in a registry

        :param tag:         Manifest name
        :param images:      List of images to add to the manifest
        :param amend:       Amend an existing manifest list
        :param insecure:    Allow communication with an insecure registry
        """
        full_cmd = self.docker_cmd + ["manifest", "create"]
        full_cmd.add_flag("--amend", amend)
        full_cmd.add_flag("--insecure", insecure)
        full_cmd.append(tag)
        full_cmd.extend(images)
        # execute command
        run(full_cmd)

    def inspect(self, name: str, insecure: bool = False):
        """
        Returns the manifest of a Docker image in a registry without pulling it.

        :param name:        Name of the manifest to inspect
        :param insecure:    Allow communication with an insecure registry
        :return:
        """
        full_cmd = self.docker_cmd + ["manifest", "inspect"]
        full_cmd.add_flag("--insecure", insecure)
        full_cmd.append(name)
        try:
            result = run(full_cmd)
        except DockerException as e:
            # manifest not found
            if "no such manifest" in e.stderr:
                return None
            raise e
        return Manifest.parse_raw(result)

    def push(self,
             tag: str,
             purge: bool = False,
             insecure: bool = False,
             ) -> None:
        """
        Pushes the manifest to a registry

        :param tag:         Manifest name
        :param purge:       Remove the local manifest list after push
        :param insecure:    Allow communication with an insecure registry
        """
        full_cmd = self.docker_cmd + ["manifest", "push"]
        full_cmd.add_flag("--purge", purge)
        full_cmd.add_flag("--insecure", insecure)
        full_cmd.append(tag)
        # execute command
        run(full_cmd)
