from pathlib import Path

import podarr


class Directory:
    DIR_HOME = Path.home()
    DIR_USER_SYSTEMD = DIR_HOME.joinpath('.config/systemd/user')
    DIR_BASE = DIR_HOME.joinpath('.podarr')
    DIR_CONFIG = DIR_BASE.joinpath('config')
    DIR_BACKUPS = DIR_BASE.joinpath('backups')
    DIR_TMP = DIR_BASE.joinpath('.tmp')
    DIR_DATA = DIR_BASE.joinpath('data')
    DIR_DATA_LOCAL = DIR_DATA.joinpath('local')

    def __init__(self) -> None:
        self.directories = {
            'base': Directory.DIR_BASE,
            'backups': Directory.DIR_BACKUPS,
            'tmp': Directory.DIR_TMP,
            'data': Directory.DIR_DATA,
            'data_local': Directory.DIR_DATA_LOCAL,
        }
        self.uid = podarr.SystemInfo.get_uid()
        self.gid = podarr.SystemInfo.get_gid()
        self.suid = podarr.SystemInfo.get_subuid()
        self.sgid = podarr.SystemInfo.get_subgid()
        self.podman_path = podarr.Basher("which podman").stdout

    def mkdir(self, path: Path) -> bool:
        """
        1. Check if directory exists.
        2. Create if not exists.
        3. Return object.
        """
        return podarr.Basher(f'{self.podman_path} '
                             f'unshare mkdir -p {path}',
                             msg=f'Creating directory: {path}').return_bool

    def rmdir(self, path: Path) -> bool:
        """
        1. Check if directory exists.
        2. Remove if exists.
        3. Return object.
        """
        if path.exists():
            return podarr.Basher(f'{self.podman_path} '
                                 f'unshare rm -r {path}',
                                 msg=f'Removing directory: {path}').return_bool
        return False

    def set_ownership(self, directory: Path) -> bool:
        """
        1. Check if directory exists.
        2. If exists, set ownership and return True.
        3. If not exists, return False.
        """
        if directory.is_dir():
            if podarr.Basher(f'stat -c "%u %g" {directory}').stdout == f'{self.uid} {self.gid}':
                return podarr.Basher(f'{self.podman_path} unshare chown -R {self.uid}:{self.gid} {directory}',
                                     msg=f'Changing ownership of {directory} to '
                                     f'{self.suid}:{self.sgid}').return_bool
        return False

    def revoke_ownership(self, directory: Path) -> bool:
        """
        1. Check if directory exists.
        2. If exists, revoke ownership and return True.
        3. If not exists, return False.
        """
        if directory.is_dir():
            if podarr.Basher(f'stat -c "%u %g" {directory}').stdout == f'{self.suid} {self.sgid}':
                return podarr.Basher(f'{self.podman_path} unshare chown -R root:root {directory}',
                                     msg=f'Changing ownership of {directory} to '
                                     f'{self.uid}:{self.gid}').return_bool
        return False

    def bind_mount(self, directory: Path) -> bool:
        """
        1. Check if directory exists.
        2. If exists, make it shared and return result.
        """
        if directory.is_dir():
            return podarr.Basher(f'{self.podman_path} unshare mount --bind --make-shared {directory} '
                                    f'{directory}', msg=f'Bind mounting {directory}').return_bool
        return False

    def bind_unmount(self, directory: Path) -> bool:
        """
        1. Check if directory exists.
        2. If exists, unmount it.
        """
        if directory.is_dir():
            return podarr.Basher(f'{self.podman_path} unshare umount {directory} '
                                    f'{directory}', msg=f'Umounting {directory}').return_bool
        return False
