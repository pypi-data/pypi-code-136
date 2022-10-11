from time import sleep

from sqlalchemy import true
import podarr


class Systemd:
    """
    1. This class will be used to create, remove, start, and stop systemd units.
    """

    def __init__(self) -> None:
        self.directory = podarr.Directory().DIR_USER_SYSTEMD
        if not self.directory:
            podarr.Basher(f'mkdir -p {self.directory}',
                          msg=f'Creating {self.directory}')

    @staticmethod
    def status(service: podarr.Service) -> bool:
        """
        1. The function status takes a service argument
        (a string) and returns an object.
        2. The function status checks if the podarr service file exists.
        3. If the file exists, the function status calls the basher
        class to check if the podarr service is enabled and active or not.
        4. If the podarr service file exists, the function status
        returns an instance of the class SystemdStatus, which takes
        the results from the basher class calls.
        """
        return podarr.Basher(
            f'systemctl --user is-enabled podarr-{service.name}.service').return_bool

    def create(self, service: podarr.Service) -> bool:
        """
        1. The function takes a service argument (a string) and returns a bool.
        2. Remove the multi-user.target because we are not using it.
        3. Move the file to our systemd directory.
        4. Check if the file exists and return the result.
        """
        podarr.Basher(f'podman generate systemd --files --new '
                      f'--name podarr-{service.name} --container-prefix= '
                      f'--separator=', msg=f"Creating systemd unit: {service.repr}")
        podarr.Basher(
            f"sed -i 's/multi-user.target //g' podarr-{service.name}.service")
        podarr.Basher(f'mv podarr-{service.name}.service '
                      f'{self.directory.joinpath(f"podarr-{service.name}.service")}')
        podarr.Basher('systemctl --user daemon-reload')
        if self.directory.joinpath(f"podarr-{service.name}.service").exists():
            return True
        return False

    def remove(self, service: podarr.Service) -> bool:
        """
        1. If the service is not running and not a container, continue.
        2. If the systemd unit exists, remove it and return True.
        3. Return False if the systemd unit does not exist.
        4. Return False if the service or a container is running.
        """
        if not self.status(service) and not podarr.Podman().status(service):
            if self.directory.joinpath(f'podarr-{service.name}.service').exists():
                return podarr.Basher(f'rm {self.directory.joinpath(f"podarr-{service.name}.service")}',
                                     msg=f'Removing systemd unit: {service.repr}').return_bool
            return False
        return False

    def start(self, service: podarr.Service) -> bool:
        """
        1. The method runs podarr.Basher to reload the user's
        systemd manager configuration.
        2. Checks if the service or the container is not running.
        3. Starts the service.
        4. The method returns a boolean.
        """
        if not self.status(service) and not podarr.Podman().status(service):
            return podarr.Basher(f'systemctl --user enable --now podarr-{service.name}.service',
                                 msg=f'Starting service: {service.repr}').return_bool
        return False

    def stop(self, service: podarr.Service) -> bool:
        """
        1. If the service is running, it will be stopped and return True.
        2. If the service is not running, it'll return False.
        """
        if self.status(service):
            stop = podarr.Basher(f'systemctl --user disable --now podarr-{service.name}.service',
                                 msg=f'Stopping service: {service.repr}').return_bool
            while (self.status(service) or podarr.Podman().status(service)):
                sleep(1)
            if stop:
                return True
        return False
