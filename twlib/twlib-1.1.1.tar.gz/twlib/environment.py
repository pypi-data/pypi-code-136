################################################################################
# Environment
################################################################################
import platform
import sys
from enum import IntEnum
from pathlib import Path

from pydantic import BaseSettings

ROOT_DIR = Path(__file__).parent.parent.absolute()


class Os(IntEnum):
    WIN = 1
    MAC = 2
    LINUX = 3


plt = platform.system()
if plt == "Windows":
    OS = Os.WIN
elif plt == "Linux":
    OS = Os.LINUX
elif plt == "Darwin":
    OS = Os.MAC
else:
    print("Unidentified system")
    sys.exit(1)


class Environment(BaseSettings):
    os: Os = OS
    log_level: str = "INFO"
    twbm_db_url: str = "sqlite:///db/bm.db"

    @property
    def dbfile(self):
        return f"{self.twbm_db_url.split('sqlite:///')[-1]}"


config = Environment()
_ = None
