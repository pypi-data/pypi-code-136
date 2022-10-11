'''
SpeedDB, a simple open source multi-model database

https://github.com/SpeedDB

###### Made by Nawaf Alqari in 2022 :)

'''

__version__ = "1.1.2"
__all__ = ["connect", "DocumentDatabase", "KeyValDatabase", "init", "build_db", "destroy_db", "TasksQueue", "run_shell"]

from .database import connect, DocumentDatabase, KeyValDatabase, init, build_db, destroy_db
from .tasks_queue import TasksQueue
from .shell import run_shell