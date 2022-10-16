import asyncio
import inspect
import sys
from datetime import datetime
from functools import partial
from threading import Timer
from typing import Any, Callable, Optional

import sqlalchemy as sa
from alert_msgs import ContentType, FontSize, Map, Text, send_alert

from .tables import task_errors_table, task_runs_table
from .utils import AlertSettings, get_engine, logger


class TaskLogger:
    def __init__(
        self,
        name: str,
        required: bool,
        settings: Optional[AlertSettings],
        exit_on_complete: bool,
    ):
        self.name = name
        self.required = required
        self.settings = settings or AlertSettings()
        self.exit_on_complete=exit_on_complete

        self.alert_methods = []
        if self.settings.alert_email:
            self.alert_methods.append("email")
        if self.settings.alert_slack:
            self.alert_methods.append("slack")

        if not self.alert_methods and any(
            (self.settings.alert_on_start, self.settings.alert_on_error, self.settings.alert_on_finish)
        ):
            raise ValueError(
                "Can not send alerts unless `alert_slack` or `alert_email` is True."
            )
        self._send_alerts = partial(send_alert, methods=self.alert_methods)
        self.engine = get_engine()
        self.errors = []
        self._task_start_recorded = False

    def record_task_start(self):
        self.start_time = datetime.utcnow()
        with self.engine.begin() as conn:
            conn.execute(
                sa.insert(task_runs_table).values(
                    {"task_name": self.name, "started": self.start_time}
                )
            )
        self._task_start_recorded = True
        if self.settings.alert_on_start:
            self._alert_task_start()

    def record_task_error(self, error: Exception):
        self.errors.append(error)
        with self.engine.begin() as conn:
            statement = sa.insert(task_errors_table).values(
                {
                    "task_name": self.name,
                    "type": str(type(error)),
                    "message": str(error),
                }
            )
            conn.execute(statement)
        if self.settings.alert_on_error:
            self._alert_task_error(error)

    def record_task_finish(
        self,
        success: bool,
        return_value: Any = None,
        retries: int = 0,
    ) -> datetime:
        if not self._task_start_recorded:
            raise RuntimeError(
                "Task finish can not be recorded unless task start is recoded first."
            )

        self.finish_time = datetime.utcnow()
        self.success = success
        self.return_value = return_value
        self.retries = retries
        self.status = "success" if success else "failed"

        with self.engine.begin() as conn:
            conn.execute(
                sa.update(task_runs_table)
                .where(
                    task_runs_table.c.task_name == self.name,
                    task_runs_table.c.started == self.start_time,
                )
                .values(
                    finished=self.finish_time,
                    retries=self.retries,
                    status=self.status,
                    return_value=self.return_value,
                )
            )

        if self.settings.alert_on_finish:
            self._alert_task_finish()

        if self.errors and self.required:
            if self.exit_on_complete:
                sys.exit(1)
            if len(self.errors) > 1:
                raise Exception(f"Error executing task {self.name}: {self.errors}")
            raise type(self.errors[0])(str(self.errors[0]))
        if self.exit_on_complete:
            sys.exit(0 if success else 1)

    def _alert_task_start(self):
        msg = (
            f"Started task {self.name} {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        components = [
            Text(
                msg,
                font_size=FontSize.LARGE,
                content_type=ContentType.IMPORTANT,
            )
        ]
        self._send_alerts(subject=msg, components=components)

    def _alert_task_error(self, error: Exception):
        subject = f"Error executing task {self.name}: {type(error)}"
        components = [
            Text(
                f"{subject} -- {error}",
                font_size=FontSize.LARGE,
                content_type=ContentType.ERROR,
            )
        ]
        self._send_alerts(subject=subject, components=components)

    def _alert_task_finish(self):
        subject = f"{self.status}: {self.name}"
        components = [
            Text(
                subject,
                font_size=FontSize.LARGE,
                content_type=ContentType.IMPORTANT if self.success else ContentType.ERROR,
            ),
            Map(
                {
                    "Start": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "Finish": self.finish_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "Return Value": self.return_value,
                }
            ),
        ]
        if self.errors:
            components.append(
                Text(
                    "ERRORS",
                    font_size=FontSize.LARGE,
                    content_type=ContentType.ERROR,
                )
            )
            for e in self.errors:
                components.append(
                    Text(
                        f"{type(e)}: {e}",
                        font_size=FontSize.MEDIUM,
                        content_type=ContentType.INFO,
                    )
                )
        self._send_alerts(subject=subject, components=components)


def task(
    name: str,
    required: bool = False,
    retries: int = 0,
    timeout: Optional[int] = None,
    settings: Optional[AlertSettings] = None,
    exit_on_complete: Optional[bool] = None,
):
    """Decorator for async tasks.

    Args:
        name (str): Name which should be used to identify the task.
        required (bool, optional): Requited tasks will raise exceptions. Defaults to False.
        retries (int, optional): How many times the task can be retried on failure. Defaults to 0.
        timeout (Optional[int], optional): Timeout for function execution. Defaults to None.
        settings (Optional[AlertSettings], optional): Settings for alerts.
        exit_on_complete (bool): Exit Python interpreter with task result status code when task is finished. Defaults to False.
    """

    def task_decorator(func):
        #@functools.wraps(func)
        task_logger = TaskLogger(
            name=name,
            required=required,
            settings=settings,
            exit_on_complete=exit_on_complete,
        )
        wrapper = _async_task_wrapper if inspect.iscoroutinefunction(func) else _task_wrapper
        # TODO lambda?
        return partial(wrapper, func=func, retries=retries, timeout=timeout, task_logger=task_logger)
    return task_decorator


def _task_wrapper(func: Callable, retries: int, timeout: float, task_logger: TaskLogger, *args, **kwargs):
    task_logger.record_task_start()
    for i in range(retries + 1):
        try:
            if timeout:
                # TODO error function
                (timer := Timer(timeout, lambda: RuntimeError)).start()
                result = func(*args, **kwargs)
                timer.cancel()
            else:
                result = func(*args, **kwargs)
            task_logger.record_task_finish(
                success=True, retries=i, return_value=result
            )
            return result
        except Exception as e:
            logger.error(
                f"Error executing task {task_logger.name}. Retries remaining: {retries-i}.\n({type(e)}) -- {e}"
            )
            task_logger.record_task_error(e)
    task_logger.record_task_finish(success=False, retries=retries)


async def _async_task_wrapper(func: Callable, retries: int, timeout: float, task_logger: TaskLogger, *args, **kwargs):
    task_logger.record_task_start()
    for i in range(retries + 1):
        try:
            if timeout:
                result = await asyncio.wait_for(func(*args, **kwargs), timeout)
            else:
                result = await func(*args, **kwargs)
            task_logger.record_task_finish(
                success=True, retries=i, return_value=result
            )
            return result
        except Exception as e:
            logger.error(
                f"Error executing task {task_logger.name}. Retries remaining: {retries-i}.\n({type(e)}) -- {e}"
            )
            task_logger.record_task_error(e)
    task_logger.record_task_finish(success=False, retries=retries)
