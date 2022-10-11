from importlib import import_module
from datetime import datetime
from inquirer import checkbox, confirm, text

import podarr


class Control:

    def __init__(self, command: str | None, settings: dict | None) -> None:
        self.command = command
        self.module = import_module('podarr')
        self.session = podarr.SESSION_MAKER
        self.bold = podarr.Notification.BOLD
        self.reset = podarr.Notification.RESET
        self.base_directories = [
            podarr.Directory.DIR_USER_SYSTEMD,
            podarr.Directory.DIR_BASE,
            podarr.Directory.DIR_CONFIG,
            podarr.Directory.DIR_BACKUPS,
            podarr.Directory.DIR_TMP,
            podarr.Directory.DIR_DATA,
            podarr.Directory.DIR_DATA_LOCAL,
        ]
        self.settings = settings

    def configure_settings(self) -> bool:
        """
        This function will modify settings.
        """
        if self.settings is None:
            raise Exception('The settings are empty.')

        def change_settings():
            """
            Allow the user to change the settings.
            """
            if self.settings is None:
                raise Exception('The settings are empty.')
            if confirm('Would you like to change the images?', default=True):
                for service, values in self.settings.items():
                    if values['enabled']:
                        if podarr.__available_services__[service]['image'] is not None:
                            self.settings[service]['image'] = text(f'Enter the desired '
                                                                   f'image for {service}',
                                                                   default=self.settings[service]['image'])
            if confirm('Would you like to change the tags?', default=True):
                for service, values in self.settings.items():
                    if values['enabled']:
                        if podarr.__available_services__[service]['tag'] is not None:
                            self.settings[service]['tag'] = text(f'Enter the desired tag for {service}',
                                                                 default=self.settings[service]['tag'])
            if confirm('Would you like to change the ports?', default=True):
                for service, values in self.settings.items():
                    if values['enabled']:
                        if podarr.__available_services__[service]['ports'] is not None:
                            ports = []
                            for index, _ in enumerate(values['ports']):
                                if len(values['ports']) == 1:
                                    ports.append(text(f'Enter the desired port for {service}',
                                                      default=values['ports'][0]))
                                else:
                                    ports.append(text(f'Enter the desired port {index + 1} for {service}',
                                                      default=values['ports'][index]))
                            self.settings[service]['ports'] = ports

        def print_settings():
            """
            Print the default settings.
            """
            confirmation = ''
            if self.settings is None:
                raise Exception('The settings are empty.')
            for service, values in self.settings.items():
                if not values['enabled']:
                    continue
                confirmation += f'{self.bold}{service}{self.reset}{":" if self.settings[service]["image"] else ""}\n'
                if self.settings[service]['image'] is not None:
                    confirmation += f'   Image: {self.bold}{values["image"]}:{values["tag"]}{self.reset}\n'
                if self.settings[service]['ports']:
                    if len(values["ports"]) > 1:
                        confirmation += f'   Ports : '\
                            f'{self.bold}{", ".join([str(port) for port in values["ports"]])}{self.reset}\n'
                    else:
                        confirmation += f'   Port : {self.bold}{values["ports"][0]}{self.reset}\n'
            print(confirmation)

        # Prompt the user to select which services to install.
        selected_services = checkbox('What services would you like to enable?',
                                     choices=[service['repr'] for service in self.settings.values()
                                              if service['repr'] not in ['MergerFS']])
        for key, value in self.settings.items():
            if value['repr'] in selected_services:
                self.settings[key]['enabled'] = True

        # Prompt the user to change the settings.
        print_settings()
        should_change_settings = confirm(
            'Would you like to change the settings?', default=False)
        while should_change_settings:
            change_settings()
            print_settings()
            should_change_settings = confirm(
                'Would you like to change the settings?', default=False)

        # Prompt the user to confirm installation or exit.
        if not confirm('Continue the installation?', default=True):
            return False
        return True

    def create_base_directories(self) -> None:
        """
        This function will create the base directories.
        """
        for directory in self.base_directories:
            podarr.Directory().mkdir(directory)

    def remove_base_directories(self) -> None:
        """
        This function will remove the base directories.
        """
        for directory in self.base_directories:
            podarr.Directory().rmdir(directory)

    def create_database_instances(self) -> None:
        """
        This function will create the database instances.
        """
        if self.settings is None:
            raise Exception('The settings are empty.')
        port_objects = []
        for key, value in self.settings.items():
            if not bool(self.session.query(podarr.Service).filter(podarr.Service.name == key).scalar()):
                for port in value['ports']:
                    port_objects.append(
                        podarr.Port(
                            number=port
                        )
                    )
                self.session.add(podarr.Service(
                    name=key,
                    repr=value['repr'],
                    priority=value['priority'],
                    enabled=value['enabled'],
                    image=value['image'],
                    tag=value['tag'],
                    ports=port_objects
                ))
                self.session.add_all(port_objects)
                port_objects = []
        self.session.commit()

    def install_all(self) -> dict:
        """
        This function performs the installation procedure.
        """
        if self.command is None:
            if self.configure_settings():
                self.create_base_directories()
            podarr.BASE_MODEL.metadata.create_all(
                bind=podarr.DATABASE_ENGINE)
            self.create_database_instances()
            for service in podarr.Query().get_all_services(order_by='priority'):
                if service.enabled:
                    getattr(self.module,
                            service.name.upper().replace('_', ''))().install()
        return {}

    def uninstall_all(self) -> dict:
        """
        This function performs the uninstallation procedure.
        """
        self.stop_all()
        rclone = self.session.query(podarr.Service).filter(
            podarr.Service.name == 'rclone').one()
        rm_img = confirm(
            'Do you want to remove service images?', default=False)
        if podarr.Systemd().status(rclone) and podarr.Podman().status(rclone):
            raise Exception(
                'Uninstallation was interrupted because rclone is still running.')
        for service in podarr.Query().get_all_services(order_by='priority'):
            if service.enabled:
                getattr(self.module,
                        service.name.upper().replace('_', ''))().uninstall(rm_img=rm_img)
        self.remove_base_directories()
        return {}

    def start_all(self) -> dict:
        """
        This function performs the start procedure.
        """
        for service in podarr.Query().get_all_services(order_by='priority'):
            if service.enabled:
                getattr(self.module,
                        service.name.upper().replace('_', ''))().start()
        return {}

    def stop_all(self) -> dict:
        """
        This function performs the stop procedure.
        """
        for service in podarr.Query().get_all_services(order_by='priority', desc=True):
            if service.enabled:
                getattr(self.module,
                        service.name.upper().replace('_', ''))().stop()
        return {}

    def restart_all(self) -> dict:
        """
        This function performs the restart procedure.
        """
        for service in podarr.Query().get_all_services(order_by='priority', desc=True):
            if service.enabled:
                getattr(self.module,
                        service.name.upper().replace('_', ''))().stop()
        for service in podarr.Query().get_all_services(order_by='priority'):
            if service.enabled:
                getattr(self.module,
                        service.name.upper().replace('_', ''))().start()
        return {}

    def enable_all(self) -> dict:
        """
        This function performs the enable procedure.
        """
        for service in podarr.Query().get_all_services(order_by='priority'):
            getattr(self.module,
                    service.name.upper().replace('_', ''))().enable()
        return {}

    def disable_all(self) -> dict:
        """
        This function performs the disable procedure.
        """
        for service in podarr.Query().get_all_services(order_by='priority', desc=True):
            getattr(self.module,
                    service.name.upper().replace('_', ''))().disable()
        return {}

    def backup_all(self) -> dict:
        """
        This function performs the backup procedure.
        """
        if 'auto' in podarr.__arguments__:
            if podarr.AUTOBACKUP().service.locks[0].datetime > datetime.now():
                podarr.Notification('yellow_alert').print(
                    f'Next backup at {podarr.AUTOBACKUP().service.locks[0].datetime}')
        else:
            for service in podarr.Query().get_all_services(order_by='priority'):
                if service.enabled:
                    getattr(self.module,
                            service.name.upper().replace('_', ''))().backup()
            podarr.AUTOBACKUP().register_next_backup_date()
        return {}

    def restore_all(self) -> dict:
        """
        This function performs the restore procedure.
        """
        for service in podarr.Query().get_all_services(order_by='priority'):
            if service.enabled:
                getattr(self.module,
                        service.name.upper().replace('_', ''))().restore()
        return {}

    def update_all(self) -> dict:
        """
        This function performs the update procedure.
        """
        for service in podarr.Query().get_all_services(order_by='priority'):
            if service.enabled:
                getattr(self.module,
                        service.name.upper().replace('_', ''))().update()

        return {}

    def recreate_systemd_all(self) -> dict:
        """
        This function performs the recreate systemd unit file procedure.
        """
        for service in podarr.Query().get_all_services(order_by='priority'):
            if service.enabled:
                getattr(self.module,
                        service.name.upper().replace('_', ''))().recreate_systemd()
        return {}
