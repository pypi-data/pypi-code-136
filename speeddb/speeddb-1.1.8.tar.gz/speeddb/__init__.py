'''
# SpeedDB
## a simple open source multi-model database

* [Documentation](https://speeddb.github.io/)
* [Repository](https://github.com/SpeedDB/speeddb)
* [Discord](https://discord.gg/Az8McWNAcg)

###### Made by Nawaf Alqari in 2022 :)

'''

__version__ = "1.1.8"
__all__ = ["connect", "DocumentDatabase", "KeyValDatabase", "init", "build_db", "destroy_db", "TasksQueue", "Collection", "Browser"]

from .database import DocumentDatabase, KeyValDatabase, Collection, connect, init, build_db, destroy_db
from .browser import Browser
from .tasks_queue import TasksQueue