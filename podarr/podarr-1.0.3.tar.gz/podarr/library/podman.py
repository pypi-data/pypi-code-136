from json import loads
from importlib import import_module

import podarr


class Podman:

    def __init__(self) -> None:
        self.podman_path = podarr.Basher('which podman').stdout

    def status(self, service: podarr.Service) -> bool:
        """
        1. If the container doesn't exist we return False.
        2. Check if the container is running and not restarting, case it'll return True.
        3. If the container is not running or restarting, we return False.
        """
        container = podarr.Basher(
            f'{self.podman_path} inspect --type=container podarr-{service.name}')
        if container.return_bool:
            running = loads(container.stdout)[0]['State']['Running']
            restarting = loads(container.stdout)[0]['State']['Restarting']
            if running and not restarting:
                return True
            return False
        return False

    def create_container(self, service: podarr.Service, command: str) -> bool:
        """
        1. Checks if the container doesn't exist.
        2. If doesn't exist, create it and return True.
        3. If exists, return False.
        """
        if not self.status(service):
            return podarr.Basher(f'{self.podman_path} create '
                                 f'--name=podarr-{service.name} {command}',
                                 msg=f'Creating container: {service.repr}').return_bool
        return False

    def remove_container(self, service: podarr.Service) -> bool:
        """
        1. Checks if the container exists.
        2. If exist, create it and return True.
        3. If doesn't exist, return False.
        """
        if self.status(service):
            return podarr.Basher(f'{self.podman_path} rm podarr-{service.name}',
                                 msg=f'Removing container: {service.repr}').return_bool
        return False

    def pull_image(self, service: podarr.Service) -> bool:
        """
        1. Checks if the image doesn't already exist.
        2. If it doesn't exist, then pull it and return True.
        3. If it exists, return False.
        """
        if not podarr.Basher(f'{self.podman_path} inspect --type=image '
                             f'{service.image}:{service.tag}').return_bool:
            return podarr.Basher(f'{self.podman_path} pull {service.image}:{service.tag}',
                                 msg=f'Pulling image: {service.image}:{service.tag}').return_bool
        return False

    def remove_image(self, service: podarr.Service) -> bool:
        """
        1. Checks if the image exists.
        2. If it doesn't exist, then pull it and return True.
        3. If it exists, return False.
        """
        if podarr.Basher(f'{self.podman_path} inspect --type=image '
                         f'{service.image}:{service.tag}').return_bool:
            return podarr.Basher(f'{self.podman_path} rmi {service.image}:{service.tag}',
                                 msg=f'Removing image: {service.image}:{service.tag}').return_bool
        return False

    def start(self, service: podarr.Service) -> bool:
        """
        1. Checks if the container is running.
        2. If it's not running, then start it and return True.
        3. If it's running, return False.
        """
        if not self.status(service):
            getattr(import_module('podarr'),
                    service.name.upper().replace('_', ''))().start()
            return podarr.Basher(f'{self.podman_path} start podarr-{service.name}',
                                 msg=f'Starting container: {service.repr}').return_bool
        return True

    def stop(self, service: podarr.Service) -> bool:
        """
        1. Checks if the container is running.
        2. If it's running, then stop it and return True.
        3. If it's not running, return False.
        """
        if self.status(service):
            return podarr.Basher(f'{self.podman_path} stop podarr-{service.name}',
                                 msg=f'Stopping container: {service.repr}').return_bool
        return True

    def run(self, command: str, msg=None, quiet=False, debug=False) -> podarr.Basher:
        """
        Runs a podman command.
        """
        return podarr.Basher(f'{self.podman_path} run {command}',
                             msg=msg, quiet=quiet, debug=debug)

    def exec(self, service: podarr.Service, command: str, msg=None, quiet=False, debug=False, decode=True) -> podarr.Basher:
        """
        Runs a podman command.
        """
        return podarr.Basher(f'{self.podman_path} exec podarr-{service.name} {command}',
                             msg=msg, quiet=quiet, debug=debug, decode=decode)

    def unshare(self, command: str, msg=None, quiet=False, debug=False, decode=True, wait=True) -> podarr.Basher:
        """
        Runs a podman command.
        """
        return podarr.Basher(f'{self.podman_path} unshare {command}',
                             msg=msg, quiet=quiet, debug=debug, decode=decode, wait=wait)
