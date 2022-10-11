from configobj import ConfigObj
from uvicorn import run as start_server
import podarr


class WEB(podarr.BaseService):

    def __init__(self) -> None:
        super().__init__('web')
        self.directories = {
            'base': podarr.Directory.DIR_USER_SYSTEMD
        }
        self.unit_file = self.directories['base'].joinpath(
            f'podarr-{self.service.name}.service')
        self.service_upload = ConfigObj(str(self.unit_file),
                                        list_values=False)
        self.service_upload["Unit"] = {
            'Description': "podarr's web service",
            'After': 'network.target',
            'Wants': 'network-online.target',
        }
        self.service_upload["Service"] = {
            'Restart': 'on-failure',
            'RestartSec': '20s',
            'ExecStart': f'{podarr.Basher("which python").stdout} -m podarr start-web-server',
        }
        self.service_upload['Install'] = {'WantedBy': 'default.target'}

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

    def update(self) -> None:
        pass

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

    def start_webserver(self):
        start_server('podarr.api.endpoints:app', host='0.0.0.0',
                     port=8000, log_level='info')
