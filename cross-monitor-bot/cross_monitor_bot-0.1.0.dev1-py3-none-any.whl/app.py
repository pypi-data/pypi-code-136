from datetime import datetime
from threading import Thread
from time import sleep
from typing import Dict, List
import logging

from croniter import croniter

from .config import Config, Task


class App:
    def __init__(self, selfName: str, config: Config, tz=None, sendRepeat=3) -> None:
        self.config = config
        self.selfName = selfName
        self.tz = tz or datetime.now().astimezone().tzinfo
        self.sendRepeat = max(sendRepeat, 1)
        logger = logging.getLogger("cmb")
        if logger:
            self.logger = logger
        else:
            self.logger = logging.Logger("cmb", logging.WARNING)
        self._threads: List[Thread] = []
        self._statuses: Dict[str, bool] = {}

    def _serveTask(self, task: Task):
        nxt = croniter(task.checkPeriod, datetime.now(tz=self.tz))
        startTimeout = None
        highers = []
        for x in self.config.tasks.values():
            if x.name == task.name:
                break
            if not x.roundRodinSkip:
                highers.append(x.name)
        while True:
            try:
                self.logger.debug(f"check status, {task.name}")
                ok = task.method.isOk()
                self.logger.debug(f"status {ok}, {task.name}")
                if ok and not startTimeout or not ok and startTimeout:
                    continue
                if not startTimeout and any(self._statuses[x] for x in highers):
                    continue
                if not startTimeout:
                    startTimeout = datetime.now(tz=self.tz)
                for m in task.messagers:
                    self.logger.debug(f"send message to {m}, {task.name}")
                    rep = 0
                    while rep != self.sendRepeat:
                        r = self.config.chats[m].messager.report(checker=self.selfName, target=task.name, status=ok,
                                                                start=startTimeout,
                                                                end=(datetime.now(tz=self.tz) if ok else None))
                        if not r:
                            rep += 1
                            self.logger.error(f"cannot send message to {m}")
                            sleep(10)
                        break
                if ok:
                    startTimeout = None
            finally:
                toSleep = max(nxt.get_next() - datetime.now(tz=self.tz).timestamp(), 0)
                self.logger.debug(f"sleep {toSleep}sec, {task.name}")
                sleep(toSleep)


    def run(self):
        self.logger.debug("start")
        for task in self.config.tasks.values():
            if self.selfName == task.name:
                continue
            self._statuses[task.name] = True
            t = Thread(target=self._serveTask, args=[task], daemon=True)
            t.start()
            self._threads.append(t)
        self.logger.debug("tasks are assigned")
        while True:
            for t in self._threads:
                if not t.is_alive():
                    self.logger.critical("thread is dead")
                    return
            sleep(120)
