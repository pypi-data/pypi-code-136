import logging
import platform
import os

from .abc import ABCMethod


class PingMethod(ABCMethod):
    def __init__(self, host: str, **kwargs) -> None:
        self.host = host
        logger = logging.getLogger("cmb")
        if logger:
            self.logger = logger
        else:
            self.logger = logging.Logger("cmb", logging.WARNING)

    def isOk(self):
        try:
            param = '-n' if platform.system().lower()=='windows' else '-c'
            # noping still may return 0 exitcode on windows
            r = os.popen(f"ping {param} {1} {self.host}").readlines()
            if any("ttl=" in x.lower() for x in r):
                return True
        except Exception as e:
            self.logger.error(e, exc_info=True)
        return False
