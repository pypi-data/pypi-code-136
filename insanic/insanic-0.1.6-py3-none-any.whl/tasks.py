from functools import partial
from typing import Coroutine

from arq import create_pool
from arq.connections import RedisSettings
from arq.worker import Worker as ArqWorker
from sanic import Sanic


class Task:
    @classmethod
    async def enqueue(cls, *args, job_id: str | None = None, **kwargs):
        application = Sanic.get_app()
        task_name = cls.__qualname__

        await application.ctx.redis_pool.enqueue_job(task_name, *args, _job_id=job_id, **kwargs)

class TaskDefinition:
    workers: int
    poll_delay: float

    task_cls: Task

    def __init__(self, task_cls: Task, workers: int = 1, poll_delay: float = 0.5):
        self.task_cls = task_cls

        self.workers = workers
        self.poll_delay = poll_delay

async def init_redis_pool() -> None:
    application = Sanic.get_app()
    redis_url = application.config.REDIS_URL
    application.ctx.redis_pool = await create_pool(RedisSettings.from_dsn(redis_url))

async def close_redis_pool() -> None:
    #@TODO: Implement pool release
    pass

async def run_task(ctx, *args, task_cls: type[Task], **kwargs) -> None:
    task = task_cls()
    await task.execute(*args, **kwargs)

def run_workers(task_name, task_definition: TaskDefinition) -> None:
    worker_function = partial(run_task, task_cls=task_definition.task_cls)
    # Some hack to pass partial to ArqWorker (see arq/worker.py:81)
    worker_function.__qualname__ = task_definition.task_cls.__qualname__

    worker = ArqWorker(
        functions=[worker_function],
        max_jobs=task_definition.workers,
        poll_delay=task_definition.poll_delay,
        keep_result=0,
    )

    worker.run()
