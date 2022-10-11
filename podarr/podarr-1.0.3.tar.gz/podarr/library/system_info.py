from time import time
import getpass
import socket
from pwd import getpwnam
from psutil import cpu_percent, virtual_memory, swap_memory, disk_usage, boot_time

import podarr


class SystemInfo:
    def __init__(self) -> None:
        self.rclone = podarr.RCLONE().service
        self.mergerfs = podarr.MERGERFS().service
        self.plex = podarr.PLEX().service
        self.radarr = podarr.RADARR().service
        self.sonarr = podarr.SONARR().service
        self.lidarr = podarr.LIDARR().service
        self.bazarr = podarr.BAZARR().service
        self.prowlarr = podarr.PROWLARR().service
        self.sabnzbd = podarr.SABNZBD().service
        self.qbittorrent = podarr.QBITTORRENT().service
        self.auto_backup = podarr.AUTOBACKUP().service
        self.auto_upload = podarr.AUTOUPLOAD().service

    @staticmethod
    def get_uname():
        return str(getpass.getuser())

    @staticmethod
    def get_uid():
        return int(getpwnam(SystemInfo.get_uname()).pw_uid)

    @staticmethod
    def get_gid():
        return int(getpwnam(SystemInfo.get_uname()).pw_gid)

    @staticmethod
    def get_subuid():
        with open("/etc/subuid", "r") as subuid_file:
            for line in subuid_file:
                if SystemInfo.get_uname() in line:
                    return int(line.split(":")[1]) + SystemInfo.get_uid() - 1

    @staticmethod
    def get_subgid():
        with open("/etc/subgid", "r") as subgid_file:
            for line in subgid_file:
                if SystemInfo.get_uname() in line:
                    return int(line.split(":")[1]) + SystemInfo.get_gid() - 1

    @staticmethod
    def get_ipv4():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s_ipv4:
                s_ipv4.connect(("10.255.255.255", 80))
                ipv4 = s_ipv4.getsockname()[0]
        except socket.error:
            ipv4 = None
        return ipv4

    @staticmethod
    def size(B: float) -> str:
        KB = float(1024)
        MB = float(KB ** 2)
        GB = float(KB ** 3)
        TB = float(KB ** 4)

        B = float(B)
        if B < KB:
            return f"{B} Bytes"
        elif KB <= B < MB:
            return f"{B/KB:.2f} KB"
        elif MB <= B < GB:
            return f"{B/MB:.2f} MB"
        elif GB <= B < TB:
            return f"{B/GB:.2f} GB"
        elif TB <= B:
            return f"{B/TB:.2f} TB"
        else:
            return 'Bandwidth Unknown'

    @staticmethod
    def get_cpu_usage():
        return cpu_percent()

    @staticmethod
    def get_ram_usage():
        return virtual_memory().percent

    @staticmethod
    def get_swap_usage():
        return swap_memory().percent

    @staticmethod
    def get_disk_usage():
        disk = [
            {'name': 'Base', 'value': disk_usage(
                podarr.Directory.DIR_BASE.as_posix()).percent},
            {'name': 'Data', 'value': disk_usage(
                podarr.RCLONE().directories['cache'].as_posix()).percent}
        ]
        return disk

    @staticmethod
    def get_system_uptime():
        return time() - boot_time()

    def get_service_status(self):
        service_status = []
        service_status.append(
            {
                'name': self.rclone.name, 'value': [
                    self.rclone.enabled,
                    podarr.Podman().status(self.rclone),
                    podarr.Systemd().status(self.rclone)
                ]
            }
        )
        service_status.append(
            {
                'name': self.mergerfs.name, 'value': [
                    self.mergerfs.enabled,
                    podarr.Podman().status(self.mergerfs),
                    podarr.Systemd().status(self.mergerfs)
                ]
            }
        )
        service_status.append(
            {
                'name': self.plex.name, 'value': [
                    self.plex.enabled,
                    podarr.Podman().status(self.plex),
                    podarr.Systemd().status(self.plex)
                ]
            }
        )
        service_status.append(
            {
                'name': self.radarr.name, 'value': [
                    self.radarr.enabled,
                    podarr.Podman().status(self.radarr),
                    podarr.Systemd().status(self.radarr)
                ]
            }
        )
        service_status.append(
            {
                'name': self.sonarr.name, 'value': [
                    self.sonarr.enabled,
                    podarr.Podman().status(self.sonarr),
                    podarr.Systemd().status(self.sonarr),
                ]
            }
        )
        service_status.append(
            {
                'name': self.lidarr.name, 'value': [
                    self.lidarr.enabled,
                    podarr.Podman().status(self.lidarr),
                    podarr.Systemd().status(self.lidarr),
                ]
            }
        )
        service_status.append(
            {
                'name': self.bazarr.name, 'value': [
                    self.bazarr.enabled,
                    podarr.Podman().status(self.bazarr),
                    podarr.Systemd().status(self.bazarr),
                ]
            }
        )
        service_status.append(
            {
                'name': self.prowlarr.name, 'value': [
                    self.prowlarr.enabled,
                    podarr.Podman().status(self.prowlarr),
                    podarr.Systemd().status(self.prowlarr),
                ]
            }
        )
        service_status.append(
            {
                'name': self.sabnzbd.name, 'value': [
                    self.sabnzbd.enabled,
                    podarr.Podman().status(self.sabnzbd),
                    podarr.Systemd().status(self.sabnzbd),
                ]
            }
        )
        service_status.append(
            {
                'name': self.qbittorrent.name, 'value': [
                    self.qbittorrent.enabled,
                    podarr.Podman().status(self.qbittorrent),
                    podarr.Systemd().status(self.qbittorrent),
                ]
            }
        )
        service_status.append(
            {
                'name': self.auto_backup.name, 'value': [
                    self.auto_backup.enabled,
                    None,
                    podarr.Systemd().status(self.auto_backup),
                ]
            }
        )
        service_status.append(
            {
                'name': self.auto_upload.name, 'value': [
                    self.auto_upload.enabled,
                    None,
                    podarr.Systemd().status(self.auto_upload)
                ]
            }
        )

        return service_status
