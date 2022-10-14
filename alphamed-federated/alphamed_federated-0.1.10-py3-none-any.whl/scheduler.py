"""Algorithm scheduler."""


from abc import ABC, abstractmethod
from functools import wraps
from tempfile import TemporaryFile
from typing import Dict, Iterable

import cloudpickle as pickle

from . import logger, task_logger
from .bass import BassProxy
from .metrics_trace import MetricsTrace


class ConfigError(Exception):
    ...


class TaskFailed(Exception):
    ...


class TaskComplete(Exception):
    ...


class DataChecker(ABC):
    """To verify local data state."""

    def __init__(self, task_id: str) -> None:
        super().__init__()
        assert task_id and isinstance(task_id, str), 'Must specify task ID.'
        self.task_id = task_id

    @property
    def bass_proxy(self) -> BassProxy:
        if not hasattr(self, '_bass_proxy'):
            self._bass_proxy = BassProxy()
        return self._bass_proxy

    @abstractmethod
    def verify_data(self) -> bool:
        """Verify if local data is ready or not."""

    def execute_verification(self):
        """Run data verification logic and deal with the result."""
        is_succ = self.verify_data()
        self.bass_proxy.notify_dataset_state(task_id=self.task_id, verified=is_succ)
        logger.info(f'Local dataset verification returns: {is_succ}.')


class Scheduler(ABC):

    def __init__(self) -> None:
        super().__init__()
        self._metrics_bucket: Dict[str, MetricsTrace] = {}

    @property
    def bass_proxy(self) -> BassProxy:
        if not hasattr(self, '_bass_proxy'):
            self._bass_proxy = BassProxy()
        return self._bass_proxy

    def launch_task(self, task_id: str):
        """Launch current task."""
        assert task_id and isinstance(task_id, str), f'invalid task ID: {task_id}'

        with TemporaryFile() as tf:
            pickle.dump(self, tf)
            tf.seek(0)
            file_key = self.bass_proxy.upload_file(upload_name='model.pickle', fp=tf)
        self.bass_proxy.launch_task(task_id=task_id, pickle_file_key=file_key)

    def push_log(self, message: str):
        """Push a running log message to the task manager."""
        assert message and isinstance(message, str), f'invalid log message: {message}'
        if hasattr(self, 'task_id') and self.task_id:
            task_logger.info(message, extra={"task_id": self.task_id})
        else:
            logger.warn('Failed to push a message because context is not initialized.')

    def get_metrics(self, name: str) -> MetricsTrace:
        return self._metrics_bucket.get(name)

    def _switch_status(self, _status: str):
        """Switch to a new status and leave a log."""
        self.status = _status
        logger.debug(f'{self.status=}')

    @abstractmethod
    def _run(self, id: str, task_id: str, is_initiator: bool = False):
        """Run the scheduler.

        This function is used by the context manager, DO NOT modify it, otherwize
        there would be strange errors raised.

        :args
            :id
                the node id of the running context
            :task_id
                the id of the task to be scheduled
            :is_initiator
                is this scheduler the initiator of the task
        """


def register_metrics(name: str, keys: Iterable[str]):
    """Register a metrics trace.

    The trace fo the metrics during training will be included in the task's
    running result and can be downloaded. However, the trace content should
    be appended manually.

    If the specified name has already registered before, nothing changes.

    :args
        :name
            The name of the metrics trace.
        :keys
            The names of the metrics items.
    """
    def decorate(func):
        if not name or not isinstance(name, str):
            raise ValueError(f'invalid name of the metrics: {name}')
        if not keys or not isinstance(keys, Iterable):
            raise ValueError(f'invalid keys of the metrics: {keys}')

        @wraps(func)
        def wrapper(_self, *args, **kwargs):
            if not isinstance(_self, Scheduler) or func.__name__ != 'test':
                raise RuntimeError(
                    'Only applicable on "test" function of a "Scheduler" object.'
                )
            if name not in _self._metrics_bucket:
                _self._metrics_bucket[name] = MetricsTrace(headers=keys)
            return func(_self, *args, **kwargs)

        return wrapper
    return decorate
