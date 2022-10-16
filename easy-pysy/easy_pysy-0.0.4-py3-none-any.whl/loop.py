import logging
from dataclasses import dataclass
from typing import Callable, Optional

import easy_pysi
from easy_pysi.plugin import Plugin
from easy_pysi.utils import Interval


logger = logging.getLogger(__name__)


@dataclass
class Loop:
    interval_ms: 1000
    callback: Callable
    stop_app_on_error: bool
    auto_start: bool
    interval: Optional[Interval] = None

    def start(self):
        self.interval = Interval(self.interval_ms, self.callback, self.on_error)
        self.interval.start()

    def stop(self):
        self.interval.stop()
        self.interval = None

    def on_error(self, exception: BaseException):
        logger.error(f'Loop execution failed: {exception}')
        if self.stop_app_on_error:
            easy_pysi.current_app().stop()

    @property
    def running(self):
        return self.interval is not None


class LoopPlugin(Plugin):
    loops: list[Loop] = []

    def start(self):
        # Init loops
        self.loops = [
            loop
            for loop in _ALL_LOOPS
            if self.app.is_available(loop.callback)
        ]

        for loop in self.loops:
            if loop.auto_start:
                logger.debug(f'Starting {loop}')
                loop.start()

    def stop(self):
        for loop in self.loops:
            if loop.running:
                loop.stop()

    def get_loop(self, callback: Callable) -> Optional[Loop]:
        # TODO: nice to have :
        # ez._(self.loops).get(lambda loop: loop.callback == callback)
        for loop in self.loops:
            if loop.callback == callback:
                return loop


_ALL_LOOPS: list[Loop] = []


def loop(every_ms: float, stop_app_on_error=True, auto_start=True):
    def decorator(func):
        loop = Loop(every_ms, func, stop_app_on_error, auto_start)
        _ALL_LOOPS.append(loop)
        return func
    return decorator
