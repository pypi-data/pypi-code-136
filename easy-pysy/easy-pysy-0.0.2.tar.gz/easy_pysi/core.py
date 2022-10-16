import enum
import inspect
import logging
import os
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from typing import Type, TypeVar

from easy_pysi import signal
from easy_pysi.cli import run_cli
from easy_pysi.configuration import ConfigurationPlugin
from easy_pysi.event import Event, emit, EventPlugin
from easy_pysi.loop import LoopPlugin
from easy_pysi.plugin import Plugin
from easy_pysi.provider import ProviderPlugin
from easy_pysi.utils import require

logger = logging.getLogger(__name__)

T = TypeVar('T')
PluginType = TypeVar('PluginType', bound=Plugin)


class AppState(enum.Enum):
    STOPPED = 1
    INITIALIZING = 2
    STARTING = 3
    STARTED = 4
    STOPPING = 5


class App:
    modules: list[ModuleType]
    state: AppState = AppState.STOPPED
    root_directory: Path = Path(os.getcwd()).resolve()
    dotenv_path: Path = Path(os.getcwd(), '.env').resolve()
    plugins: list[Plugin] = [
        EventPlugin(),
        LoopPlugin(),
        ConfigurationPlugin(),
        ProviderPlugin(),
    ]

    def start(self):
        require(self.state == AppState.STOPPED, f"Can't start application, current state: {self.state}]")

        logger.info('EZ INIT')
        logging.basicConfig(level=logging.INFO)  # TODO: where ?
        self.state = AppState.INITIALIZING
        for plugin in self.plugins:
            plugin.init(self)

        logger.info('EZ Start')
        self.state = AppState.STARTING
        for plugin in self.plugins:
            plugin.start()

        self.state = AppState.STARTED
        applications.append(self)
        emit(AppStarted(self))

    def stop(self):
        require(self.state == AppState.STARTED, f"Can't stop application, current state: {self.state}")
        logger.info(f'Stopping {self}')
        self.state = AppState.STOPPING
        for plugin in self.plugins:
            plugin.stop()

        applications.remove(self)
        self.state = AppState.STOPPED

    def get_plugin(self, plugin_type: Type[PluginType]) -> PluginType:
        for plugin in self.plugins:
            if isinstance(plugin, plugin_type):
                return plugin
        raise RuntimeError(f'No Plugin found for: {plugin_type}')

    def is_available(self, object) -> bool:
        object_module = inspect.getmodule(object)
        return object_module in self.modules

    def run(self, auto_start=True):
        if auto_start and self.state == AppState.STOPPED:
            self.start()
        run_cli()


@dataclass
class AppStarted(Event):
    app: App


applications: list[App] = []


def current_app():
    return applications[-1]


def plugin(plugin_type: Type[PluginType]) -> PluginType:
    return current_app().get_plugin(plugin_type)


def shutdown(exit_code=0):
    stop_all()
    exit(exit_code)


def stop_all():
    logger.info('Stopping all applications')
    # [:] is used to iterate over a copy of applications (since app.stop() will remove app from applications)
    for app in applications[:]:
        app.stop()


signal.sigint_callback = shutdown

