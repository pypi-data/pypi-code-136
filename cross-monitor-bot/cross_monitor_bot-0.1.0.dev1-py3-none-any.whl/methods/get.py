from typing import Any, Callable, Dict, Hashable, Optional
import requests
import logging

from .abc import ABCMethod


class GetMethod(ABCMethod):
    def __init__(self, url: str, path: str='', responseHandler: Optional[Callable[[Dict[Hashable, Any]], bool]]=None,
                 **kwargs) -> None:
        self.url = url
        self.path = path
        self.responseHandler = responseHandler
        logger = logging.getLogger("cmb")
        if logger:
            self.logger = logger
        else:
            self.logger = logging.Logger("cmb", logging.WARNING)

    def isOk(self):
        try:
            r = requests.get(self.url+self.path, timeout=10)
            if r.status_code == 200:
                if not self.responseHandler or self.responseHandler(r.json()):
                    return True
        except Exception as e:
            self.logger.error(e)
        return False
