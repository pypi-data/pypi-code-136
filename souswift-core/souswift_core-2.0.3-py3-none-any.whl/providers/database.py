import logging

import sqlalchemy as sa
from context_handler.ext import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from starlette.datastructures import State

from souswift_core.providers.config import DatabaseConfig


class DatabaseProvider(sqlalchemy.AsyncSaAdapter):
    state_name = 'database_provider'

    def __init__(
        self, database_config: DatabaseConfig, logger: logging.Logger
    ) -> None:
        self.config = database_config
        self.logger = logger
        engine, self._sync_engine = self._create_engine()
        super().__init__(engine=engine)

    def _create_engine(self):
        return (
            create_async_engine(
                self.config.get_uri(is_async=True), **self.config.pool_config
            ),
            create_engine(
                self.config.get_uri(is_async=False), **self.config.pool_config
            ),
        )

    async def health_check(self):
        async with self.context().begin() as connection:
            await connection.execute(sa.text('SELECT 1'))
        self.logger.info('Database Connection Succeeded')


def setup_database(
    config: DatabaseConfig,
    logger: logging.Logger,
):
    async def _setup_database(state: State):
        provider = DatabaseProvider(config, logger)
        setattr(
            state,
            DatabaseProvider.state_name,
            provider,
        )
        await provider.health_check()

    return _setup_database
