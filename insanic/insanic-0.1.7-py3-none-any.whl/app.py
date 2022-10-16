from __future__ import annotations

import importlib
from asyncio import AbstractEventLoop
from typing import Any

from sanic import Sanic

from insanic.config import DEFAULT_CONFIG, CONFIG_ENV_PREFIX
from insanic.db import init_db_connection, close_db_connection
from insanic.http import Request
from insanic.logger import init_logger, log
from insanic.tasks import init_redis_pool, close_redis_pool

class Application(Sanic):
    def __init__(self, *args: Any, **kwargs: Any):
        # @TODO: Implement custom error handler

        # Overriding Sanic default implementations
        kwargs['strict_slashes'] = False  # Disabling last slash at URL
        kwargs['request_class'] = Request  # Setting up custom Request class
        kwargs['configure_logging'] = False  # Disabling default Sanic logging configuration
        super().__init__(*args, **kwargs)

        # @FIXME: Move to config.py:load_configuration
        self.load_configuration()
        init_logger()

        self.register_listener(self.boot, 'before_server_start')
        self.register_listener(self.shutdown, 'after_server_stop')

    def load_configuration(self) -> None:
        # Default configuration
        self.config.update_config(DEFAULT_CONFIG)

        # Application configuration
        try:
            application_config = importlib.import_module('config', package='src') # importing src/config.py
            self.config.update_config(application_config)
        except ModuleNotFoundError as _error:
            # @TODO: Raise Insanic error
            pass

        # @FIXME: Remove support of _local.py config files. Use .env file instead
        try:
            local_config = importlib.import_module('config_local', package='src')  # importing src/config_local.py
            self.config.update_config(local_config)
        except ModuleNotFoundError as _error:
            pass

        # Applying ENV config
        self.config.load_environment_vars(prefix=CONFIG_ENV_PREFIX)

    async def boot(self, _application: Application, _loop: AbstractEventLoop) -> None: # pylint: disable=no-self-use
        await init_db_connection()
        await init_redis_pool()

    async def shutdown(self, _application: Application, _loop: AbstractEventLoop) -> None: # pylint: disable=no-self-use
        await close_db_connection()
        await close_redis_pool()
