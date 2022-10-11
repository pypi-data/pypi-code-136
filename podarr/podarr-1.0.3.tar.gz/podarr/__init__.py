"""
The importing order matters.
"""

__version__ = '1.0.3'
# Last number is related to bug fixes or minor improvements.
# Middle number is related to new features.
# First number is related to major updates, meaning how the module itself works.
# The counters never resets.

__available_services__ = {
    'rclone': {
        'repr': 'Rclone',
        'required': False,
        'priority': 0,
        'enabled': False,
        'image': 'docker.io/rclone/rclone',
        'tag': 'latest',
        'ports': [6000, 6001, 6002]
    },
    'mergerfs': {
        'repr': 'MergerFS',
        'required': True,
        'priority': 1,
        'enabled': True,
        'image': 'docker.io/hotio/mergerfs',
        'tag': 'latest',
        'ports': []
    },
    'plex': {
        'repr': 'Plex Media Server',
        'required': False,
        'priority': 2,
        'enabled': False,
        'image': 'docker.io/linuxserver/plex',
        'tag': 'latest',
        'ports': [32400]
    },
    'radarr': {
        'repr': 'Radarr',
        'required': False,
        'priority': 2,
        'enabled': False,
        'image': 'docker.io/linuxserver/radarr',
        'tag': 'latest',
        'ports': [7000]
    },
    'sonarr': {
        'repr': 'Sonarr',
        'required': False,
        'priority': 2,
        'enabled': False,
        'image': 'docker.io/linuxserver/sonarr',
        'tag': 'latest',
        'ports': [7001]
    },
    'lidarr': {
        'repr': 'Lidarr',
        'required': False,
        'priority': 2,
        'enabled': False,
        'image': 'docker.io/linuxserver/lidarr',
        'tag': 'latest',
        'ports': [7002]
    },
    'bazarr': {
        'repr': 'Bazarr',
        'required': False,
        'priority': 2,
        'enabled': False,
        'image': 'docker.io/linuxserver/bazarr',
        'tag': 'latest',
        'ports': [7003]
    },
    'prowlarr': {
        'repr': 'Prowlarr',
        'required': False,
        'priority': 2,
        'enabled': False,
        'image': 'docker.io/linuxserver/prowlarr',
        'tag': 'develop',
        'ports': [7004]
    },
    'sabnzbd': {
        'repr': 'SABnzbd',
        'required': False,
        'priority': 2,
        'enabled': False,
        'image': 'docker.io/linuxserver/sabnzbd',
        'tag': 'latest',
        'ports': [7005, 9090]
    },
    'qbittorrent': {
        'repr': 'qBittorrent',
        'required': False,
        'priority': 2,
        'enabled': False,
        'image': 'docker.io/linuxserver/qbittorrent',
        'tag': 'latest',
        'ports': [7006, 6881]
    },
    'auto_backup': {
        'repr': 'Auto Backup',
        'required': False,
        'priority': 3,
        'enabled': False,
        'image': None,
        'tag': None,
        'ports': []
    },
    'auto_upload': {
        'repr': 'Auto Upload',
        'required': False,
        'priority': 3,
        'enabled': False,
        'image': None,
        'tag': None,
        'ports': []
    },
    'web': {
        'repr': 'Web Service',
        'required': False,
        'priority': 3,
        'enabled': False,
        'image': None,
        'tag': None,
        'ports': [8080]
    },
}

__available_commands__ = [
    'install',
    'uninstall',
    'start',
    'stop',
    'restart',
    'enable',
    'disable',
    'update',
    'upload',
    'backup',
    'restore',
    'status',
    'recreate-systemd',
    'start-web-server',
    'help',
]

__available_extra_args__ = [
    'debug',
    'debugerrors',
    'auto',
    'latest',
    'skip-config',
]

__arguments__ = {}

__command__ = None

from sys import argv, modules
from os import path, chdir
from uvicorn import run as start_server

# From here, importing order matters.
from .library.basher import *
from .library.system_info import *
from .library.notifications import *
from .library.directories import *

from .database.settings import *
from .database.models import *
from .database.queries import *

from .library.podman import *
from .library.systemd import *

from .api.endpoints import *

from .services.base_service import *
from .services.control import *
from .services.mergerfs import *
from .services.rclone import *
from .services.bazarr import *
from .services.lidarr import *
from .services.plex import *
from .services.prowlarr import *
from .services.qbittorrent import *
from .services.radarr import *
from .services.sabnzbd import *
from .services.sonarr import *
from .services.web import *
from .services.autobackup import *
from .services.autoupload import *


for index, arg in enumerate(argv[1:]):
    if index == 0:
        if arg in __available_commands__:
            __command__ = arg
        else:
            raise Exception('Invalid command.')
    else:
        if '--' == arg[:2]:
            if "=" in arg:
                key, val = [x.strip() for x in arg[2:].split("=", 1)]
            else:
                key, val = arg[2:], True
            __arguments__[key] = val
        else:
            raise Exception('Invalid argument.')

chdir(path.abspath(path.dirname(__file__)))  # DO NOT REMOVE.


def run():
    """
    1. This function will execute the args passed to the module.
    """
    if __command__ in ['install', 'uninstall', 'start', 'restart',
                       'stop', 'enable', 'disable', 'update',
                       'backup', 'restore', 'recreate-systemd']:
        if not __arguments__ or (len(__arguments__) == 1
                                 and any(x in __available_extra_args__ for x in __arguments__)):
            if __command__ in __available_commands__:
                getattr(Control(command=None, settings=__available_services__),
                        f'{__command__.replace("-", "_")}_all')()
            else:
                Notification('red_alert').print(
                    'Command not yet implemented or disabled.')
        else:
            for _arg in __arguments__:
                if _arg in __available_services__:
                    if __command__ in __available_commands__:
                        getattr(getattr(modules[__name__], _arg.upper().replace(
                            '_', ''))(), __command__.replace("-", "_"))()
                    else:
                        Notification('red_alert').print(
                            'Command not yet implemented or disabled.')
                else:
                    if _arg not in __available_extra_args__:
                        Notification('red_alert').print(
                            'Invalid service or argument.')
    elif __command__ == 'upload':
        RCLONE().upload()
    elif __command__ == 'start-web-server':
        start_server('podarr.api.endpoints:app', host='0.0.0.0',
                     port=8000, log_level='info')
    elif __command__ == 'help':
        print(f"""
    Available commands: {', '.join([service for service in __available_commands__ if service != 'start-web-server'])}.

    Available services: {', '.join(__available_services__)}.

    To run a command to all services (example): podarr restart

    To run a command to a specific service (example): podarr restart --plex

    The restore command can receive additional parameter (--latest), to automatically choose the latest backups (example): podarr restore --latest

    Pass --debug parameter to debug every command ran by podarr (example): podarr restart --debug
    
    Pass --debugerrors parameter to debug errors of every command ran by podarr (example): podarr restart --debugerrors
        """)
    else:
        Notification('red_alert').print(
            'Command not yet implemented or disabled.')
    SESSION_MAKER.close()  # Close the database connection.
