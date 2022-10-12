import os
import sys

from dependency_injector import containers, providers

from dropland.app.base import ContainerBlock, ResourceBlock
from dropland.log import logger, tr
from dropland.util import default_value
from .engine import EngineConfig, SchedulerBackend


class SchedulerBlock(ContainerBlock, ResourceBlock):
    def sync_startup(self, *args, **kwargs):
        if self.initialized:
            return
        self.container.get_scheduler().start()
        logger.info(tr('dropland.blocks.scheduler.started'))
        self._initialized = True

    def sync_shutdown(self, *args, **kwargs):
        if not self.initialized:
            return
        self.container.get_scheduler().shutdown(wait=True)
        logger.info(tr('dropland.blocks.scheduler.stopped'))
        self._initialized = False

    async def startup(self, *args, **kwargs):
        if self.initialized:
            return
        self.container.get_scheduler().start()
        logger.info(tr('dropland.blocks.scheduler.started'))
        self._initialized = True

    async def shutdown(self, *args, **kwargs):
        if not self.initialized:
            return
        self.container.get_scheduler().shutdown(wait=True)
        logger.info(tr('dropland.blocks.scheduler.stopped'))
        self._initialized = False

    def get_engine(self, *args, **kwargs):
        return self.container.create_engine(*args, **kwargs)

    def get_instance(self):
        return self.container.get_scheduler()


class SimpleSchedulerContainer(containers.DeclarativeContainer):
    __self__ = providers.Self()

    # noinspection PyMethodMayBeStatic
    def _as_service(self):
        return 'worker' == sys.argv[0]

    as_service = providers.Factory(_as_service, __self__)
    engine_factory = providers.Singleton(SchedulerBackend, as_service)

    def _create_engine(self, *args, **kwargs):
        return self.engine_factory().create_engine(*args, **kwargs)

    create_engine = providers.Factory(_create_engine, __self__)
    get_scheduler = providers.Factory(create_engine)
    instance = providers.Singleton(SchedulerBlock)

    wiring_config = containers.WiringConfiguration(
        modules=['.application', '.local']
    )


class SchedulerContainer(SimpleSchedulerContainer):
    __self__ = providers.Self()
    config = providers.Configuration()

    def _create_engine(self):
        if isinstance(self.config.engine_config(), EngineConfig):
            engine_config = self.config.engine_config()
        else:
            engine_config = EngineConfig(
                sql_url=self.config.engine_config.sql_url(),
                sql_tablename=self.config.engine_config.sql_tablename(),
                redis_url=self.config.engine_config.redis_url(),
                redis_job_key=self.config.engine_config.redis_job_key(),
                job_coalesce=self.config.engine_config.job_coalesce.as_(bool)(),
                job_max_instances=self.config.engine_config.
                    job_max_instances.as_(default_value(int))(default=1),
                job_misfire_grace_time=self.config.engine_config.
                    job_misfire_grace_time.as_(default_value(int))(default=24 * 3600),
                task_host=self.config.engine_config.task_host(),
                task_port=self.config.engine_config.task_port(),
                task_processes=self.config.engine_config.
                    task_processes.as_(default_value(int))(default=os.cpu_count()),
                task_workers=self.config.engine_config.
                    task_workers.as_(default_value(int))(default=os.cpu_count()),
                task_rpc_timeout_seconds=self.config.engine_config.
                    task_rpc_timeout_seconds.as_(default_value(int))(default=5),
                task_rpc_num_connect_attempts=self.config.engine_config.
                    task_rpc_num_connect_attempts.as_(default_value(int))(default=10),
                create_remote_engine=self.config.engine_config.create_remote_engine.as_(bool)(),
                timezone=self.config.engine_config.timezone(default='UTC')
            )
        return SimpleSchedulerContainer._create_engine(self, self.config.name(), engine_config)

    create_engine = providers.Factory(_create_engine, __self__)
    get_scheduler = providers.Factory(create_engine)

    wiring_config = containers.WiringConfiguration(
        modules=['.application', '.local']
    )
