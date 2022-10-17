from __future__ import annotations

import asyncio
import datetime
import os
import uuid
from dataclasses import dataclass, field
from functools import partial
from time import time_ns
from typing import Dict, Callable, Coroutine, Any, TypeVar, Generic

import loguru
from apscheduler.events import EVENT_JOB_SUBMITTED, JobSubmissionEvent, JobExecutionEvent, \
    EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from apscheduler.executors.base import BaseExecutor
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.job import Job
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.base import BaseTrigger
from apscheduler.triggers.interval import IntervalTrigger
from pytz import utc

from web_foundation.kernel.channel import IMessage
from web_foundation.utils.helpers import get_callable_from_fnc

BackgroundTask = TypeVar("BackgroundTask", Callable[..., Coroutine[Any, Any, Any]], partial)


@dataclass
class Task:
    id: str
    status: str
    name: str
    scheduled_trigger: BaseTrigger
    scheduled_job: Job | None = field(default=None)
    on_error_callback: TaskErrorCallback = field(default=None)
    next_call_time: datetime.datetime | None = field(default=None)
    execution_time: float = field(default=0)
    done_time: float = field(default=0)
    call_time: float = field(default=0)
    call_counter: int = field(default=0)
    create_time: datetime.datetime | None = field(default_factory=datetime.datetime.now)
    error: BaseException | None = field(default=None)
    return_event: bool = False


TaskErrorCallback = Callable[[JobExecutionEvent, Task], Coroutine[Any, Any, None]]


class TaskIMessage(IMessage):
    message_type = "background_task"
    task: BackgroundTask
    args: Any | None
    kwargs: Any | None
    trigger: BaseTrigger
    add_job_kw: Dict
    on_error_callback: TaskErrorCallback
    return_event: bool
    destination = "__dispatcher__"

    def __init__(self, task: BackgroundTask,
                 trigger=None,
                 args: Any = None,
                 kwargs: Any | None = None,
                 add_job_kw: Dict = None,
                 on_error_callback: TaskErrorCallback = None,
                 return_event: bool = False):
        super().__init__()
        self.task = task
        self.args = args
        self.kwargs = kwargs
        self.add_job_kw = add_job_kw if add_job_kw else {}
        self.trigger = trigger
        self.on_error_callback = on_error_callback
        self.return_event = return_event


ProduceCall = Callable[[TaskIMessage], Coroutine[Any, Any, None]]


class TaskScheduler:
    _tasks: Dict[str, Task]
    _scheduler: BackgroundScheduler
    produce_method: ProduceCall

    def __init__(self, produce_method: ProduceCall, executors: Dict[str, BaseExecutor] = None, job_defaults=None,
                 **kwargs):
        self._tasks = {}
        self.produce_method = produce_method
        executor = {
            'default': ProcessPoolExecutor(os.cpu_count())
        }
        job_default = {
            "misfire_grace_time": 1,
            'coalesce': False,
            'max_instances': 10
        }
        self._scheduler = BackgroundScheduler(jobstores={"default": MemoryJobStore()},
                                              executors=executors if executors else executor,
                                              job_defaults=job_defaults if job_defaults else job_default,
                                              timezone=utc)
        self._add_listeners()

    async def add_task(self, message: TaskIMessage):
        message.task = get_callable_from_fnc(message.task)

        if isinstance(message.trigger, IntervalTrigger):
            for task_id, task in self._tasks.items():
                if task.scheduled_job.func == message.task:
                    task.scheduled_job.trigger = message.trigger
                    task.scheduled_trigger = message.trigger
                    return

        arc_task = Task(id=str(uuid.uuid4()),
                        name=message.task.__name__,
                        status="new",
                        scheduled_trigger=message.trigger,
                        on_error_callback=message.on_error_callback,
                        return_event=message.return_event)
        arc_task.scheduled_job = self._scheduler.add_job(message.task,
                                                         name=arc_task.name,
                                                         id=arc_task.id,
                                                         trigger=message.trigger,
                                                         args=message.args,
                                                         kwargs=message.kwargs,
                                                         **message.add_job_kw)
        loguru.logger.warning(arc_task.scheduled_job)
        loguru.logger.warning(os.getpid())
        arc_task.next_call_time = arc_task.scheduled_job.next_run_time
        self._tasks.update({arc_task.id: arc_task})

    def _add_listeners(self):
        def _on_job_submitted(event: JobSubmissionEvent):
            nonlocal self
            task = self._tasks.get(event.job_id)
            task.call_time = time_ns()
            task.call_counter += 1
            task.status = "called"

        def _on_job_exec(event: JobExecutionEvent):
            nonlocal self
            task = self._tasks.get(event.job_id)
            task.done_time = time_ns()
            task.execution_time = task.done_time - task.call_time
            task.status = "done"
            task.next_call_time = task.scheduled_job.next_run_time
            if event.exception:
                task.error = event.exception
                task.status = 'error'
                if task.on_error_callback:
                    asyncio.run(task.on_error_callback(event, task))
            elif task.return_event and event.retval:
                asyncio.run(self.produce_method(event.retval))

        self._scheduler.add_listener(_on_job_submitted, EVENT_JOB_SUBMITTED)
        self._scheduler.add_listener(_on_job_exec, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

    def close(self, *args, **kwargs):
        self._scheduler.shutdown()

    def perform(self):
        self._scheduler.start()
