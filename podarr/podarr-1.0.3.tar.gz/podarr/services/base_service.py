from importlib import import_module
from json import loads
from datetime import datetime
from inquirer import list_input

import podarr


class BaseService:

    def __init__(self, service: str) -> None:
        self.module = import_module('podarr')
        self.session = podarr.SESSION_MAKER
        self.service = self.session.query(podarr.Service).where(
            podarr.Service.name == service).one()
        self.directories = {}
        self.container_pars = ''
        self.backup_pars = ''
        self.should_restart = False
        self.uid = podarr.SystemInfo.get_uid()
        self.gid = podarr.SystemInfo.get_gid()
        self.suid = podarr.SystemInfo.get_subuid()
        self.sgid = podarr.SystemInfo.get_subgid()

    def start(self) -> bool:
        """
        1. This is a general start method. It should be replaced,
        deppending on the service, by a more specific method.
        2. Start the service and return the result.
        """
        podarr.Directory().set_ownership(self.directories['base'])
        start = podarr.Systemd().start(self.service)
        return start

    def stop(self) -> bool:
        """
        1. This is a general stop method. It should be replaced,
        deppending on the service, by a more specific method.
        2. Stop the service and return the result.
        """
        stop = podarr.Systemd().stop(self.service)
        podarr.Directory().revoke_ownership(self.directories['base'])
        return stop

    def restart(self) -> bool:
        """
        1. This is a general restart method. It should be replaced,
        deppending on the service, by a more specific method.
        2. Restart the service and return the result.
        """
        podarr.Systemd().stop(self.service)
        return podarr.Systemd().start(self.service)

    def install(self) -> tuple:
        """
        1. This is a general installation method. It should be replaced,
        deppending on the service, by a more specific method.
        2. Pull the image, create the directories, create the container and
        the systemd unit file.
        3. Return a tuple with the results of the operations.
        """
        img_return = podarr.Podman().pull_image(self.service)
        dir_return = []
        for directory in self.directories.values():
            dir_return.append(podarr.Directory().mkdir(directory))
        if self.service.name == 'rclone':
            if 'skip-config' not in podarr.__arguments__:
                podarr.RCLONE().create_config()
            podarr.RCLONE().create_remote_directories()
        container_return = podarr.Podman().create_container(
            self.service, getattr(
                self.module,
                self.service.name.upper().replace('_', ''))().container_pars)
        systemd_return = podarr.Systemd().create(self.service)
        getattr(self.module,
                self.service.name.upper().replace('_', ''))().start()
        return img_return, dir_return, container_return, systemd_return

    def uninstall(self, rm_img=False) -> tuple:
        """
        1. This is a general uninstallation method. It should be replaced,
        deppending on the service, by a more specific method.
        2. Stop the service, remove the container, remove the systemd unit file,
        remove the image and remove the directories.
        3. Return a tuple with the results of the operations.
        """
        if podarr.Systemd.status(self.service) and podarr.Podman().status(self.service):
            podarr.Systemd().stop(self.service)
        container_return = podarr.Podman().remove_container(self.service)
        systemd_return = podarr.Systemd().remove(self.service)
        if rm_img:
            img_return = podarr.Podman().remove_image(self.service)
        else:
            img_return = False
        dir_return = []
        for directory in self.directories.values():
            podarr.Directory().revoke_ownership(directory)
            dir_return.append(podarr.Directory().rmdir(directory))
        return img_return, dir_return, container_return, systemd_return

    def update(self) -> bool:
        """
        1. This is a general update method. It should be replaced,
        deppending on the service, by a more specific method.
        2. Stop the service, remove the image, pull the new image.
        3. If everything succeeds, return True. Else, returns False.
        """
        if podarr.Systemd.status(self.service):
            self.should_restart = True
            podarr.Systemd().stop(self.service)
        remove_return = podarr.Podman().remove_image(self.service)
        pull_return = podarr.Podman().pull_image(self.service)
        if self.should_restart:
            podarr.Systemd().start(self.service)
        if remove_return and pull_return:
            return True
        return False

    def enable(self) -> bool:
        """
        1. This is a general enable method. It should be replaced,
        deppending on the service, by a more specific method.
        2. Enable the service and return the result.
        """
        self.service.enabled = True
        self.session.commit()
        self.session.refresh(self.service)
        self.start()
        if self.service.enabled\
            or (podarr.Systemd.status(self.service)
                and podarr.Podman().status(self.service)):
            podarr.Notification('yellow_alert').print(
                f'{self.service.name} enabled')
            return True
        return False

    def disable(self) -> bool:
        """
        1. This is a general disable method. It should be replaced,
        deppending on the service, by a more specific method.
        2. Disable the service and return the result.
        """
        self.stop()
        self.service.enabled = False
        self.session.commit()
        self.session.refresh(self.service)

        if self.service.enabled or\
                podarr.Systemd.status(self.service)\
                or podarr.Podman().status(self.service):
            return False
        podarr.Notification('yellow_alert').print(
            f'{self.service.name} disabled')
        return True

    def backup(self) -> bool:
        """
        1. This is a general backup method. It should be replaced,
        deppending on the service, by a more specific method.
        2. Stop the service and get the current date and time.
        3. Make a tarball of the base directory.
        4. Mv the tarball to the backup directory.
        5. If everything succeeds, return True. Else, returns False.
        """
        auto_restart = False
        if podarr.Systemd().status(self.service) and podarr.Podman().status(
                self.service):
            auto_restart = True
            podarr.Systemd().stop(self.service)
        time_now = datetime.now().astimezone().strftime("%Y%m%d%H%M%S")
        mk_bkp = podarr.Basher(
            f'{podarr.Basher("which tar").stdout} -cf '
            f'{podarr.Directory.DIR_TMP}/{self.service.name}_'
            f'{time_now}.tar.gz -C '
            f'{self.directories["base"]} {self.backup_pars}'
            '--exclude="custom-services.d" .',
            msg=f"Performing backup: {self.service.repr}",
        )
        mv_bkp = podarr.Basher(f'mv {podarr.Directory.DIR_TMP}/{self.service.name}_'
                               f'{time_now}.tar.gz {podarr.Directory.DIR_BACKUPS}')
        if auto_restart:
            podarr.Systemd().start(self.service)
        if mk_bkp.return_bool and mv_bkp.return_bool:
            return True
        return False

    def restore(self) -> bool:
        """
        1. This is a general restore method. It should be replaced,
        deppending on the service, by a more specific method.
        2. Create a list of the available backups.
        3. If there are no backups, return False.
        4. If there are backups, ask the user which one to restore.
        5. Download the backup and stop the service when done.
        3. Remove the current base directory of the service.
        4. Untar the tarball in the base directory and remove it.
        5. If everything succeeds, return True. Else, returns False.
        """
        backups = {}
        for file in loads(podarr.Podman().run(f'--rm '
                                              f'-e PUID={self.uid} '
                                              f'-e PGID={self.gid} '
                                              f'-v {podarr.RCLONE().directories["base"]}:/config/rclone '
                                              f'{podarr.RCLONE().service.image}:'
                                              f'{podarr.RCLONE().service.tag} '
                                              f'lsjson --files-only {podarr.RCLONE().service.remote}:/backups '
                                              '--config /config/rclone/rclone.conf',
                                              msg=f"Fetching {self.service.repr}'s backup list").stdout):
            if self.service.name in file['Name']:
                backup_file = file['Name']
                backup_file_split = file['Name'].replace('.tar.gz', '')
                backup_file_split = backup_file_split.split('_')
                backups[f'{datetime.strptime(backup_file_split[1], "%Y%m%d%H%M%S")}'] = backup_file

        if backups.keys():
            if 'latest' in podarr.__arguments__:
                backup_dt = sorted(backups.items(), reverse=True)[0][0]
            else:
                backup_dt = list_input(
                    f"Choose which {self.service.repr} backup you'd like to restore",
                    choices=sorted(backups.items(), reverse=True))

            download_bkp = podarr.Podman().run(f'--rm --name=podarr-rclone-backup '
                                               f'-p {podarr.RCLONE().service.ports[2].number}:'
                                               f'{podarr.RCLONE().service.ports[2].number} '
                                               f'-e PUID={self.uid} '
                                               f'-e PGID={self.gid} '
                                               f'-v {podarr.Directory.DIR_BACKUPS}:/backups '
                                               f'-v {podarr.RCLONE().directories["base"]}:/config/rclone '
                                               f'{podarr.RCLONE().service.image}:'
                                               f'{podarr.RCLONE().service.tag} '
                                               '--config /config/rclone/rclone.conf '
                                               f'copy {podarr.RCLONE().service.remote}:/backups/{backups[backup_dt]} /backups '
                                               f'--rc --rc-addr 0.0.0.0:{podarr.RCLONE().service.ports[2].number} '
                                               '--rc-no-auth',
                                               msg=f"Downloading {self.service.repr}'s "
                                               f"backup from {backup_dt}").return_bool

            auto_restart = False
            if podarr.Systemd().status(self.service) and podarr.Podman().status(
                    self.service):
                auto_restart = True
            self.stop()

            rm_dir = podarr.Basher(
                f'rm -rf {self.directories["base"]}/*',
                msg=f'Removing previous {self.service.repr} instance').return_bool

            untar = podarr.Basher(f'{podarr.Basher("which tar").stdout} -xf '
                                  f'{podarr.Directory.DIR_BACKUPS.joinpath(backups[backup_dt])} -C '
                                  f'{self.directories["base"]}/',
                                  msg=f'Restoring backup: {self.service.repr}').return_bool

            podarr.Basher(f'rm {podarr.Directory.DIR_BACKUPS.joinpath(backups[backup_dt])}',
                          msg=f"Removing {self.service.repr}'s backup file")
            if auto_restart:
                self.start()
            if download_bkp and rm_dir and untar:
                return True

        podarr.Notification('red_alert').print(
            f'No backups found for {self.service.repr}.')
        return False

    def recreate_systemd(self) -> bool:
        """
        1. Remove and create a systemd unit for the service.
        2. If everything succeeds, return True. Else, return False.
        """
        started, remove, create, container_return = False, False, False, False
        if podarr.Systemd().status(self.service):
            started = True
        self.stop()
        remove = podarr.Systemd().remove(self.service)
        container_return = podarr.Podman().create_container(
            self.service, getattr(
                self.module,
                self.service.name.upper().replace('_', ''))().container_pars)
        create = podarr.Systemd().create(self.service)
        self.stop()
        if started:
            self.start()
        if remove and create and container_return:
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
        service_status = False
        if podarr.Systemd().status(self.service) and podarr.Podman().status(self.service):
            service_status = True
        return {'enabled': self.service.enabled, 'status': service_status}
