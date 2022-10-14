from typing import Optional, List

from ....client_config import DockerCLICaller
from ....utils import run
from ....exceptions import DockerException
from .models import Manifest


class ImagetoolsCLI(DockerCLICaller):

    def inspect(self, name: str) -> Optional[Manifest]:
        """Returns the manifest of a Docker image in a registry without pulling it"""
        full_cmd = self.docker_cmd + ["buildx", "imagetools", "inspect", "--raw", name]
        try:
            result = run(full_cmd)
        except DockerException as e:
            # manifest not found
            if "ERROR" in e.stderr and "not found" in e.stderr:
                return None
            raise e
        return Manifest.parse_raw(result)

    def create(self,
               tag: str,
               source: List[str],
               append: bool = False,
               dry_run: bool = False,
               builder: Optional[str] = None,
               file: Optional[str] = None,
               progress: Optional[str] = None
               ) -> None:
        """
        Creates the manifest of a Docker image in a registry

        :param tag: Manifest name
        :param source: List of images to add to the manifest
        :param append: Append to existing manifest
        :param dry_run: Show final image instead of pushing
        :param builder: Override the configured builder instance
        :param file: Read source descriptor from file
        :param progress: Set type of progress output ("auto", "plain", "tty").
        """
        full_cmd = self.docker_cmd + ["buildx", "imagetools", "create"]
        full_cmd.add_simple_arg("--tag", tag)
        full_cmd.add_flag("--append", append)
        full_cmd.add_flag("--dry-run", dry_run)
        if builder:
            full_cmd.add_simple_arg("--builder", builder)
        if file:
            full_cmd.add_simple_arg("--file", file)
        if progress:
            full_cmd.add_simple_arg("--progress", progress)
        full_cmd.extend(source)
        # execute command
        run(full_cmd)
