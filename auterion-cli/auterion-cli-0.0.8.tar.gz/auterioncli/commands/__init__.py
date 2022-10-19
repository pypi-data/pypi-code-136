from .app_command import AppCommand
from .container_command import ContainerCommand
from .info_command import InfoCommand
from .report_command import ReportCommand
from .devices_command import DevicesCommand


def available_commands(config):
    return {
        'app': AppCommand(config),
        'container': ContainerCommand(config),
        'info': InfoCommand(config),
        'report': ReportCommand(config),
        'devices': DevicesCommand(config)
    }
