from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import QueuePool


class ParentModel(ABC):

    _instance = None
    engine = None

    def __init__(self, url):
        if self._instance is None and self.engine is None:
            self._instance = True
            self.engine = create_engine(url, pool_size=10, max_overflow=5)
