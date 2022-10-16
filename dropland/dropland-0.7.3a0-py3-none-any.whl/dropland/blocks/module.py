from dependency_injector import containers, providers

from app.module import Module

from .redis import USE_REDIS
from .rmq import USE_RMQ
from .scheduler import USE_SCHEDULER
from .sql import USE_SQL
from dependency_injector import containers, providers

from app.module import Module
from .redis import USE_REDIS
from .rmq import USE_RMQ
from .scheduler import USE_SCHEDULER
from .sql import USE_SQL

__blocks__ = dict()


if USE_REDIS:
    from .redis.containers import RedisBlock
    __blocks__['redis'] = RedisBlock

if USE_RMQ:
    from .rmq.containers import RmqBlock
    __blocks__['rmq'] = RmqBlock

if USE_SCHEDULER:
    from .scheduler.containers import SchedulerBlock
    __blocks__['scheduler'] = SchedulerBlock

if USE_SQL:
    from .sql.containers import SqlBlock
    __blocks__['sql'] = SqlBlock


class BlocksContainer(containers.DeclarativeContainer):
    __self__ = providers.Self()

    blocks = providers.Aggregate(**{
        name: providers.Factory(class_) for name, class_ in __blocks__.items()
    })


class BlocksModule(Module):
    pass

