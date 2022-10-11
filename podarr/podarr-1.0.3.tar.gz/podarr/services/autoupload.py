from configobj import ConfigObj

import podarr


class AUTOUPLOAD(podarr.BaseService):

    def __init__(self) -> None:
        super().__init__('auto_upload')
        self.directories = {
            'base': podarr.Directory.DIR_USER_SYSTEMD
        }
        self.unit_file = self.directories['base'].joinpath(
            f'podarr-{self.service.name}.service')
        self.service_upload = ConfigObj(str(self.unit_file),
                                        list_values=False)
        self.service_upload["Unit"] = {
            'Description': "podarr's upload module",
            'After': 'network.target',
            'Wants': 'network-online.target',
        }
        self.service_upload["Service"] = {
            'Restart': 'always',
            'RestartSec': '20s',
            'ExecStart': f'{podarr.Basher("which python").stdout} -m podarr upload',
        }
        self.service_upload['Install'] = {'WantedBy': 'default.target'}

    def install(self) -> None:
        """
        Installs the service.
        """
        self.service_upload.write()

    def uninstall(self, rm_img=None) -> None:
        """
        Uninstalls the service.
        """
        if podarr.Systemd.status(self.service):
            self.stop()
        podarr.Systemd().remove(self.service)

    def start(self) -> bool:
        """
        1. This is a general start method. It should be replaced,
        deppending on the service, by a more specific method.
        2. Start the service and return the result.
        """
        return podarr.Systemd().start(self.service)

    def stop(self) -> bool:
        """
        1. This is a general stop method. It should be replaced,
        deppending on the service, by a more specific method.
        2. Stop the service and return the result.
        """
        return podarr.Systemd().stop(self.service)

    def backup(self) -> None:
        pass

    def restore(self) -> None:
        pass

    def recreate_systemd(self) -> bool:
        """
            1. Remove and create a systemd unit for the service.
            2. If everything succeeds, return True. Else, return False.
            """
        started, remove, create = False, False, False
        if podarr.Systemd().status(self.service):
            started = True
        self.stop()
        remove = podarr.Systemd().remove(self.service)
        self.service_upload.write()
        if self.unit_file.exists():
            create = True
        self.stop()
        if started:
            self.start()
        if remove and create:
            return True
        return False

    def status(self) -> dict:
        """
        1. Check if the service is running.
        2. Must return a dict containing two keys: name and value.
        3. If the service is also a container, the value key should return
        three boolean values:
            a. If the service is enabled.
            b. If the container is running (None in case there's no container).
            c. If the systemd service is enabled.
        4. If the service is not a container, the value key should return only 'a' and 'c'.
        """
        return {'enabled': self.service.enabled, 'status': podarr.Systemd().status(self.service)}
