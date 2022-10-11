from dataclasses import dataclass
import logging
import sys
from typing import List

from .methods.abc import ABCMethod
from .messagers.abc import ABCMessager


class Config:
    def __init__(self, chats: List["Chat"], tasks: List["Task"]) -> None:
        self.chats = {v.name: v for v in chats}
        self.tasks = {v.name: v for v in tasks}
        if len(self.tasks) != len(tasks):
            logging.getLogger("cmb").critical(f"config error, task name should be unique")
            sys.exit(1)
        if len(self.chats) != len(chats):
            logging.getLogger("cmb").critical(f"config error, chat name should be unique")
            sys.exit(1)
        for t in self.tasks.values():
            ch = [x for x in t.messagers if x not in self.chats]
            if ch:
                logging.getLogger("cmb").critical(f"config error, check messagers ids {ch}")
                sys.exit(1)

@dataclass
class Task:
    name: str
    method: ABCMethod
    checkPeriod: str
    messagers: List[str]
    roundRodinSkip: bool = False


@dataclass
class Chat:
    name: str
    messager: ABCMessager
